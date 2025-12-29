# 0\) Front Matter

**Name:** PF10-HDE-Build-Notes   
**Version:** v8.7.2  
**Status:** Living  
**Invocation tag:** INV-f2ac55d77ce9aacc

## Purpose

This file is a **working scratchpad for new, not-yet-merged documentation**. Treat it as the current source of truth **only for the specific items it explicitly covers**. For everything else, PF-Canon (PF01, PF02, PF04, PF05, PF09, PF12, PF14, PF19, PF20, etc.) remains the single home.

---

**Precedence and versioning**

* For any topic explicitly covered in this scratchpad, its content **temporarily supersedes canon** until those changes are reviewed and merged into the relevant PF docs.

* If multiple addenda exist for the same or similar scope (for example “1.”, “2.”, “ 3.”), the **highest-numbered / latest addendum is the only authoritative one**.

* **Older scratchpad files are considered fully drained or obsolete.** Agents must **not** read, reuse, or reconcile content from older scratchpads once a newer one exists; only the latest file matters.

Within a single scratchpad file:

* When an entry has been drained into PF-Canon, that entry is **removed completely** from the scratchpad.

* The current version of the file therefore contains **only live, not-yet-merged items**. If a topic is not present in the latest scratchpad, assume its source of truth is the relevant PF-Canon doc.

## Cross-references

 Inside this file, all references to PF documents MUST be **titles-only** (for example “HDE-Phased Epics”, “Glow QA Guide”), never file names or version numbers in the body text.

When editing or extending this file, ChatGPT sessions must:

* Not restate PF content here.

* Link by **document title and section only**.

# 1\) TEMPLATE

TEMPLATE Addendum Entry (do not edit/remove)

##   \<number\>. \<short, action-oriented title\>

 Timestamp: \<mmddyy hh:mm\>  
 Details: \<specific information to drain to canon, its origin, and any evidence available\>

## Addendum Index:

**This section should be considered current and authoritative. Index all addenda numbers listed below.**

1. 2.1 \- Token Registry SoT enforcement for PF20 epic rosters  
   2. 2.2 \- Acceptance tokens: PF04 registry vs PF19 QA token library (single SoT)  
   3. 2.3 \- Live QA plan approval gate: PF19 lint \+ token SoT validation \+ mechanical-only evidence  
   4. 2.4 \- Review source-retrieval guard: no excerpt-based claims for tokens/rails/bytes  
   5. 2.5 \- Showcompat checksum sidecar filename normalization for EPIC022  
   6. 2.6 \- Identity artifact checksum sidecars are optional helper artifacts (unless explicitly required)

   7. 2.7 \- EPIC022 Token Registry Bridge for Live QA

   8. 2.8 \- EPIC022 — Release ID evidence paths (canonicalize and drain drift)

   9. 2.9 \- EPIC022 internal\_version evidence filenames bridge

   10. 2.10 — Live QA Planning: Blockers-Only Approval \+ Caveats Channel (Slim Gate)

   11. 2.11 — Token Load Reduction: Tokens Are Not a Plan-Approval Gate (≥30% Reduction by Default)

   12. 2.13 — PF10 Reference Posture: Treat Build Notes as Living (No Version/Section “Anchoring”)

   13. 2.12 — PF20 Error Tolerance for Live QA Execution: “Proceed on Repo Reality, Record Doc Delta”

   14. 2.14 \- No non-canonical QA scripts or wrappers in Live QA plans (baseline commands only)

   15. 2.15 \- QA STEP 0A executed successfully   
   16. 2.16 \- QA STEP 0B executed  
   17. 2.17 \- QA STEP 0C was executed  
   18. 2.18 \- QA STEP 0D executed the Approved Plan’s token-roster validator  
   19. 2.19 \- QA Revised STEP D0.1 passes  
   20. 2.20 \- Revised STEP D0.2 is acceptable: the determinism pins evidence file exists  
   21. 2.21 \- Live QA Rails: No Non-Canonical Env Pins (PYTHONHASHSEED is not a required pin)  
   22. 2.22 \- QA Revised STEP D0.2 is acceptable with caveats.  
   23. 2.23 — EPIC022 — Freeze-Pack Manifest evidence-copy semantics \+ release\_id recompute contract (no dual semantics)  
   24. 2.24 \- HDE-EPIC022 Remedial PR1

   25. 2.25 \- HDE-EPIC022 Remedial PR2

   26. 2.26- HDE-EPIC022 Remedial Docs PR  
   27. 2.27 \- QA Revised STEP D0.3 is acceptable:  
   28. 2.28 \- QA STEP D2.1 meets the Approved Plan requirements and passes  
   29. 2.29 \- Ops tasks: PO-only execution (IA-guided), not Codex PRs  
   30. 2.30 — Remediation Implementation Guides are DEV/OPS-only (verification embedded)  
   31. 2.31 — Canonical Remediation Implementation Guide template (dependency-line rule locked)

   32. 2.32 — ADR-003 deferred: /internal/version auth posture is not yet canonized

   33. 2.33 — `/internal/version` acceptance token names are canonical and non-aliasable

   34. 2.34 — /internal/version proof surface: invariant checklist must be explicit and gated before “OK” tokens

   35. 2.35 — Planning MUST consult PF23 Reality Audits (components \+ pathnames)

   36. 2.36 — Canonical Remediation Task Plan Template \+ “Execution-Ready” Gate.

   37. 2.37 — Remediation Plan “Exact Filenames” Rule for Evidence Index \+ Path Proof Artifacts

   38. 2.38 — Portability vs Provenance: How to Reference Non-PF Evidence Without Creating Execution Dependencies

# 2\) Numbered Addendum List

## **2.1 \- Token Registry SoT enforcement for PF20 epic rosters**

 Details:  
 This addendum resolves ongoing acceptance-token drift between epic planning records and the canonical token registry by explicitly enforcing a single-source-of-truth model.

Policy:

1. The canonical Token Registry and token semantics live only in **HDE-Governance §2.0**.

2. Token lists in **HDE Phased Epics** are names-only planning rosters and MUST be a validated view of the Token Registry, not an authority.

3. Any token name present in an epic record acceptance roster MUST exist in the Token Registry and match spelling exactly. Aliases and near-matches are prohibited; fix the epic roster to the canonical name. (See HDE-Governance §9.7.10.)

4. If an epic truly needs a new token, it MUST be routed through an ADR (name, invariant, intended evidence surface(s), drain targets) and then registered in the Token Registry before it can appear as a required token in an epic record or acceptance artifacts. (See HDE-Governance §9.7.10 and HDE-Governance §2.0.)

5. Until drift is cleared, use the cross-epic tracker reserved in **HDE Phased Epics §1** (token registry drift issue record) as the single umbrella issue; do not create competing local “token lists” in other PF docs.

Drain targets (titles-only):

* HDE-Governance (Token Registry and preflight validation rules)

* HDE Phased Epics (epic record wording to clarify “validated view” posture)

* HDE Schemas & Artifacts (if any evidence-binding tooling needs to reference the registry in a deterministic way)

* Glow QA Guide (if QA checklists need a named “token roster validation” check in Live QA posture)

## **2.2 \- Acceptance tokens: PF04 registry vs PF19 QA token library (single SoT)**

Timestamp: \<mmddyy hh:mm\>  
 Details: This addendum clarifies the single source of truth boundaries when “QA tokens” appear to live in multiple PF documents.

**Policy (normative):**

1. **PF04 is the single source of truth for acceptance token names and semantics.**  
    All acceptance token names and their semantics are defined once in the governance registry and are referenced elsewhere by exact name.  
    Canon: PF04 — HDE-Governance, §2.0; PF04 — HDE-Governance, §2.0.18.

2. **PF19 is the canonical home for the QA operational token library, not the governance roster.**  
    PF19 may contain extensive QA-facing guidance for tokens (metadata, wiring, runbook mapping, evidence expectations), but it MUST reference token names exactly as defined in PF04 and MUST NOT introduce new or divergent meanings.  
    Canon: PF04 — HDE-Governance, §2.0.18; PF19 — Glow QA Guide, §9.2; PF19 — Glow QA Guide, §9.2.2.

3. **“Mirroring” rule: names MUST match, operational guidance does not need to mirror.**  
    PF19 does not need to duplicate PF04’s full governance semantics. It may carry QA operational details. The only strict mirroring requirement is that any token name used in PF19 is a PF04-registered token name, spelled exactly.  
    Canon: PF04 — HDE-Governance, §2.0.18; PF19 — Glow QA Guide, §9.2.

4. **PF20 epic acceptance rosters are names-only consumers and must validate against PF04.**  
    Any acceptance token named in an epic record MUST be present in PF04 and match spelling exactly. PF20 may reference PF19 for execution guidance by title and section, but it must not introduce new token names, aliases, or synonyms.  
    Canon: PF20 — HDE-Phased Epics, §2.1.8; PF04 — HDE-Governance, §2.0.18.

5. **No midflight token invention in QA plans or Live QA.**  
    If a QA plan encounters a token name present in PF19 or PF20 that is absent from PF04, the plan MUST treat it as a blocker and record it as token drift. The plan MUST NOT invent substitute token names.  
    Canon: PF19 — Glow QA Guide, §9.2.15.4; PF04 — HDE-Governance, §2.0.18.

6. **New QA acceptance tokens require governance registration first.**  
    Any new QA acceptance token required by PF19’s QA library must first be added to the PF04 acceptance token roster (via the governance doc-delta process) before it can be used in PF19, PF20, acceptance maps, or QA evidence logs.  
    Canon: PF04 — HDE-Governance, §2.0.18; PF19 — Glow QA Guide, §9.2.10.

**Drain targets (titles-only, stable anchors):**

* PF04 — HDE-Governance, §2.0.18

* PF19 — Glow QA Guide, §9.2; §9.2.15.4

* PF20 — HDE-Phased Epics, §2.1.8

* PF12 — HDE-Schemas and Artifacts, §8.6

## **2.3 \- Live QA plan approval gate: PF19 lint \+ token SoT validation \+ mechanical-only evidence**

**Timestamp:** 122525 00:00

**Details:** This addendum makes Live QA plan approval deterministic by turning existing canon expectations into an explicit approval gate. It is intended to prevent multi-iteration churn caused by non-executable steps, token drift, and non-conforming “evidence artifacts.”

### **Policy (normative)**

1. **A Live QA plan is not approvable unless it is directly executable in Codespaces (copy/paste discipline).**  
    All operator-run steps must be copy/paste-ready and must not rely on narrative pseudo-shell. If a step includes script content, it must be provided in a way that results in a syntactically valid file when executed.  
    Canon: PF19 — Glow QA Guide, §3.4.

2. **Gitless Live QA is mandatory for the runbook itself.**  
    Live QA runbooks must not include git gating (including “working tree clean” checks) as PASS/FAIL criteria. If traceability capture is needed, it must be artifact-only and non-blocking.  
    Canon: PF19 — Glow QA Guide, §3.4.

3. **Mechanical-only evidence posture is mandatory. No manual-fill placeholders in any QA evidence file.**  
    Any file treated as QA evidence (including close artifacts) must be mechanically produced from commands and must not contain “fill in PASS/FAIL” or similar placeholders. If a result is “no deltas,” the artifact must say so explicitly (as a produced output, not an instruction).  
    Canon: PF20 — HDE-Phased Epics, §2.7.6; PF19 — Glow QA Guide, §14.6.

4. **Codespaces Live QA plans must include Step‑0 Codespaces Snapshot \+ Doc Delta Capture.**  
    Codespaces Live QA must produce the required snapshot evidence and must include a Doc Delta Capture step that records missing/ambiguous prerequisites discovered during planning, including explicit “no deltas” when none are found.  
    Canon: PF19 — Glow QA Guide, §14.4; PF19 — Glow QA Guide, §14.6.

5. **Acceptance tokens: PF20 is the epic acceptance roster; PF04 is the token registry. Plans may not invent tokens.**

   * The plan’s token roster for the epic must be sourced from the epic’s acceptance section.

   * Any token claimed by the plan must exist in the token registry (names \+ semantics).

   * If the epic acceptance roster references a token not present in the registry, the plan must treat this as a canon gap (recorded in Doc Delta Capture) and must not substitute a new token name.  
      Canon: PF20 — HDE-Phased Epics, §2.7.5; PF04 — HDE-Governance, §2.0; PF19 — Glow QA Guide, §14.6.

