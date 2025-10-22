#!/usr/bin/env bash
set -euo pipefail

EPIC_ID="${EPIC_ID:-${1:-HDE-EPIC004}}"
STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
OUT_DIR="_arch/${EPIC_ID}_${STAMP}"
mkdir -p "${OUT_DIR}"

writel() { printf "%s\n" "$1" > "$2"; }
have_rg() { command -v rg >/dev/null 2>&1; }

EXCL_DIRS="--exclude-dir=.git --exclude-dir=_arch --exclude-dir=_archive --exclude-dir=__pycache__ --exclude-dir=.venv --exclude-dir=venv --exclude-dir=tests --exclude-dir=scripts"
INCLUDE_PY="--include=*.py --binary-files=without-match"

scan_routes() {
  if have_rg; then rg -n "add_url_rule|register_blueprint" adapter/ || true
  else grep -R -n -E "add_url_rule|register_blueprint" adapter/ ${INCLUDE_PY} ${EXCL_DIRS} || true
  fi
}
scan_imports_adapters() {
  if have_rg; then
    rg -n --type py -g '!adapters/**' -g '!core/**' -g '!server/**' -g '!tests/**' -g '!scripts/**' -g '!_archive/**' -g '!_arch/**' -g '!.venv/**' -g '!venv/**' \
      "from +adapters|import +adapters\\." . || true
  else
    grep -R -n -E "from +adapters|import +adapters\\." ${INCLUDE_PY} ${EXCL_DIRS} --exclude-dir=adapters . || true
  fi
}
scan_imports_core() {
  if have_rg; then
    rg -n --type py -g '!adapters/**' -g '!core/**' -g '!server/**' -g '!tests/**' -g '!scripts/**' -g '!_archive/**' -g '!_arch/**' -g '!.venv/**' -g '!venv/**' \
      "from +core|import +core\\." . || true
  else
    grep -R -n -E "from +core|import +core\\." ${INCLUDE_PY} ${EXCL_DIRS} --exclude-dir=core . || true
  fi
}
scan_imports_server() {
  if have_rg; then
    rg -n --type py -g '!adapters/**' -g '!core/**' -g '!server/**' -g '!tests/**' -g '!scripts/**' -g '!_archive/**' -g '!_arch/**' -g '!.venv/**' -g '!venv/**' \
      "from +server|import +server\\." . || true
  else
    grep -R -n -E "from +server|import +server\\." ${INCLUDE_PY} ${EXCL_DIRS} --exclude-dir=server . || true
  fi
}

# Public response paths only:
#  - adapter/http_*.py handlers
#  - engine/presenter/* emitters
#  - engine/emit_public.py final envelope
#  - scripts/hdctl.py (CLI presenter only)
scan_ad_hoc_emitters() {
  # resolve adapter/http_*.py to concrete list (nullglob-ish behavior)
  ADAPTER_LIST=$(ls adapter/http_*.py 2>/dev/null || true)
  if have_rg; then
    rg -n "json\\.dumps\\(|jsonify\\(|orjson|ujson|simplejson" \
      ${ADAPTER_LIST} engine/presenter/ engine/emit_public.py scripts/hdctl.py || true
  else
    # shellcheck disable=SC2086
    grep -n -E "json\\.dumps\\(|jsonify\\(|orjson|ujson|simplejson" \
      ${ADAPTER_LIST} engine/presenter/* engine/emit_public.py scripts/hdctl.py \
      ${INCLUDE_PY} --binary-files=without-match || true
  fi
}

scan_routes            > "${OUT_DIR}/routes.txt"
scan_imports_adapters  > "${OUT_DIR}/imports.adapters.txt"
scan_imports_core      > "${OUT_DIR}/imports.core.txt"
scan_imports_server    > "${OUT_DIR}/imports.server.txt"
scan_ad_hoc_emitters   > "${OUT_DIR}/emit.dumps.txt"

if command -v tree >/dev/null 2>&1; then
  tree -a -L 3 > "${OUT_DIR}/tree.txt" || writel "tree unavailable" "${OUT_DIR}/tree.txt"
else
  find . -maxdepth 3 -type f | LC_ALL=C sort > "${OUT_DIR}/tree.txt"
fi

PARITY="${OUT_DIR}/byte_parity.txt"
if [ -n "${HDE_CLI_SHOWCOMPAT:-}" ]; then
  SVC="/tmp/_svc_${STAMP}.bin"; CLI="/tmp/_cli_${STAMP}.bin"
  curl -sS "${HDE_BASE_URL:-http://127.0.0.1:5000}/api/compat/v1" \
       -H 'Content-Type: application/json' -X POST \
       --data-binary '{"a":"A","b":"B"}' -o "${SVC}" || true
  eval "${HDE_CLI_SHOWCOMPAT}" > "${CLI}" 2>/dev/null || true
  svc_sha="$(sha256sum "${SVC}" | awk '{print $1}')"
  cli_sha="$(sha256sum "${CLI}" | awk '{print $1}')"
  printf "service_sha=%s\ncli_sha=%s\nparity=%s\n" \
    "$svc_sha" "$cli_sha" "$([ "$svc_sha" = "$cli_sha" ] && echo PASS || echo FAIL)" > "${PARITY}"
else
  writel "parity=SKIPPED (HDE_CLI_SHOWCOMPAT not set)" "${PARITY}"
fi

passfail() { [ -s "$1" ] && echo FAIL || echo PASS; }
adapters="$(passfail "${OUT_DIR}/imports.adapters.txt")"
core="$(passfail "${OUT_DIR}/imports.core.txt")"
server="$(passfail "${OUT_DIR}/imports.server.txt")"
emits="$(passfail "${OUT_DIR}/emit.dumps.txt")"
routes_state="PASS"; [ -s "${OUT_DIR}/routes.txt" ] || routes_state="WARN (no routes detected)"

cat > "${OUT_DIR}/status.txt" <<TXT
EPIC_ID=${EPIC_ID}
STAMP=${STAMP}
READER_SINGLE_HOME_SCAN=${routes_state}
ADAPTERS_IMPORTS_EMPTY=${adapters}
CORE_IMPORTS_EMPTY=${core}
SERVER_IMPORTS_EMPTY=${server}
ADHOC_EMITTERS_EMPTY=${emits}
BYTE_PARITY=$(grep -o 'parity=.*' "${PARITY}" || echo 'parity=SKIPPED')
TXT

echo "Architecture snapshots written to ${OUT_DIR}"
