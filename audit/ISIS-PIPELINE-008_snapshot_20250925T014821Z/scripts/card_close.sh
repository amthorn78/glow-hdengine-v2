# --- HDCoder prelude: snapshot + full manifest (no external scripts) ---
# Extract --card VALUE or --card=VALUE
__CARD_ID=""
for arg in "$@"; do
  case "$arg" in
    --card=*) __CARD_ID="${arg#--card=}" ;;
    --card) shift; __CARD_ID="${1:-}";;
  esac
done
: "${__CARD_ID:=CARD-UNSPECIFIED}"

# Common paths
__ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
__STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
__AUDIT_DIR="${__ROOT}/audit"
mkdir -p "${__AUDIT_DIR}"

# -------- 1) Per-session change snapshot since HEAD (excludes *.zip) --------
__SNAP_DIR="${__AUDIT_DIR}/${__CARD_ID}_snapshot_${__STAMP}"
__SNAP_MAN="${__AUDIT_DIR}/${__CARD_ID}_snapshot_manifest_${__STAMP}.json"
__SNAP_DIFF="${__AUDIT_DIR}/${__CARD_ID}_diff_${__STAMP}.patch"
__SNAP_LIST="${__AUDIT_DIR}/${__CARD_ID}_changed_${__STAMP}.txt"

# Gather changed & untracked
git -C "${__ROOT}" diff --name-status HEAD > /tmp/_chg.txt 2>/dev/null || true
git -C "${__ROOT}" ls-files --others --exclude-standard > /tmp/_untracked.txt 2>/dev/null || true

python3 - <<'PY' >/tmp/_changed.json
import json, re
changed = {}
def parse(line):
    parts = line.rstrip("\n").split("\t")
    if not parts or not parts[0]: return
    tag = parts[0]
    if tag.startswith("R"):  # rename: R100\told\tnew
        if len(parts) >= 3:
            oldp, newp = parts[1], parts[2]
            changed[newp] = {"status":"R", "path": newp, "old": oldp}
    elif len(parts) >= 2:
        changed[parts[1]] = {"status": tag[:1], "path": parts[1]}
try:
    with open("/tmp/_chg.txt","r",encoding="utf-8",errors="replace") as f:
        for ln in f: parse(ln)
except FileNotFoundError: pass
try:
    with open("/tmp/_untracked.txt","r",encoding="utf-8",errors="replace") as f:
        for ln in f:
            p = ln.strip()
            if p: changed[p] = {"status":"U","path":p}
except FileNotFoundError: pass
print(json.dumps({"changed": list(changed.values())}, ensure_ascii=False))
PY

# Build list (skip deleted, skip zips at copy time)
jq -r '.changed[].path' /tmp/_changed.json 2>/dev/null | LC_ALL=C sort -u > "${__SNAP_LIST}" || : 
mkdir -p "${__SNAP_DIR}"
while IFS= read -r rel; do
  [ -z "$rel" ] && continue
  [ ! -e "$rel" ] && continue
  case "$rel" in *.zip) continue;; esac
  mkdir -p "${__SNAP_DIR}/$(dirname "$rel")"
  cp -p "$rel" "${__SNAP_DIR}/$rel" || true
done < "${__SNAP_LIST}"

# Binary-safe diff vs HEAD
git -C "${__ROOT}" diff --binary HEAD > "${__SNAP_DIFF}" 2>/dev/null || true

# Snapshot manifest (sha256 for existing non-zip files)
python3 - <<'PY' > "${__SNAP_MAN}"
import json, os, hashlib
with open("/tmp/_changed.json","r",encoding="utf-8") as f:
    changed = {e["path"]: e for e in json.load(f)["changed"]}
