# Full Session Action Log and Evidence Output (Version 1)

## Session Header
- Epic: HDE-EPIC032 (Fermentation Pass 3)
- Steps in scope: PO-013, PO-014, PO-015
- Session objective: execute the approved QA checks under closed rails and capture consolidated evidence outputs in a single report
- Approved-plan posture applied: PF10 (current), PF05, PF02
- Environment posture used for check execution: SAFE_MODE=1, ALLOW_NETWORK=0, APP_ENV=dev, LC_ALL=C, LANG=C, TZ=UTC
- Capture window (UTC): 2026-05-23T03:11:29Z to 2026-05-23T03:11:47Z
- Report generated: 2026-05-23T03:11:47Z

## Canonical Status Snapshot
- PO-013 result status: PASS
- PO-014 result status: PASS
- PO-015 result status: PASS
- Tooling-blocked state encountered: none
- Fail-tooling state encountered: none
- Fail-behavior state encountered: none

## Complete Action Log (Chronological)

### Phase 1: PO-013 preflight and execution
1. Verified required preflight loci exist:
- audit/qa/hde-epic032/00_meta/live_qa_harness.py
- docs/evidence/INDEX.json
- docs/evidence/INDEX.sha256
- artifacts/evidence_index.jsonl
- artifacts/evidence_index.jsonl.sha256
- tools/evidence/update_evidence_index.py
- tools/evidence/validate_evidence_paths.py

2. Executed harness for PO-013 under closed deterministic rails.
- Command:

```bash
export SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC
/usr/bin/python3 audit/qa/hde-epic032/00_meta/live_qa_harness.py po-013
```

- Process outcome: shell exit code 0.
- Runtime note: DeprecationWarning emitted by datetime.utcnow() usage in harness, non-fatal.

3. Validated PO-013 deliverables and outcome payload.
- Deliverables present:
  - audit/qa/hde-epic032/checks/po-013/primary.log
  - audit/qa/hde-epic032/checks/po-013/primary.log.path_proof.txt
  - audit/qa/hde-epic032/checks/po-013/result.json
- Result assertions from result.json:
  - status PASS
  - human_index_present true
  - machine_mirror_present true
  - commands return codes:
    - tools/evidence/update_evidence_index.py --check: 0
    - tools/evidence/validate_evidence_paths.py: 0
  - required_missing: []

### Phase 2: PO-014 preflight and execution
4. Verified required preflight loci exist:
- audit/qa/hde-epic032/00_meta/live_qa_harness.py
- docs/evidence/INDEX.json
- artifacts/evidence_index.jsonl
- artifacts/evidence_index.jsonl.sha256
- ci/checks/check_mirror_schema.sh
- tools/evidence/validate_evidence_paths.py

5. Executed harness for PO-014 under closed deterministic rails.
- Command:

```bash
export SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC
/usr/bin/python3 audit/qa/hde-epic032/00_meta/live_qa_harness.py po-014
```

- Process outcome: shell exit code 0.
- Runtime note: DeprecationWarning emitted by datetime.utcnow() usage in harness, non-fatal.

6. Validated PO-014 deliverables and outcome payload.
- Deliverables present:
  - audit/qa/hde-epic032/checks/po-014/primary.log
  - audit/qa/hde-epic032/checks/po-014/primary.log.path_proof.txt
  - audit/qa/hde-epic032/checks/po-014/result.json
- Result assertions from result.json:
  - status PASS
  - human_machine_loci_present true
  - commands return codes:
    - ci/checks/check_mirror_schema.sh: 0
    - tools/evidence/validate_evidence_paths.py: 0
  - required_missing: []

### Phase 3: PO-015 preflight and execution
7. Verified required preflight loci exist:
- audit/qa/hde-epic032/00_meta/live_qa_harness.py
- tools/evidence/generate_narrative_registry_diff.py
- tools/evidence/generate_db_bridge_parity.py
- tools/evidence/update_evidence_index.py
- tools/evidence/validate_evidence_paths.py
- tools/evidence/check_lf_endings.py
- ci/checks/check_evidence_index_hash.sh
- ci/checks/check_mirror_schema.sh

8. Executed harness for PO-015 under closed deterministic rails.
- Command:

```bash
export SAFE_MODE=1 ALLOW_NETWORK=0 APP_ENV=dev LC_ALL=C LANG=C TZ=UTC
/usr/bin/python3 audit/qa/hde-epic032/00_meta/live_qa_harness.py po-015
```

- Process outcome: shell exit code 0.
- Runtime note: DeprecationWarning emitted by datetime.utcnow() usage in harness, non-fatal.

