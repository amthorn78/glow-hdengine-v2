import json
from pathlib import Path

import pytest

from engine.config.registry_loader import AliasPolicyError, DuplicateIdError, SchemaValidationError, UnknownIdError, load_registry_config
from tests.config.helpers import catalog_root, write_canonical


def test_alias_policy_off_rejects_alias(tmp_path: Path) -> None:
    root = catalog_root(tmp_path)
    with pytest.raises(AliasPolicyError) as error:
        load_registry_config(root, alias_ledger={"09-10": "01-08"})
    assert error.value.code == "ALIASES_FORBIDDEN"


def test_alias_policy_requires_allow_list(tmp_path: Path) -> None:
    root = catalog_root(tmp_path)
    assert load_registry_config(root, allow_aliases=True).alias_map == {}
    cfg = load_registry_config(root, allow_aliases=True, alias_ledger={"09-10": "01-08"})
    assert cfg.alias_map == {"09-10": "01-08"}
    assert len(cfg.channels) == 36 and "09-10" not in cfg.channels


@pytest.mark.parametrize("allowed", [False, True])
def test_alias_rows_never_enter_authoritative_catalog(tmp_path: Path, allowed: bool) -> None:
    root = catalog_root(tmp_path)
    path = root / "catalog/channels_v1.json"
    data = json.loads(path.read_bytes())
    data["channels"].append(dict(data["channels"][0], id="09-10", gates=[9, 10], alias_for="01-08"))
    write_canonical(path, data)
    with pytest.raises(SchemaValidationError) as error:
        load_registry_config(root, allow_aliases=allowed, alias_ledger={"09-10": "01-08"})
    assert error.value.code == "SCHEMA_VALIDATION_FAILED"


@pytest.mark.parametrize("ledger,code", [
    ({"01-08": "02-14"}, "DUPLICATE_ALIAS"),
    ({"09-10": "01-99"}, "UNKNOWN_ALIAS_TARGET"),
    ({"9-10": "01-08"}, "INVALID_ALIAS"),
    ({"10-09": "01-08"}, "INVALID_ALIAS"),
    ({"０９-１０": "01-08"}, "INVALID_ALIAS"),
    ({"09-10\n": "01-08"}, "INVALID_ALIAS"),
])
def test_invalid_alias_ledger_refuses(tmp_path: Path, ledger: dict, code: str) -> None:
    with pytest.raises((AliasPolicyError, DuplicateIdError, UnknownIdError)) as error:
        load_registry_config(catalog_root(tmp_path), allow_aliases=True, alias_ledger=ledger)
    assert error.value.code == code
