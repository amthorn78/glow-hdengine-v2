#!/usr/bin/env bash
set -euo pipefail

PYTHON="${PYTHON:-python3}"
VENV_DIR="${VENV_DIR:-.venv}"
VENV_PYTHON="${VENV_DIR}/bin/python"

printf '%s\n' "[post-create] Ensuring ${VENV_DIR}..."
"${PYTHON}" -m venv --upgrade-deps "${VENV_DIR}"

printf '%s\n' '[post-create] Installing repo Python dependencies...'
"${VENV_PYTHON}" -m pip install -r requirements.txt -r requirements-dev.txt -e .

printf '%s\n' '[post-create] Verifying pytest readiness...'
"${VENV_PYTHON}" -m pytest --version

printf '%s\n' '[post-create] Verifying CLI help...'
"${VENV_PYTHON}" -m engine.cli --help >/tmp/devcontainer_cli_help.log

printf '%s\n' '[post-create] Done.'
