# Redlines — PF06-Canon-Change-Process-Guide v2.5.4 (T-PF06, GTWPE 100926.1)

- Package: `redlines-PF06-from-v2.5.4.md`; proof log `redlines-PF06-from-v2.5.4.proof-log.md` beside it.
- Run identity: `gtwpe-20261026-pf10-v13-8-8 / T-PF06 / TW-DRAIN-10 run 1`.
- Preparer: TW-DRAIN-10 — Prepare PF Document Redlines — 100926.1 (https://app.notion.com/p/3f44590a05eb8172a314fe6b958bb9ff), in the Claude Code session https://claude.ai/code/session_01H9YUsfAYvAB5rJUKsZrCxB.
- Preparation outcome: `READY`. Save completeness: recorded in the proof log after read-back.
- Original baseline: `docs/pfcanon/PF06-Canon-Change-Process-Guide-v2.5.4.md`, version v2.5.4, at `origin/main` `9dda63dd3f05f496c3ff67e95da78550d3950c5a`; Git blob `d2df157b4014224406a8a0c52b64e28c53395e99`; 428,753 bytes; 4,651 LF-terminated lines; SHA-256 `6f47d808c58708e03e28a0c9ca106248054257755503681d3e60e36deed9fe46`.
- Ledger: `docs/ephemeral/gtwpe/gtwpe-20261026-pf10-v13-8-8/LEDGER.md` (blob `74944b261c0e`), task T-PF06, rows S-CR1, A11, A14, A31, A15, A16, A17, X03 and S-APR.
- Header sources, in source order, for TW-APPLY-10's metadata plan: `docs/pfcanon/PF10-HDE-Build-Notes-v13.8.8.md` (PF10 v13.8.8); `HDE-CRD-0002-specification-v1.1-approved.md`. No redline below touches a document-control field.

## Payload convention

Every redline is a `REPLACE`. Its OLD block and NEW block are the literal text between the five-backtick fence lines that follow the labels `OLD` and `NEW`. The line feed that ends the last line before a closing fence belongs to the fence, not to the literal. Each OLD block is one or more complete baseline lines; the line feed that follows it in the baseline is kept, and is not part of either literal. Each OLD block occurs exactly once in the baseline (expected occurrences: 1). Line numbers are informational; the exact OLD block governs. No two OLD blocks intersect or touch.

## R-01 — §0.1: the CRD lane is not accountable to PF30

- Redline ID: R-01
- Operation: REPLACE
- Source rows: S-CR1 (Specification CR-1, lines 199-208; HDE Governance §9.1.1 as the governing owner, supporting reading)
- Change type: CONSISTENCY
- Target document: PF06-Canon-Change-Process-Guide
- Heading path: `# **0\. Front Matter**` > `## **0.1 Purpose and scope**`
- Original-baseline location: line 17; byte offsets 287 to 1109 (end exclusive)
- Expected occurrences of the OLD block: 1
- Rationale: CR-1 names §0.1's "accountable to PF30"; HDE Governance §9.1.1 makes HDE CRD Records historical/reference only, not an active work register, and §9.1 forms a CRD from the Product Owner-controlled CRD identity.

OLD

`````text
This guide defines the common change-delivery process for a human \+ pair-programming workflow with an executing agent across two governed lanes: the Epic lane for product-development work originating in or formally mapped to PF09, and the CRD lane for observed features, defects, operational needs, governance needs, and system changes originating outside PF09 and accountable to PF30. It supplies paste-ready headers, checklists, and prompts. It requires an Audit and a Sandbox Build/Test for each epic or CRD. The normal route for code-bearing epic or CRD work is PR-based, while an explicit current Product Owner instruction may authorize a bounded direct-to-`main` route. Close requires the applicable exact-source evidence, close-pack material, and authorized decisions; a PASS acceptance-token list is not required.
`````

NEW

`````text
This guide defines the common change-delivery process for a human \+ pair-programming workflow with an executing agent across two governed lanes: the Epic lane for product-development work originating in or formally mapped to PF09, and the CRD lane for observed features, defects, operational needs, governance needs, and system changes originating outside PF09 and accountable through a Product Owner-controlled CRD identity and its approved CRD Specification and change-wide Implementation Plan. It supplies paste-ready headers, checklists, and prompts. It requires an Audit and a Sandbox Build/Test for each epic or CRD. The normal route for code-bearing epic or CRD work is PR-based, while an explicit current Product Owner instruction may authorize a bounded direct-to-`main` route. Close requires the applicable exact-source evidence, close-pack material, and authorized decisions; a PASS acceptance-token list is not required.
`````

## R-02 — §0.1A: CRD lane identity and accountability

- Redline ID: R-02
- Operation: REPLACE
- Source rows: S-CR1 (Specification CR-1, lines 199-208; HDE Governance §9.1.1 as the governing owner, supporting reading)
- Change type: CONSISTENCY
- Target document: PF06-Canon-Change-Process-Guide
- Heading path: `# **0\. Front Matter**` > `## **0.1A Governing lanes, common lifecycle, and authority routing**`
- Original-baseline location: line 26; byte offsets 1554 to 1780 (end exclusive)
- Expected occurrences of the OLD block: 1
- Rationale: CR-1 names §0.1A's "PF30 accountability"; HDE Governance §9.1.1 names the approved Specification and Implementation Plan as each change's substantive authorities and forbids the active workflow to create, update or synchronize HDE CRD Records entries.

OLD

`````text
* **CRD lane.** Observed features, defects, operational needs, governance needs, and system changes originating outside PF09 use CRD identity and PF30 accountability. A canon-changing CRD requires an accompanying approved ADR.
`````

NEW

`````text
* **CRD lane.** Observed features, defects, operational needs, governance needs, and system changes originating outside PF09 use a Product Owner-controlled CRD identity and are accountable through the approved CRD Specification and change-wide Implementation Plan. A canon-changing CRD requires an accompanying approved ADR.
`````

## R-03 — §0.1A: the lanes differ in work accountability, not in a controlling register

- Redline ID: R-03
- Operation: REPLACE
- Source rows: S-CR1 (Specification CR-1, lines 199-208; HDE Governance §9.1.1 as the governing owner, supporting reading)
- Change type: CONSISTENCY
- Target document: PF06-Canon-Change-Process-Guide
- Heading path: `# **0\. Front Matter**` > `## **0.1A Governing lanes, common lifecycle, and authority routing**`
- Original-baseline location: line 28; byte offsets 1782 to 2152 (end exclusive)
- Expected occurrences of the OLD block: 1
- Rationale: Aligning §0.1A (CR-1): once PF30 is no longer the CRD lane's accountability, "controlling work register" would assert a CRD register that HDE Governance §9.1.1 says does not exist ("neither is an active work register").

OLD

`````text
The lanes differ in origin, identity, and controlling work register. They do not differ in applicable development, QA, evidence, operations, or closure rigor. A CRD is a top-level governed change container comparable to an epic and may contain one or more PRs, Ops tasks, or both. PF06 MUST NOT use CRD as an intermediate document or subordinate stage inside every epic.
`````

NEW

`````text
The lanes differ in origin, identity, and work accountability: PF09 work items for the Epic lane, and the approved CRD Specification and change-wide Implementation Plan for the CRD lane. They do not differ in applicable development, QA, evidence, operations, or closure rigor. A CRD is a top-level governed change container comparable to an epic and may contain one or more PRs, Ops tasks, or both. PF06 MUST NOT use CRD as an intermediate document or subordinate stage inside every epic.
`````

## R-04 — §0.1A lifecycle item 14: no PF30 record step

- Redline ID: R-04
- Operation: REPLACE
- Source rows: S-CR1 (Specification CR-1, lines 199-208; HDE Governance §9.1.1 as the governing owner, supporting reading)
- Change type: CONSISTENCY
- Target document: PF06-Canon-Change-Process-Guide
- Heading path: `# **0\. Front Matter**` > `## **0.1A Governing lanes, common lifecycle, and authority routing**`
- Original-baseline location: line 45; byte offsets 2682 to 2740 (end exclusive)
- Expected occurrences of the OLD block: 1
- Rationale: CR-1 names lifecycle item 14 ("PF09 or PF30 record completion"); HDE Governance §9.1.1 "Historical drainage": no PF30 entry is required at closure, and only a separately authorized historical drainage action may add one.

OLD

`````text
14. PF09 or PF30 record completion, according to the lane.
`````

NEW

`````text
14. PF09 record completion for the Epic lane. The CRD lane has no PF30 record step; only a separately authorized historical drainage action may add a CRD's history to HDE CRD Records.
`````

## R-05 — §0.1A: CRD reuse substitutes the approved Specification and Plan, not PF30 mapping

- Redline ID: R-05
- Operation: REPLACE
- Source rows: S-CR1 (Specification CR-1, lines 199-208; HDE Governance §9.1.1 as the governing owner, supporting reading)
- Change type: CONSISTENCY
- Target document: PF06-Canon-Change-Process-Guide
- Heading path: `# **0\. Front Matter**` > `## **0.1A Governing lanes, common lifecycle, and authority routing**`
- Original-baseline location: line 47; byte offsets 2742 to 3084 (end exclusive)
- Expected occurrences of the OLD block: 1
- Rationale: Aligning §0.1A (CR-1): "PF30 work mapping" treats HDE CRD Records as a work register, which HDE Governance §9.1.1 excludes; HDE Governance §9.1 "Epic and CRD change lanes": CRD formation MUST NOT manufacture a PF09 inventory.

OLD

`````text
Existing epic requirements remain operative unless PF06 explicitly changes them. The CRD lane reuses the established downstream process by substituting CRD identity for Epic identity and PF30 work mapping for PF09 work-item mapping. No duplicate CRD-specific template system is created where that substitution preserves the required contract.
`````

NEW

`````text
Existing epic requirements remain operative unless PF06 explicitly changes them. The CRD lane reuses the established downstream process by substituting CRD identity for Epic identity and the approved CRD Specification and change-wide Implementation Plan for PF09 work-item mapping; a CRD manufactures no PF09 inventory and has no PF30 work mapping. No duplicate CRD-specific template system is created where that substitution preserves the required contract.
`````

## R-06 — §0.1A authority routing: HDE CRD Records is historical and reference only

- Redline ID: R-06
- Operation: REPLACE
- Source rows: S-CR1 (Specification CR-1, lines 199-208; HDE Governance §9.1.1 as the governing owner, supporting reading)
- Change type: CONSISTENCY
- Target document: PF06-Canon-Change-Process-Guide
- Heading path: `# **0\. Front Matter**` > `## **0.1A Governing lanes, common lifecycle, and authority routing**`
- Original-baseline location: line 57; byte offsets 3730 to 3805 (end exclusive)
- Expected occurrences of the OLD block: 1
- Rationale: CR-1 names "HDE CRD Records controls PF30 CRD registration and result tracking"; HDE Governance §9.1.1. The format role stays, as §0.1A "Specification format authority" (unchanged) and the approved Specification's "Format and register posture" use it.

OLD

`````text
* **HDE CRD Records** controls PF30 CRD registration and result tracking.  
`````

NEW

`````text
* **HDE CRD Records** supplies the CRD record contract and template that CRD Specifications use; it is a historical and reference home, not an active work register, approval gate or required runtime input, and the active workflow creates, updates or synchronizes no entry in it.  
`````

## R-07 — §1.0 heading: no CRD Plan and no PF30 registration

- Redline ID: R-07
- Operation: REPLACE
- Source rows: S-CR1 (Specification CR-1, lines 199-208; HDE Governance §9.1.1 as the governing owner, supporting reading)
- Change type: CONSISTENCY
- Target document: PF06-Canon-Change-Process-Guide
- Heading path: `# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**` > `## **1.0 CRD lane intake, plan, and PF30 registration**`
- Original-baseline location: line 1429; byte offsets 150050 to 150105 (end exclusive)
- Expected occurrences of the OLD block: 1
- Rationale: CR-1 names the §1.0 heading; HDE Governance §9.1.1: "There is no third active Epic Plan, CRD Plan or Implementation Guide", and no PF30 entry is created. Section numbering is unchanged.

OLD

`````text
## **1.0 CRD lane intake, plan, and PF30 registration**
`````

NEW

`````text
## **1.0 CRD lane intake, Specification, and approval**
`````

## R-08 — §1.0.3: CRD identity and approval replace PF30 registration

- Redline ID: R-08
- Operation: REPLACE
- Source rows: S-CR1 (Specification CR-1, lines 199-208; HDE Governance §9.1.1 as the governing owner, supporting reading)
- Change type: CONSISTENCY
- Target document: PF06-Canon-Change-Process-Guide
- Heading path: `# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**` > `## **1.0 CRD lane intake, plan, and PF30 registration**` > `### **1.0.3 PF30 registration and approval**`
- Original-baseline location: lines 1461 to 1463; byte offsets 151332 to 151714 (end exclusive)
- Expected occurrences of the OLD block: 1
- Rationale: CR-1 names §1.0.3 (quoted there as "MUST receive [OMITTED] a concise initial record in PF30 before implementation begins"); HDE Governance §9.1.1 (two substantive authorities; no PF20/PF30 entry required at kickoff, Specification approval, IP approval, implementation, acceptance or closure) and §9.1 (CRD formed from the Product Owner-controlled CRD identity).

OLD

`````text
### **1.0.3 PF30 registration and approval**

The CRD MUST receive a stable CRD ID and a concise initial record in PF30 before implementation begins. The CRD Specification MUST receive the approval required by current governance. If the required PF30 record cannot be established, implementation is blocked; do not substitute PF09 accountability or claim that registration occurred.
`````

NEW

`````text
### **1.0.3 CRD identity and approval**

The CRD MUST carry a stable, Product Owner-controlled CRD ID from its formation. The CRD Specification MUST receive the approval required by current governance; the approved CRD Specification and the separately approved change-wide Implementation Plan are its substantive authorities (HDE Governance). No PF30 entry is created, updated or required at intake, Specification approval, Implementation Plan approval, implementation, acceptance or closure. If the CRD ID or the required approval cannot be established, implementation is blocked; do not substitute PF09 accountability or claim that an approval occurred.
`````

## R-09 — §1.0.4: downstream reuse without PF30 work mapping

- Redline ID: R-09
- Operation: REPLACE
- Source rows: S-CR1 (Specification CR-1, lines 199-208; HDE Governance §9.1.1 as the governing owner, supporting reading)
- Change type: CONSISTENCY
- Target document: PF06-Canon-Change-Process-Guide
- Heading path: `# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**` > `## **1.0 CRD lane intake, plan, and PF30 registration**` > `### **1.0.4 Phase separation and execution**`
- Original-baseline location: line 1469; byte offsets 152149 to 152615 (end exclusive)
- Expected occurrences of the OLD block: 1
- Rationale: CR-1 names §1.0.4 ("PF30 work mapping"); HDE Governance §9.1.1 (HDE CRD Records is not an active work register or implementation authority).

OLD

`````text
After approval, the CRD follows the applicable downstream Epic process using CRD identity and PF30 work mapping. Existing templates SHOULD be reused by substituting CRD for Epic and PF30 mapping for PF09 mapping when that substitution preserves the contract. Implementation guidance and planning, phase-bounded PR and/or Ops execution, review and correction, exact-source implementation evidence, and controlled candidate handoff to QA remain required as applicable.
`````

NEW

`````text
After approval, the CRD follows the applicable downstream Epic process using CRD identity, with its approved CRD Specification and change-wide Implementation Plan in place of PF09 work-item mapping. Existing templates SHOULD be reused by substituting CRD for Epic, and the approved CRD Specification and Implementation Plan for PF09 mapping, when that substitution preserves the contract; a CRD has no PF30 work mapping. Implementation guidance and planning, phase-bounded PR and/or Ops execution, review and correction, exact-source implementation evidence, and controlled candidate handoff to QA remain required as applicable.
`````

## R-10 — §1.0.6 heading: no PF30 result update

- Redline ID: R-10
- Operation: REPLACE
- Source rows: S-CR1 (Specification CR-1, lines 199-208; HDE Governance §9.1.1 as the governing owner, supporting reading)
- Change type: CONSISTENCY
- Target document: PF06-Canon-Change-Process-Guide
- Heading path: `# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**` > `## **1.0 CRD lane intake, plan, and PF30 registration**` > `### **1.0.6 QA, closeout, and PF30 result update**`
- Original-baseline location: line 1475; byte offsets 153052 to 153102 (end exclusive)
- Expected occurrences of the OLD block: 1
- Rationale: CR-1 names §1.0.6; its heading would otherwise announce the PF30 result update that R-11 removes. Section numbering is unchanged.

OLD

`````text
### **1.0.6 QA, closeout, and PF30 result update**
`````

NEW

`````text
### **1.0.6 QA and closeout**
`````

## R-11 — §1.0.6: closure records no PF30 entry; historical drainage only

- Redline ID: R-11
- Operation: REPLACE
- Source rows: S-CR1 (Specification CR-1, lines 199-208; HDE Governance §9.1.1 as the governing owner, supporting reading)
- Change type: CONSISTENCY
- Target document: PF06-Canon-Change-Process-Guide
- Heading path: `# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**` > `## **1.0 CRD lane intake, plan, and PF30 registration**` > `### **1.0.6 QA, closeout, and PF30 result update**`
- Original-baseline location: line 1481; byte offsets 153849 to 154101 (end exclusive)
- Expected occurrences of the OLD block: 1
- Rationale: CR-1 names §1.0.6 ("update the existing PF30 CRD record"); HDE Governance §9.1.1 ("The active workflow MUST NOT create, update or synchronize their entries"; "Historical drainage").

OLD

`````text
At closure, update the existing PF30 CRD record with the concise final result. PF30 is the accountability register, not the implementation log, QA archive, or evidence store. Detailed activity remains in its governed source and is referenced from PF30.
`````

NEW

`````text
Closure does not create, update or synchronize a PF30 entry. The CRD's final result is recorded by its own closure decision and governed records, and detailed activity remains in its governed source. HDE CRD Records is a historical and reference home, not an accountability register, implementation log, QA archive or evidence store. Only a separately authorized historical drainage action may add the CRD's approved planned baseline as planned state, and its actual implementation, PR, Ops, QA, evidence, variances and disposition as distinct actual state, to HDE CRD Records.
`````

## R-12 — §1.1.4: PR-review finding disposition, P1 rules and the repeated-finding-class trigger

- Redline ID: R-12
- Operation: REPLACE
- Source rows: A11 (PF10 addendum 2.11 rules 4, 5, 7 and 8, its drainage row for Change Process Guide §1.1.4, read by the rule each misnumbered cross-reference describes, and as narrowed by 2.14 and 2.18); A14 (addendum 2.14 rules 1 to 4 and 6, and its drainage row for Change Process Guide §1.1.4)
- Change type: NEW_CANON
- Target document: PF06-Canon-Change-Process-Guide
- Heading path: `# **1\) CHANGE INTAKE AND PLANNING (Lead Dev)**` > `## **1.1 Epic-lane workflow at a glance**` > `### **1.1.4 Live QA mechanical evidence expectations**`
- Original-baseline location: line 1684; byte offsets 172704 to 173035 (end exclusive)
- Expected occurrences of the OLD block: 1
- Rationale: 2.11's drainage row places "the rule 5 disposition and the rule 6 trigger" (by their text, rules 7 and 8) beside the Live QA churn rules of §1.1.4; 2.14's row carries its rules 2 and 3 beside them. The real-input definition (2.11 rules 4 and 5) is carried because the disposition rule depends on it and no permanent PF home defines it. The cost-ceiling text (2.11 rule 1's ceiling bullet and rule 3's ceiling clauses, 2.14 rule 5) is withdrawn by 2.18 and is not carried. The baseline line 1684 is reproduced unchanged before the new block.

OLD

`````text
QoS stop-rule (iteration churn escalation). If the Live QA plan requires repeated structural remediation for the same failure mode across revisions (suggest threshold: 2), treat the issue as a systems-level prompt/template defect. Escalate to a systems RCA and a canonical drain that targets the class of failure, not the incident.
`````

NEW

`````text
QoS stop-rule (iteration churn escalation). If the Live QA plan requires repeated structural remediation for the same failure mode across revisions (suggest threshold: 2), treat the issue as a systems-level prompt/template defect. Escalate to a systems RCA and a canonical drain that targets the class of failure, not the incident.

PR review finding disposition (every pull request; real inputs only). The Live QA churn rules above, including the QoS stop-rule, cover Live QA plans only. The rules below govern review findings, from the automated code review in the review chain or from a person, on every pull request of every Epic and CRD.

* Real input. A finding's triggering input is real when it exists on `main` or in an approved work unit's planned deliverable; occurs in the product's real operating environment, such as the deployed services, the hosted CI runner, the operator's shell or the vendor's responses; or can be supplied by a user, a vendor or an attacker through an interface the product exposes. An input constructed only to exercise code justifies no requirement, design element, test, fix or blocking finding; an input outside the real set receives one refusal or a stated limit, never a model of it.  
* Findings below P1. A finding is fixed when it shows a wrong result, a crash or a guarantee breach on a real input. Otherwise, the reply on the thread gives the traced path and the stated limit, and the thread is resolved. Declining a security finding goes to the Product Owner first. A blanket instruction to fix every finding on a pull request is read under this rule. The standing default is to fix only a wrong result on a real input, or a breach of a read-only or no-secrets guarantee; a snapshot-precision finding is a hypothetical-input finding unless it shows a write that the tool itself, or code it runs in the checkout, can make.  
* P1 findings. A P1 finding is a review finding labelled P1 or any higher priority, such as P0; the priority is the label the reviewer gives. A P1 finding whose triggering input is real MUST be fixed. It MUST NOT be declined, deferred to a later change, recorded as a stated limit, or resolved on cost, effort, design preference, a plan's earlier choice, an ADR's stated limit or a "not worth its code" judgement. Fixed means that the wrong result, crash or guarantee breach the finding reports no longer occurs on that real input, shown by a test that fails without the fix; a typed refusal of the input is a fix when refusing it is correct behavior for the product. The thread stays open until the fix is pushed and the finding's own check of it is answered. A pull request with an open P1 thread on a real input is not merge-ready.  
* The one P1 exception. A P1 finding MAY be declined only when its triggering input is not real under the definition above, so that the input is one constructed only to exercise the code. The reply on the thread gives the traced path and shows why the input can never occur in the product. Declining a P1 goes to the Product Owner first, and the thread is resolved only after that.  
* Repeated finding class. When two consecutive review rounds on one pull request raise findings of the same class, meaning the same component or contract, the PR session stops fixing instances and asks the Product Owner one design question: narrow the design, accept a stated limit, or rescope. For a P1 on a real input, accepting a stated limit is not an option: the answer is a fix, a narrowed design that removes the wrong result (a typed refusal included), or a rescope through the native route, and the P1 is resolved before the pull request merges. This is a design trigger by finding class. It is not a push count, a pause threshold or a CI-budget control, and it leaves the CI-budget rules in §0.2, including "There is no five-update circuit breaker", unchanged.  
* Unchanged duty. Nothing in these rules weakens the existing duty to fix a real defect at any priority.
`````

## R-13 — §3.5.1: name the close-mutation-set stage, its entries, exit, ownership and close-tooling repair

- Redline ID: R-13
- Operation: REPLACE
- Source rows: A31 (PF10 addendum 2.31 rules 4 to 8 and its drainage item for Change Process Guide §3.5.1 and §3.5.2)
- Change type: NEW_CANON
- Target document: PF06-Canon-Change-Process-Guide
- Heading path: `# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**` > `## **3.5 Close Gate (route-aware)**` > `### **3.5.1 Requirement**`
- Original-baseline location: line 2943; byte offsets 290272 to 290425 (end exclusive)
- Expected occurrences of the OLD block: 1
- Rationale: 2.31 drainage: "Change Process Guide §3.5.1 and §3.5.2: name the close-mutation-set stage as part of the change flow, with its entries, its exit to the closure decision and its ownership of close-tooling repair." The stage is named functionally, as PF06 names no prompt codes (Technical Writing Best Practices §2). Rule 9 (interim operation until a GCFPE Modification installs the stage) and rule 10 (HDE-CRD-0002's first run) are not carried. The baseline line 2943 is reproduced unchanged before the new block.

OLD

`````text
Only the close mutation set is required to carry the full close pack and final exact-source acceptance record. A final PASS-token roster is not required.
`````

NEW

`````text
Only the close mutation set is required to carry the full close pack and final exact-source acceptance record. A final PASS-token roster is not required.

Close-mutation-set stage. The close mutation set is produced by its own stage of the change flow, the close-mutation-set stage, which serves every Epic and CRD. It sits between the final QA Report and the closure decision.

* Entries. The stage starts from the final QA Report with verdict `PASS`, or from a closure decision of `DO_NOT_CLOSE` whose return work is the close mutation set because it is missing, incomplete or defective.  
* Exit. The stage exits to the closure decision after the Product Owner merges the close PR.  
* What it owns. The stage owns the close mutation set: the close pack, its doc-delta and drain-target ledgers, the same-run close evidence, and their Human Evidence Index and Machine Mirror registration. It also owns any repair of the close tooling that the close needs.  
* What it never does. The stage never reopens implementation, QA or the closure decision.  
* Authority and actor. The Product Owner's invocation of the stage for a change authorizes that change's close mutation set and any close-tooling repair it needs, and is the Proceed for both. The stage runs as a standalone top-level session that the Product Owner starts with the stage prompt and the change ID; it needs no handoff to start and resolves its inputs from the change's records. The closure authority judges its result at the closure decision, and the Product Owner alone merges.  
* Close-tooling repair. The stage first rehearses the close in a throwaway clone. A close-tooling defect is one where the close tools refuse or fail on correct inputs, or lack an admission the change needs. The stage repairs it in its own pull request with the smallest change to the close-tooling surface (the close-pack writer, its source schemas, the close-run and close-pack admission in the canonical evidence updater, the closeout workflow and their tests), owner tests that reproduce the defect and prove the fix, and an amendment to the close-pack ADR when the fix changes a decision the ADR records. A repair MAY narrow a close-tooling rule that the ADR or HDE Build Notes records only where that rule refuses the change's own governed evidence of record; it keeps the rule's purpose and records the narrowing and its basis. A repair never changes approved QA evidence, product code or PF canon. Close-tooling repair is this stage's own work: it uses no escalation stage, no rescope stage and no stage of the ordinary PR work-unit chain from PR instructions through lineage review.  
* Dev, not Ops. The stage is a PR work unit; §3.5.2 states the Dev and Ops boundary.
`````

## R-14 — §3.5.2: the close mutation set is Dev work; an Ops run only packages or proves

- Redline ID: R-14
- Operation: REPLACE
- Source rows: A31 (PF10 addendum 2.31 rules 5 and 6 and its drainage item for Change Process Guide §3.5.1 and §3.5.2)
- Change type: NEW_CANON
- Target document: PF06-Canon-Change-Process-Guide
- Heading path: `# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**` > `## **3.5 Close Gate (route-aware)**` > `### **3.5.2 Close PR contents**`
- Original-baseline location: line 2967; byte offsets 292896 to 292927 (end exclusive)
- Expected occurrences of the OLD block: 1
- Rationale: 2.31 drainage: "State that it is Dev, and that an Ops run only packages or proves already-produced artifacts" (rules 5 and 6, citing §0.2's Ops and OPS-01 rules and HDE Governance §9.1). The baseline heading line 2967 is reproduced unchanged before the new paragraph.

OLD

`````text
### **3.5.2 Close PR contents**
`````

NEW

`````text
### **3.5.2 Close PR contents**

The close PR carries the close mutation set that the close-mutation-set stage in §3.5.1 produces. That stage is Dev work, not Ops: it is a PR work unit that writes tracked repository state through the canonical writers, and its work lands by the Product Owner's merge. An Ops task requires privileged access to systems outside the repository and is not a repository PR. An Ops closeout run, such as OPS-01 in §0.2 or OPS-02 in §3.5.2.1, only packages or proves already-produced artifacts and does not produce the close mutation set.
`````

## R-15 — §3.5.2.1: CRD filename prefix, the v2 writer as generic producer, the close-run family as same-run evidence home

- Redline ID: R-15
- Operation: REPLACE
- Source rows: A15 (addendum 2.15 "What is approved" and "The close-run evidence family (introduced)"), A16 (addendum 2.16's drainage of Change Process Guide §3.5.2 and §3.5.2.1 through the ADR canon table), X03 (ADR "Affected canon and drainage consequences" row for §3.5.2 and §3.5.2.1; Decision items 1 to 3 and 7), S-APR (S21's canon impact: Change Process Guide §3.5.2, close pack)
- Change type: CANON_UPDATE
- Target document: PF06-Canon-Change-Process-Guide
- Heading path: `# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**` > `## **3.5 Close Gate (route-aware)**` > `### **3.5.2 Close PR contents**` > `#### **3.5.2.1 Close-pack files**`
- Original-baseline location: lines 2971 to 2976; byte offsets 292964 to 293164 (end exclusive)
- Expected occurrences of the OLD block: 1
- Rationale: ADR canon table row for §3.5.2 "Close PR contents" and §3.5.2.1 "Close-pack files": "Name the CRD filename prefix beside EPIC-NNN, the v2 writer as the generic producer, and the close-run family as the same-run evidence home"; ADR decisions 1 to 3 and 7; 2.15 "The close-run evidence family (introduced)" (path, post-verdict status, single writer, no Epic family). Baseline lines 2972 to 2976 are reproduced unchanged inside the replacement.

OLD

`````text
The close PR MUST include the epic close-pack (canonical filenames):

* audit/EPIC-\\\_close\_report.md  
* audit/EPIC-\\\_MANIFEST.json

Where \\ is the zero-padded 3-digit epic number (see §0.5.1).
`````

NEW

`````text
The close PR MUST include the change's close-pack (canonical filenames). For an epic:

* audit/EPIC-\\\_close\_report.md  
* audit/EPIC-\\\_MANIFEST.json

Where \\ is the zero-padded 3-digit epic number (see §0.5.1).

For a CRD, the CRD ID is the filename prefix beside the epic `EPIC-NNN` form, and its lower-case ID is the directory form (for example `hde-crd-0002`):

* `audit/HDE-CRD-<NNNN>_close_report.md`  
* `audit/HDE-CRD-<NNNN>_MANIFEST.json`

The generic producer of an Epic or CRD close pack is the v2 close-pack writer, `tools/qa/generate_epic_close_pack.py`, reading a `close_candidate_source.v2` candidate source; HDE Schemas and Artifacts owns the source schema, the manifest and the close-pack paths of record. For a CRD admitted in the canonical evidence updater's CRD admission, the same-run close evidence home is its post-verdict close-run family under `audit/qa/<change-dir>/close/`, where `<change-dir>` is the lower-case directory form of the CRD ID; only the canonical evidence updater writes it. That family is never listed in, and never reopens, the change's approved QA step-logs manifest or any `checks/` primary. No Epic close-run family is admitted; an Epic close run needs its own explicit admission.
`````

## R-16 — §3.5.2.1 tracked-issue mapping: the v2 writer supports only form (b)

- Redline ID: R-16
- Operation: REPLACE
- Source rows: A17 (addendum 2.17 resolution B and its drainage row for Change Process Guide §3.5.2.1); A16 (LR7-O9); A15 (C-3 as amended by 2.17)
- Change type: CANON_UPDATE
- Target document: PF06-Canon-Change-Process-Guide
- Heading path: `# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**` > `## **3.5 Close Gate (route-aware)**` > `### **3.5.2 Close PR contents**` > `#### **3.5.2.1 Close-pack files**`
- Original-baseline location: line 2983; byte offsets 293865 to 294209 (end exclusive)
- Expected occurrences of the OLD block: 1
- Rationale: 2.17 drainage row for "Change Process Guide §3.5.2.1; HDE Governance §2.0.19 canon-pointer fields": "Note that the generic v2 writer supports only form (b) (resolution B)"; the v2 schema on main defines a tracked issue as {id, adr_status} only.

OLD

`````text
* a tracked-issue closeout mapping in the close report for any TI-\* items cited by the epic (example: TI-002): each TI item MUST map to either (a) PF09 subtask pointers (repo path plus section heading) that demonstrate closure, or (b) an ADR status line in the close report that records Deferred with drain targets so closure is unambiguous.  
`````

NEW

`````text
* a tracked-issue closeout mapping in the close report for any TI-\* items cited by the epic (example: TI-002): each TI item MUST map to either (a) PF09 subtask pointers (repo path plus section heading) that demonstrate closure, or (b) an ADR status line in the close report that records Deferred with drain targets so closure is unambiguous. The generic v2 close-pack writer supports only form (b): it renders each tracked issue as an ADR-status item in HDE Governance's literal `ADR status line:` field and refuses form (a), because no PF09 or PF30 file cites a TI ID. A close whose tracked issue is closed as satisfied through PF09 or PF30 pointers needs a later source-schema version.  
`````

## R-17 — §3.5.4: the v2 ADR block, closure override and resolution A; CRD location

- Redline ID: R-17
- Operation: REPLACE
- Source rows: A15 (addendum 2.15 C-1), A17 (addendum 2.17 resolution A and its drainage row for Change Process Guide §3.5.4), A16 (LR7-O1, resolved by 2.17), X03 (ADR canon table row for §3.5.4; Decision item 9)
- Change type: CANON_UPDATE
- Target document: PF06-Canon-Change-Process-Guide
- Heading path: `# **3\) IMPLEMENTATION PLAN (Implementation Agent; Lead Dev approves once, then steps out)**` > `## **3.5 Close Gate (route-aware)**` > `### **3.5.4 ADR block in the close-pack (all epics)**`
- Original-baseline location: lines 3318 to 3320; byte offsets 323443 to 323528 (end exclusive)
- Expected occurrences of the OLD block: 1
- Rationale: ADR canon table row for §3.5.4: "Name the v2 report's ADR block, rendered from the source's ADR-block decisions and optional closure override"; 2.17 drainage row: "Carry resolution A as the close pack's treatment of a TOOLING_BLOCKED check under a closure override"; 2.15 C-1 applies the ADR block to a CRD close. Baseline lines 3318 and 3319 are reproduced unchanged, and line 3320 gains " for an epic".

OLD

`````text
Location. The ADR block lives in the close report:

* audit/EPIC-\\\_close\_report.md
`````

NEW

`````text
Rendering by the generic v2 close-pack writer. For a close pack written by the v2 close-pack writer, the ADR block is rendered from the candidate source's required, non-empty list of ADR-block decisions, each carrying the fields listed above with titles-only canon references, and from an optional closure-override entry that enumerates each accepted gap with the `TOOLING_BLOCKED` check it accepts, its evidence basis and its drain targets.

Closure override in a v2 close pack. A v2 `SATISFIED` decision requires every check of the change's current QA plan to be recorded in the QA step-logs manifest in one of two ways: as `PASS`, or as `TOOLING_BLOCKED` where a closure-override gap in the ADR block names that check, once. A check recorded as `FAIL_BEHAVIOR`, `FAIL_TOOLING` or `PARKED`, and a planned check the manifest does not record, block `SATISFIED`. A `TOOLING_BLOCKED` check accepted under a closure override is never `PASS` evidence for a met acceptance criterion.

Location. The ADR block lives in the close report:

* audit/EPIC-\\\_close\_report.md for an epic  
* `audit/HDE-CRD-<NNNN>_close_report.md` for a CRD
`````

END OF REDLINES
