import json
import pathlib

import pytest

pytestmark = pytest.mark.epic006


def test_registry_report_exists_and_is_canonical():
    p = pathlib.Path("artifacts/registry/registry_report.json")
    assert p.exists()
    data = p.read_text(encoding="utf-8")
    assert data.endswith("\n") and "\n\n" not in data
    obj = json.loads(data)
    assert isinstance(obj, dict)
    assert obj.get("schema") == "registry_report.v1"


def test_registry_report_writer_preserves_selected_root_and_is_repeatable(tmp_path, monkeypatch):
    from tests.config.helpers import catalog_root, closed_rails_env
    from tools.generate_registry_report import build_registry_report, write_registry_report
    from engine.serializer.canon import sercanon

    for name in ("LC_ALL", "LANG", "TZ", "SAFE_MODE", "ALLOW_NETWORK"):
        monkeypatch.setenv(name, closed_rails_env()[name])
    root = catalog_root(tmp_path)
    target = write_registry_report(root)
    before = target.read_bytes(), target.stat().st_mtime_ns
    assert target == root / "artifacts/registry/registry_report.json"
    assert target.read_bytes() == sercanon(build_registry_report(root), sort_keys=True)
    write_registry_report(root)
    assert (target.read_bytes(), target.stat().st_mtime_ns) == before
