import sys, json, shutil, subprocess, os
sys.dont_write_bytecode = True
from texts import T
from apply_8b_consts import CF_RETIRED
A = '/tmp/claude-0/v2work8/A'; W = '/tmp/claude-0/v2work8/regA'
ENV = {**os.environ, 'PYTHONDONTWRITEBYTECODE': '1', 'TMPDIR': '/tmp/claude-0/v2work8/tmp'}
END = '<!-- FLOWMASTER_SPECIALIZATION_END -->'
REQ = ["PR-30 and PR-35 are two phases", T['NINE'], "run in two dedicated sessions", "never as a subagent, forked agent or workflow agent of PR-30",
       "no session is created by an agent", "One Proceed per approved per-PR plan", "It carries no branch and no commit",
       "exactly one fenced `text` `NEXT_PROMPT_HANDOFF` block", "PR_RETURN_PHASE", "PF10_BUILD_NOTES_ADDENDUM", "SOURCE_RESOLUTION_ERROR",
       "Only Nathan / Product Owner may manually invoke selected `PR-50", "ALPHA_STOPPED_PENDING_CHANGE_FLOW_REFACTOR"]
def fresh():
    shutil.rmtree(W, ignore_errors=True); shutil.copytree(A, W)
def edit(rel, fn):
    p = W + '/' + rel; s = open(p, encoding='utf-8').read(); s2 = fn(s); assert s2 != s; open(p, 'w', encoding='utf-8').write(s2)
def inject(rel, text): edit(rel, lambda s: s.replace(END, text + '\n\n' + END, 1))
def cf():
    r = subprocess.run([sys.executable, W + '/change-flow/scripts/validate_gcfpe_20260914.py'], capture_output=True, text=True, env=ENV)
    return r.returncode, (r.stdout + r.stderr).strip()
def cf_all():
    s = open(W + '/change-flow/SKILL.md', encoding='utf-8').read()
    return [f"missing:{t[:30]}" for t in REQ if t not in s] + [f"retired:{t[:30]}" for t in CF_RETIRED if t.lower() in s.lower()]
def restamp():
    subprocess.run([sys.executable, '/tmp/claude-0/spec/s8b/work/restamp.py', W], capture_output=True, env=ENV)
def suite():
    r = subprocess.run([sys.executable, W + '/flowmaster-validate/scripts/validate_flowmaster.py', '--skills-root', W], capture_output=True, text=True, env=ENV)
    d = json.loads(r.stdout)
    return d['verdict'], {k: v['errors'] for k, v in d['skills'].items() if v['errors']}
res = []
def rec(rid, ok, detail): res.append((rid, ok)); print(('OK  ' if ok else 'BAD ') + rid, str(detail)[:260])
fresh(); rc, msg = cf(); rec('clean-cf', rc == 0 and cf_all() == [], msg)
for i, p in enumerate(CF_RETIRED, 1):
    fresh(); inject('change-flow/SKILL.md', p); rc, msg = cf()
    rec(f'R-CF-{i}', rc == 1 and msg == 'FAIL: retired skill clause present: ' + p and len(cf_all()) == 1, msg)
fresh(); inject('change-flow/SKILL.md', CF_RETIRED[0].upper()); rc, msg = cf(); rec('R-CF-CASE', rc == 1 and msg == 'FAIL: retired skill clause present: ' + CF_RETIRED[0] and len(cf_all()) == 1, msg)
for rid, lit, fn in [
  ('R-CF-A18', 'never as a subagent, forked agent or workflow agent of PR-30', lambda s: s.replace(' ' + T['A18'], '', 1)),
  ('R-CF-9', T['NINE'], lambda s: s.replace(T['NINE'] + '.', '', 1)),
  ('R-CF-DISP', 'no session is created by an agent', lambda s: s.replace(' No agent merges, and no session is created by an agent.', '', 1)),
  ('R-CF-PROC', 'One Proceed per approved per-PR plan', lambda s: s.replace(' ' + T['C-PROCEED'], '', 1)),
  ('R-CF-HND', 'It carries no branch and no commit', lambda s: s.replace('It carries no branch and no commit: ', '', 1)),
]:
    fresh(); edit('change-flow/SKILL.md', fn); rc, msg = cf(); rec(rid, rc == 1 and msg == 'FAIL: missing skill clause: ' + lit and len(cf_all()) == 1, msg)
fresh(); edit('change-flow/SKILL.md', lambda s: s.replace('CHANGE_FLOW_SPECIALIZATION_REVISION: 3.3.0', 'CHANGE_FLOW_SPECIALIZATION_REVISION: 3.2.9', 1)); rc, msg = cf(); rec('R-CF-REV', rc == 1 and msg == 'FAIL: specialization revision', msg)
# suite-level
fresh(); restamp(); v, e = suite(); rec('clean-suite', v == 'FLOWMASTER_SUITE_PASS' and e == {}, (v, e))
for sk, rid in (('change-flow', 'R-OV-1'), ('session-relay-flowmaster', 'R-OV-2'), ('tw-flowmaster', 'R-OV-3')):
    fresh(); edit(sk + '/SKILL.md', lambda s: s.replace(T['OVERRIDE'], 'For every GCFPE stage.', 1)); restamp(); v, e = suite()
    rec(rid, v == 'FLOWMASTER_SUITE_FAIL' and e == {sk: ['missing specialization contract: ' + T['OVERRIDE']]}, e)
for sk, rid in (('session-relay-flowmaster', 'R-TOP-R'), ('tw-flowmaster', 'R-TOP-T')):
    fresh(); edit(sk + '/SKILL.md', lambda s: s.replace(' ' + T['A18'], '', 1)); restamp(); v, e = suite()
    rec(rid, e == {sk: ['missing specialization contract: ' + T['A18']]}, e)
F4 = ["same-session PR-35 handoff", "preferred live control plane", "launched as a new session", "The Product Owner's PR-40 invocation supplies merge approval"]
for sk, tag in (('session-relay-flowmaster', 'R'), ('tw-flowmaster', 'T')):
    for i, p in enumerate(F4, 1):
        fresh(); inject(sk + '/SKILL.md', p); restamp(); v, e = suite()
        rec(f'R-FB-{tag}{i}', e == {sk: ['superseded contract present: ' + p]}, e)
for sk, o, n, rid in (('session-relay-flowmaster', '3.1.0', '3.0.0', 'R-REV-R'), ('tw-flowmaster', '1.2.0', '1.1.6', 'R-REV-T')):
    fresh(); edit(sk + '/SKILL.md', lambda s, o=o, n=n: s.replace('_REVISION: ' + o, '_REVISION: ' + n, 1)); restamp(); v, e = suite()
    rec(rid, list(e) == [sk] and len(e[sk]) == 1, e)
shutil.rmtree(W, ignore_errors=True)
print(sum(ok for _, ok in res), 'of', len(res), 'exact')
