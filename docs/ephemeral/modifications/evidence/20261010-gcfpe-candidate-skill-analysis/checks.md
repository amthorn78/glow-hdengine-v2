# Checks and ANALYZE dry run

All commands ran from extracted supplied bytes with bytecode disabled and closed product-execution rails. Fixture subprocesses used isolated temporary repositories; no product runtime was exercised. Exact source digests are in source-identities.md.

## Actual outcomes

| Check | Exit | Observed result / limit |
|---|---:|---|
| Primary core comparison / propagation list | 0 | One supplied embedding equal; core 1.0.3 / 4d8bb9bf1c9c85aeba8529995ee97b496d7938571d4b362f49c42aa9aa27d409. No writes. |
| change-flow package static | 0 | Supplied September contract/source policy passes. |
| R1 successor fixtures | 0 | 32/32: 13 positive, 19 negative. |
| September overlay validator | 0 | 55 nodes / 229 edges; **zero bodies; ALL_BODY_LEVEL_CHECKS not evaluated**. |
| September fixture runner | 0 | 236/236; 37 section-13 + 38 variants; zero live QA/timing/source mutation cases. |
| Full supplied Flowmaster suite | 1 | Five missing-dependency errors; no suite pass. |
| Four-target Flowmaster suite | 1 | Individual targets pass, same five unscoped dependency errors. |
| PR-development structural check | 0 | Structural contract PASS; not semantic current-candidate proof. |
| Attribution fixtures | 0 | suite_ok=true, 12/12. |
| Attribution collector adversarial | 0 | suite_ok=true, 19/19. |
| Attribution artifact adversarial | 0 | suite_ok=true, 77/77: 3 valid, 2 blocked, 72 reject expectations. |
| closure.py | 0 | 55 selected + 55 candidate calls; full output linked separately. |

The full-suite missing sources are session-relay-flowmaster, tw-flowmaster, session-branch-flowmaster and governance-audit; the five dispatch errors are one relay, one TW and three audit-file absences. glow-graph-contract, a separate missing package, owns candidate graph build/derivation. No missing skill was mocked or an old installed copy substituted. Nested repeated fixture totals are not added as new coverage.

## Exact command receipts

The Flowmaster receipt below is the worker's concise record of observed tool results, **not retained verbatim stdout**. Its two exploratory in-memory harnesses do not have a replayable committed command; treat them as corroborating source observations, not executable required gates. Primary shipped command lines are exact.

