# 0\) Front Matter

**Name:** PF10-HDE-Build-Notes   
**Version:** v9.5.6  
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

1. 2.1 Simplified QA Planning and Deterministic Acceptance

2. 2.2 Non-blocking plan formatting variance (presentation-only)  
3. 2.3 Prohibited characters in planning reviews and planning documents (ellipsis only)

4. 2.4 Heading levels are non-reviewable in planning reviews (AI redline limitation)’

5. 2.5 Conjunction Pass 1 scope deferral: move remaining HDE-CONJ001 and HDE-CONJ008 to HDE-EPIC026

6. 2.6 Conjunction planning token reconciliation: PF27 and PF09 must use Governance token spellings; no new compat keyset token

7. 2.7 Planning path discipline: canon-first \+ CA/IG verbatim validation; never fabricate repo paths

8. 2.8 File minting procedure for new epics (canon-first validation; CA vetted and IG Approved quotes; Codex prompts stay attachment-free)

9. 2.9 Acceptance token minting and claim rules for epic planning  
10. 2.10 PF23 consult scope: epic planning only (not PR analysis or QA planning) \+ drift assessment stub  
11. 2.11 PR01 HDE-EPIC025  
12. 2.12 PR02 HDE-EPIC025  
13. 2.13 PR03 HDE-EPIC025  
14. 2.14 PR04 HDE-EPIC025

# 2\) Numbered Addenda

---

 

## **2.1 Simplified QA Planning and Deterministic Acceptance**

Timestamp: 012826 14:30  
 Details:  
 Rule (normative)

1. **Canonical tokens only for acceptance.** Epic Plans and QA plans MUST express all acceptance criteria using canonical token names (from PF04 – HDE Governance, or PF10 if newly minted). Freeform or ad-hoc acceptance statements are not allowed. If a needed acceptance concept has no token, it MUST be treated as out-of-scope at planning time and addressed via an ADR (to create a token) rather than written as informal text. Plans MUST NOT invent or use locally coined terms for acceptance that are not backed by PF04/PF10 tokens. This ensures every acceptance condition is deterministic and governed.

2. **No stepwise QA in initial plans.** Epic planning documents (e.g. CRDs) MUST NOT include full QA step lists or detailed test procedures. They SHALL list acceptance goals and tokens (what must be true at epic close) and MAY outline the QA approach at a high level, but the actual Live QA Plan is to be developed during implementation. Reviewers MUST NOT require an epic plan to contain a complete QA runbook as a condition for approval. Overplanning QA upfront is treated as a plan defect – plans should act as pointers to QA requirements, not as the QA script itself.

3. **Evidence-bound scope for QA steps.** Every step in a Live QA Plan or QA execution guide MUST correspond to a specific acceptance token or documented evidence requirement. No QA steps should be included “for good measure” or without a clear mapping to acceptance. Conversely, for each required token in the epic’s acceptance roster, the Live QA Plan MUST have at least one step or check producing evidence to satisfy that token. This one-to-one mapping makes the plan’s scope complete and prevents drift or unnecessary test steps. Ambiguous “nice-to-have” checks or optional verifications are not permitted unless clearly labeled as non-blocking informational only (and such cases should be rare).

4. **Validated references, no guesswork.** QA planning and execution documents MUST NOT reference any repository path, file, module, or environment variable that cannot be confirmed via canon or actual repo inspection. Every reference to implementation details in a plan must be backed by either: (a) a citation of the authoritative PF source (for example, citing HDE Architecture or Reality Audit docs for component paths), or (b) an inline quoted output from a Codex audit or implementation guide showing the real value/path. If a referenced item is not found or not validated, that is a **plan blocker** – the plan must be corrected before execution. Plans and reviews MUST treat any unverified or “assumed” path as an error (to reduce plan-vs-repo drift to zero).

5. **AI-safe review practices.** Planning reviews MUST focus on substantive correctness and MUST NOT demand edits known to be error-prone for AI editors. In particular, reviewers MUST NOT require changes to Markdown heading levels, list styles, trivial formatting, or section reorders that do not impact execution. Required sections/fields per templates must be present, but how they are stylistically formatted is not an approval gate. This rule intends to minimize scenarios where AI redline tools introduce anchor errors or document drift through non-semantic changes. Reviewers should confine their requests to things that affect execution, evidence, or clarity of acceptance, and ignore minor stylistic variances.

6. **Use of standard playbooks.** QA plans SHOULD utilize the predefined playbook steps from the Glow QA Guide (PF19) wherever applicable instead of crafting new ad hoc test logic. For example, if an epic involves database changes, the plan should invoke the standard DB schema and ingest checks from PF19, rather than entirely new queries. Deviating from playbooks is allowed only when no existing playbook covers the needed scope; any such new steps SHOULD be proposed for addition to PF19 to enrich the common playbook set. This ensures consistency and that the QA approach is canon-aligned.  
    *Non-goals:* These rules do **not** relax any existing quality or evidence requirements. They do not remove any acceptance tokens or lower the standard for PASS criteria – every epic must still meet all applicable tokens with concrete evidence. They also do not change the **ownership** of artifacts: PF04 remains the source of token definitions, PF12 of artifact schemas, etc. (we are not duplicating that content here). The aim is streamlined process, not reduced rigor. Importantly, this addendum does not introduce any new tokens or evidence types; it only governs how we plan and write QA. It is not a wholesale process change but a clarification and tightening of current best practices to reduce error rates.  
    Drain targets (required)

* **PF06 – Epic Process Guide, §0.6.9** (Plans are pointers; QA planning is post-implementation): Add explicit guidance that epic plans must not contain detailed QA steps and must only commit to tokens and evidence pointers. Emphasize that full QA execution details are deferred to implementation phase, and over-specifying them in the plan is a blocker.

* **PF06 – Epic Process Guide, §Plan review rules:** Insert a rule that plan approvers must not demand exhaustive QA procedures in the plan, nor trivial format changes, reinforcing addendum points 2 and 5\.

* **PF19 – Glow QA Guide, §3.4 (Plan validity and review guardrails):** Update the plan validity lint section to include: (a) a statement that plans must use only canonical token names for acceptance (no custom names) and must map each token to evidence steps, and (b) a note that any plan reference to a path or artifact must be validated (or it’s a plan defect). This will formalize points 1 and 4 for QA authors and reviewers.

* **PF19 – Glow QA Guide, §5.x (Playbooks Overview):** Add a reminder that IAs should leverage existing playbook sections when writing QA plans and only create new test steps if no playbook exists, to address addendum point 6\.

* **PF27 – Canon Plan Templates, §Tokens and Evidence (Epic Plan template & Live QA template):** Insert that acceptance token lists in templates are names-only and must correspond to PF04 tokens. Also clarify that the Live QA Plan’s check list should cover all tokens (ensuring completeness). This enforces traceability from plan tokens to QA steps, addressing points 1 and 3\.

* **PF27 – Canon Plan Templates, §Review guardrails:** Add that formatting or heading level issues are not blockers (point 5, already partially covered by prior addenda) and that templates illustrate structure but aren’t meant for verbatim enforcement of styling.

* **PF04 – HDE Governance, §Acceptance Tokens:** (No textual change needed for rules above; however, ensure a cross-reference note that epic acceptance must be declared via these tokens. If not already clear, add a line that project practice is to only use tokens from this registry in planning and close-out, see Epic Process Guide for process.)

## **2.2 Non-blocking plan formatting variance (presentation-only)**

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

## **2.3 Prohibited characters in planning reviews and planning documents (ellipsis only)**

Timestamp: 012526  
 Details:

Rule (normative)

Planning documents and planning reviews MUST NOT contain any of the following characters or sequences:

* Unicode ellipsis character (U+2026)

* Any instance of three consecutive U+002E FULL STOP characters

This is a prohibited-character rule, not a minor formatting preference. Violations MUST be treated as mechanical blockers for plan approval and review acceptance until removed.

If a viewer shows any of these characters outside an explicit code block, reviewers MUST treat it as a potential read failure and re-open until the source text is fully visible. If the characters can be proven to exist in the source text (not a viewer artifact), they MUST be replaced before approval.

If a literal example would require prohibited characters (for example language syntax that uses a triple-dot token), the planning document MUST NOT include that literal snippet. Use one of these alternatives:

* Rewrite the example to avoid the prohibited characters (preferred).

* Move the exact snippet into a repo source file or governed evidence artifact and reference it by path, without embedding the prohibited characters in the plan text.

Approved replacements (standard placeholders)

For omitted text or continuity:

* \[OMITTED\]

* \[OMITTED: short reason\]

* \[SNIP: n lines omitted\]

* \[LIST CONTINUES\]

* \[REPEAT BLOCK\]

For inline code-like values:

* Use double quotes around the literal text, or prefix with CODE:

* Example form: CODE: python \-m pytest \-q tests/test\_name.py

Drain targets (required)

PF03 — Technical Writing Best Practices, §Plan and review hygiene  
 Proposed text (merge-ready):  
 “Planning documents and planning reviews MUST NOT contain the Unicode ellipsis character (U+2026) or any instance of three consecutive full stop characters. Violations are mechanical blockers. Use explicit omission markers such as \[OMITTED\] or \[SNIP: n lines omitted\].”

PF06 — Epic Process Guide, §Plan review rules  
 Proposed text (merge-ready):  
 “Minor presentation-only formatting variance must not block approval. However, prohibited characters are blocking. Plans and reviews MUST NOT contain U+2026 or any three consecutive full stop characters. If present, replace them before approval using the approved omission markers.”

PF19 — Glow QA Guide, §Plan validity and review guardrails  
 Proposed text (merge-ready):  
 “Live QA Plans and QA reviews MUST be free of prohibited characters: U+2026 and any three consecutive full stop characters. Presence is a mechanical blocker because it can be confused with truncation and can break portability. Use explicit omission markers.”

PF27 — Plan Templates, §Portability and plan lint  
 Proposed text (merge-ready):  
 “Plans MUST NOT contain U+2026 or any three consecutive full stop characters. This rule applies to Epic Plans, Implementation Plans, Live QA Plans, remediation plans, and review ledgers. Violations are blocking. Use explicit omission markers.”

PF04 — HDE Governance, §Review gates and acceptance posture  
 Proposed text (merge-ready):  
 “Acceptance artifacts are evaluated on tokens, evidence binding, and determinism. Plan text is evaluated on portability and unambiguous meaning. Prohibited characters (U+2026 or three consecutive full stop characters) are mechanical blockers in planning docs and reviews because they can mask truncation and degrade auditability.”

PF09 — HDE Build Checklist, §Task heading hygiene  
 Proposed text (merge-ready):  
 “Task headings MUST NOT include U+2026 or three consecutive full stop characters.”

## **2.4 Heading levels are non-reviewable in planning reviews (AI redline limitation)**

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

## **2.5 Conjunction Pass 1 scope deferral: move remaining HDE-CONJ001 and HDE-CONJ008 to HDE-EPIC026**

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

## **2.6 Conjunction planning token reconciliation: PF27 and PF09 must use Governance token spellings; no new compat keyset token**

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

## **2.7 Planning path discipline: canon-first \+ CA/IG verbatim validation; never fabricate repo paths**

Timestamp: 012626  
Owner: PO  
Details:

Rule (normative)

1. Planning documents and planning reviews MUST NOT fabricate repo file paths, directory roots, or module loci. Every asserted path or “where this lives” statement in a plan MUST be validated using exactly one of the following methods:  
   a. **Direct PF canon citation** (preferred): cite the governing PF home(s) and align the claim to the canon-defined single homes and constraints, or  
   b. **CA vetted**: the claim is supported by a verbatim quote from the planning Codex audit, included inline in the plan, or  
   c. **IG Approved**: the claim is supported by a verbatim quote from the Implementation Guide, included inline in the plan.  
   If the plan uses “CA vetted” or “IG Approved”, the supporting material MUST be quoted verbatim. Paraphrase is not permitted for these labels.  
2. Mandatory consult rule (minimum): before a plan asserts implementation loci (paths, surface roots, directories), the author MUST consult **HDE Architecture** and **Reality Audits** as the minimum canon set for path validity. Plans MUST align “expected loci” to these canon touchpoints and MUST NOT introduce alternate roots by assumption (for example, a “src/” tree) without validation.  
3. Planning Codex audit posture: each planning session begins with a planning Codex audit. Its findings MAY be referenced inside the plan narrative as “CA vetted” **only with verbatim quoted outputs**. The planning Codex audit MUST NOT be referenced in the final instructions given to Codex for implementation (portability rule); execution prompts must be self-contained and rely only on PF canon and repo paths.  
4. File creation is permitted and expected. The rule is not “no new files.” The rule is:  
   * New files and directories MAY be created under canon-defined homes once the locus is validated (canon citation or CA vetted quote).  
   * New roots or second homes (for example, a second HTTP root) MUST NOT be assumed and require explicit justification aligned to Architecture single-home constraints.  
5. Review gate (mechanical blocker): if a reviewer encounters any unvalidated, assumed, or fabricated repo path in plan text, it is a mechanical blocker until corrected to one of the valid forms:  
   * canon-cited (PF references), or  
   * “CA vetted” with verbatim audit quote, or  
   * “IG Approved” with verbatim IG quote.  
6. Incident record (scope: EPIC025 planning drift): an approved plan asserted a “src” surface root for HTTP, adapter, and presenter loci (for example “/src/http”, “/src/adapters”, “/src/presenters”). This is severe drift because it fabricated surface roots without Architecture alignment or Reality Audit validation. Going forward, plans in this scope must treat adapter/ as the single HTTP home per Architecture and must derive concrete loci via canon citation or CA vetted quotes rather than inventing new roots.

Drain targets (required)

Epic Process Guide — add a plan review blocker rule under plan review rules:  
Proposed text (merge-ready):  
“Plans and plan reviews MUST NOT fabricate repo paths. Any asserted file path, directory root, or module locus must be validated by (a) PF canon citation, or (b) CA vetted with verbatim audit quote, or (c) IG Approved with verbatim IG quote. Unvalidated path assertions are mechanical blockers.”

Canon Plan Templates — add to portability and plan lint:  
Proposed text (merge-ready):  
“Plans that reference implementation loci MUST include path validation for every asserted locus: PF canon citation, or CA vetted / IG Approved with verbatim quotation. Plans may reference the planning Codex audit inside the plan narrative, but implementation prompts to Codex must not reference audit artifacts or attachments.”

Technical Writing Best Practices — add to plan and review hygiene:  
Proposed text (merge-ready):  
“Do not invent repo paths in plans. Validate each asserted locus with PF canon citation or with a verbatim quote labeled CA vetted / IG Approved.”

HDE-Governance — add to review gates and acceptance posture:  
Proposed text (merge-ready):  
“Plan portability includes path reality: fabricated or unvalidated repo paths in plans are mechanical blockers because they cause implementation drift and invalidate evidence binding. Validations must be canon-cited or CA/IG-quoted verbatim.”

