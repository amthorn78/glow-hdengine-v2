# 0\) Front Matter

**Name:** PF10-HDE-Build-Notes   
**Version:** v11.8.9  
Effective Date: 2026.07.01

**Status:** Living  
**Invocation tag:** INV-f2ac55d77ce9aacc

## Purpose

This file is a **working scratchpad for new, not-yet-merged documentation**. Treat it as the current source of truth **only for the specific items it explicitly covers**. For everything else, PF-Canon (PF01, PF02, PF04, PF05, PF09, PF12, PF14, PF19, PF20, etc.) remains the single home.

---

## Precedence and versioning

**PF10 IS CANONICAL.** For any topic explicitly covered in this scratchpad, PF10 is the current authoritative source of truth and **supersedes all other PF canon** until that item is formally reviewed and drained into the relevant permanent PF document.

**No competing canon may be used against an active PF10 entry.** While an item remains live in this scratchpad, agents must follow PF10 for that topic and must not prefer, merge, reinterpret, or reconcile conflicting language from older PF canon.

**Later addendum wins.** If multiple addenda address the same or overlapping scope, the **highest-numbered / latest addendum is the only authoritative one**. Earlier addenda on that scope are superseded and must not be used in parallel.

**Only the latest PF10 file matters.** Older scratchpad files are **fully drained, obsolete, or both**. Agents must **not** read them, reuse them, compare them, reconcile them, or carry forward language from them once a newer PF10 exists.

**This file contains only live items.** Drained items are removed from the scratchpad. Therefore, the current version of PF10 contains only active, not-yet-merged guidance.

**Silence means canon reverts to the permanent PF home.** If a topic does **not** appear in the latest PF10, then PF10 has nothing to say about it, and the source of truth is the relevant permanent PF-Canon document.

**Operational rule for agents:** use the latest PF10 first; obey it wherever it speaks; ignore older scratchpads entirely; fall back to permanent PF-Canon only where the latest PF10 is silent.

## Cross-references

 Inside this file, all references to PF documents MUST be **titles-only** (for example “HDE-Phased Epics”, “Glow QA Guide”), never file names or version numbers in the body text.

When editing or extending this file, ChatGPT sessions must:

* Not restate PF content here.

* Link by **document title and section only**.

# 1\) TEMPLATE

TEMPLATE Addendum Entry (do not edit/remove)

##   \<number\>. \<short, action-oriented title\>

 Timestamp: \<mmddyy hh:mm\> (autofill from system info)  
 Details: \<specific information to drain to canon, its origin, and any evidence available\>

## 1.1 Addendum Index:

### **2.1) Audit Provenance Is Valid Planning Context and Must Not Be Treated as a Plan Blocker**

# 2\) Numbered Addenda

---

### **2.1) Audit Provenance Is Valid Planning Context and Must Not Be Treated as a Plan Blocker**

Timestamp: 063026

Status: Live PF10 staging decision pending permanent PF-Canon drain

Decision owner: Lead Dev

### **Details**

A plan review incorrectly treated “audit provenance” language inside an Implementation Plan as a blocker.

That interpretation is wrong.

Audits exist to preserve observed planning context, repo-reality findings, ambiguity history, drift history, risk classification, and why a piece of work is being planned. Audit provenance is allowed in Epic Plans, Implementation Plans, QA Guides, QA Plans, review artifacts, and retrospectives when it is used as planning context or source-trace context.

The valid boundary is not “no audit provenance in plans.”

The valid boundary is:

**Audit provenance may be referenced in plans, but it must not be converted into PR instructions, OPS instructions, execution authority, acceptance proof, token authority, or current repo proof without the appropriate governing source or live repo validation.**

### **Lead decision**

Audit provenance is valid and useful in planning artifacts.

It is not a blocker for a plan to include audit provenance when the audit reference explains:

* why work exists;  
* what prior review observed;  
* what risk or ambiguity was surfaced;  
* what repo area should be inspected;  
* what PF-canon or PF09 mapping may need attention;  
* why a future proof obligation exists;  
* why a gap is being carried into an epic;  
* why an implementation or QA plan includes a specific workstream.

### **Permitted use**

Plans may reference audit provenance as:

* planning context;  
* risk context;  
* discovery context;  
* source-trace context;  
* rationale for inspection;  
* rationale for a Tracked Issue;  
* rationale for an ADR stub;  
* rationale for a planned workstream;  
* rationale for a QA proof obligation;  
* rationale for a repo-validation check;  
* rationale for PF-canon drainage.

This includes wording such as:

* “Prior audit observed...”  
* “Audit provenance indicates...”  
* “The audit classified...”  
* “The audit surfaced...”  
* “Prior read-only audit reported...”  
* “Audit context for this work...”

