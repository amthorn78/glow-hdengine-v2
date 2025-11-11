# R7 Documentation Discovery Report

## Summary
- Aux section headings ("## Aux Narrative"): 3
- Legacy endpoint backticks (`GET /aux/narrative` without /api): 1
- Non-suppressed policy header values: 1
- Per-reason policy strings in public docs: 0
- Provenance header name drift (X-Narrative-Composition-Id): 0
- Coverage pointer drift (keys_10x2 references): 0
- Aux HEAD/304 capture guidance in this epic: 0

## Findings

### Aux section headings
- README.md:12 — `## Aux Narrative (EPIC-010)`
- README.md:293 — `## Aux Narrative (EPIC-010 — text surface)`
- docs/EVIDENCE_INDEX.md:31 — `## Aux Narrative (EPIC-010) — Evidence`

### Legacy endpoint backticks
- README.md:294 — `**Endpoint:** \`GET /aux/narrative\``

### Non-suppressed policy header values
- audit/qa/compat/suppressed_aux_headers.snap:9 — `X-Narrative-Policy: duplicate`

### Additional categories
- Per-reason policy strings: no hits found.
- Provenance header name drift: no hits found.
- Coverage pointer drift: no hits found.
- Aux HEAD/304 guidance: no hits found.
