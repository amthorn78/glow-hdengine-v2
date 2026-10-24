---
artifact_type: NEXT_PROMPT_HANDOFF
artifact_version: "1.0"
predecessor: none
change_id: HDE-CRD-0002
from: QA-90 — Create Bounded QA Execution Task — 100926.1, Kronos (https://claude.ai/code/session_01PnD4YNbFZStRQWZ7TCM6jV)
result: TASK_READY
result_ref: docs/ephemeral/HDE-CRD-0002-QA90-qa-task-collection-v1.0.md
---

```text
NEXT_PROMPT_HANDOFF
Destination: QA-100 — Execute Bounded QA Task — 100926.1
https://app.notion.com/p/3f44590a05eb8182a201f0e177dad431
Receiving role: the executor the Product Owner chooses for CRD HDE-CRD-0002, under the Product Owner's execution arrangement; executes tasks T01 to T15 (QA Plan v1.2 checks 1 to 15), attempt 1 each, T01 first.
Change: HDE-CRD-0002 (CRD).

Inputs:
- docs/ephemeral/HDE-CRD-0002-QA90-qa-task-collection-v1.0.md — QA task collection v1.0 (TASK_READY): common contract §4, tasks T01 to T15 §5, normalizations NZ-01 to NZ-07, publication helper §4.7
- docs/ephemeral/HDE-CRD-0002-QA50-qa-plan-v1.2.md — approved QA Plan v1.2 (blob 66f6016cc75b), the immutable base
- docs/ephemeral/HDE-CRD-0002-QA70-qa-plan-review-v1.2.md — the APPROVE of v1.2, with operator cautions in §7
- docs/ephemeral/HDE-CRD-0002-QA50-qa-audit-v1.0.md — QA Audit v1.0 (AUDIT_COMPLETE)
- docs/ephemeral/HDE-CRD-0002-QA90-checkpoint-v1.0.md — QA-90 working-state checkpoint
- docs/pfcanon/PF10-HDE-Build-Notes-v13.7.8.md — HDE Build Notes in force

Minimum context: the collection and Plan v1.2 reach main together through amthorn78/glow-hdengine-v2#724, which Nathan merges before T01 runs. The executor, tools and venue, and whether an evidence-only commit grant applies, are recorded in none of these artifacts; Nathan supplies them with this handoff. Without a grant, the Product Owner commits the published evidence.
```
