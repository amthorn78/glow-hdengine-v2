from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

from engine.compat.identity import dev_compat_identity

ARTIFACTS = (
    Path("artifacts/writer/conjunction_write_readback.log"),
    Path("artifacts/writer/conjunction_writer_summary.json"),
)
OPEN_DEV_RAILS = {
    "APP_ENV": "dev",
    "SAFE_MODE": "0",
    "ALLOW_NETWORK": "1",
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
}


def test_dev_conjunction_identity_evidence_is_current_and_nonwriting():
    env = os.environ.copy()
    env.update(OPEN_DEV_RAILS)
    before = {path: path.read_bytes() for path in ARTIFACTS}

    subprocess.run(
        [
            sys.executable,
            "tools/evidence/generate_conjunction_writer_evidence.py",
            "--check",
        ],
        check=True,
        env=env,
    )

    assert {path: path.read_bytes() for path in ARTIFACTS} == before
    summary = json.loads(
        Path("artifacts/writer/conjunction_writer_summary.json").read_bytes()
    )
    assert summary["checks"]["writer_dev_identity"] is True
    assert summary["checks"]["reader_dev_identity"] is True
    assert dev_compat_identity() == {
        "engine_tag": "dev",
        "release_id": "dev",
        "invocation_tag": "INV-DEV",
    }
