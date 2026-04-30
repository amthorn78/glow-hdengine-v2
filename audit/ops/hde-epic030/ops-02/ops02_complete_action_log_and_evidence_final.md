# OPS-02 Complete Action Log and Evidence Output FINAL

## Artifact Map

Evidence root:

- audit/ops/hde-epic030/ops-02/

Required file set:

1. vendor_command.txt
2. sample_birth_inputs.json
3. redacted_env_presence.json
4. target_disposition.md
5. pr02_runtime_binding.md
6. request_summary.txt
7. result_summary.md
8. execution_classification.md
9. stdout.json
10. stderr.log
11. exit_code.txt
12. stdout_parse_validation.md
13. stdout.json.sha256
14. files_sha256.txt
15. ops02_complete_action_log_and_evidence_final.md

Final classification:

- PASS

## Preflight Proof

command proof:

- vendor_command.txt is concrete, no placeholders, and uses birth-only vendor command shape
- request_summary.txt states command source was OPS-01 and records lineage from OPS-01 candidate to OPS-02 command file

target disposition:

- target_disposition.md classifies target as CLI_LOCAL_VENDOR_SMOKE

PR-02 runtime binding:

- pr02_runtime_binding.md states runtime includes PR-02 birth-only remediation and no caller user_id/person_uid requirement
- pr02_prerequisite_binding.md exposes PR-02 report confirmations for targeted-tests-passed and runtime/no-user compatibility surface naming

env presence:

- redacted_env_presence.json contains key names and booleans only

PO authorization:

- request_summary.txt contains po_authorization_to_run_controlled_smoke=true

no-user input check:

- request_summary.txt records no_person_uid_in_command=true, no_user_id_in_command=true, no_app_user_ids_in_command=true

no-secret check:

- request_summary.txt records no_inline_secrets=true
- stdout_parse_validation.md records secret_values_detected=false

## Command Executed

Quoted from vendor_command.txt:

hdctl showcompat --source vendor --birthdate-a "1999-10-16" --birthtime-a "04:37" --location-a "Santiago, Chile" --birthdate-b "1978-06-17" --birthtime-b "02:35" --location-b "Tallinn, Estonia"

## Birth Inputs Used

Quoted from sample_birth_inputs.json:

{"birthdate-a":"1999-10-16","birthtime-a":"04:37","location-a":"Santiago, Chile","birthdate-b":"1978-06-17","birthtime-b":"02:35","location-b":"Tallinn, Estonia","constraints":{"no_app_user_ids":true,"no_person_uid":true,"no_user_id":true,"vendor_call_executed":true}}

## Target Disposition

Decisive lines from target_disposition.md:

- Target classification: CLI_LOCAL_VENDOR_SMOKE
- command target: hdctl showcompat
- source: vendor
- execution context: PO-controlled CLI/repo environment
- hosted HD Engine service target: not required for this command
- PF07 hosted-service binding required: no
- reason: the command is a CLI vendor-source smoke, not a hosted HD Engine HTTP service smoke
- PR-02 runtime binding proof: see audit/ops/hde-epic030/ops-02/pr02_runtime_binding.md
- env binding proof: see audit/ops/hde-epic030/ops-02/redacted_env_presence.json
- command proof: see audit/ops/hde-epic030/ops-02/vendor_command.txt

Contract alignment lines:

- governing_plan_source: audit/ops/hde-epic030/r3 Remediation Plan 01 HDE-EPIC030.md
- governing_plan_rule: Target system/service section explicitly allows CLI_LOCAL_VENDOR_SMOKE and states hosted-service PF07 facts are not required for this classification
- supporting_pf10_rule: target for this smoke is HD Engine CLI with --source vendor, and HDE_BASE_URL is not required unless command target changes to HTTP service

Applicability statement:

PF07 is not being used to invent a hosted target. This smoke targets the local hdctl CLI with vendor source. Hosted-service PF07 facts are not applicable unless the command is changed to call an HD Engine HTTP service.

## PR-02 Runtime Binding

Decisive lines from pr02_runtime_binding.md:

- git branch at evidence assembly: main
- git commit at evidence assembly: 7a4804ff6607b5ac728c63aa7c2e397bfc88f9d6
- command: /usr/bin/python3 -m pytest -q tests/cli/test_showcompat_sources.py::test_showcompat_vendor_dry_run
- result: 1 passed in 0.06s
- accepted proof name: test_no_user_boundary_accepts_birth_only_input_without_person_uid_or_user_id_and_is_ab_ba_stable
- PR-02 remediation present in runtime: true
- birth-only boundary implemented: true
- no caller user_id required: true
- no caller person_uid required: true
- target runtime used for OPS-02 includes PR-02 remediation: true

