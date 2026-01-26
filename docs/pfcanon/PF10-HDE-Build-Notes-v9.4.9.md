# 0\) Front Matter

**Name:** PF10-HDE-Build-Notes   
**Version:** v9.4.9  
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

## 1.1 Addendum Index:

**This section should be considered current and authoritative. Index all addenda numbers listed below.**

1. 2.1 Non-blocking plan formatting variance (presentation-only)  
2. 2.2 Prohibited characters in planning reviews and planning documents (backtick and ellipsis)

3. 2.3 Heading levels are non-reviewable in planning reviews (AI redline limitation)’

4. 2.4 Conjunction Pass 1 scope deferral: move remaining HDE-CONJ001 and HDE-CONJ008 to HDE-EPIC026

5. 2.5 Conjunction planning token reconciliation: PF27 and PF09 must use Governance token spellings; no new compat keyset token

# 2\) Numbered Addenda

---

 

## **2.1 Non-blocking plan formatting variance (presentation-only)**

Timestamp: 012526 11:19  
Details:  
Rule (normative)

1. Minor presentation-only formatting differences in plans MUST NOT be treated as acceptance blockers and MUST NOT block plan approval. Examples include: bolding, italics, emphasis markers, minor whitespace changes, and bullet marker style (dash vs asterisk) when the underlying content is unchanged.  
2. Reviewers MAY request presentation-only formatting changes as Nits or Caveats, but MUST NOT require them as a condition for acceptance or approval.  
3. This rule does not apply to formatting that changes meaning or breaks execution or verification. The following are not “minor formatting” and may still be blockers when violated:  
* Missing required sections or required fields mandated by a plan template  
* Broken heading hierarchy when the template requires specific heading levels  
* Any change that alters required IDs, required paths, required evidence outputs, required PASS/FAIL predicates, or required tokens  
* Any markup that makes commands non-copyable or causes literal markup characters to be executed  
* Any formatting that breaks machine readability of governed artifacts (JSON, JSONL, manifests, indexes)  
* Any prohibited placeholder or prohibited character rule that is explicitly canonized for plans (for example, ellipsis prohibition)

Drain targets (required)

* PF03 — Technical Writing Best Practices, §12.5 Live QA plan approval reviews (BLOCKERS vs CAVEATS)  
  Proposed text (merge-ready):  
  “Minor presentation-only formatting variance (for example bolding, emphasis markers, and whitespace) MUST NOT be treated as a BLOCKER and MUST NOT block approval. Record as a Nit or Caveat only, unless the formatting prevents copy/paste execution or obscures required fields, PASS/FAIL predicates, or required deliverables.”  
* PF06 — Epic Process Guide, §0.6.9 Plans are pointers; QA planning is post-implementation  
  Proposed text (merge-ready):  
  “Formatting imperfections in plan documents (for example bolding and Markdown conveniences) are not business decisions and MUST NOT block approval. Treat them as Caveats unless they prevent execution or prevent reviewers from determining pass/fail with confidence.”  
* PF19 — Glow QA Guide, §3.4.10 Plan validity lint (blockers-only; deterministic)  
  Proposed text (merge-ready):  
  Add one bullet after the blockers list:  
  “Style-only formatting (bolding, italics, Markdown conveniences) MUST NOT be treated as a plan-validity blocker. Block only on issues that prevent execution or prevent confident verification.”  
* PF04 — HDE Governance, §9.8.3 Review gate (blocking)  
  Status: already covered by existing “Formatting is not an approval gate” posture; no change required unless Thoth wants the examples expanded to include bolding/emphasis explicitly.  
* PF27 — Canon Plan Templates, §Portability vs provenance (normative)  
  Proposed text (merge-ready):  
  “Plans MUST be judged on executable clarity and evidence posture. Minor presentation-only formatting variance (for example bolding and Markdown conveniences) MUST NOT be used as an approval gate.”

## **2.2 Prohibited characters in planning reviews and planning documents (backtick and ellipsis)**

Timestamp: 012526  
Details:

Rule (normative)

