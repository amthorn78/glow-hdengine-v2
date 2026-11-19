#!/usr/bin/env python3
"""EPIC030 PR-04 band-threshold/tuning evidence: frozen history (HDE-EPIC043 WU-PR-09).

The records under ``audit/qa/hde-epic030/pr-04/`` are capture-time history of the
v1 band thresholds, which the switch retires.  This generator no longer
regenerates them:

* write mode (no argument) refuses with ``FROZEN_HISTORY_NOT_REGENERATED`` and
  writes nothing;
* ``--check`` verifies each frozen record's SHA-256 and size against the
  constants pinned below and admits no release.

It imports no retired v1 module.
"""
from __future__ import annotations

import datetime as _dt  # noqa: F401  kept: the architecture snapshot keys on this file's imported modules
import hashlib
import json  # noqa: F401  kept: the architecture snapshot keys on this file's imported modules
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import ensure_determinism_env
from engine.serializer.canon import sercanon  # noqa: F401  kept: the snapshot keys on imported modules

OUT_DIR = ROOT / "audit" / "qa" / "hde-epic030" / "pr-04"
FROZEN_HISTORY_NOT_REGENERATED = "FROZEN_HISTORY_NOT_REGENERATED"
FROZEN_RECORD_MISMATCH = "FROZEN_RECORD_MISMATCH"
# Frozen record -> (SHA-256, size in bytes), as committed at HDE-EPIC043 WU-PR-09's base.
FROZEN_RECORDS = {
    "band_edges_binding.log": ("7767849cd7ba323fe6725f6096b1041578a800607c886635809b43ecbd509112", 392),
    "band_thresholds_diff.json": ("38abfd9201e72e37d4c6c0f20b80dd3ae2db6ce02061367efa979f53886283fb", 693),
    "band_thresholds_identity_hash.txt": ("889a92696521c425a7a482957b32f1d51042b72a7ceaba949a274b4e0db4ac9d", 506),
}


def frozen_record_mismatches(out_dir: Path | None = None) -> list[str]:
    """Return the names of frozen records whose bytes differ from their pins."""
    base = OUT_DIR if out_dir is None else out_dir
    mismatched = []
    for name, (sha256, size) in FROZEN_RECORDS.items():
        path = base / name
        raw = path.read_bytes() if path.is_file() else None
        if raw is None or len(raw) != size or hashlib.sha256(raw).hexdigest() != sha256:
            mismatched.append(name)
    return mismatched


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else list(argv)
    if args != ["--check"]:
        print(FROZEN_HISTORY_NOT_REGENERATED, file=sys.stderr)
        return 2
    ensure_determinism_env()
    mismatched = frozen_record_mismatches()
    if mismatched:
        print(f"{FROZEN_RECORD_MISMATCH}:{','.join(mismatched)}", file=sys.stderr)
        return 1
    print("checked frozen HDE-EPIC030 PR-04 band-threshold records (pinned SHA-256 and size)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
