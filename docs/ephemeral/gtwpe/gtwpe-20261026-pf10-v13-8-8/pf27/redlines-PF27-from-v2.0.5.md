# T-PF27 — exact redlines from PF27 v2.0.5

Run: `gtwpe-20261026-pf10-v13-8-8/T-PF27`. Preparation revision: `P1`.
Originating preparer: TW-DRAIN-10 in the Nathan-started T-PF27 document session, Claude Code cloud session https://claude.ai/code/session_01QRazLg2AQgDCgvdFbDJG1C.
Target: `docs/pfcanon/PF27-Canon-Plan-Templates-v2.0.5.md` (`PF27-Canon-Plan-Templates` v2.0.5) at `origin/main` `9dda63dd3f05f496c3ff67e95da78550d3950c5a`, byte-identical at `0838ba08254eaefc888019df49a06aa2ae99cc6c`; Git blob `96becf4158c0a7b294c38d1eb503e2c280de2cd9`; 312,281 bytes; 3,859 lines; LF line endings; ends with one LF after an empty last line; raw UTF-8 SHA-256 `1542ba9e4752a1ad3f6985dfd7e84961d0fc5fc46b3dcbaacc529bbddfc3c7f8`.
Ledger: `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md`, commit `13b64dddea4cfe0bb35e56c1833fbcd03af238c7` (blob `74944b261c0e`, unchanged on `main`), task `T-PF27`, rows S-CR1, S-CR2, A11 with A18, A11 and A14, A31, A30, X07.
Sources: PF10 v13.8.8 (`docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md`, blob `680b0accb0bdf260b0489d1a7385f90bb120cd99`, SHA-256 `f5e13efb5ab1354bda2f578ca69f41bed773160784602a896927bc091a254c2f`): front matter 1–223; addenda 2.11 (1205–1318), 2.14 (1549–1619), 2.18 (1956–2081), 2.30 (3259–3360), 2.31 (3361–3470). HDE-CRD-0002 Specification v1.1 (approved), `docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md`, blob `c4802a5a7fa3`: CR-1 (199–208), CR-2 (210–219); overlaid by delta 01, `docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md`, blob `9408d6ed091b`, which leaves CR-1 and CR-2 unchanged. Supporting cross-reference X07: `docs/ephemeral/HDE-CRD-0002-QA70-qa-plan-review-v1.0.md` §5, "CR-11 — decided" (256–274), blob `b083486fc768`.
Prompt: TW-DRAIN-10 100926.1, https://app.notion.com/p/3f44590a05eb8172a314fe6b958bb9ff.
Preparation outcome: `READY` after whole-batch producer validation. Save completeness is recorded in the separate proof log.

These are twelve independent original-bound operations, all `REPLACE`. Each insertion is expressed as a `REPLACE` whose NEW block reproduces its OLD anchor unchanged and adds the new text; no anchor text is altered. Header control fields are reserved for TW-APPLY-10. Payloads are literal: the single LF immediately before a closing fence is presentation only and is not part of the payload. Every other payload newline and every trailing space is exact. Fences are four backticks, longer than any backtick run in a payload. Each OLD block consists of complete original lines and occurs exactly once in the whole original. The original line numbers are context only, not locators.

## RL-001

Redline number: RL-001
Findings or source items: A31 (PF10 v13.8.8 addendum 2.31, "Required canon drainage", third bullet), consequential to RL-012
Change type: CONSISTENCY
Operation: `REPLACE`
Target document: `PF27-Canon-Plan-Templates`
Section path: `# **0\) Document Control**` > `## **Purpose & scope \[Required−Now\]**` > `### **Governed artifacts**`
Original-bound location: the `Epic Remediation Plan` entry of the governed-artifact list
Original line (context only): 35
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: The list states which artifact types PF27 governs, in section order. RL-012 adds the close-mutation-set task template as §3B, after §3A Epic Remediation Plan, so its artifact type joins the list in that position. The OLD line is reproduced unchanged.

OLD

````text
* Epic Remediation Plan  
````

NEW

````text
* Epic Remediation Plan  
* Close Mutation Set Task Record  
````

## RL-002

