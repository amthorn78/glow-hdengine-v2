# 0\) Front Matter

**Name:** PF10-HDE-Build-Notes   
**Version:** v10.6.1  
Effective Date: 2026.04.20

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

**This section should be considered current and authoritative. Index all addenda numbers listed below.**

2.1) HDE-EPIC030 Dissolution carry-forward conflict — reopen grouped subtasks as active scope  
2.2) PF09.2 history-lock narrowing for HDE-EPIC030 active Dissolution subtasks  
2.3) Planning markup wrappers are non-blocking when content and meaning are unchanged  
2.4) ASK OK approval sentinel is required for plans submitted for approval  
2.5) AI agents must use retrieval-first, proof-first review posture for plan and repo analysis

# 2\) Numbered Addenda

---

## 2.1) HDE-EPIC030 Dissolution carry-forward conflict — reopen grouped subtasks as active scope

### **Why**

A planning conflict exists inside the Dissolution scope for HDE-EPIC030.

The grouped epic task set for HDE-EPIC030 explicitly includes:

* `HDE-DISS005.2`  
* `HDE-DISS005.3`  
* `HDE-DISS005.4`  
* `HDE-DISS006.3`  
* `HDE-DISS006.4`  
* `HDE-DISS006.5`

and the handoff records them as still open. At the same time, PF09.2 contains broader task-family history-only wording that can be read as if the parent `HDE-DISS005` and `HDE-DISS006` families are already satisfied and not carried forward. The conflict is therefore between the grouped epic intent and the overbroad parent-family history-lock reading, not between the grouped subtasks and any already-drained subtask-level Done state.

### **Decision / rule / clarification**

For HDE-EPIC030 planning, treat the following subtasks as active Dissolution scope in this epic:

* `HDE-DISS005.2`  
* `HDE-DISS005.3`  
* `HDE-DISS005.4`  
* `HDE-DISS006.3`  
* `HDE-DISS006.4`  
* `HDE-DISS006.5`

Do **not** reclassify them into a later phase.  
Do **not** treat them as historical-only.  
Do **not** defer them out of HDE-EPIC030 solely because the broader parent-task wording in PF09.2 can be read as history-locked.

For HDE-EPIC030 planning, the grouped epic task list is the controlling scope signal for these six subtasks.

### **Scope effect for HDE-EPIC030**

The required planning posture is:

* `HDE-DISS005.2` → `Complete in this epic`  
* `HDE-DISS005.3` → `Complete in this epic`  
* `HDE-DISS005.4` → `Complete in this epic`  
* `HDE-DISS006.3` → `Complete in this epic`  
* `HDE-DISS006.4` → `Complete in this epic`  
* `HDE-DISS006.5` → `Complete in this epic`

The following rows remain unchanged:

* `HDE-DISS005.1` → `Already complete and reused`  
* `HDE-DISS006.1` → `Already complete and reused`  
* `HDE-DISS006.2` → `Already complete and reused`

### **Planning consequence**

Epic plans, reviews, and redlines for HDE-EPIC030 must treat the six reopened subtasks above as executable Dissolution work items, not as deferred tracked issues.

If an HDE-EPIC030 planning artifact currently marks any of those six rows as:

* `Deferred with rationale`  
* `historical-only`  
* `out of executable scope`  
* or any equivalent wording

that wording is superseded for this epic and must be corrected.

### **Truth constraint**

This addendum reopens scope. It does **not** declare those rows already complete.

In particular, planning artifacts for HDE-EPIC030 must not claim that public compat output is already numeric-free merely because `HDE-DISS005.2` is now in active scope. That row remains open work to be completed in this epic, not an already-true runtime fact.

### **Canon follow-up**

Record a PF09.2 doc-delta candidate to narrow or correct the overbroad parent-task history-lock wording so it no longer suppresses these six active HDE-EPIC030 subtasks.

Use these as the next two items.

PF10 is currently reset to template/no live entries, so if your first EPIC030 addendum is `2.1`, this becomes `2.2`. PF10 says it is canonical where it explicitly speaks, and later-numbered addenda win. The EPIC030 handoff explicitly groups `HDE-DISS005.2` through `HDE-DISS005.4` and `HDE-DISS006.3` through `HDE-DISS006.5` into this epic and records them as still open, while only `HDE-DISS005.1`, `HDE-DISS006.1`, and `HDE-DISS006.2` are already done/history-only under `HDE-EPIC007`. PF09.2 currently marks `HDE-DISS005.2` as only Partial because compat public output still includes numeric `score` fields, and it marks `HDE-DISS005` and `HDE-DISS006` at the task level as done/history-only in a way that is overbroad for these six subtasks.

