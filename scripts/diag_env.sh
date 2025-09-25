#!/usr/bin/env bash
set -euo pipefail
echo "=== DIAG: basic ==="
pwd
python3 -V
pip --version || true
pytest --version || true

echo
echo "=== DIAG: repo layout (top, 2 levels) ==="
ls -la
printf "\n---\n"
( command -v tree >/dev/null 2>&1 && tree -L 2 || find . -maxdepth 2 -type d -printf "%p\n" ) | sed 's|^\./||'

echo
echo "=== DIAG: key files if present ==="
for p in pyproject.toml setup.py requirements*.txt RUN.md scripts/hd_cli.py; do
  [ -f "$p" ] && echo "--- $p" && sed -n '1,120p' "$p" | sed 's/^/    /'
done

echo
echo "=== DIAG: Python import probes ==="
python3 - <<'PY'
import sys, os, importlib, pkgutil, pathlib, json
print("sys.executable:", sys.executable)
print("sys.path (first 8):")
for i,p in enumerate(sys.path[:8]):
    print(f"  {i}: {p}")
root = pathlib.Path.cwd()
candidates = [root, root/"src", root/"hd_core", root/"core"]
print("\nexists:", {str(p): p.exists() for p in candidates})

def try_import(name):
    try:
        m = importlib.import_module(name)
        print(f"OK import {name} from", getattr(m, "__file__", None))
        return m
    except Exception as e:
        print(f"FAIL import {name} -> {type(e).__name__}: {e}")

for name in ("core", "hd_core", "core.pipeline.compute", "hd_core.pipeline.compute"):
    try_import(name)

print("\nsite-packages scan (top-level pkgs containing 'core'):")
site_dirs = [p for p in sys.path if p and p.endswith("site-packages")]
seen = set()
for sd in site_dirs:
    for m in pkgutil.iter_modules([sd]):
        if "core" in m.name and m.name not in seen:
            print("  ", m.name)
            seen.add(m.name)
PY

echo
echo "=== DIAG: pytest collection sanity (no run) ==="
pytest -q --collect-only 2>/dev/null | head -n 60 || true
echo
echo "=== DIAG COMPLETE ==="