```json
{
  "receipt_type": "analysis_test_summary_from_observed_tool_results",
  "raw_stdout_retained": false,
  "notice": "This is a concise receipt of previously observed test results, not a replay or verbatim stdout log. No additional tests were run when writing it.",
  "source_root": "/workspace/scratch/fa82d6934864/skill-review-inputs",
  "repository_base": "1ea6a262032c3c4de19c38c549d737d72b03ec2f",
  "cwd": "/workspace/scratch/fa82d6934864/skill-test-work/suite",
  "environment": {
    "PYTHONDONTWRITEBYTECODE": "1",
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
    "TMPDIR": "Within /workspace/scratch/fa82d6934864/skill-test-work; exact original subdirectory spelling not retained in summary"
  },
  "tests": [
    {
      "name": "raw_core_comparison",
      "command": "python -B /workspace/scratch/fa82d6934864/skill-review-inputs/flowmaster-propagate/scripts/propagate_core.py --skills-root /workspace/scratch/fa82d6934864/skill-review-inputs --list",
      "exit_code": 0,
      "target_count": 1,
      "target": "change-flow",
      "primary_revision": "1.0.3",
      "target_revision": "1.0.3",
      "inclusive_core_sha256": "4d8bb9bf1c9c85aeba8529995ee97b496d7938571d4b362f49c42aa9aa27d409",
      "in_sync": true
    },
    {
      "name": "change_flow_package_static",
      "command": "python -B /workspace/scratch/fa82d6934864/skill-review-inputs/change-flow/scripts/validate_gcfpe_20260914.py",
      "exit_code": 0,
      "observed_message": "PASS: change-flow GCFPE-20260914.1 contract and Markdown-only source policy"
    },
    {
      "name": "change_flow_R1_successor_fixtures",
      "command": "python -B /workspace/scratch/fa82d6934864/skill-review-inputs/flowmaster-validate/scripts/run_change_flow_fixtures.py",
      "exit_code": 0,
      "passed": 32,
      "failed": 0,
      "positive": 13,
      "negative": 19,
      "oracle": "20260923"
    },
    {
      "name": "selected_overlay_validator",
      "command": "python -B /workspace/scratch/fa82d6934864/skill-review-inputs/flowmaster-validate/scripts/validate_gcfpe_20260914.py /workspace/scratch/fa82d6934864/skill-review-inputs/change-flow --contract /workspace/scratch/fa82d6934864/skill-review-inputs/change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json",
      "exit_code": 0,
      "errors": [],
      "profile": "091426.1",
      "nodes": 55,
      "edges": 229,
      "prompt_body_count": 0,
      "validated_prompt_ids": [],
      "not_evaluated": [
        "ALL_BODY_LEVEL_CHECKS"
      ]
    },
    {
      "name": "selected_overlay_fixtures",
      "command": "python -B /workspace/scratch/fa82d6934864/skill-review-inputs/flowmaster-validate/scripts/run_gcfpe_20260914_fixtures.py /workspace/scratch/fa82d6934864/skill-review-inputs/change-flow --contract /workspace/scratch/fa82d6934864/skill-review-inputs/change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json",
      "exit_code": 0,
      "passed": 236,
      "failed": 0,
      "section_13_fixtures_passed": 37,
      "section_13_variants_passed": 38,
      "qa_closure_source_cases": 0,
      "artifact_timing_cases": 0,
      "actual_source_mutations": 0,
      "profile_errors": []
    },
    {
      "name": "supplied_suite_strict",
      "command": "python -B /workspace/scratch/fa82d6934864/skill-review-inputs/flowmaster-validate/scripts/validate_flowmaster.py --skills-root /workspace/scratch/fa82d6934864/skill-review-inputs --strict-warnings",
      "exit_code": 1,
      "suite_status": "FAIL",
      "primary_core_prerequisite": "PASS",
      "self_identity_errors": 0,
      "change_flow_rows_passed": 46,
      "change_flow_rows_expected": 46,
      "change_flow_core_rows": 26,
      "change_flow_material_rows": 20,
      "individual_pass": [
        "flowmaster-primary",
        "change-flow",
        "flowmaster-validate"
      ],
      "missing_expected_skills": [
        "tw-flowmaster",
        "session-branch-flowmaster",
        "session-relay-flowmaster"
      ],
      "errors": [
        {
          "code": "FMV-GCF-DISPATCH-001",
          "missing_skill": "session-relay-flowmaster",
          "count": 1
        },
        {
          "code": "FMV-GCF-DISPATCH-001",
          "missing_skill": "tw-flowmaster",
          "count": 1
        },
        {
          "code": "FMV-GCF-DISPATCH-001",
          "missing_skill": "amthor-workspace-governance-audit",
          "count": 3
        }
      ],
      "warnings": 0,
      "advisories": 0,
      "blockers": 0,
      "interpretation": "Missing cross-suite dependencies in supplied archive set; not evidence these absent packages are defective."
    },
    {
      "name": "four_target_strict",
      "command": "python -B /workspace/scratch/fa82d6934864/skill-review-inputs/flowmaster-validate/scripts/validate_flowmaster.py --skills-root /workspace/scratch/fa82d6934864/skill-review-inputs --strict-warnings --target flowmaster-primary --target change-flow --target flowmaster-propagate --target flowmaster-validate",
      "exit_code": 1,
      "individual_pass_count": 4,
      "errors": "Same five FMV-GCF-DISPATCH-001 missing cross-suite dependency errors; dispatch validation is not scoped by --target."
    }
  ],
  "additional_in_memory_checks": [
    {
      "name": "all_file_syntax_and_inventory",
      "exit_code": 0,
      "files": 61,
      "bytes": 3770880,
      "checks": [
        "Python AST parse",
        "JSON parse",
        "SVG XML parse"
      ],
      "command_capture": "Exact one-shot harness text not retained; no standalone test file was written."
    },
    {
      "name": "D27_counterexamples",
      "harness_exit_code": 0,
      "command_capture": "Exact one-shot import harness text not retained; no standalone test file was written. These are observed comparator rejections, not D27 acceptance passes.",
      "cases": [
        {
          "fixture": "positive_specification_denial_same_thoth",
          "mutation": "Replace the two re-entry session identities with a recovered Thoth session",
          "observed_error": "FMV-GCF-SESSION-THOTH-001"
        },
        {
          "fixture": "positive_epic_happy_path",
          "mutation": "kronos_executes_qa=true",
          "observed_error": "FMV-GCF-ROLE-QA-001"
        },
        {
          "input": "current direct-handoff contract",
          "mutation": "transition_contract.receiving_role_and_exact_session=false",
          "observed_error": "HANDOFF_CONTRACT"
        }
      ]
    }
  ],
  "coverage_by_package": [
    {
      "package": "change-flow",
      "files": 22,
      "bytes": 1780288
    },
    {
      "package": "flowmaster-primary",
      "files": 2,
      "bytes": 23312
    },
    {
      "package": "flowmaster-propagate",
      "files": 3,
      "bytes": 19920
    },
    {
      "package": "flowmaster-validate",
      "files": 31,
      "bytes": 1915296
    },
    {
      "package": "typesafe-scoring",
      "files": 3,
      "bytes": 32064
    }
  ],
  "limits": [
    "All file bytes inventoried and structured sources parsed. Active relevant SKILL instructions and validator predicates inspected; historical references classified non-executable and integrity-checked through package validators, not exhaustively reviewed semantically.",
    "No native prompt bodies supplied to test runners; all body-level, live candidate, runtime, remote scoring and installed-suite acceptance remain unevaluated.",
    "No graph builder supplied; no current candidate graph/registry derivation attempted.",
    "No writes to repository, archives or extracted packages; no installs, network, propagation writes, external scoring or Notion changes.",
    "TypeSafe score.py and request-v6.json inspected only; no remote call or measured score exists.",
    "The 32 and 236 fixture totals also appear nested in suite output; they must not be summed as distinct repeated coverage."
  ]
}
```

