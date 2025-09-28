from __future__ import annotations
import pytest
from adapter.env_guard import validate_or_fail, EnvGuardError

def _call(env):
    validate_or_fail(env)

def test_engine_env_prod_raises():
    with pytest.raises(EnvGuardError):
        _call({"ENGINE_ENV": "prod", "ALLOW_NETWORK": "1"})

def test_app_env_overrides_engine_env():
    # APP_ENV non-prod wins over ENGINE_ENV=prod; even with forbidden keys, no raise
    _call({"APP_ENV": "dev", "ENGINE_ENV": "prod", "HD_ADMIN": "1"})

def test_prod_aliases_and_whitespace():
    for alias in ["prod", "production", "live", " production ", " PROD "]:
        env = {"APP_ENV": alias, "ALLOW_NETWORK": "1"}
        if alias.strip().lower() in {"prod","production","live"}:
            with pytest.raises(EnvGuardError):
                _call(env)
        else:
            _call(env)

def test_empty_app_env_falls_back_to_engine_env():
    with pytest.raises(EnvGuardError):
        _call({"APP_ENV": "", "ENGINE_ENV": "production", "HD_ADMIN": "1"})
