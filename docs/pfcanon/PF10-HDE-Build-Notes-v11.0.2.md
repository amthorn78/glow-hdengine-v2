# 0\) Front Matter

**Name:** PF10-HDE-Build-Notes   
**Version:** v11.0.2  
Effective Date: 2026.05.17

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

2.1) DB bridge/provider parity proof-label posture  
2.2) Template hygiene defects are non-blocking unless they affect truth, portability, evidence identity, or execution safety

# 2\) Numbered Addenda

---

## 2.1) DB bridge/provider parity proof-label posture

Timestamp: 051726 00:25

Details: HDE-EPIC032 planning identified a token-registry ambiguity in the DB runtime posture work. HDE-Build Checklist — Fermentation names `DB_PROVIDER_PARITY_OK`, `DB_BRIDGE_CAPS_OK`, and `DB_BRIDGE_FALLBACK_OK` in the DB posture rows for `HDE-FERM004.2` and `HDE-FERM004.4`, but the current planning audit did not confirm `DB_PROVIDER_PARITY_OK` or `DB_BRIDGE_CAPS_OK` as registered acceptance tokens in HDE-Governance, and confirmed only `DEV_DB_BRIDGE_FALLBACK_OK` for the bridge-fallback token family.

Until this addendum is drained into the owning permanent PF homes, this addendum is the live-truth rule for HDE-EPIC032 DB runtime posture token claims.

For HDE-EPIC032:

* `DB_PROVIDER_PARITY_OK` is a non-token proof label unless and until HDE-Governance registers it as an acceptance token.  
* `DB_BRIDGE_CAPS_OK` is a non-token proof label unless and until HDE-Governance registers it as an acceptance token.  
* `DB_BRIDGE_FALLBACK_OK` is a non-token proof label unless and until HDE-Governance registers it as an acceptance token.  
* `DEV_DB_BRIDGE_FALLBACK_OK` remains the canonical bridge-fallback acceptance token where the scope is dev bridge fallback.  
* Implementation plans, PR summaries, OPS evidence, QA logs, acceptance maps, token-evidence matrices, and closeout artifacts MUST NOT claim `DB_PROVIDER_PARITY_OK`, `DB_BRIDGE_CAPS_OK`, or `DB_BRIDGE_FALLBACK_OK` as satisfied acceptance tokens unless those exact names are registered in HDE-Governance or later minted by a higher-numbered PF10 addendum.  
* Evidence collection for provider parity, bridge capability, and non-dev bridge fallback MAY proceed as governed proof obligations without claiming those proof labels as acceptance tokens.  
* Acceptance artifacts MUST use existing registered tokens where applicable, including DB posture, determinism, canonical JSON, Evidence Index, Machine Mirror, path-proof, and final-LF tokens already registered in HDE-Governance.  
* If close-stage review determines that provider parity, bridge capability, or non-dev bridge fallback must become gated acceptance predicates, the token names and semantics MUST be admitted through HDE-Governance before any acceptance artifact claims them.

Drain targets:

* HDE-Governance, Acceptance Tokens: clarify whether `DB_PROVIDER_PARITY_OK`, `DB_BRIDGE_CAPS_OK`, and `DB_BRIDGE_FALLBACK_OK` are admitted tokens or explicitly non-token proof labels.  
* HDE-Build Checklist — Fermentation, `HDE-FERM004.2` and `HDE-FERM004.4`: align DB posture row language with the Governance token decision.  
* HDE-Mechanics Guide, Bridge parity mechanics: keep provider parity and bridge capability mechanics as proof obligations without token semantics unless Governance admits token names.

Plan impact:

* HDE-EPIC032 Deliverable D3 remains affected but not blocked.  
* HDE-EPIC032 Deliverable D5 remains affected but not blocked.  
* PR-03 may implement bridge capability and provider parity proof work using existing registered tokens plus non-token proof labels.  
* OPS-01 may capture provider parity evidence as OPS evidence, not QA evidence, and without token overclaim.  
* PR-04 may index DB posture and bridge evidence without claiming unregistered DB bridge/provider parity token names.

## 2.2) Template hygiene defects are non-blocking unless they affect truth, portability, evidence identity, or execution safety