9. Validated PO-015 deliverables and outcome payload.
- Deliverables present:
  - audit/qa/hde-epic032/checks/po-015/primary.log
  - audit/qa/hde-epic032/checks/po-015/primary.log.path_proof.txt
  - audit/qa/hde-epic032/checks/po-015/result.json
- Result assertions from result.json:
  - status PASS
  - all_commands_green true
  - commands return codes:
    - tools/evidence/generate_narrative_registry_diff.py --check: 0
    - tools/evidence/generate_db_bridge_parity.py --check: 0
    - tools/evidence/update_evidence_index.py --check: 0
    - tools/evidence/validate_evidence_paths.py: 0
    - ci/checks/check_evidence_index_hash.sh: 0
    - ci/checks/check_mirror_schema.sh: 0
    - tools/evidence/check_lf_endings.py: 0
  - required_missing: []

## Per-Step Evidence and Disposition

### PO-013
- Result file: audit/qa/hde-epic032/checks/po-013/result.json
- Status: PASS
- checked_at_utc: 2026-05-23T03:11:29Z
- required_missing: []

### PO-014
- Result file: audit/qa/hde-epic032/checks/po-014/result.json
- Status: PASS
- checked_at_utc: 2026-05-23T03:11:46Z
- required_missing: []

### PO-015
- Result file: audit/qa/hde-epic032/checks/po-015/result.json
- Status: PASS
- checked_at_utc: 2026-05-23T03:11:47Z
- required_missing: []

## Manifest and Header Trust Proof (Remediation)

### Per-Epic Manifest Presence and Integrity
- Manifest path: audit/qa/hde-epic032/qa_step_logs_manifest.json
- Manifest path-proof: audit/qa/hde-epic032/qa_step_logs_manifest.json.path_proof.txt
- Manifest size/hash: 3791 bytes, dafe686c7ec3b914a3c210ee95e22bd773893584b4583ef99d18ab16304b7a37
- Manifest path-proof size/hash: 214 bytes, c761a7cf90468d6b635faeafeab5e7387e980ba694e7499213acd137c4ffe2cb

### Manifest Entries for Executed Checks
- po-013 entry:
  - check_id: po-013
  - status: PASS
  - updated_at_utc: 2026-05-23T03:11:29Z
  - log_path: audit/qa/hde-epic032/checks/po-013/primary.log
  - log_path_proof: audit/qa/hde-epic032/checks/po-013/primary.log.path_proof.txt
- po-014 entry:
  - check_id: po-014
  - status: PASS
  - updated_at_utc: 2026-05-23T03:11:46Z
  - log_path: audit/qa/hde-epic032/checks/po-014/primary.log
  - log_path_proof: audit/qa/hde-epic032/checks/po-014/primary.log.path_proof.txt
- po-015 entry:
  - check_id: po-015
  - status: PASS
  - updated_at_utc: 2026-05-23T03:11:47Z
  - log_path: audit/qa/hde-epic032/checks/po-015/primary.log
  - log_path_proof: audit/qa/hde-epic032/checks/po-015/primary.log.path_proof.txt

### Primary Header Field Proof by Check
- PO-013 primary header proof (from first JSON line in primary.log):
  - captured_env: {SAFE_MODE: "1", ALLOW_NETWORK: "0", APP_ENV: "dev", LC_ALL: "C", LANG: "C", TZ: "UTC"}
  - evidence_artifacts includes:
    - audit/qa/hde-epic032/checks/po-013/primary.log
    - audit/qa/hde-epic032/checks/po-013/primary.log.path_proof.txt
    - audit/qa/hde-epic032/checks/po-013/result.json
  - intended_tokens: []
  - claimed_tokens: []
- PO-014 primary header proof (from first JSON line in primary.log):
  - captured_env: {SAFE_MODE: "1", ALLOW_NETWORK: "0", APP_ENV: "dev", LC_ALL: "C", LANG: "C", TZ: "UTC"}
  - evidence_artifacts includes:
    - audit/qa/hde-epic032/checks/po-014/primary.log
    - audit/qa/hde-epic032/checks/po-014/primary.log.path_proof.txt
    - audit/qa/hde-epic032/checks/po-014/result.json
  - intended_tokens: []
  - claimed_tokens: []
- PO-015 primary header proof (from first JSON line in primary.log):
  - captured_env: {SAFE_MODE: "1", ALLOW_NETWORK: "0", APP_ENV: "dev", LC_ALL: "C", LANG: "C", TZ: "UTC"}
  - evidence_artifacts includes:
    - audit/qa/hde-epic032/checks/po-015/primary.log
    - audit/qa/hde-epic032/checks/po-015/primary.log.path_proof.txt
    - audit/qa/hde-epic032/checks/po-015/result.json
  - intended_tokens: []
  - claimed_tokens: []

