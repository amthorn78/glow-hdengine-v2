#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   bash scripts/make_source_bundle.sh [--card CARD_ID] [--max-mb N]
# Example:
#   bash scripts/make_source_bundle.sh --card "ISIS-GREENFIELD-006"
# Env override:
#   MAX_MB=10 bash scripts/make_source_bundle.sh --card "CARD-123"

CARD=""
MAX_MB="${MAX_MB:-5}"
while [[ $# -gt 0 ]]; do
  case "$1" in
    --card) CARD="${2:-}"; shift 2;;
    --max-mb) MAX_MB="${2:-5}"; shift 2;;
    *) echo "unknown arg: $1" >&2; exit 2;;
  esac
done

ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$ROOT"

STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
OUTDIR="audit"; mkdir -p "$OUTDIR"
BASE="${CARD:+${CARD}_}source_bundle_${STAMP}"
ZIP="${OUTDIR}/${BASE}.zip"
LIST="${OUTDIR}/${BASE}__filelist.txt"
MANIFEST="${OUTDIR}/${BASE}_MANIFEST.json"

# Dir prunes (top-level names)
PRUNE_EXPR='\( -path "./.git" -o -path "./.venv" -o -path "./node_modules" -o -path "./artifacts" -o -path "./audit" -o -path "./__pycache__" -o -path "./.mypy_cache" -o -path "./.pytest_cache" -o -path "./.ruff_cache" \) -prune -o'

# Include extensions (lowercased)
IN_EXT=("py" "pyi" "js" "jsx" "ts" "tsx" "json" "md" "markdown" "sh" "bash" "zsh" "yaml" "yml" "toml" "ini" "cfg" "conf" "env" "txt" "sql" "css" "html")
# Include special base names (lowercased)
IN_BASE=("dockerfile" "makefile" ".gitignore" ".gitattributes" "pyproject.toml" "requirements.txt" "requirements-dev.txt")

# Exclude extensions (lowercased binaries/heavy)
EX_EXT=("png" "jpg" "jpeg" "gif" "pdf" "zip" "tgz" "gz" "pyc" "so" "dylib" "db" "sqlite")

# Build file list (null-separated), apply size cap and filters
tmp="$(mktemp)"; trap 'rm -f "$tmp"' EXIT

# shellcheck disable=SC2016
eval find . ${PRUNE_EXPR} -type f -size -"${MAX_MB}"M -print0 \
  | while IFS= read -r -d '' f; do
      rel="${f#./}"
      base="$(basename "$rel")"
      base_lc="${base,,}"
      ext=""
      if [[ "$rel" == *.* ]]; then ext="${rel##*.}"; fi
      ext_lc="${ext,,}"

      # exclude by extension
      for ex in "${EX_EXT[@]}"; do
        if [[ "$ext_lc" == "$ex" ]]; then continue 2; fi
      done

      # include if extension matches
      for inc in "${IN_EXT[@]}"; do
        if [[ "$ext_lc" == "$inc" ]]; then printf '%s\0' "$rel"; continue 3; fi
      done

      # include if special basename matches
      for sp in "${IN_BASE[@]}"; do
        if [[ "$base_lc" == "$sp" ]]; then printf '%s\0' "$rel"; continue 3; fi
      done

      # otherwise skip
    done \
  | LC_ALL=C sort -z | tr '\0' '\n' > "$tmp"

mv "$tmp" "$LIST"

# Create the ZIP
if ! command -v zip >/dev/null 2>&1; then
  echo "zip not found; install it (e.g., apt-get update && apt-get install -y zip)" >&2
  exit 3
fi
zip -q -@ "$ZIP" < "$LIST"

# Manifest (path, size, sha256)
python - <<'PY' "$ROOT" "$LIST" "$MANIFEST"
import sys, os, json, hashlib
root, filelist, out = sys.argv[1:4]
rows=[]
with open(filelist,'r',encoding='utf-8') as f:
  for rel in f:
    rel=rel.strip()
    if not rel: continue
    p=os.path.join(root, rel)
    try:
      st=os.stat(p)
      h=hashlib.sha256()
      with open(p,'rb') as fh:
        for chunk in iter(lambda: fh.read(1<<20), b''): h.update(chunk)
      rows.append({"path":rel.replace("\\","/"),"size":st.st_size,"sha256":h.hexdigest()})
    except Exception as e:
      rows.append({"path":rel.replace("\\","/"),"size":None,"sha256":None,"error":str(e)})
with open(out,'w',encoding='utf-8') as o:
  o.write(json.dumps(rows, ensure_ascii=False, separators=(",",":")))
print(f"FILES={len(rows)} OUT={out}")
PY

echo "[bundle] $ZIP"
