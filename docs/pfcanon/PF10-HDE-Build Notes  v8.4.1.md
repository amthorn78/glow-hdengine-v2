# 0\) Front Matter

**Name:** PF10-HDE-Build Notes   
**Version:** v8.4.1  
**Status:** Living  
**Invocation tag:** INV-f2ac55d77ce9aacc

## Purpose

This file is a **working scratchpad for new, not-yet-merged documentation**. Treat it as the current source of truth **only for the specific items it explicitly covers**. For everything else, PF-Canon (PF01, PF02, PF04, PF05, PF09, PF12, PF14, PF19, PF20, etc.) remains the single home.

---

**Precedence and versioning**

* For any topic explicitly covered in this scratchpad, its content **temporarily supersedes canon** until those changes are reviewed and merged into the relevant PF docs.

* If multiple addenda exist for the same or similar scope (for example “ADDENDUM 1”, “ADDENDUM 2”, “ADDENDUM 3”), the **highest-numbered / latest addendum is the only authoritative one**.

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

TEMPLATE — Addendum Entry (do not edit/remove)

##   \<number\>. \<short, action-oriented title\>

 Timestamp: \<mmddyy hh:mm\>  
 Details: \<specific information to drain to canon, its origin, and any evidence available\>

## Addendum Index:

**This section should be considered current and authoritative. Index all addenda numbers listed below.**

1\. LIVE QA Planning NOT part of Epic Planning Workflow.

2\. PF14 .role clarification

3\. Planning Failures 

4\. Directory Names Must Always Be Lower-Case

5\. Canonical Evidence Path Binding Validation for Acceptance Tokens

6\. Determinism Env Pins is a Single Canonical Evidence Surface for DETERMINISM\_ENV\_PINS\_OK

7\. Token Introduction Discipline During Epic Planning (ADR \+ Conflict Check \+ No Midflight Additions)

8\. — ADR: AB/BA Composite Identity Token Name Canonicalization

9\. — ADR: Epic Close-Pack Filename \+ QA Root Normalization

10\. — ADR: Error Parity Scenario Expansion Must Be Deterministic

11\. — ADR: PF09 Subtask Closeout Uses Evidence-Binding First (No New Evidence Families Without a Gap)

12\. — ADR: /internal/version Coupling Proof Uses a Single Governed Log Artifact

# 3\) Build Notes Addenda

## 1\. LIVE QA Planning NOT part of Epic Planning Workflow.

Timestamp: 121725 23:52  
Details:  
Status tag: CANON UPDATE / CONSISTENCY (process)

Context (problem being solved)

* Live QA is a required Close Gate activity and has real execution requirements (discovery artifact and QA RCA/doc-delta summary) in Epic-Process-Guide.  
* Live QA also has real runbook requirements (artifact-first pattern, behavior-run vs artifact capture/analysis) in Glow QA Guide.  
* However, forcing detailed Live QA planning into the Epic Plan / implementation workflow creates a planning deadlock: the runbook details often depend on post-implementation reality (actual surfaces, artifact families, infra facts, and what can be proven), and attempting to “solve” that upfront causes thrash and blocks Epic planning entirely.

Decision (rule, normative)

1. Live QA planning MUST NOT be part of Epic planning or implementation planning.  
2. The Epic Plan MUST include only a single statement that Live QA is required for eventual epic close, and may name the governing docs by title (Epic-Process-Guide; Glow QA Guide).  
3. Detailed Live QA plans/runbooks (commands, step-by-step checks, QA\_ROOT structure, where to capture prod-facing behavior, how to land artifacts, etc.) MUST be authored as a separate QA artifact/work product during the Close Gate stage, not inside the Epic Plan.  
4. Thoth/Lead review MUST NOT reject or block an Epic Plan for lacking a detailed Live QA runbook, provided the Epic Plan clearly marks Live QA as required for close.

Clarifications (to avoid loopholes)

* This does not weaken Live QA. It changes when and where the plan is written. Epic-Process-Guide still requires Live QA discovery and QA RCA/doc-delta outputs for Live QA epics at execution/close.  
* Glow QA Guide still governs how Live QA plans are written when they are written, including the behavior-run vs artifact capture/analysis split.  
* Even if an epic’s primary purpose is Live QA evidence consolidation, the PF20 Epic Plan should only state the requirement and the intended QA deliverable (a runbook \+ evidence), while the actual runbook content lives outside PF20.

Required canonical updates to drain (titles-only targets)

* Epic-Process-Guide: Add an explicit statement near Live QA discovery/RCA requirements (see §0.4.1) that these are execution/close gate requirements and MUST NOT be treated as Epic Plan prerequisites.  
* Glow QA Guide: Add an explicit “workflow placement” statement near the Live QA planning material (see the Live QA pattern section) that Live QA runbooks are created after Epic Plan approval and should not be embedded in PF20 epic plans.  
* HDE Phased Epics: Add an explicit template rule in the epic record template’s QA rails section that it must not contain a Live QA runbook and must only state “Live QA required for close” (with titles-only references). (Rationale: prevent planning blockage and duplication, while keeping the requirement visible.)

