---
artifact_type: NEXT_PROMPT_HANDOFF
artifact_version: "1.0"
predecessor: none
change_id: HDE-EPIC041
from: QA-90 — Create Bounded QA Execution Task — 102726.1, continuing Kronos (QA authority for HDE-EPIC041)
decision_ref: docs/ephemeral/HDE-EPIC041-QA90-qa-tasks-v1.0.md (TASK_READY; QA_STEP_IDS ALL; seven tasks, attempt 1)
---

```text
NEXT_PROMPT_HANDOFF
Destination: QA-100 — Execute Bounded QA Task — 102726.1
URL: https://app.notion.com/p/4064590a05eb8150bcfff1e25129b368
Receiver: the executing operator the Product Owner chooses (PI-01), for HDE-EPIC041 (Separation Pass 4)
Task: execute bounded QA tasks T-01 to T-07 (attempt 1) under closed rails SAFE_MODE=1, ALLOW_NETWORK=0, APP_ENV=dev, LC_ALL=C, LANG=C, TZ=UTC, then the dependency-waiting publication actions P-IDX-RUN and P-EL-01 when their dependencies are met
Inputs:
- docs/ephemeral/HDE-EPIC041-QA90-qa-tasks-v1.0.md — QA task collection v1.0 (TASK_READY): tasks, rails, setup, publication, cautions, return to QA-110
- docs/ephemeral/HDE-EPIC041-QA50-qa-plan-v1.0.md — approved QA Plan v1.0 (immutable base; source of scripts SC-D0, SC-0B, SC-05, SC-CL)
- docs/ephemeral/HDE-EPIC041-QA70-qa-plan-review-v1.0.md — QA-70 APPROVE; notes N-01 to N-14
- docs/ephemeral/HDE-EPIC041-QA50-qa-audit-v1.0.md — QA Audit v1.0; locus provenance
Not yet decided: PI-01 to PI-03 (Product Owner). P-IDX-RUN waits on IDX-01 (PI-02); P-EL-01 waits on PI-02, PI-03 and Nathan's commit instruction in the executing session.
Precondition: this collection and handoff are on main; Nathan merges their pull request first.
```
