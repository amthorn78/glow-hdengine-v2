# HDE-EPIC040-PR02 RS-20 Handoff

- artifact_type: `NEXT_PROMPT_HANDOFF`
- artifact_version: `1.0`
- change_class: `EPIC`
- change_id: `HDE-EPIC040`
- work_unit_id: `HDE-EPIC040-PR02`
- current_state: `READY_FOR_RS20_MANUAL_INVOCATION`
- created_date: `2026-09-12`

## Pasteable prompt

```plain text
Use the selected Notion prompt **RS-20 — Review Bounded Work-Unit Rescope — 091226.3**:
https://app.notion.com/p/3d94590a05eb814e8324f454988d5d30?pvs=204

Act as the continuing whole-change Implementation Agent (IA) for HDE-EPIC040. Execute RS-20 only for the existing HDE-EPIC040-PR02 bounded-rescope review.

EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
session_disposition: RETAIN_EXISTING
role_session_ref: the existing HDE-EPIC040 whole-change IA session assigned to review the PR02 rescope; no platform session ID is asserted by this handoff
invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR02 / RS-20 bounded-rescope review
context_conflict: NONE KNOWN; report any actual contradictory identity or lineage instead of inventing a replacement session

Required inputs — retrieve and read each complete Markdown artifact from its direct Google Drive link:

1. RESCOPE_PROPOSAL_ID — HDE-EPIC040-PR02-rescope-proposal-v1.0.md
   https://drive.google.com/file/d/1nbkt7F4td7keMifg582PFiscWna5oRkH/view?usp=drivesdk
2. Approved Specification — HDE-EPIC040 Approved Specification v1.1
   https://drive.google.com/file/d/11N2WhmgAf-xpSODZdAGYobJN-0F2yqt-/view?usp=drivesdk
3. Whole-change Implementation Audit v2.0
   https://drive.google.com/file/d/1BYPkQ1szI46GO1QQ11T1e6R6sKcprKIp/view?usp=drivesdk
4. Approved whole-change Implementation Plan v2.1
   https://drive.google.com/file/d/1gzhahRj93iqVXp6srL2Ty1rEqS2QDHj2/view?usp=drivesdk
5. Implementation Plan Review v2.1
   https://drive.google.com/file/d/1TIf0_ocyY5sfpgBG8u0w1O_XO_DE9cn5/view?usp=drivesdk
6. PR02 Instruction v1.0
   https://drive.google.com/file/d/15XLW2D-E3Ke_dXKAtxIdytYErhIBz_Ki/view?usp=drivesdk
7. PR02 Detailed Implementation Plan v1.0
   https://drive.google.com/file/d/1iOcCUsOMNuofrPboOyry7c-FDJWASvHQ/view?usp=drivesdk
8. PR02 Result v1.0
   https://drive.google.com/file/d/1QfM27EepUYN3kZuqv_3-SgEk8VLph43d/view?usp=drivesdk

Repository evidence:
- Pull request: https://github.com/amthorn78/glow-hdengine-v2/pull/404
- Branch: hde-epic040-pr02-immutable-admission
- Current recorded head: eed8a63807f573abc29de6f6d5ceac54f0c8da85

Current status and lineage:
- PR-30 result: RESCOPE_PENDING.
- Finding: HDE-EPIC040-PR02-F01.
- PR #404 is open, draft, and unmerged.
- The bounded rescope proposal exists and is pending RS-20 review. It has not been approved.
- No Plan correction, implementation resumption, merge, QA, Ops, release, or closure has occurred.
- GCFPE-20260912.2 publication did not resume the Alpha or authorize any of those actions.

Decisions and constraints:
- Preserve all attributable PR02 work and the existing implementation workspace. Do not rerun PR-30, RS-10, or implementation merely because the storage surface changed.
- The direct Drive links in this handoff are the authoritative runtime locators. Any `libfile_` tokens or ChatGPT Library statements retained inside the rescope proposal are historical lineage only and MUST NOT be used to retrieve an input or infer current storage authority.
- Review the actual bounded proposal against the approved Specification, Plan, Plan review, work-unit artifacts, finding evidence, and repository state.
- Do not approve Product Owner scope, execute implementation, alter the repository, merge the PR, start QA/Ops, or canonicalize PF10.
- Do not invent or attempt to inspect a platform session endpoint. Use the supplied continuing-role identity and report only a real access or identity conflict.

Next required action:
Produce one complete RS-20 `RESCOPE_REVIEW` with the exact proposal and base references, the IA decision (`APPROVE`, `DENY`, or `SPECIFICATION_CHANGE_REQUIRED`), scope classification, rationale, bounded delta or redline, affected work units and dependencies, preserved exclusions, unresolved items with owners, and the exact native next state. Save it as efficient, machine-readable Markdown under **Glow / Ephemeral Planning Files**, read it back, and return its direct Drive link.

If and only if the RS-20 decision approves the rescope and therefore qualifies as an approved rescoping or material Plan change, also produce a separate standalone Markdown artifact named as a `PF10_BUILD_NOTES_ADDENDUM`. Save it under **Glow / Ephemeral Planning Files**, read it back, and return its direct Drive link. It must include `status: READY_FOR_MANUAL_DRAIN`, `canonicality: NON_CANONICAL_PENDING_MANUAL_DRAIN`, and `drain_owner: Nathan / Product Owner`, plus the complete approved delta and required lineage. Do not edit PF10 or claim the addendum is canonical; Nathan's manual drain is the only canonicalization step.

End with exactly one standalone, paste-ready `NEXT_PROMPT_HANDOFF` for the branch actually decided by RS-20, naming the exact selected next Notion prompt, version, and direct URL and carrying every required Drive link and decision. Do not execute that handoff. For an approval, preserve the required Product Owner/manual PF10 disposition and any applicable IA-30 Plan-correction path; approval alone does not authorize implementation. For a denial or Specification change, route to the exact native correction owner with the complete review package.

Expected output:
- one saved and read-back `RESCOPE_REVIEW` with a direct Drive link;
- when the decision qualifies, one separate saved and read-back `PF10_BUILD_NOTES_ADDENDUM` with a direct Drive link and non-canonical/manual-drain status; and
- one exact paste-ready next-prompt handoff for the resulting branch, without executing downstream work.
```
