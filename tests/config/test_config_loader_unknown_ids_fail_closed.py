import json
from pathlib import Path

import pytest

from engine.config.registry_loader import SchemaValidationError, load_registry_config
from tests.config.helpers import catalog_root, write_canonical


def test_unknown_channel_gate_fails(tmp_path: Path) -> None:
    root = catalog_root(tmp_path)
    path = root / "catalog/channels_v1.json"
    payload = json.loads(path.read_bytes())
    payload["channels"][0]["gates"] = [1, 99]
    payload["channels"][0]["id"] = "01-99"
    write_canonical(path, payload)
    with pytest.raises(SchemaValidationError) as error:
        load_registry_config(root)
    assert error.value.code == "SCHEMA_VALIDATION_FAILED"
    assert error.value.details["schema"] == "schemas/channels_v1.schema.json"
    assert error.value.__cause__.validator in {"maximum", "pattern"}


def test_duplicate_gate_id_fails(tmp_path: Path) -> None:
    root = catalog_root(tmp_path)
    path = root / "catalog/gates_v1.json"
    payload = json.loads(path.read_bytes())
    payload["gates"].append(payload["gates"][0])
    write_canonical(path, payload)
    with pytest.raises(SchemaValidationError) as error:
        load_registry_config(root)
    assert error.value.code == "SCHEMA_VALIDATION_FAILED"
    assert error.value.details["schema"] == "schemas/gates_v1.schema.json"
    assert error.value.__cause__.validator == "maxItems"
