import os, json
from pathlib import Path
from core.canon.validate import detect_prod_overrides

def test_prod_override_file_triggers_fail(tmp_path, monkeypatch):
    monkeypatch.setenv("APP_ENV", "prod")
    ovdir = tmp_path / "config" / "overrides"
    ovdir.mkdir(parents=True, exist_ok=True)
    (ovdir / "x.json").write_text(json.dumps({"k":"v"}), encoding="utf-8")
    code = detect_prod_overrides(base=tmp_path)
    assert code == "CANON_TOGGLES_OVERRIDE_IN_PROD"

def test_prod_env_key_triggers_fail(tmp_path, monkeypatch):
    monkeypatch.setenv("ENGINE_ENV", "prod")
    # KEY name contains TOGGLES (value irrelevant)
    monkeypatch.setenv("HD_TOGGLES", "1")
    code = detect_prod_overrides(base=tmp_path)
    assert code == "CANON_TOGGLES_OVERRIDE_IN_PROD"

def test_dev_returns_none_even_if_overrides_present(tmp_path, monkeypatch):
    monkeypatch.setenv("APP_ENV", "dev")
    os.environ.pop("HD_TOGGLES", None)
    ovdir = tmp_path / "config" / "overrides"
    ovdir.mkdir(parents=True, exist_ok=True)
    (ovdir / "x.json").write_text("{}", encoding="utf-8")
    code = detect_prod_overrides(base=tmp_path)
    assert code is None