6. **Step logs must use the canonical status vocabulary and must separate tooling failure from behavior failure.**  
    Step logs must use the stable status set (and must not introduce ad-hoc “review statuses” for core execution state).  
    Canon: PF19 — Glow QA Guide, §4.4.

### **Approval rule**

A plan that violates any item above must be rejected for approval until corrected (this is not discretionary).

---

## **2.4 \- Review source-retrieval guard: no excerpt-based claims for tokens/rails/bytes**

**Timestamp:** 122525 00:00

**Details:** This addendum exists to prevent review defects caused by asserting canon contradictions without fully retrieving the relevant canonical passage (especially token rosters, rails rules, and byte/CLI contract expectations).

### **Policy (normative)**

1. **No excerpt-based claims about token rosters.**  
    A reviewer may not claim “token list incomplete,” “wrong tokens,” or “token semantics mismatch” unless they have fully retrieved:

   * the epic token roster section, and

   * the relevant token registry entries (for any token they claim is missing/mismatched).  
      Canon anchors for what must be consulted: PF20 — HDE-Phased Epics, §2.7.5; PF04 — HDE-Governance, §2.0.

2. **No excerpt-based claims about Live QA rails posture or evidence posture.**  
    A reviewer may not claim a rails/evidence rule violation unless they have fully retrieved the governing rails/evidence rule passage being referenced.  
    Canon anchors: PF19 — Glow QA Guide, §3.4; PF19 — Glow QA Guide, §4.4; PF20 — HDE-Phased Epics, §2.7.6.

**Addendum Draft 1 — EPIC022 Token Registry Bridge for Live QA**

* **Decision statement (normative)**

  * For **HDE-EPIC022 Live QA planning and evidence**, the **acceptance token roster remains PF20**, but **token claim validity is gated by PF04**.

  * Any token present in **PF20 — HDE-Phased Epics, §2.7.5** but absent from **PF04 — HDE-Governance, §2.0** is classified as **UNREGISTERED\_ACCEPTANCE\_TOKEN** for this epic until drained.

  * Live QA plans **must not claim** UNREGISTERED\_ACCEPTANCE\_TOKEN tokens in step logs; they must be recorded in **Doc Delta Capture** as a blocking canon gap (no substitution/renaming allowed).

* **Clarifications**

  * Evidence collection may proceed, but acceptance token claims remain blocked until registry drain.

* **Drain targets (titles-only)**

  * PF04 — HDE-Governance

  * PF20 — HDE-Phased Epics

  * PF19 — Glow QA Guide

* **Evidence**

  * None (policy addendum)

## 2.5 \- Showcompat checksum sidecar filename normalization for EPIC022

* **Decision statement (normative)**

  * For **showcompat evidence artifacts**, the canonical checksum sidecar naming is `stdout.json.sha256` (JSON-filename-qualified).

  * For **HDE-EPIC022 D2**, emit **both**:

    * canonical: `stdout.json.sha256`

    * legacy alias: `stdout.sha256`

  * Evidence indexing must reference the canonical name; the alias exists for backward compatibility until PF20 is drained.

* **Clarifications**

  * The alias must be mechanically derived from the same bytes as the canonical checksum sidecar.

* **Drain targets (titles-only)**

  * PF20 — HDE-Phased Epics

  * PF12 — HDE-Schemas-and-Artifacts

* **Evidence**

  * None (naming normalization)

## 2.6 \- Identity artifact checksum sidecars are optional helper artifacts (unless explicitly required)

* **Decision statement (normative)**

  * For **identity artifacts** under `audit/qa/<epic-id>/artifacts/identity/`, `.sha256` sidecars for JSON files are **optional helper artifacts** unless the epic acceptance section explicitly lists them as required.

  * EPIC022 acceptance for D0 requires the identity JSON \+ verify logs; checksum sidecars may be produced but **must not be used as gating** unless added to acceptance canon.

* **Clarifications**

  * If produced, checksums must be generated mechanically (`sha256sum`) and included in evidence indexing as helper artifacts.

* **Drain targets (titles-only)**

  * PF20 — HDE-Phased Epics

  * PF12 — HDE-Schemas-and-Artifacts

* **Evidence**

  * None (policy clarification)

## 2.7 \- EPIC022 Token Registry Bridge for Live QA

* **Decision statement (normative)**

  * For **HDE-EPIC022 Live QA planning and evidence**, the **acceptance token roster remains PF20**, but **token claim validity is gated by PF04**.

  * Any token present in **PF20 — HDE-Phased Epics, §2.7.5** but absent from **PF04 — HDE-Governance, §2.0** is classified as **UNREGISTERED\_ACCEPTANCE\_TOKEN** for this epic until drained.

  * Live QA plans **must not claim** UNREGISTERED\_ACCEPTANCE\_TOKEN tokens in step logs; they must be recorded in **Doc Delta Capture** as a blocking canon gap (no substitution/renaming allowed).

* **Clarifications**

  * Evidence collection may proceed, but acceptance token claims remain blocked until registry drain.

* **Drain targets (titles-only)**

  * PF04 — HDE-Governance  
  * PF20 — HDE-Phased Epics

  * PF19 — Glow QA Guide

* **Evidence**

  * None (policy addendum)

## 2.8 \- EPIC022 — Release ID evidence paths (canonicalize and drain drift)

**Decision statement (normative)**

* EPIC022 release-id evidence is canonical at `artifacts/math/release_id.txt` and `artifacts/math/release_id_recompute.log`.

* Any EPIC022 references to `audit/gates/release/release_id.txt` are deprecated and must not be used for evidence indexing or close-pack checks.

**Clarifications**

* If a gate requires `audit/gates/release/…` during transition, it must be produced as a mechanically generated copy sourced from `artifacts/math/…` (no manual editing), and the plan must index the canonical source path.

**Drain targets (titles-only)**

* PF20 — HDE-Phased Epics

* PF12 — HDE-Schemas and Artifacts

* PF27 — Plan-Templates

* PF09 — HDE-Build Checklist

**Evidence**

* none

## 2.9 \- **EPIC022 internal\_version evidence filenames bridge**

**Addendum title:** EPIC022: internal\_version evidence filenames (canonical \+ permitted aliases)

**Decision statement (normative):**

* EPIC022 Live QA **MUST** produce the internal\_version evidence bundle using the **canonical filename set** registered in **PF12 — HDE‑Schemas and Artifacts** (body JSON, sha sidecar, GET/HEAD headers, conditional header snapshots, two\_run\_identity log).

* EPIC022 Live QA **MAY** additionally emit **explicitly defined alias copies** of the conditional header snapshot files to satisfy the EPIC022 acceptance binding naming in **PF20 — HDE‑Phased Epics** and the internal\_version bundle naming in **PF04 — HDE‑Governance**.

* No other filename variants are permitted (explicitly: do **not** introduce ad‑hoc sha/headers filenames outside the canonical set \+ the named alias set).

**Clarifications:**

* Evidence indexing keys should continue to map to the canonical PF12 filenames; alias files are compatibility-only.

**Drain targets (titles-only):**

* PF12 — HDE‑Schemas and Artifacts

* PF20 — HDE‑Phased Epics

* PF04 — HDE‑Governance

* PF19 — Glow QA Guide

**Evidence:** none (this addendum governs filenames/aliases; the evidence is the resulting files)

## **2.10 — Live QA Planning: Blockers-Only Approval \+ Caveats Channel (Slim Gate)**

Timestamp: 122625 00:00

**Details**  
 Live QA planning has been failing via repeated revise/resubmit loops because review findings that do **not** prevent functional verification have been treated as **Blockers** (token ledger completeness, template strictness beyond execution needs, documentation drift that does not stop tests from running). This addendum redefines the approval gate so only execution/verification blockers block.

**Policy (normative)**

1. **Blocker definition (Live QA planning / plan approval):** A “Blocker” is **only** an issue that prevents the PO from executing the plan **or** prevents the reviewers from determining pass/fail for the in-scope feature behavior with confidence.  
    Examples: missing required PO inputs (base URL/auth), commands not runnable, missing pass/fail criteria, evidence capture not specified, plan requires production code changes, plan depends on manual-fill placeholders for outputs/evidence. (Glow QA Guide, §3.4 “Plan validity lint”; Plan Templates, §6.0–§6.5)

2. **Everything else is a Caveat, not a Blocker.**  
    Any issue that does **not** affect functional execution and verification MUST be recorded as a **CAVEAT** item (tracked), not a Blocker.  
    Examples: incomplete token rosters in the plan, token registry mismatch, template formatting imperfections that don’t obstruct execution, doc drift that can be captured via doc-delta. (Glow QA Guide, §3.4)

3. **Review outcomes:**  
    *If and only if there are Blockers →* plan is rejected for revision.  
    *If there are no Blockers →* plan is approved **even if Caveats exist**.  
    This implements “pass with caveats” **without** inflating revision cycles.

4. **Required structure in reviews:**  
    Review outputs MUST separate findings into:

   * **BLOCKERS (must fix before execution)**

   * **CAVEATS (may fix during QA / drain later)**  
      Blockers get stable IDs (e.g., BLK-01). Caveats get stable IDs (e.g., CAV-01). Only Blockers force resubmission.

**Conflict note (explicit override)**  
 If any template/checklist/process language causes non-execution issues to be treated as Blockers, this addendum overrides it for **Live QA plan approval**. (Plan Templates, §6.3; Glow QA Guide, §3.4)

**Drain targets (titles-only)**

* Glow QA Guide

* Plan Templates

* Epic Process Guide

**Evidence**  
 None.

---

## **2.11 — Token Load Reduction: Tokens Are Not a Plan-Approval Gate (≥30% Reduction by Default)**

Timestamp: 122625 00:00

**Details**  
 Token enumeration and token-ledger policing has become a dominant source of planning churn without improving functional verification. Tokens remain useful as acceptance indexing, but they must not bloat Live QA planning or block functional testing.

**Policy (normative)**

1. **Token load reduction requirement (planning):**  
    Live QA plans MUST reduce explicit token handling by design. The default posture is:

   * **No per-step token claims required.**

   * **No full token roster required in the plan body.**  
      This achieves **≥30% reduction** automatically (typically far more) by eliminating token-ledger repetition as a planning prerequisite. (Acceptance Tokens single-home \+ “non-token metadata”; HDE-Governance, §2.0.0)

2. **What a Live QA plan MUST use instead of token-ledger verbosity:**  
    Plans MUST map steps to **in-scope surfaces/flows \+ D-goals** (feature behavior) and define evidence capture and pass/fail criteria. Tokens remain an optional indexing layer, not the plan’s backbone. (HDE-Phased Epics, §2.7.x D-goals structure; Glow QA Guide, §3.4)

3. **If tokens are listed in a Live QA plan:**

   * They MUST be names-exact and registry-valid for anything claimed as acceptance. (HDE-Governance, §2.0)

   * Partial token lists are allowed and MUST NOT be treated as a plan approval Blocker (see 2.9).

   * Missing token semantics or mismatched token naming is handled as a Caveat unless it prevents determining functional pass/fail.

4. **PF20 vs registry drift handling (streamlined):**  
    If an epic roster or QA doc references a token name that is not present in the Token Registry, do **not** block functional QA.

   * Treat as **CAVEAT: UNREGISTERED\_TOKEN**

   * Do **not** claim the token for acceptance until it is registered.

   * Continue executing tests and capturing evidence normally. (HDE-Governance, §2.0.0 “Registry enforcement”; HDE-Phased Epics, §2.7.5.\* token rosters)

**Conflict note (explicit override)**  
 This overrides any Live QA plan-template posture that makes “token roster validity” a *preflight Blocker* for plan approval, except where token validity is required to interpret pass/fail for a specific test. (Plan Templates, §6.3)

**Drain targets (titles-only)**

* Plan Templates

* Glow QA Guide

* HDE Phased Epics

* HDE Governance

**Evidence**  
 None.

---

## **2.12 — PF20 Error Tolerance for Live QA Execution: “Proceed on Repo Reality, Record Doc Delta”**

Timestamp: 122625 00:00

**Details**  
 When PF20 (or any acceptance roster) contains incorrect or stale operational details (paths, filenames, command shapes), strict enforcement at planning time blocks execution without improving functional confidence. Live QA must remain executable and evidence-producing.

**Policy (normative)**

1. **Behavior \> bookkeeping:**  
    For Live QA, the primary objective is verifying in-scope behavior (“features work as expected”) via runnable checks \+ evidence. Documentation correctness is secondary and must not stop execution unless it breaks the ability to run or verify. (Glow QA Guide, §3.4)