Redline number: RL-002
Findings or source items: X07 (HDE-CRD-0002 QA-70 review v1.0 §5, "CR-11 — decided": decision `APPROVED_AS_CHANGED`, alternative (a); drainage target "Plan Templates Step-0B (CRD applicability)"); PF10 v13.8.8 addendum 2.35 lists CR-11 among the canon drainage items (supporting reading)
Change type: CLARIFY
Operation: `REPLACE`
Target document: `PF27-Canon-Plan-Templates`
Section path: `# **A) Glow Plan and Runbook Templates**` > `## **1\) Live QA Plan**` > `### **Mandatory Step‑0 artifacts**` > `#### **Step-0B — Doc Delta Capture (mechanical; runbook self-honesty)**`
Original-bound location: the epic-level canonical-output bullet, its following blank line and the `Requirements:` label
Original lines (context only): 666–668
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: CR-11 finds that for a CRD the Step-0B `00_meta` capture cannot be indexed by the governed writer and that its draft surface is a close-stage input another owner authors. It decides alternative (a): Step-0B lives in the performing check's indexed primary and is reported in the final QA reporting; alternative (b), an unindexed `00_meta/doc_deltas.md`, is rejected because HDE Mechanics Guide §1.6.3 excludes present-but-unindexed evidence. The change applies Step-0B's own rules in full, records whether either doc-delta surface exists before "no deltas", and preserves proof-bearing content. The CRD applicability block is inserted before the unchanged `Requirements:` list it refers to; the bullet and label are reproduced unchanged.

OLD

````text
* `audit/qa/<epic-id>/00_meta/doc_deltas.md`

Requirements:
````

NEW

````text
* `audit/qa/<epic-id>/00_meta/doc_deltas.md`

CRD applicability (required when the change is a CRD):

* For a CRD, the canonical CRD publication route does not index a capture at the epic-level `00_meta/doc_deltas.md` surface above, and present-but-unindexed output does not become governed evidence (HDE Mechanics Guide §1.6.3). The CRD's draft/staging doc-delta surface is a close-stage input that the close mutation set authors.  
* Step-0B therefore records its capture in the governed, indexed `primary.log` of the check that performs it, published through the canonical CRD writer, and the QA RCA & Doc Delta summary reports it. Step-0B does not create an unindexed `00_meta/doc_deltas.md` for a CRD.  
* The capture applies every requirement below: stable IDs, BLOCKERS and CAVEATS separated, generation by commands, plan-vs-execution drift recorded, and “no deltas” only when empty. Before it emits “no deltas,” it records whether either doc-delta surface exists, and it preserves, and never overwrites, any proof-bearing content it finds.

Requirements:
````

## RL-003

Redline number: RL-003
Findings or source items: A11 (addendum 2.11 rules 4, 5, 7 and 8; "Required canon drainage", third row); A14 (addendum 2.14 rules 1 to 4 and 6; "Required canon drainage", third row); A18 (addendum 2.18 rules 1, 2 and 6, which withdraw the ceiling and 2.14 rule 5)
Change type: NEW_CANON
Operation: `REPLACE`
Target document: `PF27-Canon-Plan-Templates`
Section path: `# **A) Glow Plan and Runbook Templates**` > `## **Review guardrails**` > `### **Source-bound review authority and exact-fix limits**`
Original-bound location: the section's last paragraph, beginning "Every execution-critical identifier in required fix text"
Original line (context only): 1014
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: 2.11's drainage row names this section for its finding-disposition rule and its repeated-finding-class trigger. Its own cross-references are misnumbered (2.12, LR6-O2); read by the text they describe, the "rule 5 disposition" is rule 7 (finding disposition), the "rule 6 trigger" is rule 8 (repeated finding class), and rule 7's "(rule 3)" is rule 4 (real inputs). 2.14's drainage row names this section for its rules 2 and 3 beside 2.11's rules 7 and 8. Surviving text only: 2.14 narrows 2.11 rules 7 and 8 for P1 findings, so rule 7's decline route and rule 8's "accept a stated limit" survive only below P1; 2.18 withdraws 2.14 rule 5 (budget) and every ceiling, so no ceiling or budget return is drafted. The real-input definition (2.11 rule 4) and the constructed-input sentence (rule 5) are included because the disposition rule depends on them. The trigger is kept separate from the Live QA churn rule and the CI-budget rules, as 2.11 "Scope and supersession" states. The tool is described by function ("an automated code review") under Technical Writing Best Practices §2. The OLD paragraph is reproduced unchanged.

