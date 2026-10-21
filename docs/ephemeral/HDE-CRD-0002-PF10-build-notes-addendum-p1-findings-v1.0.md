---
artifact_type: PF10_BUILD_NOTES_ADDENDUM
addendum_id: P1-FINDINGS-ADDRESSED-1
proposed_pf10_number: "2.14 (next continuous number after addendum 2.13, which PF10 v13.6.4 on pull request #668's head carries; the current controlled PF10 on main, v13.6.3, ends at 2.12; allocation and publication are the Product Owner's)"
authority: Nathan / Product Owner's direct instruction in the continuing HDE-CRD-0002 Implementation Agent session, 2026-10-20, quoted in the addendum's "Source and authority". The Product Owner named this agent to create the addendum. No approval prompt produced it, and none is claimed
producing_session: continuing whole-change HDE-CRD-0002 Implementation Agent session, https://claude.ai/code/session_01CCKsYD2yX5WgU3biWKb59j
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.6.3.md on main (blob 41d5cfd2da6d; addendum 2.11 read in full, rules 4 to 8 re-read for this addendum); docs/pfcanon/PF10-HDE-Build-Notes-v13.6.4.md on the head of pull request #668 (version line, addendum index and addendum 2.13 heading read, for numbering only). Provenance, not a gate
canon_searched_on_main: 390bc9960a3e9012f67fe7ea39905b624259c87e. Terms "P1", "declin", "stated limit", "finding disposition", "real input" across docs/pfcanon/ and AGENTS.md. The only rule on declining a P1 is PF10 addendum 2.11 rule 7 ("Declining a P1 or a security finding goes to the Product Owner first."); the real-input rule is addendum 2.11 rules 4 and 5 and AGENTS.md "Code review guidelines". Formatting rules read: Change Process Guide §0.1A; Plan Templates "Canon precedence for template use"
capture_time_utc: 2026-10-20T18:55:00Z
page_ready_text: the H2 section below, from its heading to the end of this file. The "Canon relied on" block above the H2 is record-only and is not page text
incorporated_into: not yet; the Product Owner publishes it into PF10
---

**Canon relied on:**

* PF10-HDE-Build-Notes v13.6.3 (on main), addendum 2.11, read in full: rule 4 (real inputs), rule 5 (constructed inputs), rule 7 (finding disposition, including "Declining a P1 or a security finding goes to the Product Owner first."), rule 8 (repeated finding class), "Scope and supersession". Addendum 2.12 for 2.11's numbering. PF10 v13.6.4 on pull request #668's head, for the next number only.
* PF06-Canon-Change-Process-Guide v2.5.4 §0.1A (one H2 per addendum with the next continuous number; H3 or lower below it; HDE Build Notes records material decisions and temporary pre-drain authority).
* PF27-Canon-Plan-Templates v2.0.5, "Canon precedence for template use" (page-ready, self-contained addendum; no role-addressed handling inside it).
* AGENTS.md "Code review guidelines" (the real-input reporting rule) and "PF10's authority in the canon".
* The case that prompted the rule: pull request #668 (HDE-CRD-0002 WU-PR-07), Codex findings CX7-2 and CX7-3, both P1, which the PR-35 session proposed to decline in whole or in part under rule 7.

## 2.14 A P1 finding is addressed until it is resolved; only a finding that depends on an input the product will never have may be declined

