#!/usr/bin/env bash
set -euo pipefail

EPIC_ID="${EPIC_ID:-${1:-HDE-EPIC004}}"
STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
OUT_DIR="_arch/${EPIC_ID}_${STAMP}"
mkdir -p "${OUT_DIR}"

writel() { printf "%s\n" "$1" > "$2"; }
ensure_lf(){ f="$1"; [ -f "$f" ] || : > "$f"; last="$(tail -c 1 "$f" 2>/dev/null || echo '')"; [ "$last" = $'\n' ] || printf '\n' >> "$f"; }
have_rg(){ command -v rg >/dev/null 2>&1; }

# Exclusions & includes
EXCL_DIRS="--exclude-dir=.git --exclude-dir=_arch --exclude-dir=_archive --exclude-dir=__pycache__ --exclude-dir=.venv --exclude-dir=venv --exclude-dir=tests --exclude-dir=scripts --exclude-dir=.audit_src"
INCLUDE_PY="--include=*.py --binary-files=without-match"

scan_routes(){
  if have_rg; then rg -n "add_url_rule|register_blueprint" adapter/ || true
  else grep -R -n -E "add_url_rule|register_blueprint" adapter/ ${INCLUDE_PY} ${EXCL_DIRS} || true
  fi
}

scan_imports_adapters(){
  if have_rg; then
    rg -n --type py -g '!adapters/**' -g '!core/**' -g '!server/**' -g '!tests/**' -g '!scripts/**' -g '!_archive/**' -g '!_arch/**' -g '!.venv/**' -g '!venv/**' \
      "from +adapters|import +adapters\\." adapter/ engine/ || true
  else
    grep -R -n -E "from +adapters|import +adapters\\." adapter/ engine/ ${INCLUDE_PY} ${EXCL_DIRS} --exclude-dir=adapters || true
  fi
}

scan_imports_core(){
  if have_rg; then
    rg -n --type py -g '!adapters/**' -g '!core/**' -g '!server/**' -g '!tests/**' -g '!scripts/**' -g '!_archive/**' -g '!_arch/**' -g '!.venv/**' -g '!venv/**' \
      "from +core|import +core\\." adapter/ engine/ || true
  else
    grep -R -n -E "from +core|import +core\\." adapter/ engine/ ${INCLUDE_PY} ${EXCL_DIRS} --exclude-dir=core || true
  fi
}

scan_imports_server(){
  if have_rg; then
    rg -n --type py -g '!adapters/**' -g '!core/**' -g '!server/**' -g '!tests/**' -g '!scripts/**' -g '!_archive/**' -g '!_arch/**' -g '!.venv/**' -g '!venv/**' \
      "from +server|import +server\\." adapter/ engine/ || true
  else
    grep -R -n -E "from +server|import +server\\." adapter/ engine/ ${INCLUDE_PY} ${EXCL_DIRS} --exclude-dir=server || true
  fi
}

scan_ad_hoc_emitters(){
  ADAPTER_LIST=$(ls adapter/http_*.py 2>/dev/null || true)
  if have_rg; then
    rg -n "json\\.dumps\\(|jsonify\\(|orjson|ujson|simplejson" ${ADAPTER_LIST} engine/presenter/ engine/emit_public.py scripts/hdctl.py || true
  else
    # shellcheck disable=SC2086
    grep -n -E "json\\.dumps\\(|jsonify\\(|orjson|ujson|simplejson" ${ADAPTER_LIST} engine/presenter/* engine/emit_public.py scripts/hdctl.py ${INCLUDE_PY} --binary-files=without-match || true
  fi
}

# Run scans
scan_routes            > "${OUT_DIR}/routes.txt"
scan_imports_adapters  > "${OUT_DIR}/imports.adapters.txt"
scan_imports_core      > "${OUT_DIR}/imports.core.txt"
scan_imports_server    > "${OUT_DIR}/imports.server.txt"
scan_ad_hoc_emitters   > "${OUT_DIR}/emit.dumps.txt"

# Tree snapshot (depth 3); always LF-terminate key files
if command -v tree >/dev/null 2>&1; then
  tree -a -L 3 > "${OUT_DIR}/tree.txt" || writel "tree unavailable" "${OUT_DIR}/tree.txt"
else
  find . -maxdepth 3 -type f | LC_ALL=C sort > "${OUT_DIR}/tree.txt"
fi

for f in routes.txt imports.adapters.txt imports.core.txt imports.server.txt tree.txt status.txt; do
  ensure_lf "${OUT_DIR}/$f"
done

# Byte parity (optional; skipped unless env set)
PARITY="${OUT_DIR}/byte_parity.txt"
if [ -n "${HDE_CLI_SHOWCOMPAT:-}" ]; then
  SVC="/tmp/_svc_${STAMP}.bin"; CLI="/tmp/_cli_${STAMP}.bin"
  curl -sS "${HDE_BASE_URL:-http://127.0.0.1:5000}/api/compat/v1" -H 'Content-Type: application/json' -X POST --data-binary '{"a":"A","b":"B"}' -o "${SVC}" || true
  eval "${HDE_CLI_SHOWCOMPAT}" > "${CLI}" 2>/dev/null || true
  svc_sha="$(sha256sum "${SVC}" | awk '{print $1}')"
  cli_sha="$(sha256sum "${CLI}" | awk '{print $1}')"
  printf "service_sha=%s\ncli_sha=%s\nparity=%s\n" "$svc_sha" "$cli_sha" "$([ "$svc_sha" = "$cli_sha" ] && echo PASS || echo FAIL)" > "${PARITY}"
else
  writel "parity=SKIPPED (HDE_CLI_SHOWCOMPAT not set)" "${PARITY}"
fi
ensure_lf "${PARITY}"

# Summarize (empty => PASS)
passfail() {
  f="$1"
  # PASS if file missing, zero length, or contains only whitespace (e.g., a single LF)
  [ -f "$f" ] || { echo PASS; exit 0; }
  # empty (size=0)
  if [ ! -s "$f" ]; then echo PASS; exit 0; fi
  # whitespace-only
  if [ "$(sed 's/[[:space:]]//g' "$f" | wc -c)" -eq 0 ]; then echo PASS; exit 0; fi
  # otherwise there were matches
  echo FAIL
}
