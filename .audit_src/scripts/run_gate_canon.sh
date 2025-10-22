#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
usage: scripts/run_gate_canon.sh [--help]
Runs the canon validator, archives artifacts to audit/gates/canon/<UTC-stamp>/,
writes sha256 sidecars, and logs "CANON_GATE: OK".
USAGE
}

if [[ "${1-}" == "--help" ]]; then usage; exit 0; fi
STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
OUTDIR="audit/gates/canon/${STAMP}"
mkdir -p "${OUTDIR}"

# Hash helper (sha256sum or shasum -a 256)
hash256() {
  local f="$1"
  if command -v sha256sum >/dev/null 2>&1; then
    sha256sum "$f" | awk '{print $1}'
  elif command -v shasum >/dev/null 2>&1; then
    shasum -a 256 "$f" | awk '{print $1}'
  else
    python3 - <<PY
import hashlib,sys
with open(sys.argv[1],'rb') as fh:
    print(hashlib.sha256(fh.read()).hexdigest())
PY
  fi
}

# Run validator (no --json); capture stdout/stderr into gate_log
{
  echo "# Canon Gate start: ${STAMP} (UTC)"
  echo "+ scripts/validate_canon.sh"
  bash scripts/validate_canon.sh
  echo "+ copy artifacts"
  # Copy artifacts if present
  [[ -f artifacts/canon_report.json ]] && cp artifacts/canon_report.json "${OUTDIR}/" || true
  [[ -f CANON_CHECKSUMS.json     ]] && cp CANON_CHECKSUMS.json     "${OUTDIR}/" || true
  # Hash sidecars
  for f in canon_report.json CANON_CHECKSUMS.json; do
    if [[ -f "${OUTDIR}/${f}" ]]; then
      hash256 "${OUTDIR}/${f}" > "${OUTDIR}/${f}.sha256"
      echo "+ wrote hash: ${OUTDIR}/${f}.sha256"
    fi
  done
  echo "CANON_GATE: OK"
} > "${OUTDIR}/gate_log.txt" 2>&1

echo "[gate] ${OUTDIR}"