OLD

````text
Every execution-critical identifier in required fix text MUST map to an allowed source. Reviewer-created design is not an authority basis. A finding containing reviewer-invented technical design is invalid, as is any dependent required fix, ADR or Tracked Issue disposition, approval recommendation, or final decision. If the defect is systemic or affects the final posture, discard the review and rerun it from the unchanged inputs; do not repair unsupported text through post hoc justification.
````

NEW

````text
Every execution-critical identifier in required fix text MUST map to an allowed source. Reviewer-created design is not an authority basis. A finding containing reviewer-invented technical design is invalid, as is any dependent required fix, ADR or Tracked Issue disposition, approval recommendation, or final decision. If the defect is systemic or affects the final posture, discard the review and rerun it from the unchanged inputs; do not repair unsupported text through post hoc justification.

**Finding disposition on real inputs (every Epic and CRD pull request).** A review finding, from an automated code review or from a person, is fixed when it shows a wrong result, a crash, or a guarantee breach on a real input. An input is real when it exists on `main` or in an approved unit's planned deliverable; occurs in the product's real operating environment, such as the deployed services, the hosted CI runner, the operator's shell, or the vendor's responses; or can be supplied by a user, a vendor, or an attacker through an interface the product exposes. An input constructed only to exercise code justifies no fix or blocking finding.

* A finding below P1 that shows no wrong result, crash, or guarantee breach on a real input receives a thread reply that gives the traced path and the stated limit, and the thread is resolved. Declining a security finding below P1 goes to the Product Owner first.  
* The standing default is to fix only a wrong result on a real input, or a breach of the read-only or no-secrets guarantees. A snapshot-precision finding is a hypothetical-input finding unless it shows a write that the tool itself, or code it runs in the checkout, can make.  
* A blanket instruction to fix every finding on a pull request is read under this rule.

**P1 findings.** A P1 finding is any review finding labeled P1, or any higher priority such as P0, by an automated code review or by a person, on any pull request of any Epic or CRD. The priority is the label the reviewer gives.

* A P1 finding whose triggering input is real is fixed. It is not declined, deferred to a later change, recorded as a stated limit, or resolved on cost, effort, design preference, a plan's earlier choice, an ADR's stated limit, or a “not worth its code” judgement.  
* Fixed means the wrong result, crash, or guarantee breach that the finding reports no longer occurs on that real input. A test shows it, and the test fails without the fix. A typed refusal of the input is a fix when refusing it is correct behavior for the product.  
* The thread stays open until the fix is pushed and the finding's own check of it is answered. A pull request with an open P1 thread on a real input is not merge-ready.  
* A P1 finding may be declined only when its triggering input is not real. The thread reply gives the traced path and shows why the input can never occur in the product. Declining a P1 goes to the Product Owner first, and the thread is resolved only after that.

**Repeated finding class (pull-request review).** When two consecutive review rounds on one pull request raise findings of the same class (the same component or contract), the session stops fixing instances and asks the Product Owner one design question: narrow the design, accept a stated limit, or rescope. For a P1 on a real input, accepting a stated limit is not an option: the answer is a fix, a narrowed design that removes the wrong result, including a typed refusal, or a rescope through the native route, and that P1 is resolved before the pull request merges. This is a design trigger by finding class. It is not a push count, a pause threshold, or a CI-budget control. It does not replace the Live QA iteration-churn escalation that **QA planning QoS guardrails \- templates, deferred steps, and prompt-family separation** governs, and it does not change **CI lane classification and automated budget-control discipline**.

These rules do not weaken the duty to fix a real defect at any priority.
````

## RL-004