Proposed text (merge-ready):

“Do not invent file paths in plans. If a path is needed, prove it exists or explicitly mark it as a new path with an absence-proof step.”

HDE-Governance — add to review gates and acceptance posture:

Proposed text (merge-ready):

“Plan portability includes path reality: fabricated or unproven repo paths in plans are mechanical blockers because they cause implementation drift and invalidate evidence binding.”

## **2.8 File minting procedure for new epics (canon-first validation; CA vetted and IG Approved quotes; Codex prompts stay attachment-free)**

Timestamp: 012626  
 Owner: PO  
 Details:

Rule (normative)

1. **File minting is allowed and expected.** New files and directories MAY be created as part of an epic. The control is not “no new files”. The control is: do not invent homes, do not invent roots, and do not invent paths.

2. **Every asserted file path or “where this lives” claim in a plan MUST be validated using exactly one method:**

   * **Canon-cited:** direct PF canon citation that grounds the home or locus, or

   * **CA vetted:** a verbatim quote from the planning Codex audit included inline in the plan, or

   * **IG Approved:** a verbatim quote from the Implementation Guide included inline in the plan.  
      If a plan uses “CA vetted” or “IG Approved”, the supporting material MUST be quoted verbatim in the plan. Paraphrase is not permitted for these labels.

3. **Minimum canon consult before minting paths:** before a plan asserts any surface root, directory home, or module locus, the author MUST consult:

   * **HDE Architecture** (single homes, deny-list, “no second home” posture), and

   * **Reality Audits** (current repo reality for where surfaces actually live).  
      Plans MUST align their placement decisions to these touchpoints and MUST NOT introduce alternate roots by assumption (for example a “src/” tree).

4. **Planning Codex audit posture (one-time per planning session):**

   * A planning Codex audit is performed once at the beginning of the planning session.

   * Its findings MAY be referenced inside the plan narrative as “CA vetted” only with verbatim quoted outputs.

5. **Codex portability rule (hard):**

   * The final instructions given to Codex for implementation MUST NOT reference “CA vetted”, “IG Approved”, the planning audit, or any attachments.

   * Codex prompts must be self-contained, using only PF canon references (PFxx — Title, §X.Y) and repo paths.

6. **Minting new files under existing canonical homes is normal.** If PF canon establishes the home (example: HTTP belongs under the canonical HTTP home; evidence belongs under governed evidence roots), plans MAY mint new files under that home without extra ceremony. Validation is satisfied by a canon citation or a CA vetted quote that confirms the home.

7. **New roots and second homes are prohibited by default.**

   * A plan MUST NOT propose a new top-level surface root (or a second home for an owned component) unless the plan includes:  
      a. the canon alignment rationale (Architecture single-home posture), and  
      b. a CA vetted quote showing the repo does not already contain an appropriate canonical root for the purpose, and  
      c. an explicit statement of why the existing canonical homes cannot be used.  
      If these conditions are not met, the plan must treat the proposal as invalid and revert to reuse-first under the canonical homes.

8. **Evidence file minting (clarity without clutter):**

   * Plans MUST name the **primary governed evidence outputs** that will be committed and indexed for the epic or PR.

   * Plans SHOULD avoid vague family phrases such as “plus step logs” and SHOULD avoid wildcards in evidence-output lines.

   * If a tool produces a high-churn set of member logs, the plan MAY treat the governed output as a single primary artifact (for example, a manifest or bundle) and state that member files are referenced by that primary artifact, provided the plan names the primary governed artifact by exact path and filename and keeps evidence binding deterministic.

Drain targets (required)

* **Epic Process Guide** — add a planning rule and review blocker:  
   “Plans may mint new files, but must validate every asserted locus by PF canon citation or by verbatim CA vetted or IG Approved quotes. Planning audits may be referenced in the plan narrative but must never appear in Codex implementation prompts.”

* **Plan Templates** — add to Implementation Plan template guidance:  
   “Every path claim must be canon-cited or CA vetted or IG Approved with verbatim quotes. Codex prompts must not reference audits or attachments. New roots require explicit Architecture alignment and CA vetted absence evidence.”

* **Technical Writing Best Practices** — add to plan hygiene:  
   “Do not fabricate repo paths. Use canon citations or verbatim CA vetted or IG Approved quotes. Do not carry audit references into Codex prompts.”

* **Glow QA Guide** — add to plan validity guardrails:  
   “Evidence outputs must be named as primary governed artifacts. Avoid wildcards and ambiguous families. High-churn member logs may be represented via a primary manifest or bundle where canon supports it.”

## 2.9 Acceptance token minting and claim rules for epic planning

### Purpose

Define a conservative, deterministic workflow for introducing and claiming acceptance tokens in epic planning, without plan-local token invention.

### Scope

Applies to all epic plans, implementation plans, QA plans, close packs, and any artifact that claims acceptance via tokens.

### Definitions

* Token: A named acceptance gate used in plans and evidence.

* Token claim: A statement that a token is satisfied or will be satisfied.

* Obligation: A requirement expressed without a token claim, backed by explicit commands, artifacts, and a pass predicate.

* Mint: Creating a new canonical token entry by adding it to PF10 Build Notes as an addendum.

### Non-negotiable constraints

* No plan-local minting: Plans MUST NOT invent new token spellings inside plan text.

* Canon sources for tokens: Tokens may be claimed only if they exist in PF04 or PF10.

* Exact spelling: Token spellings used in plans and evidence MUST match the canonical spelling in PF04 or PF10 exactly.

* Evidence before claim: A token MUST NOT be claimed unless the plan includes concrete proof wiring for it (commands, concrete artifact paths and filenames, pass predicate).

### When a new token is warranted

A new token SHOULD be introduced only when both are true:

* The behavior must be expressed as a reusable acceptance gate.

* No existing token in PF04 or PF10 covers the same semantics.

If the behavior is epic-local or can be handled without a named gate, use an obligation.

### Token minting workflow

#### Step 1: Check for an existing token

If a token is needed for determinism during development, the planner MUST check:

* PF04 for an existing token.

* PF10 for an existing token.

Outcomes:

* If a matching token exists, use it. Do not mint a new one.

* If no matching token exists, proceed to Step 2\.

#### Step 2: Raise an ADR during planning

If no token exists, an ADR MUST be raised during the planning process to request approval to mint the token.

The ADR MUST include:

* Proposed token name (exact spelling).

* Meaning (one line).

* Scope (surface it governs).

* Claimable evidence contract:

  * Command(s) to produce proof.

  * Concrete artifact path(s) and filenames that must exist.

  * Pass predicate.

* Non-goals.

* Drain target: PF04.

#### Step 3: If ADR approved, mint in PF10 during planning

If the ADR is approved, the token MUST be minted by adding it as a PF10 Build Notes addendum during planning, with the finalized fields from the ADR.

Once minted in PF10, the token is canonical.

#### Step 4: Plan claim gate

After the token exists in PF10, the epic plan may claim the token, subject to the evidence before claim rule.

If the token does not yet exist in PF04 or PF10, the plan MUST use an obligation and MUST NOT claim a token.

#### Step 5: Drain to PF04

Minted tokens should eventually be drained into PF04 as the long-term registry. Until drained, the token remains canonical in PF10.

### How this is baked into epic planning

Epic planning MUST include a Token Inventory step before plan finalization:

* List every token the plan intends to claim.

* For each token, record whether it is present in PF04 or PF10.

* If any intended token is missing from both PF04 and PF10:

  * Raise an ADR during planning.

  * If approved, mint the token in PF10 during planning.

  * Only then may the plan claim it.

### Downstream document rules

* PF19 may reference tokens for QA execution, but MUST use PF04 or PF10 spellings exactly and MUST NOT invent new token names.

* PF12 evidence indexing and mirroring should include concrete evidence artifacts required by any token claims.

* PF14 must not define or curate tokens. If PF14 needs to mention tokens, it may only point to PF04 or PF10 as the canonical source.

### Drain targets

This PF10 addendum should be drained into canonical homes:

* PF04: Token registry ownership, token definition schema, and claimability rules.

* PF06: Epic planning gate requirement to run Token Inventory and enforce ADR-based minting when needed.

* PF19: QA guidance restriction to PF04 or PF10 token spellings only.

* PF12: Requirement that token-claim evidence outputs are concrete, filename-specific, and indexable.

## **2.10 PF23 consult scope: epic planning only (not PR analysis or QA planning) \+ drift assessment stub**

Timestamp: 012626  
Owner: PO  
Details:

Rule (normative)

1. **Reality Audits (PF23) are post-epic audits.** They are updated at the end of an epic and are therefore not a stable, in-flight source for PR or QA work.  
2. **Consult scope (allowed and required):**  
   PF23 MUST be consulted during **Epic planning** only (Epic Plan creation or revision). In that context, PF23 may be used to ground component boundaries and canonical loci and prevent fabricated paths.  
3. **Consult scope (disallowed):**  
   PF23 MUST NOT be consulted for:  
   * PR analysis (including PR review, remediation review, and diff-first approval loops), or  
   * QA planning (including Live QA plans and runbooks).  
     These activities must rely on the owning PF canon homes for contracts, evidence, and mechanics, plus repo reality.  
4. **Non-token posture:**  
   PF23 consult must not appear as a required deliverable, a required check, or an acceptance token in Implementation Plans, QA plans, reviews, or acceptance artifacts.  
5. **Drift assessment trigger (normative):**  
   If any PF23 Reality Audit statement contradicts PF canon, that contradiction MUST be treated as **development drift requiring evaluation**, not as an automatic correction in either direction.  
   The contradiction may represent one of three conditions:  
   * **Canon defect:** PF canon is incorrect or outdated.  
   * **Implementation drift:** the repo drifted away from canon without an approved change path.  
   * **Necessary reality shift:** development changes were required in reality and canon has not yet been updated to reflect them.  
6. **Drift assessment protocol (stub; required posture, not full process):**  
   Until a full protocol is published, use this minimal, non-optional stub whenever PF23 contradicts canon:  
   * **Record the contradiction** as a drift item with:  
     * PF23 claim (quote or precise paraphrase),  
     * the conflicting PF canon claim (quote or precise paraphrase), and  
     * the impacted epic/surface.  
   * **Classify the drift** into exactly one bucket (tentative):  
     * canon defect, implementation drift, or necessary reality shift.  
   * **Do not “fix” by assumption.**  
     No plan, review, or QA artifact may treat the contradiction as resolved unless the PO explicitly adjudicates the resolution path.  
   * **Resolution routing is PO-owned.**  
     The PO decides whether the fix is: canon update, implementation remediation, or formalized exception with canon follow-up.  
7. **Routing for PR analysis and QA planning (when PF23 is out of scope):**  
   When PF23 is out of scope, reviewers and plan authors must instead rely on the owning PF homes by title (examples: HDE Architecture for component single homes, HDE Governance for tokens and transport policy, HDE CLI/API reference for wire contracts, HDE Schemas and Artifacts for governed evidence families and canonical evidence paths, HDE Build Checklist for required tasks, HDE Mechanics Guide for component anchors, Glow QA Guide for runbook discipline, Epic Process Guide for PR posture).

Drain targets (required)

* Canon Plan Templates — revise planning guidance to clarify PF23 is consulted during Epic planning only and must not be required for Implementation Plans or Live QA plans; add the drift assessment trigger stub for PF23 contradictions.  
* Glow QA Guide — remove or revise any language that treats PF23 consult as part of QA planning or QA execution; add a note that PF23 contradictions are drift items and are not adjudicated during QA planning.  
* HDE Build Checklist — remove or revise any rule that mandates PF23 consult for QA planning, remediation planning, or in-flight PR work; restrict PF23 consult to Epic planning only; add a brief drift trigger note for PF23 contradictions.  
* Epic Process Guide — add a reviewer rule: do not use PF23 as a source of blockers in PR analysis; use PF canon homes and repo reality; if PF23 contradicts PF canon, record it as a drift item for PO adjudication (do not resolve unilaterally).

## 2.11 PR01 HDE-EPIC025

### Provenance (Original → Remediation 1 → Remediation 2 → Remediation 3\) (REQUIRED; primary)

* Implementation Doc defines PR-01’s scope as hardening the compat surface’s internal contract and enforcing endpoint catalog discipline.  
  Source: Implementation Doc  
  Evidence pointer: “PR-01 — Compat Surface internal contract and endpoint catalog discipline” (section header)  
* Implementation Doc requires the compat endpoint to be internal/admin and POST-only for the actual compat computation surface.  
  Source: Implementation Doc  
  Evidence pointer: PR-01 → “Compat internal contract: enforce INTERNAL / ADMIN surface”  
* Implementation Doc requires GET to be health-only probing and to carry **no request body**.  
  Source: Implementation Doc  
  Evidence pointer: PR-01 → “Compat internal contract…” → “GET /api/compat/v1 is HEALTH-only (probing) … carries no request body.”  
* Implementation Doc requires the endpoint catalog entry for `/api/compat/v1` to reflect POST-only/internal and include an env gate field.  
  Source: Implementation Doc  
  Evidence pointer: PR-01 → “Compat internal contract…” → “Add a focused test at `tests/http/test_compat_endpoint_contract.py` … `docs/ENDPOINTS_CATALOG.json` contains an entry for `/api/compat/v1` … and a non-empty env gate field.”  
* Implementation Doc defines acceptance tokens for endpoint catalog correctness (catalog existence \+ internal classification \+ env gate presence).  
  Source: Implementation Doc  
  Evidence pointer: PR-01 → “Acceptance tokens (minimal list; explicit; do not invent)”  
* Attempt 0 (Original PR) implemented a `/api/compat/v1` handler and tests, and updated governed artifacts including endpoint catalog and evidence index artifacts.  
  Source: Original PR  
  Evidence pointer: “\#\# File Changes” table (shows docs/ENDPOINTS\_CATALOG.json, docs/evidence/INDEX.\*, artifacts/evidence\_index.jsonl, tests)  
* Attempt 0’s GET handler was not purely probe-only; it computed compat when `a_id`/`b_id` query params were present, which conflicts with the Implementation Doc’s “health-only probing” intent.  
  Source: Original PR  
  Evidence pointer: “\#\# File Diffs” → `engine/http/compat_handler.py` diff showing GET branch calling `compat_public(...)` when query args exist (see `get_ids_only()`)  
* Attempt 0 added endpoint-catalog validation via a dedicated test file (`tests/http/test_endpoint_catalog.py`) asserting POST-only/internal\_admin/a7\_eligible/env\_gate.  
  Source: Original PR  
  Evidence pointer: “\#\# File Diffs” → `tests/http/test_endpoint_catalog.py` (new file)  
