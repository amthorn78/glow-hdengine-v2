#!/bin/bash
# Round 18 bench — run the four GCFPE-20260914.1 gates against a rig.
#
#   ./run_gates.sh <rig-root>
#
# <rig-root> must be a copy of the WHOLE synced skills tree with the two packaged
# skills swapped in — not just the two extracted packages. G2 reports
# SKILL_MISSING:glow-hde-pr-development, SKILL_MISSING:glow-merged-change-attribution-lock
# and PRIMARY_FILE_IDENTITY against a two-package rig, and G4 exits 2, because both
# read the installed suite. G1 and G3, and every D8 guard layer, are satisfied by the
# two packages alone. Each gate result is read from that tool's own top-level flag,
# never inferred from stdout prose.
set -u
export PYTHONDONTWRITEBYTECODE=1 LC_ALL=C LANG=C TZ=UTC
R="${1:?usage: run_gates.sh <rig-root>}"
C="$R/change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json"

cd "$R/change-flow/scripts"
out=$(python3 validate_gcfpe_20260914.py 2>&1); echo "G1 rc=$? $(echo "$out" | tail -1)"

cd "$R/flowmaster-validate/scripts"
out=$(python3 validate_gcfpe_20260914.py "$R/change-flow" --contract "$C" 2>&1); rc=$?
echo "G2 rc=$rc $(echo "$out" | python3 -c 'import sys,json
t=sys.stdin.read()
try:
    d=json.loads(t); print("ok=%s errors=%s" % (d.get("ok"), d.get("errors")))
except Exception: print(t.strip()[-300:])')"

out=$(python3 run_gcfpe_20260914_fixtures.py "$R/change-flow" --contract "$C" 2>&1); rc=$?
echo "G3 rc=$rc $(echo "$out" | python3 -c 'import sys,json
t=sys.stdin.read()
try:
    d=json.loads(t)
    bad=[c["name"] for c in d.get("cases",[]) if not c.get("passed")]
    print("fixture_suite_ok=%s cases=%s failing=%s" % (d.get("fixture_suite_ok"), len(d.get("cases",[])), bad))
except Exception: print(t.strip()[-300:])')"

out=$(python3 validate_flowmaster.py 2>&1); rc=$?
echo "G4 rc=$rc $(echo "$out" | grep -o 'FLOWMASTER_SUITE_[A-Z]*' | tail -1)"