## 2.2) PF09.2 history-lock narrowing for HDE-EPIC030 active Dissolution subtasks

### **Why**

HDE-EPIC030 planning now explicitly reopens these Dissolution subtasks as active scope:

* `HDE-DISS005.2`  
* `HDE-DISS005.3`  
* `HDE-DISS005.4`  
* `HDE-DISS006.3`  
* `HDE-DISS006.4`  
* `HDE-DISS006.5`

But PF09.2 still contains broader parent-task history-lock language on `HDE-DISS005` and `HDE-DISS006` that can be misread as if those six subtasks are also historical-only. That wording is too broad for HDE-EPIC030 planning.

### **Decision / rule / clarification**

For HDE-EPIC030 planning and review, narrow the current PF09.2 history-only reading as follows:

* `HDE-DISS005.1` remains history-only and already complete.  
* `HDE-DISS006.1` remains history-only and already complete.  
* `HDE-DISS006.2` remains history-only and already complete.

The following subtasks are **not** covered by the history-only lock for HDE-EPIC030 planning:

* `HDE-DISS005.2`  
* `HDE-DISS005.3`  
* `HDE-DISS005.4`  
* `HDE-DISS006.3`  
* `HDE-DISS006.4`  
* `HDE-DISS006.5`

These six subtasks are active Dissolution scope in HDE-EPIC030 and must be planned as executable work, not deferred solely because of the broader parent-task wording.

### **Planning consequence**

Until PF09.2 is drained:

* planning artifacts for HDE-EPIC030 must treat the six subtasks above as active rows  
* task-family history-only wording in PF09.2 must be read narrowly, not broadly  
* no HDE-EPIC030 plan may classify those six rows as historical-only unless a later PF10 addendum explicitly reverses this decision

### **Truth constraint**

This clarification reopens scope only. It does not declare those rows already complete.

In particular:

* `HDE-DISS005.2` remains Partial on the public numeric-free compat point  
* HDE-EPIC030 planning must not claim that public compat output is already numeric-free merely because the row is active in this epic

### **Canon follow-up**

Drain this clarification into `PF09.2 - HDE Build Checklist Dissolution` by narrowing the task-level history-lock wording for `HDE-DISS005` and `HDE-DISS006`, updating task-level status where needed, and rebinding the reopened subtasks to `HDE-EPIC030`.

### PF09.2 doc delta draft

**Doc:** `PF09.2 - HDE Build Checklist Dissolution`  
**Sections:**

* `Task HDE-DISS005 — Band Thresholds & Tuning (admin)`  
* `Subtask HDE-DISS005.2 — Route thresholds to constants pack`  
* `Subtask HDE-DISS005.3 — Diffs & identity hash for tuning runs`  
* `Subtask HDE-DISS005.4 — Evidence & indexing (bands)`  
* `Task HDE-DISS006 — Category Framework (internal)`  
* `Subtask HDE-DISS006.3 — Per-channel mechanics integration`  
* `Subtask HDE-DISS006.4 — Canonical JSON & evidence`  
* `Subtask HDE-DISS006.5 — Evidence & indexing (category framework)`

#### Delta 1 — Narrow `HDE-DISS005` history-only wording

**Change:**  
Change `Task HDE-DISS005` from a broad history-only closure statement to a split posture.

**Proposed replacement posture:**

* `Task status:` change from `Done` to `Partial`  
* Replace the current task-note lock with wording in substance like:

`Status split (HDE-EPIC007 / HDE-EPIC030): HDE-DISS005.1 remains history-only and satisfied under HDE-EPIC007. HDE-DISS005.2 through HDE-DISS005.4 remain active Dissolution work and are reopened in HDE-EPIC030. The task-family row is therefore Partial rather than fully history-only.`

**Why this doc is the correct home:**  
PF09.2 is the phase checklist and is the place where the overbroad task-family history-lock currently lives. It should be narrowed there rather than left as a planning-only exception.

