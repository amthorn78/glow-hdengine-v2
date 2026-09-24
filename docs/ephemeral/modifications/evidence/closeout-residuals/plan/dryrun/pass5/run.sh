#!/bin/bash
# usage: run.sh mode:PID:PAGE:BATCH ...  (pass-5 driver; prints one summary line per page, no body text)
cd "$(dirname "$0")"
for x in "$@"; do IFS=: read m p g b <<< "$x"; python3 one.py $m $p $g $b | python3 -c "import json,sys; j=json.loads(sys.stdin.read()); pr=j.get('proof') or {}; print(j['pid'], j['exit'], j['refused'], 'PASS' if j['pass'] else 'FAIL', {k:pr.get(k) for k in ('pristine_states','ops','relanded_all_LANDED','partials','partials_repaired_exact','partials_refused','partials_repaired_wrong')} if pr else '')"; done
