#!/usr/bin/env python3
"""Run the final LF gate for evidence artifacts."""
from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env


def main() -> int:
    try:
        ensure_determinism_env(apply=True)
    except DeterminismEnvError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    script = ROOT / "ci" / "checks" / "check_final_lf.sh"
    if not script.exists():
        print(f"MISSING:{script}", file=sys.stderr)
        return 1

    result = subprocess.run([str(script)], cwd=str(ROOT), env=os.environ.copy(), check=False)
    return result.returncode


if __name__ == "__main__":  # pragma: no cover - CLI entrypoint
    raise SystemExit(main())