* Attempt 0’s PASS 2 failed CI due to step logs manifest check: the PR’s evidence/index/path-proof changes caused a mismatch requiring refresh.  
  Source: Original PR  
  Evidence pointer: “\#\# PASS 2 (Non-passing)” → “CI Failure (terminal output)” → `FAIL — tools/evidence/refresh_step_logs_manifest.py --check`  
* Attempt 0 also introduced a tooling-side change in `tools/evidence/update_evidence_index.py` (lowercasing certain path segments) to address evidence-index/path-proof normalization.  
  Source: Original PR  
  Evidence pointer: “\#\# File Diffs” → `tools/evidence/update_evidence_index.py` diff  
* Attempt 1 (Remediation 1\) initially attempted to make GET probe-only and added/expanded contract tests around GET behavior.  
  Source: Remediation 1  
  Evidence pointer: “\#\# Description” \+ “\#\# Log Summary” → “Code changes made in pass 1” / “tests/http/test\_compat\_endpoint\_contract.py (as shown)”  
* Attempt 1 then reversed direction due to an internal “canon conflict” bug report and restored ids-only GET compat computation when query params are provided. This put it out of alignment with the Implementation Doc.  
  Source: Remediation 1  
  Evidence pointer: “\#\# Actions Taken” → “Restored ids-only GET compat behavior when a\_id/b\_id are provided.”  
* Attempt 1 shows the step logs manifest check being run successfully (closing the CI failure class from Attempt 0).  
  Source: Remediation 1  
  Evidence pointer: “\#\# Actions Taken” → `✅ SAFE_MODE=1 python tools/evidence/refresh_step_logs_manifest.py --check`  
* Attempt 2 (Remediation 2\) is a non-passing review state identifying that the contract split still wasn’t resolved: GET must be probe-only and must not compute compat.  
  Source: Remediation 2  
  Evidence pointer: “Requirement Satisfaction Crosswalk” → “GET probe-only (must not compute compat)”  
* Attempt 2 introduced/expanded tests in `tests/http/test_compat_endpoint_contract.py` to enforce probe-only GET semantics and to assert endpoint catalog properties from `docs/ENDPOINTS_CATALOG.json`.  
  Source: Remediation 2  
  Evidence pointer: “\#\# Diff” → `tests/http/test_compat_endpoint_contract.py` additions (`test_get_probe_only`, catalog assertions)  
* Attempt 2 still failed because the handler behavior described in the lifecycle did not yet match the new test expectations (probe-only GET vs GET computing compat).  
  Source: Remediation 2  
  Evidence pointer: “Requirement Satisfaction Crosswalk” → attempt 2 status for “GET probe-only…”  
* Attempt 3 (Remediation 3\) identified a concrete regression risk: POST accepted empty `a_id`/`b_id` strings and could trigger a downstream UID validation `ValueError` → 500 instead of clean 400 invalid\_json.  
  Source: Remediation 3  
  Evidence pointer: “\#\# Description” (bug statement describing `{"a_id":"alice","b_id":""}` and 500 risk)  
* Attempt 3 fixed this by validating `a_id`/`b_id` against `UID_RE` before resolving them into `person_uid` objects, returning `invalid_json` 400 on invalid/empty IDs.  
  Source: Remediation 3  
  Evidence pointer: “Starting make\_pr tool implementation” → `engine/http/compat_handler.py` lines 99–112 (imports `UID_RE`, rejects non-matching IDs)  
* Attempt 3 also shows GET as probe-only (rejecting bodies, returning a fixed probe payload) and POST as the only compat computation surface, including prod gating.  
  Source: Remediation 3  
  Evidence pointer: “Starting make\_pr tool implementation” → `engine/http/compat_handler.py` lines 82–95  
* Attempt 3 provides local test proof for the required suites used in this PR lifecycle: compat endpoint contract, endpoint catalog test, and errors parity.  
  Source: Remediation 3  
  Evidence pointer: “Running required tests” (pytest invocations and pass lines)

### Review Summary

* Attempt 0 built the initial `/api/compat/v1` surface, updated endpoint catalog artifacts, and added tests, but its GET behavior still computed compat based on query params.  
  Source: Original PR  
  Evidence pointer: “\#\# File Diffs” → `engine/http/compat_handler.py` (`get_ids_only()` calling `compat_public(...)` when query args present)  
* Attempt 0 did not reach merge readiness due to CI failure on the step logs manifest check.  
  Source: Original PR  
  Evidence pointer: “\#\# PASS 2 (Non-passing)” → “CI Failure (terminal output)” (`FAIL — tools/evidence/refresh_step_logs_manifest.py --check`)  
* Attempt 1 addressed the manifest check but (after a “canon conflict” report) restored ids-only GET compat computation, which is inconsistent with the Implementation Doc’s probe-only intent.  
  Source: Remediation 1  
  Evidence pointer: “\#\# Actions Taken” → “Restored ids-only GET compat behavior…”  
* Attempt 2 tightened the contract tests to enforce probe-only GET and added catalog assertions into `tests/http/test_compat_endpoint_contract.py`, but flagged that behavior and tests were still misaligned (non-passing).  
  Source: Remediation 2  
  Evidence pointer: “\#\# Diff” (test additions) \+ “Requirement Satisfaction Crosswalk” (Attempt 2: Not satisfied)  
* Attempt 3 resolves the remaining functional gap by making GET probe-only in the handler and strengthening POST `a_id`/`b_id` validation to prevent 500s on empty IDs.  
  Source: Remediation 3  
  Evidence pointer: `engine/http/compat_handler.py` listing (GET handler \+ UID\_RE validation)  
* Endpoint catalog discipline appears satisfied (POST-only/internal\_admin/a7\_eligible/env\_gate non-empty) via tests and catalog entry evidence.  
  Source: Original PR / Remediation 2 / Remediation 3  
  Evidence pointer: Original PR `artifacts/evidence_index.jsonl` line showing `/api/compat/v1` entry; Remediation 2 diff adds catalog assertions; Remediation 3 shows catalog test passing  
* Evidence posture is materially improved vs attempt 0: the contract tests now explicitly enforce probe-only GET behavior and validate endpoint catalog entry fields.  
  Source: Remediation 2  
  Evidence pointer: “\#\# Diff” → `tests/http/test_compat_endpoint_contract.py`  
* Remaining risk: the PR lifecycle includes a non-trivial change to `tools/evidence/update_evidence_index.py`; while motivated by CI/evidence normalization, it is cross-epic surface area and should be reviewed for unintended side effects.  
  Source: Original PR  
  Evidence pointer: “\#\# File Diffs” → `tools/evidence/update_evidence_index.py`

### RCA (REQUIRED)

#### RCA-001

A) Failure statement (quoted)

* “FAIL — tools/evidence/refresh\_step\_logs\_manifest.py \--check”  
  Source: Original PR  
  Evidence pointer: “\#\# PASS 2 (Non-passing)” → “CI Failure (terminal output)”

B) Where it occurred

* Attempt 0

C) Root cause(s)

1. Evidence-path/proof outputs changed without the corresponding step-logs manifest being refreshed/updated to match the new outputs.  
   Evidence pointer(s): Original PR → “\#\# PASS 2 (Non-passing)” → “CI Failure (terminal output)” (manifest check failure)

D) Fix progression across attempts

* Remediation 1: explicitly ran the manifest checker successfully (closing the CI failure class).  
  Evidence-based why attempt 1 was insufficient overall: it later restored ids-only GET behavior (separate failure cluster).  
  Evidence pointer: Remediation 1 → “\#\# Actions Taken” → `✅ SAFE_MODE=1 python tools/evidence/refresh_step_logs_manifest.py --check`  
* Remediation 2: focused on contract/test alignment for GET/POST rather than manifest gating.  
  Evidence pointer: Remediation 2 → “\#\# Diff” (tests)  
* Remediation 3: no new manifest changes evidenced; tests run indicate stability with the current set of changes.  
  Evidence pointer: Remediation 3 → “Running required tests”

E) Fix verification

* Proof line: `✅ SAFE_MODE=1 python tools/evidence/refresh_step_logs_manifest.py --check`  
  Source: Remediation 1  
  Evidence pointer: “\#\# Actions Taken”  
* Residual risk (evidenced): none explicitly beyond the presence of evidence tooling diffs in Attempt 0\.  
  Source: Original PR  
  Evidence pointer: “\#\# File Diffs” → `tools/evidence/update_evidence_index.py`

---

#### RCA-002

A) Failure statement (quoted)

* “Restored ids-only GET compat behavior when a\_id/b\_id are provided.”  
  Source: Remediation 1  
  Evidence pointer: “\#\# Actions Taken”  
* “GET probe-only (must not compute compat)” → Attempt 2: “Not satisfied”  
  Source: Remediation 2  
  Evidence pointer: “Requirement Satisfaction Crosswalk”

B) Where it occurred

* Attempt 1, Attempt 2

C) Root cause(s)

1. Contract confusion / drift across attempts: probe-only GET intent vs an ids-driven GET compat compute path.  
   Evidence pointer(s):  
   * Remediation 1 → “\#\# Actions Taken” (restoring ids-only GET compat behavior)  
   * Remediation 2 → “Requirement Satisfaction Crosswalk” (explicitly marking GET probe-only requirement unmet)

D) Fix progression across attempts

* Remediation 1: initially moved toward probe-only GET, but reversed to ids-only GET due to an internal “canon conflict” report; insufficient because it remained inconsistent with the Implementation Doc’s health-only GET requirement.  
  Evidence pointer: Remediation 1 → “\#\# Log Summary” (probe-only work) \+ “\#\# Actions Taken” (restore ids-only)  
* Remediation 2: strengthened tests to enforce probe-only GET and added catalog assertions in `tests/http/test_compat_endpoint_contract.py`; insufficient because code behavior was still not aligned at that point.  
  Evidence pointer: Remediation 2 → “\#\# Diff” \+ “Requirement Satisfaction Crosswalk”  
* Remediation 3: updated handler to implement probe-only GET (no compat compute on GET) and keep POST as the compat computation surface.  
  Evidence pointer: Remediation 3 → `engine/http/compat_handler.py` listing (GET handler and POST route)

E) Fix verification

* Proof: `python -m pytest -q tests/http/test_compat_endpoint_contract.py` → `4 passed in 0.82s`  
  Source: Remediation 3  
  Evidence pointer: “Running required tests”  
* Proof: probe-only GET behavior is directly visible in handler listing (GET returns fixed payload and rejects body).  
  Source: Remediation 3  
  Evidence pointer: `engine/http/compat_handler.py` lines 82–89  
* Residual risk: none evidenced (no failing cases cited post-fix).

---

#### RCA-003

A) Failure statement (quoted)

* “When a client sends `{\"a_id\":\"alice\",\"b_id\":\"\"}` … this request now produces a 500 instead of the intended `invalid_json` 400.”  
  Source: Remediation 3  
  Evidence pointer: “\#\# Description”

B) Where it occurred

* Attempt 3 (bug discovered during review of remediation candidate)

C) Root cause(s)

1. POST validation treated `a_id`/`b_id` as “strings” but did not enforce non-empty/valid UID format before passing into downstream UID enforcement.  
   Evidence pointer(s): Remediation 3 → “\#\# Description” (empty IDs accepted → downstream `_uid` raises ValueError)

D) Fix progression across attempts

* Remediation 1: not evidenced as addressing this specific empty-ID edge case.  
  Evidence pointer: N/A (no mention of empty ID validation)  
* Remediation 2: not evidenced as addressing this specific empty-ID edge case.  
  Evidence pointer: N/A (no mention of empty ID validation)  
* Remediation 3: added UID regex validation (via `UID_RE`) for `a_id`/`b_id` prior to resolution.  
  Evidence pointer: Remediation 3 → `engine/http/compat_handler.py` lines 102–110

E) Fix verification

* Proof: handler now returns `invalid_json` for invalid IDs via regex gate (`or not UID_RE.match(a_id) or not UID_RE.match(b_id)`).  
  Source: Remediation 3  
  Evidence pointer: `engine/http/compat_handler.py` lines 102–110  
* Tests run still pass post-change: `4 passed`, `1 passed`, `7 passed`.  
  Source: Remediation 3  
  Evidence pointer: “Running required tests”  
* Residual risk: no explicit new test for the empty-ID case is shown in artifacts (risk is mitigated by the code change, but the specific case is not evidenced as a test assertion).

### Findings (includes diff review)

1. **Diff-focused:** Attempt 0 introduced a GET code path that computed compat when `a_id`/`b_id` query params exist (`compat_public(...)`), which is incompatible with “health-only probing” intent in the Implementation Doc.  
   * Source: Original PR / Implementation Doc  
   * Why it matters: GET becomes an unintended compat surface (contract ambiguity \+ potential exposure).  
   * Evidence pointer(s):  
     * Original PR → “\#\# File Diffs” → `engine/http/compat_handler.py` (`get_ids_only()` branch that calls `compat_public(...)`)  
     * Implementation Doc → PR-01 → “GET /api/compat/v1 is HEALTH-only (probing) … carries no request body.”  
2. **Diff-focused:** Attempt 0 added endpoint catalog validation as a standalone test file (`tests/http/test_endpoint_catalog.py`) asserting POST-only/internal\_admin/a7\_eligible/env\_gate.  
   * Source: Original PR  
   * Why it matters: creates enforceable guardrails for catalog discipline beyond manual review.  
   * Evidence pointer: Original PR → “\#\# File Diffs” → `tests/http/test_endpoint_catalog.py`  
3. **Diff-focused:** Attempt 0 updated governed endpoint catalog artifacts (including an evidence-index record that shows `/api/compat/v1` as `method:"POST"` with `classification:"internal_admin"` and `env_gate:"APP_ENV!=prod"`).  
   * Source: Original PR  
   * Why it matters: aligns catalog metadata with internal/admin contract requirements.  
   * Evidence pointer: Original PR → `artifacts/evidence_index.jsonl` entry line containing `/api/compat/v1` (shown in file excerpt around the JSON line with `/api/compat/v1`).  
4. **Diff-focused (scope expansion callout):** Attempt 0 modified `tools/evidence/update_evidence_index.py` to normalize certain path segments to lowercase for `audit/qa/hde-epic024/checks/…`.  
   * Source: Original PR  
   * Why it matters: cross-epic tooling change can have broad impact; needs deliberate review even if CI-motivated.  
   * Evidence pointer: Original PR → “\#\# File Diffs” → `tools/evidence/update_evidence_index.py`  
5. **Diff-focused:** Attempt 1 reintroduced “ids-only GET compat computation” after initially pushing toward probe-only GET, resulting in a contract split regression vs the Implementation Doc intent.  
   * Source: Remediation 1  
   * Why it matters: flips GET from probe-only to functional compat surface; undermines endpoint contract clarity.  
   * Evidence pointer: Remediation 1 → “\#\# Actions Taken” → “Restored ids-only GET compat behavior…”  