Evidence

* No code/evidence artifacts. This addendum is a process clarification intended to prevent planning stalls and to align the three canonical process homes (epic process, QA process, epic planning template).

## 2\. PF14 role clarification

ADDENDUM 2 — PF14 Role Clarification (No Governance, No Tokens)  
Timestamp: 121725 23:58  
Details:  
Status tag: CANON UPDATE / SCOPE CLARIFICATION (doc roles)

Context (problem being solved)  
PF14 has been repeatedly treated as if it can:

* define acceptance tokens,  
* curate token rosters for specific surfaces (for example `/internal/version`), or  
* act as a planning authority for epic acceptance language.

That creates drift and planning deadlock because governance and token validity are owned elsewhere, and a “mechanics/components reference” doc is not the place to decide what is provable, registered, and acceptable for close.

Decision (rule, normative)

1. PF14 MUST NOT have any role in governance.  
2. PF14 MUST NOT define, rename, alias, or curate acceptance tokens.  
3. PF14 MUST NOT be used as a planning authority. It may inform planning, but it does not govern planning structure, acceptance token sets, or close requirements.  
4. PF14’s role is strictly:  
   * a components and operational-surface reference, and  
   * a descriptive reference for bytes and operational components (what they are, what fields exist, what the surface does),  
     without asserting governance constructs (tokens, registries, close gates, mandatory acceptance sets).

Routing rules (single-home enforcement)

* Token registry, token naming, token semantics, and enforcement live in the Governance doc (PF04). If a token name is not registered there, it is not valid for acceptance artifacts.  
* Epic planning template, section structure, and baseline close requirements live in the Epic planning doc (PF20) and Epic process doc (PF06).  
* Evidence families, Evidence Index, machine mirror, and artifact path governance live in Schemas and Artifacts (PF12) and QA Guide (PF19).  
* CLI/API bytes, surface contracts, and error envelope/public-byte requirements live in CLI/API Vendor Ref (PF05).  
* PF14 may describe a surface or component, but it must not “promote” that description into governance language.

Allowed content in PF14  
PF14 MAY include:

* component inventories and descriptions (modules, surfaces, operational subsystems),  
* byte-level descriptions of operational payloads (fields, types, invariants),  
* “behavior notes” phrased as descriptive constraints (what must be true of the component),  
* pointers (titles-only) to the governing homes for tokens, evidence, and planning.

Disallowed content in PF14  
PF14 MUST NOT include:

* token lists (even “helpful” duplicates),  
* token aliases (for example legacy abbreviations),  
* acceptance matrices, proof requirements, or close-pack requirements,  
* planning instructions (how to structure an epic record, what artifacts must exist for close, what QA rails are required).  
  If PF14 currently contains any of the above, it is considered doc drift and must be drained to the correct home.

Reference style rule (to prevent reintroducing drift)  
When PF14 needs to mention governance or acceptance:

* PF14 MUST reference the governing doc by title and section, and  
* MUST NOT restate token names, acceptance lists, or evidence paths as authoritative content.  
  Example pattern: “Acceptance tokens are governed by the token registry in the Governance doc; this section describes the component fields only.”

Implications for reviews and planning

* Reviewers MUST NOT require an Epic Plan to adopt token names “because PF14 says so.” If PF14 implies a token set, that is automatically treated as a canon routing bug and must be resolved via ADR and doc-delta, not by inventing tokens in plans.  
* Epic Plans (PF20 records) MAY reference PF14 to describe an operational component or payload shape, but acceptance tokens and evidence bindings must be sourced from their proper homes.

Required canonical updates to drain (titles-only targets)

* PF14: Remove any governance/token management language and replace with titles-only pointers to the governing homes.  
* PF04: Remains the only authority for token registry and naming.  
* PF20/PF06/PF19/PF12/PF05: No role change; ensure cross-references do not imply PF14 owns tokens or planning.

Evidence

* No code/evidence artifacts. This addendum is a process and doc-role clarification intended to prevent token drift and planning blockage.


## 3\. Planning Failures

### 3.1 Prevention Policy: Evidence bundle cross-check for local-bundle deliverables

Decision statement

When a deliverable claims a “local bundle” of governed artifacts under a specific directory (example: `artifacts/ops/internal_version/*`), the Epic Plan must explicitly state:

1. The complete required bundle paths (titles-only, full paths, no byte restatement), sourced from the canonical bundle definition, and  
2. Any shared or global governed artifacts required for acceptance (example: determinism env pins), including their canonical paths, when they do not live under the local bundle root.

Purpose: prevent path guessing, missed evidence, and late-stage rework during token to evidence binding.