Timestamp: 051726 00:00

Details: HDE-EPIC032 planning and review exposed a repeated false-blocker pattern. Reviewers treated template hygiene defects as approval blockers even when the plan’s scope, PF09 mapping, PF10 posture, proof target, implementation boundary, and execution safety were otherwise clear.

This addendum distinguishes valid blockers from canon/template nits for HDE-EPIC032 and future Glow planning reviews.

\#\#\# Decision / rule / clarification

A planning artifact MUST NOT be blocked solely for template hygiene, formatting, inventory completeness, provenance-label phrasing, or quote-block style unless the defect changes at least one of the following:

\* source-of-truth authority  
\* implementation scope  
\* PF09 completion mapping  
\* acceptance-token truth  
\* evidence identity  
\* evidence trust  
\* Codex portability  
\* OPS/PR boundary  
\* execution safety  
\* public/private surface posture  
\* canon conflict handling  
\* closeout truth

If none of those are affected, the issue is a Nit, Suggestion, or Caveat, not a Blocker.

\#\#\# Valid blocker classes

The following remain valid blockers:

\* PF10 says one thing and the plan says the opposite.  
\* The plan keeps an ADR open after PF10 already resolves the exact topic.  
\* The plan routes a topic to a new PF10 addendum when an applicable PF10 addendum already exists.  
\* The plan claims an unregistered token as an acceptance token.  
\* The plan marks work Already Implemented without embedding enough proof or pointing to an allowed proof form.  
\* The plan requires Codex to consult CA, audit files, attachments, chat history, implementation guides, or other non-PF sources.  
\* The plan requires OPS work inside Codex PR work.  
\* The plan asserts an existing repo locus without any allowed proof or discovery-first posture.  
\* The plan creates or widens public surface scope without canon support.  
\* The plan makes PF23 a deliverable, token source, blocker source, or acceptance authority.  
\* The plan uses PF20 as current planning, token, evidence, acceptance, rails, or required-now authority.

\#\#\# Non-blocking template hygiene issues

The following MUST NOT be blockers by themselves:

\* a missing token row in a Token Inventory table, when the plan does not overclaim the token and the relevant evidence family is otherwise scoped  
\* a missing Epic QA root declaration in an Epic Plan, when the Epic Plan is not authorizing QA execution and no QA evidence production depends on that omission  
\* CA-vetted fact formatting that is not in perfect quote-block form, when the fact is embedded clearly and does not require Codex to consult CA  
\* use of phrases like “CA vetted path” or “vetted repo fact” as provenance labels, when the plan remains self-contained and does not require external CA access  
\* table formatting, heading style, punctuation, spacing, bold markers, or presentation style  
\* path labels that are clear enough for planning and not used as executable commands  
\* inventory-row ordering  
\* section phrasing that is semantically correct but not template-perfect  
\* lack of section locator precision where the plan is not making a canon-dependent claim  
\* missing “titles-only” polish when the source authority and plan posture remain clear

These may be raised as Caveats, Suggestions, or Nits if cleanup would improve the artifact. They do not justify REVISE AND RESUBMIT unless they create a material truth, proof, portability, or execution defect.

\#\#\# HDE-EPIC032-specific application

For HDE-EPIC032:

