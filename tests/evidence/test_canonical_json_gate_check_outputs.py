from __future__ import annotations

import copy
import json

import pytest

from engine.config.registry_loader import SchemaValidationError, _normalize_channel_id
from tools.evidence import run_canonical_json_gate


def test_stale_outputs_detects_missing_and_drift(tmp_path):
    current = tmp_path / "current.log"
    missing = tmp_path / "missing.log"
    current.write_bytes(b"expected\n")
    expected = {
        current: b"expected\n",
        missing: b"expected\n",
    }

    assert run_canonical_json_gate._stale_outputs(expected) == [missing]

    current.write_bytes(b"drifted\n")
    assert run_canonical_json_gate._stale_outputs(expected) == [
        current,
        missing,
    ]


def test_d1_inventory_is_complete_unique_sorted_and_bound():
    targets = sorted(run_canonical_json_gate.TARGETS, key=lambda target: target.rel_path)
    assert len(targets) == 26
    assert len({target.rel_path for target in targets}) == 26
    assert [target.rel_path for target in targets] == sorted(target.rel_path for target in targets)
    assert all(target.validator for target in targets)
    assert all(path and identity for target in targets for path, identity in target.set_rules)


def test_incomplete_target_inventory_fails_closed():
    assert run_canonical_json_gate._run_gate(run_canonical_json_gate.TARGETS[:-1], check_only=True) == 1


def test_topology_schemas_accept_current_catalogs_and_reject_bounded_invalid_case():
    for catalog_name in ("gates_v1", "channels_v1"):
        target = next(target for target in run_canonical_json_gate.TARGETS if target.rel_path == f"catalog/{catalog_name}.json")
        payload = json.loads((run_canonical_json_gate.ROOT / target.rel_path).read_text(encoding="utf-8"))
        run_canonical_json_gate._validate_target(target, payload)
    invalid = copy.deepcopy(payload)
    invalid["channels"][0]["centers"] = [invalid["channels"][0]["centers"][0]] * 2
    with pytest.raises(Exception):
        run_canonical_json_gate._validate_target(target, invalid)


def test_declared_set_rule_rejects_unique_but_non_ascii_order():
    target = next(target for target in run_canonical_json_gate.TARGETS if target.rel_path == "catalog/channels_v1.json")
    payload = json.loads((run_canonical_json_gate.ROOT / target.rel_path).read_text(encoding="utf-8"))
    payload["channels"][0]["domains"] = ["talk", "action_voice"]
    with pytest.raises(ValueError, match=r"set_not_canonical:\$\.channels\[\*\]\.domains:0"):
        run_canonical_json_gate._validate_target(target, payload)


def test_unimplemented_validator_and_wrong_bound_type_fail_closed():
    target_type = run_canonical_json_gate.Target
    with pytest.raises(ValueError, match="unimplemented_validator"):
        run_canonical_json_gate._validate_target(target_type("bad", "bad.json", "advertised_only"), {})
    with pytest.raises(ValueError, match="target_must_be_object"):
        run_canonical_json_gate._validate_target(target_type("bad", "bad.json", "json_object_contract"), None)


def test_duplicate_channel_gate_endpoints_fail_schema_and_loader():
    target = next(target for target in run_canonical_json_gate.TARGETS if target.rel_path == "catalog/channels_v1.json")
    payload = json.loads((run_canonical_json_gate.ROOT / target.rel_path).read_text(encoding="utf-8"))
    payload["channels"][0]["id"] = "01-01"
    payload["channels"][0]["gates"] = [1, 1]
    with pytest.raises(Exception):
        run_canonical_json_gate._validate_target(target, payload)
    with pytest.raises(SchemaValidationError, match="two distinct gates") as exc_info:
        _normalize_channel_id("01-01", [1, 1])
    assert exc_info.value.code == "DUPLICATE_CHANNEL_GATE"
