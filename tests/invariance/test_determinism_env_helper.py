import os
from pathlib import Path

import pytest

from engine.runtime.determinism_env import (
    DETERMINISM_ENV_PINS,
    DeterminismEnvError,
    ensure_determinism_env,
    record_env_log,
    render_env_log,
)

pytestmark = pytest.mark.epic006


@pytest.fixture()
def pinned_env(monkeypatch):
    for key, value in DETERMINISM_ENV_PINS.items():
        monkeypatch.setenv(key, value)
    return dict(os.environ)


def test_helper_rejects_missing_pin(monkeypatch):
    monkeypatch.delenv("LC_ALL", raising=False)
    with pytest.raises(DeterminismEnvError):
        ensure_determinism_env()


def test_helper_rejects_mismatched_pin(monkeypatch):
    monkeypatch.setenv("TZ", "America/New_York")
    with pytest.raises(DeterminismEnvError):
        ensure_determinism_env()


def test_helper_writes_and_checks_log(tmp_path: Path, pinned_env):
    log_path = tmp_path / "env.log"
    suites = ["tests:invariance", "ci:determinism"]
    record_env_log(log_path, suites, environ=pinned_env)
    expected = render_env_log(DETERMINISM_ENV_PINS, suites, "success")
    assert log_path.read_text(encoding="utf-8") == expected
    record_env_log(log_path, suites, environ=pinned_env, check_only=True)


def test_helper_apply_sets_missing(monkeypatch):
    env = {}
    result = ensure_determinism_env(environ=env, apply=True)
    assert result == DETERMINISM_ENV_PINS
    assert env == DETERMINISM_ENV_PINS