Timestamp: 102026 18:55 (UTC). Details: Records the Product Owner's rule that no P1 review finding is declined, deferred, or accepted as a stated limit while its triggering input is real; the one exception is a finding whose triggering input the product will never have. Origin: the Product Owner's direction of 2026-10-20 in the continuing HDE-CRD-0002 Implementation Agent session, after the WU-PR-07 PR-35 session offered to decline two P1 Codex findings (CX7-2 and CX7-3 on pull request [amthorn78/glow-hdengine-v2\#668](https://github.com/amthorn78/glow-hdengine-v2/pull/668)) as stated limits. Evidence: the PR-35 session's decision request and the two findings, both checked against the code on the pull request's head and against Change Process Guide §3.5.2.1, which requires the behaviour each finding reports missing.

### Source and authority

This addendum records the Product Owner's rule, in the Product Owner's words: "I do NOT want to ignore P1 findings ever. If we have some rule to do that now, it is wrong" and "P1s need to be addressed until the end, unless the violate the rule where they are testing for inputs that will never exist in this app." The Product Owner directed that this be recorded as an HDE Build Notes addendum. Where this addendum conflicts with earlier PF-Canon, an earlier addendum or an in-flight change document, this addendum governs for the scope below.

### Rule

1. **Scope.** A P1 finding is any review finding labelled P1, or any higher priority such as P0, by the Codex code review or by a person, on any pull request of any Epic or CRD.
2. **Addressed until resolved.** A P1 finding whose triggering input is real is fixed. It is not declined, deferred to a later change, recorded as a stated limit, or resolved on cost, effort, design preference, a plan's earlier choice, an ADR's stated limit, or a "not worth its code" judgement.
   * Fixed means the wrong result, crash or guarantee breach the finding reports no longer occurs on that real input. A test shows it, and the test fails without the fix.
   * A typed refusal of the input is a fix when refusing it is correct behaviour for the product.
   * The thread stays open until the fix is pushed and the finding's own check of it is answered. A pull request with an open P1 thread on a real input is not merge-ready.
3. **The one exception.** A P1 finding may be declined only when its triggering input is not real under addendum 2.11 rule 4: it does not exist on main or in an approved unit's planned deliverable, does not occur in the product's real operating environment, and cannot be supplied by a user, vendor or attacker through an interface the product exposes. The input is then one constructed only to exercise the code (addendum 2.11 rule 5).
   * The reply on the thread gives the traced path and shows why the input can never occur in the product.
   * As before, declining a P1 goes to the Product Owner first, and the thread is resolved only after that.
4. **Repeated finding class.** Addendum 2.11 rule 8 still applies: two consecutive rounds raising findings of the same class stop the fixing of instances, and the session asks the Product Owner one design question. For a P1 on a real input, "accept a stated limit" is not an option. The answer is a fix or a narrowed design that removes the wrong result, including a typed refusal, or a rescope through the native route. In every case the P1 on its real input is resolved before the pull request merges.
5. **Budget.** A P1 fix that would pass a unit's cost ceiling (addendum 2.11 rules 1 and 3) still returns to the Product Owner for budget direction before work continues. That return is about the budget. It does not make declining the P1 an option.
6. **Unchanged.**
   * Findings below P1 keep addendum 2.11 rule 7 as written.
   * Security findings below P1 keep rule 7's Product Owner-first rule for a decline.
   * The real-input reporting rule for reviewers (AGENTS.md "Code review guidelines") is unchanged.
   * Nothing here weakens the existing duty to fix a real defect at any priority.

### Scope and supersession

* **Applies from this addendum** to every open and future pull request of every Epic and CRD, including in-flight HDE-CRD-0002 units. That includes pull request #668 (WU-PR-07), whose P1 findings CX7-2 and CX7-3 rest on real inputs: a close candidate source whose tracked issues carry an ADR status, and one that omits an acceptance row for a requirement in the bound Specification. Both are therefore fixed.
* **Supersedes** addendum 2.11 rule 7 only where it allows declining a P1 on a real input: its sentence "Otherwise the reply on the thread gives the traced path and the stated limit, and the thread is resolved", as applied to a P1, and its sentence "Declining a P1 or a security finding goes to the Product Owner first", as it would let a P1 on a real input be declined.
* **Supersedes** addendum 2.11 rule 8's option "accept a stated limit" for a P1 on a real input.
* **Supersedes** any plan, instruction, ADR stated limit or Product Owner disposition recorded before this addendum, to the extent it would leave a P1 on a real input unfixed.
* **Does not change** addendum 2.11 rules 1 to 6, the real-input definition, or rule 7 for findings below P1.
* **Does not reopen** accepted-final work. Earlier declines remain historical facts, for example WU-PR-06's three declined findings, which were P2.

### Epic, task, and status effects

* No epic, CRD, task, PF09 or PF30 row changes status by this addendum.
* WU-PR-07 (pull request #668): CX7-2 and CX7-3 are fixed in the PR-35 session, as the Product Owner directed on 2026-10-20. The ADR's stated limit "Requirement coverage is the source author's" is removed.

### Required canon drainage

Drainage is unperformed.

| Target | Required change |
| :---- | :---- |
| PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1, step 3 | State that a P1 on a real input is fixed and never declined, and that only a P1 on a non-real input may be declined, with the Product Owner first (owner GCFPE-MGMT-10 and the Product Owner) |
| PR-40 — Review PR Work-Unit Lineage — 100926.1 | Check that no P1 on a real input was declined before merge |
| Plan Templates "Source-bound review authority and exact-fix limits" and Change Process Guide §1.1.4 | Carry rules 2 and 3 beside addendum 2.11's rules 7 and 8 |
| AGENTS.md "Code review guidelines" | Optional: note that a P1 the reviewer reports on a real input is fixed by the PR session. Editing AGENTS.md needs the Product Owner's explicit instruction |

### Deferred obligations and unresolved work

* The prompt and canon drainage above: the Product Owner and GCFPE-MGMT-10.
* Publication of this addendum into PF10, after addendum 2.13: the Product Owner.

### Scope boundaries and nonclaims

* This addendum changes no prompt, skill, AGENTS.md or permanent PF document; the drainage above is unperformed.
* It establishes no QA, acceptance, merge or closure, and it does not decide any finding's priority. The priority is the label the reviewer gives.

### Evidence anchors

* The Product Owner's words, quoted under "Source and authority".
* PF10 addendum 2.11 rules 4, 5, 7 and 8 (on main, v13.6.3).
* Pull request #668: Codex findings CX7-2 (tracked-issue ADR statuses not checked against the drain-targets ledger) and CX7-3 (`SATISFIED` without an acceptance row for every requirement). On its head `a6c6655`, `tools/qa/generate_epic_close_pack.py` checks only deferrals against the drain-targets ledger. Change Process Guide §3.5.2.1 requires a TI item's ADR status line to record "Deferred with drain targets", and the acceptance section to bind "each current governing requirement or acceptance criterion".

### Relationship to existing HDE Build Notes guidance

The addendum narrows addendum 2.11 rules 7 and 8 for P1 findings, as stated under "Scope and supersession", and is otherwise consistent with addenda 2.3, 2.11, 2.12 and 2.13. It keeps 2.11's real-input definition as the only ground for declining a P1.
