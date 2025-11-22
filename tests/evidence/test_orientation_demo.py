from __future__ import annotations

from pathlib import Path

from tools.evidence import orientation_demo


def test_orientation_report_matches_files(tmp_path):
    orientation_demo.generate_orientation(check=False)
    text = Path("audit/gates/topology/orientation_demo.txt").read_text(encoding="utf-8")
    assert text.startswith("orientation demo (evidence skeleton)\n")
    assert "status: ok" in text


def test_orientation_detects_mismatch(tmp_path, monkeypatch):
    entries = [{"artifact_key": "demo", "discovered_physical_path": "missing/path.txt"}]
    records = []
    messages, total = orientation_demo._validate(entries, records)
    assert total == 1
    assert messages and messages[0].startswith("MISSING_MIRROR")
