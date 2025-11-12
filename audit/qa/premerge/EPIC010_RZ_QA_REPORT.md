# EPIC-010 Readiness QA Dossier — Phase 7

## Overview
Performed a read-only sweep across phases 1–6 to confirm Aux transport posture, parity, determinism, coverage, indexing discipline, CLI preview hygiene, and documentation currency. Checked artifacts:
- audit/qa/premerge/routes/*.diff, audit/qa/premerge/routes/route_probe.json
- tests/transport/headers/aux_text_200.snap, tests/transport/headers/aux_suppression_200.snap
- audit/gates/aux/*.txt, audit/gates/aux/determinism/*.{txt,json}
- audit/gates/narratives/keys_10x4.table.json
- artifacts/cli/narrative/{stdout.txt,sidecar.json}
- docs/evidence/INDEX.{json,sha256}, artifacts/evidence_index.jsonl
- README.md, docs/INDEX.md

## 1. Routes parity
*What we checked:* Confirmed canonical and alias routes return byte-identical responses for both text and suppressed tuples.
- Evidence: audit/qa/premerge/routes/parity_text.diff, audit/qa/premerge/routes/parity_suppressed.diff, audit/qa/premerge/routes/route_probe.json
- Result: **PASS**

## 2. Suppression posture
*What we checked:* Ensured suppressed snapshot stays 200 with empty body, no ETag, lowercase headers, and optional generic policy only.
- Evidence: audit/gates/aux/suppression_snapshot_check.txt, tests/transport/headers/aux_suppression_200.snap
- Result: **PASS**

## 3. Vary on both outcomes
*What we checked:* Verified Vary: Authorization, Accept-Encoding is asserted for text and suppressed responses.
- Evidence: audit/gates/aux/headers_style_check.txt
- Result: **PASS**

## 4. Headers lowercase posture
*What we checked:* Confirmed snapshot header keys are fully lowercase.
- Evidence: audit/gates/aux/headers_style_check.txt, tests/transport/headers/aux_text_200.snap, tests/transport/headers/aux_suppression_200.snap
- Result: **PASS**

## 5. Text snapshot quality
*What we checked:* Validated text snapshot headers/body meet EPIC-010 spec (status 200, text/plain charset, quoted strong ETag, Vary header, provenance headers, LF non-empty body).
- Evidence: tests/transport/headers/aux_text_200.snap
- Result: **PASS**

## 6. Provenance echoes
*What we checked:* Ensured provenance headers (X-Narrative-Pack-Sha, X-Narrative-Composition) appear with non-empty values on all outcomes/routes.
- Evidence: audit/gates/aux/determinism/two_run_assert.json
- Result: **PASS**

## 7. Determinism under C/UTC
*What we checked:* Confirmed LC_ALL/LANG/TZ pins and two-run identity for canonical and alias routes on text/suppressed tuples.
- Evidence: audit/gates/aux/determinism/env.txt, audit/gates/aux/determinism/two_run_assert.json
- Result: **PASS**

## 8. 10×4 coverage lock
*What we checked:* Verified coverage table retains 40 rows with both shared_key and personal_key per entry.
- Evidence: audit/gates/narratives/keys_10x4.table.json
- Result: **PASS**

## 9. Indices & mirror parity
*What we checked:* Validated human index inclusion, SHA hash alignment, and single JSONL mirror with canonical ordering/proof anchors covering required artifacts.
- Evidence: docs/evidence/INDEX.json, docs/evidence/INDEX.sha256, artifacts/evidence_index.jsonl (lines 10–11, 34–35)
- Result: **PASS**

## 10. CLI preview hygiene
*What we checked:* Ensured CLI preview artifacts are LF-only, non-ANSI, ids-only sidecar, parity with Aux, and indexed in both registries.
- Evidence: artifacts/cli/narrative/stdout.txt, artifacts/cli/narrative/sidecar.json, audit/gates/cli/preview_check.txt, docs/evidence/INDEX.json, artifacts/evidence_index.jsonl
- Result: **PASS**

## 11. Documentation currency
*What we checked:* Reviewed README.md and docs/INDEX.md for canonical+alias route references, posture descriptions, provenance header names, and absence of forbidden guidance.
- Evidence: README.md (§"Aux Narrative"), docs/INDEX.md (top-level summary)
- Result: **PASS**

## Appendix
### Suppression snapshot gate
```
no_etag:true
policy_header:suppressed|absent
body_empty:true
headers_lowercase:true
```

### Headers style gate
```
vary_on_text:true
vary_on_suppressed:true
headers_lowercase:true
```

### Route parity probe (first 30 lines)
```
{"same_handler":true,"suppressed_case":{"alias":{"body_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","status":200,"url":"/aux/narrative?v=1&category=alignment&band=Cool&perspective=a_to_b"},"byte_identical":true,"canonical":{"body_sha256":"e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855","status":200,"url":"/api/aux/narrative?v=1&category=alignment&band=Cool&perspective=a_to_b"},"tuple":{"band":"Cool","category":"alignment","perspective":"a_to_b"}},"text_case":{"alias":{"body_sha256":"e4a96e2bff6638158d95833660899525cbe0e124c84544b52942e3eb79fb69c9","status":200,"url":"/aux/narrative?v=1&category=harmony&band=Cool&perspective=shared"},"byte_identical":true,"canonical":{"body_sha256":"e4a96e2bff6638158d95833660899525cbe0e124c84544b52942e3eb79fb69c9","status":200,"url":"/api/aux/narrative?v=1&category=harmony&band=Cool&perspective=shared"},"tuple":{"band":"Cool","category":"harmony","perspective":"shared"}}}
```

### Determinism pins
```
LC_ALL=C
LANG=C
TZ=UTC
```

### Determinism booleans
```
{
  "text_case": {
    "canonical": true,
    "alias": true
  },
  "suppressed_case": {
    "canonical": true,
    "alias": true
  }
}
```

### Mirror lines referenced
```
{"artifact_key":"aux.headers.text","discovered_physical_path":"tests/transport/headers/aux_text_200.snap","produced_at_utc":"2025-11-12T03:45:00Z","proof_anchor":"audit/gates/aux/text_snapshot_check.txt","role":"aux-headers","sha256":"deca94399871c57001d41e79387341c00b6fbe83fc1998711077349d03548803","size_bytes":366}
{"artifact_key":"aux.headers.suppression","discovered_physical_path":"tests/transport/headers/aux_suppression_200.snap","produced_at_utc":"2025-11-12T03:45:00Z","proof_anchor":"audit/gates/aux/suppression_snapshot_check.txt","role":"aux-headers","sha256":"081db8bc7d95e041f5dba5b62cf93f883f6763f6dccdbae55138d693bec9fa22","size_bytes":307}
{"artifact_key":"cli.narrative.preview_stdout","discovered_physical_path":"artifacts/cli/narrative/stdout.txt","produced_at_utc":"2025-11-12T01:53:51Z","proof_anchor":"audit/gates/cli/preview_check.txt","role":"cli-preview","sha256":"e4a96e2bff6638158d95833660899525cbe0e124c84544b52942e3eb79fb69c9","size_bytes":64}
{"artifact_key":"cli.narrative.preview_sidecar","discovered_physical_path":"artifacts/cli/narrative/sidecar.json","produced_at_utc":"2025-11-12T01:53:51Z","proof_anchor":"audit/gates/cli/preview_check.txt","role":"cli-preview","sha256":"8c5425aa890533ccb8877caf612b56a242abd27029d1245ba719b051c250f55b","size_bytes":242}
```
