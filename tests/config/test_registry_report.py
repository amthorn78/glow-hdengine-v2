import json
import pathlib
import subprocess
import sys

import pytest

pytestmark = pytest.mark.epic006


def test_registry_report_exists_and_is_canonical():
    subprocess.run([sys.executable, "tools/generate_registry_report.py"], check=True)
    p = pathlib.Path("artifacts/registry/registry_report.json")
    assert p.exists()
    data = p.read_text(encoding="utf-8")
    assert data.endswith("\n") and "\n\n" not in data
    obj = json.loads(data)
    assert isinstance(obj, dict)
    assert obj.get("schema") == "registry_report.v1"
