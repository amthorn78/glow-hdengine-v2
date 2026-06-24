#!/usr/bin/env bash
set -euo pipefail

printf '%s\n' '[post-create] Upgrading pip...'
python -m pip install --upgrade pip

printf '%s\n' '[post-create] Installing repo Python package...'
python -m pip install --user -e .

printf '%s\n' '[post-create] Verifying CLI help...'
python -m engine.cli --help >/tmp/devcontainer_cli_help.log

printf '%s\n' '[post-create] Done.'
