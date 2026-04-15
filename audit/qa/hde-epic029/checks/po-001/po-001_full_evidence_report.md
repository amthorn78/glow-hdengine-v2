# PO Instructions - HDE-EPIC029 - po-001

## Step Summary
- Epic: HDE-EPIC029 / Conjunction Pass 5
- Step: po-001
- Approved QA Plan File: audit/qa/hde-epic029/r5 QA Plan HDE-EPIC029.md
- Approval Doc File: none
- Previous Step Report File: none
- PF-Canon consulted in request context: PF10 (current) + PF05 + PF02
- Output target: PO Instructions - HDE-EPIC029 - po-001

## Intent and Proof Obligation (Verbatim)
- "PO-001"
- "Proof obligation:"
- "The epic must remain confined to its bounded Conjunction closeout slice and must not introduce or repurpose a new public surface."

## Pass Criteria (Verbatim)
- "PASS if:"
- "* all three snapshots exist and are non-empty"
- "* the captured route slice and catalog remain compatible with the bounded-scope statement"

## Execution Context
- SAFE_MODE=1
- ALLOW_NETWORK=0
- APP_ENV=dev
- LC_ALL=C
- LANG=C
- TZ=UTC

## Commands Executed
1) Artifact capture commands (from approved plan):
- cp audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md audit/qa/hde-epic029/checks/po-001/conjunction_json_surface_inventory.snapshot.md
- cp docs/ENDPOINTS_CATALOG.json audit/qa/hde-epic029/checks/po-001/endpoints_catalog.snapshot.json
- rg -n "(/reader|/dev/writer/conjunction|/internal/dev/sampler|/dev/sampler/conjunction|/dev/reader/conjunction)" adapter/http_reader.py | tee audit/qa/hde-epic029/checks/po-001/route_snapshot.txt

Observed tooling result:
- bash: rg: command not found

2) Canonical step-log header writer block executed with truthful outcome:
- PASS_FAIL=FAIL_TOOLING

## Determination
- Final PASS_FAIL: FAIL_TOOLING

Reason:
- The required capture command using rg failed because rg was unavailable in this shell environment.
- This matches the provided rule: FAIL_TOOLING if cp or rg fails for any of the proven loci.

## Artifact Existence, Size, and SHA-256
- audit/qa/hde-epic029/checks/po-001/primary.log
  - size_bytes: 1274
  - sha256: f33cbb936e72db4ab51c0f685ee1bb6f68e509b97968079ef3d4d3646e6186d6
- audit/qa/hde-epic029/checks/po-001/conjunction_json_surface_inventory.snapshot.md
  - size_bytes: 2442
  - sha256: 235f89ae0c090cf063fab55f0a86a6a538ea5f429a603c49b396f599ee5b1c1b
- audit/qa/hde-epic029/checks/po-001/endpoints_catalog.snapshot.json
  - size_bytes: 1749
  - sha256: 4b766ec46b69df75136611a47d03fd7268fbfed1b8b18cbb44d9b3296874d143
- audit/qa/hde-epic029/checks/po-001/route_snapshot.txt
  - size_bytes: 0
  - sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

## Quick Compatibility Notes
- Catalog snapshot includes /reader and /dev/writer/conjunction (and also /dev/reader/conjunction and /dev/sampler/conjunction).
- The explicit /internal/dev/sampler path was not found in the catalog snapshot content copied for this step.
- Route slice evidence file is empty because the rg command failed before route lines could be captured.

## Full Evidence Output

### Evidence 1: primary.log
{"schema_version": "pf27.step_log_header.v1", "timestamp_utc": "2026-04-15T13:29:18Z", "check_id": "po-001", "check_name": "Bounded Conjunction closeout slice / no new public surface", "status": "FAIL_TOOLING", "fail_status": "FAIL_TOOLING", "command": "cp audit/qa/hde-epic029/00_meta/conjunction_json_surface_inventory.md audit/qa/hde-epic029/checks/po-001/conjunction_json_surface_inventory.snapshot.md; cp docs/ENDPOINTS_CATALOG.json audit/qa/hde-epic029/checks/po-001/endpoints_catalog.snapshot.json; rg -n \"(/reader|/dev/writer/conjunction|/internal/dev/sampler|/dev/sampler/conjunction|/dev/reader/conjunction)\" adapter/http_reader.py | tee audit/qa/hde-epic029/checks/po-001/route_snapshot.txt", "command_provenance": "Copy/paste from plan", "evidence_artifacts": ["audit/qa/hde-epic029/checks/po-001/primary.log", "audit/qa/hde-epic029/checks/po-001/conjunction_json_surface_inventory.snapshot.md", "audit/qa/hde-epic029/checks/po-001/endpoints_catalog.snapshot.json", "audit/qa/hde-epic029/checks/po-001/route_snapshot.txt"], "captured_env": {"SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev", "LC_ALL": "C", "LANG": "C", "TZ": "UTC"}, "pf_refs": ["PF10 - HDE-Build Notes", "PF27 - Canon Plan Templates"], "intended_tokens": [], "claimed_tokens": []}

