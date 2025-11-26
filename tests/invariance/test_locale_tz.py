import pytest

from engine.runtime.determinism_env import DETERMINISM_ENV_PINS, ensure_determinism_env

pytestmark = pytest.mark.epic006


def test_invariance_env_pins():
    env = ensure_determinism_env()
    assert env == DETERMINISM_ENV_PINS