Redline number: RL-004
Findings or source items: A30 (addendum 2.30, "Required canon drainage", second bullet: RCA D-1, finding O-11; lesson L-3)
Change type: NEW_CANON
Operation: `REPLACE`
Target document: `PF27-Canon-Plan-Templates`
Section path: `# **A) Glow Plan and Runbook Templates**` > `## **Review guardrails**` > `### **Hard blockers for plan approval/execution**`
Original-bound location: the section's first bullet, beginning "Live QA Plans and runbooks MUST NOT require equality to a preplanned Git commit"
Original line (context only): 1018
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: D-1 proposes for Plan Templates that "a code-identity guard that excludes storage paths uses the repository's whole set of CI-exempt storage prefixes, as its change classifier defines them, rather than a hand-written subset". Its cause (O-11): the approved QA Plan's state-(b) guards excluded two of the eight CI-exempt prefixes, so a change under a third made check 21's first run `TOOLING_BLOCKED`. The first bullet already requires "validation of the required current code posture"; the new bullet, placed directly after it, states how such a guard excludes storage paths. The HDE locus was verified read-only on `main` `0838ba08254e`: `_DOCUMENTATION_PREFIXES` in `ci/checks/classify_ci_changes.py` (lines 171–180, eight prefixes; file last changed by `2ff696b`). The list itself is not copied. The OLD bullet is reproduced unchanged.

OLD

````text
* Live QA Plans and runbooks MUST NOT require equality to a preplanned Git commit as a readiness, behavior, routing, or PASS predicate. Source identity is execution provenance. The plan MUST require capture of actual execution-source identity in governed evidence, validation of the required current code posture, and preservation of routing provenance. This rule does not waive clean-source checks, authorization-bound source identity, routed-artifact provenance, OPS source binding, or exact-source release-attestation verification.  
````

NEW

````text
* Live QA Plans and runbooks MUST NOT require equality to a preplanned Git commit as a readiness, behavior, routing, or PASS predicate. Source identity is execution provenance. The plan MUST require capture of actual execution-source identity in governed evidence, validation of the required current code posture, and preservation of routing provenance. This rule does not waive clean-source checks, authorization-bound source identity, routed-artifact provenance, OPS source binding, or exact-source release-attestation verification.  
* Code-identity guard exclusions (required). A code-identity guard that excludes storage paths, such as a readiness check that compares code between two repository states, MUST exclude the repository's whole set of CI-exempt storage prefixes, as the repository's change classifier defines them, not a hand-written subset. A subset reports a change under an omitted prefix as a code change. For HDE, the set is `_DOCUMENTATION_PREFIXES` in `ci/checks/classify_ci_changes.py`.  
````

## RL-005

Redline number: RL-005
Findings or source items: A11 (addendum 2.11 rules 1 and 2; "Required canon drainage", first row); A18 (addendum 2.18 rules 1 and 4; "Required canon drainage")
Change type: CANON_UPDATE
Operation: `REPLACE`
Target document: `PF27-Canon-Plan-Templates`
Section path: `# **A) Glow Plan and Runbook Templates**` > `## **2\) HDE-EPIC-Specification**` > `### **Epic Record Template (Normative)**` > `#### **Business Case (MUST)**`
Original-bound location: the last bullet of "Minimum required contents", **Separation from technical scope**
Original line (context only): 1398
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: 2.11's drainage row requires Plan Templates "Business Case (MUST)" to state that the Business Case applies to every requirement and work unit of Epics and CRDs (rules 1 and 2). 2.18 withdraws rule 1's cost-ceiling field, so the business case is beneficiary, evidence, benefit and measure, and rule 4 restates rule 2's internal-tooling test against expected cost. The epic-level Business Case and its review posture are unchanged; the new block follows the existing list and precedes the unchanged "Review posture:". The OLD bullet is reproduced unchanged.

OLD

````text
* **Separation from technical scope:** this section MUST NOT be replaced by purely technical task lists; technical scope is covered elsewhere in the Epic Specification.
````

NEW

````text
* **Separation from technical scope:** this section MUST NOT be replaced by purely technical task lists; technical scope is covered elsewhere in the Epic Specification.

**Requirement and work-unit business case (MUST; Epics and CRDs).** Beyond the epic-level Business Case above, every Specification requirement, of an Epic or a CRD, and every work unit states its own business case:

* **Beneficiary:** who gains: Glow users, the production operator, or the delivery team.  
* **Evidence:** the observed incidents or measurements that show the problem, cited. A forecast is not evidence.  
* **Benefit:** what changes for the beneficiary, in user outcome, risk, time, or money.  
* **Measure:** how the benefit is checked after delivery.

A business case states no cost ceiling: no budget in sessions, elapsed days, review rounds, or pushes. More complete or more faithful evidence, CI, tooling, or records for their own sake, conformance to canon, and “could prevent” without an observed incident are not a business case. Internal tooling qualifies only when its expected saving, from observed incident data, exceeds its expected cost.
````