1. Planning documents and planning reviews MUST NOT contain any of the following characters or sequences:  
* Backtick character (U+0060, GRAVE ACCENT)  
* Unicode ellipsis character (U+2026)  
* Any instance of three consecutive U+002E FULL STOP characters  
2. This is a prohibited-character rule, not a minor formatting preference. Violations MUST be treated as mechanical blockers for plan approval and review acceptance until removed.  
3. If a viewer shows any of these characters outside an explicit code block, reviewers MUST treat it as a potential read failure and re-open until the source text is fully visible. If the characters can be proven to exist in the source text (not a viewer artifact), they MUST be replaced before approval.  
4. If a literal example would require prohibited characters (for example language syntax that uses a triple-dot token, or code examples containing backticks), the planning document MUST NOT include that literal snippet. Use one of these alternatives:  
* Rewrite the example to avoid the prohibited characters (preferred).  
* Move the exact snippet into a repo source file or governed evidence artifact and reference it by path, without embedding the prohibited characters in the plan text.  
* For code presentation in plans: use indented code blocks or code fences made of three tilde characters, not backticks.

Approved replacements (standard placeholders)

* For omitted text or continuity:  
  * \[OMITTED\]  
  * \[OMITTED: short reason\]  
  * \[SNIP: n lines omitted\]  
  * \[LIST CONTINUES\]  
  * \[REPEAT BLOCK\]  
* For inline code-like values:  
  * Use double quotes around the literal text, or prefix with CODE:  
  * Example form: CODE: python \-m pytest \-q tests/test\_name.py

Drain targets (required)

* PF03 — Technical Writing Best Practices, §Plan and review hygiene  
  Proposed text (merge-ready):  
  “Planning documents and planning reviews MUST NOT contain the backtick character (U+0060), the Unicode ellipsis character (U+2026), or three consecutive full stop characters. Violations are mechanical blockers. Use explicit omission markers such as \[OMITTED\] or \[SNIP: n lines omitted\]. Use indented code blocks or tilde-fenced code blocks. Do not use backticks.”  
* PF06 — Epic Process Guide, §Plan review rules  
  Proposed text (merge-ready):  
  “Minor presentation-only formatting variance must not block approval. However, prohibited characters are blocking. Plans and reviews MUST NOT contain U+0060, U+2026, or three consecutive full stop characters. If present, replace them before approval using the approved omission markers.”  
* PF19 — Glow QA Guide, §Plan validity and review guardrails  
  Proposed text (merge-ready):  
  “Live QA Plans and QA reviews MUST be free of prohibited characters: U+0060, U+2026, and any three consecutive full stop characters. Presence is a mechanical blocker because it can be confused with truncation and can break portability. Use explicit omission markers and tilde-fenced or indented code blocks only.”  
* PF27 — Plan Templates, §Portability and plan lint  
  Proposed text (merge-ready):  
  “Plans MUST NOT contain U+0060, U+2026, or three consecutive full stop characters. This rule applies to Epic Plans, Implementation Plans, Live QA Plans, remediation plans, and review ledgers. Violations are blocking. Use explicit omission markers and tilde-fenced or indented code blocks.”  
* PF04 — HDE Governance, §Review gates and acceptance posture  
  Proposed text (merge-ready):  
  “Acceptance artifacts are evaluated on tokens, evidence binding, and determinism. Plan text is evaluated on portability and unambiguous meaning. Prohibited characters (U+0060, U+2026, or three consecutive full stop characters) are mechanical blockers in planning docs and reviews because they can mask truncation and degrade auditability.”  
* PF09 — HDE Build Checklist, §Task heading hygiene  
  Proposed text (merge-ready):  
  “Task headings MUST NOT include U+0060, U+2026, or three consecutive full stop characters.”

## **2.3 Heading levels are non-reviewable in planning reviews (AI redline limitation)**

Timestamp: 012526  
 Owner: PO  
 Details:

Rule (normative)

1. During planning review (including epic plans and other planning documents), heading levels MUST NOT be reviewed and MUST NOT be used as approval blockers or review defects.

2. “Heading levels” includes Markdown/Docs hierarchy markers (for example H1 vs H2 vs H3, or the count of leading heading markers).

3. Rationale: AI redline agents cannot reliably and safely redline heading-level changes without risking incorrect anchors and placement drift. Attempts to enforce heading levels in planning review increase the probability of wrong edits.

4. Reviewers MAY still review heading text content and the presence/order of required sections, but MUST do so without requiring a specific heading level.

5. This addendum supersedes any earlier planning-review guidance that treats heading-level mismatches as blockers.

Drain targets (required)

* Technical Writing Best Practices — add a rule under plan/review hygiene:  
   “Heading levels (hierarchy markers) MUST NOT be reviewed during planning review and MUST NOT be treated as blockers. AI agents cannot reliably redline heading-level changes.”

* Epic Process Guide — add a plan review rule:  
   “Do not block plan approval on heading levels. Review required headings by text and required fields by content only.”