Normative requirements (what must be true)

* The Epic Plan’s “required evidence” list for the deliverable MUST be a complete inventory of paths required to satisfy the acceptance tokens it claims.  
* If any required evidence lives outside the deliverable’s “local bundle” directory, the plan MUST name that evidence explicitly and give its canonical path.  
* If the plan references a canonical bundle definition section by title instead of listing all paths, it MUST still list:  
  * any overrides, exclusions, or additions, and  
  * any shared or global evidence required outside the local bundle root.  
* If the plan proposes any non-canonical alternative path for an acceptance binding, it MUST be routed via ADR (no silent substitution).  
* The token\_evidence\_matrix MUST match the Epic Plan’s required-evidence paths for that deliverable.  
* Evidence Index and machine mirror MUST reflect the same canonical paths (including path-proofs) for the evidence referenced by acceptance.  
  Options considered  
* Option A: Require the plan to list all bundle paths directly (titles-only, no byte restatement).  
* Option B: Allow the plan to reference a canonical bundle definition section by title, but require explicit local overrides and explicit shared/global dependencies.  
  Recommendation

Use Option A for epic-owned bundles. Allow Option B only when the canonical section already lists the exact path set used, with no alternatives, and the plan still explicitly calls out shared/global dependencies.

Canon touchpoints (drain targets)

This policy is temporary here and must be drained into:

* PF20 (Epic Record Template): requirement for deliverable evidence lists to be complete and explicit about shared/global evidence outside a local bundle.  
* PF19 (QA Guide): token\_evidence\_matrix completeness rules and cross-check requirement against the Epic Plan deliverable evidence list.  
* PF12 (Schemas and Artifacts): canonical bundle definition patterns and explicit guidance for shared/global evidence dependencies.  
  Optional: PF06 (Epic Process Guide) as a review gate/checklist item for epic plan approval.  
  Implementation impact

Reduces “path drift” review cycles and prevents missing artifacts caused by implicit assumptions about directory-local versus shared/global evidence.

Classification

NEW CANON / CONSISTENCY

Lead linkage

Addresses the failure mode where determinism env pins (or other shared evidence) are omitted from a deliverable’s required evidence list and therefore easy to miss during binding and indexing.

---

### 3.2 RCA: Why tokens and paths were not included (and how to prevent recurrence)

RCA-1: Token modeling drift (root cause)

**Failure mode**  
PF14-level behavioral requirements (example: “Last-Modified absent”, “frozen key order”) were incorrectly treated as acceptance tokens even when the canonical token registry did not register those token names.

**Why it happened**

* No explicit “token registry validation” gate during plan authoring and review.  
* Cross-doc aliasing or informal naming patterns increased the chance of ad hoc token invention.

**Corrective action**  
Remove unregistered token names from acceptance claims and represent the behavior as verified checks within the governed evidence and verifier outputs, while binding acceptance only to registry-approved tokens.

**Preventative policy to drain**

* Plan Preflight: every token name used in an Epic Plan and token\_evidence\_matrix must be validated against the canonical token registry. Unregistered tokens must be routed via ADR plus doc-delta, not silently adopted.

**Drain targets**

* PF20 (Epic Plan acceptance section): “token registry validation is required.”  
* PF04 (Governance): reinforce registry authority and explicitly forbid acceptance tokens outside the registry.  
* PF19 (QA Guide): require token registry validation as part of matrix review.  
  ---

  RCA-2: Close-pack completeness miss (root cause)

**Failure mode**  
The plan included some close artifacts (example: manifest) but omitted required close-pack items (example: close report) and/or the required close-pack acceptance token, causing an approval failure later.

**Why it happened**

* Close-pack requirements were not treated as a plan-authoring gate.  
* Focus drift toward matrix/index artifacts caused the PF06 close-pack file set to be missed.

**Corrective action**  
Add the complete close-pack file list and the required close-pack acceptance token into baseline acceptance for every epic plan.

**Preventative policy to drain**

* Plan Preflight: a mandatory close-pack completeness check must run at plan submission time. Epic Plans must not be considered approvable unless the close-pack baseline is present.

**Drain targets**

* PF06 (Epic Process Guide): include close-pack completeness as a planning approval gate.  
* PF20 (Epic template baseline tokens/evidence): include required close-pack artifacts explicitly.  
* PF19 (QA Guide): ensure the matrix includes the close-pack bindings.  
  ---

  RCA-3: Evidence-path ambiguity for shared versus local artifacts (contributing factor)

**Failure mode**  
Shared/global evidence (example: determinism env pins) was assumed to be “implicitly available” and was not explicitly listed in the deliverable’s required evidence bundle, even though acceptance tokens depended on it.

**Why it happened**

* No explicit requirement to declare shared/global evidence dependencies when a deliverable claims a local bundle directory.  
* Similarly named artifacts across directories increased confusion and encouraged incorrect bindings.