## Attribution evidence

Python 3.12.14 / Git 2.51.1. The following exact command metadata and returned suite summaries are retained. No prompt body or temporary attribution bundle is included.

### fixtures

```json
{
  "label": "fixtures",
  "argv": [
    "python3",
    "/workspace/scratch/fa82d6934864/skill-review-inputs/glow-merged-change-attribution-lock/scripts/run_fixture_tests.py"
  ],
  "environment": {
    "PYTHONDONTWRITEBYTECODE": "1",
    "TMPDIR": "/workspace/scratch/fa82d6934864/skill-test-work/attribution-checks/tmp",
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
    "GIT_CONFIG_NOSYSTEM": "1",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_SYSTEM": "/dev/null",
    "GIT_TERMINAL_PROMPT": "0",
    "GIT_CONFIG_COUNT": "1",
    "GIT_CONFIG_KEY_0": "core.hooksPath",
    "GIT_CONFIG_VALUE_0": "/dev/null"
  },
  "path": "inherited executable search path only",
  "cwd": "/workspace/scratch/fa82d6934864/skill-test-work/attribution-checks",
  "started_utc": "2026-10-10T20:26:54.882040+00:00",
  "duration_seconds": 12.129,
  "exit_code": 0
}
```

```text
{
  "fixtures": [
    {
      "fixture": "merge",
      "status": "PASS"
    },
    {
      "fixture": "squash",
      "status": "PASS"
    },
    {
      "fixture": "rebase",
      "status": "PASS"
    },
    {
      "fixture": "later_and_worktree",
      "status": "PASS"
    },
    {
      "fixture": "conflict",
      "status": "PASS"
    },
    {
      "fixture": "lineage_order",
      "status": "PASS"
    },
    {
      "fixture": "current_comparison_state",
      "status": "PASS"
    },
    {
      "fixture": "rebase_requires_range",
      "status": "PASS"
    },
    {
      "fixture": "interstage_classification",
      "status": "PASS"
    },
    {
      "fixture": "global_stop_precedence",
      "status": "PASS"
    },
    {
      "fixture": "repository_identity_fingerprint",
      "status": "PASS"
    },
    {
      "fixture": "artifact_validator",
      "status": "PASS"
    }
  ],
  "suite_ok": true
}
```

### collector-adversarial

