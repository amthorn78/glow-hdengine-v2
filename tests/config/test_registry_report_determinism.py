import hashlib
import json
import subprocess
import sys
from pathlib import Path


def _run_generator() -> bytes:
    subprocess.run([sys.executable, "tools/generate_registry_report.py"], check=True)
    path = Path("artifacts/registry/registry_report.json")
    return path.read_bytes()


def test_registry_report_two_run_identity(tmp_path: Path) -> None:
    first = _run_generator()
    second = _run_generator()
    assert first == second
    data = json.loads(first.decode("utf-8"))
    assert data["schema"] == "registry_report.v1"
    assert first.endswith(b"\n")
    assert hashlib.sha256(first).hexdigest() == hashlib.sha256(second).hexdigest()

