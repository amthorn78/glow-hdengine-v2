# HDE-EPIC027 d0_discovery Full Step Summary and Evidence Output

Generated at: 2026-03-17 UTC
Scope: CHECK d0_discovery only
Status: PASS

## 1) Steps taken

1. Prepared deterministic closed rails for the run.
- LC_ALL=C
- LANG=C
- TZ=UTC
- SAFE_MODE=1
- ALLOW_NETWORK=0
- APP_ENV=dev

2. Ensured canonical QA output directories existed under audit/qa/hde-epic027.
- checks/d0_discovery/
- 00_meta/

3. Created and wrote a governed first-line JSON header in primary log.
- File: audit/qa/hde-epic027/checks/d0_discovery/primary.log
- Header includes schema_version, timestamp_utc, check_id, check_name, status, fail_status, command, command_provenance, evidence_artifacts, captured_env, pf_refs, intended_tokens, claimed_tokens.

4. Captured discovery transcript and command outputs to primary log.
- pwd
- find audit/qa/hde-epic027 -maxdepth 3 -print
- bash ci/checks/check_env_pins.sh
- /workspaces/glow-hdengine-v2/.venv/bin/python -m engine.runtime.determinism_env --log-path audit/gates/determinism/env_pins.log --suite ci:determinism-rails --suite tests:invariance --suite tests:evidence-ordering --suite evidence:sampler --suite evidence:engine-core --suite orientation:demo --status success --check-log
- /workspaces/glow-hdengine-v2/.venv/bin/python scripts/hdctl.py --help

5. Created and upserted d0_discovery entry in step logs manifest.
- File: audit/qa/hde-epic027/qa_step_logs_manifest.json
- Entry includes check_id, check_name, status, fail_status, log_path, timestamp_utc.

6. Created and refreshed manifest sibling path proof.
- File: audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt
- Contains path, size_bytes, sha256, mtime_utc, produced_at_utc.

7. Created run-level doc delta ledger.
- File: audit/qa/hde-epic027/00_meta/doc_deltas.md

8. Finalized d0_discovery status to PASS.
- primary.log header status: PASS
- qa_step_logs_manifest d0_discovery status: PASS

9. Integrity verification performed for path proof against manifest bytes.
- path match: true
- size match: true
- sha256 match: true

## 2) Evidence files and full output

### 2.1 primary.log
Path: audit/qa/hde-epic027/checks/d0_discovery/primary.log

