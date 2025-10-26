# HD Engine Repo Docs — Index (SoT pointers)
 
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
+
+### Acceptance crib
+- Reader (EPIC-004): `docs/acceptance/reader_a7_crib.md`
+- Internal Ops (EPIC-005): `docs/acceptance/http_transport_evidence.md`
+
+### Evidence Index (EPIC-005)
+- `docs/EVIDENCE_INDEX.md`