```json
{
  "label": "collector-adversarial",
  "argv": [
    "python3",
    "/workspace/scratch/fa82d6934864/skill-review-inputs/glow-merged-change-attribution-lock/scripts/run_collector_adversarial_tests.py"
  ],
  "environment": {
    "PYTHONDONTWRITEBYTECODE": "1",
    "TMPDIR": "/workspace/scratch/fa82d6934864/skill-test-work/attribution-checks/tmp",
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
    "GIT_CONFIG_NOSYSTEM": "1",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_SYSTEM": "/dev/null",
    "GIT_TERMINAL_PROMPT": "0",
    "GIT_CONFIG_COUNT": "1",
    "GIT_CONFIG_KEY_0": "core.hooksPath",
    "GIT_CONFIG_VALUE_0": "/dev/null"
  },
  "path": "inherited executable search path only",
  "cwd": "/workspace/scratch/fa82d6934864/skill-test-work/attribution-checks",
  "started_utc": "2026-10-10T20:26:54.856682+00:00",
  "duration_seconds": 32.61,
  "exit_code": 0
}
```

```text
{
  "suite_ok": true,
  "tests": [
    {
      "status": "PASS",
      "test": "helper_traps"
    },
    {
      "status": "PASS",
      "test": "inherited_git_redirection"
    },
    {
      "status": "PASS",
      "test": "credential_redaction_and_port"
    },
    {
      "status": "PASS",
      "test": "local_and_file_identity_equivalence"
    },
    {
      "status": "PASS",
      "test": "repository_source_aba"
    },
    {
      "status": "PASS",
      "test": "invalid_comparison_mutation_precedence"
    },
    {
      "status": "PASS",
      "test": "declared_stop_precedence"
    },
    {
      "status": "PASS",
      "test": "positive_merge_full_binding"
    },
    {
      "status": "PASS",
      "test": "merge_wrong_direct_head"
    },
    {
      "status": "PASS",
      "test": "squash_extra_landing_commit"
    },
    {
      "status": "PASS",
      "test": "rebase_range_with_merge"
    },
    {
      "status": "PASS",
      "test": "symbolic_and_abbreviated_stage_inputs"
    },
    {
      "status": "PASS",
      "test": "missing_direct_head"
    },
    {
      "status": "PASS",
      "test": "uniform_object_width"
    },
    {
      "status": "PASS",
      "test": "interstage_separation"
    },
    {
      "status": "PASS",
      "test": "later_revert_historical_semantics"
    },
    {
      "status": "PASS",
      "test": "safe_and_stable_run_keys"
    },
    {
      "status": "PASS",
      "test": "run_binding_cutoff_and_collision"
    },
    {
      "status": "PASS",
      "test": "no_fetch_or_remote_operation"
    }
  ]
}
```

### artifact-adversarial

```json
{
  "label": "artifact-adversarial",
  "argv": [
    "python3",
    "/workspace/scratch/fa82d6934864/skill-review-inputs/glow-merged-change-attribution-lock/scripts/run_artifact_adversarial_tests.py"
  ],
  "environment": {
    "PYTHONDONTWRITEBYTECODE": "1",
    "TMPDIR": "/workspace/scratch/fa82d6934864/skill-test-work/attribution-checks/tmp",
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
    "GIT_CONFIG_NOSYSTEM": "1",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_SYSTEM": "/dev/null",
    "GIT_TERMINAL_PROMPT": "0",
    "GIT_CONFIG_COUNT": "1",
    "GIT_CONFIG_KEY_0": "core.hooksPath",
    "GIT_CONFIG_VALUE_0": "/dev/null"
  },
  "path": "inherited executable search path only",
  "cwd": "/workspace/scratch/fa82d6934864/skill-test-work/attribution-checks",
  "started_utc": "2026-10-10T20:26:54.828208+00:00",
  "duration_seconds": 15.15,
  "exit_code": 0
}
```

