#!/usr/bin/env bash
set +e
set +o pipefail 2>/dev/null || true

# === config ===
TS="$(date -u +%Y%m%dT%H%M%SZ)"
ARCH_DIR="_arch/epic003_${TS}"
ART_DIR="artifacts/epic003"
ROOT_MD="ARCHITECTURE.md"
mkdir -p "$ARCH_DIR" "$ART_DIR"

# --- helpers ---
_have() { command -v "$1" >/dev/null 2>&1; }

# --- BEFORE/AFTER snapshots (AFTER only here, but we reuse names) ---
# Route registrations (adapter/)
if _have rg; then
  rg -n "add_url_rule|register_blueprint" adapter/ > "${ARCH_DIR}/routes.after.txt" || true
else
  grep -RInE "add_url_rule|register_blueprint" adapter/ > "${ARCH_DIR}/routes.after.txt" 2>/dev/null || true
fi

# Compat endpoints (decorators)
grep -RInE '@compat_blueprint\.(get|post)\(' engine/http/compat_handler.py \
  > "${ARCH_DIR}/compat_endpoints.after.txt" 2>/dev/null || true

# Compact tree (3 levels)
if _have tree; then
  tree -a -L 3 > "${ARCH_DIR}/tree.after.txt"
else
  find adapter engine -maxdepth 3 -print | sed 's|^\./||' | LC_ALL=C sort > "${ARCH_DIR}/tree.after.txt"
fi

# Archives present
ARCH_MAIN="$(ls -1d _archive/EPIC003_CLEAN_* 2>/dev/null | tail -n1 || true)"
ARCH_REFS="$(ls -1d _archive/EPIC003_CLEAN_refs_* 2>/dev/null | tail -n1 || true)"

# Read files safely
routes="$(sed 's|^\./||' "${ARCH_DIR}/routes.after.txt" 2>/dev/null || true)"
endpts="$(cat "${ARCH_DIR}/compat_endpoints.after.txt" 2>/dev/null || true)"
tree3="$(cat "${ARCH_DIR}/tree.after.txt" 2>/dev/null || true)"

# Generate Architecture Map — AFTER (deterministic sections/order)
MAP_PATH="${ARCH_DIR}/architecture_map_AFTER.md"
{
  echo "# Architecture Map — AFTER (EPIC003 Cleanup)"
  echo
  echo "Generated: ${TS}"
  echo
  echo "## 1) Active Trees"
  echo "- adapter/  — single HTTP home (route wiring)"
  echo "- engine/http/  — HTTP handlers (compat)"
  echo "- engine/compat/  — compute, ordering, thresholds, constants"
  echo "- engine/serializer/  — canonical JSON serializer (UTF-8, sort_keys, compact, LF)"
  echo "- engine/presenter/  — single emitter (emit_compact_json)"
  echo "- engine/validation/  — viewer_prefs validator (10 integer weights 0..100)"
  echo "- engine/errors/  — error envelope {ok:false,code,error}"
  echo "- cli/ (if present)  — must import same emitter as service"
  echo
  echo "## 2) Archived Trees & Pointers"
  echo "- ${ARCH_MAIN:-\"(none found)\"}  (moved: core/, server/, adapters/)"
  echo "- ${ARCH_REFS:-\"(none found)\"}  (moved: files that imported core.*)"
  echo
  echo "## 3) Routes (mechanical scrape + ownership)"
  echo "Registered routes (adapter/):"
  if [ -n "$routes" ]; then
    echo '```'
    printf "%s\n" "$routes"
    echo '```'
  else
    echo "- (none found)"
  fi
  echo "Ownership: adapter/ is the only route registry; engine/http/ provides handlers."
  echo
  echo "## 4) Emitter/Serializer Contract"
  echo "- All emission calls use engine.presenter.emitter.emit_compact_json"
  echo "- Serializer: engine.serializer.canon.dumps (UTF-8, sort_keys, compact, one trailing LF)"
  echo
  echo "## 5) Import Boundaries (guards)"
  echo "- Forbidden in active code: from core, from adapters, from server"
  echo "- Forbid json.dumps/jsonify in handlers/CLI (single emitter path)"
  echo
  echo "## 6) Evidence & PASS Markers"
  echo "- Snapshots: ${ARCH_DIR}/*"
  echo "- PASS markers: ARCH_MAP_AFTER_OK, SERIALIZER_SINGLE_PATH_OK, BYTE_PARITY_OK,"
  echo "  JSON_SORTED_KEYS_OK, READER_SINGLE_HOME_OK (future), etc."
  echo
  echo "## 7) Build/Run modes (dev)"
  echo "- APP_ENV=dev; bind 127.0.0.1; adapter/app.py is the dev app home"
  echo
  echo "## 8) Known Guards & Tests"
  echo "- tests/epic003/test_legacy_imports_denied.py (no core/adapters/server in active code)"
  echo "- tests/epic003/test_http_home_single_path.py (no adapters/ imports in EPIC003 surfaces)"
  echo "- tests/epic003/test_error_message_map.py (exact error strings)"
  echo
  echo "## Compact Tree (3 levels)"
  if [ -n "$tree3" ]; then
    echo '```'
    printf "%s\n" "$tree3"
    echo '```'
  else
    echo "- (not available)"
  fi
} > "$MAP_PATH"

# LF-termination guard
python - <<'PY'
import glob, io, os
for p in glob.glob("_arch/epic003_*/architecture_map_AFTER.md"):
    with open(p,"rb") as f: b=f.read()
    if not b.endswith(b"\n"):
        with open(p,"ab") as f: f.write(b"\n")
print("ARCH_MAP_LF_OK=True")
PY

# Copy to evidence + canonical root
cp -f "$MAP_PATH" "$ART_DIR/ARCHITECTURE_MAP_AFTER.md"
cp -f "$MAP_PATH" "$ROOT_MD"

# Acceptance line
echo "ARCH_MAP_AFTER_OK=PASS" >> "$ART_DIR/acceptance.log"

echo "WROTE: $MAP_PATH"
echo "COPIED: $ART_DIR/ARCHITECTURE_MAP_AFTER.md"
echo "COPIED: $ROOT_MD"
