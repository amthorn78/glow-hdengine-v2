# R1 successor source matrix — 2026-09-23

Authority: D23-D, D23-F; Product Owner 2026-09-23. One block per changed row.
```json
{
  "id": "GCF-14",
  "partition": "CORE",
  "name": "Dedicated PR session creates the per-PR Implementation Plan",
  "change_class": "PR",
  "actor": "Dedicated PR session",
  "session": "One new work-unit session bound to one planned PR work unit; it must later implement that same unit.",
  "consumes": [
    "pr_instruction",
    "approved_implementation_plan_lineage",
    "current_repository",
    "pr_work_unit_lineage_review"
  ],
  "produces": [
    "per_pr_implementation_plan"
  ],
  "next": [
    "GCF-15"
  ],
  "approval_contract": "The PR session authors; the Product Owner later approves only by running Proceed.",
  "failure_stop_condition": "STOP_PR_INSTRUCTION_OR_REPOSITORY_CONFLICT, STOP_SCOPE_EXPANSION, or STOP_PLAN_INCOMPLETE; recovery owner: same PR session/IA for upstream scope.",
  "supersedes_source_row_sha256": "4f033c4b644dedc5589bcb3fb2a7bdec67e9ff457907f3733c101db2168f2767"
}
```
source_row_sha256: 42db7a9e614ecf943f042a9c012112fd3934f12e504cd4b980f404735b9cfe6b

```json
{
  "id": "GCF-17",
  "partition": "CORE",
  "name": "Dedicated PR session implements and creates PR lineage; PR-35 continues it in its own session",
  "change_class": "PR",
  "actor": "Dedicated PR session (PR-30 phase) and dedicated PR-35 session (PR-35 phase)",
  "session": "PR-30: exactly the GCF-14 planning session, continuing for implementation of its one authorized work unit. PR-35: its own dedicated top-level session for the same work unit and pull request, entered from PR-30's handoff; never a subagent of another session.",
  "consumes": [
    "per_pr_authorized_execution_state",
    "pr_implementation_proceed_invocation",
    "pr_instruction",
    "current_repository"
  ],
  "produces": [
    "pr_or_ordered_lineage",
    "implementation_result_evidence"
  ],
  "next": [
    "GCF-17.LINEAGE",
    "GCF-17.RESCOPE",
    "GCF-19",
    "GCF-20"
  ],
  "approval_contract": "Proceed already supplied PO runtime approval. Normal repository review/evidence follows; no new PO approval binding is created.",
  "failure_stop_condition": "STOP_SESSION_MISMATCH, STOP_SCOPE_CHANGE, STOP_REMOTE_INTEGRITY_DRIFT, or STOP_VALIDATION_FAILURE; recovery owner: the phase's own PR session/IA rescope.",
  "supersedes_source_row_sha256": "a2b761a9bf4328cbac51afd5312fcc13b55178ea5c52d6a213678396269e8043"
}
```
source_row_sha256: 6774529046ba5050b2e62b8cf01b024766c5e99d343d0fcfdd32b0367fb99602

```json
{
  "id": "GCF-17.LINEAGE",
  "partition": "MATERIAL_BRANCH_LOOP_OR_UTILITY",
  "name": "PR Work-Unit Lineage Review",
  "change_class": "PR",
  "actor": "Responsible PR review chain",
  "session": "Review context bound to one planned work unit and its complete ordered PR lineage.",
  "consumes": [
    "pr_instruction",
    "per_pr_implementation_plan",
    "pr_implementation_proceed_invocation",
    "pr_or_ordered_lineage",
    "implementation_result_evidence"
  ],
  "produces": [
    "pr_work_unit_lineage_review"
  ],
  "next": [
    "GCF-14",
    "GCF-19",
    "GCF-20"
  ],
  "approval_contract": "Review/acceptance is evidence-based and not a new Product Owner implementation approval.",
  "failure_stop_condition": "STOP_LINEAGE_INCOMPLETE, STOP_UNATTRIBUTABLE_CHANGE, or STOP_WORK_UNIT_NOT_TO_SPEC; recovery owner: a new top-level PR session Nathan creates for a re-plan (GCF-14), the reviewer, or IA.",
  "supersedes_source_row_sha256": "46e1c8d0a127afb4851f9945afd4f7d6c607e48936ea1206ef27ca9e8b1c2061"
}
```
source_row_sha256: 73a133c18b13682cbc57d813b37caacda7ed15b183437515867166bcda70e83e