2. **Repo reality precedence for execution details:**  
    If PF20’s operational details conflict with repo reality (exact file paths, exact script locations, exact CI job names), QA MUST:

   * Use the repo-real invocation/paths to run the checks and capture evidence

   * Record the mismatch as a **CAVEAT: DOC\_DRIFT** for later drain

   * Do not block execution unless the mismatch prevents knowing what to run or how to verify. (Glow QA Guide, §3.4)

3. **Evidence posture remains non-negotiable:**  
    Even when proceeding on repo reality, evidence MUST still be captured under `audit/qa/...` (lowercase) with explicit filenames sufficient to support later audit. If naming differs from PF20 conventions, record the naming difference as a Caveat (not a blocker) unless it prevents retrieval/traceability. (Glow QA Guide, §3.4; Plan Templates, §6.2)

**Drain targets (titles-only)**

* HDE Phased Epics

* Glow QA Guide

* Plan Templates

**Evidence**  
 None.

---

## **2.13 — PF10 Reference Posture: Treat Build Notes as Living (No Version/Section “Anchoring”)**

Timestamp: 122625 00:00

**Details**  
 Build Notes are living canon and should be referenced in a way that stays stable as the document evolves.

**Policy (normative)**

1. **Do not reference PF10 by version strings.**

2. **Prefer referencing PF10 by addendum number \+ addendum title** (e.g., “Build Notes Addendum 2.10 — Token Load Reduction…”).

3. **Do not treat PF10 section numbers as durable anchors** for external enforcement; the stable unit is the addendum entry itself.

4. **When an addendum supersedes earlier Build Notes guidance**, it must explicitly name what it supersedes (by addendum number/title).

**Drain targets (titles-only)**

* Plan Templates


* Glow QA Guide

**Evidence**  
 None.

## 2.14 \- No non-canonical QA scripts or wrappers in Live QA plans (baseline commands only)

### **Decision statement (normative)**

* **Live QA plans MUST NOT depend on helper/wrapper scripts unless the script is explicitly named by path in PF canon** (PF27 template compliance does not imply permission to invent entrypoints). (PF27 — Canon Plan Templates, §1.2)

* **If a step needs “tooling,” it MUST be either:**

  * a canon-named entrypoint by explicit path (e.g., `scripts/release_id_recompute.py`, `ci/checks/check_env_pins.sh`), or

  * an inline tool whose full source is embedded in the plan step and written into the run-local QA tools directory (no hidden dependencies). (PF10 — HDE-Build Notes, §2.3; PF10 — HDE-Build Notes, §2.12)

* **Any plan that references a non-canon script path as a “required surface” is out of spec** and must be revised to validate the governed artifact surface directly using baseline commands. (PF10 — HDE-Build Notes, §2.10)

### **Clarifications**

* This addendum **does not forbid canon-named tooling** that is already part of the HDE evidence/check discipline (e.g., evidence index updater, env pin checks, release id recompute) because those are part of the product/evidence system; it forbids *invented QA harness scripts* and *unproven helper paths*.

* “Baseline commands” means: **explicit shell/Python one-liners, direct invocation of canon tools, `tee` for logs, explicit file writes**, with no reliance on opaque runners.

* When canon is silent on an entrypoint but requires an artifact surface, the plan should implement the artifact generation **directly** (e.g., write the env pins log using the canonical schema/fields required), rather than inventing a new repo script path.

### **Drain targets**

* PF27 — Canon Plan Templates (tighten template language: step log record required, but *no wrapper dependency implied*).

* PF19 — Glow QA Guide (add a short rule under rails/evidence capture: “no invented scripts; baseline commands”).

* PF20 — HDE-Phased Epics (where acceptance text implies tool paths, restate in terms of governed artifacts unless a canon entrypoint exists).

### **Evidence**

* None (policy addendum). If desired, future compliance can be checked by a lint rule in plan review: “no `tools/qa/*.sh` unless canon-named; no opaque runner scripts.”

## 2.15 \- QA STEP 0A executed successfully 

Review Summary

* STEP 0A executed successfully and matches the Approved Plan’s Step 0A pass/fail and deliverables: the canonical Codespaces snapshot JSON exists and parses, the per-run step log exists with `status: PASS`, and the per-epic step-log manifest exists and includes the 0A record.  
* Rails posture for this step is correctly “closed rails” (SAFE\_MODE=1, ALLOW\_NETWORK=0, APP\_ENV=dev, pins set) and recorded in the step log and snapshot.  
* No deviations were reported (no deviations file present), and no evidence suggests the verification goal changed.

Findings

1. **Approved Plan Step 0A deliverables present.**  
   * `audit/qa/hde-epic022/00_meta/codespaces_snapshot.json` exists (and a copy exists under the run’s `00_meta/`).  
   * `audit/qa/hde-epic022/<run-id>/step_logs/0A_bootstrap_and_codespaces_snapshot.log` exists and records `status: PASS`, `exit_code: 0`.  
   * `audit/qa/hde-epic022/qa_step_logs_manifest.json` exists and contains an entry for check\_id `0A` with `status: PASS`.  
     This meets Step 0A’s stated PASS conditions and deliverables in the Approved Plan.  
2. **Step 0A command alignment.**  
   The step log’s recorded command is the Approved Plan’s Step 0A wrapper: run `codespaces_snapshot.py` to write the canonical snapshot under `audit/qa/hde-epic022/00_meta/` and copy it into the run’s `00_meta/`.  
3. **PF19 Codespaces snapshot minimums appear satisfied for this step’s evidence artifact.**  
   The snapshot includes tool versions, rails/pins values, prod selector presence (names-only), and secrets presence booleans (names-only), and it is written to the canonical epic meta path under `audit/qa/<epic-id>/00_meta/` as JSON.  
4. **No deviations recorded.**  
   `audit/qa/hde-epic022/step0a_deviations.md` is not present, and no PO notes/deviation notes were supplied in the bundle.

ADRs — Deviations (QA Step 0A)

* None observed. (No deviation file present; executed command and deliverables match the Approved Plan Step 0A.)

Caveats (In-Flight Determinations)

* **Caveat:** The step-log manifest format used by the plan is known to differ from PF19’s harness-run manifest structure.  
  **Owner:** Lead Dev  
  **Evidence trigger:** If later governance/token claims require PF19 harness-run manifest semantics (PF19 — Glow QA Guide, §4.4.1), confirm whether the current manifest is acceptable or must be converted by the harness.  
  **Impact if unresolved:** May block any manifest-dependent governance expectations later, even though Step 0A itself is executable and passed.  
* **Caveat:** Snapshot records `HDE_BASE_URL_is_set: false` and `INTERNAL_VERSION_AUTH_HEADER: false` at the time of Step 0A.  
  **Owner:** PO  
  **Evidence trigger:** Step 0C / D3.1 later steps will capture whether prod selector/auth are available when needed; Step 0A snapshot remains a truthful “start-of-run” record.  
  **Impact if unresolved:** Later prod-touch steps can become TOOLING\_BLOCKED; Step 0A remains valid.

Doc Deltas (PF-Canon only)

* None required for Step 0A based on this run’s evidence.

QA Verdict and Optional Follow-ups

PASS WITH CAVEATS

* Step 0A PASS is supported by the Approved Plan’s Step 0A PASS criteria and the produced artifacts.  
* The Codespaces snapshot is produced at the canonical epic meta path and is JSON (good alignment with PF19’s Step-0 requirement).  
* The manifest-format caveat is inherited from the approved plan’s known caveats; it does not invalidate Step 0A execution.

## 2.16 \- QA STEP 0B executed

Review Summary

* STEP 0B executed exactly as specified in the Approved Plan: it ran under closed rails, produced the required `doc_deltas.md`, and the Step 0B step log shows `status: PASS` with token claim `DOC_DELTA_PRESENT_OK`.  
* The required PASS predicate is satisfied: `doc_deltas.md` exists and includes the required “No other deltas…” line.  
* The per-epic step-log manifest includes a Step 0B record with `status: PASS` and the expected token claim, and no deviations were recorded for this step.

Findings

1. **Plan command alignment confirmed.** The executed command recorded in `0B_doc_delta_capture.log` matches the Approved Plan’s Step 0B wrapper: closed rails, PF refs set to `PF10 — HDE-Build Notes, §2.3; PF10 — HDE-Build Notes, §2.7`, and `--tokens "DOC_DELTA_PRESENT_OK"`.  
2. **Required deliverable `doc_deltas.md` is present and content-gated line matches.** The file exists at `${QA_ROOT}/00_meta/doc_deltas.md` and includes `## No other deltas captured at this step.` as required for PASS by the Approved Plan.  
3. **Rails posture is correct for Step 0B and captured in the step log.** The step log records `SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0`, consistent with the plan’s closed-rails posture for this step.  
4. **Manifest updated; deviations absent.** `audit/qa/hde-epic022/qa_step_logs_manifest.json` contains an entry for `check_id: 0B` with `status: PASS` and token claim `DOC_DELTA_PRESENT_OK`, and no `step0b_deviations.md` was present (consistent with “no deviations occurred”).

Doc Deltas (PF-Canon only)

* None required for Step 0B (this step is a mechanical capture step; no PF-Canon update is implied by its successful execution).

QA Verdict and Optional Follow-ups

PASS

* Step 0B meets the Approved Plan’s stated PASS condition and deliverables for doc delta capture.  
* Step 0B token handling is aligned with the Approval Doc caveat: it claims only `DOC_DELTA_PRESENT_OK` and does not introduce additional token claims.  
* The step-log manifest shows Step 0B is recorded cleanly, supporting later run-level review without needing deviations entries.

## 2.17 \- QA STEP 0C was executed 

Review Summary

* STEP 0C was executed under the **open-rails posture** required by the Approved Plan and produced all three required evidence artifacts under `audit/qa/hde-epic022/<run-id>/...`.  
* The Approved Plan’s mechanical PASS condition for Step 0C (“`prod_handshake.json` exists”) is met.  
* The captured handshake headers show **HTTP 404** for `/internal/version` on the provided base URL, which does not block Step 0C per the plan but is a meaningful signal for later steps.

Findings

1. **Step 0C artifacts are present and correctly located.**  
   * `results/prod_handshake.json` exists and is populated.  
   * `results/prod_handshake.headers` exists and contains an HTTP status line.  
   * `step_logs/0C_prod_handshake.log` exists and records `status: PASS`.  
     This matches the Approved Plan’s Step 0C deliverables list.  
2. **Rails alignment matches the Approved Plan for Step 0C.**  
   The step log records `SAFE_MODE=0 ALLOW_NETWORK=1 APP_ENV=prod LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0`, which matches the plan’s specified Step 0C rails posture.  
3. **Command alignment matches the Approved Plan.**  
   The step log shows the expected command shape: create results dir, curl headers to `prod_handshake.headers` (with timeouts), then write `prod_handshake.json` noting it is “connectivity probe only”.  
4. **Handshake response indicates probable target mismatch or missing route.**  
   The captured headers show `HTTP/2 404` for `/internal/version` on `https://glow-backend-v4-production.up.railway.app` (host reachable; endpoint not found).  
   This is not a mechanical blocker for Step 0C because the plan’s PASS is “JSON artifact present,” but it is a material signal for later `/internal/version` contract validation steps.

ADRs — Deviations (QA Step 0C)

* None observed. The executed command and produced artifacts match the Approved Plan’s Step 0C requirements, and no deviations file exists (`step0c_deviations.md` not found).

Caveats (In-Flight Determinations)

* **Caveat:** Step 0C returned **HTTP 404** for `/internal/version`, suggesting `HDE_BASE_URL` may not point at the HD Engine service (or the route is not deployed on that host).  
  **Owner:** PO  
  **Evidence trigger:** A subsequent `/internal/version` probe against the intended prod target returns a non-404 status and produces the expected contract evidence (later step evidence).  
  **Impact if unresolved:** Later `/internal/version` validation will likely fail or remain non-diagnostic.  
* **Caveat:** Step 0C’s PASS is defined as “JSON artifact present,” and the command uses `curl ... || true`, so the step can PASS even if curl fails (it still writes the JSON).  
  **Owner:** Kronos  
  **Evidence trigger:** Confirm `results/prod_handshake.headers` contains an HTTP status line (it does in this run).  
  **Impact if unresolved:** If a future run produces an empty/absent headers capture, Step 0C PASS would not imply reachability.

