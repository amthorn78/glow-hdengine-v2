#!/usr/bin/env bash
set -euo pipefail
# Architecture Capture Protocol — run at epic close
# Usage:
#   EPIC_ID=HDE-EPIC003 scripts/architecture_capture.sh
# or scripts/architecture_capture.sh HDE-EPIC003

EPIC_ID="${EPIC_ID:-${1:-UNSPECIFIED_EPIC}}"
STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
OUT_DIR="_arch/${EPIC_ID}_${STAMP}"
mkdir -p "${OUT_DIR}"

# Helper: write file with guaranteed trailing LF
writel() { printf "%s\n" "$1" > "$2"; }

# 1) Routes (adapter only should register)
rg -n "add_url_rule|register_blueprint" adapter/ > "${OUT_DIR}/routes.txt" || true

# 2) Deprecated imports (must be empty in active code)
rg -n "from adapters|import adapters\." -g '!adapters/**' > "${OUT_DIR}/imports.adapters.txt" || true
rg -n "from core|import core\."       -g '!core/**'      > "${OUT_DIR}/imports.core.txt"     || true
rg -n "from server|import server\."   -g '!server/**'    > "${OUT_DIR}/imports.server.txt"   || true

# 3) Ad-hoc emitters forbidden in handlers/CLI (must be empty)
rg -n "json\.dumps\(|jsonify\(" engine/http cli > "${OUT_DIR}/emit.dumps.txt" || true

# 4) Directory tree (compact)
tree -a -L 3 > "${OUT_DIR}/tree.txt" || writel "tree unavailable" "${OUT_DIR}/tree.txt"

# 5) Optional: service vs CLI byte parity snapshot (skips if hook not set)
PARITY="${OUT_DIR}/byte_parity.txt"
if [ -n "${HDE_CLI_SHOWCOMPAT:-}" ]; then
  # Try a small service request; require defaults file if present
  SVC="/tmp/_svc_${STAMP}.bin"
  CLI="/tmp/_cli_${STAMP}.bin"
  if [ -f config/compat_defaults.json ]; then
    svc_body='{"a_id":"A","b_id":"B","viewer_prefs":'"$(cat config/compat_defaults.json)"'}'
  else
    svc_body='{"a_id":"A","b_id":"B"}'
  fi
  curl -s "${HDE_BASE_URL:-http://127.0.0.1:5000}/api/compat/v1" \
       -H 'Content-Type: application/json' -X POST \
       --data-binary "${svc_body}" > "${SVC}" || true
  # CLI env hook: e.g. export HDE_CLI_SHOWCOMPAT='hdctl showcompat --a {A} --b {B} --prefs {PREFS}'
  PREFS="/tmp/_prefs_${STAMP}.json"
  if [ -f config/compat_defaults.json ]; then cp -f config/compat_defaults.json "${PREFS}"; else echo '{}' > "${PREFS}"; fi
  CLI_CMD="${HDE_CLI_SHOWCOMPAT}"
  CLI_CMD="${CLI_CMD//\{A\}/A}"
  CLI_CMD="${CLI_CMD//\{B\}/B}"
  CLI_CMD="${CLI_CMD//\{PREFS\}/${PREFS}}"
  (eval "${CLI_CMD}" > "${CLI}" 2>/dev/null) || true
  svc_sha="$(sha256sum "${SVC}" | awk '{print $1}')"
  cli_sha="$(sha256sum "${CLI}" | awk '{print $1}')"
  printf "service_sha=%s\ncli_sha=%s\nparity=%s\n" "$svc_sha" "$cli_sha" \
    "$( [ "$svc_sha" = "$cli_sha" ] && echo PASS || echo FAIL )" > "${PARITY}"
else
  writel "parity=SKIPPED (HDE_CLI_SHOWCOMPAT not set)" "${PARITY}"
fi

# 6) ARCHITECTURE.md copy for the epic bundle (if present)
if [ -f ARCHITECTURE.md ]; then
  cp -f ARCHITECTURE.md "${OUT_DIR}/ARCHITECTURE_MAP_AFTER.md"
fi

# 7) Status summary (simple PASS/FAIL based on emptiness / presence)
passfail() { [ -s "$1" ] && echo FAIL || echo PASS; }
# Empty means *pass* for the “must be empty” scans
adapters="$(passfail "${OUT_DIR}/imports.adapters.txt")"
core    ="$(passfail "${OUT_DIR}/imports.core.txt")"
server  ="$(passfail "${OUT_DIR}/imports.server.txt")"
emits   ="$(passfail "${OUT_DIR}/emit.dumps.txt")"

routes_state="PASS" # informational: existence is expected; enforcement is in tests
[ -s "${OUT_DIR}/routes.txt" ] || routes_state="WARN (no routes detected)"

cat > "${OUT_DIR}/status.txt" <<TXT
EPIC_ID=${EPIC_ID}
STAMP=${STAMP}
READER_SINGLE_HOME_SCAN=${routes_state}
ADAPTERS_IMPORTS_EMPTY=${adapters}
CORE_IMPORTS_EMPTY=${core}
SERVER_IMPORTS_EMPTY=${server}
ADHOC_EMITTERS_EMPTY=${emits}
ARCH_SNAPSHOTS_LF=unchecked (enforced by tests)
BYTE_PARITY=$(grep -o 'parity=.*' "${PARITY}" || echo "parity=SKIPPED")
TXT

echo "Architecture snapshots written to ${OUT_DIR}"
