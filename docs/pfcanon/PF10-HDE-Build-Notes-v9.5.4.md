# 0\) Front Matter

**Name:** PF10-HDE-Build-Notes   
**Version:** v9.5.4  
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
2. 2.2 Prohibited characters in planning reviews and planning documents (ellipsis only)

3. 2.3 Heading levels are non-reviewable in planning reviews (AI redline limitation)’

4. 2.4 Conjunction Pass 1 scope deferral: move remaining HDE-CONJ001 and HDE-CONJ008 to HDE-EPIC026

5. 2.5 Conjunction planning token reconciliation: PF27 and PF09 must use Governance token spellings; no new compat keyset token

6. 2.6 Planning path discipline: canon-first \+ CA/IG verbatim validation; never fabricate repo paths

7. 2.7 File minting procedure for new epics (canon-first validation; CA vetted and IG Approved quotes; Codex prompts stay attachment-free)

8. 2.8 Acceptance token minting and claim rules for epic planning

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

## **2.2 Prohibited characters in planning reviews and planning documents (ellipsis only)**

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

## **2.6 Planning path discipline: canon-first \+ CA/IG verbatim validation; never fabricate repo paths**

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

## **2.7 File minting procedure for new epics (canon-first validation; CA vetted and IG Approved quotes; Codex prompts stay attachment-free)**

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

## 2.8 Acceptance token minting and claim rules for epic planning

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

\<eof\>