Decisive lines from pr02_prerequisite_binding.md:

- source_section: 2.23) Remediation HDE-EPIC030 - PR-02
- targeted_tests_passed_confirmation includes:
	- "✅ python -m pytest tests/compat/test_conjunction_no_user_boundary.py"
	- "✅ python -m pytest tests/compat/test_conjunction_no_user_boundary.py tests/compat/test_compat_public_lf_bom.py tests/compat/test_compat_public_ab_ba_identity.py tests/http/test_compat_endpoint_contract.py tests/http/test_endpoint_catalog.py tests/adapter/test_compat_http_parity.py tests/adapter/test_compat_http_dev.py tests/adapter/test_compat_writer_transport.py"
- runtime_no_user_compatibility_surface_named includes:
	- "The Remedial PR adds a runtime boundary change in engine/compat/compute.py."
	- "The Remedial PR adds _derived_birth_uid(...) and uses it only when the caller provided no user identifier but did provide a full birth tuple."
	- "The Remedial PR explicitly says the new proof's caller inputs include only birth fields and assert neither person_uid nor user_id exists in the caller objects."

## Request Summary

Decisive lines from request_summary.txt:

- command_source_was_ops01=true
- command_source_ops01_file=audit/ops/hde-epic030/ops-01/vendor_command_candidate.txt
- command_source_lineage=vendor_command.txt derives from OPS-01 concrete candidate with birth substitutions from sample_birth_inputs.json
- command_target=hdctl showcompat
- source=vendor
- input_shape=birth-only
- no_person_uid_in_command=true
- no_user_id_in_command=true
- no_app_user_ids_in_command=true
- no_inline_secrets=true
- target_classification=CLI_LOCAL_VENDOR_SMOKE
- hosted_pf07_service_target_required=no
- hosted_pf07_service_target_reason=not applicable because this is a CLI vendor-source smoke
- target_facts_used=command_target:hdctl_showcompat;source:vendor;execution_context:po_controlled_cli_repo;pr02_runtime_binding:present;env_binding_presence:redacted_env_presence_json;determinism_pins:LC_ALL_C_LANG_C_TZ_UTC;open_rails_vendor_step_only:SAFE_MODE_0_ALLOW_NETWORK_1;app_env:dev
- po_authorization_to_run_controlled_smoke=true

## Runtime Results

Quoted from exit_code.txt:

0

stderr size:

- 0 bytes

stdout parseability and hash:

- parseable_json: true
- stdout_nonempty: true
- stdout_sha256: d563abc5d0f01144a24719493f04b8d65efa548be6f3bb23269ba9f98f0b1c30
- secret_values_detected: false
- command_exit_code: 0

stdout hash sidecar content:

d563abc5d0f01144a24719493f04b8d65efa548be6f3bb23269ba9f98f0b1c30  audit/ops/hde-epic030/ops-02/stdout.json

## Execution Classification

Decisive lines from execution_classification.md:

- classification: PASS
- command_ran: true
- vendor_call_executed: true
- target_classification: CLI_LOCAL_VENDOR_SMOKE
- no_caller_user_id_required: true
- no_caller_person_uid_required: true
- contradiction resolution: prior vendor_call_executed=false state corrected to true in final evidence
- vendor_command_rerun_after_target_and_pr02_proof_established: false

## Result Summary

Decisive lines from result_summary.md:

- status: PASS
- target_disposition: CLI_LOCAL_VENDOR_SMOKE
- target_contract_alignment: PASS
- target_contract_alignment_basis: audit/ops/hde-epic030/r3 Remediation Plan 01 HDE-EPIC030.md Target system/service section permits CLI_LOCAL_VENDOR_SMOKE and says hosted-service PF07 facts are not required for this classification
- pr02_prerequisite_binding_file: audit/ops/hde-epic030/ops-02/pr02_prerequisite_binding.md
- command_exit_code: 0
- command_birth_only_vendor_shape_verified: true
- no_person_uid_supplied: true
- no_user_id_supplied: true
- no_app_user_ids_supplied: true
- sample_birth_inputs_vendor_call_executed: true
- stdout_non_empty: true
- stdout_parseable_json: true
- stderr_empty: true
- secret_values_persisted: false
- strict_pf10_2_24_contract_validation: PASS / PASS / none

## Checksum Ledger

Full files_sha256.txt content:

