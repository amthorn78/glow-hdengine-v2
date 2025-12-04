# 0\) Front Matter

**Name:** PF10-HDE-Build Notes   
**Version:** v8.0.9  
**Status:** Living  
**Invocation tag:** INV-f2ac55d77ce9aacc

## **Purpose** 

This file is a **working scratchpad for new, not-yet-merged documentation**. Treat it as the current source of truth **only for the specific items it explicitly covers**. For everything else, PF-Canon (PF01, PF02, PF04, PF05, PF09, PF12, PF14, PF19, PF20, etc.) remains the single home.

---

**Precedence and versioning**

* For any topic explicitly covered in this scratchpad, its content **temporarily supersedes canon** until those changes are reviewed and merged into the relevant PF docs.

* If multiple scratchpad files exist for the same or similar scope (for example “ADDENDUM 1”, “ADDENDUM 2”, “ADDENDUM 3”), the **highest-numbered / latest scratchpad is the only authoritative one**.

* **Older scratchpad files are considered fully drained or obsolete.** Agents must **not** read, reuse, or reconcile content from older scratchpads once a newer one exists; only the latest file matters.

Within a single scratchpad file:

* When an entry has been drained into PF-Canon, that entry is **removed completely** from the scratchpad.

* The current version of the file therefore contains **only live, not-yet-merged items**. If a topic is not present in the latest scratchpad, assume its source of truth is the relevant PF-Canon doc.  
  ---

**Cross-references**

* Inside this file, all references to PF documents **must be titles-only** (for example “HDE-Phased Epics”, “Glow QA Guide”), never file names or version numbers in the body text.

* When editing or extending this file, ChatGPT sessions must:  
  * **Not restate PF content** here.

  * **Link by document title and section only.**

  ---

**Relationship to Build Notes and canon**

* Build notes, epic plans, and QA findings are **not canon**; they are **raw material**.

* This scratchpad is where those notes are **organized into draft canon text** before being merged into PF docs.

* Over time, the content of this file is **drained into the appropriate PF-Canon documents** (for example: PF20 for epic records, PF09 for checklist updates, PF19 for QA tokens, PF12 for schemas).

* After draining:

  * The corresponding entries are **deleted from the scratchpad**.

  * The **latest version of this file will be empty of drained entries**, so only remaining entries represent active, not-yet-merged work.

 

## USE THIS TEMPLATE

TEMPLATE — Addendum Entry (do not edit/remove)  
ADDENDUM \<number\> — \<short, action-oriented title\>  
Timestamp: \<mmddyy hh:mm\>  
Details: \<specific information to drain to canon, it’s origin, and any evidence available\>

---

# Numbered Addenda Begin

# ADDENDUM 1 — ADR: Phase Exit Criteria for Alchemical Phases

 Timestamp: 120225 16:00

Details:

This addendum records an Architectural Decision Record (ADR) for **phase exit criteria** in the alchemical delivery cycle for the Glow HD Engine. It is a **planning rule** to be drained into **HDE Phased Epics** as a short “Phase Exit Criteria” note and used by **Epic-Process-Guide** and **Glow Development Philosophy** as a reference when deciding whether to stay in the current phase or move to the next.

**Decision (phase exit criteria, per phase)**

1. **Close-out epic required.**  
    A phase is eligible to “exit” once at least one **close-out epic** in that phase has:

   * a complete epic record in **HDE Phased Epics** with `Status: Done` and a completed **Tokens and Evidence** roster for its D-goals, and

   * a close pack with Live QA evidence and Doc-Delta mapping that is indexed in the Human Evidence Index and Machine Mirror under the standard **HDE-Schemas & Artifacts** and **HDE-Build Checklist** discipline.

2. **No “Not done” foundation rows for the phase.**  
    For the phase being exited, **HDE-Build Checklist** must show:

   * no **Not done** rows for **foundation tasks** in that phase (Calcination foundations or phase-defining Dissolution/Separation tasks), and

   * any remaining **Not done** rows must be explicitly re-scoped into later phases or marked as “Won’t Do” in **HDE Phased Epics**, not left ambiguous in PF09. This follows PF13’s tenet that foundations must be clear before moving on, and that incomplete ideas must become explicit debt, not silent drift.

