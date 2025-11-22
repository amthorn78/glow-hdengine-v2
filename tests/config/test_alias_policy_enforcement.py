import json
from pathlib import Path

import pytest

from engine.config.registry_loader import AliasPolicyError, load_registry_config


def _catalog_copy_with_alias(tmp_path: Path) -> Path:
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

    channels_path = catalog_dir / "channels_v1.json"
    payload = json.loads(channels_path.read_text(encoding="utf-8"))
    base_channel = payload["channels"][0]
    alias_entry = dict(base_channel)
    alias_entry["id"] = "09-10"
    alias_entry["gates"] = [9, 10]
    alias_entry["alias_for"] = base_channel["id"]
    payload["channels"].append(alias_entry)
    channels_path.write_text(json.dumps(payload, separators=(",", ":")), encoding="utf-8")
    return tmp_path


def test_alias_policy_off_rejects_alias(tmp_path: Path) -> None:
    root = _catalog_copy_with_alias(tmp_path)
    with pytest.raises(AliasPolicyError):
        load_registry_config(root)


def test_alias_policy_requires_allow_list(tmp_path: Path) -> None:
    root = _catalog_copy_with_alias(tmp_path)
    with pytest.raises(AliasPolicyError):
        load_registry_config(root, allow_aliases=True, alias_ledger={})

    cfg = load_registry_config(root, allow_aliases=True, alias_ledger={"09-10": "01-08"})
    assert cfg.alias_map == {"09-10": "01-08"}

