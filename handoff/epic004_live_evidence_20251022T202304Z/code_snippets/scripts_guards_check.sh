#!/usr/bin/env bash
set -euo pipefail
rg -n "json\.dumps\(|jsonify\(|orjson|ujson|simplejson" adapter engine scripts 2>/dev/null || true
