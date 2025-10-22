#!/usr/bin/env python3
import sys, re
from pathlib import Path

ROOT = Path(".").resolve()
# Paths we treat as "emit paths" (public emission happens here)
WATCH_DIRS = ["server", "adapter", "adapter/wsgi.py", "adapter/app.py", "engine/emit", "engine/emit_public.py"]
SKIP_DIRS  = {"tests", "dev", "fixtures", "artifacts", "reports", ".venv", "goldens"}

bad = []
for p in ROOT.rglob("*.py"):
    rel = p.relative_to(ROOT).as_posix()
    # skip noise dirs
    if any(part in SKIP_DIRS for part in rel.split("/")):
        continue
    # only watch emit paths
    if not any(rel == w or rel.startswith(w + "/") for w in WATCH_DIRS):
        continue
    try:
        txt = p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        continue
    for i, line in enumerate(txt.splitlines(), 1):
        if re.search(r"\bjson\.dumps?\s*\(", line):
            bad.append(f"{rel}:{i}:{line.strip()}")

if bad:
    print(f"EMIT_PATH_NO_JSON_DUMPS_FAIL {len(bad)}")
    for row in bad:
        print(row)
    sys.exit(1)

print("EMIT_PATH_NO_JSON_DUMPS_OK")
