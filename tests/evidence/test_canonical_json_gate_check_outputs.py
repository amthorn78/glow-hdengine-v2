from __future__ import annotations

import copy
import hashlib
import json
import shutil

import pytest
import jsonschema

from engine.config.registry_loader import (
    FROZEN_MAGIC10_INPUTS,
    SchemaValidationError,
    _normalize_channel_id,
)
from engine.magic10.calculators import CATEGORY_INPUTS
from tools.evidence import run_canonical_json_gate


def _refresh_reader_idempotence_hash(payload):
    preimage = {
        key: value for key, value in payload.items() if key != "idempotence_hash"
    }
    payload["idempotence_hash"] = hashlib.sha256(
        run_canonical_json_gate.sercanon(preimage, sort_keys=True)
    ).hexdigest()


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


def test_gate_capture_timestamp_is_independent_of_intentional_release_cut(
    tmp_path, monkeypatch
):
    catalog = tmp_path / "catalog"
    catalog.mkdir()
    (catalog / "manifest.json").write_text(
        json.dumps(
            {
                "built_at_utc": "2030-01-02T03:04:05Z",
                "files": [],
                "root": "catalog/",
                "version": "2.0.0",
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(run_canonical_json_gate, "ROOT", tmp_path)

    assert run_canonical_json_gate._generated_at() == (
        run_canonical_json_gate.GATE_CAPTURED_AT_UTC
    )
    assert run_canonical_json_gate._generated_at() == "2025-12-26T00:00:00Z"


def test_full_gate_outputs_remain_current_after_metadata_only_release_cut(
    tmp_path, monkeypatch
):
    source_root = run_canonical_json_gate.ROOT
    for name in ("artifacts", "audit", "schemas"):
        (tmp_path / name).symlink_to(source_root / name, target_is_directory=True)
    for name in ("adapter", "catalog", "engine", "math", "migrations"):
        shutil.copytree(source_root / name, tmp_path / name)

    manifest_path = tmp_path / "catalog" / "manifest.json"
    manifest = json.loads(manifest_path.read_bytes())
    manifest["version"] = "2.0.0"
    manifest["built_at_utc"] = "2030-01-02T03:04:05Z"
    manifest_path.write_bytes(
        run_canonical_json_gate.sercanon(manifest, sort_keys=True)
    )

    monkeypatch.setattr(run_canonical_json_gate, "ROOT", tmp_path)
    monkeypatch.setattr(
        run_canonical_json_gate,
        "CANON_DIR",
        tmp_path / "audit" / "gates" / "canonical_json",
    )
    monkeypatch.setattr(
        run_canonical_json_gate,
        "JSON_GATE_DIR",
        tmp_path / "audit" / "gates" / "json_gate" / "canonical",
    )
    assert (
        run_canonical_json_gate._run_gate(
            run_canonical_json_gate.TARGETS,
            check_only=True,
        )
        == 0
    )

    manifest["built_at_utc"] = "2030-02-30T03:04:05Z"
    manifest_path.write_bytes(
        run_canonical_json_gate.sercanon(manifest, sort_keys=True)
    )
    assert (
        run_canonical_json_gate._run_gate(
            run_canonical_json_gate.TARGETS,
            check_only=True,
        )
        == 1
    )

    manifest["built_at_utc"] = "2030-01-02T03:04:05Z"
    member_path = tmp_path / "adapter" / "http_reader.py"
    member_bytes = member_path.read_bytes() + b"# intentional release member change\n"
    member_path.write_bytes(member_bytes)
    member_entry = next(
        entry
        for entry in manifest["files"]
        if entry["path"] == "adapter/http_reader.py"
    )
    member_entry["sha256"] = hashlib.sha256(member_bytes).hexdigest()
    member_entry["size"] = len(member_bytes)
    manifest_path.write_bytes(
        run_canonical_json_gate.sercanon(manifest, sort_keys=True)
    )
    manifest_target = next(
        target
        for target in run_canonical_json_gate.TARGETS
        if target.rel_path == "catalog/manifest.json"
    )
    run_canonical_json_gate._validate_target(manifest_target, manifest)
    assert (
        run_canonical_json_gate._run_gate(
            run_canonical_json_gate.TARGETS,
            check_only=True,
        )
        == 1
    )


def test_manifest_evidence_projection_binds_root_and_files_not_cut_metadata():
    target = next(
        target
        for target in run_canonical_json_gate.TARGETS
        if target.rel_path == "catalog/manifest.json"
    )
    manifest_path = run_canonical_json_gate.ROOT / target.rel_path
    manifest = json.loads(manifest_path.read_bytes())
    canonical = run_canonical_json_gate.sercanon(manifest, sort_keys=True)

    baseline = run_canonical_json_gate._target_evidence_bytes(
        target, manifest, canonical, canonical
    )
    cut = copy.deepcopy(manifest)
    cut["version"] = "2.0.0"
    cut["built_at_utc"] = "2030-01-02T03:04:05Z"
    cut_bytes = run_canonical_json_gate.sercanon(cut, sort_keys=True)
    assert run_canonical_json_gate._target_evidence_bytes(
        target, cut, cut_bytes, cut_bytes
    ) == baseline

    changed_root = copy.deepcopy(manifest)
    changed_root["root"] = "other/"
    changed_root_bytes = run_canonical_json_gate.sercanon(
        changed_root, sort_keys=True
    )
    assert run_canonical_json_gate._target_evidence_bytes(
        target,
        changed_root,
        changed_root_bytes,
        changed_root_bytes,
    ) != baseline

    changed_files = copy.deepcopy(manifest)
    changed_files["files"][0]["sha256"] = "0" * 64
    changed_files_bytes = run_canonical_json_gate.sercanon(
        changed_files, sort_keys=True
    )
    assert run_canonical_json_gate._target_evidence_bytes(
        target,
        changed_files,
        changed_files_bytes,
        changed_files_bytes,
    ) != baseline


def test_d1_inventory_is_complete_unique_sorted_and_bound():
    targets = sorted(run_canonical_json_gate.TARGETS, key=lambda target: target.rel_path)
    assert len(targets) == 26
    assert len({target.rel_path for target in targets}) == 26
    assert run_canonical_json_gate.EXPECTED_TARGET_PATHS == tuple(
        sorted(run_canonical_json_gate.EXPECTED_TARGET_PATHS)
    )
    assert tuple(target.rel_path for target in targets) == (
        run_canonical_json_gate.EXPECTED_TARGET_PATHS
    )
    assert run_canonical_json_gate.EXPECTED_TARGET_BINDINGS == tuple(
        sorted(run_canonical_json_gate.EXPECTED_TARGET_BINDINGS)
    )
    assert tuple(
        (target.rel_path, target.validator, target.schema) for target in targets
    ) == run_canonical_json_gate.EXPECTED_TARGET_BINDINGS
    assert run_canonical_json_gate.EXPECTED_SET_RULES == tuple(
        sorted(run_canonical_json_gate.EXPECTED_SET_RULES)
    )
    assert tuple(
        sorted(
            (target.rel_path, path, identity)
            for target in targets
            for path, identity in target.set_rules
        )
    ) == run_canonical_json_gate.EXPECTED_SET_RULES
    assert all(target.validator for target in targets)
    assert all(path and identity for target in targets for path, identity in target.set_rules)
    assert {target.validator for target in targets} <= set(
        run_canonical_json_gate._VALIDATOR_REGISTRY
    )


def test_all_26_current_target_bindings_execute(monkeypatch):
    for name, value in {
        "SAFE_MODE": "1",
        "ALLOW_NETWORK": "0",
        "APP_ENV": "dev",
        "LC_ALL": "C",
        "LANG": "C",
        "TZ": "UTC",
    }.items():
        monkeypatch.setenv(name, value)
    for target in sorted(
        run_canonical_json_gate.TARGETS, key=lambda item: item.rel_path
    ):
        payload = json.loads(
            (run_canonical_json_gate.ROOT / target.rel_path).read_bytes()
        )
        run_canonical_json_gate._validate_target(target, payload)


def test_incomplete_target_inventory_fails_closed():
    assert run_canonical_json_gate._run_gate(run_canonical_json_gate.TARGETS[:-1], check_only=True) == 1


def test_same_cardinality_target_substitution_fails_closed():
    targets = list(run_canonical_json_gate.TARGETS)
    original = targets[0]
    targets[0] = run_canonical_json_gate.Target(
        original.name,
        "artifacts/cli/reader_cli_parity.bytes",
        original.validator,
        original.schema,
        original.set_rules,
    )

    assert len(targets) == len(run_canonical_json_gate.EXPECTED_TARGET_PATHS)
    assert not run_canonical_json_gate._target_inventory_is_exact(targets)


def test_same_path_binding_erasure_and_set_rule_substitution_fail_closed():
    targets = list(run_canonical_json_gate.TARGETS)
    index = next(
        index
        for index, target in enumerate(targets)
        if target.rel_path == "catalog/channels_v1.json"
    )
    original = targets[index]
    targets[index] = run_canonical_json_gate.Target(
        original.name,
        original.rel_path,
        original.validator,
        None,
        (),
    )
    assert not run_canonical_json_gate._target_inventory_is_exact(targets)

    targets[index] = run_canonical_json_gate.Target(
        original.name,
        original.rel_path,
        original.validator,
        original.schema,
        (*original.set_rules[:-1], ("$.channels[*].unknown", "value")),
    )
    assert len(targets[index].set_rules) == len(original.set_rules)
    assert not run_canonical_json_gate._target_inventory_is_exact(targets)

    targets[index] = run_canonical_json_gate.Target(
        original.name,
        original.rel_path,
        original.validator,
        original.schema,
        tuple(
            rule
            for rule in original.set_rules
            if rule != ("$.channels", "id")
        ),
    )
    assert (
        targets[index].rel_path,
        targets[index].validator,
        targets[index].schema,
    ) == (
        original.rel_path,
        original.validator,
        original.schema,
    )
    assert not run_canonical_json_gate._target_inventory_is_exact(targets)


def test_topology_schemas_accept_current_catalogs_and_reject_bounded_invalid_case():
    for catalog_name in ("gates_v1", "channels_v1"):
        target = next(target for target in run_canonical_json_gate.TARGETS if target.rel_path == f"catalog/{catalog_name}.json")
        payload = json.loads((run_canonical_json_gate.ROOT / target.rel_path).read_text(encoding="utf-8"))
        run_canonical_json_gate._validate_target(target, payload)
    invalid = copy.deepcopy(payload)
    invalid["channels"][0]["centers"] = [invalid["channels"][0]["centers"][0]] * 2
    with pytest.raises(Exception):
        run_canonical_json_gate._validate_target(target, invalid)


@pytest.mark.parametrize(
    "rel_path",
    ("schemas/gates_v1.schema.json", "schemas/channels_v1.schema.json"),
)
def test_schema_document_bindings_reject_erasure_and_constraint_drift(rel_path):
    target = next(
        target
        for target in run_canonical_json_gate.TARGETS
        if target.rel_path == rel_path
    )
    with pytest.raises(ValueError, match="schema_document_must_be_object"):
        run_canonical_json_gate._validate_target(target, True)

    payload = json.loads(
        (run_canonical_json_gate.ROOT / target.rel_path).read_bytes()
    )
    collection = payload["properties"][next(iter(payload["properties"]))]
    collection["minItems"] -= 1
    with pytest.raises(ValueError, match="schema_document_contract_mismatch"):
        run_canonical_json_gate._validate_target(target, payload)


def test_topology_loader_rejects_schema_valid_projection_defects():
    channels_target = next(
        target
        for target in run_canonical_json_gate.TARGETS
        if target.rel_path == "catalog/channels_v1.json"
    )
    channels = json.loads(
        (run_canonical_json_gate.ROOT / channels_target.rel_path).read_bytes()
    )
    schema = json.loads(
        (run_canonical_json_gate.ROOT / channels_target.schema).read_bytes()
    )

    id_mismatch = copy.deepcopy(channels)
    id_mismatch["channels"][0]["id"] = "01-09"
    jsonschema.Draft202012Validator(schema).validate(id_mismatch)
    with pytest.raises(SchemaValidationError, match="does not match gates") as exc_info:
        run_canonical_json_gate._validate_target(channels_target, id_mismatch)
    assert exc_info.value.code == "CHANNEL_ID_MISMATCH"

    center_mismatch = copy.deepcopy(channels)
    center_mismatch["channels"][0]["centers"] = ["g", "sacral"]
    jsonschema.Draft202012Validator(schema).validate(center_mismatch)
    with pytest.raises(SchemaValidationError, match="gate projection") as exc_info:
        run_canonical_json_gate._validate_target(channels_target, center_mismatch)
    assert exc_info.value.code == "CHANNEL_CENTER_PROJECTION_MISMATCH"

    gates_target = next(
        target
        for target in run_canonical_json_gate.TARGETS
        if target.rel_path == "catalog/gates_v1.json"
    )
    gates = json.loads(
        (run_canonical_json_gate.ROOT / gates_target.rel_path).read_bytes()
    )
    gates_schema = json.loads(
        (run_canonical_json_gate.ROOT / gates_target.schema).read_bytes()
    )
    gates["gates"][1]["gate"] = gates["gates"][0]["gate"]
    jsonschema.Draft202012Validator(gates_schema).validate(gates)
    with pytest.raises(Exception, match="duplicate gate id"):
        run_canonical_json_gate._validate_target(gates_target, gates)


def test_channel_loader_rejects_schema_valid_identity_substitution():
    target = next(
        target
        for target in run_canonical_json_gate.TARGETS
        if target.rel_path == "catalog/channels_v1.json"
    )
    payload = json.loads(
        (run_canonical_json_gate.ROOT / target.rel_path).read_bytes()
    )
    schema = json.loads(
        (run_canonical_json_gate.ROOT / target.schema).read_bytes()
    )
    replacement = payload["channels"][0]
    replacement["id"] = "01-03"
    replacement["gates"] = [1, 3]
    replacement["centers"] = ["g", "sacral"]
    jsonschema.Draft202012Validator(schema).validate(payload)

    with pytest.raises(
        SchemaValidationError, match="frozen 36-Channel roster"
    ) as exc_info:
        run_canonical_json_gate._validate_target(target, payload)
    assert exc_info.value.code == "CHANNEL_ID_ROSTER_MISMATCH"
    assert exc_info.value.details == {
        "missing": ["01-08"],
        "unknown": ["01-03"],
    }


def test_topology_gate_rejects_coherent_gate_center_count_drift(
    tmp_path, monkeypatch
):
    shutil.copytree(
        run_canonical_json_gate.ROOT / "catalog", tmp_path / "catalog"
    )
    shutil.copytree(
        run_canonical_json_gate.ROOT / "schemas", tmp_path / "schemas"
    )
    gates_path = tmp_path / "catalog/gates_v1.json"
    channels_path = tmp_path / "catalog/channels_v1.json"
    gates = json.loads(gates_path.read_bytes())
    channels = json.loads(channels_path.read_bytes())

    next(row for row in gates["gates"] if row["gate"] == 1)["center"] = "head"
    next(row for row in channels["channels"] if row["id"] == "01-08")[
        "centers"
    ] = ["head", "throat"]
    gates_path.write_bytes(run_canonical_json_gate.sercanon(gates, sort_keys=True))
    channels_path.write_bytes(
        run_canonical_json_gate.sercanon(channels, sort_keys=True)
    )

    monkeypatch.setattr(run_canonical_json_gate, "ROOT", tmp_path)
    for rel_path in ("catalog/gates_v1.json", "catalog/channels_v1.json"):
        target = next(
            target
            for target in run_canonical_json_gate.TARGETS
            if target.rel_path == rel_path
        )
        payload = json.loads((tmp_path / rel_path).read_bytes())
        with pytest.raises(
            SchemaValidationError, match="gate center counts must match"
        ) as exc_info:
            run_canonical_json_gate._validate_target(target, payload)
        assert exc_info.value.code == "GATE_CENTER_COUNTS_MISMATCH"
        assert exc_info.value.details == {
            "actual": {
                "ajna": 6,
                "ego": 4,
                "g": 7,
                "head": 4,
                "root": 9,
                "sacral": 9,
                "solar_plexus": 7,
                "spleen": 7,
                "throat": 11,
            },
            "expected": {
                "ajna": 6,
                "ego": 4,
                "g": 8,
                "head": 3,
                "root": 9,
                "sacral": 9,
                "solar_plexus": 7,
                "spleen": 7,
                "throat": 11,
            },
        }


def test_topology_gate_rejects_coherent_same_count_gate_center_swap(
    tmp_path, monkeypatch
):
    shutil.copytree(
        run_canonical_json_gate.ROOT / "catalog", tmp_path / "catalog"
    )
    shutil.copytree(
        run_canonical_json_gate.ROOT / "schemas", tmp_path / "schemas"
    )
    gates_path = tmp_path / "catalog/gates_v1.json"
    channels_path = tmp_path / "catalog/channels_v1.json"
    gates = json.loads(gates_path.read_bytes())
    channels = json.loads(channels_path.read_bytes())

    next(row for row in gates["gates"] if row["gate"] == 1)["center"] = "sacral"
    next(row for row in gates["gates"] if row["gate"] == 3)["center"] = "g"
    next(row for row in channels["channels"] if row["id"] == "01-08")[
        "centers"
    ] = ["sacral", "throat"]
    next(row for row in channels["channels"] if row["id"] == "03-60")[
        "centers"
    ] = ["g", "root"]
    gates_path.write_bytes(run_canonical_json_gate.sercanon(gates, sort_keys=True))
    channels_path.write_bytes(
        run_canonical_json_gate.sercanon(channels, sort_keys=True)
    )

    monkeypatch.setattr(run_canonical_json_gate, "ROOT", tmp_path)
    for rel_path in ("catalog/gates_v1.json", "catalog/channels_v1.json"):
        target = next(
            target
            for target in run_canonical_json_gate.TARGETS
            if target.rel_path == rel_path
        )
        payload = json.loads((tmp_path / rel_path).read_bytes())
        with pytest.raises(
            SchemaValidationError, match="frozen Channel topology"
        ) as exc_info:
            run_canonical_json_gate._validate_target(target, payload)
        assert exc_info.value.code == "CHANNEL_CENTER_IDENTITY_MISMATCH"
        assert exc_info.value.details == {
            "actual": [[1, "sacral"], [8, "throat"]],
            "expected": [[1, "g"], [8, "throat"]],
        }


def test_topology_gate_rejects_coherent_within_channel_endpoint_swap(
    tmp_path, monkeypatch
):
    shutil.copytree(
        run_canonical_json_gate.ROOT / "catalog", tmp_path / "catalog"
    )
    shutil.copytree(
        run_canonical_json_gate.ROOT / "schemas", tmp_path / "schemas"
    )
    gates_path = tmp_path / "catalog/gates_v1.json"
    gates = json.loads(gates_path.read_bytes())

    next(row for row in gates["gates"] if row["gate"] == 1)["center"] = "throat"
    next(row for row in gates["gates"] if row["gate"] == 8)["center"] = "g"
    gates_path.write_bytes(run_canonical_json_gate.sercanon(gates, sort_keys=True))

    monkeypatch.setattr(run_canonical_json_gate, "ROOT", tmp_path)
    for rel_path in ("catalog/gates_v1.json", "catalog/channels_v1.json"):
        target = next(
            target
            for target in run_canonical_json_gate.TARGETS
            if target.rel_path == rel_path
        )
        payload = json.loads((tmp_path / rel_path).read_bytes())
        with pytest.raises(
            SchemaValidationError, match="frozen Channel topology"
        ) as exc_info:
            run_canonical_json_gate._validate_target(target, payload)
        assert exc_info.value.code == "CHANNEL_CENTER_IDENTITY_MISMATCH"
        assert exc_info.value.details == {
            "actual": [[1, "throat"], [8, "g"]],
            "expected": [[1, "g"], [8, "throat"]],
        }


def test_top_level_channel_set_uses_id_identity_and_ascii_order():
    target = next(
        target
        for target in run_canonical_json_gate.TARGETS
        if target.rel_path == "catalog/channels_v1.json"
    )
    payload = json.loads(
        (run_canonical_json_gate.ROOT / target.rel_path).read_bytes()
    )
    payload["channels"] = list(reversed(payload["channels"]))

    with pytest.raises(ValueError, match=r"set_not_canonical:\$\.channels$"):
        run_canonical_json_gate._validate_target(target, payload)


def test_declared_set_rule_rejects_unique_but_non_ascii_order():
    target = next(target for target in run_canonical_json_gate.TARGETS if target.rel_path == "catalog/channels_v1.json")
    payload = json.loads((run_canonical_json_gate.ROOT / target.rel_path).read_text(encoding="utf-8"))
    payload["channels"][0]["domains"] = ["talk", "narrative"]
    with pytest.raises(ValueError, match=r"set_not_canonical:\$\.channels\[\*\]\.domains:0"):
        run_canonical_json_gate._validate_target(target, payload)


def test_channel_gate_set_uses_strict_ascii_scalar_identity_order():
    target = next(
        target
        for target in run_canonical_json_gate.TARGETS
        if target.rel_path == "catalog/channels_v1.json"
    )
    payload = json.loads(
        (run_canonical_json_gate.ROOT / target.rel_path).read_bytes()
    )
    channel = next(row for row in payload["channels"] if row["id"] == "02-14")
    assert channel["gates"] == [14, 2]
    channel["gates"] = [2, 14]
    with pytest.raises(
        ValueError,
        match=r"set_not_canonical:\$\.channels\[\*\]\.gates",
    ):
        run_canonical_json_gate._validate_target(target, payload)


def test_unimplemented_validator_and_wrong_bound_type_fail_closed():
    target_type = run_canonical_json_gate.Target
    with pytest.raises(ValueError, match="unimplemented_validator"):
        run_canonical_json_gate._validate_target(target_type("bad", "bad.json", "advertised_only"), {})
    reader_target = next(
        target
        for target in run_canonical_json_gate.TARGETS
        if target.rel_path == "artifacts/cli/reader_dump.json"
    )
    with pytest.raises(ValueError, match="reader_envelope_must_be_object"):
        run_canonical_json_gate._validate_target(reader_target, None)


@pytest.mark.parametrize("target", run_canonical_json_gate._GENERATED)
def test_generated_target_contracts_reject_empty_objects(target):
    with pytest.raises(ValueError):
        run_canonical_json_gate._validate_target(target, {})


def test_manifest_binding_rejects_false_integrity_and_unsafe_paths(monkeypatch):
    for name, value in {
        "SAFE_MODE": "1",
        "ALLOW_NETWORK": "0",
        "LC_ALL": "C",
        "LANG": "C",
        "TZ": "UTC",
    }.items():
        monkeypatch.setenv(name, value)
    target = next(
        target
        for target in run_canonical_json_gate.TARGETS
        if target.rel_path == "catalog/manifest.json"
    )
    payload = json.loads(
        (run_canonical_json_gate.ROOT / target.rel_path).read_bytes()
    )

    false_sha = copy.deepcopy(payload)
    false_sha["files"][0]["sha256"] = "0" * 64
    with pytest.raises(ValueError, match="member_integrity_mismatch"):
        run_canonical_json_gate._validate_target(target, false_sha)

    incomplete = copy.deepcopy(payload)
    incomplete["files"].pop()
    with pytest.raises(ValueError, match="input_roster_invalid"):
        run_canonical_json_gate._validate_target(target, incomplete)

    for field, value in (
        ("version", "1.0.1"),
        ("built_at_utc", "2025-12-27T00:00:00Z"),
    ):
        intentional_cut = copy.deepcopy(payload)
        intentional_cut[field] = value
        run_canonical_json_gate._validate_target(target, intentional_cut)

    for field, value, error in (
        ("version", "01.0.0", "release_version_invalid"),
        ("built_at_utc", "2025-02-30T00:00:00Z", "release_built_at_invalid"),
    ):
        malformed_metadata = copy.deepcopy(payload)
        malformed_metadata[field] = value
        with pytest.raises(ValueError, match=error):
            run_canonical_json_gate._validate_target(target, malformed_metadata)

    for unsafe_path in ("../escape", "catalog\\escape.json", "a" * 257):
        unsafe = copy.deepcopy(payload)
        unsafe["files"][0]["path"] = unsafe_path
        with pytest.raises(ValueError, match="path_unsafe"):
            run_canonical_json_gate._validate_target(target, unsafe)


@pytest.mark.parametrize(
    ("rel_path", "invalid"),
    (
        ("catalog/narratives/keys.json", []),
        ("catalog/narratives/manifest.json", {}),
        ("catalog/narratives/palettes.json", {}),
        ("catalog/narratives/suppression_map.json", {}),
        ("catalog/narratives/templates.json", {}),
    ),
)
def test_narrative_bindings_fail_closed_on_semantic_invalidity(rel_path, invalid):
    target = next(
        target
        for target in run_canonical_json_gate.TARGETS
        if target.rel_path == rel_path
    )
    with pytest.raises(Exception):
        run_canonical_json_gate._validate_target(target, invalid)


def test_narrative_manifest_shape_and_identity_are_closed():
    target = next(
        target
        for target in run_canonical_json_gate.TARGETS
        if target.rel_path == "catalog/narratives/manifest.json"
    )
    current = json.loads(
        (run_canonical_json_gate.ROOT / target.rel_path).read_bytes()
    )

    wrong_pack = copy.deepcopy(current)
    wrong_pack["pack_name"] = "anything"
    with pytest.raises(Exception, match="pack_name"):
        run_canonical_json_gate._validate_target(target, wrong_pack)

    extra_top_level = copy.deepcopy(current)
    extra_top_level["ungoverned"] = True
    with pytest.raises(Exception, match="manifest fields invalid"):
        run_canonical_json_gate._validate_target(target, extra_top_level)

    invalid_timestamp = copy.deepcopy(current)
    invalid_timestamp["created_utc"] = "2025-02-30T00:00:00Z"
    with pytest.raises(Exception, match="created_utc invalid"):
        run_canonical_json_gate._validate_target(target, invalid_timestamp)

    extra_child_field = copy.deepcopy(current)
    extra_child_field["files"][0]["ungoverned"] = True
    with pytest.raises(Exception, match="file entry fields invalid"):
        run_canonical_json_gate._validate_target(target, extra_child_field)


def test_narrative_template_values_must_be_strings():
    target = next(
        target
        for target in run_canonical_json_gate.TARGETS
        if target.rel_path == "catalog/narratives/templates.json"
    )
    payload = json.loads(
        (run_canonical_json_gate.ROOT / target.rel_path).read_bytes()
    )
    payload[next(iter(payload))] = {}
    with pytest.raises(Exception, match="template values must be nonempty strings"):
        run_canonical_json_gate._validate_target(target, payload)


@pytest.mark.parametrize("directions", ("a_to_b", ["bogus"], None))
def test_personal_narrative_directions_are_closed(directions):
    target = next(
        target
        for target in run_canonical_json_gate.TARGETS
        if target.rel_path == "catalog/narratives/keys.json"
    )
    payload = json.loads(
        (run_canonical_json_gate.ROOT / target.rel_path).read_bytes()
    )
    personal = next(row for row in payload if row["perspective"] == "personal")
    personal["directions"] = directions
    with pytest.raises(Exception, match="personal key directions"):
        run_canonical_json_gate._validate_target(target, payload)


def test_narrative_key_matches_its_source_identity():
    target = next(
        target
        for target in run_canonical_json_gate.TARGETS
        if target.rel_path == "catalog/narratives/keys.json"
    )
    payload = json.loads(
        (run_canonical_json_gate.ROOT / target.rel_path).read_bytes()
    )
    payload[0]["key"] = "alignment.cool.personal.renamed"
    with pytest.raises(Exception, match="key/source identity mismatch"):
        run_canonical_json_gate._validate_target(target, payload)


def test_narrative_slot_rejects_json_boolean():
    target = next(
        target
        for target in run_canonical_json_gate.TARGETS
        if target.rel_path == "catalog/narratives/keys.json"
    )
    payload = json.loads(
        (run_canonical_json_gate.ROOT / target.rel_path).read_bytes()
    )
    payload[0]["slot"] = True
    payload[0]["key"] = "alignment.cool.personal.True"
    with pytest.raises(Exception, match="key record slot has invalid type"):
        run_canonical_json_gate._validate_target(target, payload)


def test_jsonschema_is_an_operational_dependency():
    runtime = {
        line.strip()
        for line in (run_canonical_json_gate.ROOT / "requirements.txt")
        .read_text(encoding="utf-8")
        .splitlines()
        if line.strip() and not line.startswith("#")
    }
    dev = {
        line.strip()
        for line in (run_canonical_json_gate.ROOT / "requirements-dev.txt")
        .read_text(encoding="utf-8")
        .splitlines()
        if line.strip() and not line.startswith("#")
    }
    assert "jsonschema==4.23.0" in runtime
    # HDE-EPIC038 freezes the dev-requirements bytes; the duplicate exact pin
    # remains there as a retained compatibility input.
    assert "jsonschema==4.23.0" in dev


def test_generated_compat_rejects_valid_token_with_wrong_score_band():
    target = next(
        target
        for target in run_canonical_json_gate.TARGETS
        if target.rel_path == "artifacts/cli/showcompat/stdout.json"
    )
    payload = json.loads(
        (run_canonical_json_gate.ROOT / target.rel_path).read_bytes()
    )
    row = payload["compat"]["categories"][0]
    row["band"] = "Glow"
    row["personal_key"] = "heat_glow_personal_v1"
    row["shared_key"] = "heat_glow_shared_v1"
    with pytest.raises(ValueError, match="score_band_mismatch"):
        run_canonical_json_gate._validate_target(target, payload)


@pytest.mark.parametrize(
    "rel_path",
    ("artifacts/cli/showcompat/stdout.json", "artifacts/cli/ab.json"),
)
def test_generated_compat_identity_binds_immutable_runtime_source(rel_path):
    target = next(
        target
        for target in run_canonical_json_gate.TARGETS
        if target.rel_path == rel_path
    )
    payload = json.loads(
        (run_canonical_json_gate.ROOT / target.rel_path).read_bytes()
    )
    compat = payload["compat"] if "compat" in payload else payload["conjunction"]["compat"]
    compat["meta"] = {
        "engine_tag": "forged-engine",
        "invocation_tag": "FORGED",
        "release_id": "f" * 64,
    }
    with pytest.raises(ValueError, match="runtime_identity_source_mismatch"):
        run_canonical_json_gate._validate_target(target, payload)


def test_conjunction_capture_rejects_coherent_forged_uids(tmp_path, monkeypatch):
    artifact_dir = tmp_path / "artifacts" / "cli"
    artifact_dir.mkdir(parents=True)
    payloads = {}
    for name in ("ab", "ba"):
        payload = json.loads(
            (run_canonical_json_gate.ROOT / f"artifacts/cli/{name}.json").read_bytes()
        )
        payload["conjunction"]["left"]["person_uid"] = "forged-left"
        payloads[name] = payload
        (artifact_dir / f"{name}.json").write_bytes(
            run_canonical_json_gate.sercanon(payload, sort_keys=True)
        )

    monkeypatch.setattr(run_canonical_json_gate, "ROOT", tmp_path)
    for name in ("ab", "ba"):
        target = next(
            target
            for target in run_canonical_json_gate.TARGETS
            if target.rel_path == f"artifacts/cli/{name}.json"
        )
        with pytest.raises(ValueError, match="person_uid_source_mismatch"):
            run_canonical_json_gate._validate_target(target, payloads[name])


def test_conjunction_capture_rejects_coherent_same_band_score_forgery(
    tmp_path, monkeypatch
):
    source_root = run_canonical_json_gate.ROOT
    artifact_dir = tmp_path / "artifacts" / "cli"
    artifact_dir.mkdir(parents=True)
    payloads = {}
    for name in ("ab", "ba"):
        payload = json.loads(
            (source_root / f"artifacts/cli/{name}.json").read_bytes()
        )
        payload["conjunction"]["compat"]["categories"][0]["score"] = 46
        payloads[name] = payload
        (artifact_dir / f"{name}.json").write_bytes(
            run_canonical_json_gate.sercanon(payload, sort_keys=True)
        )

    monkeypatch.setattr(run_canonical_json_gate, "ROOT", tmp_path)
    for name in ("ab", "ba"):
        target = next(
            target
            for target in run_canonical_json_gate.TARGETS
            if target.rel_path == f"artifacts/cli/{name}.json"
        )
        with pytest.raises(ValueError, match="conjunction_source_mismatch"):
            run_canonical_json_gate._validate_target(target, payloads[name])


def test_showcompat_capture_rejects_coherent_same_band_score_forgery():
    target = next(
        target
        for target in run_canonical_json_gate.TARGETS
        if target.rel_path == "artifacts/cli/showcompat/stdout.json"
    )
    payload = json.loads(
        (run_canonical_json_gate.ROOT / target.rel_path).read_bytes()
    )
    payload["compat"]["categories"][0]["score"] = 22
    with pytest.raises(ValueError, match="showcompat_capture_source_mismatch"):
        run_canonical_json_gate._validate_target(target, payload)


def test_showcompat_args_bind_recorded_input_to_output_births():
    target = next(
        target
        for target in run_canonical_json_gate.TARGETS
        if target.rel_path == "artifacts/cli/showcompat/args.json"
    )
    payload = json.loads(
        (run_canonical_json_gate.ROOT / target.rel_path).read_bytes()
    )
    payload["input"]["stdin_payload"]["left"]["birthdate"] = "1990-01-11"
    stdin_bytes = (
        json.dumps(
            payload["input"]["stdin_payload"], separators=(",", ":"), sort_keys=True
        )
        + "\n"
    ).encode("utf-8")
    payload["input"]["stdin_sha256"] = hashlib.sha256(stdin_bytes).hexdigest()
    with pytest.raises(ValueError, match="source_pair_mismatch"):
        run_canonical_json_gate._validate_target(target, payload)


def test_hd_cli_reader_pair_rejects_coherent_source_forgery(tmp_path, monkeypatch):
    source_root = run_canonical_json_gate.ROOT
    artifact_dir = tmp_path / "artifacts" / "cli"
    artifact_dir.mkdir(parents=True)
    payloads = {}
    for name in ("out", "out_ba"):
        payload = json.loads(
            (source_root / f"artifacts/cli/{name}.json").read_bytes()
        )
        payload["eligible"] = False
        _refresh_reader_idempotence_hash(payload)
        payloads[name] = payload
        (artifact_dir / f"{name}.json").write_bytes(
            run_canonical_json_gate.sercanon(payload, sort_keys=True)
        )

    monkeypatch.setattr(run_canonical_json_gate, "ROOT", tmp_path)
    for name in ("out", "out_ba"):
        target = next(
            target
            for target in run_canonical_json_gate.TARGETS
            if target.rel_path == f"artifacts/cli/{name}.json"
        )
        with pytest.raises(ValueError, match="reader_hd_cli_source_mismatch"):
            run_canonical_json_gate._validate_target(target, payloads[name])


def test_frozen_audit_reader_pair_rejects_coherent_rewrite(tmp_path, monkeypatch):
    source_root = run_canonical_json_gate.ROOT
    artifact_dir = tmp_path / "artifacts" / "audit" / "cli"
    artifact_dir.mkdir(parents=True)
    payloads = {}
    for name in ("showcompat_ab", "showcompat_ba"):
        payload = json.loads(
            (source_root / f"artifacts/audit/cli/{name}.json").read_bytes()
        )
        payload["eligible"] = False
        _refresh_reader_idempotence_hash(payload)
        payloads[name] = payload
        (artifact_dir / f"{name}.json").write_bytes(
            run_canonical_json_gate.sercanon(payload, sort_keys=True)
        )

    monkeypatch.setattr(run_canonical_json_gate, "ROOT", tmp_path)
    for name in ("showcompat_ab", "showcompat_ba"):
        target = next(
            target
            for target in run_canonical_json_gate.TARGETS
            if target.rel_path == f"artifacts/audit/cli/{name}.json"
        )
        with pytest.raises(ValueError, match="frozen_generated_capture_mismatch"):
            run_canonical_json_gate._validate_target(target, payloads[name])


def test_cli_summary_rejects_open_rails_nested_evidence():
    target = next(
        target
        for target in run_canonical_json_gate.TARGETS
        if target.rel_path == "artifacts/cli/summary.json"
    )
    payload = json.loads(
        (run_canonical_json_gate.ROOT / target.rel_path).read_bytes()
    )
    payload["pf05_command_catalog"]["env"]["ALLOW_NETWORK"] = "1"
    with pytest.raises(ValueError, match="pf05_env_invalid"):
        run_canonical_json_gate._validate_target(target, payload)

    unbound_sampler = json.loads(
        (run_canonical_json_gate.ROOT / target.rel_path).read_bytes()
    )
    unbound_sampler["sampler_semantics"]["sha256"] = "0" * 64
    with pytest.raises(ValueError, match="sampler_sha_mismatch"):
        run_canonical_json_gate._validate_target(target, unbound_sampler)


def test_cli_summary_rejects_bool_int_type_aliases():
    target = next(
        target
        for target in run_canonical_json_gate.TARGETS
        if target.rel_path == "artifacts/cli/summary.json"
    )
    current = json.loads(
        (run_canonical_json_gate.ROOT / target.rel_path).read_bytes()
    )

    false_returncode = copy.deepcopy(current)
    false_returncode["installability"]["console_help"]["returncode"] = False
    with pytest.raises(ValueError, match="console_help_invalid"):
        run_canonical_json_gate._validate_target(target, false_returncode)

    integer_stream = copy.deepcopy(current)
    integer_stream["pf05_command_catalog"]["streams_checked"][
        "help_stderr_empty"
    ] = 1
    with pytest.raises(ValueError, match="streams_invalid"):
        run_canonical_json_gate._validate_target(target, integer_stream)

    integer_availability = copy.deepcopy(current)
    integer_availability["installability"]["console_entrypoint"]["available"] = 1
    with pytest.raises(ValueError, match="console_entrypoint_invalid"):
        run_canonical_json_gate._validate_target(target, integer_availability)


def test_magic10_caps_binding_rejects_coercions_and_open_entries():
    target = next(
        target
        for target in run_canonical_json_gate.TARGETS
        if target.rel_path == "catalog/magic10_caps.json"
    )
    current = json.loads(
        (run_canonical_json_gate.ROOT / target.rel_path).read_bytes()
    )

    coerced = copy.deepcopy(current)
    coerced["alignment"] = {
        "bounds": {"min": False, "max": True},
        "inputs": [1],
    }
    with pytest.raises(SchemaValidationError, match="inputs must be non-empty strings"):
        run_canonical_json_gate._validate_target(target, coerced)

    open_entry = copy.deepcopy(current)
    open_entry["alignment"]["extra"] = "ungoverned"
    with pytest.raises(SchemaValidationError, match="inputs and bounds only"):
        run_canonical_json_gate._validate_target(target, open_entry)


def test_magic10_frozen_input_sentry_matches_runtime_calculators():
    assert CATEGORY_INPUTS == FROZEN_MAGIC10_INPUTS


@pytest.mark.parametrize(
    ("mutation", "actual"),
    (
        ("substitution", ["replacement_input", "axis_agreement"]),
        ("omission", ["vector_cohesion"]),
        (
            "addition",
            ["vector_cohesion", "axis_agreement", "additional_input"],
        ),
        ("order", ["axis_agreement", "vector_cohesion"]),
    ),
)
def test_magic10_caps_binding_rejects_coherent_ordered_input_drift(
    mutation, actual
):
    target = next(
        target
        for target in run_canonical_json_gate.TARGETS
        if target.rel_path == "catalog/magic10_caps.json"
    )
    candidate = json.loads(
        (run_canonical_json_gate.ROOT / target.rel_path).read_bytes()
    )
    candidate["alignment"]["inputs"] = actual

    with pytest.raises(
        SchemaValidationError, match="inputs must match the frozen ordered contract"
    ) as exc_info:
        run_canonical_json_gate._validate_target(target, candidate)
    assert exc_info.value.code == "MAGIC10_INPUTS_MISMATCH", mutation
    assert exc_info.value.details == {
        "actual": actual,
        "expected": ["vector_cohesion", "axis_agreement"],
    }


@pytest.mark.parametrize(("field", "value"), (("min", 1), ("max", 99)))
def test_magic10_caps_binding_rejects_coherent_noncanonical_bounds(field, value):
    target = next(
        target
        for target in run_canonical_json_gate.TARGETS
        if target.rel_path == "catalog/magic10_caps.json"
    )
    candidate = json.loads(
        (run_canonical_json_gate.ROOT / target.rel_path).read_bytes()
    )
    candidate["alignment"]["bounds"][field] = value

    with pytest.raises(
        SchemaValidationError, match="bounds must be integers with min 0 and max 100"
    ):
        run_canonical_json_gate._validate_target(target, candidate)


def test_magic10_seed_binding_rejects_coercions_formats_and_open_entries():
    target = next(
        target
        for target in run_canonical_json_gate.TARGETS
        if target.rel_path == "catalog/magic10_seeds.json"
    )
    current = json.loads(
        (run_canonical_json_gate.ROOT / target.rel_path).read_bytes()
    )

    coerced = copy.deepcopy(current)
    coerced["harmony"] = {key: None for key in coerced["harmony"]}
    with pytest.raises(SchemaValidationError, match="non-empty strings"):
        run_canonical_json_gate._validate_target(target, coerced)

    invalid_checksum = copy.deepcopy(current)
    invalid_checksum["harmony"]["checksum_sha256"] = "A" * 64
    with pytest.raises(SchemaValidationError, match="checksum invalid"):
        run_canonical_json_gate._validate_target(target, invalid_checksum)

    for bad_timestamp in (
        "2025-99-99T00:00:00Z",
        "2025-1-02T0:0:0Z",
    ):
        invalid_timestamp = copy.deepcopy(current)
        invalid_timestamp["harmony"]["updated_at_utc"] = bad_timestamp
        with pytest.raises(SchemaValidationError, match="timestamp invalid"):
            run_canonical_json_gate._validate_target(target, invalid_timestamp)

    open_entry = copy.deepcopy(current)
    open_entry["harmony"]["extra"] = "ungoverned"
    with pytest.raises(SchemaValidationError, match="fields invalid"):
        run_canonical_json_gate._validate_target(target, open_entry)


def test_reader_leader_identity_must_match_band():
    target = next(
        target
        for target in run_canonical_json_gate.TARGETS
        if target.rel_path == "artifacts/cli/reader_dump.json"
    )
    payload = json.loads(
        (run_canonical_json_gate.ROOT / target.rel_path).read_bytes()
    )
    payload["categories"][0] = {"band": "Glow", "id": "cool_leader"}
    preimage = {
        key: value for key, value in payload.items() if key != "idempotence_hash"
    }
    payload["idempotence_hash"] = hashlib.sha256(
        run_canonical_json_gate.sercanon(preimage, sort_keys=True)
    ).hexdigest()
    with pytest.raises(ValueError, match="leader_band_mismatch"):
        run_canonical_json_gate._validate_target(target, payload)


def test_reader_dump_is_bound_to_its_capture_time_cli_parity_bytes():
    target = next(
        target
        for target in run_canonical_json_gate.TARGETS
        if target.rel_path == "artifacts/cli/reader_dump.json"
    )
    payload = json.loads(
        (run_canonical_json_gate.ROOT / target.rel_path).read_bytes()
    )
    payload["eligible"] = not payload["eligible"]
    preimage = {
        key: value for key, value in payload.items() if key != "idempotence_hash"
    }
    payload["idempotence_hash"] = hashlib.sha256(
        run_canonical_json_gate.sercanon(preimage, sort_keys=True)
    ).hexdigest()

    with pytest.raises(ValueError, match="reader_cli_parity_mismatch"):
        run_canonical_json_gate._validate_target(target, payload)


@pytest.mark.parametrize(
    "trace",
    (
        ["arbitrary"],
        ["step3", "step2", "step1"],
        ["step1", "step2"],
        ["step1", "step2", "step3", "step4"],
    ),
)
def test_selection_trace_is_bound_to_producer_order(trace):
    target = next(
        target
        for target in run_canonical_json_gate.TARGETS
        if target.rel_path == "artifacts/cli/abba_sidecar.json"
    )

    with pytest.raises(ValueError, match="selection_trace_source_mismatch"):
        run_canonical_json_gate._validate_target(
            target, {"selection_trace": trace}
        )


@pytest.mark.parametrize(
    ("categories", "message"),
    (
        (
            [
                {"band": "Cool", "id": "harmony"},
                {"band": "Cool", "id": "harmony"},
            ],
            "reader_category_id_duplicate",
        ),
        (
            [
                {"band": "Cool", "id": "heat"},
                {"band": "Cool", "id": "harmony"},
            ],
            "reader_category_id_order_invalid",
        ),
    ),
)
def test_reader_categories_follow_source_set_contract(categories, message):
    target = next(
        target
        for target in run_canonical_json_gate.TARGETS
        if target.rel_path == "artifacts/cli/reader_dump.json"
    )
    payload = json.loads(
        (run_canonical_json_gate.ROOT / target.rel_path).read_bytes()
    )
    payload["categories"] = categories
    preimage = {
        key: value for key, value in payload.items() if key != "idempotence_hash"
    }
    payload["idempotence_hash"] = hashlib.sha256(
        run_canonical_json_gate.sercanon(preimage, sort_keys=True)
    ).hexdigest()
    with pytest.raises(ValueError, match=message):
        run_canonical_json_gate._validate_target(target, payload)


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
