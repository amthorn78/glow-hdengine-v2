#!/usr/bin/env bash
set -euo pipefail

ART="artifacts"; mkdir -p "$ART"
MAN="$ART/release_pack_manifest.json"
RID="$ART/release_id.txt"

# Respect incoming FILES (newline-separated). If absent, use defaults.
if [[ -z "${FILES:-}" ]]; then
  FILES=$'schemas/reader.v1.schema.json
goldens/reader/v1/g01_minimal_ineligible.json
goldens/reader/v1/g03_harmony_open.json
goldens/reader/v1/g04_harmony_warm.json
goldens/reader/v1/g05_harmony_cool.json
goldens/reader/v1/g07_harmony_glow.json
goldens/reader/v1/g06_error_invalid_input.json
goldens/reader/v1/g02_ab_ba_parity_A.jsonl
goldens/reader/v1/g02_ab_ba_parity_B.jsonl'
fi
export FILES

python3 - <<'PY'
import json, hashlib, os
from pathlib import Path

ART = Path("artifacts"); ART.mkdir(parents=True, exist_ok=True)
MAN = ART / "release_pack_manifest.json"
RID = ART / "release_id.txt"

files = [p for p in os.environ["FILES"].splitlines() if p.strip()]
with MAN.open("w", encoding="utf-8") as f:
    json.dump({"files": files}, f, ensure_ascii=False, indent=2)

h = hashlib.sha256()
for p in files:
    with open(p, "rb") as fh:
        h.update(fh.read())

with RID.open("w", encoding="utf-8") as f:
    f.write(h.hexdigest() + "\n")

print("WROTE", str(MAN), str(RID))
PY
