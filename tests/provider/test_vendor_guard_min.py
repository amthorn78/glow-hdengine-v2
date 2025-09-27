import pytest
from adapter.env_guard import EnvGuardError
from engine.config import provider_loader

def test_vendor_refuses_under_safe_mode(monkeypatch, tmp_path):
    monkeypatch.setenv("ENGINE_SECRETS_DIR", str(tmp_path))  # force empty
    monkeypatch.setenv("SAFE_MODE", "1")
    monkeypatch.setenv("ENGINE_PROVIDER", "vendor_http")
    with pytest.raises(EnvGuardError) as e:
        provider_loader.resolve_provider()
    assert getattr(e.value, "code", "") in ("PROVIDER_UNAVAILABLE", "PROVIDER_MISCONFIGURED")