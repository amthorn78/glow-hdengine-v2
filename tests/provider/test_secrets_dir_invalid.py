import pathlib
import pytest
from adapter.env_guard import EnvGuardError
from engine.config import provider_loader

def test_engine_secrets_dir_nonexistent_is_invalid(tmp_path, monkeypatch):
    bad = tmp_path / "does_not_exist"
    monkeypatch.setenv("ENGINE_SECRETS_DIR", str(bad))
    with pytest.raises(EnvGuardError) as ei:
        provider_loader.resolve_provider()
    assert ei.value.code == "PROVIDER_SECRETS_DIR_INVALID"

def test_engine_secrets_dir_pointing_to_file_is_invalid(tmp_path, monkeypatch):
    f = tmp_path / "not_a_dir"
    f.write_text("x", encoding="utf-8")
    monkeypatch.setenv("ENGINE_SECRETS_DIR", str(f))
    with pytest.raises(EnvGuardError) as ei:
        provider_loader.resolve_provider()
    assert ei.value.code == "PROVIDER_SECRETS_DIR_INVALID"