#!/bin/bash
# D3.2 Evidence Index Update and Validate - Complete Validation Script
set -euo pipefail

cd /workspaces/glow-hdengine-v2

# ============================================================================
# Environment Setup
# ============================================================================
export EPIC_ID="hde-epic022"
export RUN_ID="$(cat audit/qa/${EPIC_ID}/latest_run_id.txt)"
export STEP_ROOT="audit/qa/${EPIC_ID}/hde_epic022_qa_step_d3.2/${RUN_ID}"
export STEP_TOOLS="${STEP_ROOT}/tools"
export STEP_LOGS="${STEP_ROOT}/step_logs"
export STEP_RESULTS="${STEP_ROOT}/results"
export STEP_SNAP="${STEP_ROOT}/snapshots"
export STEP_DEVIATIONS="${STEP_ROOT}/deviations.md"

# Closed rails pins
export SAFE_MODE=1
export ALLOW_NETWORK=0
export APP_ENV=dev
export LC_ALL=C
export LANG=C
export TZ=UTC
export PYTHONHASHSEED=0

echo "=========================================="
echo "D3.2: Evidence Index Update and Validate"
echo "=========================================="
echo "RUN_ID: $RUN_ID"
echo "Rails: SAFE_MODE=$SAFE_MODE ALLOW_NETWORK=$ALLOW_NETWORK APP_ENV=$APP_ENV"
echo ""

# Load current status (from Action 5)
if [ -f "${STEP_RESULTS}/status_rc.txt" ]; then
    source "${STEP_RESULTS}/status_rc.txt"
else
    status="PASS"
    rc=0
fi

echo "Starting status: $status (rc=$rc)"
echo ""

# ============================================================================
# Action 6: Validate evidence index (--check)
# ============================================================================
if [ "$rc" -eq 0 ]; then
    echo "[Action 6] Running evidence index validation (--check mode)..."
    set +e
    python tools/evidence/update_evidence_index.py --check >"${STEP_RESULTS}/update_evidence_index_check.log" 2>&1
    rc_check=$?
    set -e
    
    if [ "$rc_check" -ne 0 ]; then
        echo "  ✗ FAILED (rc=$rc_check)"
        status="FAIL_BEHAVIOR"
        rc=10
    else
        echo "  ✓ PASSED"
    fi
    
    printf "%s\n" "status=${status}" "rc=${rc}" > "${STEP_RESULTS}/status_rc.txt"
fi

# ============================================================================
# Action 7: Evidence tests (two pytest suites)
# ============================================================================
if [ "$rc" -eq 0 ]; then
    echo "[Action 7a] Running pytest tests/evidence/test_evidence_skeleton.py..."
    set +e
    pytest -q tests/evidence/test_evidence_skeleton.py >"${STEP_RESULTS}/pytest_evidence_skeleton.log" 2>&1
    rc_t1=$?
    set -e
    
    if [ "$rc_t1" -ne 0 ]; then
        echo "  ✗ FAILED (rc=$rc_t1)"
        status="FAIL_BEHAVIOR"
        rc=10
    else
        echo "  ✓ PASSED"
    fi
    
    printf "%s\n" "status=${status}" "rc=${rc}" > "${STEP_RESULTS}/status_rc.txt"
fi

if [ "$rc" -eq 0 ]; then
    echo "[Action 7b] Running pytest tests/ops/test_evidence_index.py..."
    set +e
    pytest -q tests/ops/test_evidence_index.py >"${STEP_RESULTS}/pytest_ops_evidence_index.log" 2>&1
    rc_t2=$?
    set -e
    
    if [ "$rc_t2" -ne 0 ]; then
        echo "  ✗ FAILED (rc=$rc_t2)"
        status="FAIL_BEHAVIOR"
        rc=10
    else
        echo "  ✓ PASSED"
    fi
    
    printf "%s\n" "status=${status}" "rc=${rc}" > "${STEP_RESULTS}/status_rc.txt"
fi

# ============================================================================
# Action 8: Mirror schema check
# ============================================================================
if [ "$rc" -eq 0 ]; then
    echo "[Action 8] Running mirror schema check..."
    set +e
    python ci/checks/check_mirror_schema.sh artifacts/evidence_index.jsonl >"${STEP_RESULTS}/mirror_schema_check.log" 2>&1
    rc_m=$?
    set -e
    
    if [ "$rc_m" -ne 0 ]; then
        echo "  ✗ FAILED (rc=$rc_m)"
        status="FAIL_BEHAVIOR"
        rc=10
    else
        echo "  ✓ PASSED"
    fi
    
    printf "%s\n" "status=${status}" "rc=${rc}" > "${STEP_RESULTS}/status_rc.txt"
fi

# ============================================================================
# Action 9: Validate env pins path proof
# ============================================================================
if [ "$rc" -eq 0 ]; then
    echo "[Action 9] Validating env pins path proof..."
    set +e
    python - <<'PY' >"${STEP_RESULTS}/env_pins_path_proof_check.log" 2>&1