#### Delta 2 — Rebind `HDE-DISS005.2` through `HDE-DISS005.4` to HDE-EPIC030

**Change:**  
For each of these three subtasks:

* `HDE-DISS005.2`  
* `HDE-DISS005.3`  
* `HDE-DISS005.4`

change `Epic or card:` to `HDE-EPIC030 — Dissolution Pass 3`

Keep current subtask statuses intact unless later implementation evidence changes them:

* `HDE-DISS005.2` stays `Partial`  
* `HDE-DISS005.3` stays `Not done`  
* `HDE-DISS005.4` stays `Partial`

**Additional note for `HDE-DISS005.2`:**  
Retain the current note that the public compat output still includes numeric `score` fields and that the numeric-free public-output portion is not yet satisfied. That remains true and must not be softened.

**Why this doc is the correct home:**  
These are phase-owned execution checklist rows. Their active epic binding belongs in PF09.2.

#### Delta 3 — Narrow `HDE-DISS006` history-only wording

**Change:**  
Change `Task HDE-DISS006` from a broad history-only closure statement to a split posture.

**Proposed replacement posture:**

* `Task status:` change from `Done` to `Partial`  
* Replace the current task-note lock with wording in substance like:

`Status split (HDE-EPIC007 / HDE-EPIC030): HDE-DISS006.1 and HDE-DISS006.2 remain history-only and satisfied under HDE-EPIC007. HDE-DISS006.3 through HDE-DISS006.5 remain active Dissolution work and are reopened in HDE-EPIC030. The task-family row is therefore Partial rather than fully history-only.`

**Why this doc is the correct home:**  
Again, the conflict is inside PF09.2’s task-family wording, so the narrowing belongs in PF09.2 itself.

#### Delta 4 — Rebind `HDE-DISS006.3` through `HDE-DISS006.5` to HDE-EPIC030

**Change:**  
For each of these three subtasks:

* `HDE-DISS006.3`  
* `HDE-DISS006.4`  
* `HDE-DISS006.5`

change `Epic or card:` to `HDE-EPIC030 — Dissolution Pass 3`

Keep current subtask statuses intact unless later implementation evidence changes them:

* `HDE-DISS006.3` stays `Partial`  
* `HDE-DISS006.4` stays `Partial`  
* `HDE-DISS006.5` stays `Partial`

**Why this doc is the correct home:**  
These are the exact reopened phase rows and PF09.2 is their canonical checklist home.

#### Delta 5 — Add an explicit task-note clarification against overbroad family locking

**Change:**  
Add one short note, either once in `HDE-DISS005` and once in `HDE-DISS006`, or once in PF09.2 phase notes if you prefer a more general rule:

`Task-family history-only wording must not suppress still-open subtasks explicitly rebound into a later epic. Where subtask rows remain Partial or Not done and are explicitly assigned to an active epic, subtask-level scope controls over broader parent-task history wording.`

**Why this doc is the correct home:**  
This prevents the same ambiguity from recurring the next time a task family is partially historical and partially reopened.

## 2.3) Planning markup wrappers are non-blocking when content and meaning are unchanged

### **Why**

A review blocker was raised because a planning document line was wrapped in backticks, even though the underlying planning content, field name, meaning, and required adjacency were unchanged.

That is non-substantive markup, not a planning defect.

For planning and review artifacts, markdown wrappers such as inline backticks are display-layer formatting. They do not, by themselves, change planning meaning, scope, PF09 mapping, PF14 binding, acceptance posture, sequencing, or closure truth.

### **Decision / rule / clarification**

Effective immediately, in Epic Plans, QA Plans, reviews, remediation guides, closeout memos, and other planning or review documents, markdown-only wrapper differences are non-blocking when all of the following remain true:

* the same required field name is present  
* the same required content is present  
* the same required ordering or adjacency is present  
* the meaning is unchanged  
* no executable command, code, schema, JSON, token spelling, path string, endpoint string, or other machine-sensitive content is being altered

This means that wrapping a planning line, label, or literal in backticks is not, by itself, a blocker.

### **Conforming review posture**

These are non-blocking by default in planning artifacts:

* backticks around a label such as `Includes:` when the label is still plainly present  
* backticks around a PF title, task ID, subtask ID, token name, or short literal used only for human-readable planning text  
* other markdown-only styling differences that do not change meaning or required structure