6. **Diff-focused:** Attempt 2 updated `tests/http/test_compat_endpoint_contract.py` to (a) enforce probe-only GET and (b) assert catalog entry fields from `docs/ENDPOINTS_CATALOG.json`.  
   * Source: Remediation 2  
   * Why it matters: moves acceptance into executable tests (prevents future regressions).  
   * Evidence pointer: Remediation 2 → “\#\# Diff” → `tests/http/test_compat_endpoint_contract.py` (adds `test_get_probe_only` \+ catalog assertions)  
7. **Diff-focused:** Attempt 2 refactored `tests/cli/test_errors_parity.py` assertions/helpers, consistent with moving “invalid\_json” parity away from relying on GET semantics.  
   * Source: Remediation 2  
   * Why it matters: reduces coupling between parity checks and GET behavior, enabling probe-only GET without breaking parity tests.  
   * Evidence pointer: Remediation 2 → “\#\# Diff” → `tests/cli/test_errors_parity.py`  
8. **Diff-focused:** Attempt 3’s handler now implements probe-only GET directly: it rejects any GET body with `invalid_json` and returns a fixed probe payload without computing compat.  
   * Source: Remediation 3  
   * Why it matters: resolves the primary contract ambiguity and matches probe-only semantics enforced by tests.  
   * Evidence pointer: Remediation 3 → `engine/http/compat_handler.py` listing lines 82–89  
9. **Diff-focused:** Attempt 3 added prod gating on POST (`APP_ENV == "prod"` → 404 with `ERR_NOT_FOUND`).  
   * Source: Remediation 3  
   * Why it matters: ensures internal/admin compat surface is not exposed in prod environments per intended “internal/admin” discipline.  
   * Evidence pointer: Remediation 3 → `engine/http/compat_handler.py` lines 90–95  
10. **Diff-focused:** Attempt 3 fixed the empty-ID regression by validating `a_id`/`b_id` against `UID_RE` before resolving into `person_uid`, preventing downstream `ValueError` 500s.  
* Source: Remediation 3  
* Why it matters: prevents server error regressions and enforces clean 400 invalid\_json handling for bad input.  
* Evidence pointer: Remediation 3 → `engine/http/compat_handler.py` lines 102–110  
11. Contract/test alignment is now evidenced as passing: the required contract test suite (`tests/http/test_compat_endpoint_contract.py`) and the catalog test suite pass in Attempt 3\.  
* Source: Remediation 3  
* Why it matters: provides execution proof that the handler matches the expected contract and catalog metadata constraints.  
* Evidence pointer: Remediation 3 → “Running required tests” (pass lines for both tests)  
12. Evidence/verification posture across attempts is now coherent: earlier CI gating failures (manifest check) were addressed, and the endpoint contract ambiguity that drove multiple remediations is resolved by handler \+ tests aligning.  
* Source: Original PR / Remediation 1 / Remediation 2 / Remediation 3  
* Why it matters: reduces merge risk (regressions and contract drift).  
* Evidence pointer(s):  
  * Original PR → “CI Failure … refresh\_step\_logs\_manifest.py \--check”  
  * Remediation 1 → “✅ … refresh\_step\_logs\_manifest.py \--check”  
  * Remediation 2 → test diffs enforcing probe-only GET  
  * Remediation 3 → handler listing \+ passing tests

### Requirement Satisfaction Crosswalk (Attempt 0 → Attempt 1 → Attempt 2 → Attempt 3\)

**Requirement: GET is health-only probing (no compat compute) and carries no request body**

* Attempt 0 status: **Not satisfied**  
  * Evidence pointer(s): Original PR → “\#\# File Diffs” → `engine/http/compat_handler.py` (`get_ids_only()` computes compat when query args exist)  
* Attempt 1 status: **Not satisfied**  
  * Evidence pointer(s): Remediation 1 → “\#\# Actions Taken” → “Restored ids-only GET compat behavior…”  
* Attempt 2 status: **Not satisfied**  
  * Evidence pointer(s): Remediation 2 → “Requirement Satisfaction Crosswalk” → “GET probe-only (must not compute compat)” (Attempt 2 marked Not satisfied)  
* Attempt 3 status: **Satisfied**  
  * Evidence pointer(s): Remediation 3 → `engine/http/compat_handler.py` lines 82–89 (probe-only GET; rejects body; no compat call)

**Requirement: POST is the compat computation surface and rejects invalid input cleanly**

* Attempt 0 status: **Partially satisfied / Not satisfied overall** (behavior existed, but overall attempt failed CI and contract split ambiguous)  
  * Evidence pointer(s): Original PR → `engine/http/compat_handler.py` diff (POST route exists) \+ “\#\# PASS 2 (Non-passing)” CI failure  
* Attempt 1 status: **Not satisfied overall** (attempt non-passing due to GET regression)  
  * Evidence pointer(s): Remediation 1 → “\#\# Actions Taken” (GET restored to compute compat)  
* Attempt 2 status: **Not satisfied** (tests tightened; behavior mismatch remained per attempt)  
  * Evidence pointer(s): Remediation 2 → “Requirement Satisfaction Crosswalk” (Attempt 2 still non-passing)  
* Attempt 3 status: **Satisfied**  
  * Evidence pointer(s): Remediation 3 → `engine/http/compat_handler.py` lines 90–126 (POST-only compat compute, invalid\_json paths, UID\_RE validation)  
  * Evidence pointer(s): Remediation 3 → pytest pass for contract suite (“4 passed…”)

**Requirement: Endpoint catalog entry exists for `/api/compat/v1`, is POST-only/internal\_admin, and has a non-empty env gate field**

* Attempt 0 status: **Satisfied** (artifact evidence shows correct metadata)  
  * Evidence pointer(s): Original PR → `artifacts/evidence_index.jsonl` line showing `/api/compat/v1` with `method:"POST"`, `classification:"internal_admin"`, `env_gate:"APP_ENV!=prod"`  
* Attempt 1 status: **Satisfied** (not evidenced as removed/changed)  
  * Evidence pointer(s): Remediation 1 → (no contrary evidence; attempt focuses on handler \+ tests; catalog enforcement exists via tests described)  
* Attempt 2 status: **Satisfied (tests added) but overall attempt non-passing**  
  * Evidence pointer(s): Remediation 2 → “\#\# Diff” → `tests/http/test_compat_endpoint_contract.py` catalog assertions  
* Attempt 3 status: **Satisfied**  
  * Evidence pointer(s): Remediation 3 → “Running required tests” → `tests/http/test_endpoint_catalog.py` “1 passed…” and contract tests pass

**Requirement: Update governed artifacts and path proofs for endpoint catalog \+ evidence index**

* Attempt 0 status: **Satisfied**  
  * Evidence pointer(s): Original PR → “\#\# File Changes” table includes `docs/ENDPOINTS_CATALOG.json`, `docs/ENDPOINTS_CATALOG.json.sha256`, `docs/evidence/INDEX.json`, `docs/evidence/INDEX.sha256`, `artifacts/evidence_index.jsonl`, and multiple `.path_proof.txt` files  
* Attempt 1 status: **Satisfied (no evidence of reversion)**  
  * Evidence pointer(s): Remediation 1 → “\#\# Description”/“Log Summary” references governed artifacts and evidence index updates being part of the work  
* Attempt 2 status: **Satisfied (claimed presence)**  
  * Evidence pointer(s): Remediation 2 → lines stating “Confirmed governed artifact files are present…”  
* Attempt 3 status: **Satisfied (no contrary evidence; tests relying on catalog file pass)**  
  * Evidence pointer(s): Remediation 3 → “Running required tests” includes catalog test passing

**Requirement: Required test suite passes (`tests/http/test_compat_endpoint_contract.py`)**

* Attempt 0 status: **Not satisfied overall** (PASS 2 CI failure prevents merge readiness)  
  * Evidence pointer(s): Original PR → “\#\# PASS 2 (Non-passing)” CI failure section  
* Attempt 1 status: **Not satisfied** (attempt declared non-passing)  
  * Evidence pointer(s): Remediation 1 → “\#\# Bug Reported” \+ “\#\# Actions Taken” (non-passing due to contract drift)  
* Attempt 2 status: **Not satisfied** (attempt marked non-passing)  
  * Evidence pointer(s): Remediation 2 → “Requirement Satisfaction Crosswalk” (Attempt 2 non-passing)  
* Attempt 3 status: **Satisfied**  
  * Evidence pointer(s): Remediation 3 → `python -m pytest -q tests/http/test_compat_endpoint_contract.py` → `4 passed in 0.82s`

### Doc Deltas (PF-Canon only; ALWAYS INCLUDED)

Doc: PF23 — Canon Reality Audits v1.0  
Section: “Adapter / HTTP surfaces” → “Compat HTTP surface (`engine/http/compat_handler.py`)”  
Delta: Update the documented compat HTTP contract so GET is probe-only (no compat compute) and POST is the only compat computation surface; reflect current validation and prod gating behavior (NEW CANON PROPOSAL).  
Why: PF23 currently documents GET as accepting `a_id`/`b_id` and returning compat payload; the merged PR lifecycle enforces probe-only GET and moves compat compute to POST only.  
Evidence pointer:

* PF23 excerpt (canon proof excerpt, verbatim, 1–5 lines):  
  * “\#\# **Compat HTTP surface (`engine/http/compat_handler.py`)**”  
  * “GET /api/compat/v1 accepts a\_id, b\_id as query params and returns the response payload (application/json).”  
  * “POST /api/compat/v1 accepts a/b payload JSON and returns computed compat payload (application/json).”  
    (Source: PF23 — Canon Reality Audits v1.0, section shown around the “Compat HTTP surface” heading)  
* PR behavior evidence: Remediation 3 → `engine/http/compat_handler.py` lines 82–89 (probe-only GET) and lines 90–126 (POST-only compat compute)

### Evidence Print (PASS PROOF; whole PR lifecycle)

#### A) Acceptance coverage evidence (Implementation Doc)

**Requirement: GET is health-only probing and carries no request body**

* Evidence pointer(s): Remediation 3 → `engine/http/compat_handler.py` lines 82–89  
* Key proof facts (verbatim from Remediation 3 artifacts):  
  * `if request.data: # reject GET with body`  
  * `return _writer_payload(env, status=400)`  
  * `body = {"ok": True, "schema": "v1"}`

**Requirement: POST is compat compute surface; reject invalid input; prod gate**

* Evidence pointer(s): Remediation 3 → `engine/http/compat_handler.py` lines 90–126  
* Key proof facts (verbatim):  
  * `if (os.environ.get("APP_ENV") or "").lower() == "prod":`  
  * `env = error_envelope("ERR_NOT_FOUND")`  
  * `if (a and a_id) or (b and b_id) or ((a_id or b_id) and (a or b)):` → `error_envelope("invalid_json")`

**Requirement: Endpoint catalog discipline (POST-only/internal\_admin/env gate non-empty) is enforced by tests**

* Evidence pointer(s): Remediation 3 → “Running required tests” (catalog \+ contract tests)  
* Key proof facts (verbatim pass lines):  
  * `1 passed in 0.08s` (endpoint catalog test)  
  * `4 passed in 0.82s` (compat endpoint contract test)

#### B) Closure of gaps across attempts (Attempt 0 \+ Attempt 1 \+ Attempt 2\)

**Gap: CI failed on step logs manifest check**

* Attempt 0 evidence pointer (failure): Original PR → “CI Failure (terminal output)” → `FAIL — tools/evidence/refresh_step_logs_manifest.py --check`  
* Remediation 3 evidence pointer proving closure: Remediation 1 → “\#\# Actions Taken” → `✅ SAFE_MODE=1 python tools/evidence/refresh_step_logs_manifest.py --check` (subsequent attempts report passing tests; no recurrence evidenced)  
* Key proof fact (verbatim): `✅ SAFE_MODE=1 python tools/evidence/refresh_step_logs_manifest.py --check`

**Gap: GET contract ambiguity (GET computing compat vs probe-only)**

* Attempt 0 evidence pointer: Original PR → `engine/http/compat_handler.py` diff (`get_ids_only()` calls `compat_public(...)` when query args exist)  
* Attempt 1 evidence pointer: Remediation 1 → “Restored ids-only GET compat behavior…”  
* Attempt 2 evidence pointer: Remediation 2 → crosswalk marks “GET probe-only … Not satisfied”  
* Remediation 3 evidence pointer proving closure: Remediation 3 → `engine/http/compat_handler.py` lines 82–89  
* Key proof fact (verbatim): `def get_ids_only():` … `body = {"ok": True, "schema": "v1"}` (no compat call)

**Gap: Empty `a_id`/`b_id` causing 500**

* Attempt 2 evidence pointer (risk stated): Remediation 3 → “\#\# Description” (500 risk described)  
* Remediation 3 evidence pointer proving closure: Remediation 3 → `engine/http/compat_handler.py` lines 102–110  
* Key proof fact (verbatim): `or not UID_RE.match(a_id) or not UID_RE.match(b_id)`

#### C) Token and gate evidence (names-only; do not invent)

**ENDPOINTS\_CATALOG\_OK**

* Status: **Proven**  
* Evidence pointer(s): Remediation 3 → `python -m pytest -q tests/http/test_endpoint_catalog.py` → `1 passed in 0.08s`

**ENDPOINTS\_CATALOG\_INTERNAL\_OK**

* Status: **Proven**  
* Evidence pointer(s):  
  * Original PR → `/api/compat/v1` evidence-index record showing `classification":"internal_admin"`  
  * Remediation 3 → endpoint catalog test pass line (`1 passed in 0.08s`)

**ENDPOINTS\_CATALOG\_ENV\_GATE\_OK**

* Status: **Proven**  
* Evidence pointer(s):  
  * Original PR → `/api/compat/v1` evidence-index record showing `env_gate":"APP_ENV!=prod"`  
  * Remediation 3 → endpoint catalog test pass line (`1 passed in 0.08s`)

#### D) Test/CI proof

* `python -m pytest -q tests/http/test_compat_endpoint_contract.py`  
  * Pass indicator (verbatim): `4 passed in 0.82s`  
  * Evidence pointer: Remediation 3 → “Running required tests”  
* `python -m pytest -q tests/http/test_endpoint_catalog.py`  
  * Pass indicator (verbatim): `1 passed in 0.08s`  
  * Evidence pointer: Remediation 3 → “Running required tests”  
* `python -m pytest -q tests/cli/test_errors_parity.py`  
  * Pass indicator (verbatim): `7 passed in 3.26s`  
  * Evidence pointer: Remediation 3 → “Running required tests”

#### E) Artifact/evidence outputs

* `docs/ENDPOINTS_CATALOG.json.sha256`  
  * Type: sha256 text  
  * Key proof facts (verbatim from Original PR “Evidence artifacts displayed”):  
    * `7834c27f43c5a1bab7f1527f14eec447b0e402f98f82d630875e384e6bb2eb4e docs/ENDPOINTS_CATALOG.json`  
  * Evidence pointer: Original PR → “Evidence artifacts displayed” (shows `docs/ENDPOINTS_CATALOG.json.path_proof.txt` and sha output)  
