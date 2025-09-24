#!/usr/bin/env python3
from __future__ import annotations
import re, sys, subprocess
from pathlib import Path
from datetime import datetime, timezone

from core.stable.freeze import iter_records
from core.stable.identity import compute_release_id

CFILE = Path("core/stable/identity_constants.py")
ART = Path("artifacts"); ART.mkdir(exist_ok=True)
DOCS = Path("docs"); DOCS.mkdir(exist_ok=True)

def _write_checksums():
    recs = list(iter_records("."))
    out = ART / "CHECKSUMS.txt"
    lines = [f"{r.sha256}  {r.path}" for r in sorted(recs, key=lambda r: r.path)]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return recs, out

def _compute_release_id(recs):
    pairs = [(r.path, r.sha256) for r in recs]
    return compute_release_id(pairs)

def _write_identity_txt(rid: str, n: int):
    (ART / "identity.txt").write_text(
        f"release_id={rid} artifact_count={n}\n", encoding="utf-8"
    )

def _patch_constants(rid: str):
    src = CFILE.read_text(encoding="utf-8")
    src = re.sub(r'RELEASE_ID\s*=\s*".*?"', f'RELEASE_ID = "{rid}"', src)
    tag = datetime.now(timezone.utc).strftime("v2-%Y%m%d")
    src = re.sub(r'ENGINE_TAG\s*=\s*".*?"', f'ENGINE_TAG = "{tag}"', src)
    CFILE.write_text(src, encoding="utf-8")

def _fresh_verify():
    code = (
        "from core.stable.freeze import iter_records;"
        "from core.stable.identity import compute_release_id;"
        "from core.stable.identity_constants import RELEASE_ID;"
        "pairs=[(r.path,r.sha256) for r in iter_records('.')];"
        "import sys; sys.exit(0 if compute_release_id(pairs)==RELEASE_ID else 2)"
    )
    rc = subprocess.run([sys.executable, "-c", code]).returncode
    if rc != 0:
        raise SystemExit("fresh-process verify failed")

def _append_sync_log(rid: str, n: int):
    zulu = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    line = f"{zulu} release_id={rid} artifacts={n} operator=ISIS\n"
    log = Path("docs/SYNC_LOG.md")
    prev = log.read_text(encoding="utf-8") if log.exists() else ""
    log.write_text(prev + line, encoding="utf-8")

def main() -> int:
    recs, _ = _write_checksums()
    rid = _compute_release_id(recs)
    _write_identity_txt(rid, len(recs))
    _patch_constants(rid)
    _fresh_verify()
    _append_sync_log(rid, len(recs))
    print("IDENTITY OK", rid)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