Doc Deltas (PF-Canon only)

* None required for Step 0C based on this run’s evidence.

QA Verdict and Optional Follow-ups

PASS WITH CAVEATS

* Step 0C meets the Approved Plan’s stated PASS condition and deliverables.  
* Rails posture is correctly recorded as open-rails for this connectivity probe.  
* The 404 response is a useful early signal about the selected base URL, even though it is not a Step 0C mechanical blocker.

## 2.18 \- QA STEP 0D executed the Approved Plan’s token-roster validator

Review Summary

* STEP 0D executed the Approved Plan’s token-roster validator and produced the required roster \+ JSON \+ summary \+ step log artifacts under `audit/qa/...`.  
* The step outcome is **TOOLING\_BLOCKED (exit 2\)** because the PF20 roster contains tokens classified as unregistered against PF04; this outcome is explicitly defined as expected for Step 0D and does not invalidate the step’s evidence.  
* No deviations file was provided; however, the per-epic step-log manifest shows **two 0D entries** pointing to the same log path (likely a rerun overwrote the log).

Findings

1. **Approved Plan alignment (command \+ rails).** Step 0D ran under closed rails (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`, pins) and references the expected PF anchors (`PF04 — HDE-Governance, §2.0; PF10 — HDE-Build Notes, §2.7`).  
2. **Required evidence artifacts are present and internally consistent.**  
   * Roster: `.../results/token_roster_pf20.txt` exists and contains the expected PF20 token list.  
   * Machine report: `.../results/token_registry_validation.json` exists and lists `unregistered_tokens`.  
   * Human summary: `.../results/token_registry_validation.summary.md` exists and matches the JSON’s unregistered list.  
   * Step log: `.../step_logs/0D_token_roster_validate_pf04.log` exists and records `status: TOOLING_BLOCKED` with `exit_code: 2`.  
3. **Result matches Step 0D expected outcomes.** The Approved Plan defines: PASS if no unregistered tokens; TOOLING\_BLOCKED (exit 2\) if any roster tokens are not registered in PF04, and in that case the step is “recorded as blocking canon gap; proceed with evidence collection but do not claim those tokens.”  
4. **Concrete token drift recorded (the point of Step 0D).** The unregistered token list is:  
   * `QA_PRECOMMIT_CHECKLIST_OK`  
   * `QA_POSTCOMMIT_CHECKLIST_OK`  
   * `CLOSE_PACK_FILES_PRESENT_OK`  
   * `ERROR_JSON_CANON_OK`  
   * `ERROR_TOKEN_MAP_OK`

ADRs — Deviations (QA Step 0D)

ADR-DEV-01 — Step 0D appears to have been executed twice with the same log path

* What changed: `qa_step_logs_manifest.json` contains **two** `check_id: 0D` entries with different `ended_at_utc` but the same `log_path`.  
* Why it changed: likely Step 0D was re-run, overwriting the step log file.  
* Plan reference: Approved Plan — STEP 0D: token\_roster\_validate\_pf04 (expected single step log per check id; evidence should be stable per run).  
* What was actually run: `audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/0D_token_roster_validate_pf04.log` (current file reflects the later run).  
* Evidence impact: manifest has duplicate entries; earlier log content is not preserved as a separate file.  
* Canon impact: None observed.  
* Decision: **Accepted for this step** (verification goal unchanged; final evidence files are present and consistent).

Caveats (In-Flight Determinations)

* **Caveat:** Step 0D is TOOLING\_BLOCKED due to PF20 tokens not present in PF04 (as classified by the step’s validator).  
  **Owner:** Lead Dev  
  **Evidence trigger:** PF04 token registry and/or PF20 EPIC022 token roster is updated so rerunning Step 0D yields `unregistered_tokens: []`.  
  **Impact if unresolved:** Those tokens must remain unclaimed; EPIC022 acceptance that depends on them remains a canon gap.  
* **Caveat:** The Step 0D validator is a “plan-time PF04 presence check” model, not a live parse of PF04; if PF04 changes, this check can become stale.  
  **Owner:** PO  
  **Evidence trigger:** If PF04 token registry changes after this run, rerun Step 0D and compare the new JSON report.  
  **Impact if unresolved:** Unregistered list may be inaccurate relative to the current PF04 registry.  
* **Caveat:** Duplicate `0D` entries in the step-log manifest reference the same log file path.  
  **Owner:** PO  
  **Evidence trigger:** On next rerun (if any), preserve prior logs by writing to a new filename (or avoid reruns).  
  **Impact if unresolved:** Audit trace remains slightly ambiguous about the first attempt.

Doc Deltas (PF-Canon only)

* **PF04 — HDE-Governance, §2.0:** reconcile token registry to either include the five unregistered EPIC022 tokens listed above, or explicitly define a registry policy for EPIC-scoped tokens.  
* **PF20 — HDE-Phased Epics, §2.7.5:** reconcile EPIC022 token roster to match PF04 registry names (or replace with PF04-registered equivalents if the semantics overlap).

QA Verdict and Optional Follow-ups

PASS WITH CAVEATS

* Step 0D produced the exact required evidence artifacts and correctly classified registry drift as TOOLING\_BLOCKED (expected by the Approved Plan).  
* The unregistered token list is explicit and mechanically captured (good for later canon reconciliation).  
* The only deviation observed is a benign rerun/manifest duplication; it does not change the verification goal for this step.

## 2.19 \- QA Revised STEP D0.1 **passes**

Review Summary

* Revised STEP D0.1 **passes**: the required-path scan reports `missing_count: 0`, stable and per-run `d0_scan.md` exist, and the step log records `status: PASS` under closed rails.  
* Evidence posture is correct for this step: all artifacts are under `audit/qa/...` and no deviations were recorded.  
* The only anomaly is the per-epic step-log manifest containing **multiple D0.1 entries pointing to the same log file** (likely reruns). This is not a mechanical blocker for the step’s acceptance.

Findings

1. **Behavior and pass criteria met.**  
   * `required_paths_scan.json` shows `missing_count: 0` with an empty `missing_paths` list.  
   * Both `audit/qa/hde-epic022/d0_scan.md` (stable) and `audit/qa/hde-epic022/<run-id>/closeout/d0_scan.md` (per-run copy) exist and reflect `missing_count: 0`.  
   * Step log `.../step_logs/D0.1_required_paths_scan_and_d0_scan_md.log` begins with a JSON header recording `status: PASS`, `exit_code: 0`, and the closed rails string.  
2. **Rails alignment confirmed.**  
   The step log records closed rails: `SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0`, consistent with this step’s intended posture.  
3. **Evidence posture correct and complete for the step.**  
   All step artifacts are under `audit/qa/...` and the deviations logs exist (stable \+ per-run) with “None” entries.  
4. **Verdict artifact present.**  
   `audit/qa/hde-epic022/<run-id>/results/d0_1_verdict.txt` contains `PASS`, matching the step log outcome.

ADRs — Deviations (QA Step D0.1)

ADR-DEV-01 — Manifest contains repeated D0.1 entries pointing to the same log path

* What changed: `audit/qa/hde-epic022/qa_step_logs_manifest.json` includes three `D0.1` records with different `recorded_at_utc` but the same `log_path`.  
* Why it changed: likely the step was re-run and the manifest appends a new record each time.  
* Plan reference: Revised STEP D0.1 manifest update requirement (append record).  
* What was actually run: the final step log at `audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D0.1_required_paths_scan_and_d0_scan_md.log` reflects a PASS run (exit 0).  
* Evidence impact: audit trail includes duplicates but no loss of the final PASS evidence; log content is consistent with PASS.  
* Canon impact: None observed.  
* Decision: **Accepted for this step**.

Doc Deltas (PF-Canon only)

* None required for this step based on the current evidence set.

QA Verdict and Optional Follow-ups

PASS

* Required-paths preflight is clean (`missing_count: 0`) and step evidence is complete.  
* Stable and per-run scan summaries exist and match the JSON scan.  
* Manifest duplication is noted as an accepted deviation for trace clarity, not a blocker.

## 2.20 \- Revised STEP D0.2 is **acceptable**: the determinism pins evidence file exists

Review Summary

* Revised STEP D0.2 is **acceptable**: the determinism pins evidence file exists, reports `status:"success"` with the expected pinned tuple, and the step log records `status: PASS` with the intended token claims.  
* Rails alignment is correct for this step (closed rails pins captured and consistent with the env\_pins payload).  
* Evidence posture is complete for the step: governed `audit/gates/determinism/env_pins.log` and its path-proof exist, and copies exist under the run snapshots.

Findings

1. **Behavior correctness: pins match expected closed-rails tuple and succeeded.**  
   `audit/gates/determinism/env_pins.log` shows `SAFE_MODE:"1"`, `ALLOW_NETWORK:"0"`, `LC_ALL:"C"`, `LANG:"C"`, `TZ:"UTC"`, and `status:"success"`.  
2. **Rails alignment confirmed in step log.**  
   The step log records rails as `SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0`, consistent with “closed rails” for this step.  
3. **Evidence posture complete and correctly located.**  
   * Governed evidence:  
     * `audit/gates/determinism/env_pins.log`  
     * `audit/gates/determinism/env_pins.log.path_proof.txt`  
   * Snapshot copies exist under:  
     * `audit/qa/hde-epic022/<run-id>/snapshots/env_pins/`  
       All present and consistent (same sha256 in both proof files).  
4. **Step log and manifest updated.**  
   * Step log file exists and embeds both env\_pins and path\_proof content.  
   * Per-epic manifest includes an entry for `check_id: D0.2` with `status: PASS`.  
5. **Verdict artifact present.**  
   `audit/qa/hde-epic022/<run-id>/results/d0_2_verdict.txt` contains `PASS`.

ADRs — Deviations (QA Step D0.2)

* None required for acceptance.  
  Note: `audit/qa/hde-epic022/stepd0_2_deviations.md` is reported “File not found.” The step output bundle does not indicate a deviation occurred; absence of a deviations file is not a mechanical blocker unless the Approved Plan for r16 explicitly requires a deviations artifact to be created for every run of D0.2 (not shown in the evidence bundle).

Doc Deltas (PF-Canon only)

* None required for this step based on the produced evidence.

QA Verdict and Optional Follow-ups

PASS

* Determinism pins evidence is present, correct, and proofed, and the step log records PASS.  
* Snapshot copies match the governed evidence (sha256 consistent).  
* Manifest entry for D0.2 is present and PASS, supporting run traceability.

## 2.21 \- Live QA Rails: No Non-Canonical Env Pins (PYTHONHASHSEED is not a required pin)

Timestamp: 122625 00:00

**Details**  
 Live QA plans have introduced non-canonical environment variables (example: `PYTHONHASHSEED=0`) as “determinism pins.” This increases process bloat and creates drift from the canon-defined determinism pins and rails evidence posture.

**Policy (normative)**

1. **Canonical determinism pins are limited to the canon set.**  
    Any Live QA step that produces governed bytes/evidence MUST use only the determinism pins already defined in canon (locale \+ timezone pins; rails as applicable).  
    (Glow QA Guide, §14.4.1; HDE-Governance, §4.1.4; Plan Templates, §2.1)

2. **Do not require `PYTHONHASHSEED` in Live QA plans.**  
    `PYTHONHASHSEED` MUST NOT be added as a required rail/pin for Live QA plan approval or execution. It is not part of the canonical determinism env pins set.

3. **Determinism must be achieved by explicit ordering, not interpreter knobs.**  
    If a QA step (or repo tool) produces nondeterministic output due to hash-order dependence, the step MUST normalize ordering explicitly (sort keys; sort lists; avoid set iteration without ordering) rather than relying on `PYTHONHASHSEED`.  
    If the nondeterminism exists in repo-provided tools, treat it as an implementation defect to drain via the normal canon paths (not by adding QA-only rails).

4. **If `PYTHONHASHSEED` is used for one-off diagnostics, it is non-governed.**  
    A plan MAY temporarily set `PYTHONHASHSEED` only as an explicitly labeled diagnostic control, and it MUST NOT be interpreted as satisfying or extending the canonical env pins evidence surface.

**Conflict note (explicit override)**  
 If any plan template or reviewer checklist language encourages adding non-canonical env pins for “extra determinism,” this addendum overrides it for Live QA planning and execution posture.

**Drain targets (titles-only)**

* Glow QA Guide

* HDE-Governance

* Plan Templates

**Evidence**  
 None.

## 2.22 \- QA Revised STEP D0.2 is acceptable with caveats. 

The determinism env pins evidence was emitted, proofed, snapshotted, logged, and recorded

Review Summary

* **Revised STEP D0.2 is acceptable with caveats.** The determinism env pins evidence was emitted, proofed, snapshotted, logged, and recorded in the step manifest as required by the Approved Plan r16.  
* **Closed-rails posture is correct and evidenced.** The captured pins match the required tuple and are recorded in the governed location with a path proof.  
* **No mechanical blockers were found** that would invalidate the verification goal of this step; however, several bounded alignment issues must be resolved in flight.

Findings

1. **Behavior correctness confirmed.**  
   `audit/gates/determinism/env_pins.log` exists, is LF-terminated, and reports `status:"success"` with the expected pinned values (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `LC_ALL=C`, `LANG=C`, `TZ=UTC`). The corresponding path-proof file exists and matches size/sha256.  
2. **Rails alignment verified.**  
   The step log records closed rails (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`, locale/TZ pins) consistent with Step D0.2 requirements.  
