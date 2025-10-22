#!/usr/bin/env bash
set -euo pipefail

STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
ROOT="$(pwd)"
AUDIT_DIR="${ROOT}/audit"
OUTDIR="${AUDIT_DIR}/audit_${STAMP}"
BUNDLE="${AUDIT_DIR}/audit_bundle_${STAMP}.zip"
MAN="${AUDIT_DIR}/audit_bundle_${STAMP}_MANIFEST.json"

mkdir -p "$OUTDIR"

# --- 1) Environment & repo diagnostics ---
{
  echo "=== ENV ==="
  echo "timestamp_utc: ${STAMP}"
  echo "repo: $(basename "$ROOT")"
  python3 -V || true
  pip --version || true
  pytest --version || true
  echo
  echo "=== GIT ==="
  git rev-parse --short HEAD 2>/dev/null || echo "NO-GIT"
  git status --porcelain=v1 2>/dev/null || true
  echo
  echo "=== TOP (2 levels) ==="
  find . -maxdepth 2 -mindepth 1 -print | sort
} > "${OUTDIR}/env_repo_diag.txt"

# --- 2) Focused outputs (never fail the script) ---
pytest -q tests/canon > "${OUTDIR}/pytest_canon.txt" 2>&1 || true
# Gate stdout (pure JSON if script exists)
if [[ -x scripts/validate_canon.sh ]]; then
  bash scripts/validate_canon.sh --json > "${OUTDIR}/validate_canon_stdout.json" 2> "${OUTDIR}/validate_canon_stderr.txt" || true
fi
# Copy artifacts if present
[[ -f CANON_CHECKSUMS.json ]] && cp CANON_CHECKSUMS.json "${OUTDIR}/" || true
[[ -f artifacts/canon_report.json ]] && cp artifacts/canon_report.json "${OUTDIR}/" || true

# --- 3) Build manifest + bundle (filtered) ---
export OUTDIR BUNDLE MAN
python3 - <<'PY'
import os, json, time, stat, fnmatch, pathlib, zipfile
root = pathlib.Path(".").resolve()
aud  = pathlib.Path(os.environ["OUTDIR"]).resolve()
bundle = pathlib.Path(os.environ["BUNDLE"]).resolve()
manifest = pathlib.Path(os.environ["MAN"]).resolve()

exclude_dirs = {".git", ".venv", "__pycache__", ".pytest_cache", ".cache", ".mypy_cache", ".vscode"}
exclude_globs = ["*.zip","*.tar","*.tar.gz","*.tgz","*.7z","*.rar","*.bak","*.tmp","*.pyc"]
max_bytes = 10 * 1024 * 1024  # 10 MB per file cap

def allowed(p: pathlib.Path) -> bool:
    try:
        rel = p.relative_to(root)
        if rel.parts and rel.parts[0] in exclude_dirs: return False
        name = p.name.lower()
        for pat in exclude_globs:
            if fnmatch.fnmatch(name, pat): return False
        st = p.stat()
        if not stat.S_ISREG(st.st_mode): return False
        if st.st_size > max_bytes: return False
        return True
    except FileNotFoundError:
        return False

entries = {}
for d, _, files in os.walk(root):
    dpath = pathlib.Path(d)
    head = dpath.relative_to(root).parts[:1]
    if head and head[0] in exclude_dirs: continue
    for f in files:
        p = dpath / f
        if allowed(p):
            st = p.stat()
            path = str(p.relative_to(root)).replace(os.sep,"/")
            entries[path] = {
                "path": path,
                "size": st.st_size,
                "mtime": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(st.st_mtime))
            }

# Always include the OUTDIR contents
for p in aud.rglob("*"):
    if p.is_file():
        rel = str(p.relative_to(root)).replace(os.sep,"/")
        st = p.stat()
        entries[rel] = {
            "path": rel,
            "size": st.st_size,
            "mtime": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(st.st_mtime))
        }

entries_sorted = [entries[k] for k in sorted(entries.keys())]

with zipfile.ZipFile(bundle, "w", compression=zipfile.ZIP_DEFLATED) as zf:
    for e in entries_sorted:
        zf.write(e["path"], arcname=e["path"])

manifest.parent.mkdir(parents=True, exist_ok=True)
manifest.write_text(json.dumps({
    "stamp_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "count": len(entries_sorted),
    "files": entries_sorted
}, ensure_ascii=False, indent=2), encoding="utf-8")
PY

echo "[audit] ${BUNDLE}"
