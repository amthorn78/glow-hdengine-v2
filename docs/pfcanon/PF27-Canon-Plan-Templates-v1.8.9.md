# Document Control

## **Header**

**Title:** PF27-Canon-Plan-Templates

**Version:** v1.8.9

**Status:** Canon

**Effective date:** 2026-06-15

**Last Update Gate:** BN 11.4.4 A13-14

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
* `command_provenance`: a short truthful source string for how the exact `command` string was obtained. Use `Codex prompt`, `Copy/paste from plan`, or `Explicitly created` when one source fully explains the command. When the executed command materially combines the approved plan command with a bounded canon-backed correction, syntax correction, or preflight, record the sources in one composite string. Allowed examples include `Plan + PF10 dependency preflight`, `Plan + QA syntax correction`, and `Plan + QA syntax correction + dependency preflight` when each component is evidenced.  
* **QA-correctable command syntax defects:** a local syntax, quoting, escaping, punctuation, or rendered-markup defect in an approved command is non-blocking only when the command identity, proof target, artifact family, PASS/FAIL predicate, and intended evidence output remain unchanged; the correction is made only at execution time; and the primary log records the exact executed command, the correction class, and `command_provenance` such as `Plan + QA syntax correction`.  
* `exit_code`: integer exit code for the executed `command` sequence. When an executed check is recorded as `PASS`, `exit_code` MUST be `0`. A PASS step MUST NOT rely only on file presence or the absence of a sentinel string.  
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
* `EXIT_CODE`  
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
 `exit_code_raw = env("EXIT_CODE", "")`  
 `exit_code = int(exit_code_raw) if exit_code_raw != "" else None`  
 `if status == "PASS" and exit_code != 0:`  
 `raise SystemExit("PASS requires EXIT_CODE=0")`  
 `commands = env_json("COMMANDS_JSON", [])`  
 `if isinstance(commands, str):`  
 `commands = [commands]`  
 `command = "; ".join(commands) if commands else "N/A"`  
 `` `header = {` ` "schema_version": schema_version,` ` "timestamp_utc": timestamp_utc,` ` "check_id": env("CHECK_ID"),` ` "check_name": env("CHECK_NAME"),` ` "status": status,` ` "fail_status": fail_status,` ` "command": command,` ` "command_provenance": env("COMMAND_PROVENANCE", "Explicitly created"),` ` "exit_code": exit_code,` ` "evidence_artifacts": env_json("ARTIFACTS_JSON", []),` ` "captured_env": {` ` "SAFE_MODE": env("SAFE_MODE"),` ` "ALLOW_NETWORK": env("ALLOW_NETWORK"),` ` "APP_ENV": env("APP_ENV"),` ` "LC_ALL": env("LC_ALL"),` ` "LANG": env("LANG"),` ` "TZ": env("TZ"),` ` },` ` "pf_refs": env_json("PF_REFS_JSON", []),` ` "intended_tokens": env_json("INTENDED_TOKENS_JSON", []),` ` "claimed_tokens": env_json("CLAIMED_TOKENS_JSON", []),` `}` ``  
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

Bounded step-level rerun posture (required when a plan permits one):

* The plan MUST state the exact trigger condition for the rerun and the exact check or checks that may be rerun.  
* The plan MUST state whether rails may change for the rerun and, if so, the exact replacement rails posture for that rerun only.  
* The rerun MUST stay on the same governed step root and the same deliverable family unless the plan explicitly states a narrower reporting-state-only rerun under that same step root.  
* The plan MUST preserve the earlier failed or blocked state in the same governed evidence stream and MUST require a short remediation note that records what changed and why.  
* Missing or overwritten initial failure artifacts (required). If an initial failure artifact, log, hash, timestamp, or result body is overwritten or unavailable by the time remediation begins, the plan, report, or review MUST state that the initial failure artifact is unavailable and MUST NOT reconstruct or invent the missing bytes. The remediation record may rely only on preserved failure signatures, approved sources, current evidence, and a truthful unavailability note.  
* The plan MUST require the rerun evidence to show the final step outcome without widening scope into new acceptance surfaces, new feature work, or a new evidence family.  
* Step-0B precondition remediation (required when applicable). If a later check cannot be interpreted because the required Step-0B doc-delta capture is absent at run time, the plan or review MAY accept an approved precondition remediation only when it runs the approved Step-0B commands, produces the required Step-0B artifacts under the established meta and doc-delta surfaces, reruns the affected check under the approved rails, preserves the earlier blocked or failed state, and records the remediation as an accepted PASS-only deviation. This does not change the affected check’s required deliverables or PASS/FAIL criteria.  
* QA-created harness predicate, evidence-assembly, or proof-metadata defects may be accepted as PASS-only Moon Loop deviations when the product or runtime proof target remains unchanged, the correction stays inside already-scoped QA evidence or harness files, the failure signature is preserved, the remediation note names changed paths and why, rerun PASS is captured in the same evidence stream, and patch or changed-files evidence with hashes is recorded when repo files change. Classify the original defect as planning, harness, or evidence-posture failure, not product behavior failure, when unchanged generator, runtime, or redaction evidence already proved the product predicate.  
* If an executed Moon Loop is broader than a narrow plan example but still remains minimal, auditable, within approved check scope, and does not add new acceptance surfaces, feature work, evidence family, token, or public contract, the review may accept it as a caveat or PASS-only deviation. The review must state why the deviation remained acceptable and must not hide it under PASS.  
* Live QA Moon Loop route boundary (required). Moon Loop correction may repair QA-created evidence-harness, header, manifest, path-proof, doc-delta, or QA evidence assembly defects only when the changed files remain under the approved QA root and do not change product behavior, repo evidence-generator behavior, governed artifact behavior, public contracts, PF documents, acceptance tokens, or multiple implementation subsystems.  
* Non-QA-root remediation route (required). A change to product code, repo tests, repo evidence generators, governed artifacts outside the QA root, public contracts, PF documents, acceptance tokens, or multiple implementation subsystems is remediation work, not Moon Loop correction. It MUST be routed through an approved work item type such as PR, OPS, QA\_PLAN\_UPDATE, or DOC\_UPDATE before it can be treated as the basis for a final PASS-grade QA run. Later QA review MUST cite that routing before accepting the final PASS state. When final PASS relies on non-QA-root governed evidence refresh, the final receipt or review MUST cite the routing receipt, identify the pre-routing failed or blocked receipt when one exists, preserve that pre-routing receipt as context, and distinguish routing proof from PASS proof.

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
* If the equivalent artifact is the current PF10-supported or repo-proven implemented artifact for the same proof goal, the stale planned filename is a planning failure and CAVEAT, not a blocker, only when the actual artifact is present, the PASS/FAIL predicate can be evaluated from it, no new evidence root or artifact family is introduced, and the deviation is recorded with expected-to-actual filenames.  
* If a plan-listed mismatch is wording-only inside the same check (for example, a PASS/FAIL bullet names a different target than the check title, intent, or inputs) but the intended target remains unambiguous and the evidence proves that intended target, treat it as a **CAVEAT** (not a **BLOCKER**). Record expected → actual wording and do not silently rewrite the predicate after execution.  
* If a plan action line or suggested inspection key conflicts with the plan’s own required deliverable list, but the required deliverable path is present, the check-root or governed-path posture is satisfied, and the intended PASS/FAIL predicate is proven from current evidence, treat the conflicting action line or key name as a planning failure and CAVEAT, not a blocker. Record expected-to-actual path or key posture, cite the evidence that proves the required deliverable or broader predicate, and use `Drives decision: No` when the mismatch does not affect the verdict.  
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

**PO-005 governed Reader proof-surface designation (temporary addenda-driven clarification)**

* Review precedence for this check while the relevant PF10 clarification is live: apply the live PF10 clarification first and the other owning PF homes second for this specific ambiguity.  
* While the relevant PF10 clarification is live, `/reader` is the governed Reader success-proof surface for the current closure scope addressed by PO-005.  
* `docs/ENDPOINTS_CATALOG.json` remains the single canonical machine-readable endpoint inventory.  
* If the current inventory or readout lacks an explicit governed designation for `/reader`, but the approved PO-005 evidence family proves route existence, env-gate posture, and A7 eligibility, treat that gap as canon drift to be drained, not as a reason to keep PO-005 blocked or to invent a second proof-surface carrier.  
* Use the existing approved PO-005 evidence family and keep the existing PASS, FAIL, and BLOCKED posture. Do not create a new QA step or a new evidence family to resolve this clarification.  
* This clarification does not authorize a new route, a new flag, a new proof-surface carrier invented at execution time, a second designation mechanism, or widening into writer work.  
* Downstream canon-alignment drains remain required for permanent alignment, but they are not a prerequisite for PO-005 PASS while this clarification is live.

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

**Proof-class and controlled vendor-smoke boundary (required when applicable)**

* If a check or remediation depends on no-user, vendor-backed, or externally observed behavior, the plan MUST label the proof class being claimed and MUST NOT substitute local pytest, grep, fixture-only metadata injection, public numeric-free output proof, or internal compute proof for the vendor-backed behavior proof unless the approved claim is limited to that proof class.  
* A no-user or birth-only proof claim MUST state the allowed caller or command inputs and the forbidden caller or command inputs. If the claim is birth-only, the proof must show birth data inputs and must prohibit app user IDs, `user_id`, caller-provided `person_uid`, DB-backed user BodyGraphs as caller input, and any inline secret value unless an owning canon section explicitly permits a narrower exception.  
* Fixture-only metadata injection is not sufficient for no-user proof when the claim is caller-facing or vendor-backed no-user behavior. Local pytest, grep, and internal compute proof may prove only the proof class they actually exercise.  
* Boundary-generated internal metadata may be valid only when it is created inside the resolver or compute boundary, stays internal, is not supplied by the caller, is not added as a public route contract requirement, and is stated explicitly as internal metadata rather than caller identity input.  
* Controlled vendor or external smoke steps are PO-only and IA-guided. They may run only after the plan proves exact command, approved target classification or explicit PF07-gap blocker posture, safe secret posture, no-user or other required input shape, and explicit vendor or external source posture.  
* The plan MUST prohibit guessed commands, hosts, ports, URLs, service bindings, target facts, environment facts, substituted birth values, and forced PASS edits.  
* If exact command, credentials, target facts, required source posture, or required input shape are missing, classify as `TOOLING_BLOCKED`, not `FAIL_BEHAVIOR`. If secret-bearing output is persisted, or a forbidden user identity input is used in the command or evidence, classify as `FAIL_TOOLING`. If all prerequisites are proven and runtime output contradicts the expected behavior, classify as `FAIL_BEHAVIOR`.  
* The step MUST record non-claims explicitly when the evidence is implementation validation only, including whether it does not claim QA PASS, Live QA completion, PF09 status change, epic closure, new public route, new public flag, new acceptance token, or PF document edit.

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

Dependency posture (required for executable checks):

* **Dependencies required:** exact commands, interpreters, modules, virtual-environment state, helper binaries, or other executable prerequisites this check depends on.  
* **Preflight command(s):** one or more explicit readiness checks that run before behavior evaluation.  
* **Activation or installation remediation, if allowed in the execution venue:** exact action to take when a required dependency is missing or not runnable.  
* **If remediation is not allowed or not known:** state that explicitly and classify the step as `FAIL_TOOLING` or `TOOLING_BLOCKED` if readiness cannot be established.  
* **Per-step enforcement:** each executable check must include its own dependency posture, or must explicitly depend on a bootstrap step and rerun a short step-local readiness check before the main behavior command.  
* **Dependency evidence:** the preflight result, any activation or installation action taken, and the final ready or not-ready outcome must be captured in the step’s governed evidence stream.

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

Structural governed-field predicate rule:

* When a Live QA check, remediation plan, or review depends on the presence, shape, or semantics of a field in a governed JSON artifact, the PASS predicate MUST state the structural requirement and the source relationship the field must prove. Raw string presence, grep-only visibility, or detached generator-only text is not sufficient when the field must be semantically tied to another source such as observed attempts, provider order, canonical rows, or evidence-index entries.  
* If the structural predicate is not met, classify the issue using the approved PASS/FAIL map and route the fix through the correct work type. A plan, remediation, or review MUST NOT create a new acceptance-token claim from a structural evidence field unless Governance or live PF10 explicitly mints that token.

Governed prose proof-string rule:

* When a Live QA check, remediation plan, review, or closeout artifact uses string matching against governed prose to prove a boundary, non-claim, or scope exclusion, the PASS/FAIL predicate MUST state the semantic proof target, the governed artifact being read, and whether exact literal matching, case-insensitive matching, regex-normalized matching, or machine-readable field proof is required.  
* Casing-only, punctuation-only, or prose-format mismatch against the intended governed text MUST NOT be treated as final `FAIL_BEHAVIOR` until the raw artifact and intended semantic proof target are reviewed. If the governed artifact carries the intended meaning and the proof target remains unchanged, classify the problem as planning failure, QA evidence-harness defect, or caveat according to the approved PASS/FAIL map.  
* A bounded QA-root Moon Loop may normalize case-sensitive or brittle prose checks only when the original failed receipt is preserved, the remediation stays inside the approved QA root, the same proof target is preserved, no new token or acceptance claim is introduced, and the accepted remediation receipt records the final PASS basis.

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

Supplementary captures and stream-silent command logs (required when applicable):

* If a check-scoped file is not part of the stated PASS or FAIL predicates, the plan MUST label it as supplementary and non-gating.  
* A present-but-empty supplementary capture is non-blocking when the stated PASS or FAIL predicates are satisfied by the required rc and required evidence artifacts.  
* If the plan requires a governed output log for a command that may succeed with no stdout or stderr, the plan MUST define the approved non-empty capture rule for that log and MUST keep the rc artifact authoritative.  
* The approved capture rule MUST state the exact text to be written when no stdout or stderr is produced and MUST keep that log under the same governed step root and deliverable family.

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
* states whether any undrained documentation delta remains and, if so, records it as follow-up work rather than as a close blocker when required QA evidence is complete and trustworthy and all required QA tasks are complete.  
* states that documentation drainage itself is not an allowed blocker for step verdicts, epic QA closeout review, or the readiness / closeout recommendation.  
* limits blocker posture to incomplete required QA steps, missing required deliverables, untrusted or non-governed evidence, unresolved FAIL\_BEHAVIOR / FAIL\_TOOLING / TOOLING\_BLOCKED conditions that affect acceptance, or missing required close-gate QA artifacts.  
* when documentation mismatches are found during QA or closeout, records them as doc-delta or follow-up items and names the intended drain targets by title rather than treating the undrained destination document as the blocker.  
* if the summary relies on undrained truth carried in the current epic-specific source of truth, it MUST say so explicitly and keep the caveat visible.  
* when the summary evaluates completion, it MUST keep repo-supported completion, canon-drain completion, and formal close-pack completion as separate states. Repo-supported completion is evaluated from implementation proof and Live QA logs; canon-drain completion is a no-claim state until drained into the owning PF home; formal close-pack completion is a no-claim state until the close-pack artifacts exist at the canonical paths with required sibling proofs and bindings.

