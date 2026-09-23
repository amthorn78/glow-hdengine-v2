#!/bin/sh
# E2 pipeline on a fresh scratch copy of the synced skills tree, in the §5.11 pin order.
# usage: sh run_e2.sh   (writes only /tmp/claude-0/e2/** and, via G16 and the matrix copy, the two repository paths)
set -eu
export PYTHONDONTWRITEBYTECODE=1 TMPDIR=/tmp/claude-0/e2/tmp
SYNCED=/root/.claude/skills/synced/b25b7d44-c28f-42bf-b704-023250711755_bb1d0f6b-2c07-427b-9e63-27cb0b082502
REPO=/home/user/glow-hdengine-v2
EV=$REPO/docs/ephemeral/modifications/evidence
K=/tmp/claude-0/e2/skills
mkdir -p "$TMPDIR"
rm -rf "$K"; cp -a "$SYNCED" "$K"
python3 "$EV/build_r1_successor.py" "$K" "$REPO"                                   # 1-3 matrix, oracle, map
python3 "$EV/e2/g16_graph.py" "$REPO" "$K" /tmp/claude-0/e2/graph                   # 4 graph (G16) + bundled copies
python3 "$EV/regenerate_contract.py" generate /tmp/claude-0/e2/graph/graph_final.md \
  "$SYNCED/change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json" \
  "$K/flowmaster-validate/references/glow-hde-canonical-change-flow-r1-20260923.json" \
  "$K/change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json" \
  "$K/flowmaster-validate/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json"   # 5 contract
python3 "$EV/e2/apply_skill_edits.py" "$K"                                          # skill text, reversals, checks, fixtures
python3 "$EV/e2/pin_e2.py" "$K"                                                     # 6-9 profile, literals, fixtures, tree digest
find /tmp/claude-0/e2 "$REPO/docs" -name __pycache__ -print