## RL-006

Redline number: RL-006
Findings or source items: S-CR1 (Specification CR-1: Plan Templates §2A "PF30 accountability"; drainage "the Plan Templates owner aligns §2A")
Change type: CONSISTENCY
Operation: `REPLACE`
Target document: `PF27-Canon-Plan-Templates`
Section path: `# **A) Glow Plan and Runbook Templates**` > `## **2A) HDE-CRD-Specification Profile and PF30 Record Contract**` > `### **Applicability and process routing**`
Original-bound location: the second paragraph, beginning "The Change Process Guide governs the shared lifecycle."
Original line (context only): 1872
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: CR-1 (`APPROVED_AS_CHANGED`) finds §2A's "PF30 accountability" in conflict with HDE Governance §9.1.1, which makes HDE CRD Records a historical and reference home, "not an active work register", whose entries "the active workflow MUST NOT create, update or synchronize", and follows §9.1.1 (HDE Governance §9.1.2). Glow QA Guide "Change-lane QA applicability" states the CRD's actual accountability: "CRD work retains its assigned CRD ID, approved Specification, Implementation Plan and decision lineage; PF30 registration or an invented PF09 mapping is not a prerequisite." "Controlling work register" no longer describes the CRD lane and becomes "accountability". The Epic lane, the lifecycle sentence and the rigor statement are unchanged.

OLD

````text
The Change Process Guide governs the shared lifecycle. The CRD uses CRD identity and PF30 accountability where an epic uses Epic identity and PF09 accountability. The change lanes differ by origin, identity, and controlling work register, not by implementation, QA, evidence, review, or closure rigor.
````

NEW

````text
The Change Process Guide governs the shared lifecycle. A CRD uses CRD identity and is accountable through its approved Specification, Implementation Plan, and decision lineage, where an epic uses Epic identity and PF09 accountability. HDE CRD Records is a historical and reference home, not an active work register: the active workflow does not create, update, or synchronize PF30 entries, and PF30 registration is not a prerequisite (HDE Governance §9.1.1; Glow QA Guide, “Change-lane QA applicability”). The change lanes differ by origin, identity, and accountability, not by implementation, QA, evidence, review, or closure rigor.
````

## RL-007

Redline number: RL-007
Findings or source items: S-CR2 (Specification CR-2: Plan Templates §2A intake prompt "Planned PR and Ops units"; drainage "the Plan Templates owner removes or rewords both passages")
Change type: DELETION
Operation: `REPLACE`
Target document: `PF27-Canon-Plan-Templates`
Section path: `# **A) Glow Plan and Runbook Templates**` > `## **2A) HDE-CRD-Specification Profile and PF30 Record Contract**` > `### **CRD intake and Lead Developer analysis**`
Original-bound location: the intake prompts **Planned PR and Ops units** and **Alchemical phase block or blocks**
Original lines (context only): 1891–1892
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: CR-2 (`APPROVED_AS_CHANGED`) finds that the prompt asks for planned units a Specification must not prescribe (HDE Governance §9.1.1: Specification content "MUST NOT prescribe atomic implementation tasks, file edits, commands, planned PR/Ops work units"; "The change-wide Implementation Plan identifies planned PR work units and any Ops tasks"). The prompt is removed rather than reworded, because its only correct answer would be a fixed value; RL-008 states the rule after the list. Expressed as a `REPLACE` of two whole lines so that the removed line's own newline goes with it; the next prompt is reproduced unchanged.

OLD

````text
* **Planned PR and Ops units:**  
* **Alchemical phase block or blocks:**  
````

NEW

````text
* **Alchemical phase block or blocks:**  
````

## RL-008

Redline number: RL-008
Findings or source items: S-CR1 (CR-1: §2A "a concise initial record in the active PF30 volume"); S-CR2 (CR-2: the planned-unit rule stated once after the intake prompts)
Change type: CONSISTENCY
Operation: `REPLACE`
Target document: `PF27-Canon-Plan-Templates`
Section path: `# **A) Glow Plan and Runbook Templates**` > `## **2A) HDE-CRD-Specification Profile and PF30 Record Contract**` > `### **CRD intake and Lead Developer analysis**`
Original-bound location: the paragraph after the intake prompts, beginning "The intake does not authorize implementation."
Original line (context only): 1898
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: CR-1 names "a concise initial record in the active PF30 volume" as conflicting with HDE Governance §9.1.1, under which no PF30 entry is created and none is required at kickoff, Specification approval, Implementation Plan approval, implementation, acceptance or closure ("Historical drainage"). The implementation precondition keeps the stable CRD ID and routes the approvals to HDE Governance §9.1.1 without restating them. The second added sentence carries CR-2's rule, consistent with HDE CRD Records §4.1 ("The Specification does not prescribe PR or Ops units").

