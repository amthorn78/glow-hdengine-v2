---
artifact_type: PF10_BUILD_NOTES_ADDENDUM
addendum_id: CODEX-SECURITY-REVIEW-DEPRECATION-1
proposed_pf10_number: "2.3 (next continuous number after addendum 2.2 of the current controlled PF10)"
authority: Nathan / Product Owner's direct instruction in the HDE-CRD-0002 WU-PR-01 PR-35 session, 2026-10-13, quoted in the addendum's "Source and authority". The Product Owner named this agent to create the addendum. No approval prompt produced it, and none is claimed
producing_session: dedicated HDE-CRD-0002 WU-PR-01 PR-35 session, https://claude.ai/code/session_013LyxHxzJP2ohvmmNFamZt2 (prompt PR-35 — Resolve PR Reviews and Reach Merge Readiness — 100926.1)
pf10_read: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.3.md (v13.5.3; blob a51bf40a4bcd2cc95653fb5c3e327bf61162aa52; read in full at creation; one unlettered document; addenda 2.1 and 2.2; provenance, not a gate)
canon_searched_on_main: e3a5ed4b9820964c581825f1cc9537fec133988d. Terms "security review", "code/security", "security/review", "codex" across docs/pfcanon/. Formatting rules read: Change Process Guide §0.1A; Plan Templates "Canon precedence for template use"; Technical Writing Best Practices "Output"
capture_time_utc: 2026-10-13T02:55:00Z
page_ready_text: the H2 section below, from its heading to the end of this file. The "Canon relied on" block above the H2 is record-only and is not page text
incorporated_into: docs/pfcanon/PF10-HDE-Build-Notes-v13.5.4.md, addendum 2.3. The Product Owner supplied that PF10 version, and it is committed unchanged on this branch in 9954b11. The PF10 file is the canonical text. Its 2.3 section matches the page-ready text below once Markdown formatting is normalized (links, escapes, emphasis, code marks, table rules). Until #627 merges, PF10 v13.5.3 on main remains the governing version
---

**Canon relied on:**