* `docs/ENDPOINTS_CATALOG.json.path_proof.txt`  
  * Type: json/text proof  
  * Key proof facts: (existence \+ referenced in Original PR evidence display)  
  * Evidence pointer: Original PR → “Evidence artifacts displayed” (lists the file explicitly)  
* `docs/evidence/INDEX.json.path_proof.txt` and `artifacts/evidence_index.jsonl.path_proof.txt`  
  * Type: json proof  
  * Key proof facts (verbatim JSON lines from Original PR):  
    * `{"path":"docs/evidence/INDEX.json","exists":true,"size":...,"sha256":"49d91e59b94171902a0d7f885915ea37e6e71454239115e78a62c7c3c1656b2d"}`  
    * `{"path":"artifacts/evidence_index.jsonl","exists":true,"size":...,"sha256":"af1738c38ac1137dc1f59967c3bc8181b9bc7ce256ce6b0ac569a93d1e3964ea"}`  
  * Evidence pointer: Original PR → JSON path proof lines shown in the evidence-index excerpt (around the “docs/evidence/INDEX.json” and “artifacts/evidence\_index.jsonl” proof lines)

## 2.12 PR02 HDE-EPIC025

### Review Summary

* PR focuses on making `showcompat` CLI output deterministically canonical by coupling stdout emission to the canonical serializer path and enforcing newline/CRLF constraints.  
* Scope appears aligned with PR-02 requirements in the Approved Plan (deterministic serializer coupling \+ CLI showcompat conformance) via CLI code changes, CLI canonical-bytes tests, and refreshed showcompat/evidence artifacts.  
* Evidence posture includes regenerated showcompat args/evidence index artifacts and multiple CLI conformance/identity/parity tests reported passing.  
* Diff review did not show unrelated system/config/auth scope drift (only CLI \+ artifacts \+ one CLI test changed).  
* Main notable risk is a diff-hunk ambiguity around stdout emission lines in `engine/cli/main.py` (see DR-012); however the canonical-bytes test should detect double-write if it existed.

### Diff Review (REQUIRED; primary technical review)

DR-001

* Change summary: Route `showcompat` stdout emission through a dedicated stdout-bytes enforcement helper (LF required; CRLF forbidden).  
* Risk assessment: Low  
* Why it matters: Ensures CLI output complies with deterministic/canonical stdout requirements and prevents format drift.  
* Evidence pointer: PR Artifacts — Diff — `engine/cli/main.py` (function `_emit_stdout_bytes`)  
* Approved Plan linkage: Approved Plan — PR-02 — Implementation requirements (CLI stdout conformance)

DR-002

* Change summary: Add explicit error signaling on invalid stdout byte formatting via CLI error codes (`STDOUT_MISSING_LF`, `STDOUT_CRLF`).  
* Risk assessment: Low  
* Why it matters: Converts “silent formatting drift” into explicit failures, making violations test-detectable and user-visible.  
* Evidence pointer: PR Artifacts — Diff — `engine/cli/main.py` (`raise CliError("STDOUT_MISSING_LF")`, `raise CliError("STDOUT_CRLF")`)  
* Approved Plan linkage: Approved Plan — PR-02 — Deterministic serializer coupling and CLI showcompat conformance

DR-003

* Change summary: Add/enable optional “reader bytes dump” path for `showcompat` by persisting `reader_bytes` when `dump_reader` is provided.  
* Risk assessment: Low  
* Why it matters: Supports deterministic coupling checks between CLI and Reader surfaces without ad-hoc serializers.  
* Evidence pointer: PR Artifacts — Diff — `engine/cli/main.py` (`emit_reader_public_envelope(...)`, `_dump_reader_bytes(_.dump_reader, reader_bytes)`)  
* Approved Plan linkage: Approved Plan — PR-02 — Acceptance tokens (Reader/CLI parity/identity posture)

DR-004

* Change summary: Extend admin dump emission for showcompat by writing canonical JSON dumps via `canon_dump(...)` into an admin dump directory.  
* Risk assessment: Low  
* Why it matters: Keeps diagnostic/admin artifacts canonical and deterministic, avoiding serializer forks.  
* Evidence pointer: PR Artifacts — Diff — `engine/cli/main.py` (`canon_dump(admin_dir / f"...", ...)`)  
* Approved Plan linkage: Approved Plan — PR-02 — Evidence outputs (governed artifact discipline)

DR-005

* Change summary: Introduce case naming logic based on input (`--a7`) and file stem (`_case_name`).  
* Risk assessment: Low  
* Why it matters: Stabilizes artifact naming for deterministic outputs across runs and inputs.  
* Evidence pointer: PR Artifacts — Diff — `engine/cli/main.py` (`def _case_name(...)`)  
* Approved Plan linkage: Approved Plan — PR-02 — Evidence outputs (stable artifact generation)

DR-006

* Change summary: Strengthen CLI stdout canonical-bytes test to assert `showcompat` output equals `emit_public(payload)` bytes exactly.  
* Risk assessment: Low  
* Why it matters: Ensures single canonical serializer path and prevents “almost JSON” drift (spacing/order/newline differences).  
* Evidence pointer: PR Artifacts — Diff — `tests/cli/test_cli_canonical_bytes.py` (`assert raw == expected`)  
* Approved Plan linkage: Approved Plan — PR-02 — Acceptance tokens \+ Basic QA task

DR-007

* Change summary: Add explicit checks against CRLF and double-blank-line patterns.  
* Risk assessment: Low  
* Why it matters: Directly enforces formatting constraints that otherwise slip through semantic JSON comparisons.  
* Evidence pointer: PR Artifacts — Diff — `tests/cli/test_cli_canonical_bytes.py` (`assert b"\r\n" not in raw`, `assert b"\n\n" not in raw`)  
* Approved Plan linkage: Approved Plan — PR-02 — CLI showcompat conformance

DR-008

* Change summary: Refresh showcompat args artifact content (`argv` interpreter path change; updated hashes).  
* Risk assessment: Low  
* Why it matters: Keeps governed evidence artifacts consistent with the actual invocation used to produce stdout artifacts.  
* Evidence pointer: PR Artifacts — Diff — `artifacts/cli/showcompat/args.json`  
* Approved Plan linkage: Approved Plan — PR-02 — Evidence outputs (`artifacts/cli/showcompat/args.json`)

DR-009

* Change summary: Refresh showcompat args path-proof metadata (size/sha/timestamp update).  
* Risk assessment: Low  
* Why it matters: Preserves reproducibility/provenance for governed artifacts.  
* Evidence pointer: PR Artifacts — Diff — `artifacts/cli/showcompat/args.json.path_proof.txt`  
* Approved Plan linkage: Approved Plan — PR-02 — Evidence outputs (path proof expectations)

DR-010

* Change summary: Update evidence index jsonl with refreshed records (including showcompat stdout/sha/args and registry mirrors).  
* Risk assessment: Low  
* Why it matters: Ensures evidence registry stays consistent with produced artifacts and their hashes.  
* Evidence pointer: PR Artifacts — Diff — `artifacts/evidence_index.jsonl`  
* Approved Plan linkage: Approved Plan — PR-02 — Evidence and governed updates (`tools/evidence/update_evidence_index.py` posture)

DR-011

* Change summary: Update evidence index path-proof metadata accordingly.  
* Risk assessment: Low  
* Why it matters: Evidence index is itself governed; path-proof changes preserve traceability of the registry file.  
* Evidence pointer: PR Artifacts — Diff — `artifacts/evidence_index.jsonl.path_proof.txt`  
* Approved Plan linkage: Approved Plan — PR-02 — Evidence and governed updates

DR-012

* Change summary: `showcompat` stdout emission lines appear adjacent in the diff hunk (`sys.stdout.buffer.write(compat_bytes)` and `_emit_stdout_bytes(compat_bytes)`), but without \+/- markers this is ambiguous (could be a replace, or could be an accidental double-write).  
* Risk assessment: Medium  
* Why it matters: A true double-write would concatenate two JSON payloads and break the CLI stdout contract; it *should* be caught by the canonical-bytes test, but ambiguity in the diff text reduces reviewer certainty.  
* Evidence pointer: PR Artifacts — Diff — `engine/cli/main.py` (hunk `@@ -702,51 +710,51 @@` lines showing both stdout write calls)  
* Approved Plan linkage: Approved Plan — PR-02 — Implementation requirements (canonical stdout posture)

### Findings

1. Observed: `engine/cli/main.py` introduces `_emit_stdout_bytes` that enforces LF termination and rejects CRLF via `CliError` codes.  
* Why it matters: Directly implements the CLI formatting constraints required for deterministic conformance.  
* Evidence pointer: PR Artifacts — Diff — `engine/cli/main.py` (`def _emit_stdout_bytes(...)`, `STDOUT_MISSING_LF`, `STDOUT_CRLF`)  
2. Observed: `showcompat` now has explicit wiring to emit Reader envelope bytes via `emit_reader_public_envelope(...)`, with optional persistence to a path via `_dump_reader_bytes`.  
* Why it matters: Strengthens deterministic serializer coupling between Reader and CLI surfaces.  
* Evidence pointer: PR Artifacts — Diff — `engine/cli/main.py` (`emit_reader_public_envelope(...)`, `_dump_reader_bytes(_.dump_reader, reader_bytes)`)  
3. Observed: Admin dump artifacts are written via `canon_dump(...)` in `_emit_admin_dumps`.  
* Why it matters: Prevents a parallel/“almost canonical” serializer path from emerging in admin artifacts.  
* Evidence pointer: PR Artifacts — Diff — `engine/cli/main.py` (`canon_dump(admin_dir / f"...", ...)`)  
4. Observed: Case naming for artifact emission is normalized via `_case_name` using `--a7` naming rules and file stem logic.  
* Why it matters: Stabilizes artifact naming so repeated runs produce predictable outputs.  
* Evidence pointer: PR Artifacts — Diff — `engine/cli/main.py` (`def _case_name(...)`)  
5. Observed: `tests/cli/test_cli_canonical_bytes.py` asserts `raw == expected` where `expected = emit_public(payload)` and `payload` is parsed from stdout.  
* Why it matters: This is a strict coupling test (bytes-level), not just semantic JSON equivalence.  
* Evidence pointer: PR Artifacts — Diff — `tests/cli/test_cli_canonical_bytes.py` (`expected = emit_public(payload)`, `assert raw == expected`)  
6. Observed: The same test suite adds explicit CRLF and double-blank-line suppression checks (`b"\r\n"` and `b"\n\n"`).  
* Why it matters: Enforces the formatting constraints that can slip past JSON parsing.  
* Evidence pointer: PR Artifacts — Diff — `tests/cli/test_cli_canonical_bytes.py` (`assert b"\r\n" not in raw`, `assert b"\n\n" not in raw`)  
7. Observed: `artifacts/cli/showcompat/args.json` refresh includes an updated interpreter path in `argv[0]` and still includes `--emit`, `--fmt`, and hashing fields.  
* Why it matters: Keeps the governed args artifact consistent with the actual generation environment/invocation.  
* Evidence pointer: PR Artifacts — Diff — `artifacts/cli/showcompat/args.json` (the `argv` list and hash fields)  
8. Observed: The args path-proof file updates its recorded `size_bytes`, `sha256`, and `produced_at_utc`.  
* Why it matters: Maintains traceability and non-repudiation of governed artifacts.  
* Evidence pointer: PR Artifacts — Diff — `artifacts/cli/showcompat/args.json.path_proof.txt`  
9. Observed: Evidence index jsonl includes explicit records for showcompat stdout and its `.sha256`, with stable `sha256` and `size_bytes`.  
* Why it matters: Provides governed evidence inventory for the showcompat stdout conformance artifacts expected by PR-02.  
* Evidence pointer: PR Artifacts — Diff — `artifacts/evidence_index.jsonl` (records containing `artifact_key":"cli.showcompat.stdout"` and `artifact_key":"cli.showcompat.stdout_sha256"`)  
10. Observed: Evidence index jsonl also records `serializer_grep_guard.log` and its path proof with `sha256` and `size_bytes`.  
* Why it matters: Captures the serializer anti-regression guard evidence as a governed artifact.  
* Evidence pointer: PR Artifacts — Diff — `artifacts/evidence_index.jsonl` (records for `cli.guards.serializer_grep_guard` and `cli.guards.serializer_grep_guard.path_proof`)  
11. Observed: The `engine/cli/main.py` diff hunk shows adjacent stdout emission calls (`sys.stdout.buffer.write(compat_bytes)` and `_emit_stdout_bytes(compat_bytes)`) but the PR artifact’s python diff is missing \+/- markers, making it ambiguous whether this is a replacement or an additive second write.  
* Why it matters: A true double-write would break stdout JSON validity; the strict byte-equality test should fail in that case, but ambiguity reduces reviewer confidence.  
* Evidence pointer: PR Artifacts — Diff — `engine/cli/main.py` (hunk `@@ -702,51 +710,51 @@`)  
12. Observed: Test evidence includes multiple CLI parity/identity suites and the canonical-bytes suite reported as passing.  
* Why it matters: Supports acceptance posture for deterministic coupling and conformance as required by PR-02.  
* Evidence pointer: PR Artifacts — “Tests / checks executed” section (pass lines)  
13. Observed: PR Artifacts contains inconsistent reporting for `tests/cli/test_cli_canonical_bytes.py` pass count (“2 passed…” in “Tests / checks executed” vs “3 passed…” in “Log Summary”).  
* Why it matters: This is documentation/evidence hygiene risk (not necessarily a code risk), but it’s worth tightening to avoid future audit confusion.  
* Evidence pointer: PR Artifacts — “Tests / checks executed” vs PR Artifacts — “Log Summary”

### Evidence Print (PASS PROOF; required)

A) Tokens satisfied (names-only; do not invent)

* None explicitly claimed as **satisfied** by name in PR Artifacts or Approved Plan.

B) Evidence artifacts produced/updated

* Path: `artifacts/cli/showcompat/args.json`  
  * Type: json  
  * Key proof facts (from PR Artifacts):  
    * `"argv": ["/root/.pyenv/versions/3.10.19/bin/python", "tools/cli/generate_showcompat_artifacts.py", ...]` (interpreter path change present)  
    * `"stdout_sha256": "affb9ce0c49270b6d41af9f251918d99d69bd8a29c456516ac8bddfc67b07c43"`  
    * `"trailing_lf": true`  
  * Evidence pointer: PR Artifacts — Diff — `artifacts/cli/showcompat/args.json`  
