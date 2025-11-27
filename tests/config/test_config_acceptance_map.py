import json
from pathlib import Path

import pytest

from tests.config.helpers import closed_rails_env

ALLOWED_PF09_TASKS = {
    "HDE-CALC004",
    "HDE-CALC004.3",
    "HDE-CALC004.7",
}

ALLOWED_TOKENS = {
    "CONFIG_MAGIC10_OK",
    "CONFIG_REGISTRY_OK",
}

ACCEPTANCE_MAP_PATH = Path("audit/EPIC-018_config_acceptance_map.json")


@pytest.fixture(scope="module", autouse=True)
def _hydrate_artifacts() -> None:
    # Ensure governed config artifacts exist before validating acceptance map references.
    env = closed_rails_env()
    Path("artifacts").mkdir(exist_ok=True)
    import subprocess, sys

    subprocess.run([sys.executable, "tools/config/generate_config_artifacts.py"], check=True, env=env)


@pytest.fixture(scope="module")
def _acceptance_records() -> list[dict]:
    text = ACCEPTANCE_MAP_PATH.read_text(encoding="utf-8")
    obj = json.loads(text)
    assert text == json.dumps(obj, sort_keys=True, separators=(",", ":")) + "\n"
    return obj


@pytest.fixture(scope="module")
def _artifact_keys() -> set[str]:
    index = json.loads(Path("docs/evidence/INDEX.json").read_text(encoding="utf-8"))
    return {entry["artifact_key"] for entry in index}


def _assert_test_node_exists(test_name: str) -> None:
    file_name, _, node = test_name.partition("::")
    path = Path(file_name)
    assert path.exists(), f"missing test file: {file_name}"
    if node:
        content = path.read_text(encoding="utf-8")
        assert node in content, f"missing test node: {test_name}"


def test_acceptance_map_records(_acceptance_records: list[dict], _artifact_keys: set[str]) -> None:
    for record in _acceptance_records:
        assert record["pf09_task_id"] in ALLOWED_PF09_TASKS
        assert record["artifact_key"] in _artifact_keys
        tokens = record.get("token_names")
        assert tokens, "token_names must be present"
        for token in tokens:
            assert token in ALLOWED_TOKENS
        tests = record.get("test_names")
        assert tests, "test_names must be present"
        for test_name in tests:
            _assert_test_node_exists(test_name)


def test_acceptance_map_keys_are_unique(_acceptance_records: list[dict]) -> None:
    seen: set[tuple[str, str]] = set()
    for record in _acceptance_records:
        key = (record["pf09_task_id"], record["artifact_key"])
        assert key not in seen
        seen.add(key)
