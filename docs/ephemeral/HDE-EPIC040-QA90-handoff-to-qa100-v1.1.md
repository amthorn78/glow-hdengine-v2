---
artifact_type: NEXT_PROMPT_HANDOFF
artifact_version: "1.1"
predecessor: none as a separate file (the QA-90 v1.0 handoff was a section of docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.0.md, not carried forward)
change_id: HDE-EPIC040
from: QA-90 — Create Bounded QA Execution Task — 091426.1 (Kronos-23)
result_ref: docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.1.md (TASK_READY)
---

```text
NEXT_PROMPT_HANDOFF
Destination: QA-100 — Execute Bounded QA Task — 091426.1
https://app.notion.com/p/3db4590a05eb811a8d13c0bbbf77a848
Receiving role and session: the authorized environment/operator session that the Product Owner opens for this collection in the Product Owner's QA console (the GitHub Codespace for amthorn78/glow-hdengine-v2), acting as the QA/infra executor of QA Plan v1.2; it is not Kronos.
Change: HDE-EPIC040 (Epic).

Inputs:
- docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.1.md — QA task collection v1.1 (TASK_READY): tasks T01 to T10 at attempt 1, delegation record, setup, rails, recording and evidence commit boundary
- docs/ephemeral/HDE-EPIC040-QA50-qa-plan-v1.2.md — approved QA Plan v1.2 (immutable base; checks 1 to 10 selected)
- docs/ephemeral/HDE-EPIC040-QA70-qa-plan-review-v1.4.md — QA-70 APPROVE of Plan v1.2, with execution notes N-101 to N-105
- docs/ephemeral/HDE-EPIC040-QA50-qa-audit-v1.0.md — Kronos QA Audit (loci)
- docs/ephemeral/HDE-EPIC040-QA90-checkpoint-v1.1.md — QA-90 working-state checkpoint
- docs/pfcanon/PF10-HDE-Build-Notes-v13.4.2.md — PF10 as read at QA-90
```

## Canon relied on

HDE Build Notes addendum 2.29 "PF10-CANON-001 — Repository PF-Canon Authority, Change-Process Document Storage and Canon Consultation": this handoff and the change documents it names are stored in `docs/ephemeral/`, and PF10 is named by its `docs/pfcanon/` path. The canon relied on for the tasks is recorded in the "Canon relied on" section of `docs/ephemeral/HDE-EPIC040-QA90-qa-task-collection-v1.1.md`.