89eaa38bf3b57f9532cc16b67fb86a1112186e47225766ab6d0d71e5dffd0d3a  audit/ops/hde-epic030/ops-02/execution_classification.md
9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa  audit/ops/hde-epic030/ops-02/exit_code.txt
e0c4900d5e0286ba6176efb5c32aafce9cb8b749091f05576811727d2a8c5899  audit/ops/hde-epic030/ops-02/ops02_complete_action_log_and_evidence.md
a2a71a14a02d19a09fa5a6888f7837c73dbe4e761ecada16e337b4e15565047c  audit/ops/hde-epic030/ops-02/ops02_complete_action_log_and_evidence_final.md
6ab345d513d818669825eb6f05a39d37a88ab388a06eccde252c57170655233e  audit/ops/hde-epic030/ops-02/ops02_complete_action_log_and_evidence_single.md
11d1a5fab35c844eac2c8012681814829a963ae07ef1a21f6a8f89a54df872ee  audit/ops/hde-epic030/ops-02/ops02_complete_action_log_and_evidence_v2.md
42bc91237f8824573fcdd7867785ee4be5cee7547e6ef822a8caf3153fc62d67  audit/ops/hde-epic030/ops-02/ops02_complete_action_log_and_evidence_v3.md
350ad18ab05c6617984a5756280b17796015d80f7a346a0ce742982031719724  audit/ops/hde-epic030/ops-02/ops02_complete_action_log_and_evidence_v4.md
536be72a8bb39592a7e96cd276ef5881b1cc0390e658a7111909afe948578841  audit/ops/hde-epic030/ops-02/pf07_target_binding.md
45c5abd2c4ee3c5b925e78bc0978a559a28faee838eedd602a8dc5e78039921f  audit/ops/hde-epic030/ops-02/pf10_addendum_2.24_submission.md
820ff82b15645bc1451820961dd17261da4c41c56b57103bb568568a03889c4f  audit/ops/hde-epic030/ops-02/pfcanon_ops02_completion_matrix.md
945fb1c0821fb6cd69dbd641c4188ce84b5426b625c13c005fd2425633c9a8be  audit/ops/hde-epic030/ops-02/pr02_prerequisite_binding.md
9eb4c3b742c2dea2275e97141cb55622386a1a53a114b494649d5e9dc739bb45  audit/ops/hde-epic030/ops-02/pr02_runtime_binding.md
784fda9e707dea301b429659b8e069857166fb9b16e59e8cc3002ef5c635614d  audit/ops/hde-epic030/ops-02/preflight_validation.md
f866fe98a90116d968d34dece44ba766e6a5c9244ec6cd33c3373e6371a14692  audit/ops/hde-epic030/ops-02/rails_status_validation.md
c668de5da2fd3676f6dabbc01648212f70f12bf7db732bbac49458739c8bacd1  audit/ops/hde-epic030/ops-02/rails_wrapper_validation.md
8c71cbc9734f44cfabd6adcaab89348546823cb7c27a039086488b7e83ece36b  audit/ops/hde-epic030/ops-02/redacted_env_presence.json
02e06d55ccf92701779953970668b084f39583e73df03c9003522a595ec22b03  audit/ops/hde-epic030/ops-02/request_summary.txt
b80379aa37e79a1f40d3eb24c60f140fd913419099f5004246d03b47b0b66ee3  audit/ops/hde-epic030/ops-02/result_summary.md
990365b040deefa12227104d3fe0351b4fbe64e2310961e46ac1f2fb12f7e605  audit/ops/hde-epic030/ops-02/sample_birth_inputs.json
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855  audit/ops/hde-epic030/ops-02/stderr.log
d563abc5d0f01144a24719493f04b8d65efa548be6f3bb23269ba9f98f0b1c30  audit/ops/hde-epic030/ops-02/stdout.json
a31ee26bf24e58a11662b5904f58301ffab24c40621aff1237de6d2061e02f30  audit/ops/hde-epic030/ops-02/stdout.json.sha256
856b63ee82b5f162821ba6c0f3ee38b0dd27e021cb057e8bde3de74628be65e5  audit/ops/hde-epic030/ops-02/stdout_parse_validation.md
de3ab2cbc46790098d731c709ca730da7a38d9c110a4273957e5b361e97ca8c0  audit/ops/hde-epic030/ops-02/target_disposition.md
05ef2689453801666341330444119b962db84da38b93f4ac9668e64c576ee843  audit/ops/hde-epic030/ops-02/vendor_command.txt

## Non-Claims

- not QA PASS
- not Live QA completion
- not PF09 status change
- not epic closure
- not public Reader change
- not new public compat route