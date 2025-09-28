from __future__ import annotations
import pytest
from adapter.env_guard import validate_or_fail, EnvGuardError

def _prod_env(extra: dict[str, str] | None = None) -> dict[str, str]:
    env = {"APP_ENV": "prod"}
    if extra:
        env.update(extra)
    return env

def test_success_is_silent_and_idempotent(caplog):
    caplog.clear()
    validate_or_fail({"APP_ENV": "dev"})   # success once
    validate_or_fail({"APP_ENV": "dev"})   # success twice (idempotent)
    # module must not emit logs in either case
    assert len(caplog.records) == 0

def test_failure_is_idempotent_and_keys_sorted():
    env = _prod_env({"ALLOW_NETWORK": "0", "HD_ADMIN": "false"})  # both count as 'present'
    with pytest.raises(EnvGuardError) as e1:
        validate_or_fail(env)
    with pytest.raises(EnvGuardError) as e2:
        validate_or_fail(env)

    # details.forbidden_keys must be stable and lexicographically sorted
    k1 = e1.value.details["forbidden_keys"]
    k2 = e2.value.details["forbidden_keys"]
    assert k1 == sorted(k1) and k2 == sorted(k2)
    assert k1 == k2
