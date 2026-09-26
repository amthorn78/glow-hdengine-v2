# HDE-EPIC040-PR06a — Conditional PR-40 Handoff v1.0

Issued by the dedicated PR-35 session together with PR-35 result v1.1 (`MERGE_PENDING`, `docs/ephemeral/HDE-EPIC040-PR06a-pr-implementation-result-v1.1.md`).

- It is usable only after Nathan / Product Owner's actual manual merge of PR #508, and only where no `MERGE_OBSERVED` result was returned for that merge. Once a `MERGE_OBSERVED` handoff or this block has been pasted, the other is void.
- Result v1.1's `MERGE_PENDING` is historical pre-merge evidence. Nathan's later merge assertion authorizes only the read-only PR-40 review and is not proof of merged state. PR-40 independently verifies the actual merged state and landed lineage.
- It neither creates nor dispatches a session.

```text
NEXT_PROMPT_HANDOFF

Run PR-40 — Review PR Work-Unit Lineage — 091426.1:
https://app.notion.com/p/3db4590a05eb818786c5cb6051b4d634?pvs=204

Use this block only after Nathan / Product Owner has manually merged PR #508, and only if no MERGE_OBSERVED result was returned for that merge. PR-35's MERGE_PENDING (result v1.1) is historical pre-merge evidence; Nathan's merge assertion authorizes only this read-only review; verify the actual merged state and landed lineage independently.

Receiving role and session: the retained whole-change HDE-EPIC040 Implementation Architect, in its read-only PR-40 lineage-review role (plan v1.0 §15). Not a PR06a PR-20, PR-30 or PR-35 session.

session_disposition: RETAIN_EXISTING
invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR06a / PR-40
context_conflict: NONE
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC040
WORK_UNIT_ID: HDE-EPIC040-PR06a
PR_REFS: https://github.com/amthorn78/glow-hdengine-v2/pull/508 (the work unit's only pull request)
return_owner: the same retained whole-change HDE-EPIC040 Implementation Architect

Input artifacts, by repository path on main after the merge:
- docs/ephemeral/HDE-EPIC040-PR06a-pr-instruction-v1.0.md: PR_INSTRUCTION v1.0, INSTRUCTION_READY
- docs/ephemeral/HDE-EPIC040-PR06a-pr-implementation-plan-v1.0.md: PR_IMPLEMENTATION_PLAN v1.0, the object of the original PR-30 Proceed
- docs/ephemeral/HDE-EPIC040-PR06a-rescope-decision-v1.0.md: PR07-F01 decision adding PR06a
- docs/ephemeral/HDE-EPIC040-PR06a-PF10-build-notes-addendum-v1.0.md: the PR06a overlay as issued, drained as PF10 §2.23
- docs/ephemeral/HDE-EPIC040-PR06a-pr-implementation-result-v1.0.md: PR-30 result, PR_CANDIDATE_PUBLISHED (scope, in-flight decisions IF-01 to IF-07, PR-30 validation)
- docs/ephemeral/HDE-EPIC040-PR06a-pr-implementation-result-v1.1.md: PR-35 result, MERGE_PENDING (Codex findings CR-01 to CR-03, IF-08 and IF-09, re-cut, local validation, register)
- docs/ephemeral/HDE-EPIC040-PR06a-pr-remote-action-ledger-v1.1.md: remote-action ledger (v1.0 unchanged as issued)
- docs/ephemeral/HDE-EPIC040-PR06a-pr30-checkpoint-v1.0.md: PR-30 checkpoint
- docs/ephemeral/HDE-EPIC040-PR06a-pr35-checkpoint-v1.0.md: PR-35 checkpoint
- docs/ephemeral/HDE-EPIC040-specification-v1.1-approved.md: Specification v1.1, SPECIFICATION_APPROVED
- docs/ephemeral/HDE-EPIC040-implementation-audit-v2.0.md: Implementation Audit v2.0, AUDIT_COMPLETE
- docs/ephemeral/HDE-EPIC040-implementation-plan-v2.1.md: immutable whole-change Implementation Plan v2.1
- docs/ephemeral/HDE-EPIC040-implementation-plan-review-v2.1.md: Plan Review v2.1, Isis-50 APPROVE
- docs/ephemeral/HDE-EPIC040-PR06-pr-work-unit-lineage-review-v1.0.md: accepted predecessor PR06 (earlier predecessors as plan v1.0 §2.1 lists them)
- docs/pfcanon/PF10-HDE-Build-Notes-v13.3.4.md: current PF10, read only

Not recorded in those artifacts: the remote head read back after the PR-35 records push, the three thread replies and resolutions, and that head's CI run and Codex reviews are recorded in the PR #508 body.
```