\* The PF10 DB bridge/provider parity proof-label posture is authoritative.  
\* \`DB\_PROVIDER\_PARITY\_OK\`, \`DB\_BRIDGE\_CAPS\_OK\`, and \`DB\_BRIDGE\_FALLBACK\_OK\` remain non-token proof labels unless and until HDE-Governance registers them as acceptance tokens.  
\* \`DEV\_DB\_BRIDGE\_FALLBACK\_OK\` remains the canonical bridge-fallback acceptance token where the scope is dev bridge fallback.  
\* A plan must not keep a token-registry ADR open for this exact topic after citing PF10 2.1.  
\* A plan may continue implementation planning for provider parity, bridge capability, and non-dev bridge fallback as governed proof obligations without claiming those labels as acceptance tokens.

\#\#\# Epic Plan review posture

Epic Plans are planning records. They are not QA Plans, Live QA runbooks, close reports, implementation patches, or evidence inventories.

Therefore, Epic Plan review should block only when the plan cannot safely preserve:

\* intended scope  
\* PF09 completion mapping  
\* deliverable boundaries  
\* acceptance-token truth  
\* canon hierarchy  
\* phase fidelity  
\* execution separation  
\* portability for downstream planning

Epic Plan review should not block on QA-runbook-level precision, close-pack-level evidence path completeness, or template inventory polish unless the prompt or PF canon explicitly makes that information necessary for current planning truth.

\#\#\# Implementation Plan review posture

Implementation Plans must be more concrete than Epic Plans, but the same materiality rule applies.

A formatting defect is not a blocker unless it creates real Codex or OPS ambiguity.

For CA/audit facts:

\* If the plan says Codex must consult CA or an audit, that is a blocker.  
\* If the plan embeds the needed fact and Codex can proceed without external documents, CA provenance wording is not a blocker.  
\* If an Already Implemented claim relies on CA, the plan should embed enough proof in the plan itself.  
\* Imperfect CA quote-block formatting is not a blocker when the fact is clear, self-contained, and not used to smuggle in requirements.

\#\#\# Correct severity mapping

Use this severity posture:

Blocker:  
The issue changes truth, proof, acceptance, execution, source authority, or portability.

Caveat:  
The issue creates a real risk but has a safe default and does not prevent approval.

Suggestion:  
The issue improves clarity, consistency, or future maintainability.

Nit:  
The issue is cosmetic, template-polish, or wording-level only.

\#\#\# Review burden

A reviewer who wants to block must state the material harm.

Valid blocker framing:

\* “This contradicts active PF10 guidance.”  
\* “This leaves an ADR unresolved after PF10 already resolves it.”  
\* “Codex is told to consult an external audit it will not have.”  
\* “The plan claims an unregistered token as an acceptance token.”  
\* “The plan claims Already Implemented without embedded proof.”

Invalid blocker framing:

\* “This token row is missing from the table, although the evidence family is clear.”  
\* “The Epic QA root is not declared in the Epic Plan, although no QA execution is authorized here.”  
\* “The CA quote format is not exact, although the fact is embedded and self-contained.”  
\* “The provenance label says CA vetted.”  
\* “The section is not template-perfect.”

\#\#\# Targeted drain targets

\* Canon Plan Templates  
  Add materiality-based blocker discipline for Epic Plan and Implementation Plan review. Clarify that template hygiene defects are non-blocking unless they affect truth, proof, acceptance, execution, source authority, or portability.

\* Epic Process Guide  
  Add review-loop severity discipline: REVISE AND RESUBMIT should be reserved for issues that can change execution, acceptance, scope, source authority, evidence trust, or closeout truth.

\* HDE-Governance  
  Clarify acceptance-token review materiality. Missing inventory rows should be corrected, but they are blockers only when they create token overclaim, missing acceptance truth, or unregistered token usage.

\* HDE-Schemas and Artifacts  
  Clarify that high-level evidence family references in Epic Plans are not the same as QA evidence production requirements or close-pack evidence inventories.

\* Glow QA Guide  
  Clarify that Epic Plan QA-root declarations are planning references, not QA execution proof. Missing root declaration in an Epic Plan is non-blocking unless QA execution or evidence production depends on it.

\* Technical Writing Best Practices  
  Add template-polish severity guidance: formatting, quote-block style, table order, and provenance labels should not be escalated to blockers unless they change meaning or execution.

\* HDE Build Checklist — Fermentation  
  Clarify that token-like proof labels in PF09 rows must be distinguished from registered acceptance tokens, and that non-token proof labels may guide evidence without becoming acceptance-token claims.

\#\#\# Drain priority

1\. Canon Plan Templates  
2\. Epic Process Guide  
3\. HDE-Governance  
4\. HDE-Schemas and Artifacts  
5\. Glow QA Guide  
6\. Technical Writing Best Practices  
7\. HDE Build Checklist — Fermentation

\#\#\# Immediate operating rule

Until drained, this PF10 addendum is the live rule:

Do not block HDE-EPIC032 planning artifacts for template hygiene, quote-block format, inventory polish, provenance labels, or Epic QA-root declaration omissions unless the issue materially affects truth, proof, acceptance, execution safety, source authority, or portability.  