* Path: `artifacts/cli/showcompat/args.json.path_proof.txt`  
  * Type: text  
  * Key proof facts (from PR Artifacts):  
    * `"path":"artifacts/cli/showcompat/args.json.path_proof.txt"`  
    * `"sha256":"fc4a57e5a8af649c06cadc0a8bc9ae9e03fe2dde5b85e870d0be3376e34af256"`  
    * `"produced_at_utc":"2025-09-02T14:14:04Z"`  
  * Evidence pointer: PR Artifacts — Diff — `artifacts/cli/showcompat/args.json.path_proof.txt`  
* Path: `artifacts/evidence_index.jsonl`  
  * Type: jsonl  
  * Key proof facts (from PR Artifacts):  
    * `{"artifact_key":"cli.showcompat.stdout", ... "sha256":"affb9ce0c49270b6d41af9f251918d99d69bd8a29c456516ac8bddfc67b07c43","size_bytes":3950, ...}`  
    * `{"artifact_key":"cli.showcompat.stdout_sha256", ... "sha256":"29af1914c3112a83bdb6a5cbb9f39b54ccf9d2f3b3db61a5d7f2f1e0ecf93418","size_bytes":75, ...}`  
    * `{"artifact_key":"cli.guards.serializer_grep_guard", ... "sha256":"3d5902f952106dd7f78f43fdbc376f45b4c37ddf4e815ac7ca7600a554c8a290","size_bytes":2467, ...}`  
  * Evidence pointer: PR Artifacts — Diff — `artifacts/evidence_index.jsonl`  
* Path: `artifacts/evidence_index.jsonl.path_proof.txt`  
  * Type: text  
  * Key proof facts (from PR Artifacts):  
    * `"path":"artifacts/evidence_index.jsonl"`  
    * `"sha256":"e168dbf64406f6bc042dfc61a599c8dc61796592fa7d8074968976d27f611fa7"`  
    * `"produced_at_utc":"2025-09-02T14:14:04Z"`  
  * Evidence pointer: PR Artifacts — Diff — `artifacts/evidence_index.jsonl.path_proof.txt`

C) Test/CI proof

* Job/test name: `python tools/cli/serializer_grep_guard.py`  
  * Pass indicator: `OK`  
  * Where it appears in PR Artifacts: “Tests / checks executed”  
* Job/test name: `python tools/cli/generate_showcompat_artifacts.py`  
  * Pass indicator: `OK`  
  * Where it appears in PR Artifacts: “Tests / checks executed”  
* Job/test name: `python -m pytest -q tests/cli/test_showcompat_parity_and_identity.py`  
  * Pass indicator: `4 passed in 0.74s`  
  * Where it appears in PR Artifacts: “Tests / checks executed”  
* Job/test name: `python -m pytest -q tests/cli/test_errors_parity.py`  
  * Pass indicator: `7 passed in 0.13s`  
  * Where it appears in PR Artifacts: “Tests / checks executed”  
* Job/test name: `python -m pytest -q tests/cli/test_cli_canonical_bytes.py`  
  * Pass indicator: `2 passed in 0.26s`  
  * Where it appears in PR Artifacts: “Tests / checks executed”  
* Job/test name: `python -m pytest -q tests/http/test_compat_endpoint_contract.py`  
  * Pass indicator: `4 passed in 0.20s`  
  * Where it appears in PR Artifacts: “Tests / checks executed”  
* Job/test name: `python -m pytest -q tests/http/test_endpoint_catalog.py`  
  * Pass indicator: `1 passed in 0.08s`  
  * Where it appears in PR Artifacts: “Tests / checks executed”

## 2.13 PR03 HDE-EPIC025

### Review Summary

* PR Artifacts implement Reader `/reader` A7 transport invariants (explicit Content-Length for GET/HEAD; omit Content-Type/Content-Length on 304; stable strong quoted ETag).  
* The work aligns with the Approved Plan’s PR-03 intent: enforce A7 invariants on the existing Reader success route and produce mechanically generated proof artifacts gated behind an explicit flag.  
* PR Artifacts add a focused transport test `tests/http/test_reader_a7_transport.py` and register the `epic025` pytest mark to avoid mark warnings in strict CI postures.  
* Endpoint Catalog is updated to include `/reader` as a dev-harness/internal entry with an env gate (`APP_ENV=dev`) and A7 eligibility metadata, matching the Approved Plan requirement to bind the chosen route into the catalog schema correctly.  
* Evidence posture is strong: PR Artifacts include the required proof artifacts under `artifacts/proofs/` (GET/HEAD/304 headers, writer error posture, encoding invariance, env-gate refusal) and show evidence-index refresh activity consistent with the plan’s “generated, not hand-edited” posture.  
* Tests/verification evidence is present in PR Artifacts (focused pytest pass; evidence check commands marked as passing; checksum path corrected and verified).  
* RCA section is included: PR Artifacts explicitly document an earlier CI failure and bug (ORIENTATION\_DRIFT; endpoint catalog checksum path regression; pytest mark warning) and the subsequent corrective changes and pass proofs.

### Diff Review (REQUIRED; primary technical review)

DR-001

* Change summary: Adjust 304 response handling to omit Content-Type/Content-Length and disable automatic Content-Length emission.  
* Risk assessment: **Medium** (affects HTTP semantics that caches/clients rely on)  
* Why it matters: A7 invariants require “empty-body” 304 responses without content headers to prevent cache poisoning and invariant drift.  
* Evidence pointer: `diff --git a/adapter/http_reader.py b/adapter/http_reader.py` (304 header helper changes).  
* Approved Plan linkage: PR-03 “Enforce the A7 transport invariants … omit Content-Type/Content-Length on 304 responses”.

DR-002

* Change summary: Set explicit Content-Length for 200 and HEAD responses (and ensure HEAD reflects GET length).  
* Risk assessment: **Medium** (manual Content-Length can cause subtle mismatches if body generation changes)  
* Why it matters: HEAD/GET parity is a core A7 transport invariant; inconsistent Content-Length breaks intermediate caches and clients.  
* Evidence pointer: `diff --git a/adapter/http_reader.py b/adapter/http_reader.py` (Content-Length setting).  
* Approved Plan linkage: PR-03 A7 invariant enforcement on the selected route.

DR-003

* Change summary: Introduce a focused A7 transport test for `/reader` and validate 200 invariants (ETag, cache-control, content-type, vary).  
* Risk assessment: **Low**  
* Why it matters: This is the primary regression net ensuring the contract stays true when refactors occur elsewhere.  
* Evidence pointer: `diff --git a/tests/http/test_reader_a7_transport.py b/tests/http/test_reader_a7_transport.py` (GET invariants assertions).  
* Approved Plan linkage: PR-03 “Add a focused test that validates invariants…”.

DR-004

* Change summary: Validate HEAD/GET parity (ETag equality; Content-Length equality; body absent on HEAD).  
* Risk assessment: **Medium** (this is exactly the class of subtle bug the PR is meant to prevent)  
* Why it matters: Without explicit parity checks, Content-Length/ETag drift can occur undetected while CI remains green.  
* Evidence pointer: `tests/http/test_reader_a7_transport.py` (HEAD parity assertions).  
* Approved Plan linkage: PR-03 A7 transport invariant proof requirements.

DR-005

* Change summary: Validate 304 handling (If-None-Match \-\> 304; no content headers; empty body).  
* Risk assessment: **Medium**  
* Why it matters: 304 header posture is one of the easiest places for framework defaults to violate A7 requirements.  
* Evidence pointer: `tests/http/test_reader_a7_transport.py` (304 assertions).  
* Approved Plan linkage: PR-03 A7 invariant enforcement including 304 posture.

DR-006

* Change summary: Validate writer/error posture for `/reader` (POST \-\> 405; no ETag; Cache-Control no-store).  
* Risk assessment: **Medium**  
* Why it matters: A7 success-route proofs must not accidentally “look cacheable” on error paths.  
* Evidence pointer: `tests/http/test_reader_a7_transport.py` (writer error checks).  
* Approved Plan linkage: PR-03 proof artifacts include writer/error posture proof file.

DR-007

* Change summary: Gate proof-artifact emission behind `HDE_WRITE_A7_PROOFS` (default test runs do not write files).  
* Risk assessment: **Low**  
* Why it matters: Keeps CI deterministic and prevents accidental working-tree dirt from normal test runs.  
* Evidence pointer: `tests/http/test_reader_a7_transport.py` (`HDE_WRITE_A7_PROOFS` gating).  
* Approved Plan linkage: Explicit requirement that artifact writing only happens when an explicit “write artifacts” flag is enabled.

DR-008

* Change summary: Add `/reader` dev-harness entry to the Endpoint Catalog with `internal: true`, `classification: "dev_harness"`, and `env_gate: {"APP_ENV":"dev"}`.  
* Risk assessment: **Medium** (catalog is a governed interface for tooling)  
* Why it matters: The plan requires a single stable success route to be bound into catalog \+ schema so downstream evidence tooling can reference it.  
* Evidence pointer: `artifacts/audit/ENDPOINTS_CATALOG.json` entry for `/reader`.  
* Approved Plan linkage: PR-03 “Update docs/ENDPOINTS\_CATALOG.json to include chosen Reader success route… marked internal… with correct env gate field”.

DR-009

* Change summary: Refresh `docs/ENDPOINTS_CATALOG.json.sha256` to match the new catalog body and correct the relative-path expectations for verification.  
* Risk assessment: **Low** (but CI-critical)  
* Why it matters: Incorrect checksum sidecars can silently break operator validation and CI gates.  
* Evidence pointer: `docs/ENDPOINTS_CATALOG.json.sha256` updated line referencing `docs/ENDPOINTS_CATALOG.json`.  
* Approved Plan linkage: PR-03 requires updating governed catalog artifacts and checksums as part of binding the route.

DR-010

* Change summary: Generate/check in A7 proof artifacts under `artifacts/proofs/` (success GET/HEAD/304, writer errors, encoding invariance, env-gate refusal) with `.path_proof.txt` siblings.  
* Risk assessment: **Low** (additive artifacts)  
* Why it matters: These files are the acceptance “pass proof” that the route’s transport invariants are concretely demonstrated.  
* Evidence pointer: `Files (27)` list and proof file contents under `artifacts/proofs/*`.  
* Approved Plan linkage: PR-03 explicitly requires these proof artifacts and disallows hand editing (must be generated).

DR-011

* Change summary: Register the `epic025` pytest marker to prevent `PytestUnknownMarkWarning` in strict CI settings.  
* Risk assessment: **Low**  
* Why it matters: Unknown-mark warnings can fail CI when warnings are escalated; also, marker registration clarifies test taxonomy.  
* Evidence pointer: `diff --git a/pytest.ini b/pytest.ini` adding `epic025: EPIC025 acceptance tests`.  
* Approved Plan linkage: Supports PR-03 test posture (test family tagging); not a separate plan deliverable but directly required by the introduced mark usage.

### RCA

A) Bug/Failure statement

* PR Artifacts explicitly report: “This PR has generated a CI failure and a bug. Remediation is needed.”  
* The CI failure is shown as `ORIENTATION_DRIFT` with “Error: Process completed with exit code 1.”  
* The bug is described as the endpoint catalog checksum line pointing to the wrong path (“the catalog lives under `docs/`”).

B) Root cause(s)

1. Endpoint catalog checksum sidecar referenced a path that breaks standard verification  
* Root cause statement: The checksum sidecar’s relative path expectations were wrong, so `sha256sum -c docs/ENDPOINTS_CATALOG.json.sha256` fails from repo root when it can’t find the referenced file path.  
* Evidence pointer(s): Pass-2 “Bug” description explaining the missing `./ENDPOINTS_CATALOG.json` from repo root verification expectations.  
2. Orientation proof drift after evidence updates  
* Root cause statement: Governed evidence artifacts changed (index/mirror/path proofs), but `orientation_demo` proof outputs were not refreshed coherently, causing `orientation_demo.py --check` to detect drift.  
* Evidence pointer(s): CI failure lines show `ORIENTATION_DRIFT` and exit code 1 under the `orientation_demo.py --check` step.  
3. New pytest mark used without registration  
* Root cause statement: The test uses `@pytest.mark.epic025` but the mark was not registered, producing `PytestUnknownMarkWarning` that can fail under warning-as-error policies.  
* Evidence pointer(s): “PytestUnknownMarkWarning: Unknown pytest.mark.epic025 … You can register custom marks …”.

C) Fix in this PR

* Corrected the checksum sidecar so it references the catalog under `docs/` (restoring standard `sha256sum -c` usage).  
* Regenerated topology orientation evidence and refreshed index/mirror records in the same PR (clearing the drift condition).  
* Registered the `epic025` marker in `pytest.ini` to eliminate unknown-mark warnings for this acceptance family.

D) Fix verification

* PR Artifacts show the remediation verification commands as passing:  
  * “✅ python tools/evidence/orientation\_demo.py \--check”  
  * “✅ python tools/evidence/update\_evidence\_index.py \--check”  
  * “✅ ci/checks/check\_mirror\_schema.sh”  
* The corrected checksum line references `docs/ENDPOINTS_CATALOG.json` (expected verification target).  
* Focused pytest pass proof is present for the new transport test: “1 passed”.

### Findings

