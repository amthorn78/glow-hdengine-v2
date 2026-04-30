# OPS-02 Target Disposition

Target classification: CLI_LOCAL_VENDOR_SMOKE

Contract alignment:

- governing_plan_source: audit/ops/hde-epic030/r3 Remediation Plan 01 HDE-EPIC030.md
- governing_plan_rule: Target system/service section explicitly allows CLI_LOCAL_VENDOR_SMOKE and states hosted-service PF07 facts are not required for this classification
- supporting_pf10_source: docs/pfcanon/PF10-HDE-Build-Notes-v10.6.9.md section 2.24 target fact posture
- supporting_pf10_rule: target for this smoke is HD Engine CLI with --source vendor, and HDE_BASE_URL is not required unless command target changes to HTTP service

Disposition rationale:

- command target: hdctl showcompat
- source: vendor
- execution context: PO-controlled CLI/repo environment
- hosted HD Engine service target: not required for this command
- PF07 hosted-service binding required: no
- reason: the command is a CLI vendor-source smoke, not a hosted HD Engine HTTP service smoke
- PR-02 runtime binding proof: see audit/ops/hde-epic030/ops-02/pr02_runtime_binding.md
- env binding proof: see audit/ops/hde-epic030/ops-02/redacted_env_presence.json
- command proof: see audit/ops/hde-epic030/ops-02/vendor_command.txt

Applicability statement:

PF07 is not being used to invent a hosted target. This smoke targets the local hdctl CLI with vendor source. Hosted-service PF07 facts are not applicable unless the command is changed to call an HD Engine HTTP service.

Validation against classification rules:

- executed command is hdctl showcompat: PASS
- command includes --source vendor: PASS
- command line invokes hosted HD Engine URL directly: NO
- runtime proof is PO-controlled CLI execution from repo/CLI environment: PASS
- vendor/API binding handled by env keys instead of hosted HD Engine service URL: PASS