Such wording is allowed when it does not command execution by itself and does not replace PF-canon, PF10, PF09, or repo validation.

### **Prohibited use**

Audit provenance must not be used as:

* PR instructions;  
* OPS instructions;  
* step-by-step execution procedure;  
* Codex command source;  
* acceptance authority;  
* token authority;  
* QA PASS proof;  
* OPS completion proof;  
* PF09 Done proof;  
* closeout proof;  
* current repo truth without repo validation;  
* source of invented file/path/module/test existence;  
* source of required deliverables unless the plan or PF source adopts them;  
* source of privileged live action;  
* source of secrets or external state.

Audit provenance can say why something should be inspected or planned. It cannot by itself prove that current repo contents exist, that execution succeeded, or that acceptance is satisfied.

### **Review rule**

Reviewers must not block a plan solely because it includes audit provenance.

A blocker is valid only if the plan uses audit provenance incorrectly by turning it into execution authority or proof authority.

Allowed review classification:

* No issue  
* Note  
* Context accepted  
* Planning provenance accepted  
* Repo validation required before execution  
* Keep out of PR/OPS instruction text

Forbidden review classification when audit provenance is only context:

* Blocker  
* REVISE AND RESUBMIT  
* QA-readiness blocker  
* implementation blocker  
* evidence/proof blocker  
* token blocker  
* OPS blocker  
* repo-state blocker

### **Required review test**

Before raising a blocker about audit provenance, the reviewer must ask:

1. Is the audit being used only to explain why the work exists?  
2. Is the audit being used only to guide repo inspection, PF mapping, or proof planning?  
3. Does the plan still rely on PF10, PF-Canon, PF09, and repo validation for authority?  
4. Does the plan avoid making the audit itself a command source?  
5. Does the plan avoid making the audit itself acceptance proof?  
6. Does the plan avoid making the audit itself current repo proof?

If the answer is yes, the audit provenance is allowed and not a blocker.

### **PR and OPS boundary**

Audit provenance may appear in plan context, task rationale, Tracked Issues, ADR stubs, evidence rationale, or review history.

Audit provenance should not appear as the operative instruction inside PR or OPS execution blocks.

For PR and OPS instructions, convert audit provenance into neutral work language, such as:

* inspect the current repo state;  
* validate the current route policy;  
* prove the current behavior;  
* update the governed evidence;  
* preserve the nonclaim;  
* bind the evidence under the governed root.

Do not tell Codex or an OPS executor to “implement the audit finding” as though the audit itself is the source of authority.

### **HDE-EPIC036 application**

For HDE-EPIC036, references to prior audit provenance in the Implementation Plan are allowed as planning context.

The prior blocker based on audit provenance is withdrawn.

Audit provenance may remain in the plan when it explains why the `bg:resolve --source vendor` route-policy work exists, why evidence roots are planned, or why a proof obligation is included.

The plan should only avoid making audit provenance the direct PR or OPS instruction source. The operative implementation and evidence instructions must still be grounded in PF10, PF09.5, PF05, PF12, PF14, PF19, PF27, and current repo validation.

### **Permanent PF-Canon drain targets**

#### **PF27 — Canon Plan Templates**

Drain intent:

* Clarify that audit provenance is allowed in plans as planning context.  
* Require plans to distinguish audit context from PR/OPS instructions.  
* Prohibit reviewers from blocking solely because audit provenance appears in a plan.

#### **PF06 — Epic Process Guide**

Drain intent:

* Clarify that audits are legitimate planning inputs.  
* State that audit findings may justify workstreams, Tracked Issues, and ADR stubs.  
* State that audit findings must not become execution authority unless adopted by PF-canon, PF10, plan scope, or repo validation.

#### **PF19 — Glow QA Guide**

Drain intent:

* Clarify that audit provenance can guide QA proof obligations.  
* Clarify that audit provenance does not prove QA PASS, OPS completion, acceptance, or current repo state.

#### **PF23 — Reality Audits**

Drain intent:

* Clarify the allowed role of audits as planning-time context.  
* State that audit findings may be referenced in plans but must be repo-validated for current reality claims.

#### **PF03 — Technical Writing Best Practices**

Drain intent:

* Add language for cleanly separating audit provenance, rationale, and operative task instructions.

### **Final live rule**

Audit provenance is allowed in plans.

Audit provenance is not a blocker.

Audit provenance may explain why work exists.

Audit provenance may guide inspection and proof planning.

Audit provenance must not become PR or OPS instruction text.

Audit provenance must not replace PF-canon, PF10, PF09, repo validation, QA evidence, OPS evidence, acceptance proof, or token authority.

\<eof\>