Location:

* MAY live as a section of the epic close report, or a governed artifact referenced by it.

---

## **Review guardrails**

### **Hard blockers for plan approval/execution**

* All inputs, loci, and paths MUST be explicit and reproducible. Any required executable locus (script, check entrypoint, endpoint/route, or command) that is not canon-defined or audit-proven is blocked. No fabricated loci.  
* PF09 phased-reference rule (required). Plans, reviews, and future work MUST cite the relevant phased HDE Build Checklist document or documents, using PF09.1 through PF09.7 as applicable, and MUST NOT rely on a retired single-document PF09 surface.  
* PF07-derived / PF07-gap infrastructure posture (required). Any plan, implementation guide, QA plan, review artifact, remediation guide, runbook, or epic document that includes an infra task, ops task, environment binding, service binding, URL, port, project name, provider name, config key, QA root, or start-command dependency MUST use exactly one of these postures:  
  * PF09 phased-reference rule (required). Plans, reviews, and future work MUST cite the relevant phased HDE Build Checklist document or documents, using PF09.1 through PF09.7 as applicable, and MUST NOT rely on a retired single-document PF09 surface.  
  * PF07-derived / PF07-gap infrastructure posture (required). Any plan, implementation guide, QA plan, review artifact, remediation guide, runbook, or epic document that includes an infra task, ops task, environment binding, service binding, URL, port, project name, provider name, config key, QA root, or start-command dependency MUST use exactly one of these postures:  
* Placeholder external-ownership language is non-conforming. Plans and related documents MUST NOT use phrases such as “infra to provide”, “ops to confirm”, “ask infra”, “await ops details”, guessed hostnames, guessed ports, guessed URLs, guessed start commands, guessed environment bindings, or placeholder external ownership without a concrete PF07-backed value or an explicit PF07-gap statement.  
* QA plans and Live QA runbooks MUST NOT guess or redefine environment bindings that PF07 is meant to own. This includes, as applicable, `DEV_SAMPLER_URL`, `HDE_BASE_URL`, `DATABASE_URL`, `DB_BRIDGE_URL`, production service base URLs, environment-specific host and port bindings, and canonical QA-root patterns.  
* Default documented dev and QA access address (required). When a plan, implementation plan, QA plan, remediation guide, review, runbook, example command, or inline documentation needs to show a non-prod local-style client access address, it MUST use `127.0.0.1` as the default host, plus the correct port and endpoint path.  
* This default does not replace canonical config keys, infra wiring, or per-environment configuration. It is a documented client access convention only.  
* `127.0.0.1` in these templates is not a service identity claim and not a server bind requirement. Real provider, project, service, base URL, and config-key identity remain governed elsewhere, and services may still bind to `0.0.0.0`, `$PORT`, or another infra-owned target when that is the correct runtime posture.  
* When a QA console or runbook targets a real production service, that surface MUST be documented with the real production address even if the operator is in Codespaces, CI, or another remote shell.  
* Production and other prod-facing surfaces MUST keep the real hosted service URL or other real infrastructure address. Do not rewrite prod-facing targets to `127.0.0.1`.  
* `localhost` is not the preferred canonical example host for new or revised dev and QA documentation in these templates.  
* If a dev or QA surface cannot truly be reached at `127.0.0.1` from the intended operator context, the document MUST state an explicit exception and the real access route. Do not guess hostnames, forwarded URLs, ports, config keys, start commands, or endpoints.  
* Markdown-only wrapper differences in planning and review artifacts are non-blocking when the same required field name, content, ordering or adjacency, and meaning remain present, and no executable command, code, schema, JSON, token spelling, path string, endpoint string, or other machine-sensitive literal is altered. Reviewers may note those differences as optional cleanup only.  
* Markup that changes meaning, hides required text, or alters machine-sensitive content remains blocking.  
* Approval-submitted planning artifacts MUST include the literal approval sentinel `ASK OK?`. The sentinel is required and non-blocking by default, and reviewers MUST NOT classify it as stray text, formatting noise, or a blocker merely because it appears in the document. Missing the required sentinel remains blocking.  
* The plan sentinel `ASK OK?` is distinct from a reviewer final decision line such as `ASK OK`; do not conflate those surfaces.  
* Structural template completeness is gating. Missing required sections or required structural blocks (including required end markers and required gates) is blocking. Where a template requires canon pointers (for example PF09 or PF14 pointers), missing pointers are blocking. Invalid non-PF references and ungrounded existence claims are blocking.  
* Plans MAY consult PF documents during planning and review, and MAY note drain targets or doc-delta candidates as explicitly non-mandatory follow-up intents for PO, but PF10 drainage and any other PF-canon drainage are never execution conditions, approval conditions, completion conditions, required deliverables, required checks, acceptance criteria, or blockers for the current plan, review, QA step, OPS task, or closeout artifact. Reality Audits updates are PO-only.  
* PR-slice completion discipline (required). When a plan, remediation guide, or review record claims that a PR slice or remediation lane is complete or acceptable, it MUST account for every assigned HDE Build Checklist subtask. If one or more assigned subtasks are not complete, the document MUST identify each affected subtask ID, state exactly what was completed, state exactly what remains incomplete, describe the blocking condition or limiting constraint, explain why completion was not possible within the approved scope, and name the repo evidence, test result, or other concrete basis for that conclusion. Silent omission, partial completion without this explanation, or claiming completion while assigned subtasks remain unresolved is non-conforming.  
* Review and closure posture for mapped PF09 work (required). Current PF09 recorded status text is not a pre-drain acceptability gate, closure gate, QA-entry gate, or OPS acceptability gate. When a plan, remediation guide, QA-readiness review, closeout review, or approval artifact evaluates mapped PF09.x work, the controlling question is whether the mapped work is complete in substance from approved implementation state, approved OPS state where applicable, governed evidence, and truthful review artifacts, plus PF10 live truth where PF10 explicitly speaks.  
* Combined-evidence supportability decisions (required). When live PF10 records that individually accepted PR or OPS slices intentionally did not move a mapped PF09.x row, a later plan, review, QA-readiness artifact, closeout artifact, or approval artifact may rely on a PF10-recorded combined-evidence supportability decision only if it identifies the exact slices combined, the mapped PF09.x row or subtask, the row’s substantive proof burden, the slice-local no-move conditions, what each slice proves, and the live PF10 conclusion. Prior slice-local no-status-move language must be preserved as slice-local truth, not treated as a prohibition against a later combined-evidence supportability decision.  
* Combined-evidence non-claim boundary (required). A combined-evidence supportability decision MUST state what it does not claim, including whether PF09.x has already been drained, QA has passed, the epic is closed, live vendor behavior has been proven, vendor-version runtime conformance has been completed, unregistered proof labels have become acceptance tokens, OPS evidence has become QA evidence, or any individual PR or OPS slice alone moves PF09.x status.  
* Exact mapping control (required). If a slice maps to an exact PF09.x subtask, that subtask is the controlling unit. If a slice claims to close more than one mapped PF09.x subtask, each claimed subtask must be complete in substance before acceptable-status language is allowed.  
* PF10 reopened-subtask planning rule (required). When current PF10 explicitly reopens, rebinds, or names active HDE Build Checklist subtasks for an epic, Epic Plans, QA Plans, remediation guides, and reviews MUST treat the exact subtask IDs as active scope unless a later PF10 addendum reverses that posture. Broader parent-task history-only wording MUST NOT suppress an exact subtask row that PF10 names as active.  
* Truth constraint for reopened scope (required). A reopened or rebound subtask is not automatically complete. Plans and reviews MUST preserve the current truth of its status and MUST NOT claim runtime facts are already true merely because the row is in scope. If active-scope and current-status text conflict, record the issue as a PF09.x doc-delta candidate or later-drain item rather than deferring the subtask by assumption.  
* Reused-history separation rule (required). When a plan or review distinguishes reused-history rows from active epic rows, it MUST list those categories separately, state whether any new implementation is being claimed for reused-history rows, and treat a false new-implementation claim as part of the evidence posture rather than as active-scope completion.  
* Sufficiency rule (required). Green tests, bounded diff scope, passing evidence refresh, successful OPS execution, or review-clean artifact posture are necessary but not sufficient by themselves. They do not authorize acceptable-status language if the mapped work remains open in substance.  
* Review-language discipline (required). Before mapped work is complete in substance, allowed labels are: contributory, intermediate, review-clean, bounded, and `Supportable from repo evidence:`. Labels such as acceptable, accepted, satisfied, complete-for-close, and supportable for later drain to Done are reserved for reviews where the mapped work is complete in substance, the governed evidence proves that posture, and PF10 records that live truth where PF10 explicitly speaks.  
* Current PF09 recorded status may be cited only as canon-as-recorded, not as the live blocker source. Reviewers and approval artifacts MUST NOT block a slice solely because PF09 still says `Not done`, `Partial`, `Deferred`, or another pre-drain state.  
* Implementation-plan and QA-plan approval artifacts that are intended to feed later PF-canon drain MUST include an explicit later-drain PF-canon update statement naming the affected PF canon home(s), exact locator(s), supported later-drain action, and evidence basis.  
* Review-scope unit (required). Reviewers MUST review the approved PR or OPS task itself and its explicitly approved scope. They MUST NOT widen the review to later PRs, later OPS tasks, later validation runs, or whole-epic closure work unless the approved task explicitly includes them.  
* Non-closure task rule (required). If the approved task is explicitly validation-only, classification-only, evidence-only, sequencing-only, or another bounded non-closure step, PF09 closure is not a review gate for that task. The reviewer MUST judge whether the task truthfully and correctly completed its own approved job.  
* Boundary-preservation rule (required). For approved non-closure steps, reviewers MUST verify that the task stays within approved scope, does not overclaim closure, preserves any still-open PF09 or environment truth explicitly, and does not silently imply that later closure work is already complete.  
* Decision separation (required). Review and acceptance language MUST distinguish task-level acceptance of the approved step from PF09 closure status of the mapped row or subtask.  
* Governed evidence family coherence (required). When a review or closeout decision depends on governed evidence for a bounded task and a claimed closure dimension, the governed evidence family MUST express one authoritative posture only. Mixed-state families are invalid and mechanically block acceptance until normalized.  
* Evidence-family path collision repair (required). A review MUST treat evidence outputs that overwrite or collide with an existing governed evidence family as blocking until the collision is repaired. A repair is acceptable only when the task-specific evidence is moved to the approved PR/check/task-specific governed path, the overwritten shared or dependency artifacts are restored or refreshed, matching path proofs/index/mirror bindings are coherent, and the review records the collision and repair as evidence posture rather than silently accepting the overwritten state.  
* Evidence artifact-key collision repair (required). A review MUST treat an evidence-index or Machine Mirror key that can override, shadow, duplicate, or supersede the canonical artifact key for the same discovered physical path as blocking until corrected. A repair is acceptable only when the governed source row uses the canonical artifact key, stale duplicate keys or EPIC-specific keys are filtered or removed before dedupe and regeneration, Human Evidence Index and Machine Mirror are regenerated coherently, and the review records the collision and repair as evidence posture rather than silently accepting a duplicate-key state.  
* Contradictory-source consolidation is forbidden. A review, closeout, or consolidation artifact MUST NOT summarize or bind acceptance over source artifacts that still encode contradictory closure meanings for the same closure dimension. If contradiction exists, stop and classify the issue as a documentation/evidence failure rather than producing a merged authoritative summary.  
* Documentation/evidence normalization instead of rerun (required). If the runtime proof remains unchanged and the only defect is contradictory governed evidence or closure semantics, remediation may be a documentation/evidence normalization pass rather than a new runtime rerun only when the unchanged runtime facts are already evidenced, no new runtime or OPS claim is added, the affected governed family is refreshed to one authoritative posture in the same change, the Human Evidence Index, Machine Mirror, checksum sidecars, and required sibling path-proofs are refreshed coherently, and any prior contradictory bundle or report is explicitly treated as superseded evidence.  
* Bounded evidence-refresh side effects (required). Evidence-side churn outside the direct PR or task evidence family is non-blocking only when it remains within existing governed proof families, is caused by canonical evidence refresh, updater convergence, or required dependency refresh, adds no new runtime, route, serializer, public contract, token, or artifact-family claim, and the relevant index, mirror, path-proof, checksum, LF, schema, and orientation checks are coherent. The run or review evidence MUST name each affected family, classify each side effect as expected updater convergence, required dependency refresh, or unexpected drift, and identify any affected proof-companion paths plus corresponding Machine Mirror artifact keys or discovered paths when mirror rows move. A PASS or acceptance claim MUST fail closed unless the classified side-effect paths exist, proof companions validate against their targets, and affected mirror rows match artifact key, proof anchor, sha256, and size. The review MUST NOT use bounded side effects to claim unrelated PF09 status movement.  
* Unbounded evidence churn remains blocking when it creates a new evidence home, changes contract meaning, changes runtime behavior, lacks coherent proof companions, or is used to support an unapproved scope expansion.  
* Failure classification rule (required). Reviews that rely on governed evidence MUST distinguish runtime or implementation failure from documentation/evidence failure. Stable runtime facts plus contradictory governed artifacts are a documentation/evidence failure. Runtime wrongness remains a runtime or implementation failure.  
* Evidence-generator portability (required). When a plan, remediation guide, review, or closeout artifact relies on a repo-owned evidence generator as a governed proof command, the generator must be reviewable under a normal repo-root invocation or the artifact must explicitly classify the missing invocation support as tooling failure or tooling blocked. Plans and reviews MUST NOT treat caller-supplied `PYTHONPATH`, unstated local shell state, or other ad hoc environment setup as an acceptable substitute for a portable governed proof command unless the approved task explicitly defines that environment requirement and captures it in the step evidence.  
* Evidence-generator PASS binding (required). A governed evidence generator MUST NOT emit or support a `PASS` claim unless every decisive predicate for the claimed evidence family is evaluated against the current artifacts and passes. PASS status MUST be derived from current predicate checks, not from previous-artifact drift, stale local state, artifact presence, format-only checks, parsed-object equality where byte identity is required, digest-shape checks without recomputation, file presence alone, or absence of a sentinel string.  
* Evidence-generator currentness before index proof (required). When a plan, review, or closeout relies on generated evidence plus Human Evidence Index, Machine Mirror, checksum, orientation, path-proof, LF, schema, or updater checks, the artifact MUST show that the generator materialization command and generator check ran from the current logic path before evidence-index or mirror updater commands and their checks. Index, mirror, hash, path, orientation, LF, schema, or updater checks alone are not sufficient to prove generated evidence currentness when the generator itself was not invoked or checked in the governed run.  
* Source-backed inventory and closed-rails replay proof (required). When a plan, remediation guide, review, or closeout relies on a generated source inventory, contract inventory, endpoint reference, or contract map produced from cached or pre-captured public documentation, PASS requires proof that every decisive source row is backed by current cached body bytes or an approved authoritative machine-readable source plus checksum, status, and path binding. Metadata-only rows are not sufficient when source SHA, fetch status, tier, route, or contract content is decisive.  
* Quarantined suspect-source rule (required). A suspect or non-authoritative source may be absent, non-200, unavailable, or quarantined without blocking the generator only when validated authoritative sources remain sufficient to produce the promoted evidence, the quarantine posture is recorded in the governed artifacts, tests cover the non-blocking path, and the review does not claim runtime conformance from the quarantined source.  
* Generated-proof family completeness (required). When a check claims that generated proof families fail closed, PASS requires explicit fail-closed proof for every generated proof family used by the epic. If any such family is not proven, the step MUST remain TOOLING\_BLOCKED until the missing coverage is added and the final suite is rerun from the updated proof path.  
* Final generator logic rule (required). After evidence-generator logic changes, final governed artifacts, sibling path-proofs, Human Evidence Index entries, Machine Mirror rows, checksum sidecars, and any required targeted tests MUST be regenerated or rerun from the final logic path before a review, closeout, or later-drain recommendation may rely on them. A stale artifact produced by earlier generator logic is not sufficient proof after remediation.  
* Evidence-generator check-mode binding (required). When a governed evidence generator produces or registers its own artifacts, non-check generation may avoid write-time self-hash recursion only for the materialization step. Check mode MUST validate the final committed or current Machine Mirror sha256 and size bindings for every row the generator claims or depends on, including self-generated rows and any classified side-effect rows.  
* Evidence-generator remediation scope boundary (required). Fixing generator PASS binding, current-predicate evaluation, or final-artifact regeneration does not by itself mint an acceptance token, create a new gate, require an OPS task, authorize a public-surface change, or require a blanket audit of adjacent generators. If any of those actions are needed, they must be approved and routed independently.  
* PF-Canon non-edit discipline (required). Coding and implementation agents MUST NOT directly modify PF-Canon documents as part of implementation PR work, including checklist-status canon such as HDE Build Checklist. If implementation work reveals canon drift, missing canon coverage, or supportable checklist or canon status changes, the plan or review MUST record that as a drift note or doc-delta candidate and MUST route PF-Canon changes as follow-on canon maintenance rather than direct implementation-lane edits.  
* How plans MUST express reality or existence confirmation: cite a PF clause (titles-only) when PF already establishes the claim, or capture repo-local evidence for the current run under `audit/` when PF is silent. Do not treat an intended PF update as substitute evidence.  
* AI review and plan-analysis workflow (required). AI agents reviewing plans, remediation guides, QA plans, repo audits, closeout artifacts, or related review documents MUST use a retrieval-first, proof-first workflow: use PF10 where it explicitly speaks first, then read the current artifact under review end-to-end, then retrieve the owning PF canon home for each specific issue, then gather repo-reality proof for any claimed path, command, endpoint, environment variable, test ID, artifact path, or component home.  
* Tool order for repo-reality proof (required). Use `file_search` or full-source retrieval first for uploaded documents and PF documents. When repo reality matters, run minimal inventory proof next. For known literals, use exact-string repo search before regex or broad exploratory search, including task IDs, subtask IDs, token names, headings, route strings, command strings, filenames, artifact keys, environment variable names, and other exact literals. Regex search is allowed only when exact-string search cannot prove or disprove the claim. Broader semantic or exploratory search is allowed only after exact search fails.  
* Proof classification (required). Review findings MUST distinguish canon requirement, observed repo reality, and inference. Any unproven locus, path, route, command, flag, token spelling, or environment variable name remains `UNKNOWN` or `BLOCKED`. Do not guess it into existence. Do not rely on truncated viewer snippets, omission markers, or partial excerpts as proof; reopen the full source first.  
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

