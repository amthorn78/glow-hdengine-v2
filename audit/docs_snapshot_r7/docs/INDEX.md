# HD Engine Repo Docs — Index (SoT pointers)

### Acceptance & evidence
- Evidence Index (human): `docs/EVIDENCE_INDEX.md`
- Evidence Index (machine): `artifacts/evidence_index.jsonl`
- Aux narrative surface (EPIC-010):
  - Routes: canonical `GET /api/aux/narrative?v=1`; `/aux/narrative?v=1` is the byte-identical BC alias.
  - Posture: Text → 200 text/plain + quoted strong `ETag` (LF body, `Vary: Authorization, Accept-Encoding`); Suppressed → 200 empty, no `ETag`, optional generic `X-Narrative-Policy: suppressed` only.
  - Provenance headers (both outcomes): `X-Narrative-Pack-Sha`, `X-Narrative-Composition`.
  - Evidence: `audit/gates/narratives/keys_10x4.table.json`, `tests/transport/headers/aux_text_200.snap`, `tests/transport/headers/aux_suppression_200.snap`.
- EPIC006 acceptance: run `LC_ALL=C TZ=UTC pytest -q -m epic006`

This repo contains implementation docs. Canon (spec/process) lives in PF documents; reference **titles only**:

- Mechanics Guide to the HD Engine (Build Guide)
- HD Engine Build Checklist (Components & Tasks)
- HD Engine Math & Technical Spec
- HD Engine — CLI, API & Vendor Ingest Spec
- Governance & Process Handbook

### Local map
- **ARCHITECTURE.md** — single homes (engine/, adapter/), guards, providers
- Architecture snapshots: `_arch/<epic_id>_<timestamp>/` (routes/imports/tree)

### Developer quick-links
- Emitter: `engine/presenter/emitter.py::emit_compact_json`
- Serializer: `engine/serializer/canon.py::dumps` (UTF-8; sort_keys; one LF)
- Compat handler (alpha): `engine/http/compat_handler.py`

### Acceptance crib
- Reader (EPIC-004): `docs/acceptance/reader_a7_crib.md`
- Internal Ops (EPIC-005): `docs/acceptance/http_transport_evidence.md`
  *(Aux transport is scoped in EPIC-010; A7 proofs remain Catalog-only in a later epic.)*

### Evidence Index (EPIC-005)
- `docs/EVIDENCE_INDEX.md`

### EPIC-009 — Ops Safety & DB runtime posture
- Refusal surface & keys-only logging: see README and AGENTS
- Env-matrix snapshots (selection-only): CHANGELOG entry 2025-11-07
- DB posture scripts & evidence: `docs/ADAPTER_DB.md`
- Pre-commit QA harness: `scripts/qa/epic009_precommit.sh` (report under `artifacts/qa/`)
