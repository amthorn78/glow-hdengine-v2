from __future__ import annotations

import importlib
from pathlib import Path


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_pr04_identity_status_fails_when_ab_ba_hashes_differ(monkeypatch):
    mod = importlib.import_module("tools.evidence.generate_epic030_pr04_band_thresholds_evidence")

    test_root = mod.ROOT / "tmp" / "pytest_epic030_pr04_identity_status"
    out_dir = test_root / "audit" / "qa" / "hde-epic030" / "pr-04"
    _write(test_root / "artifacts" / "compat" / "AB.json", '{"k":"ab"}\n')
    _write(test_root / "artifacts" / "compat" / "BA.json", '{"k":"ba"}\n')
    _write(
        test_root / "artifacts" / "thresholds" / "band_edges.json",
        '{"bands":["Cool","Open","Warm","Glow"],"clamp":[0,100],"edges":[24,49,74,100],"rounding":"ROUND_HALF_UP","schema":"band_edges.v1","source":"math/thresholds.json","version":"1"}\n',
    )

    monkeypatch.setattr(mod, "OUT_DIR", out_dir)
    monkeypatch.setattr(mod, "COMPAT_AB_PATH", test_root / "artifacts" / "compat" / "AB.json")
    monkeypatch.setattr(mod, "COMPAT_BA_PATH", test_root / "artifacts" / "compat" / "BA.json")
    monkeypatch.setattr(mod, "BAND_EDGES_PATH", test_root / "artifacts" / "thresholds" / "band_edges.json")
    monkeypatch.setattr(mod, "ensure_determinism_env", lambda: None)

    mod.generate()

    identity_text = (out_dir / "band_thresholds_identity_hash.txt").read_text(encoding="utf-8")
    assert "ab_ba_identity_match: False\n" in identity_text
    assert "status: FAIL\n" in identity_text
