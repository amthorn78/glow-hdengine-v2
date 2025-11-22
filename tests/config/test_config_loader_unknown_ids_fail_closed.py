import json
from pathlib import Path

import pytest

from engine.config.registry_loader import DuplicateIdError, UnknownIdError, load_registry_config


def _write_catalog_copy(tmp_path: Path) -> Path:
    catalog_dir = tmp_path / "catalog"
    catalog_dir.mkdir()
    for name in [
        "channels_v1.json",
        "gates_v1.json",
        "magic10.json",
        "magic10_caps.json",
        "magic10_seeds.json",
        "manifest.json",
    ]:
        src = Path("catalog") / name
        (catalog_dir / name).write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
    return catalog_dir


def test_unknown_channel_gate_fails(tmp_path: Path) -> None:
    catalog_dir = _write_catalog_copy(tmp_path)
    channels_path = catalog_dir / "channels_v1.json"
    payload = json.loads(channels_path.read_text(encoding="utf-8"))
    payload["channels"][0]["gates"] = [1, 99]
    payload["channels"][0]["id"] = "01-99"
    channels_path.write_text(json.dumps(payload, separators=(",", ":")), encoding="utf-8")

    with pytest.raises(UnknownIdError):
        load_registry_config(tmp_path)


def test_duplicate_gate_id_fails(tmp_path: Path) -> None:
    catalog_dir = _write_catalog_copy(tmp_path)
    gates_path = catalog_dir / "gates_v1.json"
    payload = json.loads(gates_path.read_text(encoding="utf-8"))
    payload["gates"].append(payload["gates"][0])
    gates_path.write_text(json.dumps(payload, separators=(",", ":")), encoding="utf-8")

    with pytest.raises(DuplicateIdError):
        load_registry_config(tmp_path)