**Corrective action**  
Require explicit inclusion of shared/global evidence in the deliverable’s required evidence list, with canonical paths, and ensure token\_evidence\_matrix plus index/mirror plus path-proofs point to the same canonical evidence.

**Preventative policy to drain**

* Evidence bundle cross-check for local-bundle deliverables (see §3.1).  
* Canonical path cross-check for token bindings: token to evidence bindings must be validated against the canonical evidence catalog before approval.

**Drain targets**

* PF20 (deliverable evidence requirements): explicit shared/global dependency listing.  
* PF19 (matrix discipline): matrix must mirror the plan’s evidence list and must be canon-path validated.  
* PF12 (artifact catalog): clarify shared/global evidence surfaces and disambiguate similarly named artifacts where possible.

## 4\. Directory Names Must Always Be Lower-Case

Timestamp: 121726 00:05  
Details:  
Status tag: CANON CONFIRMATION / DRIFT PREVENTION

Verification (already documented)

* Epic-Process-Guide explicitly requires lowercase directory names in canonical path examples and requirements, including repository roots like `docs/`, `artifacts/`, `audit/qa/`, `schemas/`, and per-epic QA trees like `audit/qa/hde-epic017/logs/`. It also forbids introducing mixed-case paths like `Audit/QA/...` in new specs and QA plans.  
   PF06-Canon-Epic-Process-Guide v…  
* Glow QA Guide explicitly requires all new directories created under governed roots to be all-lower-case (at minimum under `audit/`, `docs/**`, and `artifacts/**`) and treats mixed-case/upper-case directories there as a QA failure, not cosmetic drift.  
   PF19-Canon-Glow QA Guide v1.5.3

Rule (normative clarification)

1. All directories in the repository and application codebase MUST use lowercase ASCII names.  
2. This applies to every directory, including (but not limited to): source code, scripts, schemas, catalogs, docs, artifacts, audit trees, and QA subtrees.  
3. Introducing any mixed-case or upper-case directory name is non-conforming. Under governed roots, it is explicitly a QA failure.  
    PF19-Canon-Glow QA Guide v1.5.3

Remediation posture (when drift exists)

* If mixed-case directories exist, they are treated as legacy drift and MUST be normalized to lowercase, not copied forward into new work.  
   PF06-Canon-Epic-Process-Guide v…  
* Any renames that affect governed artifact paths MUST be accompanied by the required index and mirror updates (human Evidence Index, machine mirror, and path-proofs) in the same PR, per the evidence discipline

## 5\. Canonical Evidence Path Binding Validation for Acceptance Tokens

 Timestamp: 2025-12-17  
 Status: NEW CANON (process discipline, acceptance integrity)

Context  
 Acceptance tokens in Epic Plans and token\_evidence\_matrix can be bound to the wrong artifact path when similarly named artifacts exist. This creates mechanical review failures and repeat resubmission loops.

Rule (normative)

1. Every acceptance token to artifact binding that appears in an Epic Plan and in token\_evidence\_matrix MUST be validated against the canonical evidence catalog before approval or merge.

2. If the evidence catalog defines a fixed canonical path for a token’s evidence surface, the plan and matrix MUST bind to that exact path.

3. Any binding to a non-canonical path is a mechanical blocker and MUST be corrected before approval. If a non-canonical path is truly required, it MUST be routed as an explicit ADR and drained into the correct canonical home.

4. The Epic Plan, token\_evidence\_matrix, Evidence Index, machine mirror, and path-proofs MUST be consistent with each other for every token that is claimed as satisfied.

Minimum required artifacts that MUST agree when a token is claimed

* Epic Plan required evidence list (per deliverable)

* token\_evidence\_matrix row for the token

* docs/evidence/INDEX.json entry for the bound artifact

* artifacts/evidence\_index.jsonl mirror record for the same artifact\_key and discovered\_physical\_path

* the corresponding path-proof file referenced by the mirror record (proof\_anchor)

Enforcement posture (implementation-neutral)

* A human review checklist line MUST exist and be treated as pass/fail.

* An automated validator MAY be added, but the rule does not depend on automation.

Drain targets (titles only, with section anchors)

* Schemas and Artifacts: Evidence catalog and fixed-path surfaces (add explicit “validation required” language near the evidence catalog section).

* Glow QA Guide: token\_evidence\_matrix discipline and preflight validation requirement.

* HDE Phased Epics: Epic Plan acceptance section requirements for token to artifact bindings.  
   Optional: Epic-Process-Guide as an explicit plan approval gate.

Impact  
 Prevents evidence-path misbinding regressions from reaching lead review cycles and reduces avoidable REVISE AND RESUBMIT loops caused by mechanical path conflicts.

## 6\. Determinism Env Pins is a Single Canonical Evidence Surface for DETERMINISM\_ENV\_PINS\_OK