OLD

````text
The intake does not authorize implementation. Implementation may begin only after the CRD has a stable CRD ID, a concise initial record in the active PF30 volume, and the approval required by current governance.
````

NEW

````text
The intake does not authorize implementation. Implementation may begin only after the CRD has a stable CRD ID and the approvals required by current governance (HDE Governance §9.1.1); no PF30 entry is created or required. The intake and the CRD Specification do not prescribe planned PR or Ops units; the change-wide Implementation Plan identifies them.
````

## RL-009

Redline number: RL-009
Findings or source items: S-CR2 (CR-2: §2A "Alchemical phase separation", "For every phase block, identify its purpose, included PR and Ops units …")
Change type: CONSISTENCY
Operation: `REPLACE`
Target document: `PF27-Canon-Plan-Templates`
Section path: `# **A) Glow Plan and Runbook Templates**` > `## **2A) HDE-CRD-Specification Profile and PF30 Record Contract**` > `### **Alchemical phase separation**`
Original-bound location: the second paragraph, beginning "For every phase block, identify its purpose"
Original line (context only): 1904
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: CR-2 names this sentence as asking for planned units a Specification must not prescribe (HDE Governance §9.1.1). "Included PR and Ops units" is removed from the phase-block fields, and the allocation is routed to the change-wide Implementation Plan, as HDE CRD Records §4.3 records it ("its PR and Ops work units, as identified by the approved change-wide Implementation Plan"; each PR or Ops task belongs to exactly one phase). The section's first paragraph and the completion sentence are unchanged.

OLD

````text
For every phase block, identify its purpose, included PR and Ops units, dependencies, entry condition, completion boundary, and downstream handoff. Completion of one phase block does not establish completion of the CRD.
````

NEW

````text
For every phase block, identify its purpose, dependencies, entry condition, completion boundary, and downstream handoff. The CRD Specification does not prescribe the block's PR or Ops units; the change-wide Implementation Plan identifies them and allocates each to exactly one phase block. Completion of one phase block does not establish completion of the CRD.
````

## RL-010

Redline number: RL-010
Findings or source items: S-CR1 (CR-1: §2A "route CRD results and closure posture to the existing PF30 CRD record"; Change Process Guide §1.0.4 "PF30 work mapping", whose §2A counterpart is the substitution bullet)
Change type: CONSISTENCY
Operation: `REPLACE`
Target document: `PF27-Canon-Plan-Templates`
Section path: `# **A) Glow Plan and Runbook Templates**` > `## **2A) HDE-CRD-Specification Profile and PF30 Record Contract**` > `### **Existing-template reuse and substitution**`
Original-bound location: the second, third and fourth bullets of "For CRD use"
Original lines (context only): 1913–1915
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: CR-1 names "route CRD results and closure posture to the existing PF30 CRD record" and the matching "PF30 work mapping" (Change Process Guide §1.0.4) as conflicting with HDE Governance §9.1.1. The §2A substitution of "PF30 work mapping" points at the same PF30 entry that §9.1.1 forbids, so it is aligned in the same drainage. The substitute is the accountability Glow QA Guide "Change-lane QA applicability" states. CRD results and closure posture stay in the change's own records and its authorized closure decision, which "Canon, QA, and closeout boundaries" already lists. The middle bullet is reproduced unchanged.

OLD

````text
* substitute **PF30 work mapping** for **PF09 work-item mapping** for CRD-originated work;  
* route CRD activity, material decisions, and canon-drain lineage through HDE Build Notes where applicable;  
* route CRD results and closure posture to the existing PF30 CRD record; and  
````

NEW

````text
* substitute the CRD's approved Specification, Implementation Plan, and decision lineage for **PF09 work-item mapping** for CRD-originated work; PF30 registration or an invented PF09 mapping is not a prerequisite;  
* route CRD activity, material decisions, and canon-drain lineage through HDE Build Notes where applicable;  
* record CRD results and closure posture in the change's own governed records and its authorized closure decision, not in a PF30 entry; and  
````

