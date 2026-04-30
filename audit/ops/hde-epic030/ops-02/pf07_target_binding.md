# OPS-02 PF07 Target Binding (PF10 2.24 CLI Vendor Smoke)

date_utc: 2026-04-30
scope: Validate target-fact posture used by OPS-02 against PF10 2.24 required target facts.

## PF10 anchor

- docs/pfcanon/PF10-HDE-Build-Notes-v10.6.9.md:5615
  - Section 2.24 required target facts are listed for the exact CLI vendor smoke.

## Required target facts and current evidence

- command_target_hdctl_showcompat: PASS
  - evidence: audit/ops/hde-epic030/ops-02/vendor_command.txt
- data_source_vendor: PASS
  - evidence: audit/ops/hde-epic030/ops-02/vendor_command.txt
- execution_context_po_controlled_terminal_with_hdctl: PASS
  - evidence: audit/ops/hde-epic030/ops-02/request_summary.txt
- vendor_binding_hdapi_base_url_presence: PASS
  - evidence: audit/ops/hde-epic030/ops-02/redacted_env_presence.json
- vendor_credential_hd_api_key_presence: PASS
  - evidence: audit/ops/hde-epic030/ops-02/redacted_env_presence.json
- geo_api_key_presence_if_required: PASS
  - evidence: audit/ops/hde-epic030/ops-02/redacted_env_presence.json
- determinism_pins_lc_all_lang_tz: PASS
  - evidence: audit/ops/hde-epic030/ops-02/rails_wrapper_validation.md
- open_rails_vendor_step_only_safe_mode_0_allow_network_1: PASS
  - evidence: audit/ops/hde-epic030/ops-02/rails_wrapper_validation.md
- app_env_dev: PASS
  - evidence: audit/ops/hde-epic030/ops-02/rails_wrapper_validation.md
- hde_base_url_not_required_for_exact_cli_vendor_smoke: PASS
  - evidence: audit/ops/hde-epic030/ops-02/request_summary.txt

## Binding verdict

- pf07_target_fact_set_for_exact_cli_vendor_smoke: PASS
- blocker_from_pf07_target_binding: NONE

## Non-claim

This file validates target-fact binding only. It does not claim QA PASS, Live QA completion, PF09 status change, or epic closure.
