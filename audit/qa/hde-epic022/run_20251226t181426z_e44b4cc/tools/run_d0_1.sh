#!/usr/bin/env bash
set -euo pipefail

mkdir -p "${QA_RESULTS}"
mkdir -p "${QA_ROOT}/closeout"

python "${QA_TOOLS}/scan_required_paths.py" \
  --out "${QA_RESULTS}/required_paths_scan.json" \
  --paths \
    "docs/acceptance_map_epic022.json" \
    "audit/qa/hde-epic022/token_evidence_matrix.md" \
    "tools/evidence/update_evidence_index.py" \
    "tools/evidence/run_sanity_pipeline.py" \
    "tools/qa/emit_env_pins.sh" \
    "tools/cli/generate_showcompat_artifacts.py" \
    "tests/cli/test_errors_parity.py" \
    "tests/cli/test_cli_canonical_bytes.py" \
    "tests/cli/test_cli_usage_and_errors.py" \
    "tests/ops/test_evidence_index.py" \
    "tests/ops/test_machine_mirror_record.py" \
    "tests/ops/test_mirror_schema.py" \
    "ci/checks/check_mirror_schema.sh" \
    "artifacts/math/freeze_pack_manifest.json" \
    "artifacts/math/release_id.txt" \
    "artifacts/math/release_id_recompute.log" \
    "artifacts/identity/service_identity.json" \
    "artifacts/identity/emitter_sha256.txt"

python "${QA_TOOLS}/render_d0_scan.py" \
  --scan-json "${QA_RESULTS}/required_paths_scan.json" \
  --out-stable "${QA_EPIC_ROOT}/d0_scan.md" \
  --out-run "${QA_ROOT}/closeout/d0_scan.md" \
  --run-id "${RUN_ID}"