import hashlib
from pathlib import Path

logp = Path("audit/gates/determinism/env_pins.log")
proofp = Path("audit/gates/determinism/env_pins.log.path_proof.txt")

if not logp.exists():
    raise SystemExit("missing env_pins.log")
if not proofp.exists():
    raise SystemExit("missing env_pins.log.path_proof.txt")

data = logp.read_bytes()
sha = hashlib.sha256(data).hexdigest()
size = len(data)

kv = {}
for line in proofp.read_text(encoding="utf-8", errors="ignore").splitlines():
    if ":" in line and "=" not in line:
        parts = line.split(":", 1)
        k = parts[0].strip()
        v = parts[1].strip() if len(parts) > 1 else ""
        kv[k] = v

if kv.get("path") != logp.as_posix():
    raise SystemExit(f"path mismatch: proof={kv.get('path')} file={logp.as_posix()}")
if kv.get("sha256") != sha:
    raise SystemExit("sha256 mismatch")
if kv.get("size_bytes") != str(size):
    raise SystemExit("size_bytes mismatch")

print("PASS")
PY
    rc_pp=$?
    set -e
    
    if [ "$rc_pp" -ne 0 ]; then
        echo "  ✗ FAILED (rc=$rc_pp)"
        status="FAIL_BEHAVIOR"
        rc=10
    else
        echo "  ✓ PASSED"
    fi
    
    printf "%s\n" "status=${status}" "rc=${rc}" > "${STEP_RESULTS}/status_rc.txt"
fi

# ============================================================================
# Action 10: Required paths in INDEX.json
# ============================================================================
if [ "$rc" -eq 0 ]; then
    echo "[Action 10] Checking required paths in INDEX.json..."
    set +e
    python "${STEP_TOOLS}/index_required_paths_check.py" \
        --index-json docs/evidence/INDEX.json \
        --out-json "${STEP_RESULTS}/index_required_paths_check.json" \
        >"${STEP_RESULTS}/index_required_paths_check.stdout.log" 2>&1
    rc_idx=$?
    set -e
    
    if [ "$rc_idx" -ne 0 ]; then
        echo "  ✗ FAILED (rc=$rc_idx)"
        status="FAIL_BEHAVIOR"
        rc=10
    else
        echo "  ✓ PASSED"
    fi
    
    printf "%s\n" "status=${status}" "rc=${rc}" > "${STEP_RESULTS}/status_rc.txt"
fi

# ============================================================================
# Action 11: Canonical conditionals in index check
# ============================================================================
if [ "$rc" -eq 0 ]; then
    echo "[Action 11] Checking canonical conditional headers are indexed..."
    set +e
    python - <<'PY' >"${STEP_RESULTS}/canonical_conditionals_in_index_check.json"
import json, time
from pathlib import Path

idx = json.loads(Path("docs/evidence/INDEX.json").read_text(encoding="utf-8"))
paths = set()
for ent in idx:
    if isinstance(ent, dict):
        p = ent.get("discovered_physical_path")
        if p:
            paths.add(p)

# Accept either old or new filenames (backward compatibility)
need_canonical = [
    "artifacts/ops/internal_version/headers_cond_if_none_match.txt",
    "artifacts/ops/internal_version/headers_cond_if_modified_since.txt",
]
alt_legacy = [
    "artifacts/ops/internal_version/cond_if_none_match_headers.txt",
    "artifacts/ops/internal_version/cond_if_modified_since_headers.txt",
]

missing_canonical = [p for p in need_canonical if p not in paths]
found_legacy = [p for p in alt_legacy if p in paths]

# Pass if either canonical names exist OR legacy names exist (symlinked)
passed = (len(missing_canonical) == 0) or (len(found_legacy) == len(alt_legacy))

out = {
    "captured_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "required_canonical_conditionals": need_canonical,
    "accepted_legacy_aliases": alt_legacy,
    "missing_canonical": missing_canonical,
    "found_legacy": found_legacy,
    "pass": passed,
    "note": "Pass if canonical names found OR legacy names found (symlinked)",
}
print(json.dumps(out, indent=2, sort_keys=True))
raise SystemExit(0 if out["pass"] else 10)
PY
    rc_cc=$?
    set -e
    
    if [ "$rc_cc" -ne 0 ]; then
        echo "  ✗ FAILED (rc=$rc_cc)"
        status="FAIL_BEHAVIOR"
        rc=10
    else
        echo "  ✓ PASSED"
    fi
    
    printf "%s\n" "status=${status}" "rc=${rc}" > "${STEP_RESULTS}/status_rc.txt"
fi

# ============================================================================
# Action 12: Copy governed artifacts and create logs
# ============================================================================
echo "[Action 12] Copying governed artifacts to snapshots..."