3. **Evidence posture is complete for Step D0.2.**  
   Governed evidence lives at `audit/gates/determinism/…` and snapshot copies exist under `audit/qa/hde-epic022/<run-id>/snapshots/env_pins/`. The step log embeds both the pins file and the proof.  
4. **Step-log manifest updated.**  
   The per-epic manifest contains an entry for `check_id: D0.2` with `status: PASS`.  
5. **Verdict artifact present.**  
   `audit/qa/hde-epic022/<run-id>/results/d0_2_verdict.txt` contains `PASS`, matching the step outcome.

ADRs — Deviations (QA Step D0.2)

* **ADR-DEV-01 — Deviations file not created**  
  * What changed: `audit/qa/hde-epic022/stepd0_2_deviations.md` is absent.  
  * Why it changed: No deviation occurred; the step implementation only writes the deviations file when needed.  
  * Plan reference: Revised STEP D0.2 deviations handling section.  
  * What was actually run: See `…/step_logs/D0.2_determinism_env_pins_emit.log`.  
  * Evidence impact: None on verification goal; all required evidence is present.  
  * Canon impact: None observed.  
  * Decision: **Accepted for this step.**

Caveats (In-Flight Determinations)

1. **Canonical path for determinism evidence must remain the single source of truth.**  
   * Owner: PO  
   * Evidence trigger: `docs/evidence/INDEX.json` references `audit/gates/determinism/env_pins.log` (canonical) rather than snapshot copies.  
   * Impact if unresolved: Index could point to non-canonical paths, complicating later validation.  
   * PF refs: PF12 — HDE-Schemas and Artifacts, §8.6.3.  
2. **Token claim discipline must remain registry-gated.**  
   * Owner: Kronos  
   * Evidence trigger: Step logs do not claim tokens not registered in PF04; any drift is recorded as doc delta only.  
   * Impact if unresolved: Invalid acceptance claims could be made downstream.  
   * PF refs: PF10 — HDE-Build Notes, §2.7; PF04 — HDE-Governance, §2.0.  
3. **Codespaces snapshot canonicalization.**  
   * Owner: PO  
   * Evidence trigger: Presence of PF19-canonical Codespaces snapshot artifact at the required location/shape.  
   * Impact if unresolved: Reduced conformance to PF19 audit expectations.  
   * PF refs: PF19 — Glow QA Guide, §14.4.3.

Doc Deltas (PF-Canon only)

* None required for this step based on current evidence; caveats are procedural and do not mandate canon changes.

QA Verdict and Optional Follow-ups

**PASS WITH CAVEATS**

* Determinism env pins are correctly emitted, proofed, and logged.  
* Closed-rails posture is evidenced and consistent.  
* Snapshot copies are present and match governed evidence.  
* Address the listed caveats during subsequent steps to maintain canonical alignment and governance discipline.

## **2.23 — EPIC022 — Freeze-Pack Manifest evidence-copy semantics \+ `release_id` recompute contract (no dual semantics)**

Timestamp: 122725 00:00

**Decision statement (normative)**

1. **Single Source of Truth (SoT):**  
    The Freeze-Pack Manifest SoT is `catalog/manifest.json`. No other file is permitted to act as the SoT for Freeze-Pack membership or release identity. (PF12 — HDE-Schemas and Artifacts, §6.1)

2. **Manifest schema is closed; no extras:**  
    `catalog/manifest.json` top-level MUST contain exactly: `root`, `version`, `built_at_utc`, `files` (and no other keys). The manifest MUST NOT list itself in `files`. (PF12 — HDE-Schemas and Artifacts, §6.1)

3. **Canonical bytes rule:**  
    Canonical bytes are defined by canonical JSON rules (UTF‑8, no BOM, ASCII-sorted keys recursively, compact separators, exactly one trailing LF). Identity and verification MUST operate on canonical bytes. (PF12 — HDE-Schemas and Artifacts, §4.1)

4. **`release_id` definition is fixed:**  
    `release_id = sha256(canonical_bytes(catalog/manifest.json))`, encoded as lowercase 64-hex. (PF12 — HDE-Schemas and Artifacts, §6.2; PF09 — HDE-Build Checklist, Subtask HDE-DIST002.2)

5. **Release ID evidence paths (canonical):**  
    EPIC022 release identity evidence is canonical at:

   * `artifacts/math/release_id.txt`

   * `artifacts/math/release_id_recompute.log`  
      (PF10 — HDE-Build Notes, §2.8)

6. **Freeze-Pack evidence-copy path is governed and unambiguous:**  
    `artifacts/math/freeze_pack_manifest.json` is the Freeze-Pack Manifest **evidence copy** (bytes copied for evidence). It MUST be a **byte-identical copy** of the canonical on-disk `catalog/manifest.json` (i.e., identical canonical bytes). It is not permitted to be a derived schema, subset manifest, or alternate contract. (PF12 — HDE-Schemas and Artifacts, §6.4; PF09 — HDE-Build Checklist, Subtask HDE-DIST002.1)

7. **Canonical recompute entrypoint and evidence set:**  
    The canonical recompute mechanism is the governed recompute script and outputs defined by PF12, including the recompute log and checksum audit outputs. Any recompute implementation MUST (a) validate canonicalization, (b) recompute `release_id` from canonical manifest bytes, and (c) fail closed on any mismatch. (PF12 — HDE-Schemas and Artifacts, §6.4)

**Clarifications**

* **No “branching” semantics are recognized.** There is one Freeze-Pack Manifest contract and one evidence-copy meaning. Any alternate manifest-like artifacts MUST be explicitly quarantined under a different name/path and MUST NOT reuse `artifacts/math/freeze_pack_manifest.json`.

* `manifest_snapshot.json` (and any similar evidence-only summaries) are **evidence only** and MUST NOT be used as identity inputs or substituted for the Freeze-Pack Manifest. (PF12 — HDE-Schemas and Artifacts, §6.4)

* Where evidence tooling performs equality checks, “equal” means **byte-equal** on canonical bytes between `catalog/manifest.json` and `artifacts/math/freeze_pack_manifest.json` (not “JSON-equivalent”).

**Drain targets (titles-only)**

* PF12 — HDE-Schemas and Artifacts

* PF09 — HDE-Build Checklist

* PF20 — HDE-Phased Epics

* PF27 — Plan-Templates

**Evidence**

* None (policy addendum)

## 2.24 \- HDE-EPIC022 Remedial PR1

### Review Summary

* Remedial PR addresses the two remaining correctness gaps called out post-CI: `/internal/version` release\_id fallback hashing semantics and missing regression coverage for the recompute CLI’s exit-code behavior.  
* It preserves the Implementation Doc’s core contract: SoT manifest schema posture, freeze-pack evidence-copy semantics, and `release_id = sha256(canonical_bytes(catalog/manifest.json))` with a fail-closed recompute check.  
* It resolves the original PR’s mismatch signatures by driving `release_id_recompute.log` to `match=true` with `problems_count=0`.  
* It adds a focused regression test (`tests/scripts/test_release_id_recompute.py`) and demonstrates passing runs under closed rails for: the new test, `scripts/release_id_recompute.py --check`, and the `/internal/version` contract test.  
* Evidence posture looks sufficient for the failure modes actually encountered (mismatch \+ exit-code bug \+ untested fallback), but the PR does touch a larger set of governed evidence/index artifacts than the narrow change would suggest, which increases audit surface.

### Findings

1. **Implementation Doc scope/acceptance appears satisfied for PR-01’s core contract.**  
   * Observed: The required PR-01 contract is explicitly “canonical schema \+ byte-identical evidence copy \+ release\_id derived from canonical bytes \+ recompute check must succeed/fail closed,” with required evidence outputs listed.  
   * Why it matters: This is the authoritative acceptance surface; deviations would reintroduce the exact determinism/identity drift the remediation is meant to eliminate.  
2. **Original PR failure signature is materially resolved in the Remedial PR evidence.**  
   * Observed: Earlier `release_id_recompute` state showed `match=false` and problem markers; the later entry shows `match=true` and `problems_count=0`.  
   * Why it matters: This is the direct signal that freeze-pack evidence-copy, manifest schema posture, and release\_id derivation are now internally consistent.  
3. **Bug Fix Report’s P1 issue (recompute exits 1 after self-healing) is addressed, and the Remedial PR adds the missing regression coverage.**  
   * Observed: Bug Fix Report describes the defect: recompute returned failure even after rewriting stale artifacts, requiring a second run.  
   * Observed: Remedial PR claims and demonstrates a new regression test \+ passing run, and refactors recompute to re-evaluate state after writes so the final logged state is clean.  
   * Why it matters: Without the regression test, this failure mode is highly likely to recur because it is a subtle “state recomputed after mutation” bug class.  
4. **`/internal/version` coupling posture is protected by strengthening the release\_id fallback semantics (within scope).**  
   * Observed: Remedial PR explicitly targets correcting fallback hashing to use canonical manifest bytes (serializer-backed), avoiding raw-byte hashing drift.  
   * Why it matters: Even if the normal path reads `artifacts/math/release_id.txt`, the fallback path must not create a second definition of release identity. This aligns with the Implementation Doc’s “no branching semantics” posture.  
5. **Tests run are narrowly targeted and appropriate for the remediated defect set.**  
   * Observed: Remedial PR runs: `tests/scripts/test_release_id_recompute.py`, `python scripts/release_id_recompute.py --check`, and `tests/transport/test_internal_version_contract.py` under closed rails.  
   * Why it matters: These three checks map directly to the corrected behavior: recompute CLI semantics, recompute check posture, and `/internal/version` contract.  
6. **Notable review risk: broad governed-evidence churn in the Remedial PR bundle.**  
   * Observed: The Remedial PR file list includes many governed artifacts beyond the immediate release\_id surfaces (evidence index \+ multiple core artifacts/path proofs).  
   * Why it matters: Even if generated by canonical tooling, this increases merge-review complexity and can hide accidental drift. However, no concrete contract break is evidenced in the provided artifacts.

### Doc Deltas (PF-Canon only)

* Doc: PF12 — HDE-Schemas and Artifacts  
  Section: §6.4 “Evidence and CI hooks”  
  Delta: Clarify recompute script exit-code semantics across modes (NEW CANON PROPOSAL if not already stated):  
  * `--check` must be fail-closed (non-zero on any mismatch) and must not “self-heal” artifacts,  
  * non-`--check` mode may rewrite governed artifacts to the canonical state and must exit 0 when the post-write state is clean,  
  * recommend/require a regression test that covers both modes (pattern: isolated temp workspace so repo state is not mutated).

DECISION: PR ACCEPTABLE

## 2.25 \- HDE-EPIC022 Remedial PR2

### Review Summary

* PR-02 adds a fail-closed release identity gate as a new CI check (`ci/checks/check_release_identity.sh`) that enforces closed rails, runs the canonical `scripts/release_id_recompute.py --check`, validates manifest schema \+ canonical bytes posture, asserts freeze-pack byte equality, and requires the governed recompute evidence set to exist and be non-empty.  
* PR-02 wires the new gate into the closed-rails sanity pipeline (`tools/evidence/run_sanity_pipeline.py`) so it runs alongside existing determinism/evidence checks under CI posture.  
* PR-02 strengthens the existing recompute regression test (`tests/scripts/test_release_id_recompute.py`) to also assert evidence completeness after write-mode recovery, while preserving the controlled negative scenario for `--check` fail-closed behavior.  
* The PR aligns to the Approved Plan’s PR-02 scope: identity gate under closed rails, Guardrail 1 (byte-equality), Guardrail 2 (no alternate semantics at the freeze path), and evidence completeness enforcement, without modifying manifest contents.  
* Notable risk: running the gate locally can rewrite `artifacts/math/release_id_recompute.log` as a side effect of invoking the recompute script; CI is still safe, but operator guidance should be explicit that this is a gated, tool-driven surface.