Timestamp: 2025-12-17  
 Status: CANON RECONCILIATION NEEDED (clarity and enforcement, no path change)

Context  
 Multiple “env pins” artifacts exist. Without an explicit rule, Epic Plans and token\_evidence\_matrix may bind DETERMINISM\_ENV\_PINS\_OK to the wrong file, creating a canon conflict at review time.

Rule (normative)

1. DETERMINISM\_ENV\_PINS\_OK MUST be satisfied only by the canonical determinism env pins governed log:

* audit/gates/determinism/env\_pins.log

* audit/gates/determinism/env\_pins.log.path\_proof.txt

2. DETERMINISM\_ENV\_PINS\_OK MUST NOT be bound to artifacts/proofs/env\_pins.txt (or any other similarly named file).

3. When DETERMINISM\_ENV\_PINS\_OK is claimed, all acceptance ledgers MUST reference the canonical log, and indexing parity MUST be correct:

* token\_evidence\_matrix references audit/gates/determinism/env\_pins.log

* docs/evidence/INDEX.json points the determinism env pins artifact\_key to audit/gates/determinism/env\_pins.log

* artifacts/evidence\_index.jsonl mirrors that exact discovered\_physical\_path and uses audit/gates/determinism/env\_pins.log.path\_proof.txt as proof\_anchor

4. Any deviation is a mechanical blocker. The plan must be corrected, not “interpreted.”

Clarification (to reduce confusion, non-authoritative)  
 Other env pins snapshots may exist for other proof contexts. They do not satisfy DETERMINISM\_ENV\_PINS\_OK unless they are the canonical governed log surface defined above.

Drain targets (titles only, with section anchors)

* Schemas and Artifacts: determinism env pins evidence surface definition (make the “only valid surface” language explicit).

* HDE Phased Epics: baseline determinism pins requirement for epic close acceptance (explicitly name the canonical log path).

* Glow QA Guide: token\_evidence\_matrix row guidance for DETERMINISM\_ENV\_PINS\_OK and index/mirror parity requirements.

Impact  
 Makes REV-001 class issues mechanically unambiguous at planning time and prevents “similarly named artifact” confusion from stalling epic approval.

“REV-001 class issues” means a **repeatable category of mechanical review blockers** where an epic plan (or its acceptance ledger) **binds a token to the wrong evidence artifact path**, in a way that **conflicts with canon**.

In REV-001 specifically, the failure mode was:

* Token claimed: `DETERMINISM_ENV_PINS_OK`

* Bound evidence in the plan: `artifacts/proofs/env_pins.txt`

* Canonical evidence surface: `audit/gates/determinism/env_pins.log` (and its `.path_proof.txt`)

* Result: the plan’s acceptance binding was **canon-invalid**, so approval was blocked until corrected.

What makes something “REV-001 class” (the pattern):

* A token→artifact binding is **path-sensitive** and canon defines a **single authoritative path**.

* The plan/matrix uses a different path (often because filenames are similar).

* The mismatch then cascades: token\_evidence\_matrix, Evidence Index, machine mirror, and path-proofs can’t be made consistent without changing the binding.

* It’s not a “design disagreement” or “needs discussion” issue. It’s a **mechanical correctness** issue: fix the binding or don’t merge.

Typical symptoms:

* “This token is satisfied, but the artifact you cited isn’t the canonical surface for that token.”

* “Your matrix points to X, but PF12 says Y.”

* “Index/mirror can’t reference both without duplicating or inventing evidence surfaces.”

Why it matters:

* It wastes cycles (REVISE AND RESUBMIT loops) on something that should be caught by a preflight check.

* It risks shipping acceptance artifacts that look complete but are structurally invalid under governance.

How we prevent “REV-001 class” issues:

* Treat token→artifact binding as a **schema validation** problem: every binding must be cross-checked against the canonical evidence catalog before approval.

* Where canon defines a single path, treat any deviation as a **blocker**, not something to interpret.

## **7\. Token Introduction Discipline During Epic Planning (ADR \+ Conflict Check \+ No Midflight Additions)**

**Decision statement (normative rail):**  
Acceptance tokens referenced in an Epic Plan are **governance-controlled names** and **must** match the canonical token roster. **Unregistered tokens in a plan are mechanical blockers** and must not be introduced “midflight” during revise/resubmit unless explicitly requested and routed through an ADR \+ Doc‑Delta path.

r6 v3 Epic Plan HDE-EPIC022

**Rule (what must be true):**

1. **Single-home authority for token names.**  
   Token rosters are single-home: other documents and plans must **not restate or invent** token lists; they must reference the canonical roster and use the **exact** canonical names.  
    PF04-Canon-HDE-Governance v1.6.4  
