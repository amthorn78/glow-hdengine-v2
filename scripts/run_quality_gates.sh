#!/usr/bin/env bash
set -euo pipefail

export SAFE_MODE="${SAFE_MODE:-1}"
export ALLOW_NETWORK="${ALLOW_NETWORK:-0}"
export LC_ALL="${LC_ALL:-C}"
export LANG="${LANG:-C}"
export TZ="${TZ:-UTC}"

python -m pip install -r requirements-dev.txt
python -m pytest --version

# Canonical smoke gate (stable in-repo subset): public reader/compat transport plus endpoint catalog.
python -m pytest -q \
  tests/http/test_compat_endpoint_contract.py \
  tests/http/test_reader_a7_transport.py \
  tests/http/test_endpoint_catalog.py

# Optional full suite (best effort, non-blocking unless explicitly requested).
if [[ "${RUN_FULL_TEST_SUITE:-0}" == "1" ]]; then
  python -m pytest -q
fi

git diff --check
