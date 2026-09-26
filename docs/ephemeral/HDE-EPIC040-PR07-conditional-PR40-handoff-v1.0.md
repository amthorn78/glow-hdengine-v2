# HDE-EPIC040-PR07 — Conditional PR-40 Handoff v1.0

This handoff is issued by the dedicated PR-35 session together with PR-35 result v1.1 (`MERGE_PENDING`, `docs/ephemeral/HDE-EPIC040-PR07-pr-implementation-result-v1.1.md`).

- **When it may be used.** Only after Nathan / Product Owner has actually merged PR #518 manually, and only if no `MERGE_OBSERVED` result was returned for that merge. Once a `MERGE_OBSERVED` handoff or this block has been pasted, the other is void.
- **What the earlier result proves.** Result v1.1's `MERGE_PENDING` is historical pre-merge evidence. Nathan's later merge assertion authorizes only the read-only PR-40 review and is not proof of merged state. PR-40 independently verifies the actual merged state and landed lineage.
- **Sessions.** It neither creates nor dispatches a session.

```text
NEXT_PROMPT_HANDOFF

Run PR-40 — Review PR Work-Unit Lineage — 091426.1:
https://app.notion.com/p/3db4590a05eb818786c5cb6051b4d634?pvs=204

Use this block only after Nathan / Product Owner has manually merged PR #518, and only if no MERGE_OBSERVED result was returned for that merge. PR-35's MERGE_PENDING (result v1.1) is historical pre-merge evidence; Nathan's merge assertion authorizes only this read-only review; verify the actual merged state and landed lineage independently.

Receiving role and session: the retained whole-change HDE-EPIC040 Implementation Architect, in its read-only PR-40 lineage-review role (plan v1.0 §15). Not a PR07 PR-20, PR-30 or PR-35 session.

session_disposition: RETAIN_EXISTING
invocation_binding: HDE-EPIC040 / HDE-EPIC040-PR07 / PR-40
context_conflict: NONE
CHANGE_CLASS: EPIC
CHANGE_ID: HDE-EPIC040
WORK_UNIT_ID: HDE-EPIC040-PR07
PR_REFS: https://github.com/amthorn78/glow-hdengine-v2/pull/518 (the work unit's only pull request)
return_owner: the same retained whole-change HDE-EPIC040 Implementation Architect

Input artifacts, by repository path on main after the merge:
- docs/ephemeral/HDE-EPIC040-PR07-pr-instruction-v1.0.md: PR_INSTRUCTION v1.0, INSTRUCTION_READY
- docs/ephemeral/HDE-EPIC040-PR07-pr-implementation-plan-v1.0.md: PR_IMPLEMENTATION_PLAN v1.0, the object of the original PR-30 Proceed
- docs/ephemeral/HDE-EPIC040-PR07-pr-implementation-result-v1.0.md: PR-30 result, PR_CANDIDATE_PUBLISHED (implementation, proofs P-01 to P-15, in-flight decisions IFD-01 to IFD-03, observations O-P07-01 to O-P07-09)
- docs/ephemeral/HDE-EPIC040-PR07-pr-implementation-result-v1.1.md: PR-35 result, MERGE_PENDING (entry checkpoint, reviews and CI, PR-35 local re-verification, ledger, readiness, final-head condition)
- docs/ephemeral/HDE-EPIC040-specification-v1.1-approved.md: Specification v1.1, SPECIFICATION_APPROVED
- docs/ephemeral/HDE-EPIC040-implementation-audit-v2.0.md: Implementation Audit v2.0, AUDIT_COMPLETE
- docs/ephemeral/HDE-EPIC040-implementation-plan-v2.1.md: immutable whole-change Implementation Plan v2.1 (§6.7 is PR07)
- docs/ephemeral/HDE-EPIC040-implementation-plan-review-v2.1.md: Plan Review v2.1, Isis-50 APPROVE
- docs/ephemeral/HDE-EPIC040-PR06a-PF10-build-notes-addendum-v1.0.md: the PR06a overlay as issued, drained as PF10 §2.23
- docs/ephemeral/HDE-EPIC040-PR06b-PF10-build-notes-addendum-v1.0.md: the PR06b overlay as issued, drained as PF10 §2.25
- docs/ephemeral/HDE-EPIC040-PR06b-pr-work-unit-lineage-review-v1.0.md: accepted predecessor PR06b (earlier predecessors as plan v1.0 §2.1 lists them)
- docs/pfcanon/PF10-HDE-Build-Notes-v13.3.7.md: current PF10, read only

Not recorded in those artifacts: the remote head read back after the PR-35 records push, that head's CI run, any Codex activity on it and its mergeability are recorded in the PR #518 body.
```