2. **No ad-hoc “new tokens” during planning.**  
   During an Epic planning revise/resubmit loop, the plan **must not introduce new acceptance tokens** unless **explicitly requested** (by Lead review) or required due to a clearly identified canon gap. If a behavior must be enforced and no token exists, default posture is:  
   **state it as a non-token mechanical requirement** under the deliverable and prove it via tests/evidence, rather than tokenizing it.  
3. **If (and only if) a new token is genuinely required, it must be routed, not invented.**  
   A plan may *propose* a new token **only** when all of the following are true:  
   * **ADR is present in the plan’s ADR list** and explicitly states: token name, one-sentence semantics, intended evidence surface(s), and drain targets.  
   * **Conflict check is performed** against existing canonical tokens (no duplicates, no synonyms, no “near matches”).  
   * The token is **registered via Doc‑Delta** in the canonical token home before it can be required as an acceptance claim. (“New token requires doc delta.”)  
      r6 v3 Epic Plan HDE-EPIC022  
     PF04-Canon-HDE-Governance v1.6.4  
4. **Mechanical enforcement: “token roster validation” is a required preflight gate.**  
   Every token name listed in:  
   * PF20 §2.1.5 (Tokens and Evidence) and  
   * the token/evidence matrix  
     must be validated against the canonical roster **before** a plan can be approved (and ideally before submission). Unregistered tokens are treated as **mechanical blockers**, not style issues.  
      r6 v3 Epic Plan HDE-EPIC022

**Implementation impact (why this exists):**

* Prevents the exact failure mode where a plan becomes **mechanically impossible** to approve because it requires a token that cannot validly be claimed under governance.  
   r6 v3 Epic Plan HDE-EPIC022

**Drain targets (PF10 is temporary; these rules must land elsewhere):**

* **PF04 — Governance:** reinforce/clarify “token roster single-home” \+ “new token requires Doc‑Delta” \+ explicit “unregistered token in plan is a mechanical blocker.”  
   PF04-Canon-HDE-Governance v1.6.4  
  PF04-Canon-HDE-Governance v1.6.4  
* **PF06 — Epic Process Guide:** add an explicit “token roster preflight” line item to PLAN/CRD review gates.  
* **PF20 — Phased Epics:** add a short normative note under §2.1.5 conventions: “plans may not introduce new tokens without ADR \+ Doc‑Delta; otherwise use non-token requirements.”  
* **PF09 / PF14:** remove/stop listing token names that are not in the canonical roster (plans should not be forced into token invention because a checklist doc drifted).

---

### RCA — Why r5 v3 (EPIC022) Was Not Approved (and why token drift keeps recurring)

**Event / failure:**  
r5 v3 introduced **CLI\_STDERR\_ONLY\_ON\_ERROR\_OK** as a required acceptance token for D2.  
Lead review (r6) flagged this as a **mechanical blocker** because the token is **not registered** in the canonical roster; governance requires exact token names and states that a “new token” requires an explicit Doc‑Delta (and should not appear implicitly in a plan).

### **Root cause**

**Token registry validation was not enforced at plan-authoring time.**  
A token was added to the plan as if it already existed in governance, without an ADR proposing the token and without verifying it against the canonical roster. That makes the plan’s acceptance posture impossible to satisfy under governance rules.

### **Contributing factors (why drift keeps happening)**

1. **Cross-doc token drift pressures plan authors into invention.**  
   PF09 itself lists **CLI\_STDERR\_ONLY\_ON\_ERROR\_OK** under the streams-discipline subtask, which makes it easy to assume it’s a valid canonical token even when it is not actually registered in the governance roster.  
2. **No explicit “midflight token freeze” norm in the revise/resubmit loop.**  
   Without a freeze rule, token lists get “tuned” during planning iterations, which is exactly when governance disputes are most expensive.  
3. **Tokenization used as a convenience for expressing behavior.**  
   The stream-discipline requirement is real, but the *representation choice* (new token vs non-token requirement under existing CLI/showcompat tokens) wasn’t forced through a decision rail early, so it surfaced late as a blocker. r6 explicitly frames this as a decision: enforce as non-token requirement vs introduce a new token via doc delta.  
    r6 v3 Epic Plan HDE-EPIC022

### **Corrective actions (the “solution” to eliminate constant token drift)**

These are intentionally **mechanical** (they remove debate surface area):

1. **Token roster preflight gate (hard).**  
   A plan cannot be submitted/approved unless every token in §2.1.5 and the matrix is validated against the canonical roster. This turns drift into a fast fail, not a multi-day argument.  
    r6 v3 Epic Plan HDE-EPIC022  
2. **Default posture: don’t mint tokens to express behavior.**  
   If PF05/PF09 already specify the behavioral constraint (like stream discipline), treat it as a **non-token requirement** unless governance explicitly asks for a token. r6 already recommends this exact posture for the EPIC022 D2 case.  
    r6 v3 Epic Plan HDE-EPIC022  