```text
{
  "case_count": 77,
  "pass_count": 77,
  "results": [
    {
      "actual_exit": 0,
      "actual_schema": "PASS",
      "case": "valid_control",
      "expected": "VALID",
      "status": "PASS"
    },
    {
      "actual_exit": 2,
      "actual_schema": "PASS",
      "case": "blocked_control_no_prefix",
      "expected": "BLOCKED",
      "status": "PASS"
    },
    {
      "actual_exit": 2,
      "actual_schema": "PASS",
      "case": "blocked_control_retained_prefix",
      "expected": "BLOCKED",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "schema_wrong_title",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "schema_duplicate_title",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "schema_duplicate_header",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "schema_section_order",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "schema_table_columns",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "schema_wrong_terminal",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "schema_crlf",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "schema_utf8_bom",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "schema_hollow_section",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "schema_wrong_interface_revision",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "schema_legacy_v2_interface",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "schema_wrong_producer_revision",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "schema_missing_validation_predicate",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "schema_invalid_utc_cutoff",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "path_basename_mismatch",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "path_symlink",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "path_root_escape",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "path_missing_transient_root",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "manifest_path_symlink",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "manifest_path_root_escape",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "identity_shorthand_repository",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "identity_credential_source",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "identity_manifest_source_mismatch",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "identity_source_binding_mismatch",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "identity_whitespace_source",
      "expected": "REJECT",
      "note": "rendered remote source contains whitespace",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "identity_repository_traversal",
      "expected": "REJECT",
      "note": "canonical repository ID contains a traversal segment",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "identity_remote_repository_with_local_source_kind",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "run_binding_wrong_digest",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "run_key_unsafe_characters",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "run_filename_not_derived",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 0,
      "actual_schema": "PASS",
      "case": "run_binding_excludes_comparison_ref",
      "expected": "VALID",
      "status": "PASS"
    },
    {
      "actual_exit": 0,
      "actual_schema": "PASS",
      "case": "run_key_derived_from_binding",
      "expected": "VALID",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "run_key_over_64_characters",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "manifest_content_tampered",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "manifest_header_hash_tampered",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "manifest_missing",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "manifest_non_object_json",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "manifest_wrong_interface",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "manifest_wrong_schema_version",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "manifest_wrong_run_binding",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "manifest_wrong_artifact_filename",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "manifest_wrong_attribution_scope",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "manifest_claims_current_effect",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "manifest_missing_repository_source_kind",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "manifest_missing_repository_source_redacted",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "manifest_missing_repository_source_binding_sha256",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "manifest_missing_access_mode",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "manifest_missing_git_object_format",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "manifest_final_state_not_stage_derived",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "manifest_later_state_wrong_boundary",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "manifest_worktree_state_snapshot_mismatch",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "snapshot_consistency_flag_false",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "snapshot_repository_after_changed",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "snapshot_source_after_changed",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "snapshot_binding_after_changed",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "lifecycle_durable",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "consumer_scope_expanded",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "retention_policy_permanent",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "deprecated_persistent_id_header",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "blocked_lifecycle_changed",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "stop_rendered_bold_blockquote",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "stop_hidden_html_comment",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "stop_invented_header_sentinel",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "row_prefix_fully_proven_stage_omitted",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "row_prefix_claim_beyond_conflict",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "row_prefix_nonprefix_change",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "row_prefix_delta_tampered",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "row_prefix_method_tampered",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "row_prefix_pointer_tampered",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "unproven_plain_leakage",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "unproven_rendered_markdown_leakage",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "final_state_false_narrative",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "later_divergence_false_narrative",
      "expected": "REJECT",
      "status": "PASS"
    },
    {
      "actual_exit": 1,
      "actual_schema": "FAIL",
      "case": "worktree_false_narrative",
      "expected": "REJECT",
      "status": "PASS"
    }
  ],
  "suite_ok": true
}
```

### pr-development-structural

```json
{
  "label": "pr-development-structural",
  "argv": [
    "python3",
    "/workspace/scratch/fa82d6934864/skill-review-inputs/glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py"
  ],
  "environment": {
    "PYTHONDONTWRITEBYTECODE": "1",
    "TMPDIR": "/workspace/scratch/fa82d6934864/skill-test-work/attribution-checks/tmp",
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
    "GIT_CONFIG_NOSYSTEM": "1",
    "GIT_CONFIG_GLOBAL": "/dev/null",
    "GIT_CONFIG_SYSTEM": "/dev/null",
    "GIT_TERMINAL_PROMPT": "0",
    "GIT_CONFIG_COUNT": "1",
    "GIT_CONFIG_KEY_0": "core.hooksPath",
    "GIT_CONFIG_VALUE_0": "/dev/null"
  },
  "path": "inherited executable search path only",
  "cwd": "/workspace/scratch/fa82d6934864/skill-test-work/attribution-checks",
  "started_utc": "2026-10-10T20:26:54.999775+00:00",
  "duration_seconds": 0.113,
  "exit_code": 0
}
```

```text
PASS: Glow HDE PR development skill structural contract
```

## Additional bounded attribution probes

