#!/bin/sh
# Round-a3 hardening pipeline on the E2 scratch tree, then every gate: live suites, the 12 historical-layer commands
# (byte-compared with a fresh baseline copy of the installed tree), the E2 and round-a1 regressions (from the
# derive_regressions_a3.py copies) and the round-a3 regressions.
# usage: sh run_repair_a3.sh            (reads /root/.claude/skills read-only; writes only /tmp/claude-0/e2/skills
#                                         and /tmp/claude-0/repair3/**)
# The pre-repair tree must be the round-a3 reviewed tree; SKIP_APPLY=1 re-runs the gates only.
set -eu
export PYTHONDONTWRITEBYTECODE=1 TMPDIR=/tmp/claude-0/repair3/tmp
SYNCED=/root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502
REPO=/home/user/glow-hdengine-v2
EV=$REPO/docs/ephemeral/modifications/evidence
K=/tmp/claude-0/e2/skills
R=/tmp/claude-0/repair3
GRAPH=/tmp/claude-0/e2/graph/graph_final.json
mkdir -p "$TMPDIR" "$R/reg" "$R/out" "$R/scripts"
freeze() { for s in flowmaster-validate change-flow glow-hde-pr-development session-relay-flowmaster \
                    amthor-workspace-governance-audit tw-flowmaster; do
             printf '%-35s %s\n' "$s" "$(python3 "$REPO/docs/prompt_ecosystem_management/freeze.py" "$1/$s")"; done; }

if [ "${SKIP_APPLY:-0}" != 1 ]; then
  echo "== pre-repair freeze (must equal the round-a3 reviewed digests)"; freeze "$K"
  python3 "$EV/repair-a3/apply_repairs_a3.py" "$K"
  python3 "$EV/repair-a3/pin_repairs_a3.py" "$K"
fi
echo "== repaired freeze"; freeze "$K"

rm -rf "$R/base"; cp -a "$SYNCED" "$R/base"
echo "== baseline freeze (installed tree, spec §2)"; freeze "$R/base"
python3 "$EV/repair-a3/derive_regressions_a3.py" "$R/scripts"

echo "== suites: repaired"; python3 "$R/scripts/run_suites.py" "$K" "$GRAPH" "$R/out/after" > "$R/out/after.jsonl"
echo "== suites: baseline"; python3 "$R/scripts/run_suites.py" "$R/base" "$GRAPH" "$R/out/baseline" > "$R/out/baseline.jsonl"
python3 - "$R/out" <<'EOF'
import json, sys
from pathlib import Path
out = Path(sys.argv[1])
a = {r["name"]: r for r in json.loads((out / "after/summary.json").read_text())}
b = {r["name"]: r for r in json.loads((out / "baseline/summary.json").read_text())}
for n, r in a.items():
    if r["layer"] == "live":
        print(f"LIVE {n:30} exit={r['exit']} {json.dumps(r['flag'], ensure_ascii=False)[:300]}")
same = 0
for n, r in a.items():
    if r["layer"] == "hist":
        raw_a = (out / "after" / f"{n}.out").read_bytes(); raw_b = (out / "baseline" / f"{n}.out").read_bytes()
        eq = r["stdout_sha256"] == b[n]["stdout_sha256"] and r["exit"] == b[n]["exit"] == 0 and raw_a == raw_b
        same += eq
        print(f"HIST {n:30} exit={r['exit']} bytes={r['stdout_bytes']} sha256={r['stdout_sha256'][:16]} byte_equal_to_baseline={eq}")
print(f"HISTORICAL_BYTE_EQUAL {same} of {sum(r['layer'] == 'hist' for r in a.values())}")
EOF

echo "== regressions"
python3 "$R/scripts/regress_oracle.py" "$K" "$GRAPH" > "$R/out/regress_oracle.out" 2>&1 || true; tail -1 "$R/out/regress_oracle.out"
python3 "$R/scripts/regress_skills.py" "$K" "$R/base" > "$R/out/regress_skills.out" 2>&1 || true; tail -1 "$R/out/regress_skills.out"
python3 "$R/scripts/regress_contract.py" "$K" > "$R/out/regress_contract.out" 2>&1 || true; tail -1 "$R/out/regress_contract.out"
python3 "$R/scripts/regress_fixtures.py" "$K" > "$R/out/regress_fixtures.out" 2>&1 || true; tail -1 "$R/out/regress_fixtures.out"
python3 "$R/scripts/regress_repair_a1.py" "$K" "$GRAPH" > "$R/out/regress_repair_a1.out" 2>&1 || true; tail -1 "$R/out/regress_repair_a1.out"
python3 "$R/scripts/regress_repair_a2.py" "$K" "$GRAPH" > "$R/out/regress_repair_a2.out" 2>&1 || true; tail -1 "$R/out/regress_repair_a2.out"
python3 "$EV/repair-a3/regress_repair_a3.py" "$K" "$GRAPH" > "$R/out/regress_repair_a3.out" 2>&1 || true; tail -1 "$R/out/regress_repair_a3.out"
find /tmp/claude-0/e2 "$R" "$REPO/docs" -name __pycache__ -print
