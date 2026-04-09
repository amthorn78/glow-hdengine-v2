#!/usr/bin/env bash
set -euo pipefail

# Canonical dev Reader start command for internal/dev harnesses (EPIC019 C1)
: "${SAFE_MODE:=1}"
: "${ALLOW_NETWORK:=0}"
: "${LC_ALL:=C}"
: "${LANG:=C}"
: "${TZ:=UTC}"
: "${PORT:=8000}"

export SAFE_MODE ALLOW_NETWORK LC_ALL LANG TZ PORT
if [[ "${APP_ENV+x}" == "x" ]]; then
  export APP_ENV
  APP_ENV_DISPLAY="${APP_ENV}"
else
  APP_ENV_DISPLAY="<UNSET>"
fi

cat <<INFO
[dev-start] APP_ENV=${APP_ENV_DISPLAY} SAFE_MODE=${SAFE_MODE} ALLOW_NETWORK=${ALLOW_NETWORK}
[dev-start] LC_ALL=${LC_ALL} LANG=${LANG} TZ=${TZ}
[dev-start] Binding port ${PORT} via python -m adapter.http_reader (host=0.0.0.0)
INFO

exec python -m adapter.http_reader
