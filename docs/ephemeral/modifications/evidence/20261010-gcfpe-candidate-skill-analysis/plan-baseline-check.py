"""Read-only PLAN baseline receipts; never a repaired-candidate qualification gate.

Run from the repository root. No native prompt input, body persistence or network.
This script writes only its concise receipt beside itself.
"""
import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
INPUTS = Path('/workspace/scratch/fa82d6934864/skill-review-inputs')
UPLOAD = Path('/workspace/scratch/fa82d6934864/upload')
CONTROL = Path('docs/prompt_ecosystem_management')
RECORD = Path('docs/ephemeral/modifications/MODIFICATION-20261010-gcfpe-candidate-skill-analysis.md')
env = {**os.environ, 'PYTHONDONTWRITEBYTECODE': '1', 'SAFE_MODE': '1', 'ALLOW_NETWORK': '0'}


def run(argv):
    completed = subprocess.run([str(x) for x in argv], cwd=REPO, env=env,
                               text=True, capture_output=True, timeout=90)
    result = {'argv': [str(x) for x in argv], 'exit_code': completed.returncode}
    try:
        obj = json.loads(completed.stdout)
        # Retain top-level scalar flags and diagnostics; never summarize false as true.
        result['top_level_keys'] = list(obj) if isinstance(obj, dict) else None
        if isinstance(obj, dict):
            result['receipt'] = {k: v for k, v in obj.items()
                                 if not isinstance(v, (dict, list)) or
                                 k in ('errors', 'warnings', 'prompt_bodies_validated',
                                       'prompt_body_checks_not_evaluated', 'missing_expected_skills', 'findings', 'finding_counts')}
        else:
            result['receipt'] = obj
        result['stdout_kind'] = 'selected top-level JSON fields; not complete raw stdout'
    except json.JSONDecodeError:
        result['stdout'] = completed.stdout
        result['stdout_kind'] = 'complete text stdout'
    result['stderr'] = completed.stderr
    return result


receipts = []
identities = []
for line in (HERE / 'source-identities.md').read_text().splitlines():
    if not line.startswith('| ') or '.skill |' not in line:
        continue
    cols = [v.strip() for v in line.split('|')[1:-1]]
    name = cols[0].removesuffix('.skill')
    receipt = run(['python', '-B', CONTROL / 'freeze.py', INPUTS / name])
    observed = receipt.get('stdout', '').strip()
    archive = UPLOAD / (name + '.skill')
    archive_sha = hashlib.sha256(archive.read_bytes()).hexdigest()
    identities.append({'skill': name, 'expected_freeze': cols[5],
                       'observed_freeze': observed, 'freeze_matches': observed == cols[5],
                       'archive_sha256': archive_sha, 'archive_matches': archive_sha == cols[4]})
    receipts.append(receipt)

jobs = [
    ['python', '-B', CONTROL / 'modification_validate.py', RECORD],
    ['git', 'diff', '--check'],
    ['python', '-B', INPUTS / 'change-flow/scripts/validate_gcfpe_20260914.py'],
    ['python', '-B', INPUTS / 'glow-hde-pr-development/scripts/validate_glow_hde_pr_development.py'],
    ['python', '-B', INPUTS / 'flowmaster-validate/scripts/validate_gcfpe_20260914.py',
     INPUTS / 'change-flow', '--contract',
     INPUTS / 'change-flow/references/gcfpe-20260914.1-091426.1-direct-handoff-contract.json'],
    ['python', '-B', INPUTS / 'flowmaster-validate/scripts/validate_flowmaster.py',
     '--skills-root', INPUTS, '--strict-warnings'],
]
receipts.extend(run(job) for job in jobs)
parts = REPO / 'docs/ephemeral/modifications/evidence/20261009-gcfpe-latest-alpha-analysis/execute/candidate-graph-parts'
rs = json.loads((parts / 'prompts/RS-20.json').read_text())
global_part = json.loads((parts / 'global.json').read_text())
graph = {'candidate_prompt_count': len(list((parts / 'prompts').glob('*.json'))),
         'rs20_has_pr20_edge': any(edge['to'] == 'PR-20' for edge in rs['edges']),
         'producer_allocates_pf10_number': global_part['pf10_addendum_contract']['producer_allocates_pf10_number'],
         'interpretation': 'Observed unrepaired baseline, not a passing repair gate.'}
missing = [name for name in ('glow-graph-contract', 'session-relay-flowmaster', 'tw-flowmaster',
                             'session-branch-flowmaster', 'amthor-workspace-governance-audit')
           if not (INPUTS / name / 'SKILL.md').exists()]
output = {'date_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'mode': 'PLAN', 'outcome': 'INCOMPLETE_DRY_RUN_PRE_REVIEW_STOP',
          'all_baseline_identities_match': all(x['freeze_matches'] and x['archive_matches'] for x in identities),
          'source_identities': identities, 'command_receipts': receipts, 'candidate_baseline': graph,
          'missing_from_supplied_input_root': missing,
          'not_run': ['shipped candidate graph/registry derivation', 'implemented six-repair guard fixtures',
                      'governed packaging/extracted repaired gates', 'D24 package review',
                      'formal PLAN FULL review', 'any runtime QA/Ops or skill installation'],
          'limits': ['Commands run against unchanged supplied inputs.',
                     'Missing intended companions were not replaced with old installed copies.',
                     'Historical fixture results are reused from ANALYZE, not recounted as new coverage.',
                     'Native page checks are separate in plan-source-checks.json.',
                     'No prompt body was supplied, copied, hashed or saved.']}
(HERE / 'plan-dry-run.json').write_text(json.dumps(output, indent=2) + '\n')
print(json.dumps({'outcome': output['outcome'], 'all_identities_match': output['all_baseline_identities_match'],
                  'command_exit_codes': [x['exit_code'] for x in receipts],
                  'missing_inputs': missing, 'candidate_baseline': graph}, indent=2))
