#!/bin/bash
set -euo pipefail
cd /workspaces/glow-hdengine-v2

# Setup environment
export EPIC_ID="hde-epic022"
export RUN_ID="$(cat audit/qa/${EPIC_ID}/latest_run_id.txt)"
export STEP_ROOT="audit/qa/${EPIC_ID}/hde_epic022_qa_step_d3.2/${RUN_ID}"
export STEP_TOOLS="${STEP_ROOT}/tools"
export STEP_LOGS="${STEP_ROOT}/step_logs"
export STEP_RESULTS="${STEP_ROOT}/results"
export STEP_SNAP="${STEP_ROOT}/snapshots"

mkdir -p "${STEP_TOOLS}" "${STEP_LOGS}" "${STEP_RESULTS}" "${STEP_SNAP}"

export SAFE_MODE=1
export ALLOW_NETWORK=0
export APP_ENV=dev
export LC_ALL=C
export LANG=C
export TZ=UTC
export PYTHONHASHSEED=0

echo "Environment setup complete. RUN_ID=$RUN_ID"

# Initial status
status="PASS"
rc=0

# Continue with update_evidence_index_write
python tools/evidence/update_evidence_index.py >"${STEP_RESULTS}/update_evidence_index_write.log" 2>&1 || rc_write=$?

if [ "${rc_write:-0}" -ne 0 ]; then
  status="FAIL_BEHAVIOR"
  rc=10
fi

printf "%s\n" "status=${status}" "rc=${rc}" > "${STEP_RESULTS}/status_rc.txt"
echo "D3.2 partial run complete. Status: $status"
echo "See ${STEP_RESULTS}/ for logs"