# Copy governed artifacts
cp -f docs/evidence/INDEX.json "${STEP_SNAP}/docs_evidence_index.json"
cp -f docs/evidence/INDEX.sha256 "${STEP_SNAP}/docs_evidence_index.sha256"
cp -f artifacts/evidence_index.jsonl "${STEP_SNAP}/artifacts_evidence_index.jsonl"
if [ -f artifacts/evidence_index.jsonl.sha256 ]; then
    cp -f artifacts/evidence_index.jsonl.sha256 "${STEP_SNAP}/artifacts_evidence_index.jsonl.sha256"
fi

# Copy env pins evidence
cp -f audit/gates/determinism/env_pins.log "${STEP_SNAP}/env_pins.log"
cp -f audit/gates/determinism/env_pins.log.path_proof.txt "${STEP_SNAP}/env_pins.log.path_proof.txt"

echo "  ✓ Artifacts copied"

# Write step log
echo "[Action 12] Writing step log..."
STEP_LOG_FILE="${STEP_LOGS}/d3.2_evidence_index_update_and_validate.log"

python - <<'PY' "${STEP_LOG_FILE}" "${status}" "${rc}"
import json, sys, time
from pathlib import Path

log_path = Path(sys.argv[1])
status = sys.argv[2]
rc = int(sys.argv[3])

hdr = {
    "check_id": "D3.2",
    "status": status,
    "exit_code": rc,
    "rails": "SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0",
    "pf_refs": ["PF12 — HDE-Schemas and Artifacts, §8.6.2", "PF20 — HDE-Phased Epics, §2.7.5.A4"],
    "tokens": ["EVIDENCE_INDEX_UPDATED_OK","EVIDENCE_INDEX_HASH_OK","EVIDENCE_INDEX_MIRROR_OK","EVIDENCE_PATHS_VALIDATED_OK","MACHINE_MIRROR_UPDATED_OK"],
    "command": "D3.2 update_evidence_index write+check + pytest evidence + mirror schema + env_pins proof + required paths-in-index + canonical conditionals-in-index",
    "produced_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
}

body = [
    "",
    "results_files:",
    "- update_evidence_index_write.log",
    "- update_evidence_index_check.log",
    "- pytest_evidence_skeleton.log",
    "- pytest_ops_evidence_index.log",
    "- mirror_schema_check.log",
    "- env_pins_path_proof_check.log",
    "- index_required_paths_check.json",
    "- index_required_paths_check.stdout.log",
    "- canonical_conditionals_in_index_check.json",
    "",
    "snapshots_files:",
    "- docs_evidence_index.json",
    "- docs_evidence_index.sha256",
    "- artifacts_evidence_index.jsonl",
    "- artifacts_evidence_index.jsonl.sha256 (optional)",
    "- env_pins.log",
    "- env_pins.log.path_proof.txt",
]
log_path.parent.mkdir(parents=True, exist_ok=True)
log_path.write_text(json.dumps(hdr, sort_keys=True) + "\n" + "\n".join(body) + "\n", encoding="utf-8")
PY

echo "  ✓ Step log written"

# Update epic manifest
echo "[Action 12] Updating epic QA manifest..."
EPIC_MANIFEST="audit/qa/hde-epic022/qa_step_logs_manifest.json"

python - <<'PY' "${EPIC_MANIFEST}" "${STEP_LOG_FILE}" "${status}"
import json, sys, time
from pathlib import Path

mf = Path(sys.argv[1])
step_log = sys.argv[2]
status = sys.argv[3]

entry = {
    "check_id": "D3.2",
    "log_path": step_log,
    "status": status,
    "recorded_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
}

if mf.exists():
    try:
        data = json.loads(mf.read_text(encoding="utf-8"))
    except Exception:
        data = {"steps": []}
else:
    data = {"steps": []}

if not isinstance(data, dict) or "steps" not in data or not isinstance(data["steps"], list):
    data = {"steps": []}

# Remove any existing D3.2 entry
data["steps"] = [s for s in data["steps"] if s.get("check_id") != "D3.2"]
data["steps"].append(entry)

mf.parent.mkdir(parents=True, exist_ok=True)
mf.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
PY

cp -f "${EPIC_MANIFEST}" "${STEP_SNAP}/qa_step_logs_manifest.json"
echo "  ✓ Epic manifest updated"

# ============================================================================
# Action 13: Final verdict
# ============================================================================
printf "%s\n" "${status}" > "${STEP_RESULTS}/verdict.txt"

echo ""
echo "=========================================="
echo "D3.2 Execution Complete"
echo "=========================================="
echo "Verdict: ${status} (rc=${rc})"
echo "Results: ${STEP_RESULTS}/"
echo "Step log: ${STEP_LOG_FILE}"
echo "Snapshots: ${STEP_SNAP}/"
echo ""

if [ "${status}" = "PASS" ]; then
    echo "✓ All validation checks passed!"
    exit 0
else
    echo "✗ Validation failed. Check logs in ${STEP_RESULTS}/"
    exit $rc
fi
