import pytest
from adapter.env_guard import EnvGuardError  # typed (code, message, details)
from engine.config.provider_loader import resolve_provider

def test_unknown_provider_in_secrets_raises_misconfigured(tmp_path, monkeypatch):
    monkeypatch.setenv("ENGINE_SECRETS_DIR", str(tmp_path))
    (tmp_path / "provider.json").write_text('{"provider":"unknown_name"}', encoding="utf-8")
    with pytest.raises(EnvGuardError) as e:
        resolve_provider()
    assert e.value.code == "PROVIDER_MISCONFIGURED"