3. **Partial / Consolidation pending rows are debt, not blockers, when:**  
    Remaining **Partial** or **Consolidation pending** rows for a phase are treated as **carry-over debt** (not phase blockers) if and only if:

   * their notes in **HDE-Build Checklist** clearly show that they are **enhancements, tuning, or consolidation**, not missing foundational behavior, and

   * they are either:

     * linked to an **Outstanding Issue** row in **HDE Phased Epics §1**, or

     * explicitly called out in one or more future epic records as “Existing work / Debt to absorb,” so the next epic’s scope and acceptance can take them on.

4. **Tracked issues must be disposed of; none may be silently dropped.**  
    Before a phase exits, each epic in that phase that reaches `Status: Done` must:

   * list its tracked issues in **HDE Phased Epics §2.1.7**, and

   * for each issue, mark it as “Completed under \<EPIC\>”, “Carried forward to \<EPIC\>”, “Promoted to ISSUE-XXX”, or “Explicitly dropped (with rationale).”  
      A phase cannot be treated as exit-ready if any epic in that phase is `Done` in PF20 but still has unresolved, undocumented issues in reality. This aligns PF13’s “controlled change” and PF21’s phase-discipline guidance with PF20’s tracked issue rules.

5. **Phase exit is a planning decision; open work becomes cross-epic or next-phase scope.**  
    When criteria (1)–(4) are satisfied, **phase exit** is treated as a **planning decision**, not as an assertion that all work tagged with that phase is finished. Remaining work for that phase must be:

   * captured as cross-epic issues in **HDE Phased Epics §1**, or

   * explicitly listed as inputs to the next phase’s epics (for example, Dissolution sampler tuning carried into Separation’s error-envelope work).  
      This implements PF13’s instruction to avoid over-tuning and PF21’s expectation that phases do not mix: once the phase’s core aim is achieved and its debt is made explicit, new epics should be created in the next phase rather than reopening more epics in the current one.

**Applied example (Dissolution → Separation, HD Engine)**

6. **Current posture (informative, for draining later):**

   * **HDE-EPIC019 — Dissolution Pass 2** is `Done` in **HDE Phased Epics**, with D-goals (sampler core, deterministic Engine Core, dev sampler HTTP harness, sampler evidence & indexing, Live Vendor QA D6) accepted and evidenced under the standard PF06/PF09/PF12/PF19 rails.

   * **HDE-Build Checklist Phase II — Dissolution** has no **Not done** rows for its foundational tasks; remaining **Partial** cells are localized to sampler/pool tuning (`HDE-DISS003.x`) and are already represented as future work and Outstanding Issues in PF20, not as untracked gaps.

   * Cross-epic issues such as `ISSUE-017-STATELESS-JSON-QA`, `ISSUE-QA-TOKENS-LIBRARY`, and `ISSUE-APPENV-D3-GATING` are explicitly allocated in PF20 as ongoing, cross-phase concerns rather than as EPIC019-blocking tasks.

7. **ADR application (Dissolution exit):**  
    Under this ADR, the Dissolution phase for the HD Engine is now considered **exit-ready**:

   * Its designated close-out epic (**HDE-EPIC019**) is `Done` with D-goals accepted and Live QA complete.

   * No Dissolution foundation tasks remain Not done in **HDE-Build Checklist**; Partial rows are explicitly recognized as tuning/consolidation debt.

   * Cross-epic issues and residual Dissolution work are captured in **HDE Phased Epics §1** and will be scoped into future epics (likely under **Separation** and later phases), rather than keeping the meta-sprint parked in Dissolution.

**NEW CANON PROPOSAL (for later drain to “HDE Phased Epics”):**  
 Add a short **“Phase Exit Criteria”** note to **HDE Phased Epics** stating that a phase may be treated as complete for planning when:

* at least one epic in that phase is `Done` with all its D-goals accepted and evidence indexed;

* PF09 for that phase has no **Not done** foundation rows; and

* any remaining Partial or Consolidation pending tasks are explicitly carried forward as cross-epic issues or next-phase epic scope, with tracked-issue disposition per PF20 §2.1.7.

This proposal does **not** change current behavior; it formalizes the pattern already applied when leaving Calcination and now Dissolution, and should be implemented via a future PF20 Doc-Delta.

