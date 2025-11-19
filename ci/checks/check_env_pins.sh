#!/usr/bin/env bash
set -euo pipefail
fail=0

check_var() {
  local name="$1" expected="$2"
  local value="${!name:-}"
  if [[ "$value" != "$expected" ]]; then
    echo "ENV_MISMATCH:${name}:${value:-<unset>}!=${expected}" >&2
    fail=1
  fi
}

check_var "LC_ALL" "C"
check_var "LANG" "C"
check_var "TZ" "UTC"
check_var "SAFE_MODE" "1"
check_var "ALLOW_NETWORK" "0"

exit "$fail"
