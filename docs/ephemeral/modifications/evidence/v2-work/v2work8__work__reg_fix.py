import sys, json, copy, subprocess, os
sys.dont_write_bytecode = True
M = '/tmp/claude-0/v2work8/M/flowmaster-validate'
S = M + '/fixtures/gcfpe-20260914.1-091426.1/scenarios.json'
base = open(S).read()
def run_with(mut):
    d = json.loads(base)
    mut(d)
    p = '/tmp/claude-0/v2work8/tmp/scen.json'; json.dump(d, open(p, 'w'))
    r = subprocess.run([sys.executable, M + '/scripts/run_gcfpe_20260914_fixtures.py', M + '/../change-flow', '--contract', M + '/../cand_contract.json', '--fixture', p], capture_output=True, text=True, env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1', 'TMPDIR': '/tmp/claude-0/v2work8/tmp'})
    out = json.loads(r.stdout)
    return sorted(x['name'] for x in out['cases'] if not x['passed']), [x.get('errors') for x in out['cases'] if x['name'] == 'section-13-fixture-document'][0]
def v(d, name): return [x for x in [r for r in d['scenarios'] if r['id'] == 'REPLAN-NEG-01'][0]['variants'] if x['name'] == name][0]
print('R-FX-1 label', run_with(lambda d: v(d, 'reject-routed-to-pr30').__setitem__('expected_rule', 'PR40_REJECT_REPLAN_PROCEED')))
print('R-FX-2 two defects', run_with(lambda d: v(d, 'reject-routed-to-pr30')['input'].__setitem__('second_proceed_same_plan', True)))