These are synthetic altered-input observations L07/L08, not a failure of the collector on a normal run. The native skill independently forbids persistence; lifecycle prose acceptance only disproves the matrix's broader lexical promise. The inconsistent untracked-path probe requires altering and resealing manifest/body data. Probe directories were deleted; no transient attribution bundle is preserved.

```json
[
  {
    "case": "valid_control",
    "argv": [
      "python3",
      "/workspace/scratch/fa82d6934864/skill-review-inputs/glow-merged-change-attribution-lock/scripts/validate_attribution_artifact.py",
      "/workspace/scratch/fa82d6934864/skill-test-work/attribution-checks/tmp/bounded-contract-probe-khb0_dwn/MCA-fixture-run-Attribution.md",
      "--evidence-manifest",
      "/workspace/scratch/fa82d6934864/skill-test-work/attribution-checks/tmp/bounded-contract-probe-khb0_dwn/manifest.json",
      "--transient-root",
      "/workspace/scratch/fa82d6934864/skill-test-work/attribution-checks/tmp/bounded-contract-probe-khb0_dwn"
    ],
    "exit_code": 0,
    "validator": {
      "artifact_status": "VALIDATED",
      "eligible_as_validated_evidence": true,
      "errors": [],
      "interface_version": "GLOW-MERGED-CHANGE-ATTRIBUTION-082826.3",
      "schema_status": "PASS",
      "status": "PASS"
    },
    "stderr": ""
  },
  {
    "case": "contradictory_retention_prose",
    "argv": [
      "python3",
      "/workspace/scratch/fa82d6934864/skill-review-inputs/glow-merged-change-attribution-lock/scripts/validate_attribution_artifact.py",
      "/workspace/scratch/fa82d6934864/skill-test-work/attribution-checks/tmp/bounded-contract-probe-o0g_d31n/MCA-fixture-run-Attribution.md",
      "--evidence-manifest",
      "/workspace/scratch/fa82d6934864/skill-test-work/attribution-checks/tmp/bounded-contract-probe-o0g_d31n/manifest.json",
      "--transient-root",
      "/workspace/scratch/fa82d6934864/skill-test-work/attribution-checks/tmp/bounded-contract-probe-o0g_d31n"
    ],
    "exit_code": 0,
    "validator": {
      "artifact_status": "VALIDATED",
      "eligible_as_validated_evidence": true,
      "errors": [],
      "interface_version": "GLOW-MERGED-CHANGE-ATTRIBUTION-082826.3",
      "schema_status": "PASS",
      "status": "PASS"
    },
    "stderr": "",
    "contradiction": "Retain this attribution artifact permanently in the repository after review."
  },
  {
    "case": "untracked_paths_vs_hash",
    "argv": [
      "python3",
      "/workspace/scratch/fa82d6934864/skill-review-inputs/glow-merged-change-attribution-lock/scripts/validate_attribution_artifact.py",
      "/workspace/scratch/fa82d6934864/skill-test-work/attribution-checks/tmp/bounded-contract-probe-k1fwtdpm/MCA-fixture-run-Attribution.md",
      "--evidence-manifest",
      "/workspace/scratch/fa82d6934864/skill-test-work/attribution-checks/tmp/bounded-contract-probe-k1fwtdpm/manifest.json",
      "--transient-root",
      "/workspace/scratch/fa82d6934864/skill-test-work/attribution-checks/tmp/bounded-contract-probe-k1fwtdpm"
    ],
    "exit_code": 0,
    "validator": {
      "artifact_status": "VALIDATED",
      "eligible_as_validated_evidence": true,
      "errors": [],
      "interface_version": "GLOW-MERGED-CHANGE-ATTRIBUTION-082826.3",
      "schema_status": "PASS",
      "status": "PASS"
    },
    "stderr": "",
    "untracked_state": {
      "staged_delta_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "unstaged_delta_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "untracked_paths": [
        "ghost.txt"
      ],
      "untracked_paths_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "untracked_content_sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    }
  }
]
```

## Dry-run boundary

The ANALYZE normal path consists of native source resolution/readback, 110 closure queries, immutable input identity, source-based counterexample/refutation review, documentation and record validation. These were exercised before independent FULL review. Future release gates requiring the missing builder/current profile are explicitly unavailable; no claim that those passed. No implementation steps or runtime operations belong to this mode. Final record validator and git readback receipts follow in publication.md.