Materiality-based blocker discipline (required for Epic Plan and Implementation Plan review):

* A planning artifact MUST NOT be blocked solely for template hygiene, formatting, inventory completeness, provenance-label phrasing, quote-block style, table formatting, heading style, punctuation, spacing, bold markers, presentation style, inventory-row ordering, template-perfect phrasing, missing non-decisive locator precision, missing titles-only polish, or an Epic QA root omission in an Epic Plan that does not authorize QA execution, unless the defect materially changes truth, proof, acceptance, execution safety, source authority, portability, implementation scope, PF09.x completion mapping, evidence identity, evidence trust, OPS/PR boundary, public/private surface posture, canon conflict handling, or closeout truth.  
* Review severity MUST map to material effect: Blocker changes truth, proof, acceptance, execution, source authority, or portability; Caveat creates a real risk with a safe default; Suggestion improves clarity, consistency, or maintainability; Nit is cosmetic, template-polish, or wording-level only.  
* Valid blocker framing must state the material harm, such as conflict with active PF10, an unresolved ADR after PF10 resolves the exact topic, a required external CA/audit/non-PF source for Codex execution, unregistered token claimed as an acceptance token, Already Implemented claimed without embedded proof, OPS work required inside Codex PR work, unproven repo locus, public surface expansion without canon support, PF23 used as deliverable/token/blocker/acceptance authority, or PF20 used as current planning authority.  
* Invalid blocker framing includes a missing token row when the plan does not overclaim a token and the evidence family is scoped, imperfect CA quote-block formatting when the fact is embedded and self-contained, provenance labels such as CA vetted when no external CA access is required, or section formatting that is not template-perfect but preserves meaning.

Live QA Plan approval materiality discipline (required):

* Live QA Plan approval is an operational-readiness review. A Live QA Plan should be approved when it is safe, self-contained, phase-bounded, and clear enough for the assigned operator to execute the QA run and produce a meaningful governed verdict.  
* A Live QA Plan MUST NOT be blocked solely for rendered escape characters, markdown or AI-rendered backslashes, heading style, bullet style, table style, quote-block formatting, code-block formatting, whitespace, punctuation, line wrapping, command syntax polish, command invocation style, interpreter choice unless it changes operational behavior, exact shell spelling, exact command ordering unless order is required for safety or proof, evidence-ledger byte-shape polish at plan approval, path-proof transcript field polish at plan approval, canonical JSON compactness wording at plan approval, or step-log header polish at plan approval.  
* Valid Live QA Plan approval blockers are operational: missing required QA step coverage, missing required deliverables or explicit PASS/FAIL criteria, unsafe rails, secret exposure, live-provider or external-action boundary violation, public/private surface boundary violation, token overclaim, non-token proof label treated as an acceptance token, PF23 used as an execution artifact, PF20 used as current authority, PF14 used as governance or acceptance authority, PF-canon drainage required as a gate, unproven required existing locus with no source-grounded proof, no discovery posture, and no QA-created fallback, wrong target execution, prohibited mutation, no governed evidence family, no decisive receipt, contradiction of active PF10, or contradiction of permanent PF-Canon where PF10 is silent and the contradiction affects operational truth.  
* Commands in a Live QA Plan are operational instructions rather than canon contracts unless the plan explicitly states exact invocation is required and the owning PF home requires exactness for the operational result. Exact-command mismatch is a Caveat, Suggestion, or execution note when check intent, proof target, rails posture, expected evidence family, PASS/FAIL predicate, operator safety boundary, and actual-command capture remain clear and an equivalent safe command can produce the same proof.  
* A Live QA Plan may create QA-only harness scaffolding during Step 0 when the harness is limited to QA evidence capture and does not create product behavior. Reviewers MUST NOT require repo-existence proof for a QA-created harness that the plan explicitly creates during the QA run. Formatting, indentation, line wrapping, and code style inside QA-created scaffolding are non-blocking unless they prevent creation or safe execution and no bounded correction is allowed during QA execution.  
* Live QA Plan approval requires evidence identity, not final closeout perfection. At approval time, the plan must identify what each check proves, what result counts as PASS, what result counts as FAIL, where the QA run records the decisive receipt, which evidence family or evidence class supports the verdict, and how token claims are avoided unless registered and in scope. Final byte-level details may still fail QA execution or closeout validation; they are approval blockers only when the plan lacks evidence identity, lacks a decisive receipt, relies on ungoverned evidence as decisive proof, or explicitly rejects required governed-evidence discipline.  
* Review severity for Live QA Plan approval MUST map to operational harm: Blocker prevents safe execution, invalidates the intended QA verdict, breaks source authority, creates token or acceptance overclaim, violates rails or secret posture, requires unavailable execution inputs, or makes required evidence untrustworthy; Caveat creates operational risk with a safe default, bounded discovery path, or equivalent execution path; Suggestion improves clarity, operator usability, reviewability, or future maintainability; Nit is cosmetic, formatting-level, or presentation-only.  
* A reviewer who returns a Live QA Plan for revision MUST state the concrete operational harm and show that the defect prevents safe execution, invalidates the QA verdict, breaks evidence trust, changes source authority, creates token overclaim, or violates rails or safety boundaries.

Plan command, syntax, and example-literalness approval rule (required):

* Plans are not execution artifacts. Plan approval evaluates truth, proof, scope, authority, safety, acceptance posture, phase fidelity, and evidence identity, not whether every command, snippet, helper, heredoc, shell line, or example is a literal runnable transcript.  
* QA Plans, Epic Plans, Implementation Plans, remediation plans, review prompts, redline prompts, Codex prompts, closure-review artifacts, and related approval artifacts MUST NOT be blocked, rejected, returned for revision, or classified as REVISE AND RESUBMIT solely because a command, code snippet, heredoc, shell line, helper function, example invocation, indentation block, markdown-rendered string, or escaped character is not paste-ready, literal, syntactically exact, or executable as written.  
* This rule applies even when the syntax issue appears in raw source text and even when the reviewer believes the command would fail if pasted directly. Command syntax, helper-code syntax, heredoc form, indentation, markdown escaping, escape characters, shell redirection syntax, interpreter invocation, code-block formatting, quote formatting, wrapping, whitespace, punctuation, copied command exactness, non-literal examples, assistant-introduced syntax artifacts, renderer-introduced syntax artifacts, and formatting introduced during review, redline, or paste workflows are not valid plan-approval blockers by themselves.  
* QA steps and plan commands do not need to be paste-ready, literal executable commands, final runnable syntax, or exact shell, Python, or tool syntax. They may express the intended proof action in operational language, pseudocode, structured prose, or approximate command form when the proof target, scope boundary, rails posture, evidence family, and verdict posture are clear enough for the assigned operator to execute safely and produce a governed verdict.  
* Syntax correction is ordinary execution hygiene. During execution, a QA operator, Codex, Kronos, PO, or implementation owner may normalize a non-runnable command, escaped string, indentation defect, heredoc issue, shell syntax issue, or helper-code formatting issue in flight when the same proof target, QA step identity, scope boundary, rails posture, evidence intent, acceptance posture, public/private boundary, no-secret posture, no-new-token posture, and no-new-scope posture are preserved.  
* In-flight syntax normalization does not require plan rejection, a remediation guide, a PF10 addendum, or a QA Plan revision unless the underlying proof target, scope, authority, acceptance posture, or evidence identity changes.  
* Valid plan approval blockers are limited to material truth, proof, scope, authority, safety, acceptance, phase, evidence-identity, or canon-conflict defects. Examples include missing proof obligation, missing in-scope PF09.x mapping, unverified acceptance-token claim, unauthorized scope expansion, unauthorized public Reader expansion, live-provider or external-action requirement inside closed rails, secret exposure requirement, OPS work assigned to Codex, QA execution required before QA begins, PF23 treated as acceptance proof, PF20 treated as current authority, non-token proof labels claimed as acceptance tokens, missing acceptance-decisive deliverable category, unclear PASS/FAIL or verdict posture, unresolved phase boundary conflict, unresolved canon contradiction, or an evidence identity gap where the proof target cannot be distinguished.  
* A reviewer must not disguise command syntax, paste-readiness, escaping, or formatting complaints as truth/proof blockers. If the reviewer’s objection can be fixed by editing command syntax, escaping, indentation, heredoc form, shell syntax, or helper-code formatting without changing the proof target, it is not a blocker.  
* For any plan artifact, command or syntax concerns may be classified only as Non-issue, Note, In-flight normalization, or Operator caution. They MUST NOT be classified as Blocker, Approval blocker, QA readiness blocker, Implementation readiness blocker, Closure blocker, FAIL\_BEHAVIOR, FAIL\_TOOLING, TOOLING\_BLOCKED, acceptance failure, path-proof failure, evidence failure, token failure, PF locator failure, or command validity failure requiring plan revision.  
* Future plan-review, QA Plan review, implementation-plan review, remediation-plan review, redline-generation, QA-readiness review, closure-review, and Codex-audit prompts should include this guard: plan commands, snippets, helper code, heredocs, shell lines, and examples do not need to be paste-ready or literal. Syntax defects, escape characters, markdown rendering artifacts, indentation issues, and command exactness must never block plan approval. Treat them only as in-flight normalization unless they reveal a separate non-syntax truth, proof, scope, authority, safety, acceptance, phase, or evidence-identity defect.

Explicit non-blockers (do not gate approval):

