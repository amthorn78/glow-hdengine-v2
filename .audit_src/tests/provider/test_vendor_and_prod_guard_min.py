import pytest
from adapter.env_guard import EnvGuardError
from engine.config.provider_loader import resolve_provider

def _unset(monkeypatch, *names):
    for n in names:
        monkeypatch.delenv(n, raising=False)

def test_vendor_refuses_in_safe_mode(tmp_path, monkeypatch):
    # Empty secrets so env path is exercised
    monkeypatch.setenv("ENGINE_SECRETS_DIR", str(tmp_path))
    _unset(monkeypatch, "APP_ENV", "ENGINE_ENV", "ENGINE_PROVIDER", "SAFE_MODE")
    monkeypatch.setenv("ENGINE_ENV", "dev")
    monkeypatch.setenv("SAFE_MODE", "1")
    monkeypatch.setenv("ENGINE_PROVIDER", "vendor_http")
    with pytest.raises(EnvGuardError) as e:
        # S2 pin: vendor refuses to construct in SAFE_MODE=1
        resolve_provider()
    assert e.value.code == "PROVIDER_UNAVAILABLE"

def test_vendor_constructs_when_safe_mode_off_but_call_raises(tmp_path, monkeypatch):
    monkeypatch.setenv("ENGINE_SECRETS_DIR", str(tmp_path))
    _unset(monkeypatch, "APP_ENV", "ENGINE_ENV", "ENGINE_PROVIDER", "SAFE_MODE")
    monkeypatch.setenv("ENGINE_ENV", "dev")
    monkeypatch.setenv("SAFE_MODE", "0")
    monkeypatch.setenv("ENGINE_PROVIDER", "vendor_http")
    prov = resolve_provider()  # allowed to construct in dev when SAFE_MODE=0
    with pytest.raises(EnvGuardError) as e:
        prov.get_pair_profile({"a":1}, {"b":2}, preset=None)
    assert e.value.code == "PROVIDER_UNAVAILABLE"
