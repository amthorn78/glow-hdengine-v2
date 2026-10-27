# R1 successor source matrix — 2026-10-27

Authority: D23-D, D23-F; Product Owner 2026-09-23. D23 successor of 2026-10-27 (PF06 §3.5.1; DN-2); Product Owner 2026-10-27. One block per row that differs from the historical R1 oracle; a row the historical oracle lacks supersedes null.
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

```json
{
  "id": "GCF-24",
  "partition": "CORE",
  "name": "Kronos creates the final QA Report and RCA",
  "change_class": "QA",
  "actor": "Kronos",
  "session": "Same continuing Kronos session that created the QA Audit/Plan and reviewed evidence.",
  "consumes": [
    "approved_qa_plan",
    "qa_task_evidence_history",
    "escalation_and_remediation_history_if_any"
  ],
  "produces": [
    "final_qa_report",
    "qa_rca"
  ],
  "next": [
    "GCF-24.CLOSE"
  ],
  "approval_contract": "Kronos authors; these are closure inputs, not the closure decision and not Product Owner approval.",
  "failure_stop_condition": "STOP_QA_PLAN_NOT_COMPLETE, STOP_REPORT_EVIDENCE_GAP, or STOP_RCA_MISSING; recovery owner: Kronos.",
  "supersedes_source_row_sha256": "271f99808be54154c12096d94532fc71b64bab586b545cdc6beb9934977e3bdc"
}
```
source_row_sha256: 66d4c41e3992a28f5550e1fd12865ac7a127de291d34f6dd676acc07a9ad2215

```json
{
  "id": "GCF-24.CLOSE",
  "partition": "MATERIAL_BRANCH_LOOP_OR_UTILITY",
  "name": "Close-mutation-set stage prepares and publishes the close mutation set",
  "change_class": "Closure prerequisite (PR work unit)",
  "actor": "Close Implementer (CL-05); the Product Owner invokes the stage and alone merges the close pull request",
  "session": "A standalone top-level session that the Product Owner starts with the stage prompt and the change ID; it needs no handoff to start, resolves its inputs from the change's records, and is never a subagent of another session.",
  "consumes": [
    "change_identity",
    "final_qa_report",
    "qa_rca",
    "isis_closure_decision",
    "current_repository",
    "applicable_canon"
  ],
  "produces": [
    "close_mutation_set",
    "close_mutation_set_result"
  ],
  "next": [
    "GCF-25"
  ],
  "approval_contract": "The Product Owner's invocation of the stage for a change authorizes that change's close mutation set and any close-tooling repair it needs, and is the Proceed for both. The closure authority judges its result at the closure decision; the Product Owner alone merges. It never reopens implementation, QA or the closure decision.",
  "failure_stop_condition": "STOP_CLOSE_INTAKE_FAILED, STOP_APPROVED_QA_EVIDENCE_WOULD_CHANGE, STOP_DEFECT_OUTSIDE_CLOSE_TOOLING, STOP_CLOSE_RUN_FAMILY_NOT_ADMITTED or STOP_CANON_CONFLICT; recovery owner: the Close Implementer for close-tooling repair, with no escalation, rescope or PR-chain stage; otherwise the Product Owner.",
  "supersedes_source_row_sha256": null
}
```
source_row_sha256: 9c0f70693dc21f0cbaef27c7804e645f33858d30fc52b89ae57854f7e2177453

```json
{
  "id": "GCF-25",
  "partition": "CORE",
  "name": "Isis performs terminal retrospective and decides closure",
  "change_class": "Closure",
  "actor": "Isis",
  "session": "Continuing Isis Lead Developer session for the change.",
  "consumes": [
    "approved_specification_ia_intake",
    "approved_change_wide_implementation_plan",
    "complete_work_unit_results",
    "final_qa_report",
    "qa_rca",
    "close_mutation_set",
    "close_mutation_set_result",
    "outstanding_blocker_ledger"
  ],
  "produces": [
    "isis_closure_decision",
    "terminal_retrospective"
  ],
  "next": [
    "GCF-24.CLOSE",
    "GCF-26",
    "REENTER_EXACT_OWNER"
  ],
  "approval_contract": "Isis alone owns the terminal closure decision. Product Owner, IA, Kronos, QA PASS, or a memo does not substitute.",
  "failure_stop_condition": "STOP_CLOSURE_EVIDENCE_INCOMPLETE or CLOSE_DENIED_WITH_EXACT_OWNER_AND_REENTRY; recovery owner: Isis/named stage owner, and the close-mutation-set stage (GCF-24.CLOSE) when the return work is a missing, incomplete or defective close mutation set, a close-tooling defect included.",
  "supersedes_source_row_sha256": "2a59e2a5e135f2e7ef8a47318b7abd42190c118fa43649fe9756b27346a1964a"
}
```
source_row_sha256: 1b2ab0339aed2a04aff404864a1699605eb3904780c7e3b3ca25881c74ed5ee3