* Review gates are about execution safety, evidence posture, canon alignment, and mechanical paste safety. Reviewers MUST NOT gate approval on Markdown rendering choices or other presentation-only formatting.  
* Review gates are about execution safety, evidence posture, canon alignment, and mechanical paste safety. Reviewers MUST NOT gate approval on Markdown rendering choices or other presentation-only formatting.

* Template adherence is structural only. Reviewers evaluate whether required sections and required structural blocks are present. Header styling, heading levels, and indentation are not part of structural adherence.

* Header-format-only redlines are nits and MUST NOT be requested as approval conditions, including changes that only:  
  * switch between bold labels and Markdown headings  
  * adjust heading levels or heading capitalization  
  * restyle bullets or numbering  
  * change indentation, spacing, or cosmetic line wrapping

* Command syntax latitude and QA-correctable defects: approval binds to command identity, target proof output, repo-locus proof, and bounded PASS/FAIL semantics, not exact shell or Python syntax perfection at plan-review time. A syntax, quoting, escaping, punctuation, rendered-markup, or small local expression defect is non-blocking when the command identity, target check, artifact, route, path, evidence family, and intended PASS / FAIL / TOOLING classification remain clear; the QA executor can correct it locally without inventing a new repo locus, command source, route, artifact family, acceptance predicate, or PASS/FAIL criterion; and the exact corrected command is captured in governed step evidence. This latitude MUST NOT be used to accept invented commands, unproven loci, ambiguous command identity, wrong artifacts, wrong routes, changed acceptance semantics, or defects in code, canonical JSON, schemas, acceptance maps, token registries, machine-readable manifests, or executed command transcripts.

* Command syntax latitude: approval binds to command identity and bounded proof outputs, not to exact shell syntax. JSON-carrying environment variable assignments are treated as intent carriers; do not reject solely on whitespace or quoting style. Plans MAY define plan-level Command Snippets once and reference them by local IDs, provided each executed step log records the resolved command. This latitude MUST NOT be used to accept invented commands or unproven loci.

* Markdown sanitation rule (analysis-only): when quoting a plan for review notes, remove only presentation escapes that exist solely for Markdown rendering. Do not remove semantic escapes used by shell, JSON, regex, or paths, and do not rewrite commands based on sanitized excerpts.

* Optional environment snapshots may be omitted if the plan otherwise references stable loci.

* Minor formatting artifacts are non-blocking if semantic meaning is preserved, and must be treated as nits (they must not change the binary approval outcome). Examples include escaped Markdown list markers, backslashes inserted for rendering, cosmetic whitespace differences, bold/italic marker differences, and bullet style differences. If formatting changes meaning or introduces ambiguity (commands, expected outputs, file paths, loci, artifact names, evidence roots, portability constraints, required structural markers, quoted carryover blocks), it is not minor and may be gating.

* Rendered escape artifacts in source-facing work are categorically non-blocking (required). A plan, guide, QA plan, Live QA Plan, implementation plan, remediation guide, Codex prompt, review artifact, redline pass, PF10 addendum draft, PF-facing artifact, or acceptance artifact MUST NOT be blocked because assistant-rendered, Markdown-rendered, transcript-formatted, quote-formatted, preview-pane, copied-chat, or review-prose output shows escape characters in otherwise clear machine-sensitive strings. This applies to repo paths, artifact paths, evidence paths, command names, command arguments, shell redirection markers, heredoc markers, module names, endpoint paths, route strings, token names, environment variable names, config keys, JSON keys, artifact keys, PF09 task IDs or subtask IDs, ADR IDs, headings used as locators, evidence filenames, manifest filenames, path-proof filenames, hash filenames, quoted source lines, plan snippets, and QA-created script bodies.  
* Source-level verification requirement (required). A rendered escape character is never evidence of a source defect. Before treating an escape-character issue as a defect, the reviewer must inspect the raw/source artifact by direct file view, read-only command, uploaded source inspection, actual pasted document text after paste, or governed artifact/index/mirror/path-proof source. A blocker may be raised only when the raw/source artifact itself contains the unwanted character and the character changes executable, governed, canonical, or semantic identity.  
* Quote, redline, and placement posture (required). Redline placement quotes, PF proof quotes, Doc A or Doc B quotes, IG Approved or CA vetted quote blocks, and quote-verbatim checks MUST be evaluated against raw source text. If the only difference is assistant-rendered or markdown-rendered escaping, the quote is source-equivalent and MUST NOT be blocked. Redline authors MUST NOT draft corrective redlines solely to remove display-layer escapes; such a redline is allowed only when the raw target document or raw governed artifact actually contains the unwanted character.  
* Codex prompt posture (required). Codex prompts MUST treat escaped display text as non-authoritative unless it is inside a raw source file Codex opens. A prompt MUST NOT instruct Codex to create, check, rename, implement, remediate, or fix escaped paths or filenames derived from assistant rendering unless raw source contains the escape and the approved plan explicitly directs the correction.  
* Burden of proof and classification (required). The burden of proof is on the reviewer or agent raising the escape issue. A valid blocker must name the raw/source file or artifact inspected, the read-only command or source-view method used, the raw line showing the unwanted character, why it changes executable/governed/canonical/semantic identity, and why it is not merely assistant or markdown rendering. Without that proof, classify the issue as a display-layer artifact and withdraw the blocker. Rendered escapes MUST NOT be classified as FAIL\_BEHAVIOR, FAIL\_TOOLING, TOOLING\_BLOCKED, acceptance failure, path-proof failure, canonical path failure, token spelling failure, quote-verbatim failure, PF locator failure, implementation blocker, closeout blocker, or remediation requirement.  
* Current-loop and future-prompt posture (required). Any existing blocker based solely on rendered escape characters is invalid unless re-proven from raw/source artifact text. Future review, redline, plan-revision, QA-review, remediation-review, and Codex-audit prompts should include a rendering-artifact guard that tells reviewers to ignore display-layer escapes unless raw/source inspection proves a substantive source defect.  
* Headings and levels need not match a reviewer’s preferences; only required headings and required template blocks are gating.

* A plan MAY cite upstream scripts or previously-approved plan steps (for example, reused remediation steps), provided it cites exact repo paths and captures the necessary evidence outputs under `audit/`.

* Reviewers MUST NOT request changes solely to make a plan easier for LLM parsing. If a change is requested, it must be justified by execution safety, evidence posture, canon alignment, or mechanical paste safety requirements, and should be the smallest viable edit.  
* Negative audit proof and no-hit proof are non-blocking when the approved proof target is to show absence of a condition, no matching drift, no forbidden string, or no relevant hit. Reviewers MUST evaluate whether the negative proof was produced from the approved scope, search method, and evidence target; they MUST NOT require a rerun or fallback positive proof solely because the result is negative.

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

#### **Redline bundle construction discipline (required for editorial redline sets)**

Applies when a plan review, remediation review, audit review, or doc-drain task emits editorial redlines.

Rules:

* Original-document anchor space only. All placement anchors in one redline bundle MUST be resolved against the unchanged base document only. A later redline MUST NOT anchor against text that would exist only after an earlier redline is applied.

* Non-overlap invariant. No two redlines may target intersecting spans of the base document. No INSERT may land inside a span already covered by a REPLACE. No REPLACE may partially or fully cover a span already targeted by another REPLACE.

* One strategy per affected region. For any contiguous affected region, choose exactly one strategy: one consolidated REPLACE for the whole region, or multiple smaller redlines whose target spans are pairwise non-overlapping. Mixing both strategies within the same affected region is prohibited.

* Parent-child prohibition. If one redline REPLACEs a parent block, section, step block, heading block, list block, or other enclosing region, no later redline may target any line inside that parent region. All required child edits MUST be folded into the parent replacement.

* No second-pass layering. If additional fixes are discovered inside an already-targeted region, rebuild from the original base document and re-emit the affected region as one consolidated replacement or as a new non-overlapping set.

* Repeated-anchor safeguard. If a target line or boundary line is repeated in the base document, widen the target to the nearest unique enclosing heading or other unique boundary before emitting the redline. A repeated line MUST NOT be used as the only placement anchor.

* Coverage-before-emission rule. Before outputting redlines, map each required review item to the exact base-document target region that will implement it. The author MUST NOT discover scope incrementally while already emitting the redline bundle.

* Merge-on-conflict rule. If two or more required changes touch the same region, they MUST be merged into one consolidated redline. Sibling redlines that depend on one another’s output are prohibited.

* One-pass apply simulation required. Before output, the full bundle MUST be tested mentally or mechanically against the unchanged base document as a one-pass application set. A redline bundle is valid only if it can be applied once from the original base document without anchor collision, span overlap, parent-child nesting conflict, or re-anchoring later redlines after earlier edits.

* Mechanical blocker posture. If requested changes cannot be represented as a non-overlapping one-pass bundle, do not emit a self-conflicting bundle. Rebuild the affected region as one consolidated replacement, or return the item for revision when the declared review mode allows blocked output.

#### **Review stability and no-moving-target discipline (required for diff-first approval loops)**

Applies to Epic Plans, Implementation Plans, Live QA Plans, remediation plans, closeout reviews, and other diff-first approval loops that use PF27 templates.

Rules:

* Full-gate first pass is required. The first approval review MUST apply the full active review gate set to the full artifact, not a partial subset.

* Gate freeze across the same review loop. After the first review on a given artifact line, do not introduce a new blocker from already-visible unchanged text unless triggered by current-revision text, a newly supplied authoritative input, a PF canon change, or a prior read failure.

* Coupled-constraint rule. If a reviewer requires more explicitness, the same review MUST also declare the coupled constraints triggered by that explicitness, including provenance, command-string, path/locus, creation-ownership, schema/header, naming, and portability constraints.

* Unchanged-text blocker rule. Any blocker first raised against unchanged text in a later revision MUST state the trigger that made it newly raisable. Without a valid trigger, classify it as Review Drift.

* Review Drift handling. If an omitted earlier-visible blocker is discovered later, label it as Review Drift, state that it was visible earlier, consolidate other same-scope pre-existing blockers in the same review, and stop drip-feeding blockers from that same unchanged-text family in later rounds.

* Contradictory review prohibition. Do not alternate between "too implicit" and "too explicit" on the same requirement family unless the later problem is created by newly changed text or the exact canon constraint supporting the later objection was already cited in the earlier review.

* Read-failure and truncation handling. If a missed issue was caused by truncation, partial retrieval, or other read failure, rerun the full sweep after full retrieval before issuing a new decision.

* Non-author penalty rule. Issues that were visible in an earlier reviewed revision but omitted by the reviewer MUST NOT be framed as author-created churn, treated as a fresh author-side defect cycle, or used to imply that the author changed requirements when the review target itself moved.

* Approval integrity. A later-discovered real blocker may still block approval, but it MUST be handled under the provenance and Review Drift rules above.

* Required blocker provenance in review output. Every blocker or caveat in a diff-first approval loop MUST be classed as one of: Introduced by current revision, Previously raised and still unresolved, or Review Drift.

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
* PF09 scope/status-only binding rule. When an Epic Plan, acceptance map, token→evidence matrix, close report, or manifest needs to record that a slice closes, contributes to, or leaves open a PF09 task or subtask, it MUST represent that as PF09 scope/status-only binding metadata, not as an acceptance token.  
* Acceptance tokens and PF09 scope bindings MUST remain distinct surfaces. Do not mint slice-local names or PF09-derived names as substitute acceptance tokens. Use canonical acceptance tokens for acceptance only, and record PF09 scope/status posture in a separate PF09 scope-binding section or equivalent metadata surface.  
* Temporary bridge tokens may be claimed only when they are canonical in PF04 or live PF10 and are bound to truthful governed evidence.  
* PF10 non-token proof-label posture (required). When live PF10 classifies a token-like label as a non-token proof label, plans, QA plans, reviews, OPS evidence, acceptance maps, token-to-evidence matrices, manifests, and closeout artifacts MUST NOT claim that label as a satisfied acceptance token unless the exact spelling is registered in Governance or minted by a later PF10 addendum. The work may continue as a governed non-token proof obligation with commands, artifacts, and PASS predicates.  
* Proof-label ADR closure rule (required). When live PF10 already resolves the exact token/proof-label posture, a plan or review MUST cite that live PF10 decision and remove any ADR placeholder that asks to resolve the same topic. If later close-stage review requires the proof label to become a gated acceptance predicate, route token admission through Governance before any acceptance artifact claims it.  
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

  * the token→evidence matrix (when required by the QA posture for that epic), and

  * the acceptance-map viability log at `audit/qa/<epic-id>/acceptance_map_viability.log` (when the epic carries an acceptance map or token→evidence matrix as part of the close-pack posture).  
* Close report minimum required fields (required):  
  * Canon pointer fields: the close report MUST include explicit canonical path pointers to the plan’s declared close-pack artifacts (at minimum: the close report path itself, the deterministic path-of-record selection, and any declared manifest, acceptance map, token→evidence matrix, and acceptance-map viability paths).

  * TI-002 mapping (when TI-002 is claimed): the close report MUST include an explicit mapping from TI-002 to the satisfying governed artifact(s), including (a) artifact path(s) and (b) a minimal excerpt or other precise locator sufficient to audit the claim without guessing.

  * For any other token claims that require explicit mapping, apply the same mapping rule as TI-002.

  * Workflow-truthfulness fields: if the close report states that a governed write, refresh, validation, or close-pack workflow ran, it MUST point to the same-run governed artifact(s) or gate-log artifact(s) that prove the execution, rather than reporting the action as narrative-only.

  * Reused-proof-family fields: if the close-pack reuses already-existing proof families from earlier deliverables or PR slices, the close report MUST identify those reused proof families by exact governed artifact path and MUST NOT present them as newly implemented in the close slice.

**Close-pack deterministic path-of-record (normative).**

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

* when the close-pack baseline includes an acceptance map, token→evidence matrix, or acceptance-map viability log, `key_outputs` MUST include explicit named bindings for each declared close-pack artifact.

* when the close-pack binds reused proof families or same-run gate execution evidence, those reused proof artifacts and governed gate-log artifacts MUST appear as explicit named `key_outputs` bindings.

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
* IA guidance **MUST** specify **intent, constraints, verification, and evidence requirements**.  
* When canon already provides concrete operator instructions, commands, required fields, safety rails, validation checks, evidence captures, canonical paths, or decision rules for the task, the Ops task record **MUST** include those canon-grounded instructions explicitly.  
* If canon is silent, incomplete, or ambiguous, the Ops task record **MUST** state that the missing instruction is unknown and **MUST NOT** fabricate steps.

