import json, shutil, subprocess, sys, os, re
sys.dont_write_bytecode = True
from pathlib import Path
sys.path.insert(0, '/tmp/claude-0/spec/s8a/work')
from allfail import failures
from texts import T
BASE = Path('/tmp/claude-0/v2work8/A'); REG = Path('/tmp/claude-0/v2work8/reg')
OLD27 = (Path('/tmp/claude-0/v2work8/base') / 'glow-hde-pr-development/SKILL.md').read_text().split('\n')[26]
S = 'glow-hde-pr-development/SKILL.md'; B = 'glow-hde-pr-development/references/behavior-cases.md'
def inject(t, s): return t + '\n' + s + '\n'
def delete(t, s):
    assert t.count(s) == 1, (t.count(s), s[:60]); return t.replace(s, '')
def replace(t, a, b):
    assert t.count(a) == 1, (t.count(a), a[:60]); return t.replace(a, b)
F = 'FAIL: forbidden or unfinished content present: '
cases = [
 ('R-rev', S, lambda t: replace(t, 'REVISION: 1.3.0', 'REVISION: 1.2.5'), 'FAIL: missing revision contract', 1),
 ('R-32', S, lambda t: inject(t, 'Remain in the one dedicated PR-development session across both phases.'), F + 'one dedicated PR-development session', 1),
 ('R-37', S, lambda t: inject(t, T['V5'] + '.'), F + T['V5'], 2),
 ('R-38', S, lambda t: inject(t, 'followed by exactly one complete same-session `PR-35` handoff.'), F + 'same-session `PR-35` handoff', 1),
 ('R-44', S, lambda t: inject(t, 'Continue in the same dedicated PR session until all applicable predicates are true:'), F + 'Continue in the same dedicated PR session until all applicable predicates are true', 1),
 ('R-55', S, lambda t: inject(t, T['TEN'] + '.'), F + T['TEN'], 2),
 ('R-63', S, lambda t: inject(t, 'Resume the recorded phase in the same dedicated PR session, workspace/worktree, branch, open PR, current evidence and original Product Owner Proceed.'), F + 'same dedicated PR session, workspace/worktree, branch, open PR', 1),
 ('R-C6-27', S, lambda t: inject(t, OLD27), F + 'followed in the same session by PR-35', 1),
 ('R-OLDLIST', B, lambda t: inject(t, 'PR-35 returns only `MERGE_PENDING`, `RESCOPE_PENDING`, `RECOVERY_PENDING`, `REMOTE_EVIDENCE_PENDING`, or `PRODUCT_OWNER_DECISION_REQUIRED`.'), F + '`MERGE_PENDING`, `RESCOPE_PENDING`', 1),
 ('R-TENFIELD', S, lambda t: inject(t, 'The work unit keeps exactly one branch and one pull request, which the ten-field continuity list requires.'), F + 'ten-field', 1),
 ('R-CART', S, lambda t: delete(t, T['C-ART']), 'FAIL: missing artifact holds results contract', 1),
 ('R-CDEC', S, lambda t: delete(t, T['C-DEC']), 'FAIL: missing in-flight decisions contract', 1),
 ('R-CLAT', S, lambda t: delete(t, '**Decide it during work:**'), 'FAIL: missing material latitude contract', 1),
 ('R-CPROC', S, lambda t: delete(t, T['C-PROCEED']), 'FAIL: missing one Proceed per plan contract', 1),
 ('R-TOP', S, lambda t: delete(t, T['A18']), 'FAIL: missing top-level PR-35 session contract', 1),
 ('R-SUB', S, lambda t: delete(t, 'Subscribing is not polling, and it creates no session.'), 'FAIL: missing subscription is not polling contract', 1),
 ('R-DISP', S, lambda t: delete(t, ' No agent merges, and no session is created by an agent.'), 'FAIL: missing no agent-created session contract', 1),
 ('R-NOBRANCH', S, lambda t: delete(t, 'It carries no branch and no commit: '), 'FAIL: missing handoff carries no branch contract', 1),
 ('R-heading', B, lambda t: replace(t, '## PR-40 rejection re-plan', '## PR-40 rejection'), 'FAIL: missing behavior case: ## PR-40 rejection re-plan', 1),
 ('R-H-DEC', B, lambda t: replace(t, '## In-flight decisions', '## In-flight'), 'FAIL: missing behavior case: ## In-flight decisions', 1),
 ('R-H-LAT', B, lambda t: replace(t, '## Implementor latitude', '## Latitude'), 'FAIL: missing behavior case: ## Implementor latitude', 1),
 ('R-H-SUB', B, lambda t: replace(t, '## Pull request subscription', '## Subscription'), 'FAIL: missing behavior case: ## Pull request subscription', 1),
 ('R-H-OBS', B, lambda t: replace(t, '## Observed merge', '## Merge observed'), 'FAIL: missing behavior case: ## Observed merge', 1),
]
ok = True
for name, rel, mut, expected, count in cases:
    d = REG / name
    if d.exists(): shutil.rmtree(d)
    shutil.copytree(BASE / 'glow-hde-pr-development', d / 'glow-hde-pr-development')
    p = d / rel; p.write_text(mut(p.read_text(encoding='utf-8')), encoding='utf-8')
    r = subprocess.run([sys.executable, str(d / 'glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py')], capture_output=True, text=True, env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'})
    out = r.stdout.strip(); af = failures(d)
    exact = out == expected and r.returncode == 1 and len(af) == count and ('FAIL: ' + expected[6:]) in {'FAIL: ' + a for a in af}
    ok &= exact
    print(('OK  ' if exact else 'BAD ') + name, r.returncode, out[:110], '| all:', len(af), sorted(a[:60] for a in af) if len(af) > 1 else '')
    shutil.rmtree(d)
print('ALL_EXACT', ok)
# amthor
AB = BASE / 'amthor-workspace-governance-audit'
def rep(a, b):
    def f(t):
        assert t.count(a) == 1, (t.count(a), a[:50]); return t.replace(a, b)
    return f
acases = [
 ('A-skill-list', 'SKILL.md', rep(T['NINE'], T['TEN']), 'test_exact_gcf17_continuity_parity'),
 ('A-interop-list', 'references/interoperability-contracts.md', rep(T['NINE'], T['TEN']), 'test_exact_gcf17_continuity_parity'),
 ('A-fixtures-list', 'references/behavioral-fixtures.md', rep(T['NINE'], T['TEN']), 'test_exact_gcf17_continuity_parity'),
 ('A-rev', 'SKILL.md', rep('REVISION:** 1.12.0', 'REVISION:** 1.11.3'), 'test_exact_gcf17_continuity_parity'),
 ('A-handoff-kept', 'SKILL.md', rep('exactly one fenced `text` `NEXT_PROMPT_HANDOFF` block', 'one fenced `text` `NEXT_PROMPT_HANDOFF` block'), 'test_exact_fenced_text_handoff_parity'),
 ('A-inject-skill', 'SKILL.md', lambda t: t + '\n- ' + T['TEN'] + '.\n', 'test_exact_gcf17_continuity_parity'),
 ('A-inject-interop', 'references/interoperability-contracts.md', lambda t: t + '\n' + T['TEN'] + '.\n', 'test_exact_gcf17_continuity_parity'),
 ('A-inject-fixtures', 'references/behavioral-fixtures.md', lambda t: t + '\n- ' + T['TEN'] + '.\n', 'test_exact_gcf17_continuity_parity'),
]
tmp = Path('/tmp/claude-0/v2work8/tmp')
for name, rel, mut, want in acases:
    d = REG / name
    if d.exists(): shutil.rmtree(d)
    shutil.copytree(AB, d)
    p = d / rel; p.write_text(mut(p.read_text(encoding='utf-8')), encoding='utf-8')
    r = subprocess.run([sys.executable, 'run_fixture_suite.py'], cwd=d / 'scripts', capture_output=True, text=True, env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1', 'TMPDIR': str(tmp)})
    fails = re.findall(r'^(?:FAIL|ERROR): (\S+) \((\S+)\)', r.stderr, re.M)
    last = [l for l in r.stderr.strip().split('\n') if l.startswith(('OK', 'FAILED', 'Ran'))]
    good = [f[0] for f in fails] == [want] and 'FAILED (failures=1)' in last
    print(('OK  ' if good else 'BAD ') + name, fails, last)
    shutil.rmtree(d)
