"""Repair round 5 (P-88): land.py on SYNTHETIC text (no prompt body). Every subset of CL-E-20's landing operations is
applied, then `plan` and `check` run on the result. Pass: an empty subset plans normally (repair []); the full set reads
ALREADY_LANDED and check passes; every partial subset either plans only the missing edits, and the text those
operations produce equals the fully landed text and passes check, or is refused; no doubled insertion passes."""
import sys, io, json, contextlib, itertools
sys.dont_write_bytecode = True
ENG, PKG, REG = sys.argv[1], sys.argv[2], sys.argv[3]
sys.path.insert(0, ENG)
import land as L, dryrun as D, closeout_rules as R
pid = 'CL-E-20'
body = ("# Synthetic\n"
        "You run a revalidation session, read-only. Keep facts.\n"
        "Record status in permitted metadata or handoff when needed.\n"
        "Unrelated line one.\n"
        "Record it in the artifact lineage metadata or handoff.\n"
        "Unrelated line two.\n"
        "Later: PR-40 independently verifies the later asserted merge and landed lineage.\n"
        "End.\n")
def run(text, mode='plan'):
    D.latest_body = lambda page: ('2026-01-01T00:00:00Z', text)
    D.SOURCE = 'synthetic'
    sys.argv = ['land.py', mode, pid, '0'*32, '--skills', PKG, '--registry', REG]
    out = io.StringIO(); code = 0
    with contextlib.redirect_stdout(out):
        try: L.main()
        except SystemExit as e: code = e.code
    try: j = json.loads(out.getvalue())
    except Exception: j = {'raw': out.getvalue()[:300]}
    return code or 0, j
# The synthetic text cannot satisfy the registry row or the body validator, which pass 4 and pass 5 prove on the real
# bodies. Here `check` keeps everything land.py decides about the landing state (STALE, doubled insertions, tokens)
# and ignores the registry, guard and validator verdicts.
_orig = L.checks
def _state_only(pid_, text_, a_, mode_):
    r = _orig(pid_, text_, a_, mode_)
    if r.get("status"):
        return r
    return {**r, "pass": not r["doubled_insertions"] and r["unfilled_tokens"] == 0}
L.checks = _state_only
post, rep = R.apply(pid, body)
ops = D.ops_for(body, post)
full = D.simulate(body, ops)
rows, ok = [], True
for k in range(len(ops) + 1):
    for sub in itertools.combinations(range(len(ops)), k):
        text = D.simulate(body, [ops[i] for i in sub]) if sub else body
        code, j = run(text)
        row = {'applied': list(sub), 'plan_exit': code, 'refused': j.get('refused'), 'repair': j.get('repair')}
        if code == 0:
            fixed = D.simulate(text, j['ops'])
            row['equals_full'] = fixed == full
            c2, j2 = run(fixed, 'check')
            row['check_after_repair'] = j2.get('pass')
            good = row['equals_full'] and j2.get('pass') and (bool(sub) == bool(j['repair']))
        elif k == len(ops):
            c2, j2 = run(text, 'check'); row['check'] = j2.get('pass')
            good = code == 3 and j2.get('pass')
        else:
            good = code in (3, 4, 8)  # refused: the unit stops
        row['good'] = bool(good); ok &= bool(good)
        rows.append(row)
# the round-4 counterexample: OWN landed alone
dup = post.replace(R.OWN, R.OWN + " " + R.OWN, 1)
class A: pass
a = A(); a.registry = REG; a.guards = str(L.HERE.parent / 'registry/row_assertions.json'); a.skills = PKG
res = _orig(pid, dup, a, 'check')
ok &= (res['doubled_insertions'] == ['R-OWN'] and res['pass'] is False)
print(json.dumps({'ops': len(ops), 'subsets': len(rows), 'all_good': bool(ok),
                  'doubled_OWN_check': {'doubled_insertions': res['doubled_insertions'], 'pass': res['pass']},
                  'rows': rows}, indent=1))