### **Not a PR (normative)**

* Ops tasks are **not** Codex PRs and **MUST NOT** be represented as “implementable PR work.”  
* Any plan/guide that includes both DEV work and OPS work **MUST** separate them and clearly label OPS work as: **PO-only execution, IA-guided**.

### **Ops Task record fields (required; what-not-how)**

Every Ops task record **MUST** include:

* **Task ID** (stable; referenced consistently)  
* **Owner:** `PO`  
* **Facilitator:** `IA`  
* **PF07 posture:** `PF07-derived` or `PF07-gap`  
* **Infra/ops fact inventory** (as applicable):  
  * target provider  
  * target project  
  * target service  
  * target repository  
  * target base URL or port  
  * target database instance or schema  
  * exact config key name  
  * exact governed evidence root or QA root  
  * exact expected value or exact value source in PF07  
* **PF07 gap statement** (required when the exact value is missing from PF07; state the missing fact set and mark the affected task or claim blocked by missing PF07 infrastructure inventory)  
* **External execution classification, if applicable:** CLI-local smoke | hosted-service operation | vendor-backed smoke | discovery only | not applicable  
* **Exact command proof or unresolved-command posture, if applicable:**  
* **Input identity boundary, if applicable:** state whether no app user IDs, no `person_uid`, no `user_id`, or other prohibited identity inputs are allowed.  
* **Secret persistence posture:** presence-only | redacted | hashed | not applicable; plaintext secret persistence is forbidden.  
* **Non-claims preserved:** state whether the task does not claim QA PASS, Live QA completion, PF09 status change, or epic closure.  
* **Intent / desired end state** (what changes; what “done” looks like)  
* **Constraints / safety rails** (what must remain true while executing)  
* **Success criteria** (observable outcomes; not assumptions)  
* **Closure dimension, if the task claims or supports closure** (exact environment, surface, or status dimension affected)  
* **Closure mode, if applicable:** direct runtime validation | binding-equivalence | substitution | documentation/evidence normalization only | not applicable  
* **Unchanged runtime facts already evidenced, if a non-runtime closure mode is used:**  
* **Governed evidence family to normalize, if applicable:**  
* **Superseded contradictory artifacts or reports, if any:**  
* **Evidence to capture** (what will prove the change; where it will be stored)  
* **Rollback intent** (what “revert” means at a high level)  
* **Secret handling note** (explicitly: no plaintext secrets in docs or evidence)  
* **Canon-grounded instructions, when available** (titles-only PF references; carry forward concrete operator steps, commands, required fields, safety rails, validation checks, evidence captures, canonical paths, or decision rules that already exist in canon)

**Controlled execution contract (required for exact-command, vendor-backed, external-smoke, or controlled-smoke ops tasks)**

Use this block when the Ops task depends on an exact command, external system, vendor-backed smoke, controlled network rails, or a proof classification that must be preserved before PO execution.

* **Command template or command source:** exact canon-backed command template, discovered command file, or unresolved-command posture.  
* **Command substitution source:** exact source for operator-substituted values, if applicable.  
* **Executable command artifact:** path where the final executable command must be stored before execution.  
* **Placeholder rule:** state how unresolved placeholders are detected and which classification applies if any remain.  
* **Target classification:** CLI-local smoke | hosted-service operation | vendor-backed smoke | discovery only | not applicable | other approved classification.  
* **CLI-local smoke classification rule:** for a CLI-local smoke, do not require hosted-service PF07 facts unless the approved target classification changes to a hosted-service operation. The plan or Ops task must still prove CLI-local facts, including command target, data source, execution context, runtime or prerequisite binding when applicable, required config-key presence, determinism pins, rails posture, application environment, and secret-safe evidence posture.  
* **Required target facts:** command target, data source, execution context, required config keys, credential-presence keys, deterministic pins, rails posture, and application environment.  
* **Target facts not required for this classification:** state any infra fact that is not required and why.  
* **Target-change rule:** if the target classification changes, state which owning canon or approved live addendum must provide the replacement target fact set before execution.  
* **Prerequisite proof:** list any prior PR, OPS, QA, or canon proof that must exist before execution and state the classification if it is absent or contradicted.  
* **Preflight matrix:** for each preflight row, record requirement, required proof, and status rule.  
* **Execution wrapper or operator command:** exact wrapper or command posture the PO must use after preflight passes.  
* **Run rules:** state forbidden retries, guessed substitutions, command edits after failure, automated-agent execution, secret persistence, and forced-PASS edits.  
* **Required evidence outputs:** concrete governed files to produce under the approved ops evidence root.  
* **Required content for evidence outputs:** exact content expectations for each required file, including command, input summary, environment posture, stdout, stderr, exit code, result summary, prerequisite matrix, and checksum ledger when applicable.  
* **Outcome classification map:** define exact PASS, FAIL\_BEHAVIOR, FAIL\_TOOLING, and TOOLING\_BLOCKED conditions for the task.  
* **Non-claims:** state whether the task does not claim QA PASS, Live QA completion, final acceptance, public-surface change, CLI flag change, PF09 status change, epic closure, or PF-canon drain completion.

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

### **Closure-mode declaration (required when closure is claimed without a new runtime exercise)**

If the guide intends to close or recommend closure for an environment, surface, or other closure dimension by binding-equivalence, substitution, or documentation/evidence normalization rather than by a newly exercised runtime, it MUST state all of the following explicitly:

* **Closure dimension:** exact environment, surface, or status dimension affected.  
* **Closure mode:** direct runtime validation | binding-equivalence | substitution | documentation/evidence normalization only.  
* **Unchanged runtime facts already evidenced:** exact previously proved runtime facts being relied on.  
* **No-new-runtime-claim statement:** state that no new runtime command, route behavior, environment binding, or OPS action is being claimed beyond the evidenced basis.  
* **Governed evidence family to normalize:** exact governed artifact family or path set that must be rewritten or refreshed to one authoritative posture.  
* **Superseded contradictory artifacts or reports:** identify any prior contradictory bundle or report that will be treated as superseded evidence.  
* **Same-change evidence refresh requirement:** when indexed governed bytes change, refresh the Human Evidence Index, Machine Mirror, checksum sidecars, and required sibling path-proofs coherently in the same change.

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

  ---

## **5\) Remediation Review Record (Template; REVIEW mode only)**

### **Scope**

Use this template for REVIEW-mode evaluation of an approved remediation lane, bounded implementation PR slice, cleanup PR, or follow-up remediation chain. It is review-only: it compares the approved lane or slice, the original attempt, any intermediate remedial attempts, and the current state, and it does not create new runbooks or new command sequences.

### **Required structure (paste-ready)**

**Artifact Map**

* Review lane or PR name:  
* Implementation or approval source:  
* Original attempt bundle:  
* Remediation bundle(s):  
* Extra evidence bundle:  
* Output:  
* Keywords traced:  
* Artifacts used:  
* PF canon used:

**Source Posture**

* Primary source of truth for what happened:  
* Plans or other secondary sources used for intended scope only:  
* PF20 used: YES | NO, and why:  
* PF23 used: YES | NO, and why:  
* Other PF canon used only where the primary source is silent:  
* Important limit, if any:  
* Search basis, if search-driven reconstruction was used:

**Provenance (Approved \-\> Attempt Chain \-\> Current State)**

* Approved source and scope statement:  
* Attempt-chain summary, repeated as needed:  
* Current remedial-attempt summary:  
* Net-effective outcome:

**Review Summary**

* What was attempted:

* What was insufficient in the earlier attempt:

* What changed in remediation:

* Whether the current state satisfies the approved scope:

* Remaining risk:

**Scope and Closure Claim Posture**

* **Approved task type:** closure-claiming | bounded intermediate | validation-only | sequencing-only | evidence-only | read-only discovery | other  
* **Does the approved task itself claim PF09 or canon closure now:** Yes | No  
* **Repository-change claim:** files changed | no files edited, created, or deleted | governed artifacts changed only | not applicable  
* **If the task claims no repo changes or no diff hunks, no-diff proof method and result:**  
* **If tests or CI are not acceptance evidence for this task, what evidence class is decisive instead:**  
* **If No, what still-open state must remain explicit:**  
* **Which later approved task or step owns remaining closure work, if any:**  
* **Public contract and boundary check:** state whether the current attempt adds any new public route, flag, serializer path, public contract field, acceptance-map path, token-matrix path, viability-log path, doc-delta-ledger path, close-pack path, QA-ledger work, Live QA runbook work, or PF-canon edits. If none are present, say so explicitly. If any are present, classify whether they are approved scope or scope drift.  
* **If current outputs remain blocked or incomplete-planned under current evidence, how that posture is recorded without overclaiming:**

**Governed Evidence Family Consistency (required when closure or later-drain posture relies on governed evidence)**

* **Closure dimension under review:**  
* **Closure mode:** direct runtime validation | binding-equivalence | substitution | documentation/evidence normalization only | not applicable  
* **Are the relied-on runtime facts unchanged from prior evidence:** Yes | No | Not applicable  
* **Is the governed evidence family internally consistent:** Yes | No  
* **If No, classification:** documentation/evidence failure  
* **If No, required review action:** stop the closure recommendation and do not consolidate contradictory source bytes until the family is normalized to one authoritative posture  
* **If a documentation/evidence normalization pass is being accepted instead of a rerun, what same-change refresh proves it:**  
* **Superseded contradictory artifacts or reports, if any:**

**Side-effect Classification Map (required when outside-family evidence refreshes or mirror rows are in scope)**

SE-001

* **Affected outside-family evidence family:**  
* **Classification:** expected updater convergence | required dependency refresh | unexpected drift  
* **Proof-companion paths or artifact paths affected:**  
* **Affected Machine Mirror artifact keys or discovered paths, if any:**  
* **Validation result:** paths exist | proof companions validate | mirror rows match artifact key, proof anchor, sha256, and size | not yet validated  
* **PASS posture:** fail-closed PASS supported | blocker | caveat only  
* **Evidence pointer:**

Repeat SE blocks as needed.

**Keyword Hit Map (optional when search-driven reconstruction was used)**

K-001

* Artifact:  
* Keyword(s) matched:  
* Why it matters:  
* Evidence pointer:

Repeat K blocks as needed.

**Chain of Events**

EVT-001

* Event:  
* Event type:  
* Timing basis:  
* Evidence pointer:

Repeat EVT blocks as needed.

**Diff Review (required when code or governed-artifact diffs are under review)**

DR-001

* Change summary:

* Risk assessment:

* Why it matters:

* Evidence pointer:

* Approved-plan linkage:

* Supported status posture, if any:

Repeat DR blocks as needed.

**Root Cause Analysis (RCA)**

A) Bug or failure statement

* Failure sequence:  
* Where it occurred:  
* Evidence pointer(s):

B) Root cause(s)

* Root cause statement:  
* Evidence pointer(s):  
* PF references only when needed:

C) Fix across attempts

* What in the earlier attempt was insufficient:  
* What changed in remediation:  
* Why the change addresses the root cause:

D) Fix verification

* Proof the issue is resolved:  
* Residual risk or edge case evidenced:

**Deliverables and Results**

RES-001

* Deliverable produced:  
* Result now true that was not true before:  
* Residual risk:  
* Evidence pointer:

Repeat RES blocks as needed.

**Remediations Applied**

RMD-001

* Remediation:  
* Why it was needed:  
* What evidence shows it worked:  
* Evidence pointer:

Repeat RMD blocks as needed.

**Findings**

DR-001

* Source artifact or lane:  
* What I observed:  
* Why it matters:  
* PF reference(s), if canon is invoked:  
* Canon proof excerpt(s), if canon is invoked:  
* Evidence pointer(s):  
* Impacted checklist task ID(s), if proven:  
* Impacted checklist subtask ID(s), if proven:  
* Supported status posture:  
* Review provenance class, if this finding is used as a blocker or caveat: Introduced by current revision | Previously raised and still unresolved | Review Drift  
* Trigger for newly raisable unchanged-text issue, if applicable:

Repeat finding blocks as needed.

**Requirement Satisfaction Crosswalk (required when approval conditions or requirement labels exist)**

RC-001

* Requirement label:  
* Baseline attempt or step:  
* Baseline status:  
* Baseline evidence pointer(s):  
* Intermediate attempt status block(s), repeated as needed:  
  * Attempt label:  
  * Status:  
  * Evidence pointer(s):  
* Remedial change or current-state proof that addresses it:  
* Current status after the latest attempt or closure check:  
* Evidence pointer(s) in the latest attempt or closure check:  
* Notes:  
* Impacted checklist task ID(s), if proven:  
* Impacted checklist subtask ID(s), if proven:

Repeat RC blocks as needed.

**Checklist Impact & Status Posture (when a status move or later-drain posture is in scope)**

* Affected PF canon home(s) or status record:  
* Exact affected locator(s):  
* Current canon posture:  
* Current PF09 or other canon recorded status, if relevant:  
* Actual implemented state:  
* Actual OPS state, if applicable:  
* Actual governed evidence state:  
* Supported later-drain action: change to Done | change to Partial | change to Not done | change to Consolidation pending | change to Optional | No status change recommended  
* Drain readiness classification: Supportable from repo evidence | Not yet supportable from repo evidence | Already drained into PF-canon  
* Why this status posture is supported:  
* Evidence pointer(s):  
* PF proof excerpt(s) when a PF checklist or status record is relied on:  
* Epic-close expectation: at epic close | after an additional PR or OPS slice | after a separate canon-only drain step  
* Linked Findings item(s):  
* Linked CHG item(s), if any:

**Evidence Print (PASS PROOF; required)**

A) Acceptance coverage evidence

* Requirement label:

* Evidence pointer(s) proving satisfaction:

* Key proof facts copied verbatim from the reviewed artifacts:

Repeat acceptance-coverage lines as needed.

B) Evidence and verification posture now satisfied

* What earlier evidence or verification gap existed:

* What is now present:

* Evidence pointer(s):

C) Token and gate evidence

* Tokens explicitly claimed (names-only), or state that no tokens were explicitly claimed.  
* If no tokens were explicitly claimed, include the search method and result.  
* Unsupported, removed, downgraded, or non-token proof labels, if any:  
* If a prior attempt claimed an unsupported token or token-like label, the review MUST record the source-row correction, regenerated Human Evidence Index and Machine Mirror posture when affected, refreshed hash/path-proof posture when affected, and exact search method/result proving the unsupported claim is absent from the governed source and evidence surfaces.  
* Evidence pointer(s):