1. 304 responses now omit `Content-Type` and `Content-Length`, and disable auto content-length emission.  
* Evidence pointer: `adapter/http_reader.py` 304 header helper changes.  
* Why it matters: Prevents framework defaults from violating A7 304 posture and avoids cache/semantic drift.  
2. GET/HEAD responses have explicit Content-Length semantics (HEAD matches GET length).  
* Evidence pointer: `adapter/http_reader.py` Content-Length setting \+ `tests/http/test_reader_a7_transport.py` HEAD parity assertions.  
* Why it matters: HEAD/GET parity is a high-risk invariant that is easy to regress without explicit tests.  
3. The transport test enforces strong quoted ETag formatting and treats ETag as a required invariant.  
* Evidence pointer: `tests/http/test_reader_a7_transport.py` ETag assertions.  
* Why it matters: A7 requires stable ETag behavior; weak/absent/malformed ETags break cache safety and parity proofs.  
4. Encoding invariance (identity vs gzip) is explicitly tested and also captured in a proof artifact.  
* Evidence pointer: test file encoding checks \+ `artifacts/proofs/encoding_invariance.txt` content showing identical ETag under gzip.  
* Why it matters: Prevents ETag from accidentally becoming “representation-specific” when compression is used.  
5. 304 handling is validated (If-None-Match \-\> 304, empty body, no content headers).  
* Evidence pointer: `tests/http/test_reader_a7_transport.py` 304 assertions.  
* Why it matters: 304 is a common source of “framework-added” headers that violate A7 posture.  
6. Writer/error posture is tested (POST \-\> 405\) and asserts “no ETag” \+ `Cache-Control: no-store`.  
* Evidence pointer: `tests/http/test_reader_a7_transport.py` writer-error assertions; `artifacts/proofs/success_writers_errors.txt` shows a 405 response with `cache-control: no-store`.  
* Why it matters: Prevents caches from storing error responses as if they were success invariants.  
7. Proof artifact generation is correctly gated behind `HDE_WRITE_A7_PROOFS`, keeping default runs clean/deterministic.  
* Evidence pointer: `tests/http/test_reader_a7_transport.py` gating block and Approved Plan requirement for explicit flag gating.  
* Why it matters: Avoids “tests dirtied my repo” failures and preserves CI determinism.  
8. `/reader` is bound into the Endpoint Catalog as `internal`/`dev_harness` with `env_gate: {"APP_ENV":"dev"}` and `a7_eligible: true`.  
* Evidence pointer: `/reader` entry in `artifacts/audit/ENDPOINTS_CATALOG.json`.  
* Why it matters: This is the primary “contract binding” that downstream tooling will rely on.  
9. Env-gate refusal proof exists and shows a forbidden response in non-dev posture.  
* Evidence pointer: `artifacts/proofs/endpoints_env_gate_proof.log` includes `HTTP/1.0 403 FORBIDDEN` and `cache-control: no-store` with `etag: (absent)`.  
* Why it matters: Confirms the route is not accidentally “publicly usable” outside the dev harness.  
10. The endpoint catalog checksum sidecar references `docs/ENDPOINTS_CATALOG.json`, restoring typical `sha256sum -c` verification.  
* Evidence pointer: `docs/ENDPOINTS_CATALOG.json.sha256` line shows the `docs/` path target.  
* Why it matters: Prevents operator/CI checksum verification regressions.  
11. Evidence/index coherence remediation is explicitly shown as passing in PR Artifacts (“✅ … \--check” lines), addressing the earlier ORIENTATION\_DRIFT failure mode.  
* Evidence pointer: Actions Taken “Testing” section with passing checkmarks.  
* Why it matters: Ensures the governed evidence skeleton remains coherent after adding new proof artifacts and catalog entries.  
12. Scope drift check: the changed/added files listed are limited to Reader transport handling, the new transport test, Endpoint Catalog \+ checksum/path proofs, proof artifacts, and evidence index refresh outputs.  
* Evidence pointer: `Files (27)` list enumerating only these families (adapter, tests, proofs, catalog/checksums, evidence index, topology proof).  
* Why it matters: Confirms the PR stays within PR-03 scope described in the Approved Plan.

### Evidence Print (PASS PROOF; required)

A) Tokens satisfied (names-only; do not invent)

* None explicitly claimed as satisfied by PR Artifacts or Approved Plan for PR-03.  
  Search method: searched at for "tokens" (case-sensitive or insensitive: insensitive).

B) Evidence artifacts produced/updated

* `artifacts/audit/ENDPOINTS_CATALOG.json`  
  * Type: json  
  * Key proof facts: includes `/reader` entry with `classification`: `dev_harness`, `internal`: `true`, and `env_gate`: `{"APP_ENV":"dev"}`.  
* `docs/ENDPOINTS_CATALOG.json.sha256`  
  * Type: sha256 sidecar  
  * Key proof facts (verbatim): `4ff9c5c8fc53c0682dbb76e78aff27c4cddbc96ba805a297e1c2bd0c9c7c3142 docs/ENDPOINTS_CATALOG.json`.  
* `artifacts/proofs/endpoints_env_gate_proof.log`  
  * Type: log/text  
  * Key proof facts (verbatim): `HTTP/1.0 403 FORBIDDEN`; `cache-control: no-store`; `etag: (absent)`.  
  * sha256 (verbatim from PR Artifacts): `83ea8e2f8ac4bafebfcf1bba82f507e35b436a0e4dd0d0c2b369ef2fce2cd970`.  
* `artifacts/proofs/success_get.txt`  
  * Type: text  
  * Key proof facts (verbatim): `HTTP/1.0 200 OK`; `cache-control: private, max-age=0, must-revalidate`; `vary: Authorization, Accept-Encoding`; `etag: "1cbd848103ac56efd7bc284db333bd70e879a963ddb0c12a570fc05354291fac"`.  
  * sha256 (verbatim from PR Artifacts): `582d9c6b08e875cd0bd6ba2171401f760ba010836fd5f0b2ad7dce4fe78492ed`.  
* `artifacts/proofs/success_head.txt`  
  * Type: text  
  * Key proof facts (verbatim): `HTTP/1.0 200 OK`; `cache-control: private, max-age=0, must-revalidate`; `etag: "1cbd848103ac56efd7bc284db333bd70e879a963ddb0c12a570fc05354291fac"`.  
  * sha256 (verbatim from PR Artifacts): `582d9c6b08e875cd0bd6ba2171401f760ba010836fd5f0b2ad7dce4fe78492ed`.  
* `artifacts/proofs/success_304.txt`  
  * Type: text  
  * Key proof facts (verbatim): `HTTP/1.0 304 NOT MODIFIED`; `etag: "1cbd848103ac56efd7bc284db333bd70e879a963ddb0c12a570fc05354291fac"`; `content-type: (absent)`; `content-length: (absent)`.  
  * sha256 (verbatim from PR Artifacts): `75c9d1d4fc4beab98721cc777fbaec3216585975c919ad388c14e5dab2ece9c7`.  
* `artifacts/proofs/success_writers_errors.txt`  
  * Type: text  
  * Key proof facts (verbatim): `HTTP/1.0 405 METHOD NOT ALLOWED`; `cache-control: no-store`; `etag: (absent)`.  
  * sha256 (verbatim from PR Artifacts): `78fca93a0e2610dd31dcd7a95e3333f000b9b3a8042f6c2f05f1ed5f8f1c6cc3`.  
* `artifacts/proofs/encoding_invariance.txt`  
  * Type: text  
  * Key proof facts (verbatim): `etag_identity: "1cbd848103ac56efd7bc284db333bd70e879a963ddb0c12a570fc05354291fac"`; `etag_gzip: "1cbd848103ac56efd7bc284db333bd70e879a963ddb0c12a570fc05354291fac"`.  
  * sha256 (verbatim from PR Artifacts): `7c4457d2f47f5278b15108cd17ac93f25532eaa9ba8d64cf486ed1c571f7a669`.  
* Evidence/mirror refresh outputs (governed)  
  * `docs/evidence/INDEX.json` / `docs/evidence/INDEX.sha256` / `artifacts/evidence_index.jsonl` (+ their `.path_proof.txt` siblings) are updated as part of the PR-03 evidence refresh step.  
  * Key proof facts (verbatim): PR Artifacts state the evidence catalog/mirror was updated via `python tools/evidence/update_evidence_index.py` and added the new proof artifacts with `.path_proof.txt` siblings present.

C) Test/CI proof

* `python -m pytest -q tests/http/test_reader_a7_transport.py`  
  * Pass indicator (verbatim): `1 passed in 0.21s`  
  * Where it appears in PR Artifacts: Testing output block.  
* `HDE_WRITE_A7_PROOFS=1 python -m pytest -q tests/http/test_reader_a7_transport.py`  
  * Pass indicator (verbatim): outcome: `1 passed`  
  * Where it appears in PR Artifacts: Evidence Index narrative line describing the run and outcome.  
* `python tools/evidence/orientation_demo.py --check`  
  * Pass indicator (verbatim): `✅ python tools/evidence/orientation_demo.py --check`  
  * Where it appears in PR Artifacts: Actions Taken → Testing list.  
* `python tools/evidence/update_evidence_index.py --check`  
  * Pass indicator (verbatim): `✅ python tools/evidence/update_evidence_index.py --check`  
  * Where it appears in PR Artifacts: Actions Taken → Testing list.  
* `ci/checks/check_mirror_schema.sh`  
  * Pass indicator (verbatim): `✅ ci/checks/check_mirror_schema.sh`  
  * Where it appears in PR Artifacts: Actions Taken → Testing list.

## 2.14 PR04 HDE-EPIC025

### Review Summary

* PR adds the EPIC-025 close-pack pair plus a normalized QA evidence root with a step-logs manifest, and captures the required preflight \+ gate run logs under `audit/qa/hde-epic025/checks/...`.  
* PR introduces/lands evidence-discipline tooling expected by the plan: `tools/evidence/validate_evidence_paths.py` and `tools/evidence/check_lf_endings.py`, plus an EPIC-025 close-pack generator.  
* Scope aligns with the Approved Plan’s PR-04 deliverables: canonical JSON gate outputs evidence, evidence index/mirror discipline evidence, QA evidence root, and close-pack pair (no unrelated feature work observed in the diff surface).  
* Evidence posture is strong: gate logs show `status: 0` for canonical JSON, evidence index update, evidence paths validation, mirror schema, and LF endings, and pytest logs show passing runs for the required checks.  
* Diff review found one meaningful risk area (new evidence-path validator correctness), but it was explicitly remediated within the PR lifecycle (path traversal rejection \+ JSON-object enforcement).  
* RCA section included (triggered by explicit “Bug Remediation” / “bug” / “fix” content in PR Artifacts) and covers the evidence-path validation bypasses and their closure.

### Diff Review (REQUIRED; primary technical review)

DR-001

* Change summary: Add LF-ending gate wrapper `tools/evidence/check_lf_endings.py` that runs `ci/checks/check_final_lf.sh` under determinism env pins.  
* Risk assessment: Low  
* Why it matters: Ensures the plan-required LF gate can be executed in a pinned/deterministic environment and recorded as governed evidence.  
* Evidence pointer: PR Artifacts → Diff → `tools/evidence/check_lf_endings.py`  
* Approved Plan linkage: PR-04 “Evidence tool command shapes” \+ planned output `audit/qa/hde-epic025/checks/gate_lf_endings/primary.log`

DR-002

* Change summary: Add evidence-index path validator `tools/evidence/validate_evidence_paths.py` that loads `artifacts/evidence_index.jsonl` and verifies `discovered_physical_path` is safe and exists.  
* Risk assessment: Medium  
* Why it matters: This gate becomes an integrity check for all evidence binding; if wrong, it can produce false confidence or allow unsafe path references.  
* Evidence pointer: PR Artifacts → Diff → `tools/evidence/validate_evidence_paths.py`  
* Approved Plan linkage: PR-04 “Evidence index and mirror discipline” \+ planned output `audit/qa/hde-epic025/checks/gate_evidence_paths_validation/primary.log`

DR-003

* Change summary: Harden `validate_evidence_paths.py` against absolute paths, `..` traversal segments, and out-of-root resolved paths.  
* Risk assessment: Low  
* Why it matters: Prevents traversal-style bypass where a malicious/incorrect evidence index entry points outside the repo root.  
* Evidence pointer: PR Artifacts → Diff → `tools/evidence/validate_evidence_paths.py` (checks for `candidate.is_absolute()`, `.. in candidate.parts`, and `resolved.relative_to(root_resolved)`)  
* Approved Plan linkage: PR-04 “Evidence index and mirror discipline”

DR-004

* Change summary: Enforce that each evidence-index JSONL line is a JSON object (dict) before reading `discovered_physical_path`.  
* Risk assessment: Low  
* Why it matters: Prevents validator bypass via non-object JSON lines that previously could evade field checks.  
* Evidence pointer: PR Artifacts → Diff → `tools/evidence/validate_evidence_paths.py` (`if not isinstance(obj, dict): raise SystemExit(...)`)  
* Approved Plan linkage: PR-04 “Evidence index and mirror discipline”

DR-005

* Change summary: Add EPIC-025 close-pack generator `tools/qa/generate_epic025_close_pack.py` to write `audit/EPIC-025_MANIFEST.json`, `audit/EPIC-025_close_report.md`, `audit/docdeltas/hde-epic025_doc_deltas.md`, and QA step manifest \+ path proof.  
* Risk assessment: Medium  
* Why it matters: This is the mechanism producing the close-pack artifacts “mechanically” and becomes the source of truth for the close-pack schema/bindings.  
* Evidence pointer: PR Artifacts → Diff → `tools/qa/generate_epic025_close_pack.py`  
* Approved Plan linkage: PR-04 “Close-pack pair” \+ “QA evidence root”

DR-006

* Change summary: Add QA evidence root manifest `audit/qa/hde-epic025/qa_step_logs_manifest.json` mapping check IDs to `primary.log` paths.  
* Risk assessment: Low  
* Why it matters: Provides the plan-required single entrypoint to the QA evidence root and standardizes discovery of check logs.  
* Evidence pointer: PR Artifacts → Diff → `audit/qa/hde-epic025/qa_step_logs_manifest.json`  
* Approved Plan linkage: PR-04 “QA evidence root” \+ planned output list

DR-007

* Change summary: Add path proof transcript for the QA step logs manifest.  
* Risk assessment: Low  
* Why it matters: Provides governed evidence for the manifest file itself (hash/size/mtime).  
* Evidence pointer: PR Artifacts → Diff → `audit/qa/hde-epic025/qa_step_logs_manifest.json.path_proof.txt`  
* Approved Plan linkage: Planned evidence outputs include this exact file

DR-008

* Change summary: Add gate logs under `audit/qa/hde-epic025/checks/gate_*` for canonical JSON, evidence index update, evidence path validation, mirror schema, and LF endings.  
* Risk assessment: Low  
* Why it matters: These are the plan’s primary “PASS proof” artifacts for evidence discipline and canonical JSON conformance.  
* Evidence pointer: PR Artifacts → Diff → `audit/qa/hde-epic025/checks/gate_canonical_json/primary.log` (and sibling gate logs)  
* Approved Plan linkage: Planned evidence outputs list includes all gate log paths

DR-009

* Change summary: Add preflight logs `preflight_e1`…`preflight_e6` and `preflight_p3/p4/p6` under the QA evidence root.  
* Risk assessment: Low  
* Why it matters: These capture the plan’s required confirmation checks (pytest confirmation runs, token roster check, evidence endpoint hashes, rails closure).  
* Evidence pointer: PR Artifacts → Diff → `audit/qa/hde-epic025/checks/preflight_p4_evidence_endpoints/primary.log` (and sibling preflight logs)  
* Approved Plan linkage: Planned evidence outputs include these exact preflight log files

DR-010

* Change summary: Add EPIC close-pack manifest `audit/EPIC-025_MANIFEST.json` with `key_outputs` bindings across PR-01…PR-04 artifacts.  
* Risk assessment: Low  
* Why it matters: This is the primary artifact-binding index for “what ships” and “where the evidence lives” for EPIC-025 closure.  
* Evidence pointer: PR Artifacts → Diff → `audit/EPIC-025_MANIFEST.json`  
* Approved Plan linkage: PR-04 “Close-pack pair” \+ “Manifest must include a key\_outputs map…”

DR-011

