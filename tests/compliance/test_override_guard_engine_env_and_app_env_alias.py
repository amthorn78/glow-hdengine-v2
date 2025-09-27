import os, pathlib, pytest
from adapter.env_guard import EnvGuardError
from adapter.wsgi import create_app

def test_prod_fails_on_env_override(monkeypatch, caplog):
    monkeypatch.setenv("ENGINE_ENV","prod")
    monkeypatch.setenv("HD_TOGGLES","1")  # matches pattern
    with pytest.raises(EnvGuardError) as ei:
        create_app()
    assert getattr(ei.value, "code", "") == "CANON_TOGGLES_OVERRIDE_IN_PROD"

def test_prod_fails_on_file_override_with_app_env_alias(monkeypatch, tmp_path, caplog):
    # Alias prod switch
    monkeypatch.setenv("APP_ENV","prod")
    # Create override file under repo root config/overrides
    base = pathlib.Path("config/overrides")
    base.mkdir(parents=True, exist_ok=True)
    f = base / "x.json"
    f.write_text("{}", encoding="utf-8")
    try:
        with pytest.raises(EnvGuardError) as ei:
            create_app()
        assert getattr(ei.value, "code", "") == "CANON_TOGGLES_OVERRIDE_IN_PROD"
    finally:
        # cleanup
        try: f.unlink()
        except FileNotFoundError: pass

def test_dev_warn_only_continues(monkeypatch):
    monkeypatch.setenv("ENGINE_ENV","dev")
    monkeypatch.setenv("ENGINE_TOGGLES_TEST","1")  # would trip, but dev must pass
    app = create_app()
    with app.test_client() as c:
        r = c.get("/reader")  # route exists already
        assert r.status_code in (200, 304)