D) Test or CI proof

* Job or test name:

* Pass indicator copied verbatim:

* Where it appears in the reviewed artifacts:

Repeat test or CI lines as needed.

E) Artifact and evidence outputs

* Path:

* Type:

* Key proof facts copied verbatim from the reviewed artifacts:

Repeat evidence lines as needed.

**Doc Deltas (PF-Canon only; required when the review supports a canon or checklist change)**

**PF Checklist Impact Summary**

* PF task ID:

* PF subtask ID(s):

* Current status if evidenced:

* Status action:

* Evidence pointer(s):

* Linked Findings item(s):

* Linked CHG item(s), if any:

**Doc Delta Detection Workflow**

CHG-001

* Change claim type: behavior or output | configuration or environment | governed paths or artifact families | tokens, rails, or evidence posture | rails/evidence posture | interface or contract | workflow steps | PF09 status-impact requirement | supported PF09 status posture changes | other  
* Claim:  
* Evidence pointer:  
* Canon basis: CANON ALIGNED | CANON MISMATCH | NO CANON MISMATCH | CANON SILENCE | CANON SILENT | ALREADY DRAINED  
* Canon Check Gate:  
* Canon proof excerpt(s) when canon is invoked:  
* Impacted PF task ID(s), if any:  
* Impacted PF subtask ID(s), if any:  
* Proposed status action, if any:  
* Linked finding(s):

Repeat CHG blocks as needed.

**PF Doc Delta Proposal**

DD-001

* Target doc:

* Target section:

* Delta (actionable; 1–3 bullets):

* Why:

* Evidence pointer(s):

* PF proof excerpt(s) when canon is invoked:

* Why this is the correct home:

Repeat DD blocks as needed.

**Canon Documentation Outcomes**

AD-001

* Addendum title:  
* Why:  
* Supportable status change versus current canon or drain state, if relevant:  
* Decision / rule / clarification:  
* Drain targets (doc delta intents):  
* Supersedes / conflicts, if applicable:  
* Implementation impact:  
* Evidence pointer:

Repeat addendum blocks as needed.

**Retrospective Notes**

* What went well:  
* What did not go well:  
* What we learned about the process:  
* What we learned about the system:

**Unknowns or Missing Evidence**

UNK-001

* Unknown or missing item:  
* Why it matters:  
* Evidence needed:  
* Where that proof should exist, if known:  
* Search basis, if search-driven reconstruction was used:

Repeat UNK blocks as needed.

**Decision**

* Decision:  
* Why this decision is supported:  
* Residual caution or follow-up boundary, if any:

## **6\) Audit Analysis Record (Template; REVIEW mode only)**

### **Scope**

Use this template when an audit report is being translated into explicit home classification, must-act-now posture, and doc-delta proposals. It is review-only: it inventories the audit inputs, summarizes the drift themes, maps each finding to the correct PF home, and records whether any runnable checklist delta is supported.

**PF23 audit-classification posture**

* PF23 audit observations must be classified to owning canon homes before being treated as PF09.x task deltas, remediation scope, implementation work, OPS work, evidence homes, or acceptance tokens.  
* PF23 audit observations may support PF09.x task deltas only when the finding proves runnable development or operations work in the relevant phased PF09.x scope.  
* If the correct action is classification, routing, documentation alignment, or PO adjudication only, record that posture explicitly and do not convert the observation into implementation or OPS scope by assumption.

### **Required structure (paste-ready)**

**Artifact Map**

* Audit Report:

* Epic Plan:

* Existing Issues List:

* PF Canon consulted:

* Output:

**Audit Summary**

* What the audit compares:  
* Top drift themes:  
* Number of discrete findings extracted:  
* Number of must-act-now findings:  
* Concrete canon delta(s) supported:  
* Any no-task-delta conclusion, if supported:  
* PF doc homes consulted for classification:  
* PF doc homes receiving proposals:

**Findings → Doc Delta Map**

FND-001

* Finding (one sentence):  
* Audit anchor (verbatim line):  
* Audit evidence pointer:  
* Epic Plan linkage (one sentence):  
* Epic Plan anchor (verbatim line or N/A):  
* Must-act-now: YES | NO  
* Observation-only: YES | NO  
* Re-open trigger, if observation-only:  
* Disposition: Doc delta proposed | Observation only | Existing issue duplicate | No doc delta needed | No action | PO decision needed  
* Correct home(s):  
  * PF09.x task delta: YES | NO  
  * PF09.x target, if any:  
  * PF14 mechanics delta: YES | NO  
  * PF02 architecture delta: YES | NO  
  * Other PF doc delta(s):  
  * PF20 historical correction: YES | NO  
* Existing issue duplicate:  
* Why these are the correct homes:  
* Review provenance class, if this finding is used as a blocker or closeout caveat: Introduced by current revision | Previously raised and still unresolved | Review Drift  
* Trigger for newly raisable unchanged-text issue, if applicable:

Repeat FND blocks as needed.

**Doc Delta Proposals — PF09.x (Tasks)**

* None. when no PF09.x task delta is supported.

PD-001

* Target doc:  
* Target section:  
* Delta (actionable; 1–3 bullets):  
* Why:  
* Evidence pointer(s):  
* PF proof excerpt(s) when canon is invoked:

Repeat PF09.x proposal blocks as needed.

**Doc Delta Proposals — Other PF homes**

PD-001

* Target doc:

* Target section:

* Delta (actionable; 1–3 bullets):

* Why:

* Evidence pointer(s):

* PF proof excerpt(s) when canon is invoked:

* Why this is the correct home:

Repeat proposal blocks as needed.

**Open Questions for PO**

OQ-001

* Question:  
* Why it matters:  
* Evidence pointer(s):  
* Decision needed:

Repeat open-question blocks as needed.

**Final line**

END OF AUDIT ANALYSIS

## **7\) Implementation Closeout Report (Template; REVIEW mode only)**

### **Scope**

Use this template when a completed implementation slice, remediation bundle, or epic closeout needs a review-grade report of what stayed fixed, what was reused, what was newly delivered, what evidence exists, and what canon or checklist follow-up remains. It is review-only: it records implementation outcomes and closeout posture, and it does not create new runbooks, new commands, or new acceptance tokens.

### **Required structure (paste-ready)**

**Executive Summary**

* Scope classification:

* Preserved scope boundaries:

* Approved reuse baseline, if any:

* New implementation allocation or slice map:

* Biggest wins:

* Biggest remaining risks or gaps:

**Implementation Breakdown (slice-by-slice)**

CHG-001

* Slice name:

* Purpose:

* Key changes, high level:

* Key surfaces touched:

* Tests or evidence produced:

* Outcome:

* Evidence pointer(s):  
* PF10/PF-canon coverage state: fully covered | partially covered | silent | not yet drained  
* Source-limit or gap note, if any:  
* If a claim depends on a non-PF or in-session artifact, exact source that carries the claim:

Repeat CHG blocks as needed.

**Major Surfaces Affected**

* Surface family:  
* Specific surfaces:  
* Why it matters:  
* Evidence pointer(s):  
* PF10/PF-canon coverage state: fully covered | partially covered | silent | not yet drained  
* Source-limit or gap note, if any:

Repeat surface blocks as needed.

**Evidence Inventory**

* Evidence family:  
* Path(s):  
* What it proves:  
* Related token names, if explicitly claimed:  
* Evidence pointer(s):  
* PF10/PF-canon coverage state: fully covered | partially covered | silent | not yet drained  
* Source-limit or gap note, if any:

Repeat evidence-family blocks as needed.

**Source Posture**

* Primary source of truth for what happened:  
* Secondary sources used for intended scope only:  
* PF20 used: YES | NO, and why:  
* PF23 used: YES | NO, and why:  
* Other PF canon used only where the primary source is silent:  
* Non-PF in-session artifacts used, if any:  
* Important limit, if any:

**Retrospective — Process**

* What went well:  
* What did not go well:  
* What we learned:  
* Evidence pointer(s):

**Retrospective — Application / System**

* What we learned about the system:  
* System boundaries preserved or clarified:  
* Known application-level lessons:  
* Evidence pointer(s):

**Risk and Debt Register**

RISK-001

* Priority: Must-fix | Should-fix | Nice-to-have  
* Risk or debt statement:  
* Evidence status:  
* Evidence pointer(s):  
* Why it matters:  
* What would prove resolution:  
* Closeout impact:

Repeat risk/debt blocks as needed.

**Canon Alignment and Documentation Outcomes**

* Canon references used:

CR-001

* PF document title:  
* How it was used:  
* Evidence pointer(s):  
* Source-limit or gap note, if any:

Repeat canon-reference blocks as needed.

* Existing live PF10 delta or canon mismatch on record:  
* Supportable status change(s) from repo evidence, if any:  
* Current canon or drain state for those rows, if different:  
* Token or evidence semantics note, if applicable:  
* Evidence-family completeness or same-change-family note, if applicable:  
* Likely drain targets by title only:  
* Additional PF10 addendum needed: YES | NO  
* Why:

**Proposed PF10 Addenda (when the retrospective supports living-addendum text)**

* None: state when no new PF10 addenda are proposed, why no new addendum is needed, and which existing addenda, docs PR, or evidence record already carries the needed posture.

AD-001

* Addendum title:  
* Why:  
* Decision / rule / clarification:  
* Drain targets (doc delta intents):  
* Supersedes / conflicts, if applicable:  
* Implementation impact:  
* Evidence pointer(s):

Repeat addendum blocks as needed.

**Closure Decision Set (when close posture depends on explicit decisions)**

DEC-001

* Decision:

* Rationale:

* Supported status updates, if any:

* Closure timing recommendation, if any:

* No-new-runnable-task-delta conclusion, if any:

* Observation-only themes and re-open triggers, if any:

* Net resolution effect:

Repeat DEC blocks as needed.

**Closure Evidence Snapshot**

A) Evidence produced

* Path:  
* What it proves:  
* Evidence pointer(s):  
* Related token names, if explicitly claimed:  
* Source-limit or gap note, if any:

Repeat produced-evidence lines as needed.

B) Evidence missing or ambiguous

* Item:  
* Evidence status: Unknown | Missing | Ambiguous | Supportable but not drained | Not applicable  
* Why it matters:  
* What would prove it:  
* Where that proof should exist, if known:  
* Evidence pointer(s):  
* PF10/PF-canon coverage state: fully covered | partially covered | silent | not yet drained  
* Source-limit or gap note, if any:

Repeat missing-or-ambiguous lines as needed.

C) Open closure items or questions for the Lead

* Question:  
* Why it matters:  
* Relevant canon or evidence:  
* Evidence pointer(s):  
* Decision needed from Lead or PO:

Repeat question lines as needed.

## **8\) QA Pass Review Record (Template; REVIEW mode only)**

### **Scope**

Use this template when a completed Live QA check or approved Live QA check cluster is being reviewed against its approved Check Block or Check Blocks and its Deliverables Report. It is review-only: it determines whether each named step is trustworthy, whether the plan-defined deliverables and PASS criteria were satisfied for every reviewed step, whether each step stayed aligned to the approved token posture when token-attached, and whether any follow-up or doc delta is required. When a check cluster is reviewed, the review MUST account for every check ID named in the check label or `QA_STEP_NAME`, including each step’s deliverables, PASS criteria, token posture, final FAIL or BLOCKED posture, deviations, evidence-trust facts, and any no-broader-closure claim. It does not create new runbooks, new commands, or new acceptance tokens.

### **Required structure (paste-ready)**

**Review Summary**

* Check label:  
* Decision line:  
* Deliverables Report anchor:  
* Evidence-trust statement:  
* Evidence pointer(s):  
* Approved-plan PASS criteria statement:  
* Evidence pointer(s):  
* Decision lane, branch policy, or scope-discipline statement, if applicable:  
* Evidence pointer(s):  
* Approved token-posture statement, if token-attached:  
* Evidence pointer(s):  
* Doc Deltas:  
* State `None` when no PF-Canon inconsistencies or new doc requirements were found.

**Findings**

FND-001

* What you observed:  
* Classification:  
* PF touchpoints when needed:  
* Evidence pointer(s):  
* Why it matters:  
* Drives decision: Yes | No  
* Negative-claim proof, if this finding depends on the absence of direct lines in DELIVERABLES\_REPORT\_FILE:

Repeat finding blocks as needed.

Finding posture rules:

* Non-blocking planning failures, process imperfections, or earlier failed attempts MAY be recorded as findings, but they MUST be distinguished from verdict-driving facts and MUST use `Drives decision: No` when they do not affect the decision.  
* If the review relies on step-evidence trust, the findings MUST make explicit which trust facts were confirmed, such as the governed `primary.log` header, captured rails and determinism pins, and the current-state QA root and manifest-pair posture when applicable.  
* If a finding depends on the absence of a direct token-level proof line or other direct proof line in DELIVERABLES\_REPORT\_FILE, the review MUST record the exact negative-claim search and the no-match result rather than implying absence.  
* Non-fatal runtime warnings MAY be recorded as findings with `Drives decision: No` when the deliverables report also records no `TOOLING_BLOCKED`, `FAIL_TOOLING`, or `FAIL_BEHAVIOR` condition and the approved PASS predicates are otherwise satisfied. The review MUST still record the warning evidence pointer and any follow-up needed, but the warning alone is not a blocker or fail classification.

**Evidence Print**

A) Required deliverables checklist

* Deliverable name/label, quoted from plan/caveats:  
* Evidence pointer to the plan/caveats:  
* Expected path:  
* Present in DELIVERABLES\_REPORT\_FILE: Yes | No  
* Evidence pointer in DELIVERABLES\_REPORT\_FILE:

Repeat deliverable lines as needed.

B) Evidence artifacts relied on

* Path/label, exact as listed in DELIVERABLES\_REPORT\_FILE:  
* Evidence pointer:  
* Key proof facts, 1–3 short exact strings, status lines, or hashes:

Repeat artifact lines as needed.

C) Tokens/gates (required only when the reviewed step is token-attached)

* Token/gate name, quoted from plan/caveats, with Evidence pointer:  
* Evidence pointer(s) in DELIVERABLES\_REPORT\_FILE proving it, or state `Unknown.` when DELIVERABLES\_REPORT\_FILE does not surface a direct token-level proof line:  
* Negative-claim proof, if `Unknown.` is used:

