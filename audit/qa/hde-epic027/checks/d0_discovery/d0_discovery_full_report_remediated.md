# HDE-EPIC027 d0_discovery Single-File Session Report

Generated at (UTC): 2026-03-17T03:08:20Z
Scope: CHECK d0_discovery only
Result: PASS

## 1) Full Session Steps Taken (Chronological)

1. Reviewed EPIC027 plan and repo state for d0_discovery requirements and governed artifact targets.
2. Bootstrapped d0_discovery evidence under closed rails and captured the execution transcript in primary.log.
3. Generated the d0 step manifest entry at audit/qa/hde-epic027/qa_step_logs_manifest.json.
4. Generated the manifest sibling proof at audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt.
5. Added d0 bootstrap note in audit/qa/hde-epic027/00_meta/doc_deltas.md.
6. Corrected initial status handling so d0_discovery recorded PASS in governed artifacts.
7. Produced an initial single-file summary report for user review.
8. Applied PF27 trust remediation for primary.log header provenance fields.
9. Updated command_provenance to allowed canonical value: Explicitly created.
10. Remediated command to preserve the full ordered multi-command sequence used for d0 capture.
11. Refreshed qa_step_logs_manifest.json from the governed primary header.
12. Regenerated qa_step_logs_manifest.json.path_proof.txt after manifest refresh.
13. Re-read all d0 evidence artifacts to validate consistency.
14. Synced this report so embedded evidence outputs match current on-disk artifacts.
15. Re-verified d0 evidence set completeness and full-output inclusion.

## 2) Full Output: d0 Evidence Files

### 2.1 audit/qa/hde-epic027/checks/d0_discovery/primary.log

```text
{"captured_env":{"ALLOW_NETWORK":"0","APP_ENV":"dev","LANG":"C","LC_ALL":"C","SAFE_MODE":"1","TZ":"UTC"},"check_id":"d0_discovery","check_name":"d0 - Discovery, current-state evidence bootstrap, and manifest bootstrap","claimed_tokens":[],"command":"pwd; find audit/qa/hde-epic027 -maxdepth 3 -print; bash ci/checks/check_env_pins.sh; /workspaces/glow-hdengine-v2/.venv/bin/python -m engine.runtime.determinism_env --log-path audit/gates/determinism/env_pins.log --suite ci:determinism-rails --suite tests:invariance --suite tests:evidence-ordering --suite evidence:sampler --suite evidence:engine-core --suite orientation:demo --status success --check-log; /workspaces/glow-hdengine-v2/.venv/bin/python scripts/hdctl.py --help","command_provenance":"Explicitly created","evidence_artifacts":["audit/qa/hde-epic027/checks/d0_discovery/primary.log","audit/qa/hde-epic027/qa_step_logs_manifest.json","audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt","audit/qa/hde-epic027/00_meta/doc_deltas.md"],"fail_status":"","intended_tokens":[],"pf_refs":["PF10 - HDE-Build Notes","PF05 - HDE-CLI-API-Vendor-Ref","PF02 - Canon-HDE-Core","PF27 - Canon Plan Templates"],"schema_version":"pf27.step_log_header.v1","status":"PASS","timestamp_utc":"2026-03-17T03:01:30Z"}
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

### 2.2 audit/qa/hde-epic027/qa_step_logs_manifest.json

```json
{"d0_discovery":{"check_id":"d0_discovery","check_name":"d0 - Discovery, current-state evidence bootstrap, and manifest bootstrap","fail_status":"","log_path":"checks/d0_discovery/primary.log","status":"PASS","timestamp_utc":"2026-03-17T03:01:30Z"}}
```

### 2.3 audit/qa/hde-epic027/qa_step_logs_manifest.json.path_proof.txt

```text
path: audit/qa/hde-epic027/qa_step_logs_manifest.json
size_bytes: 250
sha256: 744f0679f5defe247e5acbcdaa66e230f0dbbd06c00b74bec498e98edea1d19c
mtime_utc: 2026-03-16T22:17:30Z
produced_at_utc: 2026-03-17T03:01:30Z
```

### 2.4 audit/qa/hde-epic027/00_meta/doc_deltas.md

```markdown
# EPIC027 Doc Deltas

- 2026-03-16: d0_discovery bootstrap initialized QA root and step-log manifest artifacts.
```

## 3) Completeness Check

- Included full current output of primary.log: YES
- Included full current output of qa_step_logs_manifest.json: YES
- Included full current output of qa_step_logs_manifest.json.path_proof.txt: YES
- Included full current output of doc_deltas.md: YES
- Single-file delivery for d0 session: YES