A reviewer may still note such formatting as optional cleanup, but it must not block approval.

### **What still blocks**

This addendum does not weaken real validation.

The following remain blocking when they are wrong, missing, or changed in meaning:

* missing required fields  
* incorrect field names  
* wrong PF09.x document, task ID, or subtask ID  
* wrong PF14 reference  
* wrong disposition  
* broken section order when section order is required  
* changed or incorrect token spellings  
* changed or incorrect path strings, endpoint strings, commands, schemas, JSON, or code  
* any markup usage that actually changes meaning, hides required text, or breaks machine-sensitive content

### **Rule of interpretation**

For planning artifacts, review must follow substance over markdown presentation.

If the question is whether a required planning field exists, the test is:

* is the required field text present in substance and in the required place

The test is not:

* is the field rendered without markdown wrappers

### **Non-conforming blocker examples**

The following blocker statements are non-conforming unless the wrapper actually changes meaning or machine-sensitive content:

* “Block approval because `Includes:` is wrapped in backticks.”  
* “Fail the plan because a required planning label is inline-code styled.”  
* “Treat backticks alone as a formatting-lock failure in a human-readable planning document.”

### **Notes**

This addendum applies to planning and review documents only.

It does not apply to:

* canonical JSON  
* schemas  
* code  
* commands  
* executable snippets  
* machine-read artifacts  
* acceptance maps  
* token registries  
* governed evidence artifacts  
* any other content where literal bytes or exact machine interpretation matter

### **Drain targets**

* **PF27 — Canon Plan Templates**  
  Add an explicit rule that markdown-only wrappers in planning documents are non-blocking when required fields, ordering, and meaning remain unchanged.  
* **PF03 — Technical Writing Best Practices**  
  Add a review-posture note that inline markdown styling differences must not be escalated into blockers unless they alter required content or machine-sensitive literals.  
* **PF19 — Glow QA Guide**  
  Add the same non-blocking planning-review posture for Live QA plans and QA plan reviews, limited to non-executable planning text.

## 2.4) ASK OK approval sentinel is required for plans submitted for approval

### **Why**

A review treated the presence of an `ASK OK?` line in a plan as if it were stray text or a blocker.

That is incorrect for approval-submitted planning artifacts.

For plans that are being submitted for approval, `ASK OK?` is a required approval sentinel. Its presence is intentional and must not be treated as an error, noise, or a blocker by itself.

### **Decision / rule / clarification**

Effective immediately, when a planning artifact is being submitted for approval, it MUST include an explicit `ASK OK?` approval sentinel.

This applies to approval-submitted planning artifacts, including:

* Epic Plans  
* Implementation Plans  
* QA Plans  
* remediation plans  
* other plan-form artifacts whose purpose is to request approval before execution

For these artifacts:

* the presence of `ASK OK?` is required  
* `ASK OK?` is non-blocking by default  
* reviewers must not classify `ASK OK?` as stray text, formatting noise, or a blocker merely because it appears in the document

### **Conforming review posture**

The following review statements are conforming:

* `ASK OK? is present as the required approval sentinel.`  
* `ASK OK? is not a blocker.`  
* `ASK OK? remains required for approval-submitted plans even when other review issues exist.`

### **What still blocks**

This addendum does not weaken real review standards.

The following may still block approval when applicable:

* missing required sections  
* incorrect PF mappings  
* incorrect task, subtask, token, path, endpoint, command, schema, or evidence references  
* broken section order where order is required  
* missing required approval sentinel altogether

### **Rule of interpretation**

For approval-submitted plans, the correct test is:

* is the required `ASK OK?` approval sentinel present where the artifact’s approval posture expects it

The incorrect test is:

* does the reviewer personally prefer the document without that line

### **Scope note**

This addendum governs planning artifacts submitted for approval.

It does not change separate review-prompt output rules that require a reviewer response to end with a final decision line such as `ASK OK` or `REVISE AND RESUBMIT`.

In other words:

* `ASK OK?` inside the plan is the plan’s approval-submission sentinel  
* `ASK OK` as the final line of a review response is the reviewer’s verdict format

These are different surfaces and must not be conflated.

### **Drain targets**

* **PF27 — Canon Plan Templates**  
  Add an explicit rule that approval-submitted plans MUST include `ASK OK?` as the approval sentinel and that its presence is non-blocking.  
