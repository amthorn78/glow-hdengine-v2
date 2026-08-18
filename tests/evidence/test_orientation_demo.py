from __future__ import annotations

import json
from pathlib import Path

from tools.evidence import orientation_demo


def test_orientation_report_matches_files(tmp_path):
    orientation_demo.generate_orientation(check=True)
    text = Path("audit/gates/topology/orientation_demo.txt").read_text(encoding="utf-8")
    assert text.startswith("orientation demo (evidence skeleton)\n")
    assert "status: ok" in text


def test_orientation_write_delegates_to_updater(monkeypatch):
    calls = []
    monkeypatch.setattr(orientation_demo, "update_evidence_index", lambda argv: calls.append(argv))
    orientation_demo.generate_orientation(check=False)
    assert calls == [[]]


def test_orientation_detects_mismatch(tmp_path, monkeypatch):
    entries = [{"artifact_key": "demo", "discovered_physical_path": "missing/path.txt"}]
    records = []
    mirror_lines = [
        json.dumps(
            {
                "artifact_key": "index.machine_mirror",
                "discovered_physical_path": "docs/evidence/INDEX.json",
                "sha256": "",
                "size_bytes": 0,
            }
        )
        + "\n"
    ]
    messages, total = orientation_demo._validate(entries, records, mirror_lines=mirror_lines)
    assert total == 1
    assert messages and messages[0].startswith("MISSING_MIRROR")
