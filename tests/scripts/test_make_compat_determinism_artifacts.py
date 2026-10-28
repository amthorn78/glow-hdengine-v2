"""scripts/make_compat_determinism_artifacts.py after its chart-loader migration.

HDE-EPIC041 WU-PR-02 changed only its import, to adapter.chart_orchestration.
engine.compat.compute has no compat_public, so the script still stops before
it loads a chart: exit 2, one stderr line, and nothing written.
"""
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts/make_compat_determinism_artifacts.py"


def test_generator_exits_2_and_writes_nothing_from_any_working_directory(tmp_path):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    env["PYTHONPATH"] = os.pathsep.join(p for p in (str(ROOT), env.get("PYTHONPATH", "")) if p)
    proc = subprocess.run([sys.executable, str(SCRIPT)], cwd=tmp_path, env=env, capture_output=True, text=True)
    assert (proc.returncode, proc.stdout, proc.stderr) == (2, "", "compat_public not implemented\n")
    assert list(tmp_path.iterdir()) == []
