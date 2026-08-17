#!/usr/bin/env python3
"""Validate the current manifest-derived release identity input.

Current release derivatives are built only in an external isolated attestation.
The checked-in EPIC022 release evidence is a frozen historical capture, so this
source-tree compatibility entrypoint must not compare it with the current
manifest or treat it as current release identity.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.release_id_recompute import check_manifest_only
from tools.config.artifacts import require_closed_rails


def main() -> int:
    require_closed_rails()
    return check_manifest_only(ROOT / "catalog" / "manifest.json")


if __name__ == "__main__":
    raise SystemExit(main())
