import os, json, pathlib, importlib
import pytest

from engine.config import provider_loader

def _unset(*names):
    for n in names:
        os.environ.pop(n, None)

def test_vendor_refuses_in_safe_mode(monkeypatch, tmp_path):
    _unset("ENGINE_ENV","APP_ENV","ENGINE_PROVIDER","SAFE_MODE")
    monkeypatch.setenv("SAFE_MODE","1")
    monkeypatch.setenv("ENGINE_PROVIDER","vendor_http")
    with pytest.raises(Exception) as ei:
        provider_loader.resolve_provider()
    assert getattr(ei.value, "code", "") == "PROVIDER_UNAVAILABLE"

def test_vendor_constructs_in_dev_but_call_raises(monkeypatch):
    _unset("ENGINE_ENV","APP_ENV","ENGINE_PROVIDER","SAFE_MODE")
    monkeypatch.setenv("SAFE_MODE","0")
    monkeypatch.setenv("ENGINE_PROVIDER","vendor_http")
    prov = provider_loader.resolve_provider()
    with pytest.raises(Exception) as ei:
        prov.get_pair_profile({"a":1},{"b":2}, None)
    assert getattr(ei.value, "code", "") == "PROVIDER_UNAVAILABLE"

def test_prod_fails_on_env_override(monkeypatch):
    _unset("ENGINE_ENV","APP_ENV","ENGINE_PROVIDER","SAFE_MODE")
    monkeypatch.setenv("ENGINE_ENV","prod")
    monkeypatch.setenv("ENGINE_PROVIDER","internal_engine")
    with pytest.raises(Exception) as ei:
        provider_loader.resolve_provider()
    assert getattr(ei.value, "code", "") == "CANON_TOGGLES_OVERRIDE_IN_PROD"

def test_prod_fails_on_secrets_override(monkeypatch, tmp_path):
    _unset("ENGINE_ENV","APP_ENV","ENGINE_PROVIDER","SAFE_MODE")
    monkeypatch.setenv("APP_ENV","prod")
    secrets = pathlib.Path("secrets"); secrets.mkdir(exist_ok=True)
    (secrets/"provider.json").write_text(json.dumps({"provider":"fixtures"}), encoding="utf-8")
    try:
        with pytest.raises(Exception) as ei:
            provider_loader.resolve_provider()
        assert getattr(ei.value, "code", "") == "CANON_TOGGLES_OVERRIDE_IN_PROD"
    finally:
        (secrets/"provider.json").unlink(missing_ok=True)

def test_malformed_secrets_is_misconfigured(monkeypatch):
    _unset("ENGINE_ENV","APP_ENV","ENGINE_PROVIDER","SAFE_MODE")
    import os, pathlib
    secrets_dir = pathlib.Path(os.environ.get("ENGINE_SECRETS_DIR", "secrets"))
    secrets_dir.mkdir(parents=True, exist_ok=True)
    f = secrets_dir / "provider.json"
    f.write_text("{badjson", encoding="utf-8")
    try:
        with pytest.raises(Exception) as ei:
            provider_loader.resolve_provider()
        assert getattr(ei.value, "code", "") in {"PROVIDER_MISCONFIGURED","PROVIDER_SECRETS_PARSE_ERROR"}
    finally:
        f.unlink(missing_ok=True)

def test_decision_artifact_written_by_default(monkeypatch):
    _unset("ENGINE_ENV","APP_ENV","ENGINE_PROVIDER","SAFE_MODE")
    import pathlib
    # ensure clean slate for this test's expectation
    p = pathlib.Path("artifacts/provider/decision.txt")
    p.parent.mkdir(parents=True, exist_ok=True)
    p.unlink(missing_ok=True)

    # default -> fixtures
    prov = provider_loader.resolve_provider()
    assert prov is not None
    assert p.exists()
    line = p.read_text(encoding="utf-8").strip()
    assert line == "provider=fixtures source=default"