### Evidence 2: conjunction_json_surface_inventory.snapshot.md
# HDE-EPIC029 PR-01 - Conjunction JSON Surface Inventory (Bounded)

## Scope guard (PF09.4 / HDE-CONJ009.1)

This inventory is intentionally bounded to the full in-scope conjunction JSON-emitting loci that are already repo-proven for PR-01.

Included loci (required in-scope set):
- /reader
- /dev/sampler/conjunction
- /dev/reader/conjunction
- /dev/writer/conjunction
- /internal/dev/sampler

No new routes, no new proof surfaces, and no alternate serializer/emitter paths are introduced by this inventory.

## Single-emitter verification checklist

Canonical shared emitter: engine.presenter.emitter.emit_public (delegates to engine.serializer.canon.sercanon).

### 1) /reader (GET)
- Route defined in adapter/http_reader.py as @bp.get("/reader").
- Success bytes are emitted by emit_fn(...); the default emit_fn is engine.runtime.emit_reader_public_bytes.
- engine.runtime.emit_reader_public_bytes emits through emit_public_envelope(...), which calls the shared emitter emit_public.
- Result: uses single shared emitter path.

### 2) /dev/writer/conjunction (GET)
- Route defined in adapter/http_reader.py as @bp.get("/dev/writer/conjunction").
- Handler calls _emit_dev_writer_conjunction_response(), which returns _emit_writer_response(...).
- _emit_writer_response(...) builds response bytes with emit_public(envelope, sort_keys=...).
- Result: uses single shared emitter path.

### 3) /internal/dev/sampler (POST)
- Route defined in adapter/http_reader.py as @bp.route("/internal/dev/sampler", methods=["POST"], ...).
- Handler dev_sampler_internal() returns bytes via body = emit_public(response_payload, sort_keys=True).
- Result: uses single shared emitter path.

### 4) /dev/sampler/conjunction (GET)
- Route calls _emit_conjunction_response().
- _emit_conjunction_response() returns body = emit_public(payload, sort_keys=True).
- Result: uses single shared emitter path.

### 5) /dev/reader/conjunction (GET)
- Route calls _emit_conjunction_response().
- _emit_conjunction_response() returns body = emit_public(payload, sort_keys=True).
- Result: uses single shared emitter path.

## Conclusion (PR-01 bounded outcome)

All in-scope conjunction JSON-emitting loci in this bounded PR-01 scope route through the single shared canonical emitter (emit_public -> sercanon).

No in-place emitter fix was needed for the inventoried loci.

### Evidence 3: endpoints_catalog.snapshot.json
{"endpoints":[{"a7_eligible":false,"blueprint_module":"engine.http.compat_handler","classification":"internal_admin","description":"Compat pair endpoint (internal admin)","env_gate":"APP_ENV!=prod","method":"POST","path":"/api/compat/v1","rails_profile":"internal-admin writer no-store"},{"a7_eligible":false,"blueprint_module":"adapter.http_reader","classification":"dev_harness","description":"Conjunction reader preview route (dev-only)","env_gate":"APP_ENV in {dev,test,local}","method":"GET","path":"/dev/reader/conjunction","rails_profile":"dev-harness closed-by-default SAFE rails"},{"a7_eligible":false,"blueprint_module":"adapter.http_reader","classification":"dev_harness","description":"Conjunction writer preview route (dev-only)","env_gate":"APP_ENV in {dev,test,local}","method":"GET","path":"/dev/writer/conjunction","rails_profile":"dev-harness closed-by-default SAFE rails"},{"a7_eligible":false,"blueprint_module":"adapter.http_reader","classification":"dev_harness","description":"Conjunction sampler preview route (dev-only)","env_gate":"APP_ENV in {dev,test,local}","method":"GET","path":"/dev/sampler/conjunction","rails_profile":"dev-harness closed-by-default SAFE rails"},{"a7_eligible":false,"blueprint_module":"adapter.http_reader","classification":"internal_identity","description":"Internal version endpoint for ops evidence","env_gate":"operator-network-only","method":["GET","HEAD"],"path":"/internal/version","rails_profile":"ops-only no-store"},{"a7_eligible":true,"blueprint_module":"adapter.http_reader","classification":"dev_harness","description":"Reader success route (dev-only)","env_gate":"APP_ENV=dev","method":["GET","HEAD"],"path":"/reader","rails_profile":"dev-harness reader a7"}],"success_endpoints":[]}

### Evidence 4: route_snapshot.txt
File content is empty (0 bytes).

## Final Step Result
- po-001 result: FAIL_TOOLING
- This step did not satisfy PASS criteria because route snapshot capture failed at tooling level (rg unavailable).