* PF10-HDE-Build-Notes v13.5.3, read in full: its opening rules and addenda 2.1 and 2.2 (numbering and form of the next addendum).
* PF06-Canon-Change-Process-Guide v2.5.4 §0.1A (one H2 per addendum with the next continuous number; H3 or lower below it).
* PF27-Canon-Plan-Templates v2.0.5, "Canon precedence for template use".
* PF03-Reference-Technical-Writing-Best-Practices v1.8.8, "Output".
* PF04-Canon-HDE-Governance v2.8.7 §9.1.1 "Change authority and exact-artifact lineage" (the PR implementation row, "Normal substantive code/security/review and evidence chain").
* PF20-Reference-HDE-Phased-Epics v1.9.6 §2.26.7 "Tracked Issues, Variances and Remaining Owners" (the RA-09 security-coverage row).
* PF23-Canon-Reality-Audits v1.2.2 §12 "Drift and Reality vs Expectations" (the RA-09 row only, found by the search).
* In-flight HDE-CRD-0002 documents: Implementation Plan v1.1 §7 "Ordered work units" (the common reviewer chain and WU-PR-05); WU-PR-01 PR instruction v1.0 §12; WU-PR-01 detailed PR plan v1.1 §19; Specification v1.1-approved, requirement S19 and routed decision RD-1.
* AGENTS.md (canon-first rule; PF canon is read-only; PF10's authority).

## 2.3 Codex security review is deprecated: it is no longer a step of the HDE pull-request review chain

Timestamp: 101326 02:55 (UTC). Details: records the Product Owner's deprecation of the automated Codex security review, which is no longer available. Origin: the HDE-CRD-0002 WU-PR-01 PR-35 session for pull request amthorn78/glow-hdengine-v2#627. Evidence: the Codex review summary of #627 and the precedent of #501 (below).

### Source and authority

This addendum records the Product Owner's directions of 2026-10-13, given in the HDE-CRD-0002 WU-PR-01 PR-35 session:

* "This feature (security review) is no longer available. We will need to deprecate it. You may create a PF10 build notes addendum to specify its deprecation."
* Before that direction, the Product Owner's decision for #627 was "Waive it for #627", given in answer to the question of how PR-35 should treat the security review that the HDE-CRD-0002 Implementation Plan names in its reviewer chain and that never ran on #627.

Where this addendum conflicts with earlier PF-Canon or with an in-flight change document, this addendum governs for the scope below.

### Rule

1. **Scope.** The automated Codex security review of a pull request: the "Security Review" row of the Codex review summary, produced when a pull request opens or requested by an `@codex security review` comment. It is covered wherever HDE canon, an in-flight change document, a GCFPE prompt or a skill names it as part of a pull request's review chain.
2. **Deprecation.** The Codex security review is not part of the HDE pull-request review chain. It is not obtained or waited on, and its absence is not treated as a review gap, finding, blocker or waiver need, by any of: a pull request, a work unit, a merge-readiness decision, a lineage review, a QA readiness decision or a closure decision. A `MERGE_PENDING` result does not depend on it.
3. **Unchanged.** The Codex code review remains part of the pull-request review chain and is read and resolved as before. Every other security obligation is unchanged, including:
   * security constraints in permanent canon;
   * security constraints in approved Specifications and Implementation Plans;
   * security constraints in the repository's agent instructions;
   * security deliverables of a work unit, such as the recorded code security review that HDE-CRD-0002 requirement S19 assigns to WU-PR-05, a recorded review that adds no review tooling.
4. **No substitute.** This addendum creates no replacement review tool, review step, approval or gate.
5. **Historical records.** Records of security reviews that ran or were missed on earlier pull requests keep their wording and remain historical statements, for example the HDE Phased Epics §2.26.7 RA-09 security-coverage limitation and the Reality Audits finding RA-09.

### Passages read under this rule

These passages are not rewritten. From the turn this addendum is created, each is read without the Codex security review:

| Location | Passage | Reading under this addendum |
| :- | :- | :- |
| HDE-CRD-0002 Implementation Plan v1.1, §7 "Ordered work units", common to every PR unit (`docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md`) | "reviewer chain = Codex code review and security review on the PR" | reviewer chain = Codex code review on the PR, PR-35 for review resolution, PR-40 lineage review |
| HDE-CRD-0002 WU-PR-01 PR instruction v1.0, §12 (`docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-instruction-v1.0.md`) | PR-35 "retrieves and resolves review findings (Codex code review and security review on the PR)" | PR-35 retrieves and resolves the Codex code review findings |
| HDE-CRD-0002 WU-PR-01 detailed PR plan v1.1, §19 (`docs/ephemeral/HDE-CRD-0002-WU-PR-01-pr-implementation-plan-v1.1.md`) | "(Codex code review and security review)" | the Codex code review |
| Later HDE-CRD-0002 PR instructions and detailed plans issued under Implementation Plan v1.1 | the same reviewer chain | the same reading |
| HDE-CRD-0002 Specification v1.1, routed decision RD-1 (`docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`) | the residual of item 6(a), "security-review coverage of pushes after the first", routed to GCFPE-MGMT-10 and the Product Owner | the residual concerned the deprecated review, and no coverage of that review remains to be provided |
| GCFPE prompts that direct reading a pull request's security reviews (PR-35 — Resolve PR Reviews and Reach Merge Readiness) and the PR development skill that names "Codex code and security reviews" | reading "applicable" security reviews | no Codex security review is applicable |

Permanent PF canon names no Codex security review. The HDE Governance §9.1.1 authority table entry for PR implementation, "Normal substantive code/security/review and evidence chain", is not reworded by this addendum.

### Evidence

* On #627 the Codex review summary showed only a "Code Review" row through six heads, from 2026-10-13T00:55Z to 02:47Z. No "Security Review" row appeared.
* One `@codex security review` comment on #627 (comment 6135990857, 01:19:59Z) was answered by a Code Review run with trigger "Manual request", and still no "Security Review" row appeared.
* On #501 the "Security Review" row came only from "PR opened", and a later `@codex security review` comment was answered by a code-review comment.

### Status, effects and nonclaims

* No epic, CRD, task, PF09 or PF30 row changes status by this addendum.
* The wording changes to GCFPE prompts and skills that implement this addendum are unperformed.
* This addendum does not change the Codex code review or any security requirement of canon or of a change. It does not waive a security finding, and it establishes no QA, acceptance, merge or closure.
* For #627, the Product Owner's earlier waiver and this deprecation agree: #627 has no Codex security review to obtain.

### Unresolved obligations and owners

* Whether the HDE pull-request review chain needs another source of security review is not decided by this addendum. That includes the wording of HDE Governance §9.1.1's chain entry. Owner: the Product Owner.
* The wording of the GCFPE prompts and skills that name the Codex security review. Owner: GCFPE-MGMT-10 and the Product Owner.