Repeat token lines as needed.

Acceptance-claim boundary rule:

* If a Live QA check records no acceptance-token claim and limits claims to the evidence scope, absence of an acceptance map, token matrix, or close-pack artifact is close-stage posture, not a runtime behavior failure for that check.  
* The review MUST record whether the missing close-stage artifact affects the reviewed check verdict, the later closeout posture, or neither.  
* The review MUST NOT convert a missing close-stage artifact into a token claim, PASS proof, or runtime blocker unless the approved check made that artifact a required deliverable for the check itself.

**QA Verdict and Optional Follow-ups**

* Verdict line:  
* Evidence-grounded decision bullets:  
  * primary evidence trust:  
  * deliverables posture:  
  * PASS criteria posture:  
  * token posture, if applicable:  
* Optional follow-up or planning-failure note, if any:

Execution-deviation acceptance rule:

* A QA Pass Review MAY accept final PASS after an operational dependency installation, QA-only helper reconstruction, or proof-posture append only when the deviation is recorded in the Deliverables Report or governed step evidence, the same proof target remains in scope, required deliverables remain unchanged, PASS/FAIL criteria remain unchanged, token posture remains unchanged, and final PASS evidence is captured under the approved QA evidence root.  
* For dependency-install deviations, the review MUST record the missing or unready dependency, the installation or activation action taken, the initial transient state when evidenced, the final rerun PASS evidence, and whether the issue remains a planning dependency-readiness gap with `Drives decision: No`.  
* For QA-only helper reconstruction, the review MUST record why the original helper or transcript could not be run, what wrapper or helper was actually used, whether the wrapper stayed execution-only, whether the same approved per-step validation commands or proof actions were preserved, and whether the same approved QA-root receipt families were produced.  
* For proof-posture append deviations, the review MUST record the exact proof-posture lines added, the approved proof target that required those lines, the affected primary log, the refreshed sibling path proof when applicable, and whether the append avoided any new token, PF09.x drainage claim, product-code change, repo-test change, public-contract change, PF document edit, or governed-artifact change outside the QA root.  
* If any of those conditions are not proven, the deviation MUST NOT be hidden under PASS; classify it as blocker, caveat, tooling failure, or remediation work according to the approved PASS/FAIL map and source authority.

**ADRs — Deviations (optional)**

**ADR-DEV-01**

* **What changed:**  
* **Why it changed:**  
* **Plan or caveat reference, with Evidence pointer:**  
* **What was actually run, with Evidence pointer:**  
* **Evidence impact: files added/changed/missing, using verbatim paths**  
* **Decision:**  
* **Canon impact:**  
* **PF proof excerpt, if canon is invoked:**

**Repeat ADR-DEV blocks as needed.**

* **PF proof excerpt, if canon is invoked:**

**State `No deviations observed for this step.` when no deviation block is needed.**

## **9\) Final QA Closeout Review \+ QA RCA (Template; REVIEW mode only)**

### **Scope**

**Use this template when the completed Live QA stream for an epic must be synthesized into a closeout recommendation, canonical RCA basis, coverage-vs-plan accounting, and PF-only doc-delta proposals. It is review-only: it summarizes executed QA and closeout posture, and it does not create new runbooks, new commands, or new acceptance tokens.**

### **Required structure (paste-ready)**

**Artifact Map**

* **Epic:**  
* **PF10:**  
* **Implementation Guide:**  
* **QA Plan:**  
* **Output:**

**QA Closeout Summary**

* **Epic reviewed:**  
* **PF10-stated QA execution outcome:**  
* **What was reviewed:**  
* **Overall readiness:**  
* **Root cause category:**  
* **Implementation Guide framing, if used:**  
* **Evidence pointer(s):**

**Canonical RCA Requirement Basis**

**A) PF19 references relied on**

**REF-001**

* **PF19 reference:**  
* **Proof excerpt:**  
* **Evidence pointer:**

**Repeat PF19 reference blocks as needed.**

**B) PF27 and PF06 references relied on**

**REF-001**

* **PF reference:**  
* **Proof excerpt:**  
* **Evidence pointer:**

**Repeat PF27 / PF06 reference blocks as needed.**

**Checklist of required RCA/closeout elements**

* **D0 / Step-0 discovery and baseline rails posture:** state whether D0 discovery, Step-0 discovery, Step-0 doc-delta capture when required, closed/open rails posture, deterministic pins, and captured environment posture are covered, missing, or not applicable.  
* **Functional runtime proof on changed runtime surfaces:**  
* **Governed current-state QA evidence under the epic QA root:**  
* **Per-step-cluster manifest/header/path-proof trust proof:** when a final QA closeout asks a reviewer to approve an executed QA step cluster, the artifact MUST surface the manifest entry, canonical primary-log path, primary-log header fields, `captured_env`, `evidence_artifacts`, `intended_tokens`, `claimed_tokens`, path-proof binding, token posture, rails/determinism posture, and final status for that cluster. A PASS result JSON or summary label alone is not sufficient closeout proof when manifest, header, or path-proof trust is required.  
* **QA RCA & Doc Delta summary:**  
* **Coverage vs QA Plan accounting:**  
* **All-slice coherence proof:** when the QA closeout claims post-implementation coherence after multiple slices, verify all prior step primary logs required for that claim are present, all required implementation-slice artifacts are present, and the derived status agrees with the recorded primary-log header status and exit code.  
* **Readiness / closeout recommendation:**  
* **Codespaces harness execution at least once:**  
* **Indexed evidence under Human Evidence Index and Machine Mirror:**  
* **Compliance statement:**

**Source-of-Truth Posture**

* **Primary SoT for epic-specific QA events:**  
* **Implementation Guide used:**  
* **QA Plan used:**  
* **Implementation Guide authority posture:** goals framing only | scope framing only | close authority | not used | other evidence-backed posture  
* **QA Plan authority posture:** intended QA requirement framing only | close authority | not used | other evidence-backed posture  
* **Mismatches identified between the primary SoT and the QA Plan, if any:**  
* **Negative-claim proof, if a mismatch search is used:**  
* **If a PF10 addendum is the decisive close-authority statement: say whether it provides direct evidence-pointer lines or evidence-basis prose only.**  
* **If only evidence-basis prose is available: record that as an auditability caveat and identify the governed evidence clusters used to support the closeout conclusion.**

**QA Timeline**

Chronology rule: reconstruct chronological order from explicit timestamps when present. When no timestamp is visible, use primary-source order and state that basis in the event record.

**EV-001**

* **Source order or chronology basis:**  
* **Event type:** QA Step | Remediation Loop | ADR | Decision | Closeout Event | Other  
* **Event name/label:**  
* **Outcome label:**  
* **Evidence pointer(s):**

**Repeat event blocks as needed.**

**Coverage vs QA Plan**

**CV-001**

* **Step name as written in QA Plan:**  
* **Coverage status:** fully evidenced | partially evidenced | blocked | not run | not applicable  
* **Evidence pointer(s):**  
* **Mismatches/deviations vs QA Plan, if any:**  
* **Accepted execution deviation(s), if any (examples: bounded Moon Loop rerun, rails change, QA syntax correction, step-local dependency-preflight correction):**  
* **Original planned receipt(s), if any:**  
* **Accepted remediation or rerun receipt(s), if any:**  
* **Final accepted proof basis:** original planned receipt | accepted remediation receipt | accepted rerun receipt | combined approved evidence | not applicable  
* **Why the deviation remained acceptable, with Evidence pointer(s):**  
* **Closeout impact:** blocker | non-blocker | caveat | follow-up only

**Repeat coverage blocks as needed.**

**Outcome Meaning**

* **What the final QA outcome means:**  
* **What the final QA outcome does not claim:**  
* **Truth-class separation:** state whether implementation readiness, QA readiness, final QA outcome, documentation drainage, PF09.x drainage, formal close-pack completion, vendor-version runtime conformance, and live vendor behavior are claimed, not claimed, or deferred. Local Live QA proof MUST NOT be overread as any truth class it does not directly prove.  
* **Live QA role boundary:** state whether Live QA performed proof-only work, an approved in-session remediation, implementation work, PF-canon editing, or closeout action. If implementation, remediation, PF-canon editing, or closeout action is not explicitly authorized and evidenced, record it as not claimed.  
* **Readiness caveats, if any:**  
* **Evidence pointer(s):**

**Findings**

**FND-001**

* **What happened, grounded in the reviewed evidence:**  
* **Why it matters:**  
* **Classification:** SoT internal mismatch | Evidence posture gap | Process-rail gap | Tooling-infra gap | Implementation gap | Plan-guidance ambiguity | other evidence-backed class  
* **Anomaly label, if applicable:** FAIL\_BEHAVIOR | FAIL\_TOOLING | TOOLING\_BLOCKED | none  
* **PF touchpoints when needed:**  
* **Evidence pointer(s), or state `none provided.`:**  
* **Negative-claim proof, if `none provided.` is used:**

**Repeat finding blocks as needed.**

**Root Cause Analysis**

**Failure or Friction Patterns Evidenced**

**FP-001**

* **Pattern:**  
* **Classification:** product behavior | QA harness | evidence posture | planning drift | documentation or drainage posture | current-reality context | other evidence-backed class  
* **Evidence pointer(s):**

**Repeat failure or friction pattern blocks as needed.**

**A) Primary root cause**

* **Statement:**  
* **Evidence pointer(s):**

**B) Contributing factors**

**CF-001**

* **Factor:**  
* **Evidence pointer(s):**

**Repeat contributing-factor blocks as needed.**

**C) What made it hard to detect earlier, if applicable**

* **Statement:**  
* **Evidence pointer(s):**

**D) What made it hard to close confidently, if applicable**

* **Statement:**  
* **Evidence pointer(s):**

**Remediation Loop Assessment**

**RL-001**

* **Loop label:**  
* **Outcome:**  
* **Evidence pointer(s):**  
* **Residual uncertainty, if any:**

**Repeat remediation-loop blocks as needed.**

**Evidence Hygiene and Recurrence Prevention**

* **Strong evidence posture observed:**  
* **Recurring proof-risk pattern, if any:**  
* **What would prevent recurrence:**  
* **Template or PF-canon guard to preserve:**  
* **Evidence pointer(s):**

**Implementation Gaps and Proposed Fixes**

**IMP-01**

* **Symptom, quoting reviewed evidence where useful:**  
* **Expected behavior from reviewed evidence and/or PF canon:**  
* **Evidence pointer(s):**  
* **Likely locus only if the reviewed evidence names a component or surface:**  
* **Proposed fix, high-level only:**  
* **Verification hook:**

**Doc Deltas (PF-Canon only; excluding PF10)**

**A) PF19 doc deltas (targeted)**

* **None:** state when no PF19 doc delta is required, and provide evidence pointer(s) or negative-claim proof when the reviewed source says none.

**DD-001**

* **Section:**  
* **Delta:**  
* **Tag:** NEW CANON PROPOSAL | CLARIFICATION | CONSISTENCY | DOC HYGIENE | DELETION | other evidence-backed tag  
* **Proof excerpt(s) when canon is invoked:**  
* **Why:**  
* **Evidence pointer(s):**

**Repeat PF19 delta blocks as needed.**

**B) Optional other PF doc deltas (maximum 5; only if PF19 is not the correct home)**

* **None:** state when no optional other PF doc deltas are needed, and provide evidence pointer(s) or negative-claim proof when the reviewed source says none.

**DD-001**

* **Doc:**  
* **Section:**  
* **Delta:**  
* **Tag:** NEW CANON PROPOSAL | CLARIFICATION | CONSISTENCY | DOC HYGIENE | DELETION | other evidence-backed tag  
* **Proof excerpt(s) when canon is invoked:**  
* **Why PF19 is not the correct home:**  
* **Evidence pointer(s):**

**Repeat optional other-doc delta blocks as needed.**

**QA Verdict and Recommendation**

* **Verdict:** PASS | READY WITH CAVEATS | NOT READY | BLOCKED  
* **Why this verdict is supported:**  
* **Caveats:** state what the verdict does not claim, including any undrained PF status, formal close-pack posture, or bounded execution deviation.  
* **Non-blocker rationale:** state why any accepted deviation remains non-blocking, with evidence pointer(s).  
* **Follow-up recommendation:** state any future doc delta, drain target, final close-pack acceptance concern, or review guard that should be preserved.

## **10\) Epic Closure Review \+ Retrospective (Template; REVIEW mode only)**

### **Scope**

Use this template when one review artifact must combine epic closure decision, closure-trace accounting, implementation retrospective, PF-only doc-delta routing, and recommendation posture. It is review-only: it records what was completed, what evidence supports closure, what follow-up remains, and what should drain later, and it does not create new runbooks, new commands, or new acceptance tokens.

### **Required structure (paste-ready)**

**Inputs Posture**

* **Implementation Guide provided:**  
* **QA Plan provided:**  
* **Input-name, epic-name, or phase-label mismatch, if any:** state any mismatch between prompt labels and primary-source epic identity, which source controls the review identity, whether the prompt label is preserved only as artifact-map or provenance text, and evidence pointer(s)  
* **Sources intentionally excluded from closure authority, if any:**  
* **Why excluded sources do not drive closure:**  
* **Primary epic-specific source of truth:**  
* **Current-reality source, if used:**  
* **PF-Canon homes used where the primary source is silent:**  
* **Implementation Guide used for intended scope framing only:**  
* **QA Plan used for intended QA requirement framing only:**  
* **Evidence pointer(s):**

**Closure Registers**

**A) Deliverables Register**

**CR-DEL-001**

* **Deliverable label:**  
* **Source:**  
* **Anchor quote:**  
* **Explicitly stated required evidence, path, or token strings, verbatim if present:**  
* **Evidence pointer:**

**Repeat deliverable blocks as needed.**

**B) QA Verification Register**

**CR-QA-001**

* **Step or verification label:**  
* **Source:**  
* **Anchor quote:**  
* **Required evidence outputs or pass-fail posture, verbatim if present:**  
* **Evidence pointer:**

**Repeat verification blocks as needed.**

**C) Primary Results Register**

**CR-RES-001**

* **Result claim summary:**  
* **Anchor quote:**  
* **Evidence pointers or paths, verbatim, or state `none provided.`:**  
* **Outcome label, if recorded:**  
* **Evidence pointer:**

**Repeat result blocks as needed.**

**D) Current-Reality Register**