3. **If a new token is truly necessary: ADR \+ conflict check \+ Doc‑Delta, or it doesn’t exist.**  
   This removes “random” token creation: new tokens become deliberate governance changes with explicit blast radius and evidence surfaces.  
    r6 v3 Epic Plan HDE-EPIC022  
   PF04-Canon-HDE-Governance v1.6.4  
4. **Drain drift out of PF09/PF14 (stop the upstream reintroduction).**  
   PF09 should not function as a token source; it must not list tokens that aren’t in the canonical roster, because that predictably forces plan churn.

5. PF09 should only CONSUME tokens, not create them.

## 8\. — ADR: AB/BA Composite Identity Token Name Canonicalization

Type/Tag: CANON RECONCILIATION NEEDED

Decision:

* The **only canonical acceptance token name** for AB/BA composite identity is: **`COMPOSITE_ABBA_IDENTITY_OK`**.

* Any alternate spellings or legacy variants (including PF19 wording variants) are **non-canonical** and MUST NOT appear as acceptance tokens in Epic Plans, acceptance maps, or token/evidence matrices.

* If an epic inherits legacy wording from a doc, the plan may include a **one-line clarification** (“legacy name → canonical `COMPOSITE_ABBA_IDENTITY_OK`”), but the **claimed token name remains canonical**.

* Any proposal to introduce a “new” AB/BA identity token name is prohibited unless routed through **an ADR \+ Governance doc-delta**, with a **conflict/synonym check** against the existing roster.

Scope:

* All Epic Plans, acceptance artifacts (acceptance maps \+ token/evidence matrices), token libraries, and PF docs that reference AB/BA identity acceptance.

Canon touchpoints:

* PF04 — Canon-HDE-Governance (token roster authority; naming \+ deprecations)

* PF19 — Canon-Glow QA Guide (token library section; legacy wording to drain)

* PF20 — Canon-HDE-Phased Epics (baseline acceptance posture; token usage conventions)

Implementation impact:

* All acceptance artifacts MUST use `COMPOSITE_ABBA_IDENTITY_OK` exactly (case \+ spelling).

* Any CI lint / reviewer checklist that validates token names MUST treat legacy variants as failures (or auto-detect and require correction).

* Future doc-drain work MUST remove/replace legacy AB/BA token wording in PF19 and any other PF docs that mention it.

Notes:

* This addendum does not introduce a new token; it **standardizes the canonical name** to eliminate naming drift.

---

## 9\. — ADR: Epic Close-Pack Filename \+ QA Root Normalization

Type/Tag: CANON UPDATE

Decision:

* Epic close-pack artifacts MUST use this canonical filename pattern:

  * `audit/EPIC-<NNN>_close_report.md`

  * `audit/EPIC-<NNN>_MANIFEST.json`

  * Where `<NNN>` is a **zero-padded 3-digit epic number** (example: `022`).

* Epic QA root directories MUST be **lower-case** and MUST use this canonical pattern:

  * `audit/qa/hde-epic<NNN>/` (example: `audit/qa/hde-epic022/`)

* Plans and implementations MUST NOT introduce parallel alternate spellings for the same epic (examples of disallowed alternates: `EPIC022`, `EPIC_022`, `audit/QA/...`, `audit/qa/HDE-EPIC022/...`).

* If legacy artifacts exist under non-canonical names, they are treated as **deprecated**; do not create new ones under the deprecated pattern.

Scope:

* All epics; specifically any work that produces PF06 close-pack artifacts and PF19 QA-root artifacts.

Canon touchpoints:

* PF06 — Canon-Epic-Process-Guide (close-pack requirements \+ expected artifact set)

* PF19 — Canon-Glow QA Guide (QA root posture; token/evidence matrix location conventions)

* PF20 — Canon-HDE-Phased Epics (baseline close tokens and required close artifacts)

* PF10 Addendum 4 — Directory Names Must Always Be Lower-Case (alignment; not superseded)

Implementation impact:

* Epic implementations MUST generate and commit close-pack files at the canonical paths above.

* Epic Plans MUST reference the canonical close-pack file paths explicitly (no naming ambiguity).

* Evidence indexing/mirroring that references close-pack artifacts MUST point to the canonical file paths (no duplicate index rows under alternate names).

---

## 10\. — ADR: Error Parity Scenario Expansion Must Be Deterministic

Type/Tag: ADR RESOLUTION

Decision:

* Any new/expanded **error parity scenario** used for acceptance (including DB-unavailable and closed-rails vendor attempt) MUST be reproducible under **determinism pins \+ closed rails**, without reliance on external network or a live database.

* Preferred posture: exercise the **real codepath** using a deterministic failure trigger (controlled injection / harness-level deterministic failure), producing stable envelopes and stable stored artifacts.

