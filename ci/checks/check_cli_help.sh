#!/usr/bin/env bash
set -euo pipefail

stdout_file=$(mktemp)
stderr_file=$(mktemp)

if ! python -m engine.cli --help >"$stdout_file" 2>"$stderr_file"; then
  echo "CLI_HELP_EXIT_NONZERO" >&2
  rm -f "$stdout_file" "$stderr_file"
  exit 1
fi

if [[ -s "$stderr_file" ]]; then
  echo "CLI_HELP_STDERR" >&2
  cat "$stderr_file" >&2
  rm -f "$stdout_file" "$stderr_file"
  exit 1
fi

if [[ ! -s "$stdout_file" ]]; then
  echo "CLI_HELP_EMPTY" >&2
  rm -f "$stdout_file" "$stderr_file"
  exit 1
fi

tail -c1 "$stdout_file" | od -An -t o1 | grep -q '012' || {
  echo "CLI_HELP_MISSING_LF" >&2
  rm -f "$stdout_file" "$stderr_file"
  exit 1
}

rm -f "$stdout_file" "$stderr_file"