**CR-REAL-001**

* **Surface summary:**  
* **Anchor quote:**  
* **Paths or components, verbatim if present:**  
* **Closeout impact:**  
* **Closure authority note: state whether the current-reality source proves closure, blocks closure, or only contextualizes closure.**  
* **Evidence pointer:**

**Repeat current-reality blocks as needed.**

**Closure Trace Ledger**

**CTL-001**

* **Deliverable:**  
* **Mapped QA verification item(s):**  
* **Mapped primary-source result claim(s):**  
* **Primary-source evidence pointer status:** present | partially present | missing | not applicable  
* **Current-reality check:**  
* **Status:**  
* **Why:**  
* **Evidence pointer(s):**

**Repeat closure-trace blocks as needed.**

**Path and Surface Reality Ledger**

**PSR-001**

* **Path or surface string, verbatim:**  
* **Source(s):**  
* **Status:**  
* **Closure mode, if the surface or environment is treated as closed:** direct runtime validation | binding-equivalence | substitution | documentation/evidence normalization only | not applicable  
* **Is the governed evidence family for this surface internally consistent:** Yes | No  
* **If closed without a new runtime exercise, what unchanged runtime facts or approved equivalence basis support that posture:**  
* **Required for closure:**  
* **Notes:**

**Repeat path and surface blocks as needed.**

**Closure Decision**

* **Epic closure decision:**  
* **Decision scope and PO-action boundary:** state whether the decision is a review-trace conclusion, PO closeout action, later-drain recommendation, or another bounded posture.  
* **Completion-axis separation:** state repo-supported completion, canon-drain completion, formal close-pack completion, merge provenance, board state, PO closeout action, and formal ops action as claimed, not claimed, deferred, or not applicable.  
* **Why this decision is supported:**  
* **Current PF09 or other canon recorded status, if relevant:**  
* **Actual implemented state:**  
* **Actual OPS state, if applicable:**  
* **Actual governed evidence state:**  
* **Auditability caveat, if any:** say whether the decisive primary-source close-authority statement provides direct evidence-pointer lines or evidence-basis prose only. If only evidence-basis prose is available, record that explicitly and identify the governed evidence clusters used to support the closure conclusion.  
* **Documentation-drain posture:** state whether any PF10 or PF-canon drain remains, name the intended drain targets by title, and say explicitly whether the later drain is only follow-up work or already drained; if the current verdict relies on undrained live truth, use supportable-versus-drained wording explicitly.  
* **Follow-up-only items that do not block closure, if any:** include remaining drain targets and doc-delta candidates here when required QA, implementation state, OPS state, and governed evidence already support closure. Documentation drainage itself is follow-up work, not a closure blocker.  
* **Minimal follow-ups required only if not satisfied:** list only real truth-and-proof blockers that prevent closure, such as incomplete required QA steps, missing required deliverables, untrusted or non-governed evidence, unresolved FAIL\_BEHAVIOR / FAIL\_TOOLING / TOOLING\_BLOCKED conditions that affect acceptance, or missing required close-gate QA artifacts.

**Later-Drain PF-Canon Update (required when this review supports later PF-canon drainage)**

* **Affected PF canon home(s):**  
* **Exact affected locator(s):**  
* **Current canon posture:**  
* **Supported later-drain action: change to Done | change to Partial | change to Not done | change to Consolidation pending | change to Optional | No status change recommended**  
* **Drain readiness classification: Supportable from repo evidence | Not yet supportable from repo evidence | Already drained into PF-canon**  
* **Evidence basis:**  
* **Epic-close expectation: at epic close | after an additional PR or OPS slice | after a separate canon-only drain step**

**Retrospective — Executive Summary**

* **Scope and contract-preservation summary:**  
* **Delivered implementation summary:**  
* **Biggest wins:**  
* **Biggest remaining risks or gaps:**

**Implementation Report**

**IR-001**

* **PR or slice label:**  
* **Purpose:**  
* **Key changes:**  
* **Key surfaces touched:**  
* **Tests or evidence produced:**  
* **QA steps and closeout evidence:** state Step-0, QA step groups, accepted remediation loops, final PASS or blocked posture, and closeout deliverables such as manifest, discovery artifact, QA RCA / Doc Delta summary, and path proofs when reviewed.  
* **Outcome:**  
* **Evidence pointer:**

**Repeat implementation-report blocks as needed.**

**Implementation Report — Cross-slice summary (required when the review covers more than one PR, OPS task, or QA step)**

* **Major surfaces affected:**  
* **Evidence inventory:**  
* **Docs-only or repo-docs sweep evidence, if used:** state touched docs, repo-proof method, validation checks, scope-limiting proof, and whether the docs sweep is PF10-recorded, close-pack-summarized, or non-PF provenance only.  
* **Evidence gaps or caveats:**  
* **Evidence pointer(s):**

**Closure Evidence Snapshot**

* **Evidence produced:** list only governed artifacts, PR evidence, docs sweep evidence, indexes, mirrors, path proofs, and validation outputs actually verified by the review.  
* **Evidence missing or ambiguous:** list every closure-relevant artifact or proof family that was not verified, why it matters, what would prove it, and where that proof should exist if known.  
* **Open closure items or questions for the Lead:** list decisions still required before PO closeout, including close-pack baseline existence, Live QA close-gate evidence, PF09.x drain state, parent-row status action, docs-sweep historical capture, or deferred work visibility when applicable.

**Retrospective — Process**

* **What went well:**  
* **What did not go well:**  
* **What we learned:**

**Retrospective — Application / System**

* **What we learned about the system:**  
* **Known remaining risks or debt:**

**ADRs and Ambiguity Resolution**

**ADR Overview (required when multiple ADRs or cleaned dispositions are reviewed)**

ADR-SUM-001

* ADR:  
* Related finding:  
* Cleaned disposition: New staging decision required | Existing PF10 coverage | Permanent PF-Canon already governs | New rule required | No ADR needed | Other  
* Current action:  
* Whether this becomes a template or canon rule: Yes | No  
* Evidence pointer:

Repeat ADR summary rows as needed.

**ADR-001**

* **Decision point:**  
* **Options considered:**  
* **PF-canon constraints relied on:**  
* **Proof excerpt(s) when canon is invoked:**  
* **ADR tag, if recorded:** NEW CANON PROPOSAL | CLARIFICATION | CONSISTENCY | DOC HYGIENE | DELETION | other evidence-backed tag  
* **ADR proposal text, if recorded:**  
* **Final decision for this epic:**  
* **Should this become canonical for future work:** Yes | No  
* **Evidence pointer:**

**Repeat ADR blocks as needed.**

**Canon Alignment and Documentation Outcomes**

* **Canon references used:** list current PF homes or source artifacts actually used, and the scope of use for each.  
* **Non-PF documentation or docs-sweep sources used only as provenance:** state whether they affect closure authority or only report history.  
* **New PF10 addenda proposed:** Yes | No  
* **If no new addenda are proposed:** state which existing addenda already stage the material canon or status actions, if any.  
* **Evidence pointer(s):**

**PF-Canon Doc Deltas**

* **None:** state when no PF-Canon doc delta is required, and provide evidence pointer(s) or negative-claim proof when the reviewed source says none.

**DD-001**

* **Doc:**  
* **Section:**  
* **Delta:**  
* **Tag:** NEW CANON PROPOSAL | CLARIFICATION | CONSISTENCY | DOC HYGIENE | DELETION | other evidence-backed tag  
* **Proof excerpt(s) when canon is invoked:**  
* **Why this doc is the correct home:**  
* **Evidence pointer:**

**Repeat doc-delta blocks as needed.**

**Build Improvements and Future Work**

**FW-001**

* **Short description:**  
* **Where it should live:**  
* **PF docs to reference or update if pursued later:**  
* **PF23 dependency: Yes | No**  
* **If Yes, state the gap, anchor, or why the dependency matters:**

**Repeat future-work blocks as needed.**

**Recommendation only**

* **Implementation posture recommendation:**  
* **Strongest implementation evidence:**  
* **Strongest QA evidence:**  
* **Why the recommendation is supported:**  
* **Most important policy improvement to preserve:**  
* **Most important process improvement to preserve:**  
* **Caveats or follow-ups that remain outside the recommendation:**  
* **ADRs that should be memorialized in PF-Canon:**  
* **No-hard-blocker statement:**  
* **Distinct remaining actions: PO closeout | PF09.x drainage | canon maintenance | other**

## **11\) Ops Task Final Review Record (Template; REVIEW mode only)**

### **Scope**

**Use this template when a completed Ops task, ops remediation rerun, or other bounded PO-executed ops slice must be reviewed against an approved Ops Task Record, approved plan, or approved remediation scope. It is review-only: it determines whether the run stayed within approved scope, whether the required governed outputs and environment or binding dispositions were captured truthfully, whether the result is acceptable for downstream binding or follow-on work, and what later PF-canon drain posture is supported when the review is intended to feed canon drainage. It does not create new runbooks, new commands, or new acceptance tokens.**

### **Required structure (paste-ready)**

**Review Summary**

* **Ops task or run label:**  
* **Approved task or plan source:**  
* **What actions were performed:**  
* **Environment or binding disposition, if applicable:**  
* **Whether the run stayed within approved scope:**  
* **Whether deliverables and evidence are sufficient:**  
* **Remaining operational risk, if any:**  
* **Downstream binding or follow-on use, if any:**

**Task Boundary and Closure Claim Posture**

* **Run posture:** state-changing ops run | read-only validation run | classification-only run | evidence-refresh-only run | discovery-only run | controlled vendor smoke  
* **External execution classification, if applicable:** CLI-local smoke | hosted-service operation | vendor-backed smoke | discovery only | not applicable | other approved classification  
* **Does the approved ops task itself claim PF09 or canon closure now:** Yes | No  
* **If command discovery is the approved purpose, what command-proof result was reached:** concrete command proven | unresolved sentinel recorded | blocked by missing target facts | not applicable  
* **If blocker classification is the approved purpose, what classification result was reached:**  
* **If No, what bounded purpose is being accepted:**  
* **If No, what still-open state must remain explicit:**  
* **If No, which later approved task or step owns remaining closure work, if any:**  
* **Command ledger and checksum evidence:** state whether every action actually performed is recorded and whether checksum or integrity evidence covers the captured files.  
* **Row-level closure proof for corpus, parity, or multi-row closure claims:** state the active corpus or row inventory, any excluded or skipped rows, row-level status for each active row, the closure decision artifact, the consistency-check result, and whether the consistency result agrees with the row-level proof.  
* **Scope-rationale evidence when corpus interpretation was contested or remediated:** state the authority or rationale used, whether the run resolved the issue through inclusion and match or through exclusion, and whether any external exclusion authority remains necessary.  
* **Secret and environment evidence posture:** presence-only booleans | redacted | hashed | not applicable; state whether any secret-value persistence is evidenced.  
* **Non-claims preserved:** QA PASS | Live QA completion | PF09 status change | epic closure | PF-canon drain completion | other  
* **Evidence-packaging or close-pack surfacing scope:** when run posture is evidence-refresh-only, evidence packaging, or close-pack surfacing, verify that no QA reruns, vendor calls, implementation changes, PF-Canon edits, PF09 status-drain claims, new acceptance claims, or new tokens occurred unless the approved task explicitly authorized them.  
* **Remediated evidence-packaging proof set:** when accepting a repaired Ops evidence bundle, Evidence Print must cover the corrected command transcript, labeled stdout, labeled stderr, labeled exit-code ledger, final inventory, inventory path-proof, final validation log, close-pack manifest `key_outputs` bindings when present, close report and manifest path proofs when present, checksum ledger, and any superseded artifacts preserved for audit.  
* **Final validation posture:** a narrative completion statement is not enough; the review must identify the executable validation output that reconciles file existence, manifest, close report, path-proofs, final inventory, checksum ledger, and Ops evidence files for the approved scope.  
* **Later-drain posture:** if the task only surfaces close-pack or drain-target evidence, the review must record `No status change recommended` or `Not yet supportable from repo evidence` for PF09.x status changes unless the approved task also proves the exact PF09.x row-status predicate.  
* 

**Findings**

**FND-001**

* **What I observed:**  
* **Why it matters:**  
* **Expected requirement from the Approved Plan:**  
* **Blocker for acceptance: Yes | No**  
* **Evidence pointer(s):**

**Repeat finding blocks as needed.**

**Evidence Print (PASS PROOF; required)**

**A) Required deliverables satisfied**

* **Deliverable name:**  
* **Evidence pointer:**  
* **Key proof facts:**

**Repeat deliverable lines as needed.**

**B) Commands/actions evidence**

* **Action:**  
* **Evidence pointer:**  
* **Success signal found in evidence:**

**Repeat action lines as needed.**

**C) Configuration/infra state evidence (if applicable)**

* **Evidence pointer:**  
* **What state it proves:**

**D) PF09.x later-drain support (if applicable)**

Use this section only when the approved Ops task ties the run to PF09.x completion, close, or later-drain posture.

* **PF09.x document:**  
* **PF09.x task ID:**  
* **PF09.x subtask ID, if any:**  
* **Current claim in the approved task or plan:**  
* **Supportable later-drain action:** no PF09.x support proven | supportable from Ops evidence only | supportable after PR/QA/closeout binding | supportable from repo evidence | already drained | not applicable  
* **Evidence basis:**  
* **Non-claim notes:** state whether the Ops run avoids QA PASS, PF09 status move, epic closure, acceptance-token satisfaction, or other overclaim.  
* **Later owner:** state whether later PR, QA, closeout, or canon-only drain work owns any status movement.

**Repeat state-evidence lines as needed.**

**Decision**

* **Decision:**  
* **Why this decision is supported:**  
* **Remaining risk or not-yet-closed state, if any:**  
* **Supported downstream binding or follow-on use, if any:**

**Later-Drain PF-Canon Update (required when this review supports later PF-canon drainage)**

* **Affected PF canon home(s):**  
* **Exact affected locator(s):**  
* **Current canon posture:**  
* **Supported later-drain action: change to Done | change to Partial | change to Not done | change to Consolidation pending | change to Optional | No status change recommended**  
* **Drain readiness classification: Supportable from repo evidence | Not yet supportable from repo evidence | Already drained into PF-canon**  
* **Evidence basis:**  
* **Epic-close expectation: at epic close | after an additional PR or OPS slice | after a separate canon-only drain step**