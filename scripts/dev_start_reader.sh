#!/usr/bin/env bash
set -euo pipefail

# Canonical dev Reader start command for internal/dev harnesses (EPIC019 C1)
: "${APP_ENV:=dev}"
: "${SAFE_MODE:=1}"
: "${ALLOW_NETWORK:=0}"
: "${LC_ALL:=C}"
: "${LANG:=C}"
: "${TZ:=UTC}"
: "${PORT:=8000}"

export APP_ENV SAFE_MODE ALLOW_NETWORK LC_ALL LANG TZ PORT

cat <<INFO
[dev-start] APP_ENV=${APP_ENV} SAFE_MODE=${SAFE_MODE} ALLOW_NETWORK=${ALLOW_NETWORK}
[dev-start] LC_ALL=${LC_ALL} LANG=${LANG} TZ=${TZ}
[dev-start] Binding port ${PORT} via python -m adapter.http_reader (host=0.0.0.0)
INFO

exec python -m adapter.http_reader