* Allowed fallback: if real-codepath deterministic triggering is not feasible, use a deterministic stub layer **only** to the extent required to produce the canon error envelope and parity artifacts (no live I/O).

* The acceptance proof MUST consist of stored parity artifacts for both sides of the parity claim (Reader/HTTP and CLI) and must be indexable under governed evidence surfaces.

Scope:

* All epics that claim Reader↔CLI parity closure or add required parity scenarios (including PF09 HDE-SEPA002.5 style work).

Canon touchpoints:

* PF09 — Canon-HDE-Build Checklist (HDE-SEPA002.5 parity closure expectations)

* PF19 — Canon-Glow QA Guide (required scenario semantics; matrix discipline)

* PF12 — Canon-HDE-Schemas and Artifacts (parity evidence family paths \+ indexing/mirror requirements)

* PF04 — Canon-HDE-Governance (closed-rails refusal policy and acceptance discipline)

Implementation impact:

* Parity artifacts MUST be generated from deterministic runs (no flake acceptance).

* Any scenario added MUST have a stable scenario identifier (so stored artifacts do not churn).

* Evidence Index \+ machine mirror MUST be updated in the same PR as any new parity artifacts (no “later indexing”).

---

## 11\. — ADR: PF09 Subtask Closeout Uses Evidence-Binding First (No New Evidence Families Without a Gap)

Type/Tag: CANON UPDATE

Decision:

* When closing a PF09 subtask that is described as “captured elsewhere” / “piecemeal,” the default closure method is to **bind existing governed evidence** (tests \+ artifacts) into the epic’s acceptance artifacts (acceptance map \+ token/evidence matrix) rather than creating new evidence families.

* Creating a new evidence family for closeout is allowed only if the epic includes a **gap statement** (“what is missing from existing evidence”) and the new evidence aligns to PF12’s governed artifact conventions.

* Closure is not considered complete unless the acceptance artifacts **explicitly map** the PF09 subtask to concrete evidence (no implicit “it exists somewhere else”).

Scope:

* Epic planning and epic closeout across all phases; applies whenever PF09 tasks/subtasks are being closed.

Canon touchpoints:

* PF09 — Canon-HDE-Build Checklist (task/subtask closure posture)

* PF12 — Canon-HDE-Schemas and Artifacts (evidence family governance \+ indexing/mirror rules)

* PF19 — Canon-Glow QA Guide (token/evidence matrix discipline)

* PF20 — Canon-HDE-Phased Epics (deliverables \+ acceptance posture)

Implementation impact:

* Reduces duplicate evidence creation and prevents “new artifact families” from becoming a stealth scope increase.

* Forces explicit closure binding for PF09 subtasks that otherwise linger due to ownership ambiguity.

* Reviewers can validate closure from the acceptance artifacts without hunting for “where it was captured.”

---

## 12\. — ADR: /internal/version Coupling Proof Uses a Single Governed Log Artifact

Type/Tag: ADR RESOLUTION

Decision:

* The governed proof artifact for /internal/version coupling \+ two-run identity is a single log artifact:

  * `artifacts/ops/internal_version/two_run_identity.log`

* This log MUST include, at minimum:

  * Two-run identity result: explicit statement that two consecutive captures are byte-identical (or not), with the compared digests/bytes-identifiers.

  * Coupling verification result: explicit pass/fail checks that the six /internal/version fields match their governing identity sources (by path/title reference), including `release_id` coupling.

  * Rails posture \+ determinism pins reference (names-only pointers to the governing evidence surface; the determinism pins themselves remain proven by their canonical log).

* No new acceptance tokens are introduced for “coupling proof.” The coupling proof is **evidence bound under existing tokens** (identity \+ internal-version token set), consistent with PF10 token discipline.

Scope:

* Any epic that claims /internal/version identity coupling and/or two-run identity closure.

Canon touchpoints:

* PF12 — Canon-HDE-Schemas and Artifacts (internal\_version evidence families; two-run identity log family)

* PF14 — Canon-HDE-Mechanics Guide (six-field /internal/version identity envelope requirements)

* PF04 — Canon-HDE-Governance (acceptance tokens \+ identity coupling posture)

* PF19 — Canon-Glow QA Guide (matrix discipline; indexing parity rules)

* PF20 — Canon-HDE-Phased Epics (baseline determinism \+ acceptance discipline)

Implementation impact:

* Implementation MUST produce `artifacts/ops/internal_version/two_run_identity.log` with deterministic, reviewable content (not an implied proof).

* Acceptance artifacts MUST bind coupling claims to this log (and related governed identity artifacts) rather than inventing new token names.

* Evidence Index \+ machine mirror MUST include this log when it is produced/updated (same-PR discipline).

Notes:

* This addendum intentionally avoids introducing a second “provenance note” artifact to prevent creating a new governed evidence family midstream; any additional narrative belongs in the epic close report unless/until PF12 is updated to govern a dedicated note artifact.

