#!/usr/bin/env python3
"""Compatibility wrapper for EPIC024 step logs manifest refresh."""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.evidence.refresh_epic024_step_logs_manifest import main


if __name__ == "__main__":
    raise SystemExit(main())
