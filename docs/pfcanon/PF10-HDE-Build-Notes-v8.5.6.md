# 0\) Front Matter

**Name:** PF10-HDE-Build-Notes   
**Version:** v8.5.6  
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

# 2\) TEMPLATE

TEMPLATE Addendum Entry (do not edit/remove)

##   \<number\>. \<short, action-oriented title\>

 Timestamp: \<mmddyy hh:mm\>  
 Details: \<specific information to drain to canon, its origin, and any evidence available\>

## Addendum Index:

**This section should be considered current and authoritative. Index all addenda numbers listed below.**

1. Token Registry SoT enforcement for PF20 epic rosters  
   2. Acceptance tokens: PF04 registry vs PF19 QA token library (single SoT)  
   3. Live QA plan approval gate: PF19 lint \+ token SoT validation \+ mechanical-only evidence  
   4. Review source-retrieval guard: no excerpt-based claims for tokens/rails/bytes

# 3\) Numbered Addenda Begin

## **1\. Token Registry SoT enforcement for PF20 epic rosters**

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

## **2\. Acceptance tokens: PF04 registry vs PF19 QA token library (single SoT)**

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

## **3\. Live QA plan approval gate: PF19 lint \+ token SoT validation \+ mechanical-only evidence**

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

## **4\. Review source-retrieval guard: no excerpt-based claims for tokens/rails/bytes**

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

3. **If a needed canonical passage cannot be fully retrieved, the review must not “guess.”**  
    The plan review must instead record the item as blocked by insufficient canonical visibility and constrain the conclusion to what is verifiably known from retrieved canon.  
    (This formalizes the “no hallucinated defects” requirement into the review gate itself.)