### Findings

1. **Plan alignment: PR-02 implements the required fail-closed identity gate and keeps scope within “gating/tests/check wiring.”**  
   * Observed: Approved Plan requires a CI-level fail-closed identity gate that enforces closed schema rules, byte-equality between SoT and freeze evidence copy, `release_id` correctness, and evidence completeness, with no manifest re-authoring.  
   * Observed in PR Artifacts: new `ci/checks/check_release_identity.sh` \+ wiring into the sanity pipeline \+ test extension fits that intent.  
   * Why it matters: This is exactly the “prevent recurrence” layer; without it, PR-01 can silently regress.  
2. **Guardrail 1 (byte-equality) is enforced in a strict, byte-level way (not schema-only).**  
   * Observed: The gate canonicalizes `catalog/manifest.json` bytes and asserts `artifacts/math/freeze_pack_manifest.json` bytes match exactly; mismatch fails the gate.  
   * Why it matters: This directly addresses the documented failure mode where artifacts could be schema-valid but not byte-identical (PF10 precedence where it speaks; PF12 canonical bytes posture). PF12 — HDE-Schemas and Artifacts, §6.2–§6.4.  
3. **Guardrail 2 (no alternate semantics at the freeze path) is enforced by closed key-set \+ byte-equality.**  
   * Observed: The gate asserts the freeze-pack JSON top-level keys are exactly `{root, version, built_at_utc, files}` and also enforces byte equality to canonical bytes of SoT; any derived/alternate schema or embedded extras will fail.  
   * Why it matters: This prevents path reuse drift at the governed freeze evidence path (PF10 — HDE-Build Notes, §2.23; PF12 — HDE-Schemas and Artifacts, §6.4).  
4. **Evidence completeness is explicitly enforced (prevents “partial pass”).**  
   * Observed: The gate checks existence and non-emptiness of the governed recompute evidence set and core identity inputs (manifest, freeze copy, release\_id).  
   * Observed: The recompute regression test now also asserts that the key evidence outputs are created and non-empty in write-mode recovery in a temp workspace.  
   * Why it matters: This satisfies the Approved Plan’s “verification completeness gate” requirement and prevents CI from going green without the evidence surface present.  
5. **Verification posture is sufficient for PR-02’s scope and matches the plan.**  
   * Observed: PR Artifacts show closed-rails runs of:  
     * `python scripts/release_id_recompute.py --check`  
     * `python ci/checks/check_release_identity.sh`  
     * `pytest -q tests/scripts/test_release_id_recompute.py` (pass)  
   * Why it matters: These checks are the minimal, directly relevant ones for a gating PR: recompute check correctness, gate correctness, and regression coverage.  
6. **Residual operational risk (non-blocking): recompute check writes a governed log even in `--check` mode.**  
   * Observed: PR Artifacts acknowledge that running the gate can rewrite `artifacts/math/release_id_recompute.log` and require reverting when trying to keep the working tree clean.  
   * Why it matters: This is not a correctness failure for CI (CI workspaces are ephemeral), but it should be documented as operator behavior so devs don’t accidentally commit unintended log churn. This is best handled as a PF-Canon doc delta, not a code change in this PR.

### Doc Deltas (PF-Canon only)

* Doc: PF12 — HDE-Schemas and Artifacts  
  Section: §6.4 “Release identity recompute evidence set”  
  Delta: Document the existence of a fail-closed CI identity gate entrypoint (`ci/checks/check_release_identity.sh`) that (a) enforces closed rails, (b) runs `scripts/release_id_recompute.py --check`, and (c) asserts presence/non-emptiness of the governed recompute evidence outputs. Clarify that the gate is a Python entrypoint (invoke via `python …`) and that `--check` may rewrite the recompute log in CI workspaces.  
* Doc: PF19 — Glow QA Guide  
  Section: §9.2.3 “Closed rails CI gates” (or closest section covering sanity pipeline \+ CI checks)  
  Delta: Add the release identity gate as a required closed-rails CI step (either explicitly in the sanity pipeline sequence or as a sibling gate), and note operator implications of recompute-log regeneration in ephemeral CI vs local repos.

## 2.26- HDE-EPIC022 Remedial Docs PR

### Review Summary

* Remedial PR is a narrow docs-only remediation that fixes the canon-pointer defect identified in Original PR: AGENTS now references PF10 by the correct titles-only name (“PF10 — HDE-Build Notes”), replacing the incorrect “PF10 — Provenance & Coupling.”  
* The remediation is real (not superficial): it is an actual content change in AGENTS, and the bundle includes a repo-wide search confirming no remaining incorrect “PF10 — …” references in the repo docs set.  
* Remedial PR preserves Original PR’s doc sweep substance (README/CHANGELOG/docs updates that describe the EPIC022 remediation identity posture); it does not rewrite or expand scope beyond the docs correction.  
* This aligns with the Implementation Doc’s intent for the epic at the docs layer: accurate canon pointers, with PF10 precedence where PF10 speaks, and no invented canon titles.  
* Tests are still “not run (docs-only change)” which is acceptable here; the key risk was factual drift in canon references, and that is addressed by the remediation.

### Findings

1. **Observed:** Original PR’s AGENTS canon-title list included “PF10 — Provenance & Coupling”; Remedial PR replaces it with “PF10 — HDE-Build Notes.”  
   * **Why it matters:** This workspace uses titles-only canon references. A wrong PF title is a traceability break that can misroute readers to the wrong authority source, which is exactly the kind of drift docs must prevent.  
2. **Observed:** Remedial PR evidence includes a repo-wide search for `PF10 —` references showing the corrected AGENTS line and no remaining incorrect PF10 title usage in the repo docs scope.  
   * **Why it matters:** This closes the defect fully (not just in the one file), which prevents recurrence by leaving the repo in a clean “titles-only pointer” state.  
3. **Observed:** Remedial PR is minimal in scope: it changes only AGENTS to correct the PF10 title reference; the rest of the documentation sweep remains intact.  
   * **Why it matters:** Minimizing the remediation diff reduces the chance of introducing new doc drift or accidental contract changes.

## 2.27 \- QA Revised STEP D0.3 is acceptable: 

Review Summary

* Revised STEP D0.3 is **acceptable**: the recompute log reports `match=true` with `problems_count=0`, and the step log records `status: PASS` with `exit_code: 0`.  
* Rails alignment is correct for this step (closed rails / deterministic pins recorded in the step log).  
* Evidence posture is complete: governed recompute log and snapshots exist, and the per-epic step-log manifest records the PASS outcome (with a note about a prior FAIL entry for the same check).

Findings

1. **Release ID recompute passed with zero problems.**  
   `artifacts/math/release_id_recompute.log` shows `manifest_sha256` equals `release_id_txt`, with `match=true` and `problems_count=0`.  
2. **Step log confirms PASS and closed-rails posture.**  
   `audit/qa/hde-epic022/run_20251226t181426z_e44b4cc/step_logs/D0.3_release_id_recompute_and_manifest_check.log` records `status: PASS`, `exit_code: 0`, and closed rails pins (`SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`, locale/TZ pins). It also records the PF anchors used by the step (`PF12 — HDE-Schemas and Artifacts, §6.4` plus PF10 references).  
3. **Required artifacts for review exist under audit/qa snapshots.**  
   The run snapshot includes: `snapshots/release_id/release_id.txt`, `snapshots/release_id/release_id_recompute.log`, and `snapshots/release_id/freeze_pack_manifest.json` (and they are consistent with the recompute PASS).  
4. **Step manifest records both a historical FAIL and a later PASS for D0.3.**  
   `audit/qa/hde-epic022/qa_step_logs_manifest.json` contains two D0.3 entries: one `FAIL_BEHAVIOR` (earlier) and one `PASS` (later).

ADRs — Deviations (QA Step D0.3)

ADR-DEV-01 — Step-log manifest contains two D0.3 entries pointing to the same log path

* What changed: `qa_step_logs_manifest.json` records both a FAIL\_BEHAVIOR and a PASS for D0.3, both referencing the same `log_path`.  
* Why it changed: likely the step was re-run and the step log file was overwritten in-place.  
* Plan reference: Approved QA Plan — Revised STEP D0.3 (step log \+ manifest recording).  
* What was actually run: the current on-disk step log is the PASS version (`exit_code: 0`, `status: PASS`).  
* Evidence impact: the earlier failing log content is not preserved as a distinct artifact in this packet; only the manifest record remains.  
* Canon impact: None observed.  
* Decision: **Accepted for this step** (verification goal for the current run is met; trace ambiguity is bounded to historical attempt evidence).

Doc Deltas (PF-Canon only)

* None required for this step based on the current PASS evidence.

QA Verdict and Optional Follow-ups

Verdict line: PASS

* This run satisfies the D0.3 coherence requirement: `release_id_txt` matches the recomputed `manifest_sha256` and no validator problems were reported.  
* The step log records PASS under closed rails with the expected PF anchors, supporting auditability.  
* The manifest shows an earlier FAIL and later PASS for the same check; the earlier log content is not separately preserved in this evidence bundle.

## 2.28 \- QA STEP D2.1 meets the Approved Plan requirements and passes:

Review Summary

* STEP D2.1 **meets the Approved Plan requirements and passes**: governed showcompat artifacts exist, both checksum sidecars exist and match, and the two required pytest runs passed under closed rails.  
* Evidence posture is complete: required logs live under `audit/qa/.../results/`, a primary step log exists under `audit/qa/.../step_logs/`, snapshot copies exist under `audit/qa/.../snapshots/showcompat/`, and the per-epic step-log manifest records the D2.1 PASS.  
* No deviations were provided or indicated for this step.

Findings

1. **Governed showcompat artifacts present and consistent.**  
   * `artifacts/cli/showcompat/stdout.json` and `artifacts/cli/showcompat/args.json` exist.  
   * Both checksum sidecars exist and match:  
     * `artifacts/cli/showcompat/stdout.json.sha256`  
     * `artifacts/cli/showcompat/stdout.sha256`  
       The sha lines are identical (`affb9ce0…`), indicating the legacy alias is a direct copy of the canonical sidecar (PF10 — HDE-Build Notes, §2.5 posture).  
2. **Required tests ran and passed (as required by the Approved Plan).**  
   * Canonical-bytes test: `1 passed` (`tests/cli/test_cli_canonical_bytes.py::test_showcompat_stdout_is_canonical`).  
   * Usage/errors suite: `5 passed` (`tests/cli/test_cli_usage_and_errors.py`).  
3. **Rails alignment confirmed (closed rails).**  
   The step log records `SAFE_MODE=1`, `ALLOW_NETWORK=0`, `APP_ENV=dev`, and determinism pins (`LC_ALL=C`, `LANG=C`, `TZ=UTC`, `PYTHONHASHSEED=0`).  
4. **Evidence posture complete and correctly located under `audit/qa/...`.**  
   * Results logs exist under `audit/qa/hde-epic022/<run-id>/results/` (generator \+ both pytest logs).  
   * Primary step log exists at `audit/qa/hde-epic022/<run-id>/step_logs/D2.1_showcompat_artifacts_and_tests.log` with `status: PASS` and `exit_code: 0`, embedding generator \+ pytest outputs.  
   * Snapshot copies exist under `audit/qa/hde-epic022/<run-id>/snapshots/showcompat/` (including path-proof files).  
5. **Per-epic step-log manifest updated for D2.1.**  
   `audit/qa/hde-epic022/qa_step_logs_manifest.json` contains a D2.1 entry with `status: PASS`.

Doc Deltas (PF-Canon only)

* None required for this step based on the produced evidence.

QA Verdict and Optional Follow-ups

Verdict line: PASS

* The dual-write checksum sidecar requirement is satisfied (canonical \+ legacy alias) and consistent with the plan’s PF10 reference.  
* Both required pytest validations passed, supporting the “canonical bytes \+ usage/errors discipline” intent of Step D2.1.  
* Generator stdout/stderr capture file exists but is empty in this run; this is not a blocker since the generator succeeded and downstream artifacts/tests are present.

## **2.29 \- Ops tasks: PO-only execution (IA-guided), not Codex PRs**

Timestamp: 122825 00:00

**Decision statement (normative)**

1. **Definition**  
    An **Ops task** is any work item that requires privileged access to systems **outside the repository** and therefore cannot be performed by automated agents. This includes (non-exhaustive): service configuration, secrets and env var changes, deploy/runtime settings, infrastructure console actions, and certain database operations (creation, grants, production migrations, and other privileged state changes).  
    A **DevOps task** is treated as an Ops task whenever it requires any of the above human-only access.

2. **Execution authority**  
    Ops tasks MUST be executed by the **PO (human operator)** only. Automated agents (including Codex-driven agents) MUST NOT attempt to perform them, MUST NOT claim completion, and MUST NOT simulate external state changes.

3. **IA facilitation posture**  
    Ops tasks MAY be part of an EPIC. When included, they are facilitated by the **Implementation Agent (IA)**, who MUST guide the PO through execution. The IA’s job is to specify intent, constraints, verification, and evidence requirements in a **what-not-how** manner, then work directly with the PO during execution.

4. **Not a PR**  
    Ops tasks are **not Codex PRs**. They MUST NOT be represented as “implementable PR work.” Any implementation/remediation document MUST separate Ops tasks from PR work and clearly label them as: **PO-only execution, IA-guided**.

5. **Ops task spec format (what-not-how, required fields)**  
    Every Ops task record MUST include:

* **Task ID** (stable, referenced consistently)

* **Owner:** PO

* **Facilitator:** IA

* **Target system/service** (name only, no secrets)

* **Intent / desired end state** (what changes, and what “done” looks like)

* **Constraints / safety rails** (what must remain true while executing)

* **Success criteria** (observable outcomes, not assumptions)

* **Evidence to capture** (what artifact(s) will prove the change, and where stored)

* **Rollback intent** (what “revert” means at a high level)

* **Secret handling note** (explicitly: no plaintext secrets in docs or evidence)

6. **Evidence posture (required)**  
    Completion of an Ops task MUST produce a repo-stored evidence artifact (text-first) under a lowercase path such as:

* `audit/ops/<epic-id>/...` for Ops execution evidence, or

* `audit/qa/<epic-id>/...` when the evidence is part of QA execution.

Evidence MUST NOT include secrets. If a setting/value is sensitive, evidence MUST be presence-only, redacted, or hashed, while still being sufficient to verify that the intended state was reached.

7. **Mechanics Guide tracking requirement**  
    Any Ops task included in an EPIC MUST be represented as a **subtask** in the **HDE-Mechanics Guide** so it can be tracked and reused. The Mechanics Guide entry MUST use the same Task ID and MUST carry the same required fields listed above.

8. **No governance drift**  
    Ops tasks MUST NOT create new acceptance tokens or redefine acceptance semantics. If an Ops task affects acceptance, it MUST map to existing governance-defined acceptance posture and be proven via evidence artifacts.

**Clarifications**

* If a change is fully achievable as code (including tests and deterministic artifacts), it is PR work. If any step requires human console/config action, that step is an Ops task (even if adjacent code changes exist).

* Ops tasks can be prerequisites for EPIC completion, but they are proven by evidence artifacts, not by agent execution claims.

**Drain targets (titles-only)**

* HDE-Mechanics Guide

* Plan Templates

* Epic Process Guide

* HDE-Phased Epics

* HDE-Schemas & Artifacts

* Glow QA Guide

**Evidence**  
 None (policy addendum)

## **2.30 — Remediation Implementation Guides are DEV/OPS-only (verification embedded)**

Timestamp: 122825 00:00

**Decision statement (normative)**

1. **Scope**  
   This addendum applies to **Remediation Implementation Guides** produced for escalations and remediation execution. It does not change Live QA plan formats.  
2. **Permitted step types (only)**  
   A Remediation Implementation Guide MUST use only two step types: **DEV** and **OPS**. No other step types are permitted (no QA, DOC, REVIEW, or “verification-only” steps).  
3. **Verification embedding requirement**  
   All verification MUST be embedded inside the owning DEV or OPS step. Verification MUST produce concrete, repo-stored evidence outputs (paths and filenames specified in the step).  
4. **OPS posture linkage**  
   OPS steps in remediation guides MUST follow the OPS posture defined in PF10 — HDE-Build Notes, §2.29 (PO-executed, IA-guided, not Codex PR work, secret-free evidence, lowercase audit paths).  
5. **Strict lane separation**  
   A step labeled DEV MUST contain only DEV actions. A step labeled OPS MUST contain only OPS actions. If a DEV action depends on an OPS output (or vice versa), the producing step MUST come first and the dependent step MUST declare its dependency explicitly (see §2.31).

**Clarifications**

* “DEV” includes code changes, repo-local tooling changes, and repo-local updates required to integrate outputs produced by OPS steps.  
* “OPS” includes PO-only execution tasks that require external system access, per PF10 — HDE-Build Notes, §2.29.  
* A remediation guide may include tests and evidence capture, but only as verification embedded inside a DEV/OPS step.

**Drain targets (titles-only)**

* HDE-Mechanics Guide  
* Glow QA Guide  
* Epic Process Guide  
* Plan Templates

**Evidence**  
None (policy addendum)

---

## **2.31 — Canonical Remediation Implementation Guide template (dependency-line rule locked)**

Timestamp: 122825 00:00

**Decision statement (normative)**

1. **Template is canonical for remediation guides**  
   All Remediation Implementation Guides MUST follow the canonical section ordering and step schema defined in this addendum.  
2. **Step Overview is mandatory**  
   The guide MUST include a Step Overview table listing: `Step ID`, `Step name`, `Step type (DEV/OPS)`, `Step intent (DISCOVERY/CHANGE)`, `Owner/role`, `Depends on`, `Cross-lane dependency`, `Outputs`.  
3. **Step Details schema is mandatory**  
   Each step MUST include a Step Details block with, at minimum:  
   `Step ID`, `Step name`, `Step type (DEV/OPS)`, `Step intent (DISCOVERY/CHANGE)`, `Owner/role`, `Preconditions`, `Inputs`, `Canon constraints (PF references)`, `Actions (what-not-how)`, `Outputs (required)`, `Verification (embedded)`, `In-flight determinations (optional)`.  
4. **Dependency-line rule (the required modification)**  
   If a step depends on outputs produced by a prior step in the other lane, the dependent step MUST include exactly **one** cross-lane dependency line in this exact form:

`Inputs needed from Step S<N> during implementation: <exact items>`

Rules for this line:

* `S<N>` MUST be the actual producing step ID (no placeholders such as `Sx`).  
* The line MUST appear exactly once in the dependent step. It MUST NOT be duplicated, nested, or prefixed by a placeholder field label.  
* If there is no cross-lane dependency, the line MUST be omitted (do not include placeholders).  
5. **OPS posture reminder**  
   Any step labeled OPS MUST comply with PF10 — HDE-Build Notes, §2.29.

**Canonical template skeleton (paste-ready)**

Artifact Map  
\- \<inputs...\>  
\- Output: Remediation Implementation Guide (for approval)

\#\# Executive Summary  
\- ...

\#\# Canon Frame (What “Correct” Means)  
1\. \<testable statement\> — PFxx — Title, §X.Y

\#\# Observed Evidence Snapshot (Self-Contained; non-PF)  
\#\#\# Evidence inventory reviewed (non-PF)  
\- \<paths or quoted excerpts brought into this guide\>  
\#\#\# Primary failure signatures  
\- \<short quotes / exact status lines / exact headers\>

\#\# Root Cause Analysis (RCA)  
\#\#\# What went wrong  
\#\#\# How it manifested  
\#\#\# Root causes  
\#\#\#\# Documentation ignored  
\#\#\#\# Documentation incorrect  
\#\#\#\# Documentation missing

\#\# Remediation Implementation Plan (Stepwise, DEV/OPS only)  
\#\#\# Step Overview  
| Step ID | Step name | Step type | Step intent | Owner/role | Depends on | Cross-lane dependency | Outputs |  
| \--- | \--- | \--- | \--- | \--- | \--- | \--- | \--- |

\#\#\# Step Details  
Step ID:  
Step name:  
Step type (DEV or OPS):  
Step intent (DISCOVERY or CHANGE):  
Owner/role:  
Preconditions:  
Inputs:  
Canon constraints (PF references):  
Actions (complete but scoped; what-not-how):  
Outputs (required):  
Verification (required, embedded; not a separate step):  
In-flight determinations (only if needed; must not be mechanical blockers):  
ADR linkage (if applicable):

\#\# PF Docs Consulted  
\- PFxx — Title  
\- ...

\#\# ADRs Requiring Approval (Canon and External Task Creation)  
ADR-001...

**Drain targets (titles-only)**

* Plan Templates  
* Epic Process Guide  
* Glow QA Guide  
* HDE-Mechanics Guide

**Evidence**  
None (policy addendum)

---

## **2.32 — ADR-003 deferred: /internal/version auth posture is not yet canonized**

Timestamp: 122825 00:00

**Decision statement (normative)**

1. **Canon gap recorded**  
   PF canon defines the `/internal/version` transport and content contract, but does not canonize its **auth posture** (public vs operator-network gated vs auth-header required) or the expected failure mode when access is missing/invalid.  
   PF touchpoints: PF04 — HDE-Governance, §10.5; PF14 — HDE-Mechanics Guide, §14.2–§14.4.  
2. **Non-invention rule for auth posture**  
   Until canonized, remediation guides and operational tooling MUST NOT state auth requirements for `/internal/version` as canon. Any statement about auth posture MUST be explicitly labeled as **Observed Evidence (non-PF)**.  
3. **What evidence is required to canonize auth posture**  
   A canon decision for `/internal/version` auth posture is deferred until OPS discovery captures **status line and headers** for the canonical deployment context(s) under two conditions:  
* with no auth header, and  
* with the expected auth header present (value redacted or presence-only noted).

The captured evidence MUST be secret-free and stored in-repo under a lowercase audit path, consistent with PF10 — HDE-Build Notes, §2.29.

4. **Decision inputs to be resolved by the evidence**  
   The evidence must be sufficient to decide whether `/internal/version` is intended to be:  
* (a) unauthenticated public,  
* (b) operator-network gated without auth, or  
* (c) auth-header required,

and what the expected response is for missing/invalid access (status code and headers).

**Clarifications**

* This addendum does not change the governed transport/content contract for `/internal/version`; it only records that access-control semantics are not yet canonized.  
* Once canonized, the decision MUST be drained to the owning canon homes for mechanics/governance (titles-only: HDE-Governance, HDE-Mechanics Guide).

**Drain targets (titles-only)**

* HDE-Governance  
* HDE-Mechanics Guide  
* Glow QA Guide

**Evidence**  
None (policy addendum)

Below are **paste-ready PF10 Build Notes addenda** that directly reinforce the two recurring blockers: (1) **acceptance token name drift** for `/internal/version` conditionals, and (2) **verification checklist incompleteness** (missing explicit checks for “No ETag / No Last-Modified” and canonical-bytes constraints).

---

## **2.33 — `/internal/version` acceptance token names are canonical and non-aliasable**

Timestamp: 122825 00:00

**Decision statement (normative)**

1. **Token registry is authoritative**  
   Acceptance token names for `/internal/version` MUST match the names defined in PF04 — HDE-Governance, §2.0.2. Tools, guides, matrices, and acceptance maps MUST NOT invent aliases.  
2. **Canonical conditional semantics token name**  
   The canonical token name for the conditional semantics invariant is:  
* `INTERNAL_VERSION_CONDITIONALS_IGNORED_OK`

Any other name intended to mean “conditionals return 200 and never 304” (including `INTERNAL_VERSION_COND_200_NO_304_OK`) is **non-canon** and MUST NOT be emitted or required in acceptance artifacts.

3. **Remediation and QA escalation guides**  
   All remediation implementation guides and QA escalation remediation plans MUST use canonical token names. If a tool currently emits a non-canon alias, remediation MUST treat that as a defect and plan to converge to the canonical name.

**Clarifications**

* This addendum does not expand the token registry. It forbids aliasing and forces convergence to PF04 naming.  
* If a team believes a new token is required, it MUST be proposed as governance work (not invented in guides/tools).

**Drain targets (PF references)**

* PF04 — HDE-Governance, §2.0.2  
* PF14 — HDE-Mechanics-Guide, §14.7