## RL-011

Redline number: RL-011
Findings or source items: S-CR1 (CR-1: §2A "Update the existing CRD record"; "PF30 accountability", here "the concise CRD accountability register")
Change type: CONSISTENCY
Operation: `REPLACE`
Target document: `PF27-Canon-Plan-Templates`
Section path: `# **A) Glow Plan and Runbook Templates**` > `## **2A) HDE-CRD-Specification Profile and PF30 Record Contract**` > `### **PF30-owned Specification format and record contract**`
Original-bound location: the section's first two paragraphs and the blank line between them
Original lines (context only): 1941–1943
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: CR-1 names "Update the existing CRD record" as conflicting with HDE Governance §9.1.1. "PF30 is the concise CRD accountability register" restates the same PF30 accountability against §9.1.1 ("neither is an active work register"). HDE CRD Records keeps its role as the CRD Specification's format owner (Change Process Guide §0.1A, "Specification format authority"); the approved Specification states the same posture: "This record uses PF30.1's format and status vocabulary only". A material change is recorded in the Specification's own material-change history through its revision route, and only a separately authorized historical drainage action adds PF30 history (HDE Governance §9.1.1, "Historical drainage"). The section's third paragraph is unchanged. The template's "CRD Plan approval" wording is the PF30 owner's to align (CR-1; ledger task T-PF30.1) and is not addressed here.

OLD

````text
PF30 is the concise CRD accountability register, not the implementation log, QA archive, evidence store, runbook or retrospective. Resolve its current active volume and use its **Minimum CRD record contract** and **CRD record template** for the permanent CRD Specification, including initial registration, material-change history, phase tracking and closure fields. The current format owner is `PF30.1-Canon-HDE-CRD-Records`, **Minimum CRD record contract** and **CRD record template**; this profile does not replace or compress that contract.

Update the existing CRD record when material scope, status, authority or final outcome changes. Preserve its actual historical approval and lineage wording; current Specification terminology does not retrospectively rewrite records.
````

NEW

````text
HDE CRD Records is a historical and reference home, not an active work register, the implementation log, QA archive, evidence store, runbook or retrospective; the active workflow creates, updates or synchronizes no PF30 entry (HDE Governance §9.1.1). Resolve its current active volume and use its **Minimum CRD record contract** and **CRD record template** as the format of the permanent CRD Specification, including initial registration, material-change history, phase tracking and closure fields; the Specification uses that format and its status vocabulary without a PF30 entry. The current format owner is `PF30.1-Canon-HDE-CRD-Records`, **Minimum CRD record contract** and **CRD record template**; this profile does not replace or compress that contract.

Record a material change of scope, status, authority or final outcome in the CRD Specification's own material-change history through its approved revision route, not in a PF30 entry (HDE Governance §9.1.1). Only a separately authorized historical drainage action adds a CRD's approved planned baseline and actual history to HDE CRD Records. Preserve the actual historical approval and lineage wording of existing records; current Specification terminology does not retrospectively rewrite records.
````

## RL-012

Redline number: RL-012
Findings or source items: A31 (addendum 2.31, "Required canon drainage", third bullet: "Plan Templates: a close-mutation-set task template beside the Ops Task Record"; content from "Retained decisions and requirements" rules 4 to 8 only)
Change type: NEW_CANON
Operation: `REPLACE`
Target document: `PF27-Canon-Plan-Templates`
Section path: `# **A) Glow Plan and Runbook Templates**` > `## **3A) Epic Remediation Plan (Template)**` (end), followed by `## **4\) Remediation Implementation Guide (Template)**`
Original-bound location: the section-ending rule after §3A and the §4 heading
Original lines (context only): 2185–2187
Expected non-overlapping occurrence count: `1` (whole original).
Action: replace the exact OLD block once at that original-bound location with the complete NEW block.
Controlling basis and rationale: 2.31 directs a close-mutation-set task template beside the Ops Task Record, and the ledger's uncertainty note limits its content to 2.31 rules 4 to 8. The new §3B takes the next free position after §3 and §3A, so no existing section is renumbered. Every statement maps to those rules: entries, exit, ownership and the never-reopens rule (rule 4); Dev, not Ops (rules 5 and 6, including the close PR and the Ops-run limit); authority, actor and merge (rule 7); and close-tooling repair, narrowing and limits (rule 8). The record fields restate only those elements. Rule 9 (interim operation and the candidate page) and rule 10 (HDE-CRD-0002) are not drafted. No path, schema, command or writer name is minted; the stage's code and title are the ones 2.31 gives. New headings follow Technical Writing Best Practices §8 ("Do not wrap headings in outer bold"). The rule and the §4 heading are reproduced unchanged after the new section.

