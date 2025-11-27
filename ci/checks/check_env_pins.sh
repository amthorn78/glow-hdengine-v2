#!/usr/bin/env bash
set -euo pipefail
python -m engine.runtime.determinism_env \
  --log-path audit/gates/determinism/env_pins.log \
  --suite ci:determinism-rails \
  --suite tests:invariance \
  --suite tests:evidence-ordering \
  --suite orientation:demo \
  --status success \
  --check-log
