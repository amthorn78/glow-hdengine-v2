import os
from pathlib import Path

import pytest

from engine.runtime.determinism_env import (
    DETERMINISM_ENV_PINS,
    ensure_determinism_env,
    record_env_log,
)


@pytest.fixture(autouse=True)
def _rails(monkeypatch: pytest.MonkeyPatch) -> None:
    for key, value in DETERMINISM_ENV_PINS.items():
        monkeypatch.setenv(key, value)


def test_env_pins_log_written(tmp_path: Path) -> None:
    log_path = Path("artifacts/cli/env_pins_epic021.log")
    log_path.parent.mkdir(parents=True, exist_ok=True)
    if log_path.exists():
        log_path.unlink()

    ensure_determinism_env()
    recorded = record_env_log(log_path, ["epic021-cli"], status="success")

    assert recorded == log_path
    content = log_path.read_text(encoding="utf-8")
    assert "\n" in content and content.endswith("\n")
    assert "epic021-cli" in content
    for key, value in DETERMINISM_ENV_PINS.items():
        assert f"\"{key}\":\"{value}\"" in content