OLD

````text
---

## **4\) Remediation Implementation Guide (Template)**
````

NEW

````text
## 3B) Close Mutation Set Task Record (Template)

### Definition

A close mutation set task performs the change flow's close-mutation-set stage, CL-05 — Prepare and Publish the Close Mutation Set, for one Epic or CRD. The stage serves every Epic and CRD. It produces the change's close mutation set: the close pack, its two ledgers, the same-run close evidence, and their Index and Mirror registration. It also owns any repair of the close tooling that the close needs. This template states the task's boundaries and the fields its record carries.

### Entries and exit (normative)

* **Entries:** the final QA Report with verdict PASS; or a closure decision of `DO_NOT_CLOSE` whose return work is the close mutation set, because the set is missing, incomplete, or defective.  
* **Exit:** the closure decision, after the Product Owner merges the close pull request.  
* The task never reopens implementation, QA, or the closure decision.

### Dev, not Ops (normative)

* A close mutation set task is a PR work unit. It writes tracked repository state through the canonical writers, and its work lands by the Product Owner's merge.  
* It is not an Ops task and does not use the **Ops Task Record (Template)**. An Ops task requires privileged access to systems outside the repository and is not a repository PR; an Ops run only packages or proves already-produced close-pack artifacts.

### Authority and actor (normative)

* The Product Owner's invocation of the stage for a change authorizes that change's close mutation set and any close-tooling repair it needs, and is the Proceed for both.  
* The task runs as a standalone top-level session that the Product Owner starts with the stage page and the change ID. It needs no handoff to start and resolves its inputs from the change's records.  
* The closure authority (Isis) judges its result at the closure decision. The Product Owner alone merges.

### Close-tooling repair (normative)

* **Rehearsal first:** the task first rehearses the close in a throwaway clone.  
* **Defect:** a close-tooling defect is one where the close tools refuse or fail on correct inputs, or lack an admission the change needs.  
* **Repair:** the task repairs a close-tooling defect in its own pull request with the smallest change to the close-tooling surface (the close-pack writer, its source schemas, the close-run and close-pack admission in the canonical updater, the closeout workflow, and their tests); owner tests that reproduce the defect and prove the fix; and an amendment to the close-pack ADR when the fix changes a decision the ADR records.  
* **Route:** close-tooling repair uses no escalation (ESC), rescope (RS), or PR-10 to PR-40 stage.  
* **Narrowing a recorded rule:** a repair may narrow a close-tooling rule that the close-pack ADR or HDE Build Notes records only where that rule refuses the change's own governed evidence of record. The repair keeps the rule's purpose and records the narrowing and its basis.  
* **Limits:** a repair never changes approved QA evidence, product code, or PF canon.

### Record fields (required)

Every close mutation set task record MUST include:

* **Change identity:** the exact Epic or CRD identity.  
* **Entry:** the final QA Report with verdict PASS, or the `DO_NOT_CLOSE` closure decision whose return work is the close mutation set, by exact source.  
* **Authorization:** the Product Owner's invocation of the stage for this change.  
* **Close mutation set:** the close pack, its two ledgers, the same-run close evidence, and their Index and Mirror registration, each by exact path and produced through the canonical writers.  
* **Close rehearsal:** the throwaway-clone rehearsal and its outcome.  
* **Close-tooling repair:** each defect found, its repair, the owner tests, any close-pack ADR amendment, and any narrowed rule with its basis, or `None`.  
* **Close pull request:** its identity and the Product Owner's merge.  
* **Exit:** the closure decision that judges the result.  
* **Nonclaims:** the task does not reopen implementation, QA, or the closure decision, and changes no approved QA evidence, product code, or PF canon.

---

## **4\) Remediation Implementation Guide (Template)**
````

END OF REDLINES
