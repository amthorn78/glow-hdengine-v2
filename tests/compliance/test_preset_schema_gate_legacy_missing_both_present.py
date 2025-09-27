import os, json, pathlib, pytest
from adapter.wsgi import create_app
from engine.errors import PresetSchemaError

def _write(p: pathlib.Path, data: dict):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

def test_legacy_key_rejected_startup(tmp_path, monkeypatch):
    d = tmp_path / "presets"
    _write(d/"bad_legacy.json", {"constraints":{
        "em_scoring_enabled": True,
        "electromagnetic_scoring_enabled": True,
        "emotional_scoring_enabled": True,
    }})
    monkeypatch.setenv("ENGINE_PRESETS_DIRS", str(d))
    with pytest.raises(PresetSchemaError) as ei:
        create_app()
    assert ei.value.code == "PRESET_SCHEMA_LEGACY_FIELD"

def test_missing_fields_rejected_startup(tmp_path, monkeypatch):
    d = tmp_path / "presets"
    _write(d/"bad_missing.json", {"constraints": {}})
    monkeypatch.setenv("ENGINE_PRESETS_DIRS", str(d))
    with pytest.raises(PresetSchemaError) as ei:
        create_app()
    assert ei.value.code == "PRESET_SCHEMA_MISSING_FIELD"
    assert "electromagnetic_scoring_enabled" in ei.value.message
    assert "emotional_scoring_enabled" in ei.value.message

def test_both_present_accepts_startup(tmp_path, monkeypatch):
    d = tmp_path / "presets"
    _write(d/"good.json", {"constraints":{
        "electromagnetic_scoring_enabled": True,
        "emotional_scoring_enabled": False,
    }})
    monkeypatch.setenv("ENGINE_PRESETS_DIRS", str(d))
    app = create_app()
    # smoke one request
    with app.test_client() as c:
        r = c.get("/reader")
        assert r.status_code in (200, 304, 401, 200)