```text
{"captured_env":{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"check_id":"d0_discovery","check_name":"d0 - Discovery, current-state evidence bootstrap, and manifest bootstrap","claimed_tokens":[],"command":"/workspaces/glow-hdengine-v2/.venv/bin/python -m engine.runtime.determinism_env --log-path audit/gates/determinism/env_pins.log --suite ci:determinism-rails --suite tests:invariance --suite tests:evidence-ordering --suite evidence:sampler --suite evidence:engine-core --suite orientation:demo --status success --check-log","command_provenance":"Explicitly created","evidence_artifacts":["audit/qa/hde-epic027/checks/d0_discovery/primary.log","audit/qa/hde-epic027/qa_step_logs_manifest.json","audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt","audit/qa/hde-epic027/00_meta/doc_deltas.md"],"fail_status":"","intended_tokens":[],"pf_refs":["PF10 - HDE-Build Notes","PF05 - HDE-CLI-API-Vendor-Ref","PF02 - Canon-HDE-Core","PF27 - Canon Plan Templates"],"schema_version":"pf27.step_log_header.v1","status":"PASS","timestamp_utc":"2026-03-17T00:26:39Z"}
$ pwd
rc=0
stdout:
/workspaces/glow-hdengine-v2

$ find audit/qa/hde-epic027 -maxdepth 3 -print
rc=0
stdout:
audit/qa/hde-epic027
audit/qa/hde-epic027/qa_step_logs_manifest.json
audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt
audit/qa/hde-epic027/token_evidence_matrix.md
audit/qa/hde-epic027/r6 Live QA Plan HDE-EPIC027.md
audit/qa/hde-epic027/00_meta
audit/qa/hde-epic027/00_meta/doc_deltas.md
audit/qa/hde-epic027/acceptance_map_viability.log
audit/qa/hde-epic027/token_evidence_matrix.md.path_proof.txt
audit/qa/hde-epic027/acceptance_map_viability.log.path_proof.txt
audit/qa/hde-epic027/checks
audit/qa/hde-epic027/checks/gate_orientation_demo_check
audit/qa/hde-epic027/checks/gate_orientation_demo_check/stderr.log
audit/qa/hde-epic027/checks/gate_orientation_demo_check/stdout.log
audit/qa/hde-epic027/checks/gate_orientation_demo_check/command_used.txt
audit/qa/hde-epic027/checks/gate_orientation_demo_check/primary.log
audit/qa/hde-epic027/checks/gate_orientation_demo_check/rc.txt
audit/qa/hde-epic027/checks/gate_evidence_paths_validation
audit/qa/hde-epic027/checks/gate_evidence_paths_validation/stderr.log
audit/qa/hde-epic027/checks/gate_evidence_paths_validation/stdout.log
audit/qa/hde-epic027/checks/gate_evidence_paths_validation/command_used.txt
audit/qa/hde-epic027/checks/gate_evidence_paths_validation/primary.log
audit/qa/hde-epic027/checks/gate_evidence_paths_validation/rc.txt
audit/qa/hde-epic027/checks/d0_discovery
audit/qa/hde-epic027/checks/d0_discovery/primary.log
audit/qa/hde-epic027/checks/gate_update_evidence_index_write
audit/qa/hde-epic027/checks/gate_update_evidence_index_write/stderr.log
audit/qa/hde-epic027/checks/gate_update_evidence_index_write/stdout.log
audit/qa/hde-epic027/checks/gate_update_evidence_index_write/command_used.txt
audit/qa/hde-epic027/checks/gate_update_evidence_index_write/primary.log
audit/qa/hde-epic027/checks/gate_update_evidence_index_write/rc.txt
audit/qa/hde-epic027/checks/gate_orientation_demo_write
audit/qa/hde-epic027/checks/gate_orientation_demo_write/stderr.log
audit/qa/hde-epic027/checks/gate_orientation_demo_write/stdout.log
audit/qa/hde-epic027/checks/gate_orientation_demo_write/command_used.txt
audit/qa/hde-epic027/checks/gate_orientation_demo_write/primary.log
audit/qa/hde-epic027/checks/gate_orientation_demo_write/rc.txt
audit/qa/hde-epic027/checks/gate_lf_endings
audit/qa/hde-epic027/checks/gate_lf_endings/stderr.log
audit/qa/hde-epic027/checks/gate_lf_endings/stdout.log
audit/qa/hde-epic027/checks/gate_lf_endings/command_used.txt
audit/qa/hde-epic027/checks/gate_lf_endings/primary.log
audit/qa/hde-epic027/checks/gate_lf_endings/rc.txt
audit/qa/hde-epic027/checks/gate_mirror_schema
audit/qa/hde-epic027/checks/gate_mirror_schema/stderr.log
audit/qa/hde-epic027/checks/gate_mirror_schema/stdout.log
audit/qa/hde-epic027/checks/gate_mirror_schema/command_used.txt
audit/qa/hde-epic027/checks/gate_mirror_schema/primary.log
audit/qa/hde-epic027/checks/gate_mirror_schema/rc.txt
audit/qa/hde-epic027/checks/gate_update_evidence_index_check
audit/qa/hde-epic027/checks/gate_update_evidence_index_check/stderr.log
audit/qa/hde-epic027/checks/gate_update_evidence_index_check/stdout.log
audit/qa/hde-epic027/checks/gate_update_evidence_index_check/command_used.txt
audit/qa/hde-epic027/checks/gate_update_evidence_index_check/primary.log
audit/qa/hde-epic027/checks/gate_update_evidence_index_check/rc.txt

$ bash ci/checks/check_env_pins.sh
rc=0

$ /workspaces/glow-hdengine-v2/.venv/bin/python -m engine.runtime.determinism_env --log-path audit/gates/determinism/env_pins.log --suite ci:determinism-rails --suite tests:invariance --suite tests:evidence-ordering --suite evidence:sampler --suite evidence:engine-core --suite orientation:demo --status success --check-log
rc=0

$ /workspaces/glow-hdengine-v2/.venv/bin/python scripts/hdctl.py --help
rc=0
stdout:
usage: hdctl [-h] [--version]
             {showcompat,aux-preview,bg:resolve,dev:sampler} ...

Glow HD Engine compatibility CLI

positional arguments:
  {showcompat,aux-preview,bg:resolve,dev:sampler}
    showcompat          Emit canonical Reader v1 bytes from vendor JSON (stdin
                        or files)
    aux-preview         Preview Aux narrative text for a public tuple
    bg:resolve          Resolve BodyGraphs from db/vendor sources (Phase S8a
                        stub)
    dev:sampler         DEV/ADMIN ONLY: deterministic sampler harness
                        (seedable)

options:
  -h, --help            show this help message and exit
  --version             show program version and exit
```

### 2.2 qa_step_logs_manifest.json
Path: audit/qa/hde-epic027/qa_step_logs_manifest.json

```json
{"d0_discovery":{"check_id":"d0_discovery","check_name":"d0 - Discovery, current-state evidence bootstrap, and manifest bootstrap","fail_status":"","log_path":"checks/d0_discovery/primary.log","status":"PASS","timestamp_utc":"2026-03-17T00:26:39Z"}}
```

### 2.3 qa_step_logs_manifest.json.path_proof.txt
Path: audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt

```text
path: audit/qa/hde-epic027/qa_step_logs_manifest.json
size_bytes: 250
sha256: 2080fcfcbccd76e60b8887a824f8c95b179e58e31ceed2d04ee00bcc999e23af
mtime_utc: 2026-03-16T22:17:30Z
produced_at_utc: 2026-03-17T00:26:39Z
```

### 2.4 doc_deltas.md
Path: audit/qa/hde-epic027/00_meta/doc_deltas.md

```markdown
# EPIC027 Doc Deltas

- 2026-03-16: d0_discovery bootstrap initialized QA root and step-log manifest artifacts.
```

## 3) Final outcome

- d0_discovery check status: PASS
- Manifest entry for d0_discovery: present and PASS
- Manifest path proof: present and verified against current manifest bytes
- All required d0 deliverables: present
