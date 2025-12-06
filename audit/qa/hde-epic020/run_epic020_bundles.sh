#!/usr/bin/env bash
set -euo pipefail

export SAFE_MODE="${SAFE_MODE:-1}"
export ALLOW_NETWORK="${ALLOW_NETWORK:-0}"
export LC_ALL="${LC_ALL:-C}"
export LANG="${LANG:-C}"
export TZ="${TZ:-UTC}"
export APP_ENV="${APP_ENV:-dev}"

python -m tools.evidence.epic020_bundle build --epic-id HDE-EPIC020
python tools/evidence/update_evidence_index.py --epic-id HDE-EPIC020 --check

python - <<'PY'
import json
from pathlib import Path
index = json.loads(Path("docs/evidence/INDEX.json").read_text())
paths = []
for entry in index:
    if entry.get("epic_id") != "HDE-EPIC020":
        continue
    if entry.get("record_type") not in {"epic020_bundle", "epic020_bundle_manifest"}:
        continue
    paths.append((entry.get("artifact_key"), entry.get("discovered_physical_path")))
for token, path in sorted(paths):
    print(f"{token}: {path}")
PY
