---
artifact_type: NEXT_PROMPT_HANDOFF
artifact_id: HDE-CRD-0002-WU-PR-03-CORRECTIVE-ARCHITECTURE-DECISIONS-HANDOFF
artifact_version: "1.0"
from_artifact: docs/ephemeral/HDE-CRD-0002-WU-PR-03-corrective-architecture-decisions-v1.0.md (Product Owner-directed corrective architecture decisions v1.0)
destination_prompt: PR-20 — Create Detailed PR Implementation Plan — 100926.1 (https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba)
CHANGE_CLASS: CRD
CHANGE_ID: HDE-CRD-0002
WORK_UNIT_ID: WU-PR-03
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
capture_time_utc: 2026-10-14T05:10:00Z
---

# HDE-CRD-0002 WU-PR-03 — handoff to PR-20 (corrective plan v2.0)

The block below is the complete, paste-ready continuation. The decision record and the addendum record hold the decisions, the scope and the TypeSafe reading. This file carries nothing else.

```text
NEXT_PROMPT_HANDOFF
Run PR-20 — Create Detailed PR Implementation Plan — 100926.1 https://app.notion.com/p/3f44590a05eb819fbea5dcd966a750ba
Receiving role: the dedicated HDE-CRD-0002 WU-PR-03 PR engineering session (CHANGE_CLASS: CRD), in a PR-20 pre-Proceed planning context for the unit's corrective cycle. Last known WU-PR-03 planning session https://claude.ai/code/session_01GC6jqu4Lczzk7PR7QGXSTJ; Nathan chooses whether to reuse it. Isis is not involved.
Task: write corrective PR implementation plan v2.0 for WU-PR-03 under the approved base plus applicable overlays (Build Notes 2.2, 2.3, 2.5, 2.6, and the corrective addendum record proposed as 2.7), applying architecture decisions AD-1 to AD-6 exactly. #643 merged as c98d41f and its delivered work stands; plan only the corrective delta from main. AUTHORING_CONTEXT: APPROVED_BASE_WITH_OVERLAYS. End at AWAITING_PO_PROCEED when complete and executable.
EXECUTION_POSTURE: MANUAL_PROMPT_EXECUTION
Inputs:
- docs/ephemeral/HDE-CRD-0002-WU-PR-03-corrective-architecture-decisions-v1.0.md — the Product Owner-directed decision record: why, AD index, scope table §4, route §5, CR-7 and CR-8 §6
- docs/ephemeral/HDE-CRD-0002-WU-PR-03-corrective-PF10-build-notes-addendum-v1.0.md — the corrective addendum record (proposed 2.7): binding text of AD-1 to AD-6, overlaid clauses, binding requirements
- docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr35-rescope-request-v1.0.md — RP-4 and RP-5 evidence, now decided
- docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr35-rescope-request-v1.0-prototype.diff — scratch prototypes of the AD-1 and AD-2 changes
- docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr35-rescope-review-v1.0.md — the IA's RS-20 assessment this direction resolves
- docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-plan-v1.1.md — the spent plan #643 implemented; predecessor of plan v2.0
- docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-result-v1.0.md — PR-30 result for #643
- docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-implementation-result-v1.1.md — PR-35 result for #643 (RESCOPE_PENDING; historical)
- docs/ephemeral/HDE-CRD-0002-WU-PR-03-pr-instruction-v1.0.md — PR_INSTRUCTION_ID, unchanged; overlaid by 2.6 and 2.7
- docs/ephemeral/HDE-CRD-0002-WU-PR-03-rescope-review-v1.0.md — first RS-20 decision (B-1 to B-12)
- docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md — IMPLEMENTATION_PLAN_ID, immutable
- docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md — PLAN_REVIEW_ID (INITIAL_APPROVE)
- docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md — SPECIFICATION_ID
- docs/pfcanon/PF10-HDE-Build-Notes-v13.5.7.md — resolve and read the current controlled PF10 afresh; if 2.7 has been published there, it governs over the record
Pull request: amthorn78/glow-hdengine-v2#643 is merged (c98d41f) and is not resumed; the corrective work is a new pull request after a new Proceed.
Prerequisite: pull request amthorn78/glow-hdengine-v2#644 (carrying the decision record, the addendum record and this handoff) is merged to main before you start.
No Proceed, vehicle or open pull request exists for the corrective work; PR_RETURN_PHASE does not apply. Plan v2.0 is presented at AWAITING_PO_PROCEED and authorizes nothing by itself.
```

## Canon relied on

This handoff adds no decision. The sources for the decisions it carries are in the decision record's "Canon relied on" block:
- PF02-Canon-HDE-Architecture v2.4.6 §1.3, §3.2 to §3.5.
- PF29-Canon-HDE-Users-Guide v1.0.2 §1.1.
- PF12-Canon-HDE-Schemas-and-Artifacts v2.9.6 §8.8.
- PF05-Canon-HDE-CLI-API-Vendor-Ref v2.5.3 §5.4 to §5.6.
- PF14-Canon-HDE-Mechanics-Guide v3.5.8 §34.
- PF04-Canon-HDE-Governance v2.8.7 §9.1.2 and its dev/admin gating rule.
- PF27-Canon-Plan-Templates v2.0.5 "Canon precedence for template use".
- PF10-HDE-Build-Notes v13.5.7.
- The HDE-CRD-0002 in-flight records named above.
