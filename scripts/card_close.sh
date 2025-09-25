#!/usr/bin/env bash
set -euo pipefail

# Args
CARD=""
MAX_MB=10
while [[ $# -gt 0 ]]; do
  case "$1" in
    --card) CARD="${2:-}"; shift 2;;
    --card=*) CARD="${1#--card=}"; shift 1;;
    --max-mb) MAX_MB="${2:-10}"; shift 2;;
    --max-mb=*) MAX_MB="${1#--max-mb=}"; shift 1;;
    *) echo "unknown arg: $1" >&2; exit 2;;
  esac
done
[[ -n "$CARD" ]] || { echo "Usage: $0 --card \"CARD-ID\" [--max-mb N]" >&2; exit 2; }

ROOT="$(pwd)"
STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
AUDIT_DIR="${ROOT}/audit"
mkdir -p "$AUDIT_DIR"

# 1) Commit (and push if upstream exists)
if command -v git >/dev/null 2>&1; then
  git add -A
  if ! git diff --cached --quiet; then
    git commit -m "${CARD}: close ${STAMP}"
  fi
  if git rev-parse --abbrev-ref --symbolic-full-name @{u} >/dev/null 2>&1; then
    git push || true
  fi
  COMMIT_SHA="$(git rev-parse --short HEAD 2>/dev/null || echo NONE)"
else
  COMMIT_SHA="NO-GIT"
fi

# 2) Build file list, manifest, and zip via Python (filters + size cap)
BUNDLE_ZIP="${AUDIT_DIR}/${CARD}_source_bundle_${STAMP}.zip"
BUNDLE_MAN="${AUDIT_DIR}/${CARD}_source_bundle_${STAMP}_MANIFEST.json"
PYTHON_BIN="${PYTHON_BIN:-python3}"

"$PYTHON_BIN" - <<PY
import os, json, time, hashlib, zipfile, stat
root = os.getcwd()
max_bytes = int(${MAX_MB}) * 1024 * 1024
exclude_dirs = {'.git', '.venv', '__pycache__', '.pytest_cache'}
exclude_exts = {'.zip','.tar','.tar.gz','.tgz','.7z','.rar','.bak','.tmp'}
bundle = r"${BUNDLE_ZIP}"
manifest_path = r"${BUNDLE_MAN}"

entries = []
def allow(path):
    rp = os.path.relpath(path, root)
    parts = rp.split(os.sep)
    if parts and parts[0] in exclude_dirs: return False
    le = path.lower()
    for ext in exclude_exts:
        if le.endswith(ext): return False
    try:
        st = os.stat(path)
        if not stat.S_ISREG(st.st_mode): return False
        if st.st_size > max_bytes: return False
        return True
    except FileNotFoundError:
        return False

for d, _, files in os.walk(root):
    # Skip excluded directories early
    base = os.path.relpath(d, root)
    head = base.split(os.sep)[0] if base != '.' else '.'
    if head in exclude_dirs: 
        continue
    for f in files:
        p = os.path.join(d, f)
        if allow(p):
            st = os.stat(p)
            entries.append({
                "path": os.path.relpath(p, root).replace("\\","/"),
                "size": st.st_size,
                "mtime": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(st.st_mtime))
            })

# Write manifest
with open(manifest_path, "w", encoding="utf-8") as mf:
    json.dump({
        "card": "${CARD}",
        "generated_at": "${STAMP}",
        "count": len(entries),
        "max_file_mb": ${MAX_MB},
        "files": sorted(entries, key=lambda e: e["path"])
    }, mf, ensure_ascii=False, indent=2)

# Create zip
with zipfile.ZipFile(bundle, "w", compression=zipfile.ZIP_DEFLATED) as zf:
    for e in entries:
        zf.write(e["path"], arcname=e["path"])
PY

# 3) Checksums
CHK="${AUDIT_DIR}/${CARD}_artifacts_sha256_${STAMP}.txt"
: > "$CHK"
if command -v sha256sum >/dev/null 2>&1; then
  sha256sum "$BUNDLE_ZIP" >> "$CHK"
  sha256sum "$BUNDLE_MAN" >> "$CHK"
elif command -v shasum >/dev/null 2>&1; then
  shasum -a 256 "$BUNDLE_ZIP" >> "$CHK"
  shasum -a 256 "$BUNDLE_MAN" >> "$CHK"
fi

# 4) Close note (human-readable)
CLOSE_MD="${AUDIT_DIR}/${CARD}_closeout_${STAMP}.md"
{
  echo "# Closeout — ${CARD}"
  echo
  echo "- Timestamp (UTC): ${STAMP}"
  echo "- Commit: ${COMMIT_SHA}"
  echo "- Bundle: ${BUNDLE_ZIP}"
  echo "- Manifest: ${BUNDLE_MAN}"
  echo "- Checksums: ${CHK}"
} > "$CLOSE_MD"

# Required lines for your workflow:
echo "[closeout] ${CLOSE_MD}"
echo "[bundle] ${BUNDLE_ZIP}"
echo "[manifest] ${BUNDLE_MAN}"
