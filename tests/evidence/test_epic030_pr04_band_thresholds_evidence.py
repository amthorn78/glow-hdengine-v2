"""HDE-EPIC030 PR-04 band-threshold records: frozen history (HDE-EPIC043 WU-PR-09).

The generator no longer regenerates its records, because the v1 thresholds it
compared are retired by the switch. These tests pin the frozen bytes:

* write mode refuses with ``FROZEN_HISTORY_NOT_REGENERATED`` and writes nothing;
* ``--check`` passes on the repository's committed records;
* an altered copy is named by the check (a negative control on its named check);
* the generator imports no retired v1 module.

Retired with the subject: the former regeneration case
(``test_pr04_identity_status_fails_when_ab_ba_hashes_differ``), which exercised
v1 threshold comparison and AB/BA hashing in write mode.
"""
from __future__ import annotations

import ast
import hashlib
import importlib
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GENERATOR = ROOT / "tools" / "evidence" / "generate_epic030_pr04_band_thresholds_evidence.py"
RETIRED = ("engine.compat.thresholds", "engine.magic10")


def _module():
    return importlib.import_module("tools.evidence.generate_epic030_pr04_band_thresholds_evidence")


def test_frozen_pins_equal_the_committed_records() -> None:
    mod = _module()
    for name, (sha256, size) in mod.FROZEN_RECORDS.items():
        raw = (mod.OUT_DIR / name).read_bytes()
        assert (hashlib.sha256(raw).hexdigest(), len(raw)) == (sha256, size), name
    assert mod.frozen_record_mismatches() == []


def test_write_mode_refuses_and_writes_nothing(tmp_path, monkeypatch, capsys) -> None:
    mod = _module()
    out = tmp_path / "pr-04"
    monkeypatch.setattr(mod, "OUT_DIR", out)
    assert mod.main([]) == 2
    assert capsys.readouterr().err == "FROZEN_HISTORY_NOT_REGENERATED\n"
    assert not out.exists()


def test_check_passes_on_the_repository() -> None:
    result = subprocess.run([sys.executable, str(GENERATOR), "--check"], cwd=ROOT, capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
    assert "pinned SHA-256 and size" in result.stdout


def test_check_names_an_altered_record(tmp_path, monkeypatch, capsys) -> None:
    mod = _module()
    copy = tmp_path / "pr-04"
    shutil.copytree(mod.OUT_DIR, copy)
    target = copy / "band_thresholds_diff.json"
    target.write_bytes(target.read_bytes().replace(b"PASS", b"FAIL", 1))
    assert mod.frozen_record_mismatches(copy) == ["band_thresholds_diff.json"]
    monkeypatch.setattr(mod, "OUT_DIR", copy)
    assert mod.main(["--check"]) == 1
    assert capsys.readouterr().err == "FROZEN_RECORD_MISMATCH:band_thresholds_diff.json\n"


def test_generator_imports_no_retired_module() -> None:
    tree = ast.parse(GENERATOR.read_text(encoding="utf-8"))
    imported = {node.module for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)}
    imported |= {alias.name for node in ast.walk(tree) if isinstance(node, ast.Import) for alias in node.names}
    assert not any(name == prefix or name.startswith(prefix + ".") for name in imported for prefix in RETIRED)
