# Integration summary — PR-03 (HDE-EPIC022)

## Regeneration commands
- env SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py
- env SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/orientation_demo.py

## Validation commands
- env SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/update_evidence_index.py --check
- env SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python tools/evidence/orientation_demo.py --check
- env SAFE_MODE=1 ALLOW_NETWORK=0 LC_ALL=C LANG=C TZ=UTC python ci/checks/check_mirror_schema.sh
