#!/usr/bin/env python3
"""Fail if active source reintroduces database bridge transport."""
from __future__ import annotations
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
EXCLUDE=('audit/','artifacts/','docs/crd/','docs/plans/','docs/pfcanon/','docs/design/','docs/adr/','handoff/','tests/','CHANGELOG.md','AGENTS.md','codex/out/','notes/')
BAD=('BridgeProvider','BridgeUnavailable','BridgeUnsupported','bridge_factory','generate_db_bridge_parity','check_bridge_consistency','hde_epic038_ops01r','hde_epic038_ops01_v5')
ALLOW_FILES={'ci/checks/check_direct_db_contract.py'}
ALLOW_RETIRED={'engine/db/adapter.py','adapter/db_access.py','tools/evidence/generate_hde_epic038_direct_db_selection.py','scripts/ops/hde_epic038_ops03.py','tools/evidence/hde_epic038_ops03.py','docs/ADAPTER_DB.md','docs/SECRETS.md','scripts/db/capture_epic011_posture.py','scripts/ops/capture_rails_open_scope.py','tools/evidence/generate_architecture_snapshot.py','tools/evidence/generate_env_matrix_snapshot.py','tools/evidence/retained_evidence_safety.py','tools/evidence/run_sanity_pipeline.py','ci/checks/check_direct_db_contract.py'}
def active(p):
 s=p.relative_to(ROOT).as_posix()
 return not any(s.startswith(x) for x in EXCLUDE) and p.is_file() and p.suffix in {'.py','.md','.yml','.yaml','.sh','.txt'}
def main():
 violations=[]
 for p in ROOT.rglob('*'):
  rel=p.relative_to(ROOT).as_posix()
  if not active(p): continue
  text=p.read_text(errors='ignore')
  if rel not in ALLOW_FILES:
   for bad in BAD:
    if bad in text: violations.append(f'{rel}:{bad}')
  for key in ('DB_BRIDGE_URL','DB_FORCE_BRIDGE','DB_ALLOW_BRIDGE_IN_PROD'):
   if key in text and rel not in ALLOW_RETIRED and not rel.startswith('tests/'):
    violations.append(f'{rel}:{key}')
 if violations:
  print('\n'.join(sorted(violations))); return 1
 print('DIRECT_DB_CONTRACT_OK'); return 0
if __name__=='__main__': raise SystemExit(main())
