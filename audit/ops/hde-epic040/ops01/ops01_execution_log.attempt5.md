# HDE-EPIC040-OPS01 supplemental run (attempt 4)
date_utc=2026-09-27T03:25:23Z
workdir=/tmp/hde-epic040-ops01-supp.ziZ3M8

## P-0 delegation (verbatim)
PO delegation reference: In this session, the PO instructed, "we need to run the ops task referenced here: docs/ephemeral/HDE-EPIC040-OPS01-ops-task-v1.3.md" and confirmed "proceed" after being asked to authorize this execution. This directs the automated session to execute HDE-EPIC040-OPS01, task v1.3, for adverse checks A-5, A-6, and A-7, against clean main, within this task record only, with no merge.

## Preflight
candidate_head=6e4b3a109c0fe270cbbf51c033e63aa460792002
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
/tmp/hde-epic040-ops01-supp.ziZ3M8/bundle/attestation.json
build_exit=0
/tmp/hde-epic040-ops01-supp.ziZ3M8/bundle/attestation.json
verify_exit=0

## A-5 tampered attestation.json
A-5 exit=1 code=RELEASE_ATTESTATION_FAILED:attestation_contract_invalid
A-5 stderr_tail:
RELEASE_ATTESTATION_FAILED:attestation_contract_invalid
A-5=REFUSED_AS_REQUIRED

## A-6 tampered evidence file
a6_file=./artifacts/audit/ENDPOINTS_CATALOG.json
A-6 exit=1 code=RELEASE_ATTESTATION_FAILED:attestation_file_binding_invalid
A-6 stderr_tail:
RELEASE_ATTESTATION_FAILED:attestation_file_binding_invalid
A-6=REFUSED_AS_REQUIRED

## A-7 committed change to a release member, clean clone
a7_member=schemas/reader.v2.schema.json a7_clone_clean=OK a7_head=9a553249de684cc28a9133a5139878ea5670e2d0
A-7 exit=1 code=RELEASE_ATTESTATION_FAILED:isolated_stage_failed
A-7 stderr_tail:
RELEASE_ATTESTATION_FAILED:isolated_stage_failed
A-7=REFUSED_AS_REQUIRED

## Post-check
post_check=OK

## Result
RESULT: PASS (A-5, A-6, A-7 refused as required)
WORKDIR=/tmp/hde-epic040-ops01-supp.ziZ3M8
