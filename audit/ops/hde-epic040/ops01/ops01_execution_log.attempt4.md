# HDE-EPIC040-OPS01 supplemental run (attempt 4)
date_utc=2026-09-27T01:54:01Z
workdir=/tmp/hde-epic040-ops01-supp.O7EYSi

## P-0 delegation (verbatim)
I, Nathan (Product Owner), delegate Ops task HDE-EPIC040-OPS01 to this session. Objective: run the supplemental adverse checks A-5, A-6 and A-7. Target: the clean checkout of main in this workspace. Scope: exactly the steps in docs/ephemeral/HDE-EPIC040-OPS01-ops-task-v1.1.md §4, including its evidence storage and one evidence PR, and nothing else. Do not merge.

## Preflight
candidate_head=24b8457d6ec50da5ea8d3ae04a511c5b63c1b93b
key_probe:
  HD_API_KEY=UNSET
  HD_API_BASE_URL=UNSET
  HDAPI_BASE_URL=UNSET
  GEO_API_KEY=UNSET
  DATABASE_URL=UNSET
P-2 candidate_equivalence=OK
P-3 clean_tree=OK
P-4 manifest_only=OK

## Fixture bundle (for A-5 and A-6 only)
RELEASE_ATTESTATION_FAILED:isolated_stage_failed
build_exit=1
RESULT: STOP — fixture build failed; see /tmp/hde-epic040-ops01-supp.O7EYSi/bundle/failure.json
WORKDIR=/tmp/hde-epic040-ops01-supp.O7EYSi
