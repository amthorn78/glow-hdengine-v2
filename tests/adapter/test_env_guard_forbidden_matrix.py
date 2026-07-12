from __future__ import annotations
import pytest
from adapter.env_guard import validate_or_fail, EnvGuardError

def _prod_env(kvs):
    env = {"APP_ENV": "prod"}
    env.update(kvs)
    return env

def test_each_forbidden_key_raises():
    keys = [
        "ENGINE_SECRETS_DIR","ENGINE_PROVIDER","KEEP_REAL_SECRETS","FEATURE_TOGGLES",
        "PRESET_OVERRIDE","COPY_OVERRIDE","HD_ADMIN"
    ]
    for k in keys:
        with pytest.raises(EnvGuardError):
            validate_or_fail(_prod_env({k: "1"}))

def test_zero_and_false_with_spaces_still_forbidden():
    with pytest.raises(EnvGuardError):
        validate_or_fail(_prod_env({"ENGINE_PROVIDER": " 0 "}))
    with pytest.raises(EnvGuardError):
        validate_or_fail(_prod_env({"HD_ADMIN": "  false  "}))

def test_whitespace_or_unset_is_ok():
    validate_or_fail(_prod_env({"ENGINE_PROVIDER": "   "}))
    validate_or_fail(_prod_env({}))

def test_sorted_keys_in_details():
    try:
        validate_or_fail(_prod_env({"HD_ADMIN": "1", "ENGINE_PROVIDER": "x", "ALLOW_NETWORK": "0"}))
    except EnvGuardError as e:
        assert e.details["forbidden_keys"] == ["ENGINE_PROVIDER","HD_ADMIN"]

def test_allowed_keys_do_not_raise_in_prod():
    validate_or_fail(_prod_env({
        "RELEASE_ID": "a"*64,
        "ENGINE_TAG": "tag",
        "INVOCATION_TAG": "CID-deadbeef",
        "LOG_LEVEL": "INFO",
        "ENGINE_SERVICE_TOKEN": "x",
        "SENTRY_DSN": "x",
        "PORT": "8080",
        "ENGINE_ENV": "dev",
        "SAFE_MODE": "0",
        "ALLOW_NETWORK": "1",
    }))
