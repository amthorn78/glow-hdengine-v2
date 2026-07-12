from __future__ import annotations
import pytest
from adapter.env_guard import validate_or_fail, EnvGuardError

def _call(env):
    validate_or_fail(env)

def test_engine_env_prod_accepts_canonical_rails():
    _call({"ENGINE_ENV": "prod", "SAFE_MODE": "0", "ALLOW_NETWORK": "1"})

def test_app_env_overrides_engine_env():
    # APP_ENV non-prod wins over ENGINE_ENV=prod; even with forbidden keys, no raise
    _call({"APP_ENV": "dev", "ENGINE_ENV": "prod", "HD_ADMIN": "1"})

def test_prod_aliases_accept_canonical_rails():
    for alias in ["prod", "production", "live", " production ", " PROD "]:
        _call({"APP_ENV": alias, "SAFE_MODE": "0", "ALLOW_NETWORK": "1"})

def test_prod_aliases_still_reject_forbidden_overrides():
    for alias in ["prod", "production", "live", " production ", " PROD "]:
        with pytest.raises(EnvGuardError):
            _call({"APP_ENV": alias, "ALLOW_NETWORK": "1", "HD_ADMIN": "1"})

def test_empty_app_env_falls_back_to_engine_env():
    with pytest.raises(EnvGuardError):
        _call({"APP_ENV": "", "ENGINE_ENV": "production", "HD_ADMIN": "1"})
