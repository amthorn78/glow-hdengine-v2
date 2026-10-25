---
artifact_type: NEXT_PROMPT_HANDOFF
artifact_version: "1.0"
predecessor: none
change_id: HDE-CRD-0002
from: ESC-40 — Review and Return Approved Remediation — 100926.1, Isis (https://claude.ai/code/session_01NxRhYei7RDGmMPYdKEkpok)
decision_ref: docs/ephemeral/HDE-CRD-0002-remediation-review-QA110-F01-v1.0.md (APPROVE_AS_CHANGED), with addendum record docs/ephemeral/HDE-CRD-0002-remediation-QA110-F01-PF10-build-notes-addendum-v1.0.md (2.27)
---

```text
NEXT_PROMPT_HANDOFF
Destination: PR-10 — Create PR Work-Unit Instructions — 100926.1
https://app.notion.com/p/3f44590a05eb815d97d5f3930c7d3e8a
Receiving role: the whole-change Implementation Agent for CRD HDE-CRD-0002, in its continuing session; create the PR instruction v1.0 for WORK_UNIT_ID WU-REM-02, the remediation of finding QA110-F01 (S20; QA Plan v1.2 check 13), under the approved overlay.
Change: HDE-CRD-0002 (CRD).

Inputs:
- docs/ephemeral/HDE-CRD-0002-remediation-review-QA110-F01-v1.0.md — REMEDIATION_REVIEW v1.0 (APPROVE_AS_CHANGED, change C-1): the approved overlay, verification and return
- docs/ephemeral/HDE-CRD-0002-remediation-QA110-F01-PF10-build-notes-addendum-v1.0.md — HDE Build Notes addendum 2.27 recording the approved delta (R-1 to R-6, V-1 to V-6, business case, WU-REM-02, C-1)
- docs/ephemeral/HDE-CRD-0002-remediation-proposal-QA110-F01-v1.0.md — REMEDIATION_PROPOSAL v1.0 (Thoth): diagnosis, rehearsals and the §6.3 prototype
- docs/ephemeral/HDE-CRD-0002-ESC10-qa-escalation-report-v1.0.md — originating finding QA110-F01 and its return point (§12)
- docs/ephemeral/HDE-CRD-0002-specification-v1.1-approved.md — SPECIFICATION_REF: approved Specification v1.1 (S20), with docs/ephemeral/HDE-CRD-0002-specification-delta-v1.0.md
- docs/ephemeral/HDE-CRD-0002-implementation-plan-v1.1.md — IMPLEMENTATION_PLAN_REF: approved Implementation Plan v1.1 (§7 WU-PR-06), with docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-v1.1.md
- docs/ephemeral/HDE-CRD-0002-implementation-plan-review-v1.1.md — PLAN_REVIEW_REF: IA-30 INITIAL_APPROVE, with docs/ephemeral/HDE-CRD-0002-implementation-plan-delta-01-review-v1.1.md (DELTA_APPROVE)
- docs/ephemeral/HDE-CRD-0002-WU-PR-06-pr-instruction-v1.0.md — WU-PR-06 instruction v1.0 (ID-2, §5.7, §5.8), the accepted-final unit this remedy repairs
- docs/ephemeral/HDE-CRD-0002-WU-REM-01-pr-instruction-v1.1.md — the prior remediation work-unit instruction (form precedent)
- docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md — HDE Build Notes in force, read with addendum 2.27 above

Minimum context: the review, addendum record and this handoff reach main through amthorn78/glow-hdengine-v2#731, which Nathan merges before PR-10 starts.
```

## Canon relied on

The handoff carries the decision of `docs/ephemeral/HDE-CRD-0002-remediation-review-QA110-F01-v1.0.md`, whose "Canon relied on" block is the full record. For the routing in this block:
- ESC-40 — Review and Return Approved Remediation — 100926.1, "Result routing" (a non-PR delivery owner takes its exact prompt from the approved return map), read in full;
- PR-10 — Create PR Work-Unit Instructions — 100926.1, "Inputs" (remediation lineage) and "Required result" (SPECIFICATION_REF, IMPLEMENTATION_PLAN_REF, PLAN_REVIEW_REF), read;
- PF19-Canon-Glow-QA-Guide v3.0.6 §10.6 "Common remediation cycle and return owner", step 4 (continuing IA delivers through the established PR lane), read in full;
- `docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md`, with the addendum 2.27 record named above.