## Deliverables Checklist
- PO-013
  - audit/qa/hde-epic032/checks/po-013/primary.log present
  - audit/qa/hde-epic032/checks/po-013/primary.log.path_proof.txt present
  - audit/qa/hde-epic032/checks/po-013/result.json present
- PO-014
  - audit/qa/hde-epic032/checks/po-014/primary.log present
  - audit/qa/hde-epic032/checks/po-014/primary.log.path_proof.txt present
  - audit/qa/hde-epic032/checks/po-014/result.json present
- PO-015
  - audit/qa/hde-epic032/checks/po-015/primary.log present
  - audit/qa/hde-epic032/checks/po-015/primary.log.path_proof.txt present
  - audit/qa/hde-epic032/checks/po-015/result.json present
- Epic-level
  - audit/qa/hde-epic032/qa_step_logs_manifest.json present
  - audit/qa/hde-epic032/qa_step_logs_manifest.json.path_proof.txt present

## Evidence Output Inventory (Hashes)

| Path | Size (bytes) | SHA256 |
|---|---:|---|
| audit/qa/hde-epic032/checks/po-013/result.json | 833 | 5785decb4811d3997edb9289137457caba240d4ef40f3e6a091e31a6ae6ee97d |
| audit/qa/hde-epic032/checks/po-013/primary.log | 1586 | cd5b00148d53736545003db1950109bb3d6d378caebce40a249a3405126bcaa2 |
| audit/qa/hde-epic032/checks/po-013/primary.log.path_proof.txt | 213 | 1a33c1a5067a0a16d29eae1693f6bb16d50409029998a178cf26078244974320 |
| audit/qa/hde-epic032/checks/po-014/result.json | 701 | 0730424f5457b7a23ca8a14163fb801323c9ef413ab94789de2d79891bbaad54 |
| audit/qa/hde-epic032/checks/po-014/primary.log | 1454 | 6b9349d4d1de6acbd463338adabd6971c1ae87df5235bd4c7e0a3b452add008b |
| audit/qa/hde-epic032/checks/po-014/primary.log.path_proof.txt | 213 | 524f8899893b850602a8a8665b4530f1ed6dd35012b31b576c839df66e89f81f |
| audit/qa/hde-epic032/checks/po-015/result.json | 1711 | c68566f5196a57c931390856cb232c88efe3070f3ee5683e07ba69bf482fd8df |
| audit/qa/hde-epic032/checks/po-015/primary.log | 2464 | e4920e563d0393782b29bf766d34e716dc866e5d741f9e2b38cd7349edecd321 |
| audit/qa/hde-epic032/checks/po-015/primary.log.path_proof.txt | 213 | e94c8fe74e21e872b84c8fdd29ba449a364f73918760a4a6109dded3a1a2f937 |
| audit/qa/hde-epic032/qa_step_logs_manifest.json | 3791 | dafe686c7ec3b914a3c210ee95e22bd773893584b4583ef99d18ab16304b7a37 |
| audit/qa/hde-epic032/qa_step_logs_manifest.json.path_proof.txt | 214 | c761a7cf90468d6b635faeafeab5e7387e980ba694e7499213acd137c4ffe2cb |

## Command Families Executed in This Session
- Preflight existence checks using test -f for required plan loci per step.
- Harness execution under closed deterministic rails:
  - /usr/bin/python3 audit/qa/hde-epic032/00_meta/live_qa_harness.py po-013
  - /usr/bin/python3 audit/qa/hde-epic032/00_meta/live_qa_harness.py po-014
  - /usr/bin/python3 audit/qa/hde-epic032/00_meta/live_qa_harness.py po-015
- Post-run evidence verification:
  - file-presence checks for each deliverable
  - result payload inspection for command return codes and step status
  - deterministic inventory capture with stat and sha256sum
  - manifest entry extraction for po-013, po-014, po-015 from qa_step_logs_manifest.json
  - primary header extraction (first JSON line) from each check primary.log to prove captured_env, evidence_artifacts, intended_tokens, and claimed_tokens

## Final Session Disposition
- All in-scope checks (PO-013, PO-014, PO-015) are PASS in current governed artifacts.
- Required deliverables for each step are present, including primary logs, path-proof sidecars, and result payloads.
- This file is the consolidated single-file detailed action log and evidence output for this session.
