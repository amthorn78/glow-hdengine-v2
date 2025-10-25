#!/usr/bin/env bash
set -euo pipefail

CMD_ARGS="'adapter.factory:create_app()' --bind 0.0.0.0:${PORT:-8000} --workers 2 --threads 4 --timeout 30"

if [ -x /app/.venv/bin/python ]; then
  echo "[start_web] using venv python at /app/.venv/bin/python"
  exec /app/.venv/bin/python -m gunicorn ${CMD_ARGS}
else
  echo "[start_web] /app/.venv/bin/python not found; falling back to shimmed gunicorn on PATH"
  command -v gunicorn >/dev/null 2>&1 || { echo "[start_web] gunicorn not found on PATH"; exit 127; }
  exec gunicorn ${CMD_ARGS}
fi