* **PF06 — Epic-Process-Guide**  
  Add review-posture language clarifying that approval-submitted planning artifacts use `ASK OK?` as a required submission marker and that reviewers must not treat it as stray text.  
* **PF03 — Technical Writing Best Practices**  
  Add a review-discipline note that required approval sentinels in planning artifacts are substance-bearing markers, not optional presentation text.

This fits PF10’s current live-addendum posture and cleanly resolves the issue without changing the underlying review standards.

## 2.5) AI agents must use retrieval-first, proof-first review posture for plan and repo analysis

### **Why**

Review drift and false blockers recur when AI agents reason from memory, partial snippets, display-layer artifacts, or guessed repo loci instead of proving claims from the current artifact set and current repo reality.

Existing canon already requires full retrieval of governing passages before asserting contradictions and already requires validated loci in plans. What is still missing is an explicit tool-order and proof-order rule for AI agents.

### **Decision / rule / clarification**

Effective immediately, AI agents reviewing plans, remediation guides, QA plans, repo audits, closeout artifacts, or related review documents MUST use a retrieval-first, proof-first workflow.

#### **Source order**

Use sources in this order:

1. **PF10 first**, where it explicitly speaks.  
2. The **current artifact under review**, read end-to-end.  
3. The **owning PF canon home** for each specific issue.  
4. **Repo-reality proof** for any claimed path, command, endpoint, environment variable, test ID, artifact path, or component home.

#### **Tool order**

Use tools in this order:

1. **file\_search / full-source retrieval first** for uploaded documents, PF documents, Epic Plans, Implementation Plans, QA Plans, audits, and closeout artifacts.  
2. **Container inventory commands** next when repo reality matters, using minimal proof commands such as repo-root discovery and directory inventory.  
3. **Exact-string repo search first** with `rg -n --fixed-strings` for:  
   * task IDs  
   * subtask IDs  
   * token names  
   * headings  
   * route strings  
   * command strings  
   * filenames  
   * artifact keys  
   * environment variable names  
   * other exact literals  
4. **Regex `rg`** only when exact-string search cannot prove or disprove the claim.  
5. **Broader semantic or exploratory search** only after exact search fails.

#### **Proof rules**

* Do not rely on truncated viewer snippets, ellipsized passages, or partial excerpts as proof. Reopen the full source first.  
* Distinguish explicitly between:  
  * **canon requirement**  
  * **observed repo reality**  
  * **inference**  
* Any unproven locus, path, route, command, flag, token spelling, or environment variable name remains **UNKNOWN** or **BLOCKED**. Do not guess it into existence.  
* Review findings MUST anchor to verbatim source text and controlling proof, not to paraphrase or memory.  
* Web lookup is not a substitute for uploaded-file truth or repo-local truth.

#### **Conforming review posture**

A conforming AI review may say, in substance:

* the current artifact says X  
* the owning PF home says Y  
* repo search proves Z  
* therefore the issue is Blocker, Suggestion, Nit, or no issue

#### **Non-conforming review posture**

The following are non-conforming:

* using memory before current-source retrieval  
* using broad semantic search before exact lookup on known strings  
* asserting repo path, command, route, or env-var existence without proof  
* treating truncated or ellipsized text as trustworthy evidence  
* inventing near-match token names, paths, flags, headings, or IDs  
* blocking on display-layer artifacts without first resolving source truth

### **Scope note**

This addendum governs retrieval and proof posture only.

It does not change canon precedence, acceptance semantics, portability rules, or the single-home policy. It clarifies how AI agents must prove what they are claiming before they block or approve.

### **Drain targets**

* **Epic-Process-Guide**  
   Add explicit AI review/retrieval order and proof-first repo-review posture.  
* **Canon Plan Templates**  
   Add exact search and validated-locus tool-order guidance for plans, remediation guides, and reviews.  
* **Glow QA Guide**  
   Add the same retrieval-first, proof-first tool-order rule for QA plans, Live QA reviews, and QA closeout analysis.

This addendum fits the direction already present in the current process canon: PF10 gives live override precedence, PF06 already requires full retrieval before asserting contradictions, and PF27 already requires validated loci and rejects truncation-based reasoning. The addendum would make the tool discipline explicit instead of leaving it implied.

\<eof\>