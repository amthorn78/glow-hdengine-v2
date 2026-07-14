#!/usr/bin/env bash
set -euo pipefail

required_vars=(ALLOW_NETWORK LANG LC_ALL SAFE_MODE TZ)

for v in "${required_vars[@]}"; do
  if [[ -z "${!v:-}" ]]; then
    echo "[env-pins] missing required var: $v" >&2
    exit 1
  fi
done

[[ "${ALLOW_NETWORK}" == "0" ]] || { echo "[env-pins] ALLOW_NETWORK must be 0" >&2; exit 1; }
[[ "${LANG}" == "C" ]]          || { echo "[env-pins] LANG must be C" >&2; exit 1; }
[[ "${LC_ALL}" == "C" ]]        || { echo "[env-pins] LC_ALL must be C" >&2; exit 1; }
[[ "${SAFE_MODE}" == "1" ]]     || { echo "[env-pins] SAFE_MODE must be 1" >&2; exit 1; }
[[ "${TZ}" == "UTC" ]]          || { echo "[env-pins] TZ must be UTC" >&2; exit 1; }

python -m engine.runtime.determinism_env \
  --log-path audit/gates/determinism/env_pins.log \
  --suite ci:determinism-rails \
  --suite tests:invariance \
  --suite tests:evidence-ordering \
  --suite evidence:sampler \
  --suite evidence:engine-core \
  --suite orientation:demo \
  --status success \
  --check-log

echo "[env-pins] OK: ALLOW_NETWORK=$ALLOW_NETWORK,LANG=$LANG,LC_ALL=$LC_ALL,SAFE_MODE=$SAFE_MODE,TZ=$TZ"