* Change summary: Add EPIC close report `audit/EPIC-025_close_report.md` summarizing deliverables, explicit deferrals, and pointing to `key_outputs`.  
* Risk assessment: Low  
* Why it matters: Human-readable closure summary and deferral inventory are required for EPIC close-pack completeness.  
* Evidence pointer: PR Artifacts → Diff → `audit/EPIC-025_close_report.md`  
* Approved Plan linkage: PR-04 “Close report must summarize… list deferrals… point to key\_outputs entries”

DR-012

* Change summary: Update canonical JSON gate output path-proof transcripts under `audit/gates/json_gate/canonical/*.path_proof.txt`.  
* Risk assessment: Low  
* Why it matters: Keeps governed proofs for canonical JSON gate outputs current (hash/mtime evidence).  
* Evidence pointer: PR Artifacts → Diff → `audit/gates/json_gate/canonical/json_gate_check_log.ndjson.path_proof.txt` (and sibling path proofs)  
* Approved Plan linkage: Planned evidence outputs include these exact path proof files

### RCA (only if RCA ADD-ON is triggered)

A) Bug/Failure statement (1–3 sentences; quote key lines from PR Artifacts)

* “A bug was found: tools/evidence/validate\_evidence\_paths.py allows path traversal attacks by passing in a path with ".." segments and pointing to a file outside of the artifacts directory.”  
  Evidence pointer: PR Artifacts → Bug Remediation 1 → Fix Prompt  
* “A bug was found: tools/evidence/validate\_evidence\_paths.py validates discovered\_physical\_path without ensuring each evidence index record is a JSON object, allowing bypass with a non-object line.”  
  Evidence pointer: PR Artifacts → Bug Remediation 2 → Fix Prompt

B) Root cause(s)

1. Root cause: Path validation did not explicitly reject `..` traversal segments / absolute paths before resolving and checking existence.  
   Evidence pointer(s):  
   * PR Artifacts → Bug Remediation 1 → Fix Prompt  
   * PR Artifacts → Diff → `tools/evidence/validate_evidence_paths.py` (now includes `candidate.is_absolute()` and `if ".." in candidate.parts:` and `resolved.relative_to(root_resolved)` guards)  
2. Root cause: Evidence index parsing allowed non-object JSON lines such that the validator could not reliably enforce field-level invariants.  
   Evidence pointer(s):  
   * PR Artifacts → Bug Remediation 2 → Fix Prompt  
   * PR Artifacts → Diff → `tools/evidence/validate_evidence_paths.py` (now includes `if not isinstance(obj, dict): raise SystemExit(...)`)

C) Fix in this PR

* Add absolute-path rejection and traversal-segment rejection (`..`) before resolution.  
  Evidence pointer: PR Artifacts → Diff → `tools/evidence/validate_evidence_paths.py`  
* Enforce root containment on the resolved path via `relative_to(root_resolved)` failure handling.  
  Evidence pointer: PR Artifacts → Diff → `tools/evidence/validate_evidence_paths.py`  
* Require each JSONL record to be a JSON object before reading `discovered_physical_path`.  
  Evidence pointer: PR Artifacts → Diff → `tools/evidence/validate_evidence_paths.py`

D) Fix verification

* Proof the validator passes after hardening:  
  * `python tools/evidence/validate_evidence_paths.py` → `evidence-paths-validation: ok`  
    Evidence pointer: PR Artifacts → Bug Remediation 1 → Testing  
* Proof the validator passes after JSON-object enforcement:  
  * `python tools/evidence/validate_evidence_paths.py` → `evidence-paths-validation: ok`  
    Evidence pointer: PR Artifacts → Bug Remediation 2 → Testing  
* Gate evidence also shows execution \+ success:  
  * `status: 0` and `output: evidence-paths-validation: ok`  
    Evidence pointer: PR Artifacts → Diff → `audit/qa/hde-epic025/checks/gate_evidence_paths_validation/primary.log`

Residual risk/edge case (only if evidenced): None evidenced in PR Artifacts beyond the two closed bypass classes above.

### Findings

1. PR adds the plan-required QA evidence root manifest (`qa_step_logs_manifest.json`) mapping check IDs to log paths.  
   * Evidence pointer: PR Artifacts → Diff → `audit/qa/hde-epic025/qa_step_logs_manifest.json`  
   * Why it matters: This is the primary index for human review and automated discovery of evidence logs.  
2. PR adds a governed path proof for the QA evidence root manifest.  
   * Evidence pointer: PR Artifacts → Diff → `audit/qa/hde-epic025/qa_step_logs_manifest.json.path_proof.txt`  
   * Why it matters: Ensures the QA manifest itself is verifiable (hash/size/mtime).  
3. PR lands `tools/evidence/check_lf_endings.py` matching the Approved Plan’s command shape and recording via `gate_lf_endings/primary.log`.  
   * Evidence pointer: PR Artifacts → Diff → `tools/evidence/check_lf_endings.py`  
   * Why it matters: Provides a stable, repo-local gate entrypoint for LF checks and evidence capture.  
4. Gate evidence shows LF endings check ran and passed (`status: 0`).  
   * Evidence pointer: PR Artifacts → Diff → `audit/qa/hde-epic025/checks/gate_lf_endings/primary.log`  
   * Why it matters: Satisfies acceptance token `CI_CHECK_FINAL_LF_OK` from the Approved Plan.  
5. PR lands `tools/evidence/validate_evidence_paths.py` and it enforces determinism env pins and safe/contained path resolution.  
   * Evidence pointer: PR Artifacts → Diff → `tools/evidence/validate_evidence_paths.py`  
   * Why it matters: This is the core integrity check preventing evidence-index → filesystem drift or unsafe bindings.  
6. Evidence-path validation gate ran and passed (`status: 0`, `output: evidence-paths-validation: ok`).  
   * Evidence pointer: PR Artifacts → Diff → `audit/qa/hde-epic025/checks/gate_evidence_paths_validation/primary.log`  
   * Why it matters: Satisfies acceptance token `EVIDENCE_PATHS_VALIDATED_OK` from the Approved Plan.  
7. Evidence index update gate ran and passed (`status: 0`, `output: evidence-index: ok`).  
   * Evidence pointer: PR Artifacts → Diff → `audit/qa/hde-epic025/checks/gate_evidence_index_update/primary.log`  
   * Why it matters: This is the direct proof for `EVIDENCE_INDEX_UPDATED_OK` and underpins index/hash/mirror discipline.  
8. Evidence index mirror `--check` was executed and passed (`status: 0`).  
   * Evidence pointer: PR Artifacts → Diff → `audit/qa/hde-epic025/checks/preflight_e6_evidence_index_mirror/primary.log`  
   * Why it matters: Strengthens proof for `EVIDENCE_INDEX_MIRROR_OK` / `EVIDENCE_INDEX_HASH_OK` as a consistency check.  
9. Mirror schema validation gate ran and passed (`status: 0`).  
   * Evidence pointer: PR Artifacts → Diff → `audit/qa/hde-epic025/checks/gate_mirror_schema/primary.log`  
   * Why it matters: Satisfies acceptance token `CI_CHECK_MIRROR_SCHEMA_OK`.  
10. Canonical JSON gate ran and passed (`status: 0`) and enumerated the canonical output artifact paths under `audit/gates/json_gate/canonical/`.  
* Evidence pointer: PR Artifacts → Diff → `audit/qa/hde-epic025/checks/gate_canonical_json/primary.log`  
* Why it matters: Satisfies `JSON_CANONICAL_CHECK_OK` and provides a governed gate record.  
11. PR updates canonical JSON gate path-proof transcripts, including sha256 values.  
* Evidence pointer: PR Artifacts → Diff → `audit/gates/json_gate/canonical/json_gate_check_log.ndjson.path_proof.txt` (and sibling path proofs)  
* Why it matters: Provides governed proof artifacts for canonical JSON outputs as required by the Approved Plan’s planned output list.  
12. EPIC-025 close-pack manifest is added with a `key_outputs` map binding primary artifacts across PR-01…PR-04.  
* Evidence pointer: PR Artifacts → Diff → `audit/EPIC-025_MANIFEST.json`  
* Why it matters: This is the closure binding surface reviewers depend on to locate canonical evidence.  
13. EPIC-025 close report is added and includes the required explicit deferral TI-002 and a key\_outputs pointer section.  
* Evidence pointer: PR Artifacts → Diff → `audit/EPIC-025_close_report.md`  
* Why it matters: Meets the Approved Plan’s close report requirement to summarize delivered work, list deferrals, and reference the manifest bindings.  
14. Mechanization path: PR adds `tools/qa/generate_epic025_close_pack.py` to generate close-pack artifacts and the QA step manifest \+ path proof.  
* Evidence pointer: PR Artifacts → Diff → `tools/qa/generate_epic025_close_pack.py`  
* Why it matters: This supports the “mechanically generated” requirement in the Approved Plan; main risk is future coupling to helper internals, but no breakage is evidenced here.

### Evidence Print (PASS PROOF; required)

A) Tokens satisfied (names-only; do not invent)

EVIDENCE\_INDEX\_UPDATED\_OK

* Evidence pointer(s): PR Artifacts → Diff → `audit/qa/hde-epic025/checks/gate_evidence_index_update/primary.log` (`status: 0`, `output: evidence-index: ok`)

EVIDENCE\_INDEX\_HASH\_OK

* Evidence pointer(s):  
  * PR Artifacts → Diff → `audit/qa/hde-epic025/checks/preflight_p4_evidence_endpoints/primary.log` (`sha256 docs/evidence/INDEX.sha256: ...`)  
  * PR Artifacts → Diff → `audit/qa/hde-epic025/checks/preflight_e6_evidence_index_mirror/primary.log` (`python tools/evidence/update_evidence_index.py --check`, `status: 0`)

EVIDENCE\_INDEX\_MIRROR\_OK

* Evidence pointer(s):  
  * PR Artifacts → Diff → `audit/qa/hde-epic025/checks/preflight_e6_evidence_index_mirror/primary.log` (`status: 0`, `evidence-index: ok`)  
  * PR Artifacts → Diff → `audit/qa/hde-epic025/checks/gate_mirror_schema/primary.log` (`status: 0`)

EVIDENCE\_PATHS\_VALIDATED\_OK

* Evidence pointer(s): PR Artifacts → Diff → `audit/qa/hde-epic025/checks/gate_evidence_paths_validation/primary.log` (`status: 0`, `output: evidence-paths-validation: ok`)

CI\_CHECK\_MIRROR\_SCHEMA\_OK

* Evidence pointer(s): PR Artifacts → Diff → `audit/qa/hde-epic025/checks/gate_mirror_schema/primary.log` (`status: 0`)

CI\_CHECK\_FINAL\_LF\_OK

* Evidence pointer(s): PR Artifacts → Diff → `audit/qa/hde-epic025/checks/gate_lf_endings/primary.log` (`status: 0`)

JSON\_CANONICAL\_CHECK\_OK

* Evidence pointer(s): PR Artifacts → Diff → `audit/qa/hde-epic025/checks/gate_canonical_json/primary.log` (`status: 0`, output lists canonical JSON gate outputs)

B) Evidence artifacts produced/updated

audit/EPIC-025\_MANIFEST.json

* Type: json  
* Key proof facts (verbatim):  
  * `"close_report":"audit/EPIC-025_close_report.md"`  
  * `"key_outputs":{...}`  
* Evidence pointer: PR Artifacts → Diff → `audit/EPIC-025_MANIFEST.json`

audit/EPIC-025\_close\_report.md

* Type: markdown  
* Key proof facts (verbatim):  
  * `- TI-002: defers Dev HTTP Harness and Writer Surfaces to HDE-EPIC026.`  
  * `Key outputs`  
* Evidence pointer: PR Artifacts → Diff → `audit/EPIC-025_close_report.md`

audit/qa/hde-epic025/qa\_step\_logs\_manifest.json

* Type: json  
* Key proof facts (verbatim):  
  * `"gate_canonical_json":{"check_id":"gate_canonical_json","log_path":"audit/qa/hde-epic025/checks/gate_canonical_json/primary.log"}`  
* Evidence pointer: PR Artifacts → Diff → `audit/qa/hde-epic025/qa_step_logs_manifest.json`

audit/qa/hde-epic025/qa\_step\_logs\_manifest.json.path\_proof.txt

* Type: text  
* Key proof facts (verbatim):  
  * `sha256: 29aab9a93ab8b19f5c126a0c5b00da3d6fbc3446ea91111566adbb9f3bce49c2`  
* Evidence pointer: PR Artifacts → Diff → `audit/qa/hde-epic025/qa_step_logs_manifest.json.path_proof.txt`

audit/qa/hde-epic025/checks/gate\_evidence\_index\_update/primary.log

* Type: log  
* Key proof facts (verbatim):  
  * `status: 0`  
  * `output: evidence-index: ok`  
* Evidence pointer: PR Artifacts → Diff → `audit/qa/hde-epic025/checks/gate_evidence_index_update/primary.log`

audit/qa/hde-epic025/checks/gate\_evidence\_paths\_validation/primary.log

* Type: log  
* Key proof facts (verbatim):  
  * `status: 0`  
  * `output: evidence-paths-validation: ok`  
* Evidence pointer: PR Artifacts → Diff → `audit/qa/hde-epic025/checks/gate_evidence_paths_validation/primary.log`

audit/qa/hde-epic025/checks/gate\_canonical\_json/primary.log

* Type: log  
* Key proof facts (verbatim):  
  * `status: 0`  
  * `output: canonical-json-gate: ok`  
* Evidence pointer: PR Artifacts → Diff → `audit/qa/hde-epic025/checks/gate_canonical_json/primary.log`

audit/docdeltas/hde-epic025\_doc\_deltas.md

* Type: markdown  
* Key proof facts (verbatim):  
  * `Doc Deltas: None (no PF-Canon inconsistencies or new doc requirements found)`  
* Evidence pointer: PR Artifacts → Diff → `audit/docdeltas/hde-epic025_doc_deltas.md`

C) Test/CI proof

tests/http/test\_compat\_endpoint\_contract.py

* Pass indicator (verbatim): `4 passed in 0.51s`  
* Where it appears: PR Artifacts → Diff → `audit/qa/hde-epic025/checks/preflight_e1_http_compat/primary.log`

tests/cli/test\_cli\_canonical\_bytes.py

* Pass indicator (verbatim): `3 passed in 0.03s`  
* Where it appears: PR Artifacts → Diff → `audit/qa/hde-epic025/checks/preflight_e3_cli_entrypoint/primary.log`

tests/http/test\_reader\_a7\_transport.py

* Pass indicator (verbatim): `1 passed in 0.08s`  
* Where it appears: PR Artifacts → Diff → `audit/qa/hde-epic025/checks/preflight_e5_a7_transport_invariants/primary.log`

tests/ops/test\_evidence\_index.py

* Pass indicator (verbatim): `1 passed in 0.06s`  
* Where it appears: PR Artifacts → Diff → `audit/qa/hde-epic025/checks/preflight_e6_evidence_index_mirror/primary.log`

\<eof\>