* Canon Plan Templates — add a review posture note:  
   “Templates may show preferred heading levels, but plan approval reviews MUST NOT enforce heading levels.”

* Glow QA Guide — add to plan-validity review guardrails:  
   “Heading-level mismatches are non-reviewable in planning review and are not plan-validity blockers.”

## **2.4 Conjunction Pass 1 scope deferral: move remaining HDE-CONJ001 and HDE-CONJ008 to HDE-EPIC026**

Timestamp: 012626  
 Owner: PO  
 Details:

Rule (normative)

1. For Conjunction Pass 1 planning scope, the remaining Conjunction tasks that are not assigned inside the current epic slice are explicitly deferred to HDE-EPIC026.

2. This deferral applies to the following PF09 subtasks:

   * HDE-CONJ001.1 through HDE-CONJ001.4 (Dev HTTP Harness, single home)

   * HDE-CONJ008.1 through HDE-CONJ008.4 (Writer Surfaces, API)

3. Any Epic Plan text that presents the decision as unresolved (for example “decide whether these deferred items remain inside EPIC025 or move to a different epic”) must be treated as resolved: the destination epic is HDE-EPIC026.

4. Epic Plans for Conjunction Pass 1 must not silently drop these deferred items. They must appear in Tracked Issues as deferred scope with the explicit destination epic ID and with no acceptance claims for the deferred tasks in the current epic slice.

Drain targets (required)

* HDE-Build Checklist — Conjunction phase notes:  
   Add one short note under Phase IV that HDE-CONJ001 and HDE-CONJ008 are tracked as deferred to HDE-EPIC026 for Conjunction Pass 1 planning slices, and must not be claimed in-scope when deferred.

* Canon Plan Templates — Epic Plan Tracked Issues guidance:  
   Add one sentence that deferrals must name the destination epic ID explicitly (no “decide later” language in approved plans).

## **2.5 Conjunction planning token reconciliation: PF27 and PF09 must use Governance token spellings; no new compat keyset token**

Timestamp: 012626  
 Owner: PO  
 Details:

Rule (normative)

1. Token spellings used in Epic Plans, acceptance artifacts, and Tracked Issues must always match the Governance token registry spelling exactly. If any template or checklist uses a legacy or non-registry token spelling, plans must claim the Governance spelling only and treat the other string as canon drift until drained.

2. Conjunction checklist token lists must not introduce token drift. When PF09 references tokens using legacy names or non-registry names, the checklist must be drained to the Governance spellings below:

   * CLI\_READER\_EMITTER\_PARITY\_OK is deprecated and must be normalized to CLI\_READER\_PARITY\_OK.

   * AB\_BA\_PARITY\_OK and CLI\_AB\_BA\_PARITY\_OK are non-registry names for Conjunction parity. Normalize them to COMPOSITE\_ABBA\_IDENTITY\_OK.

   * CATEGORY\_FRAMEWORK\_OK is not a Governance token name. Where the intent is “closed Magic-10 id domain,” use MAGIC10\_DOMAIN\_CLOSED\_OK. Where the intent is “preference keyset is the canonical 10,” use PREFS\_KEYSET\_10\_OK.

   * CANON\_JSON\_OK is a non-canonical alias and must be normalized to JSON\_CANONICAL\_CHECK\_OK.

3. Internal compat “keyset contract” posture does not require minting a new Governance token for Conjunction Pass 1\. The required posture must be proven as evidence under existing tokens (for example via contract tests plus the existing catalog, canonical JSON, and determinism tokens already in the epic roster). If an Epic Plan wants to call out keyset posture explicitly, it must do so as an evidence requirement (test and proof artifact), not by inventing a token name.

4. Ownership posture for planning artifacts in this scope: Owner for Tracked Issues and ADR stubs is PO.

Drain targets (required)

* HDE-Governance — Acceptance Tokens:  
   Add an explicit note in the relevant token entries that legacy spellings listed above must not be claimed in new plans or acceptance artifacts, and that only the canonical spellings are claimable.

* HDE-Build Checklist — Conjunction tasks:  
   Replace legacy and non-registry token names in Conjunction task token lists with the canonical spellings above. Remove any token strings that cannot be reconciled to Governance spellings.

* Canon Plan Templates — Tokens and Evidence:  
   Add one line clarifying that token lists in templates are names-only, but must still be Governance-valid spellings, and any legacy names must be treated as drift and not claimed.

* Glow QA Guide — Plan validity and token usage notes:  
   Add one short reminder that plans must claim canonical token spellings only and must not mint local aliases for convenience.

\<eof\>