**Evidence**  
None (policy addendum)

---

## **2.34 — `/internal/version` proof surface: invariant checklist must be explicit and gated before “OK” tokens**

Timestamp: 122825 00:00

**Decision statement (normative)**

1. **Explicit invariant checklist requirement**  
   Any remediation guide, QA step, or probe tool that produces `/internal/version` governed evidence MUST explicitly enumerate and verify the canon-critical invariants listed below. It is not acceptable to imply these checks by referencing PF sections only.  
2. **Canon-critical invariants (minimum set)**  
   For the canonical `/internal/version` identity response:

A. **Transport**

* GET MUST return `200`  
* HEAD MUST return `200` and satisfy parity expectations  
* Conditional requests (`If-None-Match`, `If-Modified-Since`) MUST NOT yield `304`; they MUST return `200`

B. **Headers**

* `Cache-Control: no-store` MUST be present  
* `Content-Type: application/json; charset=utf-8` MUST be present  
* `ETag` MUST be absent  
* `Last-Modified` MUST be absent

C. **Body (identity payload)**

* Body MUST be fixed-schema JSON with exactly these keys (no extras):  
  `engine_tag`, `build_commit`, `invocation_tag`, `invocation_sha256`, `emitter_sha256`, `release_id`  
* Body bytes MUST satisfy the canon “identity bytes” posture (canonical bytes, including LF termination) where applicable to the proof surface.  
3. **Token emission gating (no “false OK”)**  
   A tool MUST NOT emit any `*_OK` token unless the corresponding invariant has been verified **against the same captured bytes** that are being written as governed artifacts for that run.  
4. **FAIL\_TOOLING semantics**  
   If the run status is `FAIL_TOOLING` (or equivalent failure), the tool MUST NOT emit `*_OK` tokens for invariants that did not pass. In particular, it MUST NOT emit “integrity success” tokens (for example path-proof match or two-run identity) unless those checks demonstrably passed on the produced artifacts.  
5. **Coupling requirement (anti-mixed-target / anti-redirect drift)**  
   For each probe run, the evidence must be coupled such that the emitted tokens, captured headers, captured body, and any two-run identity digest refer to the same resolved target/response chain. If coupling cannot be established, the run MUST fail and MUST NOT emit `*_OK` tokens.

**Clarifications**

* This addendum is intentionally **implementation-neutral**: it defines what MUST be verified and how tokens MUST relate to bytes and artifacts, not how to implement the probe.  
* This addendum applies equally to DEV and OPS steps when they produce governed `/internal/version` evidence.

**Drain targets (PF references)**

* PF04 — HDE-Governance, §10.5  
* PF14 — HDE-Mechanics-Guide, §14.2; PF14 — HDE-Mechanics-Guide, §14.3; PF14 — HDE-Mechanics-Guide, §14.4; PF14 — HDE-Mechanics-Guide, §14.7  
* PF12 — HDE-Schemas-and-Artifacts, §8.3; PF12 — HDE-Schemas-and-Artifacts, §8.4

**Evidence**  
None (policy addendum)

## **2.35 — Planning MUST consult PF23 Reality Audits (components \+ pathnames)**

Timestamp: 122925 00:00

### **Decision statement (normative)**

1. **Applicability**  
   This addendum applies to all planning artifacts, including (non-exhaustive): QA plans, remediation guides, implementation guides, EPIC records, and any stepwise runbooks produced in support of an EPIC.  
2. **Mandatory PF23 consult**  
   When planning for QA, remediation, development, or any other execution work, agents MUST consult **PF23 — Reality Audits** as a primary input for:  
* component boundaries (what the “thing” is),  
* canonical pathnames and repo loci (where the “thing” lives),  
* audit-provided component metadata needed to avoid drift.  
3. **Freshness posture**  
   PF23 is updated at the end of each EPIC for every product component. Plans MUST treat PF23 as the freshest source for component/pathname reality at the time of planning.  
4. **How to use PF23 in plans (what-not-how)**  
   Planning documents SHOULD include a short “PF23 Anchors” subsection that lists:  
* the component(s) used from PF23, and  
* the key pathnames/loci pulled from PF23 that the plan will touch.

This is a traceability anchor only; it must not duplicate PF23 contents.

5. **Ownership**  
   PF23 is PO-maintained. Planning documents MUST NOT create tasks that assign PF23 updates. If PF23 appears stale or missing required component coverage, the plan MAY note that as an observation, but must not assign it as agent work.

### **Drain targets (PF references)**

* PF23 — Reality Audits  
* PF20 — HDE-Phased Epics (planning posture)  
* PF19 — Glow QA Guide (QA plan posture)  
* PF06 — Epic Process Guide (planning conventions)

### **Evidence**

None (policy addendum)

## **2.36 — Canonical Remediation Task Plan Template \+ “Execution-Ready” Gate**

Timestamp: 122925 00:00

Decision statement:

* A remediation **task plan** (DEV PRs \+ OPS tasks) that is submitted for approval MUST be execution-ready: every task is runnable as written by its assigned actor (PO for OPS; Codex for DEV PRs) with no missing inputs, no missing outputs, and no ambiguous success criteria.

* The plan MUST contain only two task types:

  * **DEV** tasks are PRs only and MUST be enumerated as `PR-01..` (no mixed-task steps).

  * **OPS** tasks are PO-run procedures only and MUST be enumerated as `OPS-01..` (no mixed-task steps).

* Discovery is allowed but MUST be explicit per task as **DISCOVERY** vs **CHANGE**.

* Cross-lane dependencies MUST be explicitly declared in the dependent task using the exact line:

  * `Inputs needed from Task <ID> during implementation: <exact items>`

  * Placeholders (e.g., “Sx”, “TBD”, “to be determined”) in this line are a mechanical blocker.

Mechanical blockers (auto-reject if present anywhere in the plan):

* Any `PR-xx` task missing a **paste-ready Codex Prompt** embedded inside that task.

* Any `OPS-xx` task missing ALL of the following: working directory assumptions, exact command lines (or explicit non-command actions), expected outputs/success criteria, and failure-handling capture instructions.

* Any deliverable that is specified only as a directory (must be a concrete lowercase file path including filename, e.g., `audit/qa/<epic>/<task_id>/<filename>`).

* Any cross-lane dependency missing the exact dependency line above, or using non-concrete “exact items.”

* Any task that mixes DEV \+ OPS work in a single task.

Clarifications:

* The plan is permitted to include a short “evidence inventory reviewed” list for provenance, but MUST inline any non-PF facts required to execute downstream tasks (quotes or precise paraphrases) rather than requiring access to external bundles.

* Remediation-only diagnostics/manifests MUST NOT be introduced under governed artifact surfaces unless explicitly framed as an ADR-worthy governance change. Default posture: remediation-only artifacts live under remediation audit paths (e.g., `audit/qa/.../remediation/...`) and do not enter governed evidence indices/mirror. (See PF04 — HDE-Governance, §10.5; PF12 — HDE-Schemas-and-Artifacts, §8.3–§8.4 for governed indexing posture.)

Drain targets (titles-only):

* PF10 — HDE-Build-Notes, §2.31

* PF12 — HDE-Schemas-and-Artifacts, §8.3

* PF12 — HDE-Schemas-and-Artifacts, §8.4

* PF04 — HDE-Governance, §10.5

Evidence: None.

---

## **2.37 — Remediation Plan “Exact Filenames” Rule for Evidence Index \+ Path Proof Artifacts**

Timestamp: 122925 00:00

Decision statement:

* Any remediation plan that includes tasks touching governed evidence indices/mirrors MUST explicitly name the exact index \+ path-proof filenames as task outputs and as embedded verification checks (inside OPS/DEV tasks; not as standalone verification-only tasks).

* Canonical placement is co-located “sibling” path proofs: `<file>.path_proof.txt` MUST sit next to `<file>` and MUST NOT be placed in an alternate directory (e.g., `docs/evidence/path_proofs/...` is non-canon).

Canonical quick reference (must be used verbatim in plans where applicable):

* Evidence index (human-readable):

  * `docs/evidence/INDEX.json`

  * `docs/evidence/INDEX.sha256`

  * `docs/evidence/INDEX.json.path_proof.txt`

  * `docs/evidence/INDEX.sha256.path_proof.txt`  
     (PF12 — HDE-Schemas-and-Artifacts, §8.4)

* Evidence index mirror (machine-readable):

  * `artifacts/evidence_index.jsonl`

  * `artifacts/evidence_index.jsonl.path_proof.txt`  
     (PF12 — HDE-Schemas-and-Artifacts, §8.3)

Clarifications:

* Plans MUST treat path-proof artifacts as first-class deliverables: if a task edits an index/mirror file, the sibling `.path_proof.txt` update is part of the same task’s outputs \+ verification.

* If a plan proposes a new file under governed surfaces, it MUST state whether it is intended to appear in the indices/mirror; absence of that statement is a blocker.

Drain targets (titles-only):

* PF12 — HDE-Schemas-and-Artifacts, §8.3

* PF12 — HDE-Schemas-and-Artifacts, §8.4

Evidence: None.

---

## **2.38 — Portability vs Provenance: How to Reference Non-PF Evidence Without Creating Execution Dependencies**

Timestamp: 122925 00:00

Decision statement:

* Remediation guides and task plans may include a short **Evidence inventory reviewed (non-PF)** list for provenance, but MUST NOT require the reader/executor to open external files to perform the work.

* If a remediation plan depends on any non-PF fact (command outputs, headers, error strings, file paths observed, specific status lines), the plan MUST embed that fact directly in the document as a short quote or precise paraphrase inside an “Observed Evidence Snapshot” section.

Clarifications:

* If an Artifact Map (or equivalent) is included, it MUST explicitly label non-PF inputs as:

  * “provenance only; not required to execute”  
     Otherwise it is treated as an execution dependency and becomes a portability blocker.

* When a non-PF observation drives a branching decision, the plan MUST include:

  * the observation to look for (exact string/status/shape),

  * the decision rule,

  * the output artifact path where the observation is captured (lowercase file path including filename).

Drain targets (titles-only):

* PF10 — HDE-Build-Notes, §2.31

Evidence: None.

## **2.39 — Remediation Task Plans: Commands and Failure Handling Are Not Plan-Approval Gates**

Timestamp: 122925 00:00

**Decision statement (normative)**

1. **Approval gate scope (tight):** For remediation **task plans** (DEV PRs \+ OPS tasks), approval MUST focus on:  
   * correct task model (OPS vs DEV; DISCOVERY vs CHANGE; no mixed tasks),  
   * correct sequencing and explicit cross-lane dependencies,  
   * concrete deliverables (lowercase paths \+ filenames),  
   * concrete verification success criteria (what “done” means).  
     Detailed command lines and step-by-step failure handling are **not** required as a plan-approval condition.  
2. **In-flight operational detail is allowed:** OPS command selection, exact CLI flags, and procedural failure handling MAY be developed **in flight** during execution, using repo reality and operator judgment, as long as the evidence posture remains intact.  
3. **Evidence posture remains non-negotiable:** Even when commands/failure handling are developed in flight, OPS execution MUST still capture:  
   * the exact commands actually run (verbatim),  
   * stdout/stderr \+ exit code (or equivalent output),  
   * the produced artifacts at the declared output paths,  
   * and any deviation notes needed to explain why a different command/flag was used.  
     This evidence MUST land under `audit/qa/...` (lowercase) with explicit filenames sufficient for later audit.  
4. **No drift on governed surfaces:** In-flight command flexibility does not permit:  
   * changing governed artifact locations or filenames,  
   * introducing new governed files without explicit statement of indexing/mirror intent,  
   * or indexing remediation-only diagnostics into governed indices/mirror.  
     Governed evidence surfaces and index/mirror rules remain enforced by the relevant addenda.

**Clarifications**

* This addendum is a **PO decision** to end repeated approval thrash and allow execution to proceed without further plan-roundtrip on command mechanics.  
* This addendum does **not** waive the requirement for concrete deliverables and verification criteria in the plan. It only removes “exact commands” and “failure handling scripts” as approval blockers.

**Supersedes / modifies**

* Modifies the “execution-ready” interpretation for remediation task plans introduced in Addendum 2.36 by removing “exact commands” and “failure handling” as approval gates, while keeping task model, deliverables, and verification gates intact.

**Drain targets (titles-only)**

* Glow QA Guide  
* Plan Templates

**Evidence**  
None.

