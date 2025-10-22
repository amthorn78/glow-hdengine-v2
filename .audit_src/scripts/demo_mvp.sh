#!/usr/bin/env bash
set -euo pipefail

mkdir -p artifacts/mvp
unset ALLOW_NETWORK HD_API_KEY GEO_API_KEY ENGINE_PROVIDER
export SAFE_MODE=1 APP_ENV=dev

# CLI compat → artifacts/mvp/compat_cli.json
python scripts/hdctl.py showcompat \
  --birthdate 1990-01-01 --birthtime 12:00 --place "Tallinn, EE" --tz Europe/Tallinn \
  --birthdate2 1992-02-02 --birthtime2 09:30 --place2 "Sarajevo, BA" --tz2 Europe/Sarajevo \
  --out artifacts/mvp/compat_cli.json

# Start API
python adapter/app.py >/dev/null 2>&1 & PID=$!
trap 'kill $PID 2>/dev/null || true' EXIT

# HTTP compat → artifacts/mvp/compat_http.json
curl -sS -H 'Content-Type: application/json' \
  -d '{"a":{"birthdate":"1990-01-01","birthtime":"12:00","place":"Tallinn, EE","tz":"Europe/Tallinn"}, "b":{"birthdate":"1992-02-02","birthtime":"09:30","place":"Sarajevo, BA","tz":"Europe/Sarajevo"}}' \
  http://127.0.0.1:5000/reader > artifacts/mvp/compat_http.json

# Chart read MVP → artifacts/mvp/singlebg.json
python scripts/hdctl.py read singlebg \
  --birthdate 1990-01-01 --birthtime 12:00 --place "Tallinn, EE" --tz Europe/Tallinn \
  --out artifacts/mvp/singlebg.json

cmp -s artifacts/mvp/compat_cli.json artifacts/mvp/compat_http.json
echo "DEMO_OK"
