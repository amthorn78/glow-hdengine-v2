# EPIC003 Acceptance — PO Summary

Artifacts rooted at artifacts/epic003/.

## Markers (PASS lines)
- COMPAT_ENGINE_AB_BA_OK=PASS
- COMPAT_CATEGORY_KEYS_MIN_OK=PASS
- COMPAT_SCORE_INT_RANGE_OK=PASS
- COMPAT_BAND_ENUM_OK=PASS
- M10_ORDER_OK=PASS
- CATEGORIES_SET_V1_OK=PASS
- COMPAT_META_INVOCATION_TAG_OK=PASS
- LF_TERMINATED_OK=PASS
- NO_BOM_OK=PASS
- JSON_SORTED_KEYS_OK=PASS
- COMPAT_ALPHA_200_OK=PASS
- COMPAT_CT_UTF8_OK=PASS
- STATUS_400_OK=PASS
- ERROR_CACHECTL_NOSTORE_OK=PASS
- ERR_TOKENS_OK=PASS
- ERROR_MESSAGE_MAP_OK=PASS
- INPUT_WEIGHTS_CANON_OK=PASS
- BYTE_PARITY_OK=PASS
- THRESHOLDS_SCHEMA_OK=PASS

## Notable files
- compat_success.json (200 body)
- compat_success_BA.json (BA body)
- compat_identity_hash.txt (sha256 of 200 body bytes)
- headers_compat_200.raw / headers_compat_400_get_body.raw
- narrative_keys_table.json
- thresholds_snapshot_v1.json / thresholds_schema.txt
- acceptance.log (PASS lines)
- manifest.json / checksums.txt

---

## Cleanup follow-up (EPIC003 scope)
- Reader modules (`adapter/http_reader.py`, `adapter/logging_filter.py`) contain `json.dumps(...)` for Reader development harness paths. **Compat surface is clean** (no ad-hoc emitters).
- No runtime imports from `adapters/` in EPIC003 surfaces; guard test enforces the single-home rule (adapter/).
- Any consolidation of `adapters/` is deferred to a future card per Isis’ scope.

---
## EPIC003 Cleanup — Final
- Archived legacy trees: `core/`, `server/`, `adapters/` → `_archive/EPIC003_CLEAN_refs_20251017_211906/`.
- Removed active files that imported `core.*` (moved to `_archive/EPIC003_CLEAN_refs_*`).
- Added deny-list test to prevent re-introduction (`tests/epic003/test_legacy_imports_denied.py`).
- Compat surface re-verified OK post-cleanup.
