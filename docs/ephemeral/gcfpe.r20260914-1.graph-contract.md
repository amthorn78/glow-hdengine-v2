# GCFPE-20260914.1 Candidate Graph Contract

```yaml
artifact_type: GCFPE_CANDIDATE_GRAPH_CONTRACT
release: GCFPE-20260914.1
prompt_version_family: '091426.1'
selection_status: UNSELECTED_CANDIDATE
complete_source_path: candidate/graph/GCFPE-20260914.1-Candidate-Graph-Contract.json
complete_source_bytes: 569396
complete_source_sha256: 6b5211f3ea51aa1e2ecfa178e243e9821ab15cad625de6424bcae603bf563ea6
content_status: COMPLETE
source_binding_revision: 20260915.5-batch-1-targeted-correction
validation_scope: TARGETED_AUTHOR_SELF_REVIEW_PENDING_INDEPENDENT_POSTFLIGHT_REQUIRED
```

```json
{
  "abort_contract": {
    "agent_skill_prompt_hub_inbound_edges": 0,
    "automatic_inbound_edges": 0,
    "identified_pr_required": true,
    "manual_invoker": "Nathan / Product Owner",
    "prompt": "PR-50",
    "prompt_inbound_edges": 0
  },
  "alpha_resumption_contract": {
    "current_handoff_status": "NOT_YET_APPROVED",
    "execute_pr10": false,
    "last_accepted_state": "ACCEPTED_FINAL",
    "last_accepted_unit": "HDE-EPIC040-PR03",
    "next_intended_stage": "PR-10",
    "next_intended_unit": "HDE-EPIC040-PR04",
    "preparation_prerequisites": [
      "successor selected",
      "production validation passed",
      "predecessors archived intact",
      "selected release and Alpha record reread",
      "PR03 acceptance reread",
      "current controlled PF10 Markdown reread",
      "every applicable active addendum reread",
      "handoff saved and completely read back in Glow / Ephemeral Planning Files"
    ],
    "prepare_only": true,
    "resume_alpha": false,
    "resume_authority": "Nathan / Product Owner",
    "state": "ALPHA_STOPPED_PENDING_CHANGE_FLOW_REFACTOR"
  },
  "artifact_availability_contract": {
    "formation_has_no_approved_implementation_plan_prerequisite": true,
    "initial_implementation_planning_has_no_own_approved_plan_prerequisite": true,
    "later_remediation_to_pr": "Bounded approved remedy plus actual originating finding/reference and return owner. Existing QA evidence, including a Guide, may be read when specifically relevant and travels with the remedy when it depends on that evidence; no future QA artifact or blanket QA prerequisite, approved PR base or QA authority is introduced.",
    "pr_local_tests_and_code_security_reviews_required": true,
    "pr_qa_artifact_prerequisites": [],
    "pr_work_products": [
      "PR_INSTRUCTION",
      "PR_IMPLEMENTATION_PLAN",
      "PR_IMPLEMENTATION_RESULT",
      "PR_WORK_UNIT_LINEAGE_REVIEW",
      "PR_ABORT_ESCALATION_RECORD",
      "RESCOPE_REQUEST"
    ],
    "pre_readiness_remediation_requires_future_qa_artifacts": false,
    "preservation_rule": "Protect only existing applicable bases; immutability does not require absent artifacts or invent approval.",
    "protected_native_graph_changes": false,
    "qa_artifact_births": {
      "LIVE_QA_GUIDE": {
        "after": "READY_FOR_QA",
        "producer": "QA-20",
        "separate_approval_required": false,
        "state": "GUIDE_READY"
      },
      "QA_AUDIT": {
        "after": "GUIDE_READY",
        "producer": "QA-50",
        "state": "AUDIT_COMPLETE"
      },
      "QA_EVIDENCE_REVIEW": {
        "after": "MATCHED_TASK_AND_ACTUAL_RESULT",
        "producer": "QA-110"
      },
      "QA_EXECUTION_RESULT": {
        "after": "AUTHORIZED_DEPENDENCY_READY_SELECTED_TASK",
        "producer": "QA-100"
      },
      "QA_PLAN": {
        "after": "COMPLETE_QA_AUDIT",
        "approval_owner": "QA-70",
        "plan_only_recovery_producer": "QA-60",
        "producer": "QA-50",
        "state": "PLAN_PENDING"
      },
      "QA_PLAN_REVIEW": {
        "after": "COMPLETE_PENDING_QA_PLAN_OR_EXPLICIT_APPROVED_BASE_DELTA",
        "producer": "QA-70"
      },
      "QA_READINESS": {
        "after": "ACCEPTED_IMPLEMENTATION_OPS_AND_FINAL_DOCUMENTATION",
        "producer": "QA-10",
        "state": "READY_FOR_QA"
      },
      "QA_REPORT_AND_SEPARATE_RCA": {
        "after": "COMPLETE_REQUIRED_RUN_ACCOUNTING",
        "closure_owner": "CLASS_MATCHING_ISIS_RECEIVER",
        "producer": "QA-120"
      },
      "QA_TASK": {
        "after": "APPROVED_QA_PLAN_AND_PRODUCT_OWNER_SELECTION",
        "producer": "QA-90"
      }
    },
    "qa_guide_authoring_has_no_qa_plan_prerequisite": true,
    "readiness_has_no_qa_guide_or_qa_plan_prerequisite": true,
    "recovery_rule": "Reuse only a complete valid actual result with unchanged relevant lineage; preserve unproduced future fields.",
    "remediation_artifact_identity": {
      "legacy_alias_rule": "Preserve actual existing REMEDIATION_PLAN/REMEDIATION_PLAN_REVIEW identity only with equivalent semantics and exact lineage; no duplicate artifact or approval.",
      "proposal": "REMEDIATION_PROPOSAL",
      "review": "REMEDIATION_REVIEW"
    },
    "required_input_rule": "Actual native stage and branch; producer completion and required approval must precede consumption on that lineage.",
    "role": "VALIDATION_METADATA_NOT_AN_ADDITIONAL_RUNTIME_INPUT_OR_GATE",
    "schema_version": "gcfpe-artifact-availability/1.0",
    "stage_categories": {
      "CF-C-10": "FORMATION",
      "CF-C-20": "FORMATION",
      "CF-C-30": "FORMATION",
      "CF-C-40": "FORMATION",
      "CF-E-10": "FORMATION",
      "CF-E-20": "FORMATION",
      "CF-E-30": "FORMATION",
      "CF-E-40": "FORMATION",
      "CF-PO-10": "FORMATION",
      "CL-20": "POST_CLOSURE",
      "CL-30": "POST_CLOSURE",
      "CL-40": "POST_CLOSURE",
      "CL-C-10": "CLOSURE",
      "CL-E-10": "CLOSURE",
      "CL-E-20": "POST_CLOSURE",
      "CL-E-30": "POST_CLOSURE",
      "CL-E-40": "POST_CLOSURE",
      "DOC-10": "ORIGIN_SCOPED_DELIVERY",
      "DOC-20": "ORIGIN_SCOPED_DELIVERY",
      "ESC-10": "QA_EXECUTION_EVIDENCE",
      "ESC-25": "ORIGIN_SCOPED_REMEDIATION",
      "ESC-30": "ORIGIN_SCOPED_REMEDIATION",
      "ESC-40": "ORIGIN_SCOPED_REMEDIATION",
      "GCFPE-MGMT-10": "CONTEXT_SCOPED",
      "IA-10": "IMPLEMENTATION_PLANNING",
      "IA-20": "IMPLEMENTATION_PLANNING",
      "IA-30": "IMPLEMENTATION_PLANNING",
      "IA-40": "IMPLEMENTATION_PLANNING",
      "IA-50": "IMPLEMENTATION_PLANNING",
      "IA-60": "IMPLEMENTATION_PLANNING",
      "MGR-10": "CONTEXT_SCOPED",
      "OPS-10": "ORIGIN_SCOPED_DELIVERY",
      "OPS-20": "ORIGIN_SCOPED_DELIVERY",
      "OPS-30": "ORIGIN_SCOPED_DELIVERY",
      "PR-10": "PR_DELIVERY",
      "PR-20": "PR_DELIVERY",
      "PR-30": "PR_DELIVERY",
      "PR-35": "PR_DELIVERY",
      "PR-40": "PR_DELIVERY",
      "PR-50": "PR_DELIVERY",
      "QA-10": "READINESS",
      "QA-100": "QA_EXECUTION_EVIDENCE",
      "QA-110": "QA_EXECUTION_EVIDENCE",
      "QA-120": "QA_EXECUTION_EVIDENCE",
      "QA-20": "GUIDE_AUTHORING",
      "QA-50": "QA_PLANNING",
      "QA-60": "QA_PLANNING",
      "QA-70": "QA_REVIEW",
      "QA-80": "QA_REVIEW",
      "QA-90": "QA_EXECUTION_EVIDENCE",
      "RS-10": "ORIGIN_SCOPED_DELIVERY",
      "RS-20": "ORIGIN_SCOPED_DELIVERY",
      "RS-30": "ORIGIN_SCOPED_DELIVERY",
      "RS-40": "ORIGIN_SCOPED_DELIVERY",
      "UTIL-10": "CONTEXT_SCOPED"
    }
  },
  "authority_sources": [
    "recovery-20260914.1/sources/drive/1QfCDo6pw3_FRjJi5qTooLaxgLThFcURI-repin.md §§5–8",
    "candidate/contracts/GCFPE-20260914.1-Candidate-Authoring-Contract.md",
    "baseline/preflight/project-prompt-registry.yaml"
  ],
  "baseline": {
    "member_count": 54,
    "registry": "baseline/preflight/project-prompt-registry.yaml",
    "release": "GCFPE-20260913.1",
    "version_family": "091326.2"
  },
  "boundary_nodes": {
    "ACTUAL_OWNER_TERMINAL_RETURN": {
      "kind": "native_owner_terminal_sink",
      "selected_member": false
    },
    "NATHAN_ABORT_INSTRUCTION": {
      "kind": "manual_product_owner_invocation",
      "selected_member": false
    },
    "NATHAN_MANUAL_MERGE_ASSERTION": {
      "kind": "manual_product_owner_event",
      "selected_member": false
    },
    "NATHAN_MANUAL_PF10_DRAIN": {
      "kind": "manual_product_owner_event",
      "selected_member": false
    },
    "NATHAN_PROCEED": {
      "kind": "manual_product_owner_gate",
      "selected_member": false
    },
    "NATHAN_TERMINAL_RETURN": {
      "kind": "human_terminal_sink",
      "selected_member": false
    },
    "ORIGINAL_NATIVE_STAGE": {
      "kind": "dynamic_native_owner_boundary",
      "selected_member": false
    }
  },
  "boundary_transitions": {
    "NATHAN_ABORT_INSTRUCTION": [
      {
        "branch_id": "nathan_abort",
        "condition": "Nathan directly instructs Abort PR and Escalate for one exact identified PR",
        "origin_prompt": "NATHAN_DIRECT_ONLY",
        "origin_state": "IDENTIFIED_PR",
        "to": "PR-50"
      }
    ],
    "NATHAN_MANUAL_MERGE_ASSERTION": [
      {
        "branch_id": "manual_merge_then_lineage_review",
        "condition": "Nathan has manually merged the identified PR and invokes the conditional PR-40 block",
        "origin_prompt": "PR-35_OR_RS-40",
        "origin_state": "MERGE_PENDING",
        "to": "PR-40"
      }
    ],
    "NATHAN_MANUAL_PF10_DRAIN": [
      {
        "branch_id": "crd_specification_delta_return",
        "condition": "the exact affected native receiver recorded by the approved CRD Specification delta freshly verifies current PF10; this is not an RS-40 rescope route",
        "origin_prompt": "CF-C-30",
        "origin_state": "DELTA_APPROVE",
        "to": "ORIGINAL_NATIVE_STAGE"
      },
      {
        "branch_id": "epic_specification_delta_return",
        "condition": "the exact affected native receiver recorded by the approved Epic Specification delta freshly verifies current PF10; this is not an RS-40 rescope route",
        "origin_prompt": "CF-E-30",
        "origin_state": "DELTA_APPROVE",
        "to": "ORIGINAL_NATIVE_STAGE"
      },
      {
        "branch_id": "plan_delta_return",
        "condition": "REVIEW_MODE=MATERIAL_DELTA; the exact return_phase receiver freshly verifies current PF10",
        "origin_prompt": "IA-30",
        "origin_state": "APPROVE",
        "to": "ORIGINAL_NATIVE_STAGE"
      },
      {
        "branch_id": "qa_plan_delta_return",
        "condition": "REVIEW_MODE=DELTA; the exact native receiver freshly verifies current PF10",
        "origin_prompt": "QA-70",
        "origin_state": "APPROVE",
        "to": "ORIGINAL_NATIVE_STAGE"
      },
      {
        "branch_id": "remediation_pr30_return",
        "condition": "recorded remediation return is PR-30_PREPUBLICATION or PR-30_POSTPUBLICATION; resume PR-30 directly after fresh verification, preserving actual vehicle state",
        "origin_prompt": "ESC-40",
        "origin_state": "APPROVE_OR_APPROVE_AS_CHANGED",
        "to": "PR-30"
      },
      {
        "branch_id": "remediation_pr35_return",
        "condition": "recorded remediation return is PR-35; resume PR-35 directly after fresh verification in the same open PR",
        "origin_prompt": "ESC-40",
        "origin_state": "APPROVE_OR_APPROVE_AS_CHANGED",
        "to": "PR-35"
      },
      {
        "branch_id": "remediation_non_pr_return",
        "condition": "recorded remediation return is a non-PR native delivery owner; that receiver freshly verifies current PF10",
        "origin_prompt": "ESC-40",
        "origin_state": "APPROVE_OR_APPROVE_AS_CHANGED",
        "to": "ORIGINAL_NATIVE_STAGE"
      },
      {
        "branch_id": "rescope_pr30_prepublication",
        "condition": "PR_RETURN_PHASE=PR-30_PREPUBLICATION; PR-30 freshly verifies current PF10; no open PR and RS-40 forbidden",
        "origin_prompt": "RS-20",
        "origin_state": "APPROVE",
        "to": "PR-30"
      },
      {
        "branch_id": "rescope_open_pr",
        "condition": "PR_RETURN_PHASE in {PR-30_POSTPUBLICATION, PR-35}; existing open PR identity verified",
        "origin_prompt": "RS-20",
        "origin_state": "APPROVE",
        "to": "RS-40"
      },
      {
        "branch_id": "rescope_non_pr",
        "condition": "qualifying non-PR bounded rescope; exact native stage freshly verifies current PF10",
        "origin_prompt": "RS-20",
        "origin_state": "APPROVE",
        "to": "ORIGINAL_NATIVE_STAGE"
      }
    ],
    "NATHAN_PROCEED": [
      {
        "branch_id": "original_proceed",
        "condition": "original explicit Proceed for the exact work unit; never a second Proceed",
        "origin_prompt": "PR-20",
        "origin_state": "AWAITING_PO_PROCEED",
        "to": "PR-30"
      }
    ]
  },
  "candidate": {
    "member_count": 55,
    "member_rule": "54 selected predecessors + PR-35; no removals",
    "release": "GCFPE-20260914.1",
    "version_family": "091426.1"
  },
  "candidate_member_count_excludes_boundaries": true,
  "canonical_source_contract": {
    "forbidden_source_types": [
      "GOOGLE_DOCS",
      "DOC",
      "DOCX"
    ],
    "fresh_current_pf10_resolution_required_after_manual_drain": true,
    "google_docs_fallback": false,
    "native_document_candidate_content_may_be_opened": false,
    "native_document_equivalence_check": false,
    "pfcanon_authority": "CONTROLLED_MARKDOWN_ONLY",
    "pre_drain_reference_role": "PRE_DRAIN_BASELINE_EVIDENCE",
    "source_failure_result": "SOURCE_RESOLUTION_ERROR"
  },
  "contract_id": "GCFPE-20260914.1-CANDIDATE-GRAPH",
  "edges": [
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-C-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "material_source_omission_recovery",
          "condition": "material source omission is repairable by the same kickoff owner",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-C-10.md",
            "section": "Required result and routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "BLOCKED"
      ],
      "to": "CF-C-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-C-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "KICKOFF_READY"
          ],
          "branch_id": "kickoff_ready",
          "condition": "valid CRD class selection and complete sanitized source",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-C-10.md",
            "section": "Required result and routing"
          },
          "state": "KICKOFF_READY",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "KICKOFF_READY"
      ],
      "to": "CF-C-20",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-C-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "class_or_identity_recovery",
          "condition": "CRD selection record or change identity is missing or conflicting; CF-PO-10 records exact existing evidence or requests Nathan's decision and never chooses the class",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-C-10.md",
            "section": "Required result and routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "BLOCKED"
      ],
      "to": "CF-PO-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-C-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "kickoff_terminal",
          "condition": "the Product Owner decision itself remains unavailable or another true authority/source stop has no runnable prompt receiver",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-C-10.md",
            "section": "Required result and routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "BLOCKED"
      ],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-C-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "invalid_kickoff_recovery",
          "condition": "kickoff is incomplete or contradictory and the kickoff owner can correct it",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-C-20.md",
            "section": "Required result and routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "BLOCKED"
      ],
      "to": "CF-C-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-C-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "SPECIFICATION_PENDING"
          ],
          "branch_id": "specification_pending",
          "condition": "complete pending CRD Specification is ready for Thoth review",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-C-20.md",
            "section": "Required result and routing"
          },
          "state": "SPECIFICATION_PENDING",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "SPECIFICATION_PENDING"
      ],
      "to": "CF-C-30",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-C-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "specification_authoring_terminal",
          "condition": "unrecoverable source, identity, or authority blocker",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-C-20.md",
            "section": "Required result and routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "BLOCKED"
      ],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-C-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "INITIAL_DENY"
          ],
          "branch_id": "initial_deny",
          "condition": "initial denial returns exact redlines to the same Isis author; no addendum",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-C-30.md",
            "section": "Required result and routing"
          },
          "state": "INITIAL_DENY",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "CORRECTION_REDLINE"
          ],
          "branch_id": "approved_base_correction_redline",
          "condition": "approved immutable CRD base plus a source-backed factual finding or actual authorized product/scope decision is assessed as justified; exact Thoth correction redline goes to the same Isis author for the first standalone pending delta; no approval or PF10 addendum",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-C-30.md",
            "section": "Required result and routing"
          },
          "state": "CORRECTION_REDLINE",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "DELTA_DENY"
          ],
          "branch_id": "delta_deny",
          "condition": "return bounded delta redlines to the same Specification author; no addendum",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-C-30.md",
            "section": "Required result and routing"
          },
          "state": "DELTA_DENY",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "INITIAL_DENY",
        "DELTA_DENY",
        "CORRECTION_REDLINE"
      ],
      "to": "CF-C-40",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-C-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "INITIAL_APPROVE"
          ],
          "branch_id": "initial_approve",
          "condition": "initial approval; no addendum",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-C-30.md",
            "section": "Required result and routing"
          },
          "state": "INITIAL_APPROVE",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "INITIAL_APPROVE"
      ],
      "to": "IA-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-C-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "DELTA_APPROVE"
          ],
          "branch_id": "delta_approve",
          "condition": "material delta to an already approved base; exactly one addendum; reuse an existing read-back artifact for the same stable addendum_id and approved-delta digest; never duplicate; terminal for this invocation pending Nathan manual drain",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-C-30.md",
            "section": "Required result and routing"
          },
          "state": "DELTA_APPROVE",
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "DELTA_APPROVE"
      ],
      "to": "NATHAN_MANUAL_PF10_DRAIN",
      "to_kind": "boundary",
      "transport": "MANUAL_PRODUCT_OWNER_BOUNDARY"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-C-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [],
          "branch_id": "review_terminal",
          "condition": "missing source, authority, or review mode",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-C-30.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": true
        },
        {
          "applicable_states": [],
          "branch_id": "correction_not_substantiated_terminal",
          "condition": "source-backed factual finding is assessed as unsupported; immutable approved base remains unchanged and no delta, denial, approval, or PF10 addendum is produced",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-C-30.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": true
        },
        {
          "applicable_states": [],
          "branch_id": "product_scope_decision_required_terminal",
          "condition": "the requested correction requires an unresolved genuine product-intent or scope choice; return the exact decision required to Nathan without disguising it as a factual correction",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-C-30.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-C-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "SPECIFICATION_PENDING"
          ],
          "branch_id": "preapproval_revision",
          "condition": "pending preapproval CRD Specification corrected under the exact redline",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-C-40.md",
            "section": "Required result and routing"
          },
          "state": "SPECIFICATION_PENDING",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "SPECIFICATION_PENDING"
          ],
          "branch_id": "approved_base_first_delta_authoring",
          "condition": "first standalone CRD Specification delta authored from the exact Thoth correction assessment/redline; immutable approved base unchanged; return to the same Thoth reviewer for approved-base delta review",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-C-40.md",
            "section": "Required result and routing"
          },
          "state": "SPECIFICATION_PENDING",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "SPECIFICATION_PENDING"
          ],
          "branch_id": "approved_base_delta_revision",
          "condition": "pending bounded approved-base SPECIFICATION_DELTA corrected without rewriting the approved base",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-C-40.md",
            "section": "Required result and routing"
          },
          "state": "SPECIFICATION_PENDING",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "SPECIFICATION_PENDING"
      ],
      "to": "CF-C-30",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-C-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [],
          "branch_id": "revision_terminal",
          "condition": "the redline or authority owner cannot be resolved",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-C-40.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-C-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [],
          "branch_id": "redline_owner_recovery",
          "condition": "missing or contradictory redline/authority has an exact evidenced native owner",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "CONDITIONAL_RECOVERY",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-C-40.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [],
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "COMPLETE_DYNAMIC_NATIVE_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-E-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "wrong_class_crd",
          "condition": "the supplied Product Owner class is CRD",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-E-10.md",
            "section": "Required result and routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "BLOCKED"
      ],
      "to": "CF-C-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-E-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "material_source_omission_recovery",
          "condition": "material source omission is repairable by the same kickoff owner",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-E-10.md",
            "section": "Required result and routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "BLOCKED"
      ],
      "to": "CF-E-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-E-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "KICKOFF_READY"
          ],
          "branch_id": "kickoff_ready",
          "condition": "valid Epic class selection and complete sanitized source",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-E-10.md",
            "section": "Required result and routing"
          },
          "state": "KICKOFF_READY",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "KICKOFF_READY"
      ],
      "to": "CF-E-20",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-E-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "class_selection_recovery",
          "condition": "Epic selection record or change identity is missing or conflicting; CF-PO-10 records exact existing evidence or requests Nathan's decision and never chooses the class",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-E-10.md",
            "section": "Required result and routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "BLOCKED"
      ],
      "to": "CF-PO-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-E-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "kickoff_terminal",
          "condition": "another true Product Owner/source/authority stop has no runnable receiver",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-E-10.md",
            "section": "Required result and routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "BLOCKED"
      ],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-E-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "invalid_kickoff_recovery",
          "condition": "kickoff is incomplete, defective, or contradictory and the kickoff owner can correct it",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-E-20.md",
            "section": "Required result and routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "BLOCKED"
      ],
      "to": "CF-E-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-E-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "SPECIFICATION_PENDING"
          ],
          "branch_id": "specification_pending",
          "condition": "complete pending Epic Specification is ready for Thoth review",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-E-20.md",
            "section": "Required result and routing"
          },
          "state": "SPECIFICATION_PENDING",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "SPECIFICATION_PENDING"
      ],
      "to": "CF-E-30",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-E-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "specification_authoring_terminal",
          "condition": "unrecoverable source, identity, or authority blocker",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-E-20.md",
            "section": "Required result and routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "BLOCKED"
      ],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-E-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "INITIAL_DENY"
          ],
          "branch_id": "initial_deny",
          "condition": "initial denial returns exact redlines to the same Isis author; no addendum",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-E-30.md",
            "section": "Required result and routing"
          },
          "state": "INITIAL_DENY",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "CORRECTION_REDLINE"
          ],
          "branch_id": "approved_base_correction_redline",
          "condition": "approved immutable Epic base plus a source-backed factual finding or actual authorized product/scope decision is assessed as justified; exact Thoth correction redline goes to the same Isis author for the first standalone pending delta; no approval or PF10 addendum",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-E-30.md",
            "section": "Required result and routing"
          },
          "state": "CORRECTION_REDLINE",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "DELTA_DENY"
          ],
          "branch_id": "delta_deny",
          "condition": "return bounded delta redlines to the same Specification author; no addendum",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-E-30.md",
            "section": "Required result and routing"
          },
          "state": "DELTA_DENY",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "INITIAL_DENY",
        "DELTA_DENY",
        "CORRECTION_REDLINE"
      ],
      "to": "CF-E-40",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-E-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "INITIAL_APPROVE"
          ],
          "branch_id": "initial_approve",
          "condition": "initial approval; no addendum",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-E-30.md",
            "section": "Required result and routing"
          },
          "state": "INITIAL_APPROVE",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "INITIAL_APPROVE"
      ],
      "to": "IA-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-E-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "DELTA_APPROVE"
          ],
          "branch_id": "delta_approve",
          "condition": "material delta to an already approved base; exactly one addendum; reuse an existing read-back artifact for the same stable addendum_id and approved-delta digest; never duplicate; terminal for this invocation pending Nathan manual drain",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-E-30.md",
            "section": "Required result and routing"
          },
          "state": "DELTA_APPROVE",
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "DELTA_APPROVE"
      ],
      "to": "NATHAN_MANUAL_PF10_DRAIN",
      "to_kind": "boundary",
      "transport": "MANUAL_PRODUCT_OWNER_BOUNDARY"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-E-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [],
          "branch_id": "review_terminal",
          "condition": "missing source, authority, or review mode",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-E-30.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": true
        },
        {
          "applicable_states": [],
          "branch_id": "correction_not_substantiated_terminal",
          "condition": "source-backed factual finding is assessed as unsupported; immutable approved base remains unchanged and no delta, denial, approval, or PF10 addendum is produced",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-E-30.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": true
        },
        {
          "applicable_states": [],
          "branch_id": "product_scope_decision_required_terminal",
          "condition": "the requested correction requires an unresolved genuine product-intent or scope choice; return the exact decision required to Nathan without disguising it as a factual correction",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-E-30.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-E-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "SPECIFICATION_PENDING"
          ],
          "branch_id": "preapproval_revision",
          "condition": "pending preapproval Epic Specification corrected under the exact redline",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-E-40.md",
            "section": "Required result and routing"
          },
          "state": "SPECIFICATION_PENDING",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "SPECIFICATION_PENDING"
          ],
          "branch_id": "approved_base_first_delta_authoring",
          "condition": "first standalone Epic Specification delta authored from the exact Thoth correction assessment/redline; immutable approved base unchanged; return to the same Thoth reviewer for approved-base delta review",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-E-40.md",
            "section": "Required result and routing"
          },
          "state": "SPECIFICATION_PENDING",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "SPECIFICATION_PENDING"
          ],
          "branch_id": "approved_base_delta_revision",
          "condition": "pending bounded approved-base SPECIFICATION_DELTA corrected without rewriting the approved base",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-E-40.md",
            "section": "Required result and routing"
          },
          "state": "SPECIFICATION_PENDING",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "SPECIFICATION_PENDING"
      ],
      "to": "CF-E-30",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-E-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [],
          "branch_id": "revision_terminal",
          "condition": "the redline or authority owner cannot be resolved",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-E-40.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-E-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [],
          "branch_id": "redline_owner_recovery",
          "condition": "missing or contradictory redline/authority has an exact evidenced native owner",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "CONDITIONAL_RECOVERY",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-E-40.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [],
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "COMPLETE_DYNAMIC_NATIVE_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-PO-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "CLASS_SELECTED"
          ],
          "branch_id": "class_selected_crd",
          "condition": "CHANGE_CLASS=CRD with an exact Product Owner selection and change identity",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-PO-10.md",
            "section": "Required result and routing"
          },
          "state": "CLASS_SELECTED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "CLASS_SELECTED"
      ],
      "to": "CF-C-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-PO-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "CLASS_SELECTED"
          ],
          "branch_id": "class_selected_epic",
          "condition": "CHANGE_CLASS=EPIC with an exact Product Owner selection and change identity",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-PO-10.md",
            "section": "Required result and routing"
          },
          "state": "CLASS_SELECTED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "CLASS_SELECTED"
      ],
      "to": "CF-E-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CF-PO-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [],
          "branch_id": "selection_missing_or_conflicting",
          "condition": "no usable explicit Product Owner selection evidence, conflicting evidence, or unresolved change identity/source remains after CF-PO-10 requests or attempts to record it; return the exact requirement to Nathan with no CLASS_SELECTED result or kickoff",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CF-PO-10.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "POST_CLOSURE_PENDING"
          ],
          "branch_id": "manual_or_owner_pending",
          "condition": "the required manual act or native owner cannot yet supply a runnable continuation",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CL-20.md",
            "section": "Required result and routing"
          },
          "state": "POST_CLOSURE_PENDING",
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "POST_CLOSURE_PENDING"
      ],
      "to": "ACTUAL_OWNER_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "POST_CLOSURE_PENDING"
          ],
          "branch_id": "adr_branch",
          "condition": "the conditional ADR predicate is satisfied and the ADR branch is explicitly selected",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CL-20.md",
            "section": "Required result and routing"
          },
          "state": "POST_CLOSURE_PENDING",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "POST_CLOSURE_PENDING"
      ],
      "to": "CL-30",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "POST_CLOSURE_PENDING"
          ],
          "branch_id": "final_scan",
          "condition": "CL-20 and every actually selected managed post-closure branch have truthful dispositions",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CL-20.md",
            "section": "Required result and routing"
          },
          "state": "POST_CLOSURE_PENDING",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "POST_CLOSURE_PENDING"
      ],
      "to": "CL-40",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "POST_CLOSURE_PENDING"
          ],
          "branch_id": "epic_pf09_revalidation",
          "condition": "the authorized Epic PF09 branch requires initial or corrected revalidation authoring",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CL-20.md",
            "section": "Required result and routing"
          },
          "state": "POST_CLOSURE_PENDING",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "POST_CLOSURE_PENDING"
      ],
      "to": "CL-E-20",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "POST_CLOSURE_PENDING"
          ],
          "branch_id": "epic_pf09_review",
          "condition": "the authorized Epic PF09 branch has a complete revalidation ready for review",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CL-20.md",
            "section": "Required result and routing"
          },
          "state": "POST_CLOSURE_PENDING",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "POST_CLOSURE_PENDING"
      ],
      "to": "CL-E-30",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "POST_CLOSURE_PENDING"
          ],
          "branch_id": "epic_pf09_maintenance",
          "condition": "the authorized Epic PF09 branch requires post-Epic maintenance authoring",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CL-20.md",
            "section": "Required result and routing"
          },
          "state": "POST_CLOSURE_PENDING",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "POST_CLOSURE_PENDING"
      ],
      "to": "CL-E-40",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "POST_CLOSURE_PENDING"
          ],
          "branch_id": "native_owner_branch",
          "condition": "an exact manual, source-recovery, escalation, rescope, or other native owner branch is evidenced",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CL-20.md",
            "section": "Required result and routing"
          },
          "state": "POST_CLOSURE_PENDING",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "POST_CLOSURE_PENDING"
      ],
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "COMPLETE_DYNAMIC_NATIVE_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "ADR_CANDIDATE",
            "NO_ADR_NEEDED"
          ],
          "branch_id": "adr_owner_terminal",
          "condition": "source-qualified recovery/manual/TW/terminal owner is not a runnable selected prompt",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CL-30.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "ADR_CANDIDATE",
        "NO_ADR_NEEDED"
      ],
      "to": "ACTUAL_OWNER_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "ADR_CANDIDATE",
            "NO_ADR_NEEDED"
          ],
          "branch_id": "final_scan",
          "condition": "CL-20 and every selected post-closure managed branch are complete or validly disposed",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "CONDITIONAL_CONTINUATION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CL-30.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "ADR_CANDIDATE",
        "NO_ADR_NEEDED"
      ],
      "to": "CL-40",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "ADR_CANDIDATE"
          ],
          "branch_id": "adr_candidate_native_route",
          "condition": "the authorized repository or manual/TW maintenance receiver is exactly resolved",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CL-30.md",
            "section": "Required result and routing"
          },
          "state": "ADR_CANDIDATE",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "NO_ADR_NEEDED"
          ],
          "branch_id": "no_adr_native_route",
          "condition": "an applicable source-native post-closure route remains",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CL-30.md",
            "section": "Required result and routing"
          },
          "state": "NO_ADR_NEEDED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "ADR_CANDIDATE",
        "NO_ADR_NEEDED"
      ],
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "COMPLETE_DYNAMIC_NATIVE_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [],
          "branch_id": "scan_terminal",
          "condition": "a true source/authority/manual-owner stop has no runnable selected receiver",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CL-40.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [],
      "to": "ACTUAL_OWNER_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "INCOMPLETE"
          ],
          "branch_id": "incomplete_same_task",
          "condition": "resume the same CL-40 task after the exact missing bounded condition is resolved",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CL-40.md",
            "section": "Required result and routing"
          },
          "state": "INCOMPLETE",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "INCOMPLETE"
      ],
      "to": "CL-40",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "COMPLETE"
          ],
          "branch_id": "complete",
          "condition": "true end-cycle terminal",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CL-40.md",
            "section": "Required result and routing"
          },
          "state": "COMPLETE",
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "COMPLETE"
      ],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [],
          "branch_id": "selected_native_boundary",
          "condition": "a selected post-closure, evidence, scope, acceptance, or recovery branch has an exact native owner",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "CONDITIONAL_RECOVERY",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CL-40.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [],
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "COMPLETE_DYNAMIC_NATIVE_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-C-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "CHANGE_CLOSED"
          ],
          "branch_id": "change_closed",
          "condition": "positive CRD closure decision",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CL-C-10.md",
            "section": "Required result and routing"
          },
          "state": "CHANGE_CLOSED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "CHANGE_CLOSED"
      ],
      "to": "CL-20",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-C-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "DO_NOT_CLOSE"
          ],
          "branch_id": "do_not_close_new_remedy",
          "condition": "substantive new bounded remedy requires Thoth remediation",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CL-C-10.md",
            "section": "Required result and routing"
          },
          "state": "DO_NOT_CLOSE",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "DO_NOT_CLOSE"
      ],
      "to": "ESC-30",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-C-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [],
          "branch_id": "shared_source_authority_terminal",
          "condition": "true source, authority, identity, or owner stop with no runnable selected receiver; preserve evidence and return without a handoff",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CL-C-10.md",
            "section": "Terminal operator return and receiver compatibility"
          },
          "state": null,
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-C-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "DO_NOT_CLOSE"
          ],
          "branch_id": "do_not_close_existing_owner",
          "condition": "an already-authorized ordinary correction has an exact existing owner",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CL-C-10.md",
            "section": "Required result and routing"
          },
          "state": "DO_NOT_CLOSE",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "DO_NOT_CLOSE"
      ],
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "COMPLETE_DYNAMIC_NATIVE_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-E-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "CHANGE_CLOSED"
          ],
          "branch_id": "change_closed_postclosure",
          "condition": "positive Epic closure decision with ordinary post-closure work",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CL-E-10.md",
            "section": "Required result and routing"
          },
          "state": "CHANGE_CLOSED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "CHANGE_CLOSED"
      ],
      "to": "CL-20",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-E-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "CHANGE_CLOSED"
          ],
          "branch_id": "change_closed_epic_pf09",
          "condition": "a separately authorized Epic PF09 revalidation branch is selected",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CL-E-10.md",
            "section": "Required result and routing"
          },
          "state": "CHANGE_CLOSED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "CHANGE_CLOSED"
      ],
      "to": "CL-E-20",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-E-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "DO_NOT_CLOSE"
          ],
          "branch_id": "do_not_close_new_remedy",
          "condition": "substantive new bounded remedy requires Thoth remediation",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CL-E-10.md",
            "section": "Required result and routing"
          },
          "state": "DO_NOT_CLOSE",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "DO_NOT_CLOSE"
      ],
      "to": "ESC-30",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-E-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [],
          "branch_id": "shared_source_authority_terminal",
          "condition": "true source, authority, identity, or owner stop with no runnable selected receiver; preserve evidence and return without a handoff",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CL-E-10.md",
            "section": "Terminal operator return and receiver compatibility"
          },
          "state": null,
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-E-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "DO_NOT_CLOSE"
          ],
          "branch_id": "do_not_close_existing_owner",
          "condition": "an already-authorized ordinary correction has an exact existing owner",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/a/CL-E-10.md",
            "section": "Required result and routing"
          },
          "state": "DO_NOT_CLOSE",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "DO_NOT_CLOSE"
      ],
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "COMPLETE_DYNAMIC_NATIVE_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-E-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "PARTIAL"
          ],
          "branch_id": "partial",
          "condition": "repairable authoring or evidence gap; same author/session resumes",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/CL-E-20.md",
            "section": "Required result and routing"
          },
          "state": "PARTIAL",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "PARTIAL"
      ],
      "to": "CL-E-20",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-E-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "COMPLETE"
          ],
          "branch_id": "complete",
          "condition": "complete PF09 revalidation is ready for review",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/CL-E-20.md",
            "section": "Required result and routing"
          },
          "state": "COMPLETE",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "COMPLETE"
      ],
      "to": "CL-E-30",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-E-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "blocked",
          "condition": "missing closure, unresolved authority, or unrecoverable source/access failure",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/CL-E-20.md",
            "section": "Required result and routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "BLOCKED"
      ],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-E-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "DENY"
          ],
          "branch_id": "deny",
          "condition": "denied revalidation returns to the same author",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/CL-E-30.md",
            "section": "Required result and routing"
          },
          "state": "DENY",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "DENY"
      ],
      "to": "CL-E-20",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-E-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "ACCEPT"
          ],
          "branch_id": "accept",
          "condition": "accepted revalidation",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/CL-E-30.md",
            "section": "Required result and routing"
          },
          "state": "ACCEPT",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "ACCEPT"
      ],
      "to": "CL-E-40",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-E-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [],
          "branch_id": "review_terminal",
          "condition": "unresolved source, closure, authority, or owner",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/CL-E-30.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-E-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "MAINTENANCE_PENDING"
          ],
          "branch_id": "final_scan",
          "condition": "every selected post-closure author/reviewer branch and CL-20 work has a truthful disposition",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/CL-E-40.md",
            "section": "Required result and routing"
          },
          "state": "MAINTENANCE_PENDING",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "MAINTENANCE_PENDING"
      ],
      "to": "CL-40",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-E-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "MAINTENANCE_PENDING"
          ],
          "branch_id": "selected_evidence_gap",
          "condition": "a selected evidence gap requires PF09 revalidation",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/CL-E-40.md",
            "section": "Required result and routing"
          },
          "state": "MAINTENANCE_PENDING",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "MAINTENANCE_PENDING"
      ],
      "to": "CL-E-20",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-E-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "MAINTENANCE_PENDING"
          ],
          "branch_id": "maintenance_terminal",
          "condition": "manual/TW receiver, source, closure, or authority remains unresolved",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/CL-E-40.md",
            "section": "Required result and routing"
          },
          "state": "MAINTENANCE_PENDING",
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "MAINTENANCE_PENDING"
      ],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "CL-E-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "MAINTENANCE_PENDING"
          ],
          "branch_id": "manual_tw_route",
          "condition": "the exact authorized manual/TW maintenance receiver is resolved",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/CL-E-40.md",
            "section": "Required result and routing"
          },
          "state": "MAINTENANCE_PENDING",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "MAINTENANCE_PENDING"
      ],
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "COMPLETE_DYNAMIC_NATIVE_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "DOC-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "DRAFT",
            "PENDING",
            "BLOCKED"
          ],
          "branch_id": "repairable_instruction_defect",
          "condition": "instruction defect is repairable in the same IA session from a saved checkpoint",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "CONDITIONAL_RECOVERY",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/DOC-10.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "DRAFT",
        "PENDING",
        "BLOCKED"
      ],
      "to": "DOC-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "DOC-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "DRAFT",
            "PENDING",
            "BLOCKED"
          ],
          "branch_id": "instruction_terminal",
          "condition": "product-intent, source, authority, or unrecoverable evidence blocker",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/DOC-10.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "DRAFT",
        "PENDING",
        "BLOCKED"
      ],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "DOC-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "INSTRUCTION_READY"
          ],
          "branch_id": "instruction_ready",
          "condition": "complete documentation PR instruction is ready for detailed planning",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/DOC-10.md",
            "section": "Required result and routing"
          },
          "state": "INSTRUCTION_READY",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "INSTRUCTION_READY"
      ],
      "to": "PR-20",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "DOC-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "DRAFT",
            "PENDING",
            "BLOCKED"
          ],
          "branch_id": "material_boundary",
          "condition": "repository evidence proves a complete bounded material boundary",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "CONDITIONAL_RECOVERY",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/DOC-10.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "DRAFT",
        "PENDING",
        "BLOCKED"
      ],
      "to": "RS-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "DOC-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "INCOMPLETE",
            "PENDING",
            "BLOCKED"
          ],
          "branch_id": "instruction_repair",
          "condition": "documentation instruction is missing or defective",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "CONDITIONAL_RECOVERY",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/DOC-20.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "INCOMPLETE",
        "PENDING",
        "BLOCKED"
      ],
      "to": "DOC-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "DOC-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "INCOMPLETE",
            "PENDING",
            "BLOCKED"
          ],
          "branch_id": "documentation_terminal",
          "condition": "product-intent, source, authority, or unrecoverable merge-evidence failure",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/DOC-20.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "INCOMPLETE",
        "PENDING",
        "BLOCKED"
      ],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "DOC-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "COMPLETE"
          ],
          "branch_id": "remediation_complete_native_return",
          "condition": "approved remediation documentation is verified without the QA-10 predicate; resolve the exact originating selected owner/stage and complete its native intake under unchanged authority",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/DOC-20.md",
            "section": "Result routing"
          },
          "state": "COMPLETE",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "INCOMPLETE",
            "PENDING",
            "BLOCKED"
          ],
          "branch_id": "remediation_incomplete_native_return",
          "condition": "an incomplete or blocked remediation result has an exact lawful originating recovery/evidence owner and complete native return package; no PR-50, merge, PF10 drain or manual-gate bypass",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "CONDITIONAL_RECOVERY",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/DOC-20.md",
            "section": "Result routing"
          },
          "state": null,
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "COMPLETE",
        "INCOMPLETE",
        "PENDING",
        "BLOCKED"
      ],
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "COMPLETE_DYNAMIC_NATIVE_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "DOC-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "INCOMPLETE",
            "PENDING",
            "BLOCKED"
          ],
          "branch_id": "landed_lineage_review",
          "condition": "actual merged state or landed-lineage review is required after Nathan asserts the manual merge",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "CONDITIONAL_RECOVERY",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/DOC-20.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "INCOMPLETE",
        "PENDING",
        "BLOCKED"
      ],
      "to": "PR-40",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "DOC-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "COMPLETE"
          ],
          "branch_id": "complete",
          "condition": "all documentation obligations and landed lineage are verified, and this is ordinary initial documentation or the remedy materially affects readiness or Nathan explicitly requires a QA-10 rerun",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/DOC-20.md",
            "section": "Required result and routing"
          },
          "state": "COMPLETE",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "COMPLETE"
      ],
      "to": "QA-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "DOC-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "INCOMPLETE",
            "PENDING",
            "BLOCKED"
          ],
          "branch_id": "material_delta",
          "condition": "evidence proves a bounded material delta",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "CONDITIONAL_RECOVERY",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/DOC-20.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "INCOMPLETE",
        "PENDING",
        "BLOCKED"
      ],
      "to": "RS-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "ESC-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "AWAITING_THOTH_REMEDIATION"
          ],
          "branch_id": "awaiting_thoth_remediation",
          "condition": "complete QA escalation report is ready for Thoth remediation",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/ESC-10.md",
            "section": "Required result and routing"
          },
          "state": "AWAITING_THOTH_REMEDIATION",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "AWAITING_THOTH_REMEDIATION"
      ],
      "to": "ESC-30",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "ESC-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [],
          "branch_id": "escalation_terminal",
          "condition": "missing decisive source, owner, authority, or irrecoverable evidence",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/ESC-10.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "ESC-25",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "COMPLETE"
          ],
          "branch_id": "complete",
          "condition": "complete discovery result returns to continuing Thoth",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/ESC-25.md",
            "section": "Required result and routing"
          },
          "state": "COMPLETE",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "PARTIAL"
          ],
          "branch_id": "partial",
          "condition": "usable partial discovery result returns to continuing Thoth",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/ESC-25.md",
            "section": "Required result and routing"
          },
          "state": "PARTIAL",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "blocked_evidence_return",
          "condition": "a discovery fact is inaccessible but exact task, evidence/limitations and complete same-Thoth return package are known",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/ESC-25.md",
            "section": "Result routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "COMPLETE",
        "PARTIAL",
        "BLOCKED"
      ],
      "to": "ESC-30",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "ESC-25",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "blocked_terminal",
          "condition": "the exact discovery task/return owner or complete lawful return package cannot be established",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/ESC-25.md",
            "section": "Result routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "BLOCKED"
      ],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "ESC-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "DISCOVERY_REQUIRED"
          ],
          "branch_id": "discovery_required",
          "condition": "one complete bounded discovery task is linked to the saved/read-back actual pending Thoth remediation record, which may truthfully be DISCOVERY_REQUIRED; no complete or approved remedy is invented",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/ESC-30.md",
            "section": "Required result and routing"
          },
          "state": "DISCOVERY_REQUIRED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "DISCOVERY_REQUIRED"
      ],
      "to": "ESC-25",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "ESC-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "REMEDIATION_PENDING"
          ],
          "branch_id": "remediation_pending",
          "condition": "complete bounded remediation proposal is ready for continuing-Isis review",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/ESC-30.md",
            "section": "Required result and routing"
          },
          "state": "REMEDIATION_PENDING",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "REMEDIATION_PENDING"
      ],
      "to": "ESC-40",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "ESC-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "blocked",
          "condition": "product-intent, authority, or decisive source blocker",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/ESC-30.md",
            "section": "Required result and routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "BLOCKED"
      ],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "ESC-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "DENY"
          ],
          "branch_id": "deny",
          "condition": "return to remediation author; no addendum",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/ESC-40.md",
            "section": "Required result and routing"
          },
          "state": "DENY",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "DENY"
      ],
      "to": "ESC-30",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "ESC-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "APPROVE"
          ],
          "branch_id": "approve",
          "condition": "qualifying approved remediation creates exactly one addendum and a conditional post-drain native-delivery handoff",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/ESC-40.md",
            "section": "Required result and routing"
          },
          "state": "APPROVE",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "APPROVE_AS_CHANGED"
          ],
          "branch_id": "approve_as_changed",
          "condition": "qualifying approved-as-changed remediation creates exactly one addendum and a conditional post-drain native-delivery handoff",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/ESC-40.md",
            "section": "Required result and routing"
          },
          "state": "APPROVE_AS_CHANGED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "APPROVE",
        "APPROVE_AS_CHANGED"
      ],
      "to": "NATHAN_MANUAL_PF10_DRAIN",
      "to_kind": "boundary",
      "transport": "MANUAL_PRODUCT_OWNER_BOUNDARY"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "ESC-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [],
          "branch_id": "remediation_review_terminal",
          "condition": "native continuation identity, Product Owner/source, or authority predicate is unresolved",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/ESC-40.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "GCFPE-MGMT-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "ECOSYSTEM_CHANGE_COMPLETE"
          ],
          "branch_id": "maintenance_complete_terminal",
          "condition": "scoped maintenance complete; no exact further substantive invocation is both authorized and ready; return the saved/read-back GCFPE_ECOSYSTEM_CHANGE_REPORT to Nathan",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/GCFPE-MGMT-10.md",
            "section": "Result routing"
          },
          "state": "ECOSYSTEM_CHANGE_COMPLETE",
          "terminal_for_invocation": true
        },
        {
          "applicable_states": [
            "IMPLEMENTATION_BLOCKED"
          ],
          "branch_id": "implementation_blocked",
          "condition": "real blocker; preserve a read-back recovery checkpoint and return to Nathan",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/GCFPE-MGMT-10.md",
            "section": "Required result and routing"
          },
          "state": "IMPLEMENTATION_BLOCKED",
          "terminal_for_invocation": true
        },
        {
          "applicable_states": [
            "PROMOTION_CHECKPOINT_REQUIRED"
          ],
          "branch_id": "promotion_checkpoint_required",
          "condition": "exact-snapshot promotion approval or a required active control-layer checkpoint is outstanding; return the fully specified imminent transaction without treating general repair authorization as promotion approval",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/GCFPE-MGMT-10.md",
            "section": "Required result and routing"
          },
          "state": "PROMOTION_CHECKPOINT_REQUIRED",
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "ECOSYSTEM_CHANGE_COMPLETE",
        "IMPLEMENTATION_BLOCKED",
        "PROMOTION_CHECKPOINT_REQUIRED"
      ],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "GCFPE-MGMT-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "ECOSYSTEM_CHANGE_COMPLETE"
          ],
          "branch_id": "maintenance_complete_native_return",
          "condition": "scoped maintenance complete and the exact case separately authorizes one ready native continuation; resolve the actual selected receiver and preserve original authority, session and inputs; exclude PR-50, merge, PF10 drain, unselected candidates and unauthorized Alpha; emit one complete handoff without executing it",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/GCFPE-MGMT-10.md",
            "section": "Result routing"
          },
          "state": "ECOSYSTEM_CHANGE_COMPLETE",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "ECOSYSTEM_CHANGE_COMPLETE"
      ],
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "COMPLETE_DYNAMIC_NATIVE_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "GCFPE-MGMT-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION"
          ],
          "branch_id": "ready_for_product_owner_alpha_resumption_decision",
          "condition": "separately authorized EPIC040 Alpha-preparation branch only, after exact approved promotion, complete production readback/validation and intact archival; exactly one saved/read-back PR-10 invocation for HDE-EPIC040-PR04, for Nathan to review and manually invoke; does not execute Alpha",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/GCFPE-MGMT-10.md",
            "section": "Separate EPIC040 Alpha preparation branch and Result routing"
          },
          "state": "READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION"
      ],
      "to": "PR-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "audit_recovery",
          "condition": "Audit is incomplete but useful local recovery remains in the same IA session; no separate answer-seeding or research package is required",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/IA-10.md",
            "section": "Required result and routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "BLOCKED"
      ],
      "to": "IA-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "AUDIT_COMPLETE"
          ],
          "branch_id": "plan_interrupted",
          "condition": "Audit is complete and the Plan phase was interrupted; no separate answer-seeding or research package is required first",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/IA-10.md",
            "section": "Required result and routing"
          },
          "state": "AUDIT_COMPLETE",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "AUDIT_COMPLETE"
      ],
      "to": "IA-20",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "PLAN_PENDING"
          ],
          "branch_id": "audit_and_plan_complete",
          "condition": "both Implementation Audit and initial Plan are complete and decisive architecture/feasibility questions are resolved for submission",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/IA-10.md",
            "section": "Required result and routing"
          },
          "state": "PLAN_PENDING",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "PLAN_PENDING"
      ],
      "to": "IA-30",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "initial_denial_correction",
          "condition": "an exact initial Plan denial correction is already authorized",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/IA-10.md",
            "section": "Required result and routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "BLOCKED"
      ],
      "to": "IA-40",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "answer_available",
          "condition": "an actual partial or complete answer is available for bounded validation/application; carry complete RECOVERY_ENVELOPE and ANSWER_REF with exact paused artifacts and authority; preserve unanswered questions and deadlines and same-author return; do not repeat research or infer whole-Plan readiness",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/IA-10.md",
            "section": "Planning readiness, questions, and recovery; Result routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "BLOCKED"
      ],
      "to": "IA-50",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "bounded_research",
          "condition": "a complete bounded planning research need is identified and no usable answer exists yet; carry PLANNING_INQUIRY and RECOVERY_ENVELOPE",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/IA-10.md",
            "section": "Required result and routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "BLOCKED"
      ],
      "to": "IA-60",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "ia10_terminal",
          "condition": "approved-base rewrite request, product decision, or unrecoverable source/authority blocker",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/IA-10.md",
            "section": "Required result and routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "BLOCKED"
      ],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "plan_recovery",
          "condition": "Plan remains incomplete but useful local recovery remains in the same IA session; no separate answer-seeding or research package is required",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/IA-20.md",
            "section": "Required result and routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "BLOCKED"
      ],
      "to": "IA-20",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "PLAN_PENDING"
          ],
          "branch_id": "plan_pending",
          "condition": "complete initial Plan is ready for Isis review with decisive architecture/feasibility questions resolved",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/IA-20.md",
            "section": "Required result and routing"
          },
          "state": "PLAN_PENDING",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "PLAN_PENDING"
      ],
      "to": "IA-30",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "initial_denial_correction",
          "condition": "an exact initial denial correction is already authorized",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/IA-20.md",
            "section": "Required result and routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "BLOCKED"
      ],
      "to": "IA-40",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "answer_available",
          "condition": "an actual partial or complete answer is available for bounded validation/application; carry complete RECOVERY_ENVELOPE and ANSWER_REF, valid completed Audit and exact Plan checkpoint; preserve unanswered questions and deadlines and same-author return; do not repeat research or infer whole-Plan readiness",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/IA-20.md",
            "section": "Planning readiness, questions, and recovery; Result routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "BLOCKED"
      ],
      "to": "IA-50",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "bounded_research",
          "condition": "a bounded planning research need is identified and no usable answer exists yet; carry PLANNING_INQUIRY and RECOVERY_ENVELOPE",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/IA-20.md",
            "section": "Required result and routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "BLOCKED"
      ],
      "to": "IA-60",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "ia20_terminal",
          "condition": "approved-base rewrite request, product decision, or unrecoverable source/authority blocker",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/IA-20.md",
            "section": "Required result and routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "BLOCKED"
      ],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "DENY"
          ],
          "branch_id": "initial_deny",
          "condition": "REVIEW_MODE=INITIAL; exact redlines return to the same IA author",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/IA-30.md",
            "section": "Required result and routing"
          },
          "state": "DENY",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "DENY"
      ],
      "to": "IA-40",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "APPROVE"
          ],
          "branch_id": "material_delta_approve",
          "condition": "REVIEW_MODE=MATERIAL_DELTA; exactly one addendum and conditional post-drain native continuation",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/IA-30.md",
            "section": "Required result and routing"
          },
          "state": "APPROVE",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "APPROVE"
      ],
      "to": "NATHAN_MANUAL_PF10_DRAIN",
      "to_kind": "boundary",
      "transport": "MANUAL_PRODUCT_OWNER_BOUNDARY"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [],
          "branch_id": "plan_review_terminal",
          "condition": "source, authority, manual-continuation identity, or Product Owner decision blocker",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/IA-30.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "DENY"
          ],
          "branch_id": "material_delta_deny",
          "condition": "REVIEW_MODE=MATERIAL_DELTA; return denial to the exact recorded proposed-delta author",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/IA-30.md",
            "section": "Required result and routing"
          },
          "state": "DENY",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "DENY"
      ],
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "COMPLETE_DYNAMIC_NATIVE_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "APPROVE"
          ],
          "branch_id": "initial_approve",
          "condition": "REVIEW_MODE=INITIAL and the pending whole-change Plan is approved; no addendum",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/b/IA-30.md",
            "section": "Required result and routing"
          },
          "state": "APPROVE",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "APPROVE"
      ],
      "to": "PR-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "WRONG_ROUTE_APPROVED_BASE"
          ],
          "branch_id": "approved_base_remediation",
          "condition": "the approved-base request is an already-authored bounded remediation ready for Isis review",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/IA-40.md",
            "section": "Required result and routing"
          },
          "state": "WRONG_ROUTE_APPROVED_BASE",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "WRONG_ROUTE_APPROVED_BASE"
      ],
      "to": "ESC-40",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "PLAN_PENDING_REVISED"
          ],
          "branch_id": "plan_pending_revised",
          "condition": "valid preapproval revision returns to the same Isis reviewer",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/IA-40.md",
            "section": "Required result and routing"
          },
          "state": "PLAN_PENDING_REVISED",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "WRONG_ROUTE_APPROVED_BASE"
          ],
          "branch_id": "approved_base_plan_delta",
          "condition": "the approved-base request is another material whole-Plan delta for IA-30 bounded-delta review",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/IA-40.md",
            "section": "Required result and routing"
          },
          "state": "WRONG_ROUTE_APPROVED_BASE",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "PLAN_PENDING_REVISED",
        "WRONG_ROUTE_APPROVED_BASE"
      ],
      "to": "IA-30",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "WRONG_ROUTE_APPROVED_BASE"
          ],
          "branch_id": "approved_base_terminal",
          "condition": "the actual qualifying approver or source/authority predicate cannot be resolved",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/IA-40.md",
            "section": "Required result and routing"
          },
          "state": "WRONG_ROUTE_APPROVED_BASE",
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "WRONG_ROUTE_APPROVED_BASE"
      ],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "WRONG_ROUTE_APPROVED_BASE"
          ],
          "branch_id": "approved_base_rescope",
          "condition": "the approved-base request is a bounded rescope with complete RS-20 intake",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/IA-40.md",
            "section": "Required result and routing"
          },
          "state": "WRONG_ROUTE_APPROVED_BASE",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "WRONG_ROUTE_APPROVED_BASE"
      ],
      "to": "RS-20",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-50",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "SEED_INCOMPLETE"
          ],
          "branch_id": "seed_incomplete_terminal",
          "condition": "answer is stale, contradictory, incomplete, duplicate without a resolvable continuation, or wrong-authority; return evidence to the actual answer/base owner with no synthetic runnable successor",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/IA-50.md",
            "section": "Required result and routing"
          },
          "state": "SEED_INCOMPLETE",
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "SEED_INCOMPLETE"
      ],
      "to": "ACTUAL_OWNER_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-50",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "SEED_READY"
          ],
          "branch_id": "seed_remediation_review",
          "condition": "the answer belongs to integrated remediation with a complete pending Thoth proposal",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/IA-50.md",
            "section": "Required result and routing"
          },
          "state": "SEED_READY",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "SEED_READY"
      ],
      "to": "ESC-40",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-50",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "SEED_READY"
          ],
          "branch_id": "seed_incomplete_audit",
          "condition": "the validated answer applies to an incomplete IA-10 Audit",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/IA-50.md",
            "section": "Required result and routing"
          },
          "state": "SEED_READY",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "SEED_READY"
      ],
      "to": "IA-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-50",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "SEED_READY"
          ],
          "branch_id": "seed_paused_plan",
          "condition": "the Audit is complete and the answer applies to a paused initial Plan",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/IA-50.md",
            "section": "Required result and routing"
          },
          "state": "SEED_READY",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "SEED_READY"
      ],
      "to": "IA-20",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-50",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "SEED_READY"
          ],
          "branch_id": "seed_plan_review",
          "condition": "same-Isis correction intake or material approved-Plan delta lacks an existing correction instruction",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/IA-50.md",
            "section": "Required result and routing"
          },
          "state": "SEED_READY",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "SEED_READY"
      ],
      "to": "IA-30",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-50",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "SEED_READY"
          ],
          "branch_id": "seed_preapproval_correction",
          "condition": "the answer applies to an authorized pending-preapproval Plan correction",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/IA-50.md",
            "section": "Required result and routing"
          },
          "state": "SEED_READY",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "SEED_READY"
      ],
      "to": "IA-40",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-50",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "SEED_INCOMPLETE"
          ],
          "branch_id": "duplicate_existing_continuation",
          "condition": "a duplicate answer is already applied and its existing valid continuation/result is exactly resolved; reuse it without creating another successor",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/IA-50.md",
            "section": "Required result and routing"
          },
          "state": "SEED_INCOMPLETE",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "SEED_INCOMPLETE"
      ],
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "COMPLETE_DYNAMIC_NATIVE_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-60",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "PARTIAL"
          ],
          "branch_id": "partial",
          "condition": "incomplete evidence or missing owner decision prevents a synthetic IA-50 continuation",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/IA-60.md",
            "section": "Required result and routing"
          },
          "state": "PARTIAL",
          "terminal_for_invocation": true
        },
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "blocked",
          "condition": "source, authority, or terminal owner stop; return the exact question/evidence to its native owner",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/IA-60.md",
            "section": "Required result and routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "PARTIAL",
        "BLOCKED"
      ],
      "to": "ACTUAL_OWNER_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-60",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "RESEARCH_COMPLETE"
          ],
          "branch_id": "research_post_failure_remediation",
          "condition": "the complete finding is actual post-failure remediation evidence with unchanged ESC-30 native inputs",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/IA-60.md",
            "section": "Required result and routing"
          },
          "state": "RESEARCH_COMPLETE",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "RESEARCH_COMPLETE"
      ],
      "to": "ESC-30",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "IA-60",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "RESEARCH_COMPLETE"
          ],
          "branch_id": "research_to_seeder",
          "condition": "bounded planning finding is complete and authorized for answer seeding",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/IA-60.md",
            "section": "Required result and routing"
          },
          "state": "RESEARCH_COMPLETE",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "RESEARCH_COMPLETE"
      ],
      "to": "IA-50",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "MGR-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "FLOW_PROGRESS"
          ],
          "branch_id": "crd_entry",
          "condition": "new cycle entry has an exact CRD classification and complete intake",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/MGR-10.md",
            "section": "Required result and routing"
          },
          "state": "FLOW_PROGRESS",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "FLOW_PROGRESS"
      ],
      "to": "CF-C-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "MGR-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "FLOW_PROGRESS"
          ],
          "branch_id": "epic_entry",
          "condition": "new cycle entry has an exact Epic classification and complete intake",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/MGR-10.md",
            "section": "Required result and routing"
          },
          "state": "FLOW_PROGRESS",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "FLOW_PROGRESS"
      ],
      "to": "CF-E-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "MGR-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "FLOW_PROGRESS"
          ],
          "branch_id": "class_selection",
          "condition": "new cycle entry has no Product Owner class-decision evidence, or has exact evidence whose selection record is missing; CF-PO-10 receives the unresolved or evidenced-recording case and never chooses the class",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/MGR-10.md",
            "section": "Required result and routing"
          },
          "state": "FLOW_PROGRESS",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "FLOW_PROGRESS"
      ],
      "to": "CF-PO-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "MGR-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "FLOW_PROGRESS"
          ],
          "branch_id": "final_scan",
          "condition": "closure and all selected post-closure work are disposed and the final scan is next",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/MGR-10.md",
            "section": "Required result and routing"
          },
          "state": "FLOW_PROGRESS",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "FLOW_PROGRESS"
      ],
      "to": "CL-40",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "MGR-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "TERMINAL_RETURN"
          ],
          "branch_id": "terminal_return",
          "condition": "true completed-cycle or Product Owner terminal return",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/MGR-10.md",
            "section": "Required result and routing"
          },
          "state": "TERMINAL_RETURN",
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "TERMINAL_RETURN"
      ],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "MGR-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "FLOW_PROGRESS"
          ],
          "branch_id": "other_native_stage",
          "condition": "another exact selected native stage is the evidenced next unmet contract; the dynamic boundary resolves one prompt at runtime",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/MGR-10.md",
            "section": "Required result and routing"
          },
          "state": "FLOW_PROGRESS",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "FLOW_PROGRESS"
      ],
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "COMPLETE_DYNAMIC_NATIVE_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "MGR-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "FLOW_PROGRESS"
          ],
          "branch_id": "pre_qa",
          "condition": "the exact next unmet contract is integrated pre-QA audit/triage/readiness",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/MGR-10.md",
            "section": "Required result and routing"
          },
          "state": "FLOW_PROGRESS",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "FLOW_PROGRESS"
      ],
      "to": "QA-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "automatic": false,
      "branch_id": "nathan_abort",
      "condition": "Nathan directly instructs Abort PR and Escalate for one exact identified PR",
      "from": "NATHAN_ABORT_INSTRUCTION",
      "from_kind": "boundary",
      "immediate": true,
      "origin_prompt": "NATHAN_DIRECT_ONLY",
      "origin_state": "IDENTIFIED_PR",
      "to": "PR-50",
      "to_kind": "prompt",
      "transport": "MANUAL_PRODUCT_OWNER_INVOCATION"
    },
    {
      "automatic": false,
      "branch_id": "manual_merge_then_lineage_review",
      "condition": "Nathan has manually merged the identified PR and invokes the conditional PR-40 block",
      "from": "NATHAN_MANUAL_MERGE_ASSERTION",
      "from_kind": "boundary",
      "immediate": true,
      "origin_prompt": "PR-35_OR_RS-40",
      "origin_state": "MERGE_PENDING",
      "to": "PR-40",
      "to_kind": "prompt",
      "transport": "MANUAL_PRODUCT_OWNER_INVOCATION"
    },
    {
      "automatic": false,
      "branch_id": "crd_specification_delta_return",
      "condition": "the exact affected native receiver recorded by the approved CRD Specification delta freshly verifies current PF10; this is not an RS-40 rescope route",
      "from": "NATHAN_MANUAL_PF10_DRAIN",
      "from_kind": "boundary",
      "immediate": true,
      "origin_prompt": "CF-C-30",
      "origin_state": "DELTA_APPROVE",
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "MANUAL_PRODUCT_OWNER_INVOCATION"
    },
    {
      "automatic": false,
      "branch_id": "epic_specification_delta_return",
      "condition": "the exact affected native receiver recorded by the approved Epic Specification delta freshly verifies current PF10; this is not an RS-40 rescope route",
      "from": "NATHAN_MANUAL_PF10_DRAIN",
      "from_kind": "boundary",
      "immediate": true,
      "origin_prompt": "CF-E-30",
      "origin_state": "DELTA_APPROVE",
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "MANUAL_PRODUCT_OWNER_INVOCATION"
    },
    {
      "automatic": false,
      "branch_id": "plan_delta_return",
      "condition": "REVIEW_MODE=MATERIAL_DELTA; the exact return_phase receiver freshly verifies current PF10",
      "from": "NATHAN_MANUAL_PF10_DRAIN",
      "from_kind": "boundary",
      "immediate": true,
      "origin_prompt": "IA-30",
      "origin_state": "APPROVE",
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "MANUAL_PRODUCT_OWNER_INVOCATION"
    },
    {
      "automatic": false,
      "branch_id": "qa_plan_delta_return",
      "condition": "REVIEW_MODE=DELTA; the exact native receiver freshly verifies current PF10",
      "from": "NATHAN_MANUAL_PF10_DRAIN",
      "from_kind": "boundary",
      "immediate": true,
      "origin_prompt": "QA-70",
      "origin_state": "APPROVE",
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "MANUAL_PRODUCT_OWNER_INVOCATION"
    },
    {
      "automatic": false,
      "branch_id": "remediation_non_pr_return",
      "condition": "recorded remediation return is a non-PR native delivery owner; that receiver freshly verifies current PF10",
      "from": "NATHAN_MANUAL_PF10_DRAIN",
      "from_kind": "boundary",
      "immediate": true,
      "origin_prompt": "ESC-40",
      "origin_state": "APPROVE_OR_APPROVE_AS_CHANGED",
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "MANUAL_PRODUCT_OWNER_INVOCATION"
    },
    {
      "automatic": false,
      "branch_id": "rescope_non_pr",
      "condition": "qualifying non-PR bounded rescope; exact native stage freshly verifies current PF10",
      "from": "NATHAN_MANUAL_PF10_DRAIN",
      "from_kind": "boundary",
      "immediate": true,
      "origin_prompt": "RS-20",
      "origin_state": "APPROVE",
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "MANUAL_PRODUCT_OWNER_INVOCATION"
    },
    {
      "automatic": false,
      "branch_id": "remediation_pr30_return",
      "condition": "recorded remediation return is PR-30_PREPUBLICATION or PR-30_POSTPUBLICATION; resume PR-30 directly after fresh verification, preserving actual vehicle state",
      "from": "NATHAN_MANUAL_PF10_DRAIN",
      "from_kind": "boundary",
      "immediate": true,
      "origin_prompt": "ESC-40",
      "origin_state": "APPROVE_OR_APPROVE_AS_CHANGED",
      "to": "PR-30",
      "to_kind": "prompt",
      "transport": "MANUAL_PRODUCT_OWNER_INVOCATION"
    },
    {
      "automatic": false,
      "branch_id": "rescope_pr30_prepublication",
      "condition": "PR_RETURN_PHASE=PR-30_PREPUBLICATION; PR-30 freshly verifies current PF10; no open PR and RS-40 forbidden",
      "from": "NATHAN_MANUAL_PF10_DRAIN",
      "from_kind": "boundary",
      "immediate": true,
      "origin_prompt": "RS-20",
      "origin_state": "APPROVE",
      "to": "PR-30",
      "to_kind": "prompt",
      "transport": "MANUAL_PRODUCT_OWNER_INVOCATION"
    },
    {
      "automatic": false,
      "branch_id": "remediation_pr35_return",
      "condition": "recorded remediation return is PR-35; resume PR-35 directly after fresh verification in the same open PR",
      "from": "NATHAN_MANUAL_PF10_DRAIN",
      "from_kind": "boundary",
      "immediate": true,
      "origin_prompt": "ESC-40",
      "origin_state": "APPROVE_OR_APPROVE_AS_CHANGED",
      "to": "PR-35",
      "to_kind": "prompt",
      "transport": "MANUAL_PRODUCT_OWNER_INVOCATION"
    },
    {
      "automatic": false,
      "branch_id": "rescope_open_pr",
      "condition": "PR_RETURN_PHASE in {PR-30_POSTPUBLICATION, PR-35}; existing open PR identity verified",
      "from": "NATHAN_MANUAL_PF10_DRAIN",
      "from_kind": "boundary",
      "immediate": true,
      "origin_prompt": "RS-20",
      "origin_state": "APPROVE",
      "to": "RS-40",
      "to_kind": "prompt",
      "transport": "MANUAL_PRODUCT_OWNER_INVOCATION"
    },
    {
      "automatic": false,
      "branch_id": "original_proceed",
      "condition": "original explicit Proceed for the exact work unit; never a second Proceed",
      "from": "NATHAN_PROCEED",
      "from_kind": "boundary",
      "immediate": true,
      "origin_prompt": "PR-20",
      "origin_state": "AWAITING_PO_PROCEED",
      "to": "PR-30",
      "to_kind": "prompt",
      "transport": "MANUAL_PRODUCT_OWNER_INVOCATION"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "OPS-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "blocked_terminal",
          "condition": "a decisive source, authority, target, or owner fact prevents a runnable task",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/OPS-10.md",
            "section": "Required result and routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "BLOCKED"
      ],
      "to": "ACTUAL_OWNER_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "OPS-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [],
          "branch_id": "remediation_discovery",
          "condition": "the exact authorized remediation package requires bounded discovery",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "CONDITIONAL_CONTINUATION",
          "route_steps": [
            "OPS-10 -> ESC-25",
            "ESC-25 result -> ESC-30"
          ],
          "source_evidence": {
            "path": "candidate/prompts/c/OPS-10.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [],
      "to": "ESC-25",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "OPS-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "READY"
          ],
          "branch_id": "ready",
          "condition": "complete bounded OPS_TASK with actual action authority is ready for execution",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/OPS-10.md",
            "section": "Required result and routing"
          },
          "state": "READY",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "READY"
      ],
      "to": "OPS-20",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "OPS-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "blocked_native_owner",
          "condition": "the complete recovery package resolves the same creator or exact native owner",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/OPS-10.md",
            "section": "Required result and routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "BLOCKED"
      ],
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "COMPLETE_DYNAMIC_NATIVE_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "OPS-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [],
          "branch_id": "material_boundary_proposal",
          "condition": "a new complete material boundary requires a bounded rescope proposal",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "CONDITIONAL_RECOVERY",
          "route_steps": [
            "OPS-10 -> RS-10",
            "RS-10 complete proposal -> RS-20",
            "RS-20 REVISION_REQUIRED -> RS-30"
          ],
          "source_evidence": {
            "path": "candidate/prompts/c/OPS-10.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [],
      "to": "RS-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "OPS-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BLOCKED",
            "FAILED",
            "NOT_EXECUTED",
            "NOT_PRODUCED"
          ],
          "branch_id": "ops_execution_terminal",
          "condition": "a decisive source, authority, target, access, or owner fact prevents any runnable continuation",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/OPS-20.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "BLOCKED",
        "FAILED",
        "NOT_EXECUTED",
        "NOT_PRODUCED"
      ],
      "to": "ACTUAL_OWNER_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "OPS-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "PARTIAL",
            "BLOCKED",
            "FAILED",
            "NOT_EXECUTED",
            "NOT_PRODUCED"
          ],
          "branch_id": "remediation_discovery",
          "condition": "the exact authorized remediation package requires bounded discovery before Thoth resumes",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "CONDITIONAL_CONTINUATION",
          "route_steps": [
            "OPS-20 -> ESC-25",
            "ESC-25 result -> ESC-30"
          ],
          "source_evidence": {
            "path": "candidate/prompts/c/OPS-20.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "PARTIAL",
        "BLOCKED",
        "FAILED",
        "NOT_EXECUTED",
        "NOT_PRODUCED"
      ],
      "to": "ESC-25",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "OPS-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "COMPLETE"
          ],
          "branch_id": "result_complete",
          "condition": "one truthful OPS_EXECUTION_RESULT returns to the task creator and receipt reviewer",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/OPS-20.md",
            "section": "Required result and routing"
          },
          "state": "COMPLETE",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "PARTIAL"
          ],
          "branch_id": "result_partial",
          "condition": "one truthful OPS_EXECUTION_RESULT returns to the task creator and receipt reviewer",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/OPS-20.md",
            "section": "Required result and routing"
          },
          "state": "PARTIAL",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "result_blocked",
          "condition": "one truthful OPS_EXECUTION_RESULT returns to the task creator and receipt reviewer",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/OPS-20.md",
            "section": "Required result and routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "FAILED"
          ],
          "branch_id": "result_failed",
          "condition": "one truthful OPS_EXECUTION_RESULT returns to the task creator and receipt reviewer",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/OPS-20.md",
            "section": "Required result and routing"
          },
          "state": "FAILED",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "NOT_EXECUTED"
          ],
          "branch_id": "result_notexecuted",
          "condition": "one truthful OPS_EXECUTION_RESULT returns to the task creator and receipt reviewer",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/OPS-20.md",
            "section": "Required result and routing"
          },
          "state": "NOT_EXECUTED",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "NOT_PRODUCED"
          ],
          "branch_id": "result_notproduced",
          "condition": "one truthful OPS_EXECUTION_RESULT returns to the task creator and receipt reviewer",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/OPS-20.md",
            "section": "Required result and routing"
          },
          "state": "NOT_PRODUCED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "COMPLETE",
        "PARTIAL",
        "BLOCKED",
        "FAILED",
        "NOT_EXECUTED",
        "NOT_PRODUCED"
      ],
      "to": "OPS-30",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "OPS-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "PARTIAL",
            "BLOCKED",
            "FAILED",
            "NOT_EXECUTED",
            "NOT_PRODUCED"
          ],
          "branch_id": "ops_execution_native_owner",
          "condition": "a blocked, incomplete, contradictory, or access-limited result has an exact native owner",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "CONDITIONAL_RECOVERY",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/OPS-20.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "PARTIAL",
        "BLOCKED",
        "FAILED",
        "NOT_EXECUTED",
        "NOT_PRODUCED"
      ],
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "COMPLETE_DYNAMIC_NATIVE_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "OPS-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "PARTIAL",
            "BLOCKED",
            "FAILED",
            "NOT_EXECUTED",
            "NOT_PRODUCED"
          ],
          "branch_id": "material_boundary_proposal",
          "condition": "actual execution evidence establishes a new bounded material boundary requiring proposal",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "CONDITIONAL_RECOVERY",
          "route_steps": [
            "OPS-20 -> RS-10",
            "RS-10 complete proposal -> RS-20",
            "RS-20 REVISION_REQUIRED -> RS-30"
          ],
          "source_evidence": {
            "path": "candidate/prompts/c/OPS-20.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "PARTIAL",
        "BLOCKED",
        "FAILED",
        "NOT_EXECUTED",
        "NOT_PRODUCED"
      ],
      "to": "RS-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "OPS-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "REJECT"
          ],
          "branch_id": "receipt_terminal",
          "condition": "the exact native recovery owner or decisive prerequisite is unresolved",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/OPS-30.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "REJECT"
      ],
      "to": "ACTUAL_OWNER_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "OPS-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "REJECT"
          ],
          "branch_id": "remediation_discovery",
          "condition": "the actual receipt and remediation package explicitly require bounded discovery",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "CONDITIONAL_RECOVERY",
          "route_steps": [
            "OPS-30 -> ESC-25",
            "ESC-25 result -> ESC-30"
          ],
          "source_evidence": {
            "path": "candidate/prompts/c/OPS-30.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "REJECT"
      ],
      "to": "ESC-25",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "OPS-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "REJECT"
          ],
          "branch_id": "reject_corrective_task",
          "condition": "bounded correction or retry begins with a new corrective OPS_TASK; OPS-20 follows only after that task is complete",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [
            "OPS-30 -> OPS-10",
            "complete corrective OPS_TASK -> OPS-20",
            "OPS_EXECUTION_RESULT -> OPS-30"
          ],
          "source_evidence": {
            "path": "candidate/prompts/c/OPS-30.md",
            "section": "Required result and routing"
          },
          "state": "REJECT",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "REJECT"
      ],
      "to": "OPS-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "OPS-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "ACCEPT"
          ],
          "branch_id": "accept_native_consumer",
          "condition": "accepted receipt returns to the exact Plan-named downstream consumer or same creator IA",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/OPS-30.md",
            "section": "Required result and routing"
          },
          "state": "ACCEPT",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "REJECT"
          ],
          "branch_id": "receipt_native_owner",
          "condition": "a blocked, contradictory, incomplete, or access-limited receipt has an exact native recovery owner",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "CONDITIONAL_RECOVERY",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/OPS-30.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "ACCEPT",
        "REJECT"
      ],
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "COMPLETE_DYNAMIC_NATIVE_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "OPS-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "REJECT"
          ],
          "branch_id": "material_boundary",
          "condition": "the actual receipt establishes a material scope, architecture, requirement, or design boundary",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "CONDITIONAL_RECOVERY",
          "route_steps": [
            "OPS-30 -> RS-10",
            "RS-10 complete proposal -> RS-20",
            "RS-20 REVISION_REQUIRED -> RS-30"
          ],
          "source_evidence": {
            "path": "candidate/prompts/c/OPS-30.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "REJECT"
      ],
      "to": "RS-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "PR-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "DRAFT",
            "BLOCKED"
          ],
          "branch_id": "instruction_terminal",
          "condition": "accepted manual prerequisite or true source/authority/product decision has no runnable prompt receiver",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/PR-10.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "DRAFT",
        "BLOCKED"
      ],
      "to": "ACTUAL_OWNER_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "PR-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "DRAFT",
            "BLOCKED"
          ],
          "branch_id": "upstream_owner_recovery",
          "condition": "the defective upstream Plan, review, remediation, Specification, or other source has an exact native owner",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "CONDITIONAL_RECOVERY",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/PR-10.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "DRAFT",
        "BLOCKED"
      ],
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "COMPLETE_DYNAMIC_NATIVE_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "PR-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "DRAFT",
            "BLOCKED"
          ],
          "branch_id": "same_owner_recovery",
          "condition": "an ordinary instruction defect is repairable by the same PR-10 owner",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "CONDITIONAL_RECOVERY",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/PR-10.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "DRAFT",
        "BLOCKED"
      ],
      "to": "PR-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "PR-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "INSTRUCTION_READY"
          ],
          "branch_id": "instruction_ready",
          "condition": "complete approved-scope instruction is ready for detailed planning",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/PR-10.md",
            "section": "Required result and routing"
          },
          "state": "INSTRUCTION_READY",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "INSTRUCTION_READY"
      ],
      "to": "PR-20",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "PR-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "DRAFT",
            "BLOCKED"
          ],
          "branch_id": "material_boundary",
          "condition": "a genuine material scope, architecture, requirement, or design boundary is substantiated",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "CONDITIONAL_RECOVERY",
          "route_steps": [
            "PR-10 -> RS-10",
            "RS-10 complete proposal -> RS-20"
          ],
          "source_evidence": {
            "path": "candidate/prompts/c/PR-10.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "DRAFT",
        "BLOCKED"
      ],
      "to": "RS-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "PR-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "DRAFT",
            "BLOCKED"
          ],
          "branch_id": "planning_terminal",
          "condition": "accepted manual prerequisite or true source/authority/product decision has no runnable prompt receiver",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/PR-20.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "DRAFT",
        "BLOCKED"
      ],
      "to": "ACTUAL_OWNER_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "PR-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "AWAITING_PO_PROCEED"
          ],
          "branch_id": "awaiting_po_proceed",
          "condition": "one complete executable approved-scope plan awaits the original Product Owner Proceed",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/PR-20.md",
            "section": "Required result and routing"
          },
          "state": "AWAITING_PO_PROCEED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "AWAITING_PO_PROCEED"
      ],
      "to": "NATHAN_PROCEED",
      "to_kind": "boundary",
      "transport": "MANUAL_PRODUCT_OWNER_BOUNDARY"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "PR-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "DRAFT",
            "BLOCKED"
          ],
          "branch_id": "upstream_owner_recovery",
          "condition": "the exact upstream instruction, Plan, remediation, Specification, or other source owner must act",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "CONDITIONAL_RECOVERY",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/PR-20.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "DRAFT",
        "BLOCKED"
      ],
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "COMPLETE_DYNAMIC_NATIVE_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "PR-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "DRAFT",
            "BLOCKED"
          ],
          "branch_id": "same_owner_recovery",
          "condition": "a bounded planning defect is repairable by the same dedicated PR planning session",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "CONDITIONAL_RECOVERY",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/PR-20.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "DRAFT",
        "BLOCKED"
      ],
      "to": "PR-20",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "PR-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "DRAFT",
            "BLOCKED"
          ],
          "branch_id": "material_boundary",
          "condition": "the planning result substantiates a material scope, architecture, requirement, or design boundary",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "CONDITIONAL_RECOVERY",
          "route_steps": [
            "PR-20 -> RS-10",
            "RS-10 complete proposal -> RS-20"
          ],
          "source_evidence": {
            "path": "candidate/prompts/c/PR-20.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "DRAFT",
        "BLOCKED"
      ],
      "to": "RS-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "PR-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "PRODUCT_OWNER_DECISION_REQUIRED"
          ],
          "branch_id": "product_owner_decision_required",
          "condition": "genuine Product Owner decision outside existing PR authority",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/PR-30.md",
            "section": "Required result and routing"
          },
          "state": "PRODUCT_OWNER_DECISION_REQUIRED",
          "terminal_for_invocation": true
        },
        {
          "applicable_states": [],
          "branch_id": "pr30_terminal",
          "condition": "unrecoverable source, owner, authority, or incompatible identity; never convert this into PR-50",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/PR-30.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "PRODUCT_OWNER_DECISION_REQUIRED"
      ],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "PR-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "RECOVERY_PENDING"
          ],
          "branch_id": "recovery_pending",
          "condition": "complete same-session re-entry; no new vehicle",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/PR-30.md",
            "section": "Required result and routing"
          },
          "state": "RECOVERY_PENDING",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "RECOVERY_PENDING"
      ],
      "to": "PR-30",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "PR-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "PR_CANDIDATE_PUBLISHED"
          ],
          "branch_id": "pr_candidate_published",
          "condition": "one complete same-session phase continuation",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/PR-30.md",
            "section": "Required result and routing"
          },
          "state": "PR_CANDIDATE_PUBLISHED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "PR_CANDIDATE_PUBLISHED"
      ],
      "to": "PR-35",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "PR-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "RESCOPE_PENDING"
          ],
          "branch_id": "rescope_pending",
          "condition": "formal RESCOPE_REQUEST with exact PR_RETURN_PHASE",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/PR-30.md",
            "section": "Required result and routing"
          },
          "state": "RESCOPE_PENDING",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "RESCOPE_PENDING"
      ],
      "to": "RS-20",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "PR-35",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "MERGE_PENDING"
          ],
          "branch_id": "merge_pending",
          "condition": "conditional PR-40 invocation usable only after Nathan manually merges",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/PR-35.md",
            "section": "Required result and routing"
          },
          "state": "MERGE_PENDING",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "MERGE_PENDING"
      ],
      "to": "NATHAN_MANUAL_MERGE_ASSERTION",
      "to_kind": "boundary",
      "transport": "MANUAL_PRODUCT_OWNER_BOUNDARY"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "PR-35",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "PRODUCT_OWNER_DECISION_REQUIRED"
          ],
          "branch_id": "product_owner_decision_required",
          "condition": "genuine Product Owner decision outside existing PR authority",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/PR-35.md",
            "section": "Required result and routing"
          },
          "state": "PRODUCT_OWNER_DECISION_REQUIRED",
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "PRODUCT_OWNER_DECISION_REQUIRED"
      ],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "PR-35",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "RECOVERY_PENDING"
          ],
          "branch_id": "recovery_pending",
          "condition": "complete same-session re-entry with checkpoint",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/PR-35.md",
            "section": "Required result and routing"
          },
          "state": "RECOVERY_PENDING",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "REMOTE_EVIDENCE_PENDING"
          ],
          "branch_id": "remote_evidence_pending",
          "condition": "actual remote evidence unavailable and no local action remains; durable checkpoint required",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/PR-35.md",
            "section": "Required result and routing"
          },
          "state": "REMOTE_EVIDENCE_PENDING",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "RECOVERY_PENDING",
        "REMOTE_EVIDENCE_PENDING"
      ],
      "to": "PR-35",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "PR-35",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "RESCOPE_PENDING"
          ],
          "branch_id": "rescope_pending",
          "condition": "formal RESCOPE_REQUEST with PR_RETURN_PHASE=PR-35",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/PR-35.md",
            "section": "Required result and routing"
          },
          "state": "RESCOPE_PENDING",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "RESCOPE_PENDING"
      ],
      "to": "RS-20",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "PR-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "PENDING"
          ],
          "branch_id": "pending_terminal",
          "condition": "manual merge, repository fact, review result, or evidence remains unavailable and no runnable native owner prompt is resolved",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/PR-40.md",
            "section": "Required result and routing"
          },
          "state": "PENDING",
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "PENDING"
      ],
      "to": "ACTUAL_OWNER_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "PR-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [],
          "branch_id": "lineage_review_terminal",
          "condition": "an in-scope correction lacks required repository authority/vehicle or another genuine Product Owner decision is required",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/PR-40.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "PR-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "ACCEPT"
          ],
          "branch_id": "accept",
          "condition": "return the accepted whole-unit result to the same whole-change IA/native Plan-progress owner",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/PR-40.md",
            "section": "Required result and routing"
          },
          "state": "ACCEPT",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "PENDING"
          ],
          "branch_id": "pending_native_owner",
          "condition": "the exact Product Owner, evidence, PR, or IA recovery owner is known and can perform the bounded missing act",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/PR-40.md",
            "section": "Required result and routing"
          },
          "state": "PENDING",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "ACCEPT",
        "PENDING"
      ],
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "COMPLETE_DYNAMIC_NATIVE_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "PR-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "REJECT"
          ],
          "branch_id": "reject_instruction_owner",
          "condition": "the substantiated in-scope defect is in the IA-issued PR instruction",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/PR-40.md",
            "section": "Required result and routing"
          },
          "state": "REJECT",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "REJECT"
      ],
      "to": "PR-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "PR-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "REJECT"
          ],
          "branch_id": "reject_existing_pr_owner",
          "condition": "a precise in-scope implementation/review/corrected-code/PR-lineage defect has an authorized existing PR vehicle and original Proceed",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/PR-40.md",
            "section": "Required result and routing"
          },
          "state": "REJECT",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "REJECT"
      ],
      "to": "PR-30",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "PR-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "REJECT"
          ],
          "branch_id": "reject_material_boundary_proposal",
          "condition": "a substantiated material boundary requires a new bounded rescope proposal",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [
            "PR-40 -> RS-10",
            "RS-10 complete proposal -> RS-20",
            "RS-20 REVISION_REQUIRED -> RS-30"
          ],
          "source_evidence": {
            "path": "candidate/prompts/c/PR-40.md",
            "section": "Required result and routing"
          },
          "state": "REJECT",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "REJECT"
      ],
      "to": "RS-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "PR-50",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "PR_ABORTED_ESCALATED"
          ],
          "branch_id": "pr_aborted_escalated",
          "condition": "terminal record after Nathan-only identified-PR invocation",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/PR-50.md",
            "section": "Required result and routing"
          },
          "state": "PR_ABORTED_ESCALATED",
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "PR_ABORTED_ESCALATED"
      ],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "ASSESSMENT_INCOMPLETE"
          ],
          "branch_id": "qa10_terminal",
          "condition": "manual prerequisite, source/authority stop, or unresolved evidence owner prevents a runnable continuation",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/QA-10.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "ASSESSMENT_INCOMPLETE"
      ],
      "to": "ACTUAL_OWNER_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "NOT_READY"
          ],
          "branch_id": "not_ready",
          "condition": "evidence proves failure of an applicable approved Plan objective",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/QA-10.md",
            "section": "Required result and routing"
          },
          "state": "NOT_READY",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "NOT_READY"
      ],
      "to": "ESC-30",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "ASSESSMENT_INCOMPLETE"
          ],
          "branch_id": "evidence_owner_recovery",
          "condition": "the exact evidence/retrieval owner is identified and can perform the smallest supported recovery",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/QA-10.md",
            "section": "Required result and routing"
          },
          "state": "ASSESSMENT_INCOMPLETE",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "NOT_READY",
            "ASSESSMENT_INCOMPLETE"
          ],
          "branch_id": "material_native_boundary",
          "condition": "a substantiated material scope, Canon, Specification, Plan, or authority boundary has an exact native owner",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "CONDITIONAL_RECOVERY",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/QA-10.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "ASSESSMENT_INCOMPLETE",
        "NOT_READY"
      ],
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "COMPLETE_DYNAMIC_NATIVE_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "READY_FOR_QA"
          ],
          "branch_id": "ready_for_qa",
          "condition": "complete integrated audit/triage/readiness supports live QA Guide creation",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/c/QA-10.md",
            "section": "Required result and routing"
          },
          "state": "READY_FOR_QA",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "READY_FOR_QA"
      ],
      "to": "QA-20",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-100",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [],
          "branch_id": "shared_source_authority_terminal",
          "condition": "true source, authority, identity, or owner stop with no runnable selected receiver; preserve evidence and return without a handoff",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-100.md",
            "section": "Terminal operator return and receiver compatibility"
          },
          "state": null,
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-100",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "COMPLETE"
          ],
          "branch_id": "complete",
          "condition": "execution receipt always returns to evidence reviewer",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-100.md",
            "section": "Required result and routing"
          },
          "state": "COMPLETE",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "PARTIAL"
          ],
          "branch_id": "partial",
          "condition": "execution receipt always returns to evidence reviewer",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-100.md",
            "section": "Required result and routing"
          },
          "state": "PARTIAL",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "blocked",
          "condition": "execution receipt always returns to evidence reviewer",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-100.md",
            "section": "Required result and routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "FAILED"
          ],
          "branch_id": "failed",
          "condition": "execution receipt always returns to evidence reviewer",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-100.md",
            "section": "Required result and routing"
          },
          "state": "FAILED",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "NOT_EXECUTED"
          ],
          "branch_id": "not_executed",
          "condition": "execution receipt always returns to evidence reviewer",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-100.md",
            "section": "Required result and routing"
          },
          "state": "NOT_EXECUTED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "COMPLETE",
        "PARTIAL",
        "BLOCKED",
        "FAILED",
        "NOT_EXECUTED"
      ],
      "to": "QA-110",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-110",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "INCOMPLETE"
          ],
          "branch_id": "incomplete_terminal",
          "condition": "the evidence owner or required authority cannot be resolved into a runnable receiver",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-110.md",
            "section": "Required result and routing"
          },
          "state": "INCOMPLETE",
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "INCOMPLETE"
      ],
      "to": "ACTUAL_OWNER_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-110",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "ESCALATION_REQUIRED"
          ],
          "branch_id": "escalation_required",
          "condition": "material QA evidence finding requires the native QA escalation report",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-110.md",
            "section": "Required result and routing"
          },
          "state": "ESCALATION_REQUIRED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "ESCALATION_REQUIRED"
      ],
      "to": "ESC-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-110",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "INCOMPLETE"
          ],
          "branch_id": "incomplete_named_owner",
          "condition": "another exact evidence owner is identified; preserve QA-110 resume phase",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-110.md",
            "section": "Required result and routing"
          },
          "state": "INCOMPLETE",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "INCOMPLETE"
      ],
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "COMPLETE_DYNAMIC_NATIVE_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-110",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BOUNDED_RERUN_REQUIRED"
          ],
          "branch_id": "rerun_execution",
          "condition": "the authorized attempt-2 task is already complete and ready for execution",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-110.md",
            "section": "Required result and routing"
          },
          "state": "BOUNDED_RERUN_REQUIRED",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "INCOMPLETE"
          ],
          "branch_id": "incomplete_execution_evidence",
          "condition": "the exact missing evidence is lawfully producible by bounded QA execution",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-110.md",
            "section": "Required result and routing"
          },
          "state": "INCOMPLETE",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "BOUNDED_RERUN_REQUIRED",
        "INCOMPLETE"
      ],
      "to": "QA-100",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-110",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "ACCEPT"
          ],
          "branch_id": "accept",
          "condition": "the complete approved QA run requires final reporting, including a completed failing run; the union of selected collections is reconciled to every required Plan step and requirement, not merely a completed subset",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-110.md",
            "section": "Required result and routing"
          },
          "state": "ACCEPT",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "ACCEPT"
      ],
      "to": "QA-120",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-110",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BOUNDED_RERUN_REQUIRED"
          ],
          "branch_id": "rerun_task_authoring",
          "condition": "a new selected attempt-2 execution task still must be authored",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-110.md",
            "section": "Required result and routing"
          },
          "state": "BOUNDED_RERUN_REQUIRED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "BOUNDED_RERUN_REQUIRED"
      ],
      "to": "QA-90",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-120",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "PASS"
          ],
          "branch_id": "pass_crd",
          "change_class": "CRD",
          "condition": "PASS with verified existing CRD class, complete QA Report/RCA and the matching continuing-Isis closure intake",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "required_artifacts": [
            "QA_REPORT",
            "QA_RCA"
          ],
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-120.md",
            "section": "Required result and routing"
          },
          "state": "PASS",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "PASS"
      ],
      "to": "CL-C-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-120",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "PASS"
          ],
          "branch_id": "pass_epic",
          "change_class": "EPIC",
          "condition": "PASS with verified existing EPIC class, complete QA Report/RCA and the matching continuing-Isis closure intake",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "required_artifacts": [
            "QA_REPORT",
            "QA_RCA"
          ],
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-120.md",
            "section": "Required result and routing"
          },
          "state": "PASS",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "PASS"
      ],
      "to": "CL-E-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-120",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "FAIL"
          ],
          "branch_id": "fail",
          "condition": "final QA Report/RCA demonstrates a material failure requiring escalation",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-120.md",
            "section": "Required result and routing"
          },
          "state": "FAIL",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "FAIL"
      ],
      "to": "ESC-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-120",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [],
          "branch_id": "shared_source_authority_terminal",
          "condition": "true source, authority, identity, or owner stop with no runnable selected receiver; preserve evidence and return without a handoff",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-120.md",
            "section": "Terminal operator return and receiver compatibility"
          },
          "state": null,
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-120",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "INTERIM"
          ],
          "branch_id": "interim_evidence_review",
          "condition": "remaining evidence requires Kronos classification",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-120.md",
            "section": "Required result and routing"
          },
          "state": "INTERIM",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "INTERIM"
      ],
      "to": "QA-110",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-120",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "INTERIM"
          ],
          "branch_id": "interim_task_authoring",
          "condition": "an unissued selected instruction or authorized retry task must be authored",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-120.md",
            "section": "Required result and routing"
          },
          "state": "INTERIM",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "INTERIM"
      ],
      "to": "QA-90",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [],
          "branch_id": "shared_source_authority_terminal",
          "condition": "true source, authority, identity, or owner stop with no runnable selected receiver; preserve evidence and return without a handoff",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-20.md",
            "section": "Terminal operator return and receiver compatibility"
          },
          "state": null,
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "blocked",
          "condition": "material readiness invalidation or recoverable QA-10 evidence gap requires same-Isis reassessment",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-20.md",
            "section": "Required result and routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "BLOCKED"
      ],
      "to": "QA-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "GUIDE_READY"
          ],
          "branch_id": "guide_ready",
          "condition": "complete live QA Guide is ready for whole-change QA Audit/Plan",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-20.md",
            "section": "Required result and routing"
          },
          "state": "GUIDE_READY",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "GUIDE_READY"
      ],
      "to": "QA-50",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-50",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [],
          "branch_id": "qa50_terminal",
          "condition": "true source or authority stop has no runnable receiver",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-50.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-50",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "AUDIT_COMPLETE"
          ],
          "branch_id": "audit_complete",
          "condition": "QA Audit is complete but a recoverable interruption prevented Plan completion",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-50.md",
            "section": "Required result and routing"
          },
          "state": "AUDIT_COMPLETE",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "blocked_plan_recovery",
          "condition": "Audit is complete and the planning gap is recoverable",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-50.md",
            "section": "Required result and routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "AUDIT_COMPLETE",
        "BLOCKED"
      ],
      "to": "QA-60",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-50",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "PLAN_PENDING"
          ],
          "branch_id": "plan_pending",
          "condition": "both QA Audit and QA Plan are complete and separately read back",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-50.md",
            "section": "Required result and routing"
          },
          "state": "PLAN_PENDING",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "blocked_complete_pending_plan",
          "condition": "the pending QA Plan is complete and ready for review",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-50.md",
            "section": "Required result and routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "PLAN_PENDING",
        "BLOCKED"
      ],
      "to": "QA-70",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-50",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "blocked_initial_denial",
          "condition": "an initial pending QA Plan was denied by QA-70 with exact redlines",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-50.md",
            "section": "Required result and routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "BLOCKED"
      ],
      "to": "QA-80",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-50",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [],
          "branch_id": "existing_approval_reuse",
          "condition": "a subsequent still-valid actual QA-70 approval of this exact Plan already exists and its complete native task-creation intake is available; preserve Isis decision and same Kronos lineage without new Plan/review/task execution",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "CONDITIONAL_RECOVERY",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-50.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [],
      "to": "QA-90",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-60",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "BLOCKED"
          ],
          "branch_id": "blocked",
          "condition": "unique source failure, approved-base rewrite request, unrecoverable authority conflict, or missing decisive Audit",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-60.md",
            "section": "Required result and routing"
          },
          "state": "BLOCKED",
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "BLOCKED"
      ],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-60",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "PLAN_PENDING"
          ],
          "branch_id": "plan_pending",
          "condition": "complete QA Plan returns to continuing Isis review",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-60.md",
            "section": "Required result and routing"
          },
          "state": "PLAN_PENDING",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "PLAN_PENDING"
      ],
      "to": "QA-70",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-60",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [],
          "branch_id": "existing_revision_reuse",
          "condition": "actual initial QA-70 denial or bounded redline review of this exact Plan already exists with complete review/Audit/upstream intake and same Kronos author lineage",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "CONDITIONAL_RECOVERY",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-60.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [],
      "to": "QA-80",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-60",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [],
          "branch_id": "existing_approval_reuse",
          "condition": "a subsequent still-valid actual QA-70 approval of this exact Plan already exists and its complete native task-creation intake is available; preserve Isis decision and same Kronos lineage without new Plan/review/task execution",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "CONDITIONAL_RECOVERY",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-60.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [],
      "to": "QA-90",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-70",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "APPROVE"
          ],
          "branch_id": "delta_approve",
          "condition": "REVIEW_MODE=DELTA; exactly one addendum and conditional post-drain native continuation",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-70.md",
            "section": "Required result and routing"
          },
          "state": "APPROVE",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "APPROVE"
      ],
      "to": "NATHAN_MANUAL_PF10_DRAIN",
      "to_kind": "boundary",
      "transport": "MANUAL_PRODUCT_OWNER_BOUNDARY"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-70",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [],
          "branch_id": "qa70_terminal",
          "condition": "source, authority, mode, or continuation identity is unresolved",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-70.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-70",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "DENY"
          ],
          "branch_id": "delta_deny",
          "condition": "REVIEW_MODE=DELTA; return denial to the exact originating proposed-delta owner; no addendum",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-70.md",
            "section": "Required result and routing"
          },
          "state": "DENY",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "DENY"
      ],
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "COMPLETE_DYNAMIC_NATIVE_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-70",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "DENY"
          ],
          "branch_id": "initial_deny",
          "condition": "REVIEW_MODE=INITIAL; exact redlines return to the same Kronos author; no addendum",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-70.md",
            "section": "Required result and routing"
          },
          "state": "DENY",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "DENY"
      ],
      "to": "QA-80",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-70",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "APPROVE"
          ],
          "branch_id": "initial_approve",
          "condition": "REVIEW_MODE=INITIAL; approve the pending QA Plan; no addendum",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-70.md",
            "section": "Required result and routing"
          },
          "state": "APPROVE",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "APPROVE"
      ],
      "to": "QA-90",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-80",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "WRONG_ROUTE_APPROVED_BASE"
          ],
          "branch_id": "wrong_route_terminal",
          "condition": "approved-base rewrite refused and a complete lawful bounded-delta review intake is absent; identify the actual proposal owner without inventing a delta",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-80.md",
            "section": "Required result and routing"
          },
          "state": "WRONG_ROUTE_APPROVED_BASE",
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "WRONG_ROUTE_APPROVED_BASE"
      ],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-80",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "PLAN_PENDING_REVISED"
          ],
          "branch_id": "plan_pending_revised",
          "condition": "complete corrected pending preapproval QA Plan returns to the same Isis reviewer",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-80.md",
            "section": "Required result and routing"
          },
          "state": "PLAN_PENDING_REVISED",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "WRONG_ROUTE_APPROVED_BASE"
          ],
          "branch_id": "existing_delta_review",
          "condition": "approved-base rewrite refused but a complete existing explicit bounded delta, actual author, approval lineage and current PF10/addenda satisfy QA-70 APPROVED_QA_PLAN_DELTA_REVIEW intake; carry the existing delta unchanged",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-80.md",
            "section": "Required result and routing"
          },
          "state": "WRONG_ROUTE_APPROVED_BASE",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "PLAN_PENDING_REVISED",
        "WRONG_ROUTE_APPROVED_BASE"
      ],
      "to": "QA-70",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-90",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "ESCALATION_REQUIRED"
          ],
          "branch_id": "escalation_required",
          "condition": "material pre-execution defect; create the native QA escalation report",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-90.md",
            "section": "Required result and routing"
          },
          "state": "ESCALATION_REQUIRED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "ESCALATION_REQUIRED"
      ],
      "to": "ESC-10",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-90",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [],
          "branch_id": "shared_source_authority_terminal",
          "condition": "true source, authority, identity, or owner stop with no runnable selected receiver; preserve evidence and return without a handoff",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-90.md",
            "section": "Terminal operator return and receiver compatibility"
          },
          "state": null,
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-90",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "TASK_READY"
          ],
          "branch_id": "task_ready",
          "condition": "bounded QA execution task is complete",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-90.md",
            "section": "Required result and routing"
          },
          "state": "TASK_READY",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "TASK_READY"
      ],
      "to": "QA-100",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "QA-90",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "NOT_EXECUTED"
          ],
          "branch_id": "not_executed",
          "condition": "preserve non-execution evidence for the QA evidence reviewer",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/QA-90.md",
            "section": "Required result and routing"
          },
          "state": "NOT_EXECUTED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "NOT_EXECUTED"
      ],
      "to": "QA-110",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "RS-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [],
          "branch_id": "shared_source_authority_terminal",
          "condition": "true source, authority, identity, or owner stop with no runnable selected receiver; preserve evidence and return without a handoff",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/RS-10.md",
            "section": "Terminal operator return and receiver compatibility"
          },
          "state": null,
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "RS-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [],
          "branch_id": "in_scope_native_return",
          "condition": "observed ordinary in-scope correction needs no rescope proposal or formal RS-20 decision; exact selected existing repair owner/session and complete native intake are resolved under unchanged authority; no PR-50, merge, PF10 drain or manual-gate bypass",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_OWNER_RETURN",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/RS-10.md",
            "section": "Required result and routing"
          },
          "state": null,
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [],
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "COMPLETE_DYNAMIC_NATIVE_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "RS-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "RESCOPE_PROPOSAL_PENDING_REVIEW"
          ],
          "branch_id": "rescope_proposal_pending_review",
          "condition": "a real bounded delta has a complete proposal and exact actual native-stage lineage; pre-Proceed planning does not require future Proceed, PR or execution-return-phase fields",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/RS-10.md",
            "section": "Required result and routing"
          },
          "state": "RESCOPE_PROPOSAL_PENDING_REVIEW",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "RESCOPE_PROPOSAL_PENDING_REVIEW"
      ],
      "to": "RS-20",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "RS-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "APPROVE"
          ],
          "branch_id": "approve",
          "condition": "exactly one addendum; conditional post-drain receiver selected only by PR_RETURN_PHASE",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [
            "RS-20 -> Nathan manual PF10 drain",
            "PR-30_PREPUBLICATION -> PR-30 fresh verification",
            "PR-30_POSTPUBLICATION or PR-35 -> RS-40 fresh verification",
            "non-PR -> exact original native stage fresh verification"
          ],
          "source_evidence": {
            "path": "candidate/prompts/d/RS-20.md",
            "section": "Required result and routing"
          },
          "state": "APPROVE",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "APPROVE"
      ],
      "to": "NATHAN_MANUAL_PF10_DRAIN",
      "to_kind": "boundary",
      "transport": "MANUAL_PRODUCT_OWNER_BOUNDARY"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "RS-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "SPECIFICATION_CHANGE_REQUIRED"
          ],
          "branch_id": "specification_change_required",
          "condition": "native Product Owner Specification-delta decision; no RS-20 addendum",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/RS-20.md",
            "section": "Required result and routing"
          },
          "state": "SPECIFICATION_CHANGE_REQUIRED",
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "SPECIFICATION_CHANGE_REQUIRED"
      ],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "RS-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "REJECT"
          ],
          "branch_id": "reject_native",
          "condition": "recorded origin is a non-PR native stage; unchanged authority; no addendum",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/RS-20.md",
            "section": "Required result and routing"
          },
          "state": "REJECT",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "IN_SCOPE_REPAIR"
          ],
          "branch_id": "in_scope_native",
          "condition": "existing repair owner is a non-PR native stage under unchanged authority; no addendum",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/RS-20.md",
            "section": "Required result and routing"
          },
          "state": "IN_SCOPE_REPAIR",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "REJECT",
        "IN_SCOPE_REPAIR"
      ],
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "COMPLETE_DYNAMIC_NATIVE_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "RS-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "REJECT"
          ],
          "branch_id": "reject_pr30",
          "condition": "recorded origin/phase is PR-30; unchanged authority; no addendum",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/RS-20.md",
            "section": "Required result and routing"
          },
          "state": "REJECT",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "IN_SCOPE_REPAIR"
          ],
          "branch_id": "in_scope_pr30",
          "condition": "existing repair owner/phase is PR-30 under the original Proceed; no addendum",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/RS-20.md",
            "section": "Required result and routing"
          },
          "state": "IN_SCOPE_REPAIR",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "REJECT",
        "IN_SCOPE_REPAIR"
      ],
      "to": "PR-30",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "RS-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "REJECT"
          ],
          "branch_id": "reject_pr35",
          "condition": "recorded origin/phase is PR-35; unchanged authority; no addendum",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/RS-20.md",
            "section": "Required result and routing"
          },
          "state": "REJECT",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "IN_SCOPE_REPAIR"
          ],
          "branch_id": "in_scope_pr35",
          "condition": "existing repair owner/phase is PR-35 under the original Proceed; no addendum",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/RS-20.md",
            "section": "Required result and routing"
          },
          "state": "IN_SCOPE_REPAIR",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "REJECT",
        "IN_SCOPE_REPAIR"
      ],
      "to": "PR-35",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "RS-20",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "REVISION_REQUIRED"
          ],
          "branch_id": "revision_required",
          "condition": "same request/proposal author; no addendum",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/RS-20.md",
            "section": "Required result and routing"
          },
          "state": "REVISION_REQUIRED",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "REVISION_REQUIRED"
      ],
      "to": "RS-30",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "RS-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "RESCOPE_PROPOSAL_PENDING_REVIEW"
          ],
          "branch_id": "product_owner_revision_return",
          "condition": "actual correction authority is Nathan and no exact native decision route is already supplied; preserve his decision ownership and emit no continuation block",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/RS-30.md",
            "section": "Required result and routing"
          },
          "state": "RESCOPE_PROPOSAL_PENDING_REVIEW",
          "terminal_for_invocation": true
        },
        {
          "applicable_states": [],
          "branch_id": "revision_source_terminal",
          "condition": "source, exact correction authority, target or owner identity is missing; preserve valid artifact and return the exact gap",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "TERMINAL_EXCEPTION",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/RS-30.md",
            "section": "Required inputs"
          },
          "state": null,
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "RESCOPE_PROPOSAL_PENDING_REVIEW"
      ],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "RS-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "RESCOPE_PROPOSAL_PENDING_REVIEW"
          ],
          "branch_id": "product_owner_explicit_native_return",
          "condition": "Nathan already supplied one exact selected native decision route with complete intake; preserve actual owner, same artifact type and manual gates; never invent IA approval, route PR-50 or bypass Alpha, merge or PF10 controls",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/RS-30.md",
            "section": "Required result and routing"
          },
          "state": "RESCOPE_PROPOSAL_PENDING_REVIEW",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "RESCOPE_PROPOSAL_PENDING_REVIEW"
      ],
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "COMPLETE_DYNAMIC_NATIVE_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "RS-30",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "RESCOPE_PROPOSAL_PENDING_REVIEW"
          ],
          "branch_id": "ia_revision_return",
          "condition": "actual correction authority is RS-20 REVISION_REQUIRED; preserve RESCOPE_REQUEST vs RESCOPE_PROPOSAL type and return to the same IA decision owner",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/RS-30.md",
            "section": "Required result and routing"
          },
          "state": "RESCOPE_PROPOSAL_PENDING_REVIEW",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "RESCOPE_PROPOSAL_PENDING_REVIEW"
      ],
      "to": "RS-20",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "RS-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "MERGE_PENDING"
          ],
          "branch_id": "merge_pending",
          "condition": "recorded PR-35 phase result; historical pre-merge evidence",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/RS-40.md",
            "section": "Required result and routing"
          },
          "state": "MERGE_PENDING",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "MERGE_PENDING"
      ],
      "to": "NATHAN_MANUAL_MERGE_ASSERTION",
      "to_kind": "boundary",
      "transport": "MANUAL_PRODUCT_OWNER_BOUNDARY"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "RS-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "SOURCE_RESOLUTION_ERROR"
          ],
          "branch_id": "source_resolution_error",
          "condition": "unique current controlled PF10 Markdown unresolved; make no drain inference",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/RS-40.md",
            "section": "Required result and routing"
          },
          "state": "SOURCE_RESOLUTION_ERROR",
          "terminal_for_invocation": true
        },
        {
          "applicable_states": [
            "MANUAL_DRAIN_REQUIRED"
          ],
          "branch_id": "manual_drain_required",
          "condition": "current PF10 read; exact anchor absent",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/RS-40.md",
            "section": "Required result and routing"
          },
          "state": "MANUAL_DRAIN_REQUIRED",
          "terminal_for_invocation": true
        },
        {
          "applicable_states": [
            "MANUAL_DRAIN_MISMATCH"
          ],
          "branch_id": "manual_drain_mismatch",
          "condition": "related content differs in decision/base/normalized delta or a later conflicting overlay exists",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/RS-40.md",
            "section": "Required result and routing"
          },
          "state": "MANUAL_DRAIN_MISMATCH",
          "terminal_for_invocation": true
        },
        {
          "applicable_states": [
            "PRODUCT_OWNER_DECISION_REQUIRED"
          ],
          "branch_id": "product_owner_decision_required",
          "condition": "genuine Product Owner decision or unrecoverable authority conflict",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/RS-40.md",
            "section": "Required result and routing"
          },
          "state": "PRODUCT_OWNER_DECISION_REQUIRED",
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "SOURCE_RESOLUTION_ERROR",
        "MANUAL_DRAIN_REQUIRED",
        "MANUAL_DRAIN_MISMATCH",
        "PRODUCT_OWNER_DECISION_REQUIRED"
      ],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "RS-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "RECOVERY_PENDING"
          ],
          "branch_id": "recovery_pr30",
          "condition": "recorded resumed phase is PR-30_POSTPUBLICATION; same session/vehicle re-entry",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/RS-40.md",
            "section": "Required result and routing"
          },
          "state": "RECOVERY_PENDING",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "RECOVERY_PENDING"
      ],
      "to": "PR-30",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "RS-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "PR_CANDIDATE_PUBLISHED"
          ],
          "branch_id": "pr_candidate_published",
          "condition": "recorded PR-30_POSTPUBLICATION phase result",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/RS-40.md",
            "section": "Required result and routing"
          },
          "state": "PR_CANDIDATE_PUBLISHED",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "RECOVERY_PENDING"
          ],
          "branch_id": "recovery_pr35",
          "condition": "recorded resumed phase is PR-35; same session/vehicle re-entry",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/RS-40.md",
            "section": "Required result and routing"
          },
          "state": "RECOVERY_PENDING",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "REMOTE_EVIDENCE_PENDING"
          ],
          "branch_id": "remote_evidence_pending",
          "condition": "PR-35 only; durable checkpoint",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/RS-40.md",
            "section": "Required result and routing"
          },
          "state": "REMOTE_EVIDENCE_PENDING",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "PR_CANDIDATE_PUBLISHED",
        "RECOVERY_PENDING",
        "REMOTE_EVIDENCE_PENDING"
      ],
      "to": "PR-35",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "RS-40",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "RESCOPE_PENDING"
          ],
          "branch_id": "rescope_pending",
          "condition": "new formal RESCOPE_REQUEST preserves same vehicle",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/RS-40.md",
            "section": "Required result and routing"
          },
          "state": "RESCOPE_PENDING",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "RESCOPE_PENDING"
      ],
      "to": "RS-20",
      "to_kind": "prompt",
      "transport": "COMPLETE_NEXT_PROMPT_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "UTIL-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "INCOMPLETE"
          ],
          "branch_id": "incomplete_terminal",
          "condition": "no selected native receiver can be resolved; do not invent one",
          "next_prompt_handoff_count": 0,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/UTIL-10.md",
            "section": "Required result and routing"
          },
          "state": "INCOMPLETE",
          "terminal_for_invocation": true
        }
      ],
      "state_predicates": [
        "INCOMPLETE"
      ],
      "to": "NATHAN_TERMINAL_RETURN",
      "to_kind": "boundary",
      "transport": "TERMINAL_RETURN_NO_HANDOFF"
    },
    {
      "actual_branch_cardinality": "EXACTLY_ONE_BRANCH_PER_ACTUAL_RESULT",
      "automatic": false,
      "from": "UTIL-10",
      "from_kind": "prompt",
      "immediate": true,
      "route_branches": [
        {
          "applicable_states": [
            "COMPLETE"
          ],
          "branch_id": "complete",
          "condition": "return the revised artifact and report to the exact original decision/review owner",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/UTIL-10.md",
            "section": "Required result and routing"
          },
          "state": "COMPLETE",
          "terminal_for_invocation": false
        },
        {
          "applicable_states": [
            "INCOMPLETE"
          ],
          "branch_id": "incomplete_native_owner",
          "condition": "return the checkpoint to the exact redline/artifact owner when a selected native receiver resolves",
          "next_prompt_handoff_count": 1,
          "public_result": true,
          "route_kind": "NATIVE_RESULT",
          "route_steps": [],
          "source_evidence": {
            "path": "candidate/prompts/d/UTIL-10.md",
            "section": "Required result and routing"
          },
          "state": "INCOMPLETE",
          "terminal_for_invocation": false
        }
      ],
      "state_predicates": [
        "COMPLETE",
        "INCOMPLETE"
      ],
      "to": "ORIGINAL_NATIVE_STAGE",
      "to_kind": "boundary",
      "transport": "COMPLETE_DYNAMIC_NATIVE_HANDOFF"
    }
  ],
  "handoff_contract": {
    "actual_branch_only": true,
    "complete_paste_ready_prompt": true,
    "fence_language": "text",
    "first_line": "NEXT_PROMPT_HANDOFF",
    "nonterminal_actual_result_next_prompt_handoff_blocks": 1,
    "prohibited": [
      "menu",
      "metadata-only summary",
      "blank form",
      "placeholder after publication",
      "Library ID",
      "unlinked filename",
      "above",
      "conversation reconstruction",
      "model/strength/reasoning/eligibility/suitability/account/configuration route"
    ],
    "required": [
      "exact selected prompt full name/version/direct Notion URL",
      "receiving role and exact session",
      "Epic/change and work unit",
      "direct Drive artifacts and repository/PR references",
      "status, completed work, decisions, constraints, unresolved items, preserved authority",
      "next action and expected output"
    ],
    "terminal_result_next_prompt_handoff_blocks": 0
  },
  "nodes": [
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb8119a5a8e4d083fcf360?pvs=204",
      "candidate_version": "091426.1",
      "id": "CF-C-10",
      "lane": "CF-C",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Prepare CRD Specification Kickoff Handoff for the exact supplied change.",
      "output_artifacts": [
        "SPECIFICATION_KICKOFF"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb81bf954dfd72c05caa31",
        "release": "GCFPE-20260913.1",
        "title": "CF-C-10 — Prepare CRD Specification Kickoff Handoff — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb81bf954dfd72c05caa31",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "CF-C-20"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are Master Scrum in the class-specific kickoff session.",
      "result_states": [
        "KICKOFF_READY",
        "BLOCKED"
      ],
      "sequence": 10,
      "session_class": "DEDICATED_ONE_OFF",
      "title": "CF-C-10 — Prepare CRD Specification Kickoff Handoff — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb8173a73edc73f302a90a?pvs=204",
      "candidate_version": "091426.1",
      "id": "CF-C-20",
      "lane": "CF-C",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Create CRD Specification for the exact supplied change.",
      "output_artifacts": [
        "CRD_SPECIFICATION"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb8173a162e1b06427c7bf",
        "release": "GCFPE-20260913.1",
        "title": "CF-C-20 — Create CRD Specification — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb8173a162e1b06427c7bf",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "CF-C-30"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are Isis, the continuing Lead Developer and Specification author.",
      "result_states": [
        "SPECIFICATION_PENDING",
        "BLOCKED"
      ],
      "sequence": 20,
      "session_class": "ROLE_CONTINUING",
      "title": "CF-C-20 — Create CRD Specification — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb8149a8d2ed42c9c01ffd?pvs=204",
      "candidate_version": "091426.1",
      "id": "CF-C-30",
      "lane": "CF-C",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Review an initial pending CRD Specification, assess a requested correction to an approved immutable CRD base, or review one pending bounded CRD Specification delta.",
      "output_artifacts": [
        "INITIAL_SPECIFICATION_REVIEW / SPECIFICATION_CORRECTION_ASSESSMENT / SPECIFICATION_DELTA_REVIEW",
        "CORRECTION_REDLINE"
      ],
      "pf10_addendum_role": "QUALIFYING_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb81d19cd5f7ffa80a5f09",
        "release": "GCFPE-20260913.1",
        "title": "CF-C-30 — Review and Approve CRD Specification — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb81d19cd5f7ffa80a5f09",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "IA-10",
        "CF-C-40"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are Thoth, Head of Development, in the same continuing review session for this change.",
      "result_states": [
        "INITIAL_APPROVE",
        "INITIAL_DENY",
        "CORRECTION_REDLINE",
        "DELTA_APPROVE",
        "DELTA_DENY"
      ],
      "sequence": 30,
      "session_class": "ROLE_CONTINUING",
      "title": "CF-C-30 — Review and Approve CRD Specification — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb81269931cee342ce8a0e?pvs=204",
      "candidate_version": "091426.1",
      "id": "CF-C-40",
      "lane": "CF-C",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Revise a pending CRD Specification, author the first bounded delta from a justified approved-base correction redline, or revise a denied pending delta.",
      "output_artifacts": [
        "CRD_SPECIFICATION / SPECIFICATION_DELTA"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb81d19536ff2d6eac93dc",
        "release": "GCFPE-20260913.1",
        "title": "CF-C-40 — Revise CRD Specification — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb81d19536ff2d6eac93dc",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "CF-C-30"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are Isis, the same continuing Specification author.",
      "result_states": [
        "SPECIFICATION_PENDING"
      ],
      "sequence": 40,
      "session_class": "ROLE_CONTINUING",
      "title": "CF-C-40 — Revise CRD Specification — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb815b84a5c5a5ace85fe1?pvs=204",
      "candidate_version": "091426.1",
      "id": "CF-E-10",
      "lane": "CF-E",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Prepare Epic Specification Kickoff Handoff for the exact supplied change.",
      "output_artifacts": [
        "SPECIFICATION_KICKOFF"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb811f927adfc2243861ff",
        "release": "GCFPE-20260913.1",
        "title": "CF-E-10 — Prepare Epic Specification Kickoff Handoff — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb811f927adfc2243861ff",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "CF-E-20"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are Master Scrum in the class-specific kickoff session.",
      "result_states": [
        "KICKOFF_READY",
        "BLOCKED"
      ],
      "sequence": 10,
      "session_class": "DEDICATED_ONE_OFF",
      "title": "CF-E-10 — Prepare Epic Specification Kickoff Handoff — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb810eb177f7dced41bc8f?pvs=204",
      "candidate_version": "091426.1",
      "id": "CF-E-20",
      "lane": "CF-E",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Create Epic Specification for the exact supplied change.",
      "output_artifacts": [
        "EPIC_SPECIFICATION"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb81b084acde09866a52db",
        "release": "GCFPE-20260913.1",
        "title": "CF-E-20 — Create Epic Specification — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb81b084acde09866a52db",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "CF-E-30"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are Isis, the continuing Lead Developer and Specification author.",
      "result_states": [
        "SPECIFICATION_PENDING",
        "BLOCKED"
      ],
      "sequence": 20,
      "session_class": "ROLE_CONTINUING",
      "title": "CF-E-20 — Create Epic Specification — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb81b4be79f405566da9a7?pvs=204",
      "candidate_version": "091426.1",
      "id": "CF-E-30",
      "lane": "CF-E",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Review an initial pending Epic Specification, assess a requested correction to an approved immutable Epic base, or review one pending bounded Epic Specification delta.",
      "output_artifacts": [
        "INITIAL_SPECIFICATION_REVIEW / SPECIFICATION_CORRECTION_ASSESSMENT / SPECIFICATION_DELTA_REVIEW",
        "CORRECTION_REDLINE"
      ],
      "pf10_addendum_role": "QUALIFYING_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb817c918ac77bad1bfc97",
        "release": "GCFPE-20260913.1",
        "title": "CF-E-30 — Review and Approve Epic Specification — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb817c918ac77bad1bfc97",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "IA-10",
        "CF-E-40"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are Thoth, Head of Development, in the same continuing review session for this change.",
      "result_states": [
        "INITIAL_APPROVE",
        "INITIAL_DENY",
        "CORRECTION_REDLINE",
        "DELTA_APPROVE",
        "DELTA_DENY"
      ],
      "sequence": 30,
      "session_class": "ROLE_CONTINUING",
      "title": "CF-E-30 — Review and Approve Epic Specification — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb8101b655ed223b11a85e?pvs=204",
      "candidate_version": "091426.1",
      "id": "CF-E-40",
      "lane": "CF-E",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Revise a pending Epic Specification, author the first bounded delta from a justified approved-base correction redline, or revise a denied pending delta.",
      "output_artifacts": [
        "EPIC_SPECIFICATION / SPECIFICATION_DELTA"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb81ba9fcad5e656614e30",
        "release": "GCFPE-20260913.1",
        "title": "CF-E-40 — Revise Epic Specification — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb81ba9fcad5e656614e30",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "CF-E-30"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are Isis, the same continuing Specification author.",
      "result_states": [
        "SPECIFICATION_PENDING"
      ],
      "sequence": 40,
      "session_class": "ROLE_CONTINUING",
      "title": "CF-E-40 — Revise Epic Specification — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb8161b4d7cb6d07f5101c?pvs=204",
      "candidate_version": "091426.1",
      "id": "CF-PO-10",
      "lane": "CF-PO",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Record Product Owner Change-Class Selection for the exact supplied change.",
      "output_artifacts": [
        "CHANGE_CLASS_SELECTION"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb8175b86cdfc3d7fc40c7",
        "release": "GCFPE-20260913.1",
        "title": "CF-PO-10 — Record Product Owner Change-Class Selection — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb8175b86cdfc3d7fc40c7",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "CF-E-10",
        "CF-C-10"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are the recording assistant in the Product Owner context.",
      "result_states": [
        "CLASS_SELECTED"
      ],
      "sequence": 10,
      "session_class": "DEDICATED_ONE_OFF",
      "title": "CF-PO-10 — Record Product Owner Change-Class Selection — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb81f4812be61e8877c02c?pvs=204",
      "candidate_version": "091426.1",
      "id": "CL-20",
      "lane": "CL",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Prepare Post-Closure Drainage and Closure Memo for the exact supplied change.",
      "output_artifacts": [
        "CLOSURE_MEMO / POST_CLOSURE_DRAINAGE"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb81a2a0c9c98f719350a1",
        "release": "GCFPE-20260913.1",
        "title": "CL-20 — Prepare Post-Closure Drainage and Closure Memo — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb81a2a0c9c98f719350a1",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "CL-30",
        "CL-E-20",
        "CL-E-40",
        "CL-40"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are Isis, after the positive terminal closure decision.",
      "result_states": [
        "POST_CLOSURE_PENDING"
      ],
      "sequence": 20,
      "session_class": "ROLE_CONTINUING",
      "title": "CL-20 — Prepare Post-Closure Drainage and Closure Memo — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb8190a444d8818e445c1d?pvs=204",
      "candidate_version": "091426.1",
      "id": "CL-30",
      "lane": "CL",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Prepare Conditional Post-Change ADR Maintenance for the exact supplied change.",
      "output_artifacts": [
        "ADR_CANDIDATE / NO_ADR_NEEDED"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb818c8f90db54a25544b1",
        "release": "GCFPE-20260913.1",
        "title": "CL-30 — Prepare Conditional Post-Change ADR Maintenance — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb818c8f90db54a25544b1",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "CL-20",
        "CL-40"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are the explicitly assigned architecture documentation author.",
      "result_states": [
        "ADR_CANDIDATE",
        "NO_ADR_NEEDED"
      ],
      "sequence": 30,
      "session_class": "DEDICATED_ONE_OFF",
      "title": "CL-30 — Prepare Conditional Post-Change ADR Maintenance — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb81db9c88cde6027e07bf?pvs=204",
      "candidate_version": "091426.1",
      "id": "CL-40",
      "lane": "CL",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Scan for PF09 Gaps and CRD Candidates for the exact supplied change.",
      "output_artifacts": [
        "CYCLE_GAP_SCAN"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb815ba2e2fb45ba7d056f",
        "release": "GCFPE-20260913.1",
        "title": "CL-40 — Scan for PF09 Gaps and CRD Candidates — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb815ba2e2fb45ba7d056f",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are the same continuing Isis Lead Developer for the exact closed Epic or CRD change.",
      "result_states": [
        "COMPLETE",
        "INCOMPLETE"
      ],
      "sequence": 40,
      "session_class": "DEDICATED_ONE_OFF",
      "title": "CL-40 — Scan for PF09 Gaps and CRD Candidates — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb81ad8989faa77f441a64?pvs=204",
      "candidate_version": "091426.1",
      "id": "CL-C-10",
      "lane": "CL-C",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Perform CRD Retrospective and Decide Closure for the exact supplied change.",
      "output_artifacts": [
        "CHANGE_CLOSURE_DECISION"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb812bab7bf770bcef9527",
        "release": "GCFPE-20260913.1",
        "title": "CL-C-10 — Perform CRD Retrospective and Decide Closure — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb812bab7bf770bcef9527",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "CL-20",
        "ESC-30"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are Isis, continuing Lead Developer and terminal closure authority.",
      "result_states": [
        "CHANGE_CLOSED",
        "DO_NOT_CLOSE"
      ],
      "sequence": 10,
      "session_class": "ROLE_CONTINUING",
      "title": "CL-C-10 — Perform CRD Retrospective and Decide Closure — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb811a8578d75885c16cac?pvs=204",
      "candidate_version": "091426.1",
      "id": "CL-E-10",
      "lane": "CL-E",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Perform Epic Retrospective and Decide Closure for the exact supplied change.",
      "output_artifacts": [
        "CHANGE_CLOSURE_DECISION"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb8177bf3cd7c9c7ca39f7",
        "release": "GCFPE-20260913.1",
        "title": "CL-E-10 — Perform Epic Retrospective and Decide Closure — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb8177bf3cd7c9c7ca39f7",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "CL-20",
        "CL-E-20",
        "ESC-30"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are Isis, continuing Lead Developer and terminal closure authority.",
      "result_states": [
        "CHANGE_CLOSED",
        "DO_NOT_CLOSE"
      ],
      "sequence": 10,
      "session_class": "ROLE_CONTINUING",
      "title": "CL-E-10 — Perform Epic Retrospective and Decide Closure — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb81c2b5d5ff46126f9e45?pvs=204",
      "candidate_version": "091426.1",
      "id": "CL-E-20",
      "lane": "CL-E",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Perform Bounded PF09 Epic Revalidation for the exact supplied change.",
      "output_artifacts": [
        "PF09_REVALIDATION"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb8182bc57f512fe2fc79c",
        "release": "GCFPE-20260913.1",
        "title": "CL-E-20 — Perform Bounded PF09 Epic Revalidation — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb8182bc57f512fe2fc79c",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "CL-E-30"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are the explicitly assigned Lead Developer revalidation session, read-only.",
      "result_states": [
        "COMPLETE",
        "PARTIAL",
        "BLOCKED"
      ],
      "sequence": 20,
      "session_class": "DEDICATED_ONE_OFF",
      "title": "CL-E-20 — Perform Bounded PF09 Epic Revalidation — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb81b4a649fdcdb1903345?pvs=204",
      "candidate_version": "091426.1",
      "id": "CL-E-30",
      "lane": "CL-E",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Review Bounded PF09 Revalidation for the exact supplied change.",
      "output_artifacts": [
        "PF09_REVALIDATION_REVIEW"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb8170abede3b92037d246",
        "release": "GCFPE-20260913.1",
        "title": "CL-E-30 — Review Bounded PF09 Revalidation — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb8170abede3b92037d246",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "CL-E-40",
        "CL-E-20"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are the assigned reviewer of the bounded revalidation deliverable.",
      "result_states": [
        "ACCEPT",
        "DENY"
      ],
      "sequence": 30,
      "session_class": "DEDICATED_ONE_OFF",
      "title": "CL-E-30 — Review Bounded PF09 Revalidation — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb81e78e82f83a5f2e4b68?pvs=204",
      "candidate_version": "091426.1",
      "id": "CL-E-40",
      "lane": "CL-E",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Prepare Post-Epic PF09 Maintenance for the exact supplied change.",
      "output_artifacts": [
        "PF09_MAINTENANCE_CANDIDATE"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb8148a9cad59ae5bf98ae",
        "release": "GCFPE-20260913.1",
        "title": "CL-E-40 — Prepare Post-Epic PF09 Maintenance — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb8148a9cad59ae5bf98ae",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "CL-E-20",
        "CL-E-30",
        "CL-20",
        "CL-40"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are the assigned Lead Developer maintenance author.",
      "result_states": [
        "MAINTENANCE_PENDING"
      ],
      "sequence": 40,
      "session_class": "DEDICATED_ONE_OFF",
      "title": "CL-E-40 — Prepare Post-Epic PF09 Maintenance — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb8193a9a8d7ddd751cd2d?pvs=204",
      "candidate_version": "091426.1",
      "id": "DOC-10",
      "lane": "DOC",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Create Final Repository Documentation PR Instructions for the exact supplied change.",
      "output_artifacts": [
        "PR_INSTRUCTION"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb81e5b888c8c780244d0c",
        "release": "GCFPE-20260913.1",
        "title": "DOC-10 — Create Final Repository Documentation PR Instructions — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb81e5b888c8c780244d0c",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "PR-20"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are the same whole-change Implementation Agent (IA).",
      "result_states": [
        "INSTRUCTION_READY",
        "DRAFT",
        "PENDING",
        "BLOCKED"
      ],
      "sequence": 10,
      "session_class": "CHANGE_LIFETIME",
      "title": "DOC-10 — Create Final Repository Documentation PR Instructions — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb8164ac09e722dc967f25?pvs=204",
      "candidate_version": "091426.1",
      "id": "DOC-20",
      "lane": "DOC",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Verify Final Repository Documentation Completion for the exact supplied change.",
      "output_artifacts": [
        "DOCUMENTATION_COMPLETION"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb81a4bf2ad969439c8ffe",
        "release": "GCFPE-20260913.1",
        "title": "DOC-20 — Verify Final Repository Documentation Completion — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb81a4bf2ad969439c8ffe",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "QA-10"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are the continuing whole-change Implementation Agent (IA), read-only.",
      "result_states": [
        "COMPLETE",
        "INCOMPLETE",
        "PENDING",
        "BLOCKED"
      ],
      "sequence": 20,
      "session_class": "CHANGE_LIFETIME",
      "title": "DOC-20 — Verify Final Repository Documentation Completion — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb81d582b8d490e77f9f40?pvs=204",
      "candidate_version": "091426.1",
      "id": "ESC-10",
      "lane": "ESC",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Create QA Escalation Report for the exact supplied change.",
      "output_artifacts": [
        "QA_ESCALATION_REPORT"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb81dca03dc24874692130",
        "release": "GCFPE-20260913.1",
        "title": "ESC-10 — Create QA Escalation Report — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb81dca03dc24874692130",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "ESC-30"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are the same continuing Kronos QA authority.",
      "result_states": [
        "AWAITING_THOTH_REMEDIATION"
      ],
      "sequence": 10,
      "session_class": "ROLE_CONTINUING",
      "title": "ESC-10 — Create QA Escalation Report — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb81bf9326e46a1017de38?pvs=204",
      "candidate_version": "091426.1",
      "id": "ESC-25",
      "lane": "ESC",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Execute Bounded Escalation Discovery for the exact supplied change.",
      "output_artifacts": [
        "DISCOVERY_RESULT"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb81e09ff9c34bda83e49e",
        "release": "GCFPE-20260913.1",
        "title": "ESC-25 — Execute Bounded Escalation Discovery — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb81e09ff9c34bda83e49e",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "ESC-30"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are the explicitly named read-only repository reviewer or authorized environment operator.",
      "result_states": [
        "COMPLETE",
        "PARTIAL",
        "BLOCKED"
      ],
      "sequence": 25,
      "session_class": "DEDICATED_ONE_OFF",
      "title": "ESC-25 — Execute Bounded Escalation Discovery — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb813e99b4e416bc7afdae?pvs=204",
      "candidate_version": "091426.1",
      "id": "ESC-30",
      "lane": "ESC",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Diagnose and Propose Bounded Remediation for the exact supplied change.",
      "output_artifacts": [
        "REMEDIATION_PROPOSAL",
        "DISCOVERY_TASK"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb81f8ba50fdc497a8b2ec",
        "release": "GCFPE-20260913.1",
        "title": "ESC-30 — Diagnose and Propose Bounded Remediation — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb81f8ba50fdc497a8b2ec",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "ESC-25",
        "ESC-40"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are Thoth, the continuing Head of Development and remediation proposal author for this change.",
      "result_states": [
        "REMEDIATION_PENDING",
        "DISCOVERY_REQUIRED",
        "BLOCKED"
      ],
      "sequence": 30,
      "session_class": "ROLE_CONTINUING",
      "title": "ESC-30 — Diagnose and Propose Bounded Remediation — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb81efb6d4cd8d02ba9756?pvs=204",
      "candidate_version": "091426.1",
      "id": "ESC-40",
      "lane": "ESC",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Review and Return Approved Remediation for the exact supplied change.",
      "output_artifacts": [
        "REMEDIATION_REVIEW"
      ],
      "pf10_addendum_role": "QUALIFYING_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb8101bc3bd23243f1d4c5",
        "release": "GCFPE-20260913.1",
        "title": "ESC-40 — Review and Return Approved Remediation — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb8101bc3bd23243f1d4c5",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "ESC-30",
        "PR-30",
        "RS-40",
        "IA-40",
        "IA-30"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are Isis, the continuing Lead Developer and remediation decision owner.",
      "result_states": [
        "APPROVE",
        "APPROVE_AS_CHANGED",
        "DENY"
      ],
      "sequence": 40,
      "session_class": "ROLE_CONTINUING",
      "title": "ESC-40 — Review and Return Approved Remediation — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb81d1bb64ebcb3ca8eb54?pvs=204",
      "candidate_version": "091426.1",
      "id": "GCFPE-MGMT-10",
      "lane": "GCFPE-MGMT",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Manage an Ecosystem Change for the exact supplied change.",
      "output_artifacts": [
        "GCFPE_ECOSYSTEM_CHANGE_REPORT"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb81ac80e6d886a25aa026",
        "release": "GCFPE-20260913.1",
        "title": "GCFPE-MGMT-10 — Manage an Ecosystem Change — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb81ac80e6d886a25aa026",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "ORIGINAL_NATIVE_STAGE",
        "PR-10"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "Act as the Managing Prompt Engineer for one requested GCFPE change.",
      "result_states": [
        "ECOSYSTEM_CHANGE_COMPLETE",
        "READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION",
        "IMPLEMENTATION_BLOCKED",
        "PROMOTION_CHECKPOINT_REQUIRED"
      ],
      "sequence": 10,
      "session_class": "DEDICATED_ONE_OFF",
      "title": "GCFPE-MGMT-10 — Manage an Ecosystem Change — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb817aa191f1e822c30480?pvs=204",
      "candidate_version": "091426.1",
      "id": "IA-10",
      "lane": "IA",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Create Whole-Change Implementation Audit and Plan for the exact supplied change.",
      "output_artifacts": [
        "IMPLEMENTATION_AUDIT / IMPLEMENTATION_PLAN"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb8130b2fcf3993239096c",
        "release": "GCFPE-20260913.1",
        "title": "IA-10 — Create Whole-Change Implementation Audit and Plan — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb8130b2fcf3993239096c",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "IA-30"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are the dedicated Implementation Agent (IA) for this entire change.",
      "result_states": [
        "AUDIT_COMPLETE",
        "PLAN_PENDING",
        "BLOCKED"
      ],
      "sequence": 10,
      "session_class": "CHANGE_LIFETIME",
      "title": "IA-10 — Create Whole-Change Implementation Audit and Plan — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb81c4825df2ad0dec4750?pvs=204",
      "candidate_version": "091426.1",
      "id": "IA-20",
      "lane": "IA",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Create Whole-Change Implementation Plan for the exact supplied change.",
      "output_artifacts": [
        "IMPLEMENTATION_PLAN"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb8198bffdf367600ab5b3",
        "release": "GCFPE-20260913.1",
        "title": "IA-20 — Create Whole-Change Implementation Plan — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb8198bffdf367600ab5b3",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "IA-30"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are the same whole-change Implementation Agent (IA).",
      "result_states": [
        "PLAN_PENDING",
        "BLOCKED"
      ],
      "sequence": 20,
      "session_class": "CHANGE_LIFETIME",
      "title": "IA-20 — Create Whole-Change Implementation Plan — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb81c6bfb5f36f7df8f464?pvs=204",
      "candidate_version": "091426.1",
      "id": "IA-30",
      "lane": "IA",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Review Whole-Change Implementation Plan for the exact supplied change.",
      "output_artifacts": [
        "IMPLEMENTATION_PLAN_REVIEW / MATERIAL_PLAN_DELTA_REVIEW"
      ],
      "pf10_addendum_role": "QUALIFYING_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb81029c49c21113701638",
        "release": "GCFPE-20260913.1",
        "title": "IA-30 — Review Whole-Change Implementation Plan — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb81029c49c21113701638",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "PR-10",
        "IA-40"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are Isis, continuing Lead Developer for the approved change.",
      "result_states": [
        "APPROVE",
        "DENY"
      ],
      "sequence": 30,
      "session_class": "ROLE_CONTINUING",
      "title": "IA-30 — Review Whole-Change Implementation Plan — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb8197bb1bc8f52f896969?pvs=204",
      "candidate_version": "091426.1",
      "id": "IA-40",
      "lane": "IA",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Prepare or Revise Whole-Change Implementation Plan for the exact supplied change.",
      "output_artifacts": [
        "IMPLEMENTATION_PLAN"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb819d920ac5f14a042d08",
        "release": "GCFPE-20260913.1",
        "title": "IA-40 — Prepare or Revise Whole-Change Implementation Plan — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb819d920ac5f14a042d08",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "IA-30"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are the same Implementation Agent (IA) who authored the pending preapproval whole-change Plan.",
      "result_states": [
        "PLAN_PENDING_REVISED",
        "WRONG_ROUTE_APPROVED_BASE"
      ],
      "sequence": 40,
      "session_class": "CHANGE_LIFETIME",
      "title": "IA-40 — Prepare or Revise Whole-Change Implementation Plan — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb81d78eeae384e93dd697?pvs=204",
      "candidate_version": "091426.1",
      "id": "IA-50",
      "lane": "IA",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute IA Answer Seeder for the exact supplied change.",
      "output_artifacts": [
        "IA_RECOVERY_SEED"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb8107a012f68e6b8fd98c",
        "release": "GCFPE-20260913.1",
        "title": "IA-50 — IA Answer Seeder — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb8107a012f68e6b8fd98c",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "IA-10",
        "IA-20",
        "IA-30",
        "IA-40",
        "ESC-40"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "Act as the IA Answer Seeder, a bounded resolution assistant.",
      "result_states": [
        "SEED_READY",
        "SEED_INCOMPLETE"
      ],
      "sequence": 50,
      "session_class": "CHANGE_LIFETIME",
      "title": "IA-50 — IA Answer Seeder — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb8141b5b2c8fbf7b725e2?pvs=204",
      "candidate_version": "091426.1",
      "id": "IA-60",
      "lane": "IA",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Thoth Planning Research for the exact supplied change.",
      "output_artifacts": [
        "PLANNING_RESEARCH_FINDING"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb81f78afcca35f2dcb7db",
        "release": "GCFPE-20260913.1",
        "title": "IA-60 — Thoth Planning Research — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb81f78afcca35f2dcb7db",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "IA-50",
        "ESC-30"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "Act as Thoth for one bounded advanced engineering planning inquiry before Plan approval.",
      "result_states": [
        "RESEARCH_COMPLETE",
        "PARTIAL",
        "BLOCKED"
      ],
      "sequence": 60,
      "session_class": "ROLE_CONTINUING",
      "title": "IA-60 — Thoth Planning Research — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb8108ad2dd4d0e20bd6c4?pvs=204",
      "candidate_version": "091426.1",
      "id": "MGR-10",
      "lane": "MGR",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Coordinate the Complete Change Flow within Current Authority for the exact supplied change.",
      "output_artifacts": [
        "FLOW_PROGRESS"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb81c585d2f70e28f1c2bf",
        "release": "GCFPE-20260913.1",
        "title": "MGR-10 — Coordinate the Complete Change Flow within Current Authority — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb81c585d2f70e28f1c2bf",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "CF-PO-10",
        "CF-E-10",
        "CF-C-10",
        "QA-10",
        "CL-40"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are the Change Flow coordinator, without taking over any substantive actor or approval.",
      "result_states": [
        "FLOW_PROGRESS",
        "TERMINAL_RETURN"
      ],
      "sequence": 10,
      "session_class": "ORCHESTRATOR_RUN",
      "title": "MGR-10 — Coordinate the Complete Change Flow within Current Authority — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb81db98cce3e30a62bce5?pvs=204",
      "candidate_version": "091426.1",
      "id": "OPS-10",
      "lane": "OPS",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Create Bounded Ops Task for the exact supplied change.",
      "output_artifacts": [
        "OPS_TASK"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb8173b6becbea1fd53aa6",
        "release": "GCFPE-20260913.1",
        "title": "OPS-10 — Create Bounded Ops Task — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb8173b6becbea1fd53aa6",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "OPS-20"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are the same Implementation Agent (IA) and future task-acceptance owner.",
      "result_states": [
        "READY",
        "BLOCKED"
      ],
      "sequence": 10,
      "session_class": "CHANGE_LIFETIME",
      "title": "OPS-10 — Create Bounded Ops Task — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb81858a9dd361d3689ce8?pvs=204",
      "candidate_version": "091426.1",
      "id": "OPS-20",
      "lane": "OPS",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Execute Bounded Ops Task for the exact supplied change.",
      "output_artifacts": [
        "OPS_EXECUTION_RESULT"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb8137b923d8f5eee107aa",
        "release": "GCFPE-20260913.1",
        "title": "OPS-20 — Execute Bounded Ops Task — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb8137b923d8f5eee107aa",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "OPS-30"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are the authorized DevOps or target-environment operator for the exact bounded operation supplied in OPS_TASK_ID.",
      "result_states": [
        "COMPLETE",
        "PARTIAL",
        "BLOCKED",
        "FAILED",
        "NOT_EXECUTED",
        "NOT_PRODUCED"
      ],
      "sequence": 20,
      "session_class": "DEDICATED_ONE_OFF",
      "title": "OPS-20 — Execute Bounded Ops Task — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb816f91c9c394f9c9fa57?pvs=204",
      "candidate_version": "091426.1",
      "id": "OPS-30",
      "lane": "OPS",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Review Ops Execution Receipt for the exact supplied change.",
      "output_artifacts": [
        "OPS_TASK_RECEIPT"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb8134a4fce2e3f4aabf68",
        "release": "GCFPE-20260913.1",
        "title": "OPS-30 — Review Ops Execution Receipt — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb8134a4fce2e3f4aabf68",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "OPS-10",
        "OPS-20",
        "ESC-30",
        "RS-10",
        "RS-20"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are the same Implementation Agent (IA) who created the Ops Task.",
      "result_states": [
        "ACCEPT",
        "REJECT"
      ],
      "sequence": 30,
      "session_class": "CHANGE_LIFETIME",
      "title": "OPS-30 — Review Ops Execution Receipt — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb818e8359de1994e97a7d?pvs=204",
      "candidate_version": "091426.1",
      "id": "PR-10",
      "lane": "PR",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Create PR Work-Unit Instructions for the exact supplied change.",
      "output_artifacts": [
        "PR_INSTRUCTION"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb81c594a0f9bf5cb151a7",
        "release": "GCFPE-20260913.1",
        "title": "PR-10 — Create PR Work-Unit Instructions — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb81c594a0f9bf5cb151a7",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "PR-20"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are the same Implementation Agent (IA).",
      "result_states": [
        "INSTRUCTION_READY",
        "DRAFT",
        "BLOCKED"
      ],
      "sequence": 10,
      "session_class": "CHANGE_LIFETIME",
      "title": "PR-10 — Create PR Work-Unit Instructions — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb8174abf8c04318ab04be?pvs=204",
      "candidate_version": "091426.1",
      "id": "PR-20",
      "lane": "PR",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Create Detailed PR Implementation Plan for the exact supplied change.",
      "output_artifacts": [
        "PR_IMPLEMENTATION_PLAN"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb8147b34ccfabf608c2e3",
        "release": "GCFPE-20260913.1",
        "title": "PR-20 — Create Detailed PR Implementation Plan — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb8147b34ccfabf608c2e3",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "PR-30"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are the dedicated PR engineering session for this one work unit.",
      "result_states": [
        "AWAITING_PO_PROCEED",
        "DRAFT",
        "BLOCKED"
      ],
      "sequence": 20,
      "session_class": "DEDICATED_ONE_OFF",
      "title": "PR-20 — Create Detailed PR Implementation Plan — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb8123afb8caeeaa83a294?pvs=204",
      "candidate_version": "091426.1",
      "id": "PR-30",
      "lane": "PR",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute PR Implementation Proceed for the exact supplied change.",
      "output_artifacts": [
        "PR_IMPLEMENTATION_RESULT"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb81c0aee0d0862b242e09",
        "release": "GCFPE-20260913.1",
        "title": "PR-30 — PR Implementation Proceed — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb81c0aee0d0862b242e09",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "PR-35",
        "RS-20"
      ],
      "r1_mapping": "GCF-17",
      "receiving_role": "You are the same dedicated PR engineering session for one exact approved work unit.",
      "result_states": [
        "PR_CANDIDATE_PUBLISHED",
        "RESCOPE_PENDING",
        "RECOVERY_PENDING",
        "PRODUCT_OWNER_DECISION_REQUIRED"
      ],
      "sequence": 30,
      "session_class": "DEDICATED_ONE_OFF",
      "title": "PR-30 — PR Implementation Proceed — 091426.1"
    },
    {
      "adds_approval": false,
      "adds_merge_authority": false,
      "adds_proceed": false,
      "adds_product_owner_gate": false,
      "adds_r1_row": false,
      "adds_role": false,
      "adds_session": false,
      "adds_work_unit": false,
      "adds_work_vehicle": false,
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb8120b443ed2cb08b723c?pvs=204",
      "candidate_version": "091426.1",
      "cross_session_route": false,
      "id": "PR-35",
      "lane": "PR",
      "lifecycle": "UNSELECTED_CANDIDATE_NEW_MEMBER",
      "native_function": "Continue the same proceeded PR work unit after initial publication; resolve reviews, retest, publish coherent corrections, verify current-head CI/reviews/head/mergeability, and return MERGE_PENDING without merging.",
      "output_artifacts": [
        "PR_IMPLEMENTATION_RESULT"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": null,
      "predecessor_union_destinations": [],
      "r1_mapping": "GCF-17",
      "receiving_role": "Same dedicated PR engineer in the same PR-development session; no new role.",
      "result_states": [
        "MERGE_PENDING",
        "RESCOPE_PENDING",
        "RECOVERY_PENDING",
        "REMOTE_EVIDENCE_PENDING",
        "PRODUCT_OWNER_DECISION_REQUIRED"
      ],
      "sequence": 35,
      "session_class": "SAME_DEDICATED_PR_DEVELOPMENT_SESSION_AS_PR-30",
      "title": "PR-35 — Resolve PR Reviews and Reach Merge Readiness — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb818786c5cb6051b4d634?pvs=204",
      "candidate_version": "091426.1",
      "id": "PR-40",
      "lane": "PR",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Review PR Work-Unit Lineage for the exact supplied change.",
      "output_artifacts": [
        "PR_WORK_UNIT_LINEAGE_REVIEW"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb813c8b47e77f94ff1def",
        "release": "GCFPE-20260913.1",
        "title": "PR-40 — Review PR Work-Unit Lineage — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb813c8b47e77f94ff1def",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "DOC-20",
        "QA-10",
        "PR-30",
        "PR-10",
        "RS-10",
        "RS-20"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are the designated PR reviewer for the complete work unit, operating read-only.",
      "result_states": [
        "ACCEPT",
        "REJECT",
        "PENDING"
      ],
      "sequence": 40,
      "session_class": "DEDICATED_ONE_OFF",
      "title": "PR-40 — Review PR Work-Unit Lineage — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb8138ac99c13cf6f2f282?pvs=204",
      "candidate_version": "091426.1",
      "id": "PR-50",
      "lane": "PR",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Abort PR and Escalate for the exact supplied change.",
      "output_artifacts": [
        "PR_ABORT_ESCALATION_RECORD"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb813bb505eea620942e30",
        "release": "GCFPE-20260913.1",
        "title": "PR-50 — Abort PR and Escalate — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb813bb505eea620942e30",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are acting only on Nathan / Product Owner's direct manual invocation.",
      "result_states": [
        "PR_ABORTED_ESCALATED"
      ],
      "sequence": 50,
      "session_class": "DEDICATED_ONE_OFF",
      "title": "PR-50 — Abort PR and Escalate — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb818bad2fcb4bc2610b29?pvs=204",
      "candidate_version": "091426.1",
      "id": "QA-10",
      "lane": "QA",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Audit Implementation and Establish QA Readiness for the exact supplied change.",
      "output_artifacts": [
        "REALITY_AUDIT / CHANGE_AUDIT_TRIAGE / QA_READINESS"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb814fbda7f3b722487b6b",
        "release": "GCFPE-20260913.1",
        "title": "QA-10 — Audit Implementation and Establish QA Readiness — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb814fbda7f3b722487b6b",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "QA-20",
        "ESC-30"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are Isis, the continuing Lead Developer and whole-change readiness decision owner for the exact supplied change.",
      "result_states": [
        "READY_FOR_QA",
        "NOT_READY",
        "ASSESSMENT_INCOMPLETE"
      ],
      "sequence": 10,
      "session_class": "ROLE_CONTINUING",
      "title": "QA-10 — Audit Implementation and Establish QA Readiness — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb811a8d13c0bbbf77a848?pvs=204",
      "candidate_version": "091426.1",
      "id": "QA-100",
      "lane": "QA",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Execute Bounded QA Task for the exact supplied change.",
      "output_artifacts": [
        "QA_EXECUTION_RESULT"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb8111b12cea07a97f1a50",
        "release": "GCFPE-20260913.1",
        "title": "QA-100 — Execute Bounded QA Task — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb8111b12cea07a97f1a50",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "QA-110",
        "QA-90",
        "QA-80",
        "QA-70"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are the authorized environment or DevOps operator, not Kronos acting as the executor.",
      "result_states": [
        "COMPLETE",
        "PARTIAL",
        "BLOCKED",
        "FAILED",
        "NOT_EXECUTED"
      ],
      "sequence": 100,
      "session_class": "DEDICATED_ONE_OFF",
      "title": "QA-100 — Execute Bounded QA Task — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb816984d1d34da0e08f40?pvs=204",
      "candidate_version": "091426.1",
      "id": "QA-110",
      "lane": "QA",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Review QA Evidence and Route the Next Action for the exact supplied change.",
      "output_artifacts": [
        "QA_EVIDENCE_REVIEW"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb81e2890ec3a36ad7221f",
        "release": "GCFPE-20260913.1",
        "title": "QA-110 — Review QA Evidence and Route the Next Action — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb81e2890ec3a36ad7221f",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "QA-120",
        "QA-90",
        "QA-100",
        "ESC-10"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are the same continuing Kronos QA authority.",
      "result_states": [
        "ACCEPT",
        "BOUNDED_RERUN_REQUIRED",
        "ESCALATION_REQUIRED",
        "INCOMPLETE"
      ],
      "sequence": 110,
      "session_class": "ROLE_CONTINUING",
      "title": "QA-110 — Review QA Evidence and Route the Next Action — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb81589d21e798cf38e8ba?pvs=204",
      "candidate_version": "091426.1",
      "id": "QA-120",
      "lane": "QA",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Create Final QA Report and RCA for the exact supplied change.",
      "output_artifacts": [
        "QA_REPORT / QA_RCA / QA_INTERIM_STATUS"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb81a99a28d8c1c17aa861",
        "release": "GCFPE-20260913.1",
        "title": "QA-120 — Create Final QA Report and RCA — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb81a99a28d8c1c17aa861",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "CL-C-10",
        "QA-110",
        "QA-90",
        "ESC-10"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are Kronos, continuing QA authority for this Epic or CRD.",
      "result_states": [
        "PASS",
        "FAIL",
        "INTERIM"
      ],
      "sequence": 120,
      "session_class": "ROLE_CONTINUING",
      "title": "QA-120 — Create Final QA Report and RCA — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb816daa3adff37283482b?pvs=204",
      "candidate_version": "091426.1",
      "id": "QA-20",
      "lane": "QA",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Create Live QA Guide for the exact supplied change.",
      "output_artifacts": [
        "LIVE_QA_GUIDE"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb81e4ac5fe5de703e5455",
        "release": "GCFPE-20260913.1",
        "title": "QA-20 — Create Live QA Guide — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb81e4ac5fe5de703e5455",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "QA-50",
        "QA-10"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are the same Isis who established readiness.",
      "result_states": [
        "GUIDE_READY",
        "BLOCKED"
      ],
      "sequence": 20,
      "session_class": "ROLE_CONTINUING",
      "title": "QA-20 — Create Live QA Guide — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb81a3ac91f602bad8cfa2?pvs=204",
      "candidate_version": "091426.1",
      "id": "QA-50",
      "lane": "QA",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Create Whole-Change QA Audit and Plan for the exact supplied change.",
      "output_artifacts": [
        "QA_AUDIT / QA_PLAN"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb819883dff9cd98c22985",
        "release": "GCFPE-20260913.1",
        "title": "QA-50 — Create Whole-Change QA Audit and Plan — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb819883dff9cd98c22985",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "QA-70",
        "QA-80",
        "QA-60"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are Kronos, the continuing QA authority for this entire change.",
      "result_states": [
        "AUDIT_COMPLETE",
        "PLAN_PENDING",
        "BLOCKED"
      ],
      "sequence": 50,
      "session_class": "ROLE_CONTINUING",
      "title": "QA-50 — Create Whole-Change QA Audit and Plan — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb810b8aa3e1692830d4b8?pvs=204",
      "candidate_version": "091426.1",
      "id": "QA-60",
      "lane": "QA",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Create Whole-Change QA Plan for the exact supplied change.",
      "output_artifacts": [
        "QA_PLAN"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb81e79893ef7df08bf7fe",
        "release": "GCFPE-20260913.1",
        "title": "QA-60 — Create Whole-Change QA Plan — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb81e79893ef7df08bf7fe",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "QA-70",
        "QA-80"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are the same continuing Kronos QA authority.",
      "result_states": [
        "PLAN_PENDING",
        "BLOCKED"
      ],
      "sequence": 60,
      "session_class": "ROLE_CONTINUING",
      "title": "QA-60 — Create Whole-Change QA Plan — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb8143bf26d1459fbbcad7?pvs=204",
      "candidate_version": "091426.1",
      "id": "QA-70",
      "lane": "QA",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Review Whole-Change QA Plan for the exact supplied change.",
      "output_artifacts": [
        "QA_PLAN_REVIEW / MATERIAL_QA_PLAN_DELTA_REVIEW"
      ],
      "pf10_addendum_role": "QUALIFYING_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb816f8399e55ce20e4e21",
        "release": "GCFPE-20260913.1",
        "title": "QA-70 — Review Whole-Change QA Plan — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb816f8399e55ce20e4e21",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "QA-90",
        "QA-80"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are Isis, continuing Lead Developer and QA Plan reviewer.",
      "result_states": [
        "APPROVE",
        "DENY"
      ],
      "sequence": 70,
      "session_class": "ROLE_CONTINUING",
      "title": "QA-70 — Review Whole-Change QA Plan — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb813ba9a9dbd9a641d36c?pvs=204",
      "candidate_version": "091426.1",
      "id": "QA-80",
      "lane": "QA",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Revise Whole-Change QA Plan for the exact supplied change.",
      "output_artifacts": [
        "QA_PLAN"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb81e58172ec98c21f8eb2",
        "release": "GCFPE-20260913.1",
        "title": "QA-80 — Revise Whole-Change QA Plan — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb81e58172ec98c21f8eb2",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "QA-70"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are the same Kronos who authored the Plan.",
      "result_states": [
        "PLAN_PENDING_REVISED",
        "WRONG_ROUTE_APPROVED_BASE"
      ],
      "sequence": 80,
      "session_class": "ROLE_CONTINUING",
      "title": "QA-80 — Revise Whole-Change QA Plan — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb811e8582cf30238c5b9c?pvs=204",
      "candidate_version": "091426.1",
      "id": "QA-90",
      "lane": "QA",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Create Bounded QA Execution Task for the exact supplied change.",
      "output_artifacts": [
        "QA_TASK / QA_PREEXECUTION_FINDING"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb8118a902dfced4429f2c",
        "release": "GCFPE-20260913.1",
        "title": "QA-90 — Create Bounded QA Execution Task — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb8118a902dfced4429f2c",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "QA-100",
        "QA-110",
        "QA-80",
        "QA-70"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are the continuing Kronos QA authority.",
      "result_states": [
        "TASK_READY",
        "ESCALATION_REQUIRED",
        "NOT_EXECUTED"
      ],
      "sequence": 90,
      "session_class": "ROLE_CONTINUING",
      "title": "QA-90 — Create Bounded QA Execution Task — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb811ca0cdc66e0d508ac4?pvs=204",
      "candidate_version": "091426.1",
      "id": "RS-10",
      "lane": "RS",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Create Bounded Work-Unit Rescope Proposal for the exact supplied change.",
      "output_artifacts": [
        "RESCOPE_PROPOSAL"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb81f99430fcb7c24fe8af",
        "release": "GCFPE-20260913.1",
        "title": "RS-10 — Create Bounded Work-Unit Rescope Proposal — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb81f99430fcb7c24fe8af",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "RS-20"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are Sekhmet or the explicitly assigned finding author, with no approval authority.",
      "result_states": [
        "RESCOPE_PROPOSAL_PENDING_REVIEW"
      ],
      "sequence": 10,
      "session_class": "DEDICATED_ONE_OFF",
      "title": "RS-10 — Create Bounded Work-Unit Rescope Proposal — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb81c183aac2ecb40b1497?pvs=204",
      "candidate_version": "091426.1",
      "id": "RS-20",
      "lane": "RS",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Review Bounded Work-Unit Rescope for the exact supplied change.",
      "output_artifacts": [
        "RESCOPE_REVIEW"
      ],
      "pf10_addendum_role": "QUALIFYING_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb81d3adf1ecac218d0beb",
        "release": "GCFPE-20260913.1",
        "title": "RS-20 — Review Bounded Work-Unit Rescope — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb81d3adf1ecac218d0beb",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "PR-30",
        "PR-35",
        "RS-30",
        "RS-40"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are the continuing whole-change Implementation Agent (IA).",
      "result_states": [
        "APPROVE",
        "REJECT",
        "REVISION_REQUIRED",
        "SPECIFICATION_CHANGE_REQUIRED",
        "IN_SCOPE_REPAIR"
      ],
      "sequence": 20,
      "session_class": "CHANGE_LIFETIME",
      "title": "RS-20 — Review Bounded Work-Unit Rescope — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb81ed9fd3d2ef439ceaaf?pvs=204",
      "candidate_version": "091426.1",
      "id": "RS-30",
      "lane": "RS",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Revise Bounded Work-Unit Rescope Proposal for the exact supplied change.",
      "output_artifacts": [
        "RESCOPE_REQUEST / RESCOPE_PROPOSAL"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb81f99c6df22213fe675e",
        "release": "GCFPE-20260913.1",
        "title": "RS-30 — Revise Bounded Work-Unit Rescope Proposal — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb81f99c6df22213fe675e",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "RS-20"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are the same Sekhmet or explicitly assigned rescope-artifact author.",
      "result_states": [
        "RESCOPE_PROPOSAL_PENDING_REVIEW"
      ],
      "sequence": 30,
      "session_class": "DEDICATED_ONE_OFF",
      "title": "RS-30 — Revise Bounded Work-Unit Rescope Proposal — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb8183b5ffdf4270133226?pvs=204",
      "candidate_version": "091426.1",
      "id": "RS-40",
      "lane": "RS",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Approved Rescope — Resume PR Implementation for the exact supplied change.",
      "output_artifacts": [
        "PR_IMPLEMENTATION_RESULT"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb815e98f5ea7b605b70a3",
        "release": "GCFPE-20260913.1",
        "title": "RS-40 — Approved Rescope — Resume PR Implementation — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb815e98f5ea7b605b70a3",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [
        "PR-35",
        "RS-20"
      ],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are the same dedicated PR engineering session for the exact suspended work unit.",
      "result_states": [
        "SOURCE_RESOLUTION_ERROR",
        "MANUAL_DRAIN_REQUIRED",
        "MANUAL_DRAIN_MISMATCH",
        "DRAIN_VERIFIED",
        "PR_CANDIDATE_PUBLISHED",
        "MERGE_PENDING",
        "RESCOPE_PENDING",
        "RECOVERY_PENDING",
        "REMOTE_EVIDENCE_PENDING",
        "PRODUCT_OWNER_DECISION_REQUIRED"
      ],
      "sequence": 40,
      "session_class": "DEDICATED_ONE_OFF",
      "title": "RS-40 — Approved Rescope — Resume PR Implementation — 091426.1"
    },
    {
      "candidate_page_binding": "NOTION_STAGED_UNSELECTED",
      "candidate_url": "https://app.notion.com/p/3db4590a05eb81b89fbaf4b31a3ed2a9?pvs=204",
      "candidate_version": "091426.1",
      "id": "UTIL-10",
      "lane": "UTIL",
      "lifecycle": "UNSELECTED_CANDIDATE",
      "native_function": "Execute Apply Exact Redline to a Complete Artifact for the exact supplied change.",
      "output_artifacts": [
        "REVISED_TARGET_ARTIFACT / REDLINE_APPLICATION_REPORT"
      ],
      "pf10_addendum_role": "NON_PRODUCER",
      "predecessor": {
        "notion_page_id": "3da4590a05eb8114a88cda5c9728e26c",
        "release": "GCFPE-20260913.1",
        "title": "UTIL-10 — Apply Exact Redline to a Complete Artifact — 091326.2",
        "url": "https://app.notion.com/p/3da4590a05eb8114a88cda5c9728e26c",
        "version": "091326.2"
      },
      "predecessor_union_destinations": [],
      "r1_mapping": "PRESERVED_PREDECESSOR_MAPPING",
      "receiving_role": "You are the original author or explicitly authorized editor of the exact target.",
      "result_states": [
        "COMPLETE",
        "INCOMPLETE"
      ],
      "sequence": 10,
      "session_class": "DEDICATED_ONE_OFF",
      "title": "UTIL-10 — Apply Exact Redline to a Complete Artifact — 091426.1"
    }
  ],
  "pf10_addendum_contract": {
    "canonicality": "NON_CANONICAL_PENDING_MANUAL_DRAIN",
    "drain_owner": "Nathan / Product Owner",
    "exact_producer_set": [
      "CF-C-30",
      "CF-E-30",
      "ESC-40",
      "IA-30",
      "QA-70",
      "RS-20"
    ],
    "exactly_one_per_qualifying_approval": true,
    "native_outcome_normalization": {
      "DELTA_DENY": "DENIAL",
      "DENY": "DENIAL",
      "EDITORIAL": "EDITORIAL",
      "INITIAL_APPROVE": "INITIAL_APPROVAL",
      "INITIAL_DENY": "DENIAL",
      "IN_SCOPE_REPAIR": "IN_SCOPE_REPAIR",
      "PENDING": "PENDING",
      "REJECT": "REJECTION",
      "REVISION_REQUIRED": "REVISION_REQUIRED",
      "UNCHANGED": "UNCHANGED"
    },
    "never_for": [
      "INITIAL_APPROVAL",
      "REJECTION",
      "DENIAL",
      "REVISION_REQUIRED",
      "PENDING",
      "UNCHANGED",
      "EDITORIAL",
      "IN_SCOPE_REPAIR"
    ],
    "producer_allocates_pf10_number": false,
    "producer_claims_canonical_adoption": false,
    "producer_edits_pf10": false,
    "producers": {
      "CF-C-30": "approved material delta to already approved CRD Specification",
      "CF-E-30": "approved material delta to already approved Epic Specification",
      "ESC-40": "approved material escalation/remediation or approved-base delta",
      "IA-30": "approved material delta to already approved whole-change Plan",
      "QA-70": "approved material delta to already approved QA Plan",
      "RS-20": "APPROVE of complete bounded work-unit rescope within approved Specification intent"
    },
    "required_fields": [
      "artifact_type",
      "addendum_id",
      "artifact_version",
      "status",
      "canonicality",
      "drain_owner",
      "producing_prompt",
      "approval_decision",
      "immutable_base",
      "applicable_prior_addenda",
      "approved_delta",
      "affected_surfaces",
      "exclusions",
      "conflicts",
      "unresolved_items",
      "return_phase",
      "drain_verification_anchor.addendum_id",
      "drain_verification_anchor.decision_id",
      "drain_verification_anchor.immutable_base_id",
      "drain_verification_anchor.approved_delta_digest"
    ],
    "status": "READY_FOR_MANUAL_DRAIN"
  },
  "pf10_post_drain_verification": {
    "DRAIN_VERIFIED": "Exact anchor and normalized approved delta are verified in freshly resolved current controlled PF10 Markdown and no later conflicting overlay exists; affected continuation may resume at the exact recorded return phase.",
    "MANUAL_DRAIN_MISMATCH": "Related current PF10 content exists but the decision, immutable base, normalized approved delta differs, or a later conflicting overlay exists.",
    "MANUAL_DRAIN_REQUIRED": "Current controlled PF10 Markdown was completely read and the exact approved anchor is absent.",
    "SOURCE_RESOLUTION_ERROR": "Unique controlled current PF10 Markdown cannot be resolved or completely read; no inference about whether Nathan drained.",
    "exhaustive_mutually_exclusive_results": [
      "SOURCE_RESOLUTION_ERROR",
      "MANUAL_DRAIN_REQUIRED",
      "MANUAL_DRAIN_MISMATCH",
      "DRAIN_VERIFIED"
    ]
  },
  "post_merge_three_event_contract": {
    "agent_merge_authorized": false,
    "direct_PR35_to_PR40_automatic_edge": false,
    "event_1": {
      "fact": "prior_pr35_result",
      "producer": "PR-35",
      "time": "pre_merge_historical_evidence",
      "value": "MERGE_PENDING"
    },
    "event_2": {
      "actor": "Nathan / Product Owner",
      "fact": "product_owner_manual_merge_assertion",
      "time": "later PR-40 invocation",
      "value": true
    },
    "event_3": {
      "consumer": "PR-40",
      "fact": "pr40_actual_merge_verification",
      "independent": true,
      "values": [
        "VERIFIED",
        "PENDING"
      ]
    }
  },
  "pr_continuity_contract": {
    "adds": {
      "approval": 0,
      "cross_session_route": 0,
      "duplicate_work_vehicle": 0,
      "merge_authority": 0,
      "proceed": 0,
      "product_owner_gate": 0,
      "r1_row": 0,
      "role": 0,
      "session": 0,
      "work_unit": 0,
      "work_vehicle": 0
    },
    "invented_session_inspection_endpoint_prohibited": true,
    "phase_aware_rescope_sequences": {
      "PR-30_POSTPUBLICATION": [
        "PR-30",
        "RS-20",
        "NATHAN_MANUAL_PF10_DRAIN",
        "RS-40",
        "PR-30"
      ],
      "PR-30_PREPUBLICATION": [
        "PR-30",
        "RS-20",
        "NATHAN_MANUAL_PF10_DRAIN",
        "PR-30"
      ],
      "PR-35": [
        "PR-35",
        "RS-20",
        "NATHAN_MANUAL_PF10_DRAIN",
        "RS-40",
        "PR-35"
      ]
    },
    "primary_skill": "glow-hde-pr-development",
    "prompts": [
      "PR-30",
      "PR-35",
      "eligible RS-40 continuation"
    ],
    "r1_row": "GCF-17",
    "shared_exactly_one": [
      "WORK_UNIT_ID",
      "original Product Owner Proceed",
      "dedicated PR-development session",
      "workspace/worktree",
      "branch",
      "pull request",
      "PR instruction",
      "detailed PR plan",
      "primary skill authority",
      "continuous recovery/artifact lineage"
    ],
    "unsupported_platform_limitation_claim_prohibited": true
  },
  "proofs": {
    "PR-35_same_r1_row_as_PR-30": true,
    "all_candidate_urls_are_observed_direct_notion_urls": true,
    "all_edge_endpoints_resolved": true,
    "baseline_ids_retained": true,
    "boundary_nodes_counted_as_members": false,
    "candidate_node_count": 55,
    "candidate_url_placeholder_count": 0,
    "observed_pf10_producers": [
      "CF-C-30",
      "CF-E-30",
      "ESC-40",
      "IA-30",
      "QA-70",
      "RS-20"
    ],
    "pf10_producer_set_exact": true,
    "prompt_inbound_edges_to_PR-50": 0,
    "sole_added_node": [
      "PR-35"
    ],
    "unique_node_ids": true,
    "unresolved_edges": []
  },
  "protected_identities": {
    "flowmaster_primary_core_sha256": "495c2ca6f33a8b6b837754a518b1cbc64570e9c911e137fd5b81004d487e498c",
    "r1_core_rows": 26,
    "r1_material_rows": 20,
    "r1_oracle_sha256": "52807e58c4a4659e6c1fc822749f6e50253ad7b01846c833f727ee266ca71d5e",
    "r1_rows": 46
  },
  "qa_closure_contract": {
    "classification_source": "EXISTING_PRODUCT_OWNER_CLASSIFICATION_AND_APPROVED_SPECIFICATION",
    "closure_actor": "Isis",
    "closure_session": "RETAIN_EXISTING",
    "crd_strategy_card_required": false,
    "epic_strategy_card": "EXISTING_APPROVED_SPECIFICATION_STRATEGY_CARD",
    "pass_receivers": {
      "CRD": "CL-C-10",
      "EPIC": "CL-E-10"
    },
    "qa_pass_closes_change": false,
    "required_artifacts": [
      "QA_REPORT",
      "QA_RCA"
    ],
    "unresolved_class_effect": "NATHAN_TERMINAL_RETURN_NO_HANDOFF",
    "unresolved_receiver_evidence_effect": "NATHAN_TERMINAL_RETURN_NO_HANDOFF",
    "valid_result_reuse": true
  },
  "rca_separation_contract": {
    "classification": "ACCEPTED_TECHNICAL_HISTORY",
    "evidence_id": "PR03-R02",
    "may_authorize_alpha_resumption": false,
    "may_prove_pf10_drainage": false,
    "may_prove_prompt_completion_or_hang": false,
    "may_reopen_accepted_pr03": false
  },
  "schema_version": "gcfpe-candidate-graph-contract/2.1",
  "selection_status": "UNSELECTED_CANDIDATE",
  "source_bindings": {
    "binding_revision": "20260914.1-recovery.1",
    "binding_scope": "REPAIR_BASELINE_EVIDENCE_ONLY_NOT_A_RUNTIME_CURRENT_PF10_ALIAS",
    "bindings": [
      {
        "external_id": "1MEMi5OTUr-c7Qd3rtjntnNjSpnxfIXJ4",
        "parent_ids": [
          "1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3"
        ],
        "path": "recovery-20260914.1/sources/drive/1MEMi5OTUr-c7Qd3rtjntnNjSpnxfIXJ4.md",
        "provider_size_bytes": 354325,
        "representation": "EXACT_RAW_DRIVE_FILE_BYTES",
        "retrieved_at": "2026-09-14T21:29:11.721Z",
        "sha256": "4f4f015bc8fe8c0a9f7d518fce13b7428a1427b49ca463982b769827169b22a0",
        "size_bytes": 354325,
        "source_id": "drive:1MEMi5OTUr-c7Qd3rtjntnNjSpnxfIXJ4",
        "title": "PF27-Canon-Plan-Templates-v2.0.5.md",
        "url": "https://drive.google.com/file/d/1MEMi5OTUr-c7Qd3rtjntnNjSpnxfIXJ4/view?usp=drivesdk"
      },
      {
        "external_id": "1PUqOyiY285Yo4dxq3JucrzakiNTNLc-j",
        "parent_ids": [
          "1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3"
        ],
        "path": "recovery-20260914.1/sources/drive/1PUqOyiY285Yo4dxq3JucrzakiNTNLc-j.md",
        "provider_size_bytes": 26815,
        "representation": "EXACT_RAW_DRIVE_FILE_BYTES",
        "retrieved_at": "2026-09-14T21:29:14.265Z",
        "sha256": "106c50bb2e06702c1c72764ccece3d5c500bddf4b553e12afa0c4d1f8c7a4c21",
        "size_bytes": 26815,
        "source_id": "drive:1PUqOyiY285Yo4dxq3JucrzakiNTNLc-j",
        "title": "PF13- Reference-Glow-Development-Philosophy v1.md",
        "url": "https://drive.google.com/file/d/1PUqOyiY285Yo4dxq3JucrzakiNTNLc-j/view?usp=drivesdk"
      },
      {
        "external_id": "1PfbPLcgsI5T7UbbPK1bJNvcdsf3vMzsQ",
        "parent_ids": [
          "1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3"
        ],
        "path": "recovery-20260914.1/sources/drive/1PfbPLcgsI5T7UbbPK1bJNvcdsf3vMzsQ.md",
        "provider_size_bytes": 619584,
        "representation": "EXACT_RAW_DRIVE_FILE_BYTES",
        "retrieved_at": "2026-09-14T21:29:16.935Z",
        "sha256": "90e6af98fd18ce3ab4e91cb16fcfefbdb5bdf539690d8726f8e47359238bf853",
        "size_bytes": 619584,
        "source_id": "drive:1PfbPLcgsI5T7UbbPK1bJNvcdsf3vMzsQ",
        "title": "PF12-Canon-HDE-Schemas-and-Artifacts-v2.9.6.md",
        "url": "https://drive.google.com/file/d/1PfbPLcgsI5T7UbbPK1bJNvcdsf3vMzsQ/view?usp=drivesdk"
      },
      {
        "external_id": "1Q83saZ9QqxG9c9slV6bYkfDiCXLSK4Lp",
        "parent_ids": [
          "1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3"
        ],
        "path": "recovery-20260914.1/sources/drive/1Q83saZ9QqxG9c9slV6bYkfDiCXLSK4Lp.md",
        "provider_size_bytes": 558988,
        "representation": "EXACT_RAW_DRIVE_FILE_BYTES",
        "retrieved_at": "2026-09-14T21:29:20.208Z",
        "sha256": "e8234398902ab47e3492d54a83d79ef5e2d17399dee8ad03d0688aec98a23696",
        "size_bytes": 558988,
        "source_id": "drive:1Q83saZ9QqxG9c9slV6bYkfDiCXLSK4Lp",
        "title": "PF04-Canon-HDE-Governance-v2.8.6.md",
        "url": "https://drive.google.com/file/d/1Q83saZ9QqxG9c9slV6bYkfDiCXLSK4Lp/view?usp=drivesdk"
      },
      {
        "external_id": "1XdZYpx0Kcuu800fW0Yhi7aicD4wU_dJt",
        "parent_ids": [
          "1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3"
        ],
        "path": "recovery-20260914.1/sources/drive/1XdZYpx0Kcuu800fW0Yhi7aicD4wU_dJt.md",
        "provider_size_bytes": 657008,
        "representation": "EXACT_RAW_DRIVE_FILE_BYTES",
        "retrieved_at": "2026-09-14T21:29:23.438Z",
        "sha256": "2a4a254422da92933e7f4dce9e074bcd7e1a1a6609ed54a7897d3f5f8cc059d0",
        "size_bytes": 657008,
        "source_id": "drive:1XdZYpx0Kcuu800fW0Yhi7aicD4wU_dJt",
        "title": "PF19-Canon-Glow-QA-Guide-v3.0.5.md",
        "url": "https://drive.google.com/file/d/1XdZYpx0Kcuu800fW0Yhi7aicD4wU_dJt/view?usp=drivesdk"
      },
      {
        "external_id": "1_ej-UY2JaKS1vFnxMfSKnK881Y_hzlrP",
        "parent_ids": [
          "1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3"
        ],
        "path": "recovery-20260914.1/sources/drive/1_ej-UY2JaKS1vFnxMfSKnK881Y_hzlrP.md",
        "provider_size_bytes": 175083,
        "representation": "EXACT_RAW_DRIVE_FILE_BYTES",
        "retrieved_at": "2026-09-14T21:29:09.197Z",
        "sha256": "4b2b0d198cecf6f4ece852c82951342e512124abfb93fa90678df8d97b4f4f86",
        "size_bytes": 175083,
        "source_id": "drive:1_ej-UY2JaKS1vFnxMfSKnK881Y_hzlrP",
        "title": "PF10-HDE-Build-Notes-v13.2.6.md",
        "url": "https://drive.google.com/file/d/1_ej-UY2JaKS1vFnxMfSKnK881Y_hzlrP/view?usp=drivesdk"
      },
      {
        "external_id": "1f9hWZbmKVt6bMDs4RbdGAONFC_r06yR9",
        "parent_ids": [
          "1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3"
        ],
        "path": "recovery-20260914.1/sources/drive/1f9hWZbmKVt6bMDs4RbdGAONFC_r06yR9.md",
        "provider_size_bytes": 395891,
        "representation": "EXACT_RAW_DRIVE_FILE_BYTES",
        "retrieved_at": "2026-09-14T21:29:26.388Z",
        "sha256": "ad238a8fc07af27bcecf5afce71368766d96d0d40104649b2a005a0f721dd2f9",
        "size_bytes": 395891,
        "source_id": "drive:1f9hWZbmKVt6bMDs4RbdGAONFC_r06yR9",
        "title": "PF06-Canon-Change-Process-Guide-v2.5.4.md",
        "url": "https://drive.google.com/file/d/1f9hWZbmKVt6bMDs4RbdGAONFC_r06yR9/view?usp=drivesdk"
      },
      {
        "external_id": "1zYQC27hl7ynq8b2cWGlQ4kkIRBGxaWmI",
        "parent_ids": [
          "1gdBmaB_EqXdlwGBiaz-BP2tlhl9QfXd3"
        ],
        "path": "recovery-20260914.1/sources/drive/1zYQC27hl7ynq8b2cWGlQ4kkIRBGxaWmI.md",
        "provider_size_bytes": 10375,
        "representation": "EXACT_RAW_DRIVE_FILE_BYTES",
        "retrieved_at": "2026-09-14T21:29:29.374Z",
        "sha256": "391bf7d2eb51022e22edb69b90a2ed6eaa63f621dedcf817513c2ae1a0c77e24",
        "size_bytes": 10375,
        "source_id": "drive:1zYQC27hl7ynq8b2cWGlQ4kkIRBGxaWmI",
        "title": "PF21-Reference-7 Phases of Alchemical Engineering.md",
        "url": "https://drive.google.com/file/d/1zYQC27hl7ynq8b2cWGlQ4kkIRBGxaWmI/view?usp=drivesdk"
      },
      {
        "external_id": "1QfCDo6pw3_FRjJi5qTooLaxgLThFcURI",
        "parent_ids": [
          "1pRJ8R1a-p5dYQFY89a1YyJpDceYZ2MLc"
        ],
        "path": "recovery-20260914.1/sources/drive/1QfCDo6pw3_FRjJi5qTooLaxgLThFcURI-repin.md",
        "provider_size_bytes": 53118,
        "representation": "EXACT_RAW_DRIVE_FILE_BYTES",
        "retrieved_at": "2026-09-14T21:48:21.881Z",
        "sha256": "e14c9fa0574633186959c0f96dc62c7a28998336bf892f8046d6359820e7df01",
        "size_bytes": 53118,
        "source_id": "drive:1QfCDo6pw3_FRjJi5qTooLaxgLThFcURI",
        "title": "GCFPE-Change-Flow-Repair-Plan-v2.0-20260914.md",
        "url": "https://drive.google.com/file/d/1QfCDo6pw3_FRjJi5qTooLaxgLThFcURI/view?usp=drivesdk"
      }
    ],
    "candidate_release": "GCFPE-20260914.1",
    "candidate_version_family": "091426.1",
    "correction_report_url": "https://drive.google.com/file/d/1BlPiTmlfSdtpkgSkKm9pHaPSvyL4L6br/view?usp=drivesdk",
    "prior_capture_disposition": "HISTORICAL_DEFECTIVE_RAW_CAPTURE_PLUS_ONE_LF_NOT_AUTHORITY",
    "runtime_rule": "Each affected runtime receiver must freshly resolve current controlled PF10 after manual drain; these historical repair pins never replace that lookup.",
    "schema_version": "gcfpe-recovery-source-bindings/1.0",
    "selection_status": "UNSELECTED_CANDIDATE",
    "source_manifest_file_sha256": "252fbc9abf573af052e2572c77a3e8dac9725dc8a35c8acbc42d74ee9dca680a",
    "source_manifest_url": "https://drive.google.com/file/d/14lL-wbaefBcieLxVLVsoMXyvk_DdZCcc/view?usp=drivesdk",
    "source_snapshot_id": "GCFPE-REPAIR-RECOVERY-CORRECTION-20260914.1",
    "source_snapshot_sha256": "a8f3351c15279224af81eac4e013d7bbcc7436c3dd5b26b7385abd870f7160be"
  },
  "state_routes": {
    "CF-C-10": [
      {
        "applicable_states": [
          "KICKOFF_READY"
        ],
        "branch_id": "kickoff_ready",
        "condition": "valid CRD class selection and complete sanitized source",
        "destinations": [
          "CF-C-20"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-C-10.md",
          "section": "Required result and routing"
        },
        "state": "KICKOFF_READY",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "material_source_omission_recovery",
        "condition": "material source omission is repairable by the same kickoff owner",
        "destinations": [
          "CF-C-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-C-10.md",
          "section": "Required result and routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "class_or_identity_recovery",
        "condition": "CRD selection record or change identity is missing or conflicting; CF-PO-10 records exact existing evidence or requests Nathan's decision and never chooses the class",
        "destinations": [
          "CF-PO-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-C-10.md",
          "section": "Required result and routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "kickoff_terminal",
        "condition": "the Product Owner decision itself remains unavailable or another true authority/source stop has no runnable prompt receiver",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-C-10.md",
          "section": "Required result and routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": true
      }
    ],
    "CF-C-20": [
      {
        "applicable_states": [
          "SPECIFICATION_PENDING"
        ],
        "branch_id": "specification_pending",
        "condition": "complete pending CRD Specification is ready for Thoth review",
        "destinations": [
          "CF-C-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-C-20.md",
          "section": "Required result and routing"
        },
        "state": "SPECIFICATION_PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "invalid_kickoff_recovery",
        "condition": "kickoff is incomplete or contradictory and the kickoff owner can correct it",
        "destinations": [
          "CF-C-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-C-20.md",
          "section": "Required result and routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "specification_authoring_terminal",
        "condition": "unrecoverable source, identity, or authority blocker",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-C-20.md",
          "section": "Required result and routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": true
      }
    ],
    "CF-C-30": [
      {
        "applicable_states": [
          "INITIAL_APPROVE"
        ],
        "branch_id": "initial_approve",
        "condition": "initial approval; no addendum",
        "destinations": [
          "IA-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-C-30.md",
          "section": "Required result and routing"
        },
        "state": "INITIAL_APPROVE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "INITIAL_DENY"
        ],
        "branch_id": "initial_deny",
        "condition": "initial denial returns exact redlines to the same Isis author; no addendum",
        "destinations": [
          "CF-C-40"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-C-30.md",
          "section": "Required result and routing"
        },
        "state": "INITIAL_DENY",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "CORRECTION_REDLINE"
        ],
        "branch_id": "approved_base_correction_redline",
        "condition": "approved immutable CRD base plus a source-backed factual finding or actual authorized product/scope decision is assessed as justified; exact Thoth correction redline goes to the same Isis author for the first standalone pending delta; no approval or PF10 addendum",
        "next_prompt_handoff_count": 1,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-C-30.md",
          "section": "Required result and routing"
        },
        "state": "CORRECTION_REDLINE",
        "terminal_for_invocation": false,
        "destinations": [
          "CF-C-40"
        ],
        "notes": null
      },
      {
        "applicable_states": [
          "DELTA_APPROVE"
        ],
        "branch_id": "delta_approve",
          "condition": "material delta to an already approved base; exactly one addendum; reuse an existing read-back artifact for the same stable addendum_id and approved-delta digest; never duplicate; terminal for this invocation pending Nathan manual drain",
        "destinations": [
          "NATHAN_MANUAL_PF10_DRAIN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-C-30.md",
          "section": "Required result and routing"
        },
        "state": "DELTA_APPROVE",
        "terminal_for_invocation": true
      },
      {
        "applicable_states": [
          "DELTA_DENY"
        ],
        "branch_id": "delta_deny",
        "condition": "return bounded delta redlines to the same Specification author; no addendum",
        "destinations": [
          "CF-C-40"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-C-30.md",
          "section": "Required result and routing"
        },
        "state": "DELTA_DENY",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [],
        "branch_id": "review_terminal",
        "condition": "missing source, authority, or review mode",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-C-30.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": true
      },
      {
        "applicable_states": [],
        "branch_id": "correction_not_substantiated_terminal",
        "condition": "source-backed factual finding is assessed as unsupported; immutable approved base remains unchanged and no delta, denial, approval, or PF10 addendum is produced",
        "next_prompt_handoff_count": 0,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-C-30.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": true,
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "notes": null
      },
      {
        "applicable_states": [],
        "branch_id": "product_scope_decision_required_terminal",
        "condition": "the requested correction requires an unresolved genuine product-intent or scope choice; return the exact decision required to Nathan without disguising it as a factual correction",
        "next_prompt_handoff_count": 0,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-C-30.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": true,
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "notes": null
      }
    ],
    "CF-C-40": [
      {
        "applicable_states": [
          "SPECIFICATION_PENDING"
        ],
        "branch_id": "preapproval_revision",
        "condition": "pending preapproval CRD Specification corrected under the exact redline",
        "destinations": [
          "CF-C-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-C-40.md",
          "section": "Required result and routing"
        },
        "state": "SPECIFICATION_PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "SPECIFICATION_PENDING"
        ],
        "branch_id": "approved_base_first_delta_authoring",
        "condition": "first standalone CRD Specification delta authored from the exact Thoth correction assessment/redline; immutable approved base unchanged; return to the same Thoth reviewer for approved-base delta review",
        "next_prompt_handoff_count": 1,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-C-40.md",
          "section": "Required result and routing"
        },
        "state": "SPECIFICATION_PENDING",
        "terminal_for_invocation": false,
        "destinations": [
          "CF-C-30"
        ],
        "notes": null
      },
      {
        "applicable_states": [
          "SPECIFICATION_PENDING"
        ],
        "branch_id": "approved_base_delta_revision",
        "condition": "pending bounded approved-base SPECIFICATION_DELTA corrected without rewriting the approved base",
        "destinations": [
          "CF-C-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-C-40.md",
          "section": "Required result and routing"
        },
        "state": "SPECIFICATION_PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [],
        "branch_id": "redline_owner_recovery",
        "condition": "missing or contradictory redline/authority has an exact evidenced native owner",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "CONDITIONAL_RECOVERY",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-C-40.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [],
        "branch_id": "revision_terminal",
        "condition": "the redline or authority owner cannot be resolved",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-C-40.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": true
      }
    ],
    "CF-E-10": [
      {
        "applicable_states": [
          "KICKOFF_READY"
        ],
        "branch_id": "kickoff_ready",
        "condition": "valid Epic class selection and complete sanitized source",
        "destinations": [
          "CF-E-20"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-E-10.md",
          "section": "Required result and routing"
        },
        "state": "KICKOFF_READY",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "material_source_omission_recovery",
        "condition": "material source omission is repairable by the same kickoff owner",
        "destinations": [
          "CF-E-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-E-10.md",
          "section": "Required result and routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "class_selection_recovery",
        "condition": "Epic selection record or change identity is missing or conflicting; CF-PO-10 records exact existing evidence or requests Nathan's decision and never chooses the class",
        "destinations": [
          "CF-PO-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-E-10.md",
          "section": "Required result and routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "wrong_class_crd",
        "condition": "the supplied Product Owner class is CRD",
        "destinations": [
          "CF-C-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-E-10.md",
          "section": "Required result and routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "kickoff_terminal",
        "condition": "another true Product Owner/source/authority stop has no runnable receiver",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-E-10.md",
          "section": "Required result and routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": true
      }
    ],
    "CF-E-20": [
      {
        "applicable_states": [
          "SPECIFICATION_PENDING"
        ],
        "branch_id": "specification_pending",
        "condition": "complete pending Epic Specification is ready for Thoth review",
        "destinations": [
          "CF-E-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-E-20.md",
          "section": "Required result and routing"
        },
        "state": "SPECIFICATION_PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "invalid_kickoff_recovery",
        "condition": "kickoff is incomplete, defective, or contradictory and the kickoff owner can correct it",
        "destinations": [
          "CF-E-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-E-20.md",
          "section": "Required result and routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "specification_authoring_terminal",
        "condition": "unrecoverable source, identity, or authority blocker",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-E-20.md",
          "section": "Required result and routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": true
      }
    ],
    "CF-E-30": [
      {
        "applicable_states": [
          "INITIAL_APPROVE"
        ],
        "branch_id": "initial_approve",
        "condition": "initial approval; no addendum",
        "destinations": [
          "IA-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-E-30.md",
          "section": "Required result and routing"
        },
        "state": "INITIAL_APPROVE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "INITIAL_DENY"
        ],
        "branch_id": "initial_deny",
        "condition": "initial denial returns exact redlines to the same Isis author; no addendum",
        "destinations": [
          "CF-E-40"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-E-30.md",
          "section": "Required result and routing"
        },
        "state": "INITIAL_DENY",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "CORRECTION_REDLINE"
        ],
        "branch_id": "approved_base_correction_redline",
        "condition": "approved immutable Epic base plus a source-backed factual finding or actual authorized product/scope decision is assessed as justified; exact Thoth correction redline goes to the same Isis author for the first standalone pending delta; no approval or PF10 addendum",
        "next_prompt_handoff_count": 1,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-E-30.md",
          "section": "Required result and routing"
        },
        "state": "CORRECTION_REDLINE",
        "terminal_for_invocation": false,
        "destinations": [
          "CF-E-40"
        ],
        "notes": null
      },
      {
        "applicable_states": [
          "DELTA_APPROVE"
        ],
        "branch_id": "delta_approve",
          "condition": "material delta to an already approved base; exactly one addendum; reuse an existing read-back artifact for the same stable addendum_id and approved-delta digest; never duplicate; terminal for this invocation pending Nathan manual drain",
        "destinations": [
          "NATHAN_MANUAL_PF10_DRAIN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-E-30.md",
          "section": "Required result and routing"
        },
        "state": "DELTA_APPROVE",
        "terminal_for_invocation": true
      },
      {
        "applicable_states": [
          "DELTA_DENY"
        ],
        "branch_id": "delta_deny",
        "condition": "return bounded delta redlines to the same Specification author; no addendum",
        "destinations": [
          "CF-E-40"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-E-30.md",
          "section": "Required result and routing"
        },
        "state": "DELTA_DENY",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [],
        "branch_id": "review_terminal",
        "condition": "missing source, authority, or review mode",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-E-30.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": true
      },
      {
        "applicable_states": [],
        "branch_id": "correction_not_substantiated_terminal",
        "condition": "source-backed factual finding is assessed as unsupported; immutable approved base remains unchanged and no delta, denial, approval, or PF10 addendum is produced",
        "next_prompt_handoff_count": 0,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-E-30.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": true,
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "notes": null
      },
      {
        "applicable_states": [],
        "branch_id": "product_scope_decision_required_terminal",
        "condition": "the requested correction requires an unresolved genuine product-intent or scope choice; return the exact decision required to Nathan without disguising it as a factual correction",
        "next_prompt_handoff_count": 0,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-E-30.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": true,
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "notes": null
      }
    ],
    "CF-E-40": [
      {
        "applicable_states": [
          "SPECIFICATION_PENDING"
        ],
        "branch_id": "preapproval_revision",
        "condition": "pending preapproval Epic Specification corrected under the exact redline",
        "destinations": [
          "CF-E-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-E-40.md",
          "section": "Required result and routing"
        },
        "state": "SPECIFICATION_PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "SPECIFICATION_PENDING"
        ],
        "branch_id": "approved_base_first_delta_authoring",
        "condition": "first standalone Epic Specification delta authored from the exact Thoth correction assessment/redline; immutable approved base unchanged; return to the same Thoth reviewer for approved-base delta review",
        "next_prompt_handoff_count": 1,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-E-40.md",
          "section": "Required result and routing"
        },
        "state": "SPECIFICATION_PENDING",
        "terminal_for_invocation": false,
        "destinations": [
          "CF-E-30"
        ],
        "notes": null
      },
      {
        "applicable_states": [
          "SPECIFICATION_PENDING"
        ],
        "branch_id": "approved_base_delta_revision",
        "condition": "pending bounded approved-base SPECIFICATION_DELTA corrected without rewriting the approved base",
        "destinations": [
          "CF-E-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-E-40.md",
          "section": "Required result and routing"
        },
        "state": "SPECIFICATION_PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [],
        "branch_id": "redline_owner_recovery",
        "condition": "missing or contradictory redline/authority has an exact evidenced native owner",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "CONDITIONAL_RECOVERY",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-E-40.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [],
        "branch_id": "revision_terminal",
        "condition": "the redline or authority owner cannot be resolved",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-E-40.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": true
      }
    ],
    "CF-PO-10": [
      {
        "applicable_states": [
          "CLASS_SELECTED"
        ],
        "branch_id": "class_selected_epic",
        "condition": "CHANGE_CLASS=EPIC with an exact Product Owner selection and change identity",
        "destinations": [
          "CF-E-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-PO-10.md",
          "section": "Required result and routing"
        },
        "state": "CLASS_SELECTED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "CLASS_SELECTED"
        ],
        "branch_id": "class_selected_crd",
        "condition": "CHANGE_CLASS=CRD with an exact Product Owner selection and change identity",
        "destinations": [
          "CF-C-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-PO-10.md",
          "section": "Required result and routing"
        },
        "state": "CLASS_SELECTED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [],
        "branch_id": "selection_missing_or_conflicting",
        "condition": "no usable explicit Product Owner selection evidence, conflicting evidence, or unresolved change identity/source remains after CF-PO-10 requests or attempts to record it; return the exact requirement to Nathan with no CLASS_SELECTED result or kickoff",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CF-PO-10.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": true
      }
    ],
    "CL-20": [
      {
        "applicable_states": [
          "POST_CLOSURE_PENDING"
        ],
        "branch_id": "adr_branch",
        "condition": "the conditional ADR predicate is satisfied and the ADR branch is explicitly selected",
        "destinations": [
          "CL-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CL-20.md",
          "section": "Required result and routing"
        },
        "state": "POST_CLOSURE_PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "POST_CLOSURE_PENDING"
        ],
        "branch_id": "epic_pf09_revalidation",
        "condition": "the authorized Epic PF09 branch requires initial or corrected revalidation authoring",
        "destinations": [
          "CL-E-20"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CL-20.md",
          "section": "Required result and routing"
        },
        "state": "POST_CLOSURE_PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "POST_CLOSURE_PENDING"
        ],
        "branch_id": "epic_pf09_review",
        "condition": "the authorized Epic PF09 branch has a complete revalidation ready for review",
        "destinations": [
          "CL-E-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CL-20.md",
          "section": "Required result and routing"
        },
        "state": "POST_CLOSURE_PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "POST_CLOSURE_PENDING"
        ],
        "branch_id": "epic_pf09_maintenance",
        "condition": "the authorized Epic PF09 branch requires post-Epic maintenance authoring",
        "destinations": [
          "CL-E-40"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CL-20.md",
          "section": "Required result and routing"
        },
        "state": "POST_CLOSURE_PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "POST_CLOSURE_PENDING"
        ],
        "branch_id": "final_scan",
        "condition": "CL-20 and every actually selected managed post-closure branch have truthful dispositions",
        "destinations": [
          "CL-40"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CL-20.md",
          "section": "Required result and routing"
        },
        "state": "POST_CLOSURE_PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "POST_CLOSURE_PENDING"
        ],
        "branch_id": "native_owner_branch",
        "condition": "an exact manual, source-recovery, escalation, rescope, or other native owner branch is evidenced",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CL-20.md",
          "section": "Required result and routing"
        },
        "state": "POST_CLOSURE_PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "POST_CLOSURE_PENDING"
        ],
        "branch_id": "manual_or_owner_pending",
        "condition": "the required manual act or native owner cannot yet supply a runnable continuation",
        "destinations": [
          "ACTUAL_OWNER_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CL-20.md",
          "section": "Required result and routing"
        },
        "state": "POST_CLOSURE_PENDING",
        "terminal_for_invocation": true
      }
    ],
    "CL-30": [
      {
        "applicable_states": [
          "ADR_CANDIDATE"
        ],
        "branch_id": "adr_candidate_native_route",
        "condition": "the authorized repository or manual/TW maintenance receiver is exactly resolved",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CL-30.md",
          "section": "Required result and routing"
        },
        "state": "ADR_CANDIDATE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "NO_ADR_NEEDED"
        ],
        "branch_id": "no_adr_native_route",
        "condition": "an applicable source-native post-closure route remains",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CL-30.md",
          "section": "Required result and routing"
        },
        "state": "NO_ADR_NEEDED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "ADR_CANDIDATE",
          "NO_ADR_NEEDED"
        ],
        "branch_id": "final_scan",
        "condition": "CL-20 and every selected post-closure managed branch are complete or validly disposed",
        "destinations": [
          "CL-40"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "CONDITIONAL_CONTINUATION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CL-30.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "ADR_CANDIDATE",
          "NO_ADR_NEEDED"
        ],
        "branch_id": "adr_owner_terminal",
        "condition": "source-qualified recovery/manual/TW/terminal owner is not a runnable selected prompt",
        "destinations": [
          "ACTUAL_OWNER_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CL-30.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": true
      }
    ],
    "CL-40": [
      {
        "applicable_states": [
          "COMPLETE"
        ],
        "branch_id": "complete",
        "condition": "true end-cycle terminal",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CL-40.md",
          "section": "Required result and routing"
        },
        "state": "COMPLETE",
        "terminal_for_invocation": true
      },
      {
        "applicable_states": [
          "INCOMPLETE"
        ],
        "branch_id": "incomplete_same_task",
        "condition": "resume the same CL-40 task after the exact missing bounded condition is resolved",
        "destinations": [
          "CL-40"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CL-40.md",
          "section": "Required result and routing"
        },
        "state": "INCOMPLETE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [],
        "branch_id": "selected_native_boundary",
        "condition": "a selected post-closure, evidence, scope, acceptance, or recovery branch has an exact native owner",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "CONDITIONAL_RECOVERY",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CL-40.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [],
        "branch_id": "scan_terminal",
        "condition": "a true source/authority/manual-owner stop has no runnable selected receiver",
        "destinations": [
          "ACTUAL_OWNER_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CL-40.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": true
      }
    ],
    "CL-C-10": [
      {
        "applicable_states": [
          "CHANGE_CLOSED"
        ],
        "branch_id": "change_closed",
        "condition": "positive CRD closure decision",
        "destinations": [
          "CL-20"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CL-C-10.md",
          "section": "Required result and routing"
        },
        "state": "CHANGE_CLOSED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "DO_NOT_CLOSE"
        ],
        "branch_id": "do_not_close_new_remedy",
        "condition": "substantive new bounded remedy requires Thoth remediation",
        "destinations": [
          "ESC-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CL-C-10.md",
          "section": "Required result and routing"
        },
        "state": "DO_NOT_CLOSE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "DO_NOT_CLOSE"
        ],
        "branch_id": "do_not_close_existing_owner",
        "condition": "an already-authorized ordinary correction has an exact existing owner",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CL-C-10.md",
          "section": "Required result and routing"
        },
        "state": "DO_NOT_CLOSE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [],
        "branch_id": "shared_source_authority_terminal",
        "condition": "true source, authority, identity, or owner stop with no runnable selected receiver; preserve evidence and return without a handoff",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CL-C-10.md",
          "section": "Terminal operator return and receiver compatibility"
        },
        "state": null,
        "terminal_for_invocation": true
      }
    ],
    "CL-E-10": [
      {
        "applicable_states": [
          "CHANGE_CLOSED"
        ],
        "branch_id": "change_closed_postclosure",
        "condition": "positive Epic closure decision with ordinary post-closure work",
        "destinations": [
          "CL-20"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CL-E-10.md",
          "section": "Required result and routing"
        },
        "state": "CHANGE_CLOSED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "CHANGE_CLOSED"
        ],
        "branch_id": "change_closed_epic_pf09",
        "condition": "a separately authorized Epic PF09 revalidation branch is selected",
        "destinations": [
          "CL-E-20"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CL-E-10.md",
          "section": "Required result and routing"
        },
        "state": "CHANGE_CLOSED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "DO_NOT_CLOSE"
        ],
        "branch_id": "do_not_close_new_remedy",
        "condition": "substantive new bounded remedy requires Thoth remediation",
        "destinations": [
          "ESC-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CL-E-10.md",
          "section": "Required result and routing"
        },
        "state": "DO_NOT_CLOSE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "DO_NOT_CLOSE"
        ],
        "branch_id": "do_not_close_existing_owner",
        "condition": "an already-authorized ordinary correction has an exact existing owner",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CL-E-10.md",
          "section": "Required result and routing"
        },
        "state": "DO_NOT_CLOSE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [],
        "branch_id": "shared_source_authority_terminal",
        "condition": "true source, authority, identity, or owner stop with no runnable selected receiver; preserve evidence and return without a handoff",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/a/CL-E-10.md",
          "section": "Terminal operator return and receiver compatibility"
        },
        "state": null,
        "terminal_for_invocation": true
      }
    ],
    "CL-E-20": [
      {
        "applicable_states": [
          "COMPLETE"
        ],
        "branch_id": "complete",
        "condition": "complete PF09 revalidation is ready for review",
        "destinations": [
          "CL-E-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/CL-E-20.md",
          "section": "Required result and routing"
        },
        "state": "COMPLETE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "PARTIAL"
        ],
        "branch_id": "partial",
        "condition": "repairable authoring or evidence gap; same author/session resumes",
        "destinations": [
          "CL-E-20"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/CL-E-20.md",
          "section": "Required result and routing"
        },
        "state": "PARTIAL",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "blocked",
        "condition": "missing closure, unresolved authority, or unrecoverable source/access failure",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/CL-E-20.md",
          "section": "Required result and routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": true
      }
    ],
    "CL-E-30": [
      {
        "applicable_states": [
          "ACCEPT"
        ],
        "branch_id": "accept",
        "condition": "accepted revalidation",
        "destinations": [
          "CL-E-40"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/CL-E-30.md",
          "section": "Required result and routing"
        },
        "state": "ACCEPT",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "DENY"
        ],
        "branch_id": "deny",
        "condition": "denied revalidation returns to the same author",
        "destinations": [
          "CL-E-20"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/CL-E-30.md",
          "section": "Required result and routing"
        },
        "state": "DENY",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [],
        "branch_id": "review_terminal",
        "condition": "unresolved source, closure, authority, or owner",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/CL-E-30.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": true
      }
    ],
    "CL-E-40": [
      {
        "applicable_states": [
          "MAINTENANCE_PENDING"
        ],
        "branch_id": "selected_evidence_gap",
        "condition": "a selected evidence gap requires PF09 revalidation",
        "destinations": [
          "CL-E-20"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/CL-E-40.md",
          "section": "Required result and routing"
        },
        "state": "MAINTENANCE_PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "MAINTENANCE_PENDING"
        ],
        "branch_id": "final_scan",
        "condition": "every selected post-closure author/reviewer branch and CL-20 work has a truthful disposition",
        "destinations": [
          "CL-40"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/CL-E-40.md",
          "section": "Required result and routing"
        },
        "state": "MAINTENANCE_PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "MAINTENANCE_PENDING"
        ],
        "branch_id": "manual_tw_route",
        "condition": "the exact authorized manual/TW maintenance receiver is resolved",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/CL-E-40.md",
          "section": "Required result and routing"
        },
        "state": "MAINTENANCE_PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "MAINTENANCE_PENDING"
        ],
        "branch_id": "maintenance_terminal",
        "condition": "manual/TW receiver, source, closure, or authority remains unresolved",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/CL-E-40.md",
          "section": "Required result and routing"
        },
        "state": "MAINTENANCE_PENDING",
        "terminal_for_invocation": true
      }
    ],
    "DOC-10": [
      {
        "applicable_states": [
          "INSTRUCTION_READY"
        ],
        "branch_id": "instruction_ready",
        "condition": "complete documentation PR instruction is ready for detailed planning",
        "destinations": [
          "PR-20"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/DOC-10.md",
          "section": "Required result and routing"
        },
        "state": "INSTRUCTION_READY",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "DRAFT",
          "PENDING",
          "BLOCKED"
        ],
        "branch_id": "material_boundary",
        "condition": "repository evidence proves a complete bounded material boundary",
        "destinations": [
          "RS-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "CONDITIONAL_RECOVERY",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/DOC-10.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "DRAFT",
          "PENDING",
          "BLOCKED"
        ],
        "branch_id": "repairable_instruction_defect",
        "condition": "instruction defect is repairable in the same IA session from a saved checkpoint",
        "destinations": [
          "DOC-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "CONDITIONAL_RECOVERY",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/DOC-10.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "DRAFT",
          "PENDING",
          "BLOCKED"
        ],
        "branch_id": "instruction_terminal",
        "condition": "product-intent, source, authority, or unrecoverable evidence blocker",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/DOC-10.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": true
      }
    ],
    "DOC-20": [
      {
        "applicable_states": [
          "COMPLETE"
        ],
        "branch_id": "complete",
        "condition": "all documentation obligations and landed lineage are verified, and this is ordinary initial documentation or the remedy materially affects readiness or Nathan explicitly requires a QA-10 rerun",
        "destinations": [
          "QA-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/DOC-20.md",
          "section": "Required result and routing"
        },
        "state": "COMPLETE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "COMPLETE"
        ],
        "branch_id": "remediation_complete_native_return",
        "condition": "approved remediation documentation is verified without the QA-10 predicate; resolve the exact originating selected owner/stage and complete its native intake under unchanged authority",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/DOC-20.md",
          "section": "Result routing"
        },
        "state": "COMPLETE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "INCOMPLETE",
          "PENDING",
          "BLOCKED"
        ],
        "branch_id": "remediation_incomplete_native_return",
        "condition": "an incomplete or blocked remediation result has an exact lawful originating recovery/evidence owner and complete native return package; no PR-50, merge, PF10 drain or manual-gate bypass",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "CONDITIONAL_RECOVERY",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/DOC-20.md",
          "section": "Result routing"
        },
        "state": null,
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "INCOMPLETE",
          "PENDING",
          "BLOCKED"
        ],
        "branch_id": "instruction_repair",
        "condition": "documentation instruction is missing or defective",
        "destinations": [
          "DOC-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "CONDITIONAL_RECOVERY",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/DOC-20.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "INCOMPLETE",
          "PENDING",
          "BLOCKED"
        ],
        "branch_id": "landed_lineage_review",
        "condition": "actual merged state or landed-lineage review is required after Nathan asserts the manual merge",
        "destinations": [
          "PR-40"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "CONDITIONAL_RECOVERY",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/DOC-20.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "INCOMPLETE",
          "PENDING",
          "BLOCKED"
        ],
        "branch_id": "material_delta",
        "condition": "evidence proves a bounded material delta",
        "destinations": [
          "RS-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "CONDITIONAL_RECOVERY",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/DOC-20.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "INCOMPLETE",
          "PENDING",
          "BLOCKED"
        ],
        "branch_id": "documentation_terminal",
        "condition": "product-intent, source, authority, or unrecoverable merge-evidence failure",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/DOC-20.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": true
      }
    ],
    "ESC-10": [
      {
        "applicable_states": [
          "AWAITING_THOTH_REMEDIATION"
        ],
        "branch_id": "awaiting_thoth_remediation",
        "condition": "complete QA escalation report is ready for Thoth remediation",
        "destinations": [
          "ESC-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/ESC-10.md",
          "section": "Required result and routing"
        },
        "state": "AWAITING_THOTH_REMEDIATION",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [],
        "branch_id": "escalation_terminal",
        "condition": "missing decisive source, owner, authority, or irrecoverable evidence",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/ESC-10.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": true
      }
    ],
    "ESC-25": [
      {
        "applicable_states": [
          "COMPLETE"
        ],
        "branch_id": "complete",
        "condition": "complete discovery result returns to continuing Thoth",
        "destinations": [
          "ESC-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/ESC-25.md",
          "section": "Required result and routing"
        },
        "state": "COMPLETE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "PARTIAL"
        ],
        "branch_id": "partial",
        "condition": "usable partial discovery result returns to continuing Thoth",
        "destinations": [
          "ESC-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/ESC-25.md",
          "section": "Required result and routing"
        },
        "state": "PARTIAL",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "blocked_evidence_return",
        "condition": "a discovery fact is inaccessible but exact task, evidence/limitations and complete same-Thoth return package are known",
        "destinations": [
          "ESC-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/ESC-25.md",
          "section": "Result routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "blocked_terminal",
        "condition": "the exact discovery task/return owner or complete lawful return package cannot be established",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/ESC-25.md",
          "section": "Result routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": true
      }
    ],
    "ESC-30": [
      {
        "applicable_states": [
          "REMEDIATION_PENDING"
        ],
        "branch_id": "remediation_pending",
        "condition": "complete bounded remediation proposal is ready for continuing-Isis review",
        "destinations": [
          "ESC-40"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/ESC-30.md",
          "section": "Required result and routing"
        },
        "state": "REMEDIATION_PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "DISCOVERY_REQUIRED"
        ],
        "branch_id": "discovery_required",
        "condition": "one complete bounded discovery task is linked to the saved/read-back actual pending Thoth remediation record, which may truthfully be DISCOVERY_REQUIRED; no complete or approved remedy is invented",
        "destinations": [
          "ESC-25"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/ESC-30.md",
          "section": "Required result and routing"
        },
        "state": "DISCOVERY_REQUIRED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "blocked",
        "condition": "product-intent, authority, or decisive source blocker",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/ESC-30.md",
          "section": "Required result and routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": true
      }
    ],
    "ESC-40": [
      {
        "applicable_states": [
          "APPROVE"
        ],
        "branch_id": "approve",
        "condition": "qualifying approved remediation creates exactly one addendum and a conditional post-drain native-delivery handoff",
        "destinations": [
          "NATHAN_MANUAL_PF10_DRAIN"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/ESC-40.md",
          "section": "Required result and routing"
        },
        "state": "APPROVE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "APPROVE_AS_CHANGED"
        ],
        "branch_id": "approve_as_changed",
        "condition": "qualifying approved-as-changed remediation creates exactly one addendum and a conditional post-drain native-delivery handoff",
        "destinations": [
          "NATHAN_MANUAL_PF10_DRAIN"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/ESC-40.md",
          "section": "Required result and routing"
        },
        "state": "APPROVE_AS_CHANGED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "DENY"
        ],
        "branch_id": "deny",
        "condition": "return to remediation author; no addendum",
        "destinations": [
          "ESC-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/ESC-40.md",
          "section": "Required result and routing"
        },
        "state": "DENY",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [],
        "branch_id": "remediation_review_terminal",
        "condition": "native continuation identity, Product Owner/source, or authority predicate is unresolved",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/ESC-40.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": true
      }
    ],
    "GCFPE-MGMT-10": [
      {
        "applicable_states": [
          "ECOSYSTEM_CHANGE_COMPLETE"
        ],
        "branch_id": "maintenance_complete_terminal",
        "condition": "scoped maintenance complete; no exact further substantive invocation is both authorized and ready; return the saved/read-back GCFPE_ECOSYSTEM_CHANGE_REPORT to Nathan",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/GCFPE-MGMT-10.md",
          "section": "Result routing"
        },
        "state": "ECOSYSTEM_CHANGE_COMPLETE",
        "terminal_for_invocation": true
      },
      {
        "applicable_states": [
          "ECOSYSTEM_CHANGE_COMPLETE"
        ],
        "branch_id": "maintenance_complete_native_return",
        "condition": "scoped maintenance complete and the exact case separately authorizes one ready native continuation; resolve the actual selected receiver and preserve original authority, session and inputs; exclude PR-50, merge, PF10 drain, unselected candidates and unauthorized Alpha; emit one complete handoff without executing it",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/GCFPE-MGMT-10.md",
          "section": "Result routing"
        },
        "state": "ECOSYSTEM_CHANGE_COMPLETE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION"
        ],
        "branch_id": "ready_for_product_owner_alpha_resumption_decision",
        "condition": "separately authorized EPIC040 Alpha-preparation branch only, after exact approved promotion, complete production readback/validation and intact archival; exactly one saved/read-back PR-10 invocation for HDE-EPIC040-PR04, for Nathan to review and manually invoke; does not execute Alpha",
        "destinations": [
          "PR-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/GCFPE-MGMT-10.md",
          "section": "Separate EPIC040 Alpha preparation branch and Result routing"
        },
        "state": "READY_FOR_PRODUCT_OWNER_ALPHA_RESUMPTION_DECISION",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "IMPLEMENTATION_BLOCKED"
        ],
        "branch_id": "implementation_blocked",
        "condition": "real blocker; preserve a read-back recovery checkpoint and return to Nathan",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/GCFPE-MGMT-10.md",
          "section": "Required result and routing"
        },
        "state": "IMPLEMENTATION_BLOCKED",
        "terminal_for_invocation": true
      },
      {
        "applicable_states": [
          "PROMOTION_CHECKPOINT_REQUIRED"
        ],
        "branch_id": "promotion_checkpoint_required",
        "condition": "exact-snapshot promotion approval or a required active control-layer checkpoint is outstanding; return the fully specified imminent transaction without treating general repair authorization as promotion approval",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/GCFPE-MGMT-10.md",
          "section": "Required result and routing"
        },
        "state": "PROMOTION_CHECKPOINT_REQUIRED",
        "terminal_for_invocation": true
      }
    ],
    "IA-10": [
      {
        "applicable_states": [
          "PLAN_PENDING"
        ],
        "branch_id": "audit_and_plan_complete",
        "condition": "both Implementation Audit and initial Plan are complete and decisive architecture/feasibility questions are resolved for submission",
        "destinations": [
          "IA-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/IA-10.md",
          "section": "Required result and routing"
        },
        "state": "PLAN_PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "audit_recovery",
        "condition": "Audit is incomplete but useful local recovery remains in the same IA session; no separate answer-seeding or research package is required",
        "destinations": [
          "IA-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/IA-10.md",
          "section": "Required result and routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "AUDIT_COMPLETE"
        ],
        "branch_id": "plan_interrupted",
        "condition": "Audit is complete and the Plan phase was interrupted; no separate answer-seeding or research package is required first",
        "destinations": [
          "IA-20"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/IA-10.md",
          "section": "Required result and routing"
        },
        "state": "AUDIT_COMPLETE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "initial_denial_correction",
        "condition": "an exact initial Plan denial correction is already authorized",
        "destinations": [
          "IA-40"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/IA-10.md",
          "section": "Required result and routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "bounded_research",
        "condition": "a complete bounded planning research need is identified and no usable answer exists yet; carry PLANNING_INQUIRY and RECOVERY_ENVELOPE",
        "destinations": [
          "IA-60"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/IA-10.md",
          "section": "Required result and routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "answer_available",
        "condition": "an actual partial or complete answer is available for bounded validation/application; carry complete RECOVERY_ENVELOPE and ANSWER_REF with exact paused artifacts and authority; preserve unanswered questions and deadlines and same-author return; do not repeat research or infer whole-Plan readiness",
        "destinations": [
          "IA-50"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/IA-10.md",
          "section": "Planning readiness, questions, and recovery; Result routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "ia10_terminal",
        "condition": "approved-base rewrite request, product decision, or unrecoverable source/authority blocker",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/IA-10.md",
          "section": "Required result and routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": true
      }
    ],
    "IA-20": [
      {
        "applicable_states": [
          "PLAN_PENDING"
        ],
        "branch_id": "plan_pending",
        "condition": "complete initial Plan is ready for Isis review with decisive architecture/feasibility questions resolved",
        "destinations": [
          "IA-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/IA-20.md",
          "section": "Required result and routing"
        },
        "state": "PLAN_PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "plan_recovery",
        "condition": "Plan remains incomplete but useful local recovery remains in the same IA session; no separate answer-seeding or research package is required",
        "destinations": [
          "IA-20"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/IA-20.md",
          "section": "Required result and routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "initial_denial_correction",
        "condition": "an exact initial denial correction is already authorized",
        "destinations": [
          "IA-40"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/IA-20.md",
          "section": "Required result and routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "bounded_research",
        "condition": "a bounded planning research need is identified and no usable answer exists yet; carry PLANNING_INQUIRY and RECOVERY_ENVELOPE",
        "destinations": [
          "IA-60"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/IA-20.md",
          "section": "Required result and routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "answer_available",
        "condition": "an actual partial or complete answer is available for bounded validation/application; carry complete RECOVERY_ENVELOPE and ANSWER_REF, valid completed Audit and exact Plan checkpoint; preserve unanswered questions and deadlines and same-author return; do not repeat research or infer whole-Plan readiness",
        "destinations": [
          "IA-50"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/IA-20.md",
          "section": "Planning readiness, questions, and recovery; Result routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "ia20_terminal",
        "condition": "approved-base rewrite request, product decision, or unrecoverable source/authority blocker",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/IA-20.md",
          "section": "Required result and routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": true
      }
    ],
    "IA-30": [
      {
        "applicable_states": [
          "APPROVE"
        ],
        "branch_id": "initial_approve",
        "condition": "REVIEW_MODE=INITIAL and the pending whole-change Plan is approved; no addendum",
        "destinations": [
          "PR-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/IA-30.md",
          "section": "Required result and routing"
        },
        "state": "APPROVE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "DENY"
        ],
        "branch_id": "initial_deny",
        "condition": "REVIEW_MODE=INITIAL; exact redlines return to the same IA author",
        "destinations": [
          "IA-40"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/IA-30.md",
          "section": "Required result and routing"
        },
        "state": "DENY",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "DENY"
        ],
        "branch_id": "material_delta_deny",
        "condition": "REVIEW_MODE=MATERIAL_DELTA; return denial to the exact recorded proposed-delta author",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/IA-30.md",
          "section": "Required result and routing"
        },
        "state": "DENY",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "APPROVE"
        ],
        "branch_id": "material_delta_approve",
        "condition": "REVIEW_MODE=MATERIAL_DELTA; exactly one addendum and conditional post-drain native continuation",
        "destinations": [
          "NATHAN_MANUAL_PF10_DRAIN"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/IA-30.md",
          "section": "Required result and routing"
        },
        "state": "APPROVE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [],
        "branch_id": "plan_review_terminal",
        "condition": "source, authority, manual-continuation identity, or Product Owner decision blocker",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/b/IA-30.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": true
      }
    ],
    "IA-40": [
      {
        "applicable_states": [
          "PLAN_PENDING_REVISED"
        ],
        "branch_id": "plan_pending_revised",
        "condition": "valid preapproval revision returns to the same Isis reviewer",
        "destinations": [
          "IA-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/IA-40.md",
          "section": "Required result and routing"
        },
        "state": "PLAN_PENDING_REVISED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "WRONG_ROUTE_APPROVED_BASE"
        ],
        "branch_id": "approved_base_rescope",
        "condition": "the approved-base request is a bounded rescope with complete RS-20 intake",
        "destinations": [
          "RS-20"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/IA-40.md",
          "section": "Required result and routing"
        },
        "state": "WRONG_ROUTE_APPROVED_BASE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "WRONG_ROUTE_APPROVED_BASE"
        ],
        "branch_id": "approved_base_remediation",
        "condition": "the approved-base request is an already-authored bounded remediation ready for Isis review",
        "destinations": [
          "ESC-40"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/IA-40.md",
          "section": "Required result and routing"
        },
        "state": "WRONG_ROUTE_APPROVED_BASE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "WRONG_ROUTE_APPROVED_BASE"
        ],
        "branch_id": "approved_base_plan_delta",
        "condition": "the approved-base request is another material whole-Plan delta for IA-30 bounded-delta review",
        "destinations": [
          "IA-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/IA-40.md",
          "section": "Required result and routing"
        },
        "state": "WRONG_ROUTE_APPROVED_BASE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "WRONG_ROUTE_APPROVED_BASE"
        ],
        "branch_id": "approved_base_terminal",
        "condition": "the actual qualifying approver or source/authority predicate cannot be resolved",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/IA-40.md",
          "section": "Required result and routing"
        },
        "state": "WRONG_ROUTE_APPROVED_BASE",
        "terminal_for_invocation": true
      }
    ],
    "IA-50": [
      {
        "applicable_states": [
          "SEED_READY"
        ],
        "branch_id": "seed_incomplete_audit",
        "condition": "the validated answer applies to an incomplete IA-10 Audit",
        "destinations": [
          "IA-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/IA-50.md",
          "section": "Required result and routing"
        },
        "state": "SEED_READY",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "SEED_READY"
        ],
        "branch_id": "seed_paused_plan",
        "condition": "the Audit is complete and the answer applies to a paused initial Plan",
        "destinations": [
          "IA-20"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/IA-50.md",
          "section": "Required result and routing"
        },
        "state": "SEED_READY",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "SEED_READY"
        ],
        "branch_id": "seed_plan_review",
        "condition": "same-Isis correction intake or material approved-Plan delta lacks an existing correction instruction",
        "destinations": [
          "IA-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/IA-50.md",
          "section": "Required result and routing"
        },
        "state": "SEED_READY",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "SEED_READY"
        ],
        "branch_id": "seed_preapproval_correction",
        "condition": "the answer applies to an authorized pending-preapproval Plan correction",
        "destinations": [
          "IA-40"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/IA-50.md",
          "section": "Required result and routing"
        },
        "state": "SEED_READY",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "SEED_READY"
        ],
        "branch_id": "seed_remediation_review",
        "condition": "the answer belongs to integrated remediation with a complete pending Thoth proposal",
        "destinations": [
          "ESC-40"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/IA-50.md",
          "section": "Required result and routing"
        },
        "state": "SEED_READY",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "SEED_INCOMPLETE"
        ],
        "branch_id": "duplicate_existing_continuation",
        "condition": "a duplicate answer is already applied and its existing valid continuation/result is exactly resolved; reuse it without creating another successor",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/IA-50.md",
          "section": "Required result and routing"
        },
        "state": "SEED_INCOMPLETE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "SEED_INCOMPLETE"
        ],
        "branch_id": "seed_incomplete_terminal",
        "condition": "answer is stale, contradictory, incomplete, duplicate without a resolvable continuation, or wrong-authority; return evidence to the actual answer/base owner with no synthetic runnable successor",
        "destinations": [
          "ACTUAL_OWNER_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/IA-50.md",
          "section": "Required result and routing"
        },
        "state": "SEED_INCOMPLETE",
        "terminal_for_invocation": true
      }
    ],
    "IA-60": [
      {
        "applicable_states": [
          "RESEARCH_COMPLETE"
        ],
        "branch_id": "research_to_seeder",
        "condition": "bounded planning finding is complete and authorized for answer seeding",
        "destinations": [
          "IA-50"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/IA-60.md",
          "section": "Required result and routing"
        },
        "state": "RESEARCH_COMPLETE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "RESEARCH_COMPLETE"
        ],
        "branch_id": "research_post_failure_remediation",
        "condition": "the complete finding is actual post-failure remediation evidence with unchanged ESC-30 native inputs",
        "destinations": [
          "ESC-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/IA-60.md",
          "section": "Required result and routing"
        },
        "state": "RESEARCH_COMPLETE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "PARTIAL"
        ],
        "branch_id": "partial",
        "condition": "incomplete evidence or missing owner decision prevents a synthetic IA-50 continuation",
        "destinations": [
          "ACTUAL_OWNER_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/IA-60.md",
          "section": "Required result and routing"
        },
        "state": "PARTIAL",
        "terminal_for_invocation": true
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "blocked",
        "condition": "source, authority, or terminal owner stop; return the exact question/evidence to its native owner",
        "destinations": [
          "ACTUAL_OWNER_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/IA-60.md",
          "section": "Required result and routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": true
      }
    ],
    "MGR-10": [
      {
        "applicable_states": [
          "FLOW_PROGRESS"
        ],
        "branch_id": "class_selection",
        "condition": "new cycle entry has no Product Owner class-decision evidence, or has exact evidence whose selection record is missing; CF-PO-10 receives the unresolved or evidenced-recording case and never chooses the class",
        "destinations": [
          "CF-PO-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/MGR-10.md",
          "section": "Required result and routing"
        },
        "state": "FLOW_PROGRESS",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "FLOW_PROGRESS"
        ],
        "branch_id": "epic_entry",
        "condition": "new cycle entry has an exact Epic classification and complete intake",
        "destinations": [
          "CF-E-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/MGR-10.md",
          "section": "Required result and routing"
        },
        "state": "FLOW_PROGRESS",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "FLOW_PROGRESS"
        ],
        "branch_id": "crd_entry",
        "condition": "new cycle entry has an exact CRD classification and complete intake",
        "destinations": [
          "CF-C-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/MGR-10.md",
          "section": "Required result and routing"
        },
        "state": "FLOW_PROGRESS",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "FLOW_PROGRESS"
        ],
        "branch_id": "pre_qa",
        "condition": "the exact next unmet contract is integrated pre-QA audit/triage/readiness",
        "destinations": [
          "QA-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/MGR-10.md",
          "section": "Required result and routing"
        },
        "state": "FLOW_PROGRESS",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "FLOW_PROGRESS"
        ],
        "branch_id": "final_scan",
        "condition": "closure and all selected post-closure work are disposed and the final scan is next",
        "destinations": [
          "CL-40"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/MGR-10.md",
          "section": "Required result and routing"
        },
        "state": "FLOW_PROGRESS",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "FLOW_PROGRESS"
        ],
        "branch_id": "other_native_stage",
        "condition": "another exact selected native stage is the evidenced next unmet contract; the dynamic boundary resolves one prompt at runtime",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/MGR-10.md",
          "section": "Required result and routing"
        },
        "state": "FLOW_PROGRESS",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "TERMINAL_RETURN"
        ],
        "branch_id": "terminal_return",
        "condition": "true completed-cycle or Product Owner terminal return",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/MGR-10.md",
          "section": "Required result and routing"
        },
        "state": "TERMINAL_RETURN",
        "terminal_for_invocation": true
      }
    ],
    "OPS-10": [
      {
        "applicable_states": [
          "READY"
        ],
        "branch_id": "ready",
        "condition": "complete bounded OPS_TASK with actual action authority is ready for execution",
        "destinations": [
          "OPS-20"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/OPS-10.md",
          "section": "Required result and routing"
        },
        "state": "READY",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [],
        "branch_id": "remediation_discovery",
        "condition": "the exact authorized remediation package requires bounded discovery",
        "destinations": [
          "ESC-25"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "CONDITIONAL_CONTINUATION",
        "route_steps": [
          "OPS-10 -> ESC-25",
          "ESC-25 result -> ESC-30"
        ],
        "source_evidence": {
          "path": "candidate/prompts/c/OPS-10.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [],
        "branch_id": "material_boundary_proposal",
        "condition": "a new complete material boundary requires a bounded rescope proposal",
        "destinations": [
          "RS-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "CONDITIONAL_RECOVERY",
        "route_steps": [
          "OPS-10 -> RS-10",
          "RS-10 complete proposal -> RS-20",
          "RS-20 REVISION_REQUIRED -> RS-30"
        ],
        "source_evidence": {
          "path": "candidate/prompts/c/OPS-10.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "blocked_native_owner",
        "condition": "the complete recovery package resolves the same creator or exact native owner",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/OPS-10.md",
          "section": "Required result and routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "blocked_terminal",
        "condition": "a decisive source, authority, target, or owner fact prevents a runnable task",
        "destinations": [
          "ACTUAL_OWNER_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/OPS-10.md",
          "section": "Required result and routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": true
      }
    ],
    "OPS-20": [
      {
        "applicable_states": [
          "COMPLETE"
        ],
        "branch_id": "result_complete",
        "condition": "one truthful OPS_EXECUTION_RESULT returns to the task creator and receipt reviewer",
        "destinations": [
          "OPS-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/OPS-20.md",
          "section": "Required result and routing"
        },
        "state": "COMPLETE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "PARTIAL"
        ],
        "branch_id": "result_partial",
        "condition": "one truthful OPS_EXECUTION_RESULT returns to the task creator and receipt reviewer",
        "destinations": [
          "OPS-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/OPS-20.md",
          "section": "Required result and routing"
        },
        "state": "PARTIAL",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "result_blocked",
        "condition": "one truthful OPS_EXECUTION_RESULT returns to the task creator and receipt reviewer",
        "destinations": [
          "OPS-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/OPS-20.md",
          "section": "Required result and routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "FAILED"
        ],
        "branch_id": "result_failed",
        "condition": "one truthful OPS_EXECUTION_RESULT returns to the task creator and receipt reviewer",
        "destinations": [
          "OPS-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/OPS-20.md",
          "section": "Required result and routing"
        },
        "state": "FAILED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "NOT_EXECUTED"
        ],
        "branch_id": "result_notexecuted",
        "condition": "one truthful OPS_EXECUTION_RESULT returns to the task creator and receipt reviewer",
        "destinations": [
          "OPS-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/OPS-20.md",
          "section": "Required result and routing"
        },
        "state": "NOT_EXECUTED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "NOT_PRODUCED"
        ],
        "branch_id": "result_notproduced",
        "condition": "one truthful OPS_EXECUTION_RESULT returns to the task creator and receipt reviewer",
        "destinations": [
          "OPS-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/OPS-20.md",
          "section": "Required result and routing"
        },
        "state": "NOT_PRODUCED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "PARTIAL",
          "BLOCKED",
          "FAILED",
          "NOT_EXECUTED",
          "NOT_PRODUCED"
        ],
        "branch_id": "remediation_discovery",
        "condition": "the exact authorized remediation package requires bounded discovery before Thoth resumes",
        "destinations": [
          "ESC-25"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "CONDITIONAL_CONTINUATION",
        "route_steps": [
          "OPS-20 -> ESC-25",
          "ESC-25 result -> ESC-30"
        ],
        "source_evidence": {
          "path": "candidate/prompts/c/OPS-20.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "PARTIAL",
          "BLOCKED",
          "FAILED",
          "NOT_EXECUTED",
          "NOT_PRODUCED"
        ],
        "branch_id": "material_boundary_proposal",
        "condition": "actual execution evidence establishes a new bounded material boundary requiring proposal",
        "destinations": [
          "RS-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "CONDITIONAL_RECOVERY",
        "route_steps": [
          "OPS-20 -> RS-10",
          "RS-10 complete proposal -> RS-20",
          "RS-20 REVISION_REQUIRED -> RS-30"
        ],
        "source_evidence": {
          "path": "candidate/prompts/c/OPS-20.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "PARTIAL",
          "BLOCKED",
          "FAILED",
          "NOT_EXECUTED",
          "NOT_PRODUCED"
        ],
        "branch_id": "ops_execution_native_owner",
        "condition": "a blocked, incomplete, contradictory, or access-limited result has an exact native owner",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "CONDITIONAL_RECOVERY",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/OPS-20.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED",
          "FAILED",
          "NOT_EXECUTED",
          "NOT_PRODUCED"
        ],
        "branch_id": "ops_execution_terminal",
        "condition": "a decisive source, authority, target, access, or owner fact prevents any runnable continuation",
        "destinations": [
          "ACTUAL_OWNER_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/OPS-20.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": true
      }
    ],
    "OPS-30": [
      {
        "applicable_states": [
          "ACCEPT"
        ],
        "branch_id": "accept_native_consumer",
        "condition": "accepted receipt returns to the exact Plan-named downstream consumer or same creator IA",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/OPS-30.md",
          "section": "Required result and routing"
        },
        "state": "ACCEPT",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "REJECT"
        ],
        "branch_id": "reject_corrective_task",
        "condition": "bounded correction or retry begins with a new corrective OPS_TASK; OPS-20 follows only after that task is complete",
        "destinations": [
          "OPS-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [
          "OPS-30 -> OPS-10",
          "complete corrective OPS_TASK -> OPS-20",
          "OPS_EXECUTION_RESULT -> OPS-30"
        ],
        "source_evidence": {
          "path": "candidate/prompts/c/OPS-30.md",
          "section": "Required result and routing"
        },
        "state": "REJECT",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "REJECT"
        ],
        "branch_id": "remediation_discovery",
        "condition": "the actual receipt and remediation package explicitly require bounded discovery",
        "destinations": [
          "ESC-25"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "CONDITIONAL_RECOVERY",
        "route_steps": [
          "OPS-30 -> ESC-25",
          "ESC-25 result -> ESC-30"
        ],
        "source_evidence": {
          "path": "candidate/prompts/c/OPS-30.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "REJECT"
        ],
        "branch_id": "material_boundary",
        "condition": "the actual receipt establishes a material scope, architecture, requirement, or design boundary",
        "destinations": [
          "RS-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "CONDITIONAL_RECOVERY",
        "route_steps": [
          "OPS-30 -> RS-10",
          "RS-10 complete proposal -> RS-20",
          "RS-20 REVISION_REQUIRED -> RS-30"
        ],
        "source_evidence": {
          "path": "candidate/prompts/c/OPS-30.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "REJECT"
        ],
        "branch_id": "receipt_native_owner",
        "condition": "a blocked, contradictory, incomplete, or access-limited receipt has an exact native recovery owner",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "CONDITIONAL_RECOVERY",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/OPS-30.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "REJECT"
        ],
        "branch_id": "receipt_terminal",
        "condition": "the exact native recovery owner or decisive prerequisite is unresolved",
        "destinations": [
          "ACTUAL_OWNER_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/OPS-30.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": true
      }
    ],
    "PR-10": [
      {
        "applicable_states": [
          "INSTRUCTION_READY"
        ],
        "branch_id": "instruction_ready",
        "condition": "complete approved-scope instruction is ready for detailed planning",
        "destinations": [
          "PR-20"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/PR-10.md",
          "section": "Required result and routing"
        },
        "state": "INSTRUCTION_READY",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "DRAFT",
          "BLOCKED"
        ],
        "branch_id": "material_boundary",
        "condition": "a genuine material scope, architecture, requirement, or design boundary is substantiated",
        "destinations": [
          "RS-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "CONDITIONAL_RECOVERY",
        "route_steps": [
          "PR-10 -> RS-10",
          "RS-10 complete proposal -> RS-20"
        ],
        "source_evidence": {
          "path": "candidate/prompts/c/PR-10.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "DRAFT",
          "BLOCKED"
        ],
        "branch_id": "same_owner_recovery",
        "condition": "an ordinary instruction defect is repairable by the same PR-10 owner",
        "destinations": [
          "PR-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "CONDITIONAL_RECOVERY",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/PR-10.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "DRAFT",
          "BLOCKED"
        ],
        "branch_id": "upstream_owner_recovery",
        "condition": "the defective upstream Plan, review, remediation, Specification, or other source has an exact native owner",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "CONDITIONAL_RECOVERY",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/PR-10.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "DRAFT",
          "BLOCKED"
        ],
        "branch_id": "instruction_terminal",
        "condition": "accepted manual prerequisite or true source/authority/product decision has no runnable prompt receiver",
        "destinations": [
          "ACTUAL_OWNER_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/PR-10.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": true
      }
    ],
    "PR-20": [
      {
        "applicable_states": [
          "AWAITING_PO_PROCEED"
        ],
        "branch_id": "awaiting_po_proceed",
        "condition": "one complete executable approved-scope plan awaits the original Product Owner Proceed",
        "destinations": [
          "NATHAN_PROCEED"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/PR-20.md",
          "section": "Required result and routing"
        },
        "state": "AWAITING_PO_PROCEED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "DRAFT",
          "BLOCKED"
        ],
        "branch_id": "material_boundary",
        "condition": "the planning result substantiates a material scope, architecture, requirement, or design boundary",
        "destinations": [
          "RS-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "CONDITIONAL_RECOVERY",
        "route_steps": [
          "PR-20 -> RS-10",
          "RS-10 complete proposal -> RS-20"
        ],
        "source_evidence": {
          "path": "candidate/prompts/c/PR-20.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "DRAFT",
          "BLOCKED"
        ],
        "branch_id": "same_owner_recovery",
        "condition": "a bounded planning defect is repairable by the same dedicated PR planning session",
        "destinations": [
          "PR-20"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "CONDITIONAL_RECOVERY",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/PR-20.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "DRAFT",
          "BLOCKED"
        ],
        "branch_id": "upstream_owner_recovery",
        "condition": "the exact upstream instruction, Plan, remediation, Specification, or other source owner must act",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "CONDITIONAL_RECOVERY",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/PR-20.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "DRAFT",
          "BLOCKED"
        ],
        "branch_id": "planning_terminal",
        "condition": "accepted manual prerequisite or true source/authority/product decision has no runnable prompt receiver",
        "destinations": [
          "ACTUAL_OWNER_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/PR-20.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": true
      }
    ],
    "PR-30": [
      {
        "applicable_states": [
          "PR_CANDIDATE_PUBLISHED"
        ],
        "branch_id": "pr_candidate_published",
        "condition": "one complete same-session phase continuation",
        "destinations": [
          "PR-35"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/PR-30.md",
          "section": "Required result and routing"
        },
        "state": "PR_CANDIDATE_PUBLISHED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "RESCOPE_PENDING"
        ],
        "branch_id": "rescope_pending",
        "condition": "formal RESCOPE_REQUEST with exact PR_RETURN_PHASE",
        "destinations": [
          "RS-20"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/PR-30.md",
          "section": "Required result and routing"
        },
        "state": "RESCOPE_PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "RECOVERY_PENDING"
        ],
        "branch_id": "recovery_pending",
        "condition": "complete same-session re-entry; no new vehicle",
        "destinations": [
          "PR-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/PR-30.md",
          "section": "Required result and routing"
        },
        "state": "RECOVERY_PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "PRODUCT_OWNER_DECISION_REQUIRED"
        ],
        "branch_id": "product_owner_decision_required",
        "condition": "genuine Product Owner decision outside existing PR authority",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/PR-30.md",
          "section": "Required result and routing"
        },
        "state": "PRODUCT_OWNER_DECISION_REQUIRED",
        "terminal_for_invocation": true
      },
      {
        "applicable_states": [],
        "branch_id": "pr30_terminal",
        "condition": "unrecoverable source, owner, authority, or incompatible identity; never convert this into PR-50",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/PR-30.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": true
      }
    ],
    "PR-35": [
      {
        "applicable_states": [
          "MERGE_PENDING"
        ],
        "branch_id": "merge_pending",
        "condition": "conditional PR-40 invocation usable only after Nathan manually merges",
        "destinations": [
          "NATHAN_MANUAL_MERGE_ASSERTION"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/PR-35.md",
          "section": "Required result and routing"
        },
        "state": "MERGE_PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "RESCOPE_PENDING"
        ],
        "branch_id": "rescope_pending",
        "condition": "formal RESCOPE_REQUEST with PR_RETURN_PHASE=PR-35",
        "destinations": [
          "RS-20"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/PR-35.md",
          "section": "Required result and routing"
        },
        "state": "RESCOPE_PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "RECOVERY_PENDING"
        ],
        "branch_id": "recovery_pending",
        "condition": "complete same-session re-entry with checkpoint",
        "destinations": [
          "PR-35"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/PR-35.md",
          "section": "Required result and routing"
        },
        "state": "RECOVERY_PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "REMOTE_EVIDENCE_PENDING"
        ],
        "branch_id": "remote_evidence_pending",
        "condition": "actual remote evidence unavailable and no local action remains; durable checkpoint required",
        "destinations": [
          "PR-35"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/PR-35.md",
          "section": "Required result and routing"
        },
        "state": "REMOTE_EVIDENCE_PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "PRODUCT_OWNER_DECISION_REQUIRED"
        ],
        "branch_id": "product_owner_decision_required",
        "condition": "genuine Product Owner decision outside existing PR authority",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/PR-35.md",
          "section": "Required result and routing"
        },
        "state": "PRODUCT_OWNER_DECISION_REQUIRED",
        "terminal_for_invocation": true
      }
    ],
    "PR-40": [
      {
        "applicable_states": [
          "ACCEPT"
        ],
        "branch_id": "accept",
        "condition": "return the accepted whole-unit result to the same whole-change IA/native Plan-progress owner",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/PR-40.md",
          "section": "Required result and routing"
        },
        "state": "ACCEPT",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "REJECT"
        ],
        "branch_id": "reject_existing_pr_owner",
        "condition": "a precise in-scope implementation/review/corrected-code/PR-lineage defect has an authorized existing PR vehicle and original Proceed",
        "destinations": [
          "PR-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/PR-40.md",
          "section": "Required result and routing"
        },
        "state": "REJECT",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "REJECT"
        ],
        "branch_id": "reject_instruction_owner",
        "condition": "the substantiated in-scope defect is in the IA-issued PR instruction",
        "destinations": [
          "PR-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/PR-40.md",
          "section": "Required result and routing"
        },
        "state": "REJECT",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "REJECT"
        ],
        "branch_id": "reject_material_boundary_proposal",
        "condition": "a substantiated material boundary requires a new bounded rescope proposal",
        "destinations": [
          "RS-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [
          "PR-40 -> RS-10",
          "RS-10 complete proposal -> RS-20",
          "RS-20 REVISION_REQUIRED -> RS-30"
        ],
        "source_evidence": {
          "path": "candidate/prompts/c/PR-40.md",
          "section": "Required result and routing"
        },
        "state": "REJECT",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "PENDING"
        ],
        "branch_id": "pending_native_owner",
        "condition": "the exact Product Owner, evidence, PR, or IA recovery owner is known and can perform the bounded missing act",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/PR-40.md",
          "section": "Required result and routing"
        },
        "state": "PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "PENDING"
        ],
        "branch_id": "pending_terminal",
        "condition": "manual merge, repository fact, review result, or evidence remains unavailable and no runnable native owner prompt is resolved",
        "destinations": [
          "ACTUAL_OWNER_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/PR-40.md",
          "section": "Required result and routing"
        },
        "state": "PENDING",
        "terminal_for_invocation": true
      },
      {
        "applicable_states": [],
        "branch_id": "lineage_review_terminal",
        "condition": "an in-scope correction lacks required repository authority/vehicle or another genuine Product Owner decision is required",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/PR-40.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": true
      }
    ],
    "PR-50": [
      {
        "applicable_states": [
          "PR_ABORTED_ESCALATED"
        ],
        "branch_id": "pr_aborted_escalated",
        "condition": "terminal record after Nathan-only identified-PR invocation",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/PR-50.md",
          "section": "Required result and routing"
        },
        "state": "PR_ABORTED_ESCALATED",
        "terminal_for_invocation": true
      }
    ],
    "QA-10": [
      {
        "applicable_states": [
          "READY_FOR_QA"
        ],
        "branch_id": "ready_for_qa",
        "condition": "complete integrated audit/triage/readiness supports live QA Guide creation",
        "destinations": [
          "QA-20"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/QA-10.md",
          "section": "Required result and routing"
        },
        "state": "READY_FOR_QA",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "NOT_READY"
        ],
        "branch_id": "not_ready",
        "condition": "evidence proves failure of an applicable approved Plan objective",
        "destinations": [
          "ESC-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/QA-10.md",
          "section": "Required result and routing"
        },
        "state": "NOT_READY",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "ASSESSMENT_INCOMPLETE"
        ],
        "branch_id": "evidence_owner_recovery",
        "condition": "the exact evidence/retrieval owner is identified and can perform the smallest supported recovery",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/QA-10.md",
          "section": "Required result and routing"
        },
        "state": "ASSESSMENT_INCOMPLETE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "NOT_READY",
          "ASSESSMENT_INCOMPLETE"
        ],
        "branch_id": "material_native_boundary",
        "condition": "a substantiated material scope, Canon, Specification, Plan, or authority boundary has an exact native owner",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "CONDITIONAL_RECOVERY",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/QA-10.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "ASSESSMENT_INCOMPLETE"
        ],
        "branch_id": "qa10_terminal",
        "condition": "manual prerequisite, source/authority stop, or unresolved evidence owner prevents a runnable continuation",
        "destinations": [
          "ACTUAL_OWNER_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/c/QA-10.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": true
      }
    ],
    "QA-100": [
      {
        "applicable_states": [
          "COMPLETE"
        ],
        "branch_id": "complete",
        "condition": "execution receipt always returns to evidence reviewer",
        "destinations": [
          "QA-110"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-100.md",
          "section": "Required result and routing"
        },
        "state": "COMPLETE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "PARTIAL"
        ],
        "branch_id": "partial",
        "condition": "execution receipt always returns to evidence reviewer",
        "destinations": [
          "QA-110"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-100.md",
          "section": "Required result and routing"
        },
        "state": "PARTIAL",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "blocked",
        "condition": "execution receipt always returns to evidence reviewer",
        "destinations": [
          "QA-110"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-100.md",
          "section": "Required result and routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "FAILED"
        ],
        "branch_id": "failed",
        "condition": "execution receipt always returns to evidence reviewer",
        "destinations": [
          "QA-110"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-100.md",
          "section": "Required result and routing"
        },
        "state": "FAILED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "NOT_EXECUTED"
        ],
        "branch_id": "not_executed",
        "condition": "execution receipt always returns to evidence reviewer",
        "destinations": [
          "QA-110"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-100.md",
          "section": "Required result and routing"
        },
        "state": "NOT_EXECUTED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [],
        "branch_id": "shared_source_authority_terminal",
        "condition": "true source, authority, identity, or owner stop with no runnable selected receiver; preserve evidence and return without a handoff",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-100.md",
          "section": "Terminal operator return and receiver compatibility"
        },
        "state": null,
        "terminal_for_invocation": true
      }
    ],
    "QA-110": [
      {
        "applicable_states": [
          "ACCEPT"
        ],
        "branch_id": "accept",
        "condition": "the complete approved QA run requires final reporting, including a completed failing run; the union of selected collections is reconciled to every required Plan step and requirement, not merely a completed subset",
        "destinations": [
          "QA-120"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-110.md",
          "section": "Required result and routing"
        },
        "state": "ACCEPT",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BOUNDED_RERUN_REQUIRED"
        ],
        "branch_id": "rerun_task_authoring",
        "condition": "a new selected attempt-2 execution task still must be authored",
        "destinations": [
          "QA-90"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-110.md",
          "section": "Required result and routing"
        },
        "state": "BOUNDED_RERUN_REQUIRED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BOUNDED_RERUN_REQUIRED"
        ],
        "branch_id": "rerun_execution",
        "condition": "the authorized attempt-2 task is already complete and ready for execution",
        "destinations": [
          "QA-100"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-110.md",
          "section": "Required result and routing"
        },
        "state": "BOUNDED_RERUN_REQUIRED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "ESCALATION_REQUIRED"
        ],
        "branch_id": "escalation_required",
        "condition": "material QA evidence finding requires the native QA escalation report",
        "destinations": [
          "ESC-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-110.md",
          "section": "Required result and routing"
        },
        "state": "ESCALATION_REQUIRED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "INCOMPLETE"
        ],
        "branch_id": "incomplete_execution_evidence",
        "condition": "the exact missing evidence is lawfully producible by bounded QA execution",
        "destinations": [
          "QA-100"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-110.md",
          "section": "Required result and routing"
        },
        "state": "INCOMPLETE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "INCOMPLETE"
        ],
        "branch_id": "incomplete_named_owner",
        "condition": "another exact evidence owner is identified; preserve QA-110 resume phase",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-110.md",
          "section": "Required result and routing"
        },
        "state": "INCOMPLETE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "INCOMPLETE"
        ],
        "branch_id": "incomplete_terminal",
        "condition": "the evidence owner or required authority cannot be resolved into a runnable receiver",
        "destinations": [
          "ACTUAL_OWNER_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-110.md",
          "section": "Required result and routing"
        },
        "state": "INCOMPLETE",
        "terminal_for_invocation": true
      }
    ],
    "QA-120": [
      {
        "applicable_states": [
          "PASS"
        ],
        "branch_id": "pass_epic",
        "change_class": "EPIC",
        "condition": "PASS with verified existing EPIC class, complete QA Report/RCA and the matching continuing-Isis closure intake",
        "destinations": [
          "CL-E-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "required_artifacts": [
          "QA_REPORT",
          "QA_RCA"
        ],
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-120.md",
          "section": "Required result and routing"
        },
        "state": "PASS",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "PASS"
        ],
        "branch_id": "pass_crd",
        "change_class": "CRD",
        "condition": "PASS with verified existing CRD class, complete QA Report/RCA and the matching continuing-Isis closure intake",
        "destinations": [
          "CL-C-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "required_artifacts": [
          "QA_REPORT",
          "QA_RCA"
        ],
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-120.md",
          "section": "Required result and routing"
        },
        "state": "PASS",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "FAIL"
        ],
        "branch_id": "fail",
        "condition": "final QA Report/RCA demonstrates a material failure requiring escalation",
        "destinations": [
          "ESC-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-120.md",
          "section": "Required result and routing"
        },
        "state": "FAIL",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "INTERIM"
        ],
        "branch_id": "interim_evidence_review",
        "condition": "remaining evidence requires Kronos classification",
        "destinations": [
          "QA-110"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-120.md",
          "section": "Required result and routing"
        },
        "state": "INTERIM",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "INTERIM"
        ],
        "branch_id": "interim_task_authoring",
        "condition": "an unissued selected instruction or authorized retry task must be authored",
        "destinations": [
          "QA-90"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-120.md",
          "section": "Required result and routing"
        },
        "state": "INTERIM",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [],
        "branch_id": "shared_source_authority_terminal",
        "condition": "true source, authority, identity, or owner stop with no runnable selected receiver; preserve evidence and return without a handoff",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-120.md",
          "section": "Terminal operator return and receiver compatibility"
        },
        "state": null,
        "terminal_for_invocation": true
      }
    ],
    "QA-20": [
      {
        "applicable_states": [
          "GUIDE_READY"
        ],
        "branch_id": "guide_ready",
        "condition": "complete live QA Guide is ready for whole-change QA Audit/Plan",
        "destinations": [
          "QA-50"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-20.md",
          "section": "Required result and routing"
        },
        "state": "GUIDE_READY",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "blocked",
        "condition": "material readiness invalidation or recoverable QA-10 evidence gap requires same-Isis reassessment",
        "destinations": [
          "QA-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-20.md",
          "section": "Required result and routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [],
        "branch_id": "shared_source_authority_terminal",
        "condition": "true source, authority, identity, or owner stop with no runnable selected receiver; preserve evidence and return without a handoff",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-20.md",
          "section": "Terminal operator return and receiver compatibility"
        },
        "state": null,
        "terminal_for_invocation": true
      }
    ],
    "QA-50": [
      {
        "applicable_states": [],
        "branch_id": "existing_approval_reuse",
        "condition": "a subsequent still-valid actual QA-70 approval of this exact Plan already exists and its complete native task-creation intake is available; preserve Isis decision and same Kronos lineage without new Plan/review/task execution",
        "destinations": [
          "QA-90"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "CONDITIONAL_RECOVERY",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-50.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "PLAN_PENDING"
        ],
        "branch_id": "plan_pending",
        "condition": "both QA Audit and QA Plan are complete and separately read back",
        "destinations": [
          "QA-70"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-50.md",
          "section": "Required result and routing"
        },
        "state": "PLAN_PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "AUDIT_COMPLETE"
        ],
        "branch_id": "audit_complete",
        "condition": "QA Audit is complete but a recoverable interruption prevented Plan completion",
        "destinations": [
          "QA-60"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-50.md",
          "section": "Required result and routing"
        },
        "state": "AUDIT_COMPLETE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "blocked_initial_denial",
        "condition": "an initial pending QA Plan was denied by QA-70 with exact redlines",
        "destinations": [
          "QA-80"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-50.md",
          "section": "Required result and routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "blocked_plan_recovery",
        "condition": "Audit is complete and the planning gap is recoverable",
        "destinations": [
          "QA-60"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-50.md",
          "section": "Required result and routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "blocked_complete_pending_plan",
        "condition": "the pending QA Plan is complete and ready for review",
        "destinations": [
          "QA-70"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-50.md",
          "section": "Required result and routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [],
        "branch_id": "qa50_terminal",
        "condition": "true source or authority stop has no runnable receiver",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-50.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": true
      }
    ],
    "QA-60": [
      {
        "applicable_states": [],
        "branch_id": "existing_approval_reuse",
        "condition": "a subsequent still-valid actual QA-70 approval of this exact Plan already exists and its complete native task-creation intake is available; preserve Isis decision and same Kronos lineage without new Plan/review/task execution",
        "destinations": [
          "QA-90"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "CONDITIONAL_RECOVERY",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-60.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [],
        "branch_id": "existing_revision_reuse",
        "condition": "actual initial QA-70 denial or bounded redline review of this exact Plan already exists with complete review/Audit/upstream intake and same Kronos author lineage",
        "destinations": [
          "QA-80"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "CONDITIONAL_RECOVERY",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-60.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "PLAN_PENDING"
        ],
        "branch_id": "plan_pending",
        "condition": "complete QA Plan returns to continuing Isis review",
        "destinations": [
          "QA-70"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-60.md",
          "section": "Required result and routing"
        },
        "state": "PLAN_PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "BLOCKED"
        ],
        "branch_id": "blocked",
        "condition": "unique source failure, approved-base rewrite request, unrecoverable authority conflict, or missing decisive Audit",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-60.md",
          "section": "Required result and routing"
        },
        "state": "BLOCKED",
        "terminal_for_invocation": true
      }
    ],
    "QA-70": [
      {
        "applicable_states": [
          "APPROVE"
        ],
        "branch_id": "initial_approve",
        "condition": "REVIEW_MODE=INITIAL; approve the pending QA Plan; no addendum",
        "destinations": [
          "QA-90"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-70.md",
          "section": "Required result and routing"
        },
        "state": "APPROVE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "DENY"
        ],
        "branch_id": "initial_deny",
        "condition": "REVIEW_MODE=INITIAL; exact redlines return to the same Kronos author; no addendum",
        "destinations": [
          "QA-80"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-70.md",
          "section": "Required result and routing"
        },
        "state": "DENY",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "APPROVE"
        ],
        "branch_id": "delta_approve",
        "condition": "REVIEW_MODE=DELTA; exactly one addendum and conditional post-drain native continuation",
        "destinations": [
          "NATHAN_MANUAL_PF10_DRAIN"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-70.md",
          "section": "Required result and routing"
        },
        "state": "APPROVE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "DENY"
        ],
        "branch_id": "delta_deny",
        "condition": "REVIEW_MODE=DELTA; return denial to the exact originating proposed-delta owner; no addendum",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-70.md",
          "section": "Required result and routing"
        },
        "state": "DENY",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [],
        "branch_id": "qa70_terminal",
        "condition": "source, authority, mode, or continuation identity is unresolved",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-70.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": true
      }
    ],
    "QA-80": [
      {
        "applicable_states": [
          "PLAN_PENDING_REVISED"
        ],
        "branch_id": "plan_pending_revised",
        "condition": "complete corrected pending preapproval QA Plan returns to the same Isis reviewer",
        "destinations": [
          "QA-70"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-80.md",
          "section": "Required result and routing"
        },
        "state": "PLAN_PENDING_REVISED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "WRONG_ROUTE_APPROVED_BASE"
        ],
        "branch_id": "existing_delta_review",
        "condition": "approved-base rewrite refused but a complete existing explicit bounded delta, actual author, approval lineage and current PF10/addenda satisfy QA-70 APPROVED_QA_PLAN_DELTA_REVIEW intake; carry the existing delta unchanged",
        "destinations": [
          "QA-70"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-80.md",
          "section": "Required result and routing"
        },
        "state": "WRONG_ROUTE_APPROVED_BASE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "WRONG_ROUTE_APPROVED_BASE"
        ],
        "branch_id": "wrong_route_terminal",
        "condition": "approved-base rewrite refused and a complete lawful bounded-delta review intake is absent; identify the actual proposal owner without inventing a delta",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-80.md",
          "section": "Required result and routing"
        },
        "state": "WRONG_ROUTE_APPROVED_BASE",
        "terminal_for_invocation": true
      }
    ],
    "QA-90": [
      {
        "applicable_states": [
          "TASK_READY"
        ],
        "branch_id": "task_ready",
        "condition": "bounded QA execution task is complete",
        "destinations": [
          "QA-100"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-90.md",
          "section": "Required result and routing"
        },
        "state": "TASK_READY",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "ESCALATION_REQUIRED"
        ],
        "branch_id": "escalation_required",
        "condition": "material pre-execution defect; create the native QA escalation report",
        "destinations": [
          "ESC-10"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-90.md",
          "section": "Required result and routing"
        },
        "state": "ESCALATION_REQUIRED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "NOT_EXECUTED"
        ],
        "branch_id": "not_executed",
        "condition": "preserve non-execution evidence for the QA evidence reviewer",
        "destinations": [
          "QA-110"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-90.md",
          "section": "Required result and routing"
        },
        "state": "NOT_EXECUTED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [],
        "branch_id": "shared_source_authority_terminal",
        "condition": "true source, authority, identity, or owner stop with no runnable selected receiver; preserve evidence and return without a handoff",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/QA-90.md",
          "section": "Terminal operator return and receiver compatibility"
        },
        "state": null,
        "terminal_for_invocation": true
      }
    ],
    "RS-10": [
      {
        "applicable_states": [
          "RESCOPE_PROPOSAL_PENDING_REVIEW"
        ],
        "branch_id": "rescope_proposal_pending_review",
        "condition": "a real bounded delta has a complete proposal and exact actual native-stage lineage; pre-Proceed planning does not require future Proceed, PR or execution-return-phase fields",
        "destinations": [
          "RS-20"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/RS-10.md",
          "section": "Required result and routing"
        },
        "state": "RESCOPE_PROPOSAL_PENDING_REVIEW",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [],
        "branch_id": "in_scope_native_return",
        "condition": "observed ordinary in-scope correction needs no rescope proposal or formal RS-20 decision; exact selected existing repair owner/session and complete native intake are resolved under unchanged authority; no PR-50, merge, PF10 drain or manual-gate bypass",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_OWNER_RETURN",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/RS-10.md",
          "section": "Required result and routing"
        },
        "state": null,
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [],
        "branch_id": "shared_source_authority_terminal",
        "condition": "true source, authority, identity, or owner stop with no runnable selected receiver; preserve evidence and return without a handoff",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/RS-10.md",
          "section": "Terminal operator return and receiver compatibility"
        },
        "state": null,
        "terminal_for_invocation": true
      }
    ],
    "RS-20": [
      {
        "applicable_states": [
          "APPROVE"
        ],
        "branch_id": "approve",
        "condition": "exactly one addendum; conditional post-drain receiver selected only by PR_RETURN_PHASE",
        "destinations": [
          "NATHAN_MANUAL_PF10_DRAIN"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [
          "RS-20 -> Nathan manual PF10 drain",
          "PR-30_PREPUBLICATION -> PR-30 fresh verification",
          "PR-30_POSTPUBLICATION or PR-35 -> RS-40 fresh verification",
          "non-PR -> exact original native stage fresh verification"
        ],
        "source_evidence": {
          "path": "candidate/prompts/d/RS-20.md",
          "section": "Required result and routing"
        },
        "state": "APPROVE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "REJECT"
        ],
        "branch_id": "reject_pr30",
        "condition": "recorded origin/phase is PR-30; unchanged authority; no addendum",
        "destinations": [
          "PR-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/RS-20.md",
          "section": "Required result and routing"
        },
        "state": "REJECT",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "REJECT"
        ],
        "branch_id": "reject_pr35",
        "condition": "recorded origin/phase is PR-35; unchanged authority; no addendum",
        "destinations": [
          "PR-35"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/RS-20.md",
          "section": "Required result and routing"
        },
        "state": "REJECT",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "REJECT"
        ],
        "branch_id": "reject_native",
        "condition": "recorded origin is a non-PR native stage; unchanged authority; no addendum",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/RS-20.md",
          "section": "Required result and routing"
        },
        "state": "REJECT",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "IN_SCOPE_REPAIR"
        ],
        "branch_id": "in_scope_pr30",
        "condition": "existing repair owner/phase is PR-30 under the original Proceed; no addendum",
        "destinations": [
          "PR-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/RS-20.md",
          "section": "Required result and routing"
        },
        "state": "IN_SCOPE_REPAIR",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "IN_SCOPE_REPAIR"
        ],
        "branch_id": "in_scope_pr35",
        "condition": "existing repair owner/phase is PR-35 under the original Proceed; no addendum",
        "destinations": [
          "PR-35"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/RS-20.md",
          "section": "Required result and routing"
        },
        "state": "IN_SCOPE_REPAIR",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "IN_SCOPE_REPAIR"
        ],
        "branch_id": "in_scope_native",
        "condition": "existing repair owner is a non-PR native stage under unchanged authority; no addendum",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/RS-20.md",
          "section": "Required result and routing"
        },
        "state": "IN_SCOPE_REPAIR",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "REVISION_REQUIRED"
        ],
        "branch_id": "revision_required",
        "condition": "same request/proposal author; no addendum",
        "destinations": [
          "RS-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/RS-20.md",
          "section": "Required result and routing"
        },
        "state": "REVISION_REQUIRED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "SPECIFICATION_CHANGE_REQUIRED"
        ],
        "branch_id": "specification_change_required",
        "condition": "native Product Owner Specification-delta decision; no RS-20 addendum",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/RS-20.md",
          "section": "Required result and routing"
        },
        "state": "SPECIFICATION_CHANGE_REQUIRED",
        "terminal_for_invocation": true
      }
    ],
    "RS-30": [
      {
        "applicable_states": [
          "RESCOPE_PROPOSAL_PENDING_REVIEW"
        ],
        "branch_id": "ia_revision_return",
        "condition": "actual correction authority is RS-20 REVISION_REQUIRED; preserve RESCOPE_REQUEST vs RESCOPE_PROPOSAL type and return to the same IA decision owner",
        "destinations": [
          "RS-20"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/RS-30.md",
          "section": "Required result and routing"
        },
        "state": "RESCOPE_PROPOSAL_PENDING_REVIEW",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "RESCOPE_PROPOSAL_PENDING_REVIEW"
        ],
        "branch_id": "product_owner_revision_return",
        "condition": "actual correction authority is Nathan and no exact native decision route is already supplied; preserve his decision ownership and emit no continuation block",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/RS-30.md",
          "section": "Required result and routing"
        },
        "state": "RESCOPE_PROPOSAL_PENDING_REVIEW",
        "terminal_for_invocation": true
      },
      {
        "applicable_states": [
          "RESCOPE_PROPOSAL_PENDING_REVIEW"
        ],
        "branch_id": "product_owner_explicit_native_return",
        "condition": "Nathan already supplied one exact selected native decision route with complete intake; preserve actual owner, same artifact type and manual gates; never invent IA approval, route PR-50 or bypass Alpha, merge or PF10 controls",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/RS-30.md",
          "section": "Required result and routing"
        },
        "state": "RESCOPE_PROPOSAL_PENDING_REVIEW",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [],
        "branch_id": "revision_source_terminal",
        "condition": "source, exact correction authority, target or owner identity is missing; preserve valid artifact and return the exact gap",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "TERMINAL_EXCEPTION",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/RS-30.md",
          "section": "Required inputs"
        },
        "state": null,
        "terminal_for_invocation": true
      }
    ],
    "RS-40": [
      {
        "applicable_states": [
          "SOURCE_RESOLUTION_ERROR"
        ],
        "branch_id": "source_resolution_error",
        "condition": "unique current controlled PF10 Markdown unresolved; make no drain inference",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/RS-40.md",
          "section": "Required result and routing"
        },
        "state": "SOURCE_RESOLUTION_ERROR",
        "terminal_for_invocation": true
      },
      {
        "applicable_states": [
          "MANUAL_DRAIN_REQUIRED"
        ],
        "branch_id": "manual_drain_required",
        "condition": "current PF10 read; exact anchor absent",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/RS-40.md",
          "section": "Required result and routing"
        },
        "state": "MANUAL_DRAIN_REQUIRED",
        "terminal_for_invocation": true
      },
      {
        "applicable_states": [
          "MANUAL_DRAIN_MISMATCH"
        ],
        "branch_id": "manual_drain_mismatch",
        "condition": "related content differs in decision/base/normalized delta or a later conflicting overlay exists",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/RS-40.md",
          "section": "Required result and routing"
        },
        "state": "MANUAL_DRAIN_MISMATCH",
        "terminal_for_invocation": true
      },
      {
        "applicable_states": [
          "DRAIN_VERIFIED"
        ],
        "branch_id": "drain_verified",
        "condition": "exact anchor and normalized delta match with no later conflicting overlay; internal gate only; immediately resume recorded eligible phase",
        "destinations": [],
        "next_prompt_handoff_count": null,
        "notes": null,
        "public_result": false,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/RS-40.md",
          "section": "Required result and routing"
        },
        "state": "DRAIN_VERIFIED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "PR_CANDIDATE_PUBLISHED"
        ],
        "branch_id": "pr_candidate_published",
        "condition": "recorded PR-30_POSTPUBLICATION phase result",
        "destinations": [
          "PR-35"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/RS-40.md",
          "section": "Required result and routing"
        },
        "state": "PR_CANDIDATE_PUBLISHED",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "MERGE_PENDING"
        ],
        "branch_id": "merge_pending",
        "condition": "recorded PR-35 phase result; historical pre-merge evidence",
        "destinations": [
          "NATHAN_MANUAL_MERGE_ASSERTION"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/RS-40.md",
          "section": "Required result and routing"
        },
        "state": "MERGE_PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "RESCOPE_PENDING"
        ],
        "branch_id": "rescope_pending",
        "condition": "new formal RESCOPE_REQUEST preserves same vehicle",
        "destinations": [
          "RS-20"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/RS-40.md",
          "section": "Required result and routing"
        },
        "state": "RESCOPE_PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "RECOVERY_PENDING"
        ],
        "branch_id": "recovery_pr30",
        "condition": "recorded resumed phase is PR-30_POSTPUBLICATION; same session/vehicle re-entry",
        "destinations": [
          "PR-30"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/RS-40.md",
          "section": "Required result and routing"
        },
        "state": "RECOVERY_PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "RECOVERY_PENDING"
        ],
        "branch_id": "recovery_pr35",
        "condition": "recorded resumed phase is PR-35; same session/vehicle re-entry",
        "destinations": [
          "PR-35"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/RS-40.md",
          "section": "Required result and routing"
        },
        "state": "RECOVERY_PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "REMOTE_EVIDENCE_PENDING"
        ],
        "branch_id": "remote_evidence_pending",
        "condition": "PR-35 only; durable checkpoint",
        "destinations": [
          "PR-35"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/RS-40.md",
          "section": "Required result and routing"
        },
        "state": "REMOTE_EVIDENCE_PENDING",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "PRODUCT_OWNER_DECISION_REQUIRED"
        ],
        "branch_id": "product_owner_decision_required",
        "condition": "genuine Product Owner decision or unrecoverable authority conflict",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/RS-40.md",
          "section": "Required result and routing"
        },
        "state": "PRODUCT_OWNER_DECISION_REQUIRED",
        "terminal_for_invocation": true
      }
    ],
    "UTIL-10": [
      {
        "applicable_states": [
          "COMPLETE"
        ],
        "branch_id": "complete",
        "condition": "return the revised artifact and report to the exact original decision/review owner",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/UTIL-10.md",
          "section": "Required result and routing"
        },
        "state": "COMPLETE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "INCOMPLETE"
        ],
        "branch_id": "incomplete_native_owner",
        "condition": "return the checkpoint to the exact redline/artifact owner when a selected native receiver resolves",
        "destinations": [
          "ORIGINAL_NATIVE_STAGE"
        ],
        "next_prompt_handoff_count": 1,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/UTIL-10.md",
          "section": "Required result and routing"
        },
        "state": "INCOMPLETE",
        "terminal_for_invocation": false
      },
      {
        "applicable_states": [
          "INCOMPLETE"
        ],
        "branch_id": "incomplete_terminal",
        "condition": "no selected native receiver can be resolved; do not invent one",
        "destinations": [
          "NATHAN_TERMINAL_RETURN"
        ],
        "next_prompt_handoff_count": 0,
        "notes": null,
        "public_result": true,
        "route_kind": "NATIVE_RESULT",
        "route_steps": [],
        "source_evidence": {
          "path": "candidate/prompts/d/UTIL-10.md",
          "section": "Required result and routing"
        },
        "state": "INCOMPLETE",
        "terminal_for_invocation": true
      }
    ]
  },
  "state_vocabularies": {
    "AUTHORING_CONTEXT": [
      "INITIAL_OR_PREAPPROVAL_AUTHORING",
      "APPROVED_BASE_WITH_OVERLAYS"
    ],
    "PF10_POST_DRAIN_VERIFICATION": [
      "SOURCE_RESOLUTION_ERROR",
      "MANUAL_DRAIN_REQUIRED",
      "MANUAL_DRAIN_MISMATCH",
      "DRAIN_VERIFIED"
    ],
    "PR-30_RESULT": [
      "PR_CANDIDATE_PUBLISHED",
      "RESCOPE_PENDING",
      "RECOVERY_PENDING",
      "PRODUCT_OWNER_DECISION_REQUIRED"
    ],
    "PR-35_RESULT": [
      "MERGE_PENDING",
      "RESCOPE_PENDING",
      "RECOVERY_PENDING",
      "REMOTE_EVIDENCE_PENDING",
      "PRODUCT_OWNER_DECISION_REQUIRED"
    ],
    "PR_RETURN_PHASE": [
      {
        "open_pr_required": false,
        "post_drain_receiver": "PR-30",
        "resumed_phase": "PR-30",
        "rs40_eligible": false,
        "value": "PR-30_PREPUBLICATION"
      },
      {
        "open_pr_required": true,
        "post_drain_receiver": "RS-40",
        "resumed_phase": "PR-30",
        "rs40_eligible": true,
        "value": "PR-30_POSTPUBLICATION"
      },
      {
        "open_pr_required": true,
        "post_drain_receiver": "RS-40",
        "resumed_phase": "PR-35",
        "rs40_eligible": true,
        "value": "PR-35"
      }
    ],
    "RS-20_DECISION": [
      "APPROVE",
      "REJECT",
      "REVISION_REQUIRED",
      "SPECIFICATION_CHANGE_REQUIRED",
      "IN_SCOPE_REPAIR"
    ]
  },
  "status": "FROZEN_FOR_CANDIDATE_AUTHORING",
  "terminal_contract": {
    "invocation_terminal_recoverable": [
      "SOURCE_RESOLUTION_ERROR",
      "MANUAL_DRAIN_REQUIRED",
      "MANUAL_DRAIN_MISMATCH",
      "CURRENT EVIDENCE PENDING IN A NON-PR35 BRANCH WHEN NO RUNNABLE RECEIVER EXISTS"
    ],
    "rule": "state completion/stop and return to Nathan; no continuation prompt",
    "workflow_terminal": [
      "PR_ABORTED_ESCALATED",
      "terminal closure/completion native results",
      "SPECIFICATION_CHANGE_REQUIRED return to Nathan",
      "PRODUCT_OWNER_DECISION_REQUIRED return to Nathan"
    ]
  },
  "unresolved_graph_predicates": []
}
```
