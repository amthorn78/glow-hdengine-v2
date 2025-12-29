
# 0\) Front Matter

**Name:** PF10-HDE-Build-Notes   
**Version:** v8.6.4  
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