def sha256(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for chunk in iter(lambda: f.read(131072), b''):
            h.update(chunk)
    return h.hexdigest()
entries=[]
for rel, meta in changed.items():
    e={"path":rel,"status":meta.get("status","")}
    if os.path.exists(rel) and not rel.endswith(".zip"):
        try:
            e["size"]=os.path.getsize(rel)
            e["sha256"]=sha256(rel)
        except Exception as exc:
            e["error"]=f"{type(exc).__name__}: {exc}"
    else:
        e["size"]=None; e["sha256"]=None
    if "old" in meta: e["old"]=meta["old"]
    entries.append(e)
print(json.dumps({"count":len(entries),"files":entries}, ensure_ascii=False, indent=2))
PY

echo "[snapshot_dir] ${__SNAP_DIR}"
echo "[snapshot_manifest] ${__SNAP_MAN}"
echo "[snapshot_list] ${__SNAP_LIST}"
echo "[snapshot_diff] ${__SNAP_DIFF}"

# -------- 2) Full-repo manifest (≤10MB per file; include docs) ----------
__FF_JSON="${__AUDIT_DIR}/${__CARD_ID}_full_manifest_${__STAMP}.json"
__FF_LIST="${__AUDIT_DIR}/${__CARD_ID}_full_filelist_${__STAMP}.txt"
__MAX=$((10*1024*1024))  # 10 MB

# Enumerate files (exclude .git, .venv, caches, zips/tars)
LC_ALL=C find . -type f \
  -not -path "./.git/*" \
  -not -path "./.venv/*" \
  -not -path "./__pycache__/*" \
  -not -path "./.pytest_cache/*" \
  -not -name "*.zip" -not -name "*.tar" -not -name "*.tar.gz" \
  -printf "%P\n" | sort > "${__FF_LIST}"

python3 - <<'PY' > "${__FF_JSON}"
import os, json, hashlib, time, sys
ROOT="."
MAX = 10*1024*1024
with open(sys.argv[1],"r",encoding="utf-8") as f:
    paths=[ln.strip() for ln in f if ln.strip()]
def sha256(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for chunk in iter(lambda: f.read(131072), b''):
            h.update(chunk)
    return h.hexdigest()
out={"root":os.path.abspath(ROOT),"timestamp":time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
     "count":0,"total_bytes":0,"entries":[]}
for rel in paths:
    p=os.path.join(ROOT,rel)
    if not os.path.exists(p): continue
    st=os.stat(p); size=st.st_size
    rec={"path":rel,"size":size,"mtime":time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(st.st_mtime))}
    if size<=MAX:
        try: rec["sha256"]=sha256(p)
        except Exception as e: rec["error"]=f"{type(e).__name__}: {e}"
    else:
        rec["skipped_due_to_size"]=True
    out["entries"].append(rec); out["count"]+=1; out["total_bytes"]+=size
print(json.dumps(out, ensure_ascii=False, indent=2))
PY "${__FF_LIST}"

echo "[full_manifest_json] ${__FF_JSON}"
echo "[full_manifest_list] ${__FF_LIST}"
# --- end HDCoder prelude ---
# Add per-session change snapshot (since last commit), excluding *.zip
mkdir -p scripts audit && cat > scripts/make_change_snapshot.sh <<'SH'
#!/usr/bin/env bash
set -euo pipefail

CARD="${1:-CARD-UNSPECIFIED}"
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"; cd "$ROOT"
STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
OUTDIR="audit"; mkdir -p "$OUTDIR"
SNAP_DIR="${OUTDIR}/${CARD}_snapshot_${STAMP}"
MANIFEST="${OUTDIR}/${CARD}_snapshot_manifest_${STAMP}.json"
PATCH="${OUTDIR}/${CARD}_diff_${STAMP}.patch"
LIST="${OUTDIR}/${CARD}_changed_${STAMP}.txt"

# 1) Collect changed paths vs HEAD (M/A/R/D) + untracked
#    We keep deleted in the manifest (cannot copy), copy everything else except *.zip.
git diff --name-status -z HEAD > /tmp/_chg_z.txt || true
git ls-files --others --exclude-standard -z >> /tmp/_untracked_z.txt || true

# Parse to line/fields
python3 - <<'PY' >/tmp/_changed.json
import sys, json, os
def parse_z_status(p):
    data = sys.stdin.buffer.read().split(b'\x00')
    it = iter(data)
    out=[]
    for rec in it:
        if not rec: continue
        # rec may be like "M\tpath" or "A\tpath" or "R100\told\tnew"
        parts = rec.decode('utf-8', 'replace').split('\t')
        if parts[0].startswith('R'):  # rename
            try:
                oldp = next(it).decode('utf-8','replace'); newp = next(it).decode('utf-8','replace')
            except StopIteration:
                continue
            out.append({"status":"R", "path": newp, "old": oldp})
        else:
            status = parts[0][:1]
            path = parts[1] if len(parts)>1 else ''
            out.append({"status":status, "path": path})
    return out

changed = []
# HEAD diff
try:
    with open("/tmp/_chg_z.txt","rb") as f:
        sys.stdin = f; changed.extend(parse_z_status(sys.stdin))
except FileNotFoundError:
    pass

# Untracked
try:
    with open("/tmp/_untracked_z.txt","rb") as f:
        data = f.read().split(b'\x00')
        for p in data:
            if not p: continue
            changed.append({"status":"U", "path": p.decode('utf-8','replace')})
except FileNotFoundError:
    pass

# Deduplicate, keep last status
seen={}
for item in changed:
    seen[item["path"]] = item

print(json.dumps({"changed": list(seen.values())}))
PY

jq -r '.changed[].path' /tmp/_changed.json 2>/dev/null | LC_ALL=C sort -u > "$LIST" || echo -n > "$LIST"

# 2) Snapshot copy (exclude *.zip). Keep directory structure under SNAP_DIR.
mkdir -p "$SNAP_DIR"
while IFS= read -r rel; do
  [[ -z "$rel" ]] && continue
  [[ ! -e "$rel" ]] && continue               # skip deleted files
  [[ "$rel" == *.zip ]] && continue           # exclude zip files
  destdir="${SNAP_DIR}/$(dirname "$rel")"
  mkdir -p "$destdir"
  # Preserve mode/time; copy file content
  cp -p "$rel" "${SNAP_DIR}/$rel"
done < "$LIST"

# 3) Create a binary-safe diff patch vs HEAD for reference
git diff --binary HEAD > "$PATCH" || true

# 4) Build manifest with sha256, size, status (for existing files); include deletions.
python3 - <<'PY' > "$MANIFEST"
import json, os, hashlib, sys
with open("/tmp/_changed.json","r",encoding="utf-8") as f:
    changed = {e["path"]: e for e in json.load(f)["changed"]}
def sha256_of(path):
    h=hashlib.sha256()
    with open(path,'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()
entries=[]
for rel, meta in changed.items():
    entry={"path": rel, "status": meta["status"]}
    if os.path.exists(rel) and not rel.endswith(".zip"):
        try:
            entry["size"] = os.path.getsize(rel)
            entry["sha256"] = sha256_of(rel)
        except Exception as e:
            entry["error"] = f"{type(e).__name__}: {e}"
    else:
        entry["size"] = None
        entry["sha256"] = None
    entries.append(entry)
print(json.dumps({
    "card": os.environ.get("CARD_ID",""),
    "base": "HEAD",
    "count": len(entries),
    "files": entries
}, ensure_ascii=False, indent=2))
PY

# 5) Announce artifacts (machine-readable markers)
echo "[snapshot_dir] $SNAP_DIR"
echo "[snapshot_manifest] $MANIFEST"
echo "[snapshot_list] $LIST"
echo "[snapshot_diff] $PATCH"
SH
chmod +x scripts/make_change_snapshot.sh
# --- HDCoder postlude: bundle checksums (no duplicate artifacts) ---
# Re-extract CARD id (same logic as prelude) so this block is robust even if moved.
__CARD_ID_POST=""
__args_post=("$@")
for i in "${!__args_post[@]}"; do
  case "${__args_post[$i]}" in
    --card=*) __CARD_ID_POST="${__args_post[$i]#--card=}" ;;
    --card) if [ $((i+1)) -lt ${#__args_post[@]} ]; then __CARD_ID_POST="${__args_post[$((i+1))]}"; fi ;;
  esac
done
: "${__CARD_ID_POST:=${__CARD_ID:-CARD-UNSPECIFIED}}"

# Find the newest source bundle + companions for this card
__BUNDLE_ZIP="$(ls -1t "audit/${__CARD_ID_POST}_source_bundle_"*.zip 2>/dev/null | head -n 1 || true)"
__BUNDLE_MAN="$(ls -1t "audit/${__CARD_ID_POST}_source_bundle_"*_MANIFEST.json 2>/dev/null | head -n 1 || true)"
__BUNDLE_LIST="$(ls -1t "audit/${__CARD_ID_POST}_source_bundle_"*__filelist.txt 2>/dev/null | head -n 1 || true)"

# Use the same timestamp as the prelude if available; otherwise generate a fresh one.
__STAMP_POST="${__STAMP:-$(date -u +%Y%m%dT%H%M%SZ)}"
__SHA_OUT="audit/${__CARD_ID_POST}_artifacts_sha256_${__STAMP_POST}.txt"

# Compute SHA256s (only for files that exist)
: > "${__SHA_OUT}"
if [ -n "${__BUNDLE_ZIP}" ] && [ -f "${__BUNDLE_ZIP}" ]; then sha256sum "${__BUNDLE_ZIP}" >> "${__SHA_OUT}"; fi
if [ -n "${__BUNDLE_MAN}" ] && [ -f "${__BUNDLE_MAN}" ]; then sha256sum "${__BUNDLE_MAN}" >> "${__SHA_OUT}"; fi
if [ -n "${__BUNDLE_LIST}" ] && [ -f "${__BUNDLE_LIST}" ]; then sha256sum "${__BUNDLE_LIST}" >> "${__SHA_OUT}"; fi
# Also checksum the prelude manifests if present (names defined in prelude)
if [ -n "${__SNAP_MAN:-}" ] && [ -f "${__SNAP_MAN}" ]; then sha256sum "${__SNAP_MAN}" >> "${__SHA_OUT}"; fi
if [ -n "${__FF_JSON:-}" ] && [ -f "${__FF_JSON}" ]; then sha256sum "${__FF_JSON}" >> "${__SHA_OUT}"; fi

# Announce one line so it shows up in the closeout log
echo "[checksums] ${__SHA_OUT}"
# --- end HDCoder postlude ---
