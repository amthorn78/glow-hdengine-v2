#!/usr/bin/env bash
set -euo pipefail
m="${1:-release/manifest.sorted.json}"
[ -f "$m" ] && [ -s "$m" ] || { echo "missing $m" >&2; exit 4; }
h="$(sha256sum "$m" | awk '{print $1}')"
printf '%s\n' "$h" | grep -Eq '^[a-f0-9]{64}$' || { echo "bad sha: $h" >&2; exit 4; }
printf '%s\n' "$h"
