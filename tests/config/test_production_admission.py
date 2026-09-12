from __future__ import annotations

import hashlib
import inspect
import json
import shutil
from dataclasses import FrozenInstanceError, fields, is_dataclass
from collections.abc import Mapping
from pathlib import Path
from types import MappingProxyType

import pytest

from engine.config import registry_loader
from engine.config.registry_loader import (
    ADMITTED_RELEASE_BUILT_AT_UTC,
    ADMITTED_RELEASE_ROSTER,
    ADMITTED_RELEASE_VERSION,
    AdmittedMechanicsBundle,
    RegistryConfigError,
    SchemaValidationError,
    _LocalCapture,
    _load_active_mechanics_bundle_from_root,
    load_active_mechanics_bundle,
)
from tests.config.helpers import (
    synthetic_complete_release_root,
    write_canonical,
    write_synthetic_release_manifest,
)


@pytest.fixture
def release_root(tmp_path: Path) -> Path:
    return synthetic_complete_release_root(tmp_path)


def _manifest(root: Path) -> dict:
    return json.loads((root / "catalog/manifest.json").read_bytes())


def _write_manifest(root: Path, value: object) -> None:
    write_canonical(root / "catalog/manifest.json", value)


def _expect_code(root: Path, code: str) -> None:
    with pytest.raises(RegistryConfigError) as caught:
        _load_active_mechanics_bundle_from_root(root)
    assert caught.value.code == code


def test_synthetic_complete_release_is_labeled_and_admits_exact_identities(release_root: Path) -> None:
    bundle = _load_active_mechanics_bundle_from_root(release_root)
    manifest_raw = (release_root / "catalog/manifest.json").read_bytes()
    mechanics_raw = (release_root / "catalog/magic10_mechanics_v1.json").read_bytes()

    assert "synthetic-complete-release-only" in release_root.name
    assert isinstance(bundle, AdmittedMechanicsBundle)
    assert bundle.manifest.version == ADMITTED_RELEASE_VERSION
    assert bundle.manifest.built_at_utc == ADMITTED_RELEASE_BUILT_AT_UTC
    assert tuple(row.path for row in bundle.manifest.files) == ADMITTED_RELEASE_ROSTER
    assert tuple(row.path for row in bundle.source_identities) == ADMITTED_RELEASE_ROSTER
    assert bundle.config_sha256 == hashlib.sha256(mechanics_raw).hexdigest()
    assert bundle.manifest_sha256 == hashlib.sha256(manifest_raw).hexdigest()
    assert bundle.release_id == bundle.manifest_sha256
    assert bundle.release_id != bundle.config_sha256
    for identity in bundle.source_identities:
        raw = (release_root / identity.path).read_bytes()
        assert identity.sha256 == hashlib.sha256(raw).hexdigest()
        assert identity.size == len(raw)


def test_actual_partial_repository_cannot_return_an_active_handle(monkeypatch, release_root: Path) -> None:
    monkeypatch.chdir(release_root)
    monkeypatch.setenv("HDE_CONFIG_ROOT", str(release_root))
    monkeypatch.setenv("HDE_RELEASE_ID", _manifest(release_root)["files"][0]["sha256"])
    assert tuple(inspect.signature(load_active_mechanics_bundle).parameters) == ()
    with pytest.raises(RegistryConfigError) as caught:
        load_active_mechanics_bundle()
    assert caught.value.code == "INCOMPLETE_RELEASE_ROSTER"


def test_candidate_apis_do_not_return_release_bearing_handles() -> None:
    root = Path(__file__).resolve().parents[2]
    candidate = registry_loader._capture_mechanics_config(root)
    registry = registry_loader.load_registry_config(root)
    assert not isinstance(candidate, AdmittedMechanicsBundle)
    assert not hasattr(candidate, "release_id")
    assert not hasattr(registry, "release_id")


@pytest.mark.parametrize("retarget", [False, True])
def test_public_admission_refuses_symlinked_import_root(
    tmp_path: Path, release_root: Path, monkeypatch, retarget: bool,
) -> None:
    imported_alias = tmp_path / "current-release"
    imported_alias.symlink_to(release_root, target_is_directory=True)
    monkeypatch.setattr(
        registry_loader, "__file__", str(imported_alias / "engine/config/registry_loader.py")
    )
    if retarget:
        next_parent = tmp_path / "next"
        next_parent.mkdir()
        next_root = synthetic_complete_release_root(next_parent)
        imported_alias.unlink()
        imported_alias.symlink_to(next_root, target_is_directory=True)
    with pytest.raises(RegistryConfigError) as caught:
        load_active_mechanics_bundle()
    assert caught.value.code == "UNSAFE_SOURCE_PATH"


def test_public_admission_never_resolves_relative_module_path_from_cwd(monkeypatch) -> None:
    monkeypatch.setattr(registry_loader, "__file__", "engine/config/registry_loader.py")
    with pytest.raises(RegistryConfigError) as caught:
        load_active_mechanics_bundle()
    assert caught.value.code == "UNSAFE_SOURCE_PATH"


def test_source_changed_after_its_verification_read_is_refused(release_root: Path, monkeypatch) -> None:
    original = registry_loader._read_captured_file
    reads = 0

    def replace_verified_manifest(root, relative_path):
        nonlocal reads
        result = original(root, relative_path)
        if relative_path == "catalog/manifest.json":
            reads += 1
            if reads == 2:
                # Initial capture was read 1. Change a source after read 2
                # returned its old verified bytes, while other reads remain.
                (root / relative_path).write_bytes(b"{}\n")
        return result

    monkeypatch.setattr(registry_loader, "_read_captured_file", replace_verified_manifest)
    _expect_code(release_root, "SOURCE_CHANGED")
    assert reads == 2


def test_source_removed_during_final_identity_check_has_typed_refusal(release_root: Path, monkeypatch) -> None:
    capture = _LocalCapture(release_root)
    capture.read("catalog/gates_v1.json")
    original = registry_loader._safe_source_path
    calls = 0

    def remove_after_safe_path(root, relative_path):
        nonlocal calls
        result = original(root, relative_path)
        calls += 1
        if calls == 3:
            result.unlink()
        return result

    monkeypatch.setattr(registry_loader, "_safe_source_path", remove_after_safe_path)
    with pytest.raises(RegistryConfigError) as caught:
        capture.verify_unchanged()
    assert caught.value.code == "SOURCE_CHANGED"
    assert calls == 3


@pytest.mark.parametrize(
    ("raw", "code"),
    [
        (b'{"x":1,"x":2}\n', "DUPLICATE_JSON_KEY"),
        (b'{"nested":{"x":1,"x":2}}\n', "DUPLICATE_JSON_KEY"),
        (b'{"nested":[{"x":1,"x":2}]}\n', "DUPLICATE_JSON_KEY"),
        (b'\xef\xbb\xbf{}\n', "INVALID_UTF8"),
        (b'{}\r\n', "NONCANONICAL_JSON"),
        (b'{}\n\n', "NONCANONICAL_JSON"),
        (b'{ "x": 1 }\n', "NONCANONICAL_JSON"),
        (b'{"z":1,"a":2}\n', "NONCANONICAL_JSON"),
        (b'{"x":1e0}\n', "NONCANONICAL_JSON"),
        (b'{"x":NaN}\n', "NONFINITE_JSON"),
        (b'{"x":"\xff"}\n', "INVALID_JSON"),
    ],
)
def test_json_member_bytes_fail_before_admission(release_root: Path, raw: bytes, code: str) -> None:
    path = release_root / "errors/token_map/token_map.json"
    path.write_bytes(raw)
    write_synthetic_release_manifest(release_root)
    _expect_code(release_root, code)


@pytest.mark.parametrize(
    ("relative_path", "raw", "code"),
    [
        ("engine/magic10/signals.py", b"if invalid syntax\n", "INVALID_PYTHON_MEMBER"),
        ("engine/magic10/signals.py", b"\n", "EMPTY_MEMBER"),
        ("engine/magic10/signals.py", b"pass\n\n", "INVALID_MEMBER_FINAL_LF"),
        ("engine/magic10/signals.py", b"pass\r\n", "INVALID_MEMBER_FINAL_LF"),
        ("engine/magic10/signals.py", b"pass", "INVALID_MEMBER_FINAL_LF"),
        ("engine/magic10/signals.py", b"\xef\xbb\xbfpass\n", "INVALID_UTF8"),
        ("engine/magic10/signals.py", b"\xff\n", "INVALID_UTF8"),
        ("migrations/005_identity.sql", b"\n", "EMPTY_MEMBER"),
        ("migrations/005_identity.sql", b"select 1;\n\n", "INVALID_MEMBER_FINAL_LF"),
        ("migrations/005_identity.sql", b"select 1;\r\n", "INVALID_MEMBER_FINAL_LF"),
        ("migrations/005_identity.sql", b"\xef\xbb\xbfselect 1;\n", "INVALID_UTF8"),
        ("migrations/005_identity.sql", b"\xff\n", "INVALID_UTF8"),
    ],
)
def test_text_member_format_is_exact(
    release_root: Path, relative_path: str, raw: bytes, code: str
) -> None:
    (release_root / relative_path).write_bytes(raw)
    write_synthetic_release_manifest(release_root)
    _expect_code(release_root, code)


def test_capture_refuses_an_unapproved_extension(release_root: Path) -> None:
    path = release_root / "unsupported.txt"
    path.write_text("unsupported\n", encoding="utf-8")
    capture = _LocalCapture(release_root)
    with pytest.raises(SchemaValidationError) as caught:
        capture.capture_release_member("unsupported.txt")
    assert caught.value.code == "UNSUPPORTED_MEMBER_FORMAT"


def test_manifest_hash_and_size_bind_exact_unmodified_bytes(release_root: Path) -> None:
    target = release_root / "engine/magic10/signals.py"
    target.write_bytes(target.read_bytes().replace(b"placeholder", b"replacement"))
    _expect_code(release_root, "MANIFEST_MEMBER_HASH_MISMATCH")

    write_synthetic_release_manifest(release_root)
    manifest = _manifest(release_root)
    row = next(item for item in manifest["files"] if item["path"] == "engine/magic10/signals.py")
    row["size"] += 1
    _write_manifest(release_root, manifest)
    _expect_code(release_root, "MANIFEST_MEMBER_SIZE_MISMATCH")


def test_manifest_requires_exact_roster_version_and_timestamp(release_root: Path) -> None:
    manifest = _manifest(release_root)
    manifest["files"].pop()
    _write_manifest(release_root, manifest)
    _expect_code(release_root, "INCOMPLETE_RELEASE_ROSTER")

    write_synthetic_release_manifest(release_root)
    manifest = _manifest(release_root)
    extra = release_root / "unexpected.json"
    extra.write_bytes(b"{}\n")
    manifest["files"].append(
        {"path": "unexpected.json", "sha256": hashlib.sha256(b"{}\n").hexdigest(), "size": 3}
    )
    manifest["files"].sort(key=lambda row: row["path"])
    _write_manifest(release_root, manifest)
    _expect_code(release_root, "RELEASE_ROSTER_MISMATCH")

    write_synthetic_release_manifest(release_root)
    manifest = _manifest(release_root)
    manifest["version"] = "1.1.1"
    _write_manifest(release_root, manifest)
    _expect_code(release_root, "RELEASE_VERSION_MISMATCH")

    manifest["version"] = ADMITTED_RELEASE_VERSION
    manifest["built_at_utc"] = "2026-08-24T18:04:48Z"
    _write_manifest(release_root, manifest)
    _expect_code(release_root, "RELEASE_TIMESTAMP_MISMATCH")


@pytest.mark.parametrize("unsafe", ["/absolute.json", "../escape.json", "a\\b.json", "a/./b.json", "a//b.json"])
def test_manifest_member_paths_remain_canonical(release_root: Path, unsafe: str) -> None:
    manifest = _manifest(release_root)
    manifest["files"][0]["path"] = unsafe
    _write_manifest(release_root, manifest)
    _expect_code(release_root, "INVALID_MANIFEST_PATH")


def test_member_leaf_and_ancestor_symlinks_are_refused(release_root: Path, tmp_path: Path) -> None:
    target = release_root / "engine/magic10/signals.py"
    outside = tmp_path / "outside.py"
    outside.write_text("pass\n", encoding="utf-8")
    target.unlink()
    target.symlink_to(outside)
    _expect_code(release_root, "UNSAFE_SOURCE_PATH")

    target.unlink()
    target.write_text('"""Synthetic nonfunctional future-owner placeholder."""\n', encoding="utf-8")
    write_synthetic_release_manifest(release_root)
    token_dir = release_root / "errors/token_map"
    outside_dir = tmp_path / "outside-token-map"
    outside_dir.mkdir()
    shutil.copy2(token_dir / "token_map.json", outside_dir / "token_map.json")
    shutil.rmtree(token_dir)
    token_dir.symlink_to(outside_dir, target_is_directory=True)
    _expect_code(release_root, "UNSAFE_SOURCE_PATH")


def test_missing_and_nonregular_members_are_refused(release_root: Path) -> None:
    target = release_root / "engine/magic10/signals.py"
    target.unlink()
    _expect_code(release_root, "MISSING_FILE")
    target.mkdir()
    _expect_code(release_root, "UNSAFE_SOURCE_PATH")


def test_selected_root_itself_cannot_be_a_symlink(tmp_path: Path) -> None:
    actual = synthetic_complete_release_root(tmp_path / "actual")
    link = tmp_path / "linked-root"
    link.symlink_to(actual, target_is_directory=True)
    _expect_code(link, "UNSAFE_SOURCE_PATH")


def test_two_valid_roots_never_cross_read(tmp_path: Path) -> None:
    first_root = synthetic_complete_release_root(tmp_path / "first")
    second_root = synthetic_complete_release_root(tmp_path / "second")
    second_member = second_root / "engine/magic10/signals.py"
    second_member.write_text('"""Distinct synthetic placeholder."""\n', encoding="utf-8")
    write_synthetic_release_manifest(second_root)

    first = _load_active_mechanics_bundle_from_root(first_root)
    second = _load_active_mechanics_bundle_from_root(second_root)
    assert first.config_sha256 == second.config_sha256
    assert first.manifest_sha256 != second.manifest_sha256
    first_signals = next(row for row in first.source_identities if row.path == "engine/magic10/signals.py")
    second_signals = next(row for row in second.source_identities if row.path == "engine/magic10/signals.py")
    assert first_signals.sha256 != second_signals.sha256


def test_schema_identity_remote_reference_and_relation_fail_closed(release_root: Path) -> None:
    schema_path = release_root / "schemas/reader.v1.schema.json"
    schema = json.loads(schema_path.read_bytes())
    schema["$id"] = "https://example.invalid/changed"
    write_canonical(schema_path, schema)
    write_synthetic_release_manifest(release_root)
    _expect_code(release_root, "SCHEMA_IDENTITY_MISMATCH")

    schema["$id"] = "https://example.org/schemas/reader.v1.schema.json"
    schema["$defs"]["category"]["$ref"] = "https://example.invalid/remote.json"
    write_canonical(schema_path, schema)
    write_synthetic_release_manifest(release_root)
    _expect_code(release_root, "NONLOCAL_SCHEMA_REFERENCE")

    schema = json.loads((Path(__file__).resolve().parents[2] / "schemas/reader.v1.schema.json").read_bytes())
    write_canonical(schema_path, schema)
    gates_path = release_root / "catalog/gates_v1.json"
    gates = json.loads(gates_path.read_bytes())
    gates["gates"][0]["center"] = "head"
    write_canonical(gates_path, gates)
    write_synthetic_release_manifest(release_root)
    _expect_code(release_root, "GATE_CENTER_COUNTS_MISMATCH")


def test_mechanics_defaults_and_source_bindings_remain_closed(release_root: Path) -> None:
    path = release_root / "catalog/magic10_mechanics_v1.json"
    mechanics = json.loads(path.read_bytes())
    mechanics["config_id"] = "unapproved-config"
    write_canonical(path, mechanics)
    write_synthetic_release_manifest(release_root)
    _expect_code(release_root, "INITIAL_CONFIG_ID_MISMATCH")

    mechanics["config_id"] = "m10-channel-state-v1.0.0"
    mechanics["sources"]["caps"]["sha256"] = "0" * 64
    write_canonical(path, mechanics)
    write_synthetic_release_manifest(release_root)
    _expect_code(release_root, "MECHANICS_SOURCE_MISMATCH")


@pytest.mark.parametrize(
    ("reference", "code"),
    [
        ("#/$defs/missing", "UNRESOLVED_SCHEMA_REFERENCE"),
        ("#missing-anchor", "UNRESOLVED_SCHEMA_REFERENCE"),
        ("#/$id", "INVALID_SCHEMA_REFERENCE_TARGET"),
    ],
)
def test_result_schema_references_must_resolve_without_constructing_a_result(
    release_root: Path, reference: str, code: str
) -> None:
    path = release_root / "schemas/reader.v1.schema.json"
    schema = json.loads(path.read_bytes())
    schema["properties"]["categories"]["items"]["$ref"] = reference
    write_canonical(path, schema)
    write_synthetic_release_manifest(release_root)
    _expect_code(release_root, code)


def test_nested_schema_identity_cannot_redirect_local_resolution(release_root: Path) -> None:
    path = release_root / "schemas/reader.v1.schema.json"
    schema = json.loads(path.read_bytes())
    schema["$defs"]["category"]["$id"] = "https://example.invalid/alternate.json"
    write_canonical(path, schema)
    write_synthetic_release_manifest(release_root)
    _expect_code(release_root, "NESTED_SCHEMA_ID_FORBIDDEN")


def test_admitted_graph_is_recursively_immutable(release_root: Path) -> None:
    bundle = _load_active_mechanics_bundle_from_root(release_root)
    assert isinstance(bundle.registry.gates, MappingProxyType)
    assert isinstance(bundle.registry.magic10_caps["harmony"].bounds, MappingProxyType)
    assert isinstance(bundle.mechanics, MappingProxyType)
    assert isinstance(bundle.mechanics["profiles"], tuple)
    assert isinstance(bundle.mechanics["profiles"][0], MappingProxyType)
    assert isinstance(bundle.mechanics["profiles"][0]["responses"], MappingProxyType)
    assert isinstance(bundle.mechanics["signals"][0]["channels"], tuple)

    with pytest.raises(TypeError):
        bundle.registry.gates[1] = bundle.registry.gates[1]
    with pytest.raises(TypeError):
        bundle.registry.magic10_caps["harmony"].bounds["min"] = 1
    with pytest.raises(TypeError):
        bundle.mechanics["config_id"] = "changed"
    with pytest.raises(TypeError):
        bundle.mechanics["profiles"][0]["responses"]["none"] = 1
    with pytest.raises(FrozenInstanceError):
        bundle.source_identities[0].size = 0


def test_source_replacement_during_final_verification_returns_no_handle(
    release_root: Path, monkeypatch
) -> None:
    original = registry_loader._read_captured_file
    target = "engine/magic10/signals.py"
    calls = 0

    def replace_on_verify(root: Path, relative_path: str):
        nonlocal calls
        if relative_path == target:
            calls += 1
            if calls == 2:
                path = Path(root) / target
                path.write_text('"""Changed after validation."""\n', encoding="utf-8")
        return original(root, relative_path)

    monkeypatch.setattr(registry_loader, "_read_captured_file", replace_on_verify)
    _expect_code(release_root, "SOURCE_CHANGED")
    assert calls == 2


def test_no_stale_success_fallback_and_fresh_repair_can_succeed(release_root: Path) -> None:
    first = _load_active_mechanics_bundle_from_root(release_root)
    target = release_root / "engine/magic10/signals.py"
    original = target.read_bytes()
    target.write_text('"""Corrupts the manifest binding."""\n', encoding="utf-8")
    _expect_code(release_root, "MANIFEST_MEMBER_HASH_MISMATCH")
    assert first.source_identities

    target.write_bytes(original)
    repaired = _load_active_mechanics_bundle_from_root(release_root)
    assert repaired == first


def test_post_return_source_mutation_cannot_mutate_the_prior_bundle(release_root: Path) -> None:
    bundle = _load_active_mechanics_bundle_from_root(release_root)
    original_config_id = bundle.mechanics["config_id"]
    path = release_root / "catalog/magic10_mechanics_v1.json"
    mechanics = json.loads(path.read_bytes())
    mechanics["config_id"] = "changed-after-return"
    write_canonical(path, mechanics)
    assert bundle.mechanics["config_id"] == original_config_id


def test_every_reachable_container_and_record_is_immutable(release_root: Path) -> None:
    bundle = _load_active_mechanics_bundle_from_root(release_root)
    visited = set()
    counts = {"mapping": 0, "tuple": 0, "record": 0}

    def inspect_value(value):
        if id(value) in visited:
            return
        visited.add(id(value))
        assert not isinstance(value, (dict, list, set))
        if isinstance(value, Mapping):
            counts["mapping"] += 1
            with pytest.raises(TypeError):
                value["mutation-probe"] = None
            for item in value.values():
                inspect_value(item)
        elif isinstance(value, tuple):
            counts["tuple"] += 1
            if value:
                with pytest.raises(TypeError):
                    value[0] = None
            for item in value:
                inspect_value(item)
        elif is_dataclass(value):
            counts["record"] += 1
            assert not hasattr(value, "__dict__")
            with pytest.raises(TypeError):
                vars(value)
            for item in fields(value):
                with pytest.raises(FrozenInstanceError):
                    setattr(value, item.name, None)
                inspect_value(getattr(value, item.name))

    inspect_value(bundle)
    assert counts["mapping"] > 100
    assert counts["tuple"] > 100
    assert counts["record"] > 150


def test_parser_and_registry_aliases_cannot_mutate_admitted_values(release_root: Path, monkeypatch) -> None:
    captures = []
    original = registry_loader._MechanicsCapture.verify_unchanged

    def retain_capture(capture):
        original(capture)
        captures.append(capture)

    monkeypatch.setattr(registry_loader._MechanicsCapture, "verify_unchanged", retain_capture)
    bundle = _load_active_mechanics_bundle_from_root(release_root)
    capture = captures[-1]
    capture.config["profiles"][0]["responses"]["none"] = 99
    capture.config["signals"][0]["channels"][0]["weight"] = 99
    capture.config["category_weights"][0]["weights"][0] = 99
    capture.config["sources"]["caps"]["sha256"] = "0" * 64
    capture.registry.magic10_caps["harmony"].bounds["max"] = 99
    # The admitted graph owns new records, even if privileged test machinery
    # mutates a retained candidate record through frozen-dataclass internals.
    gate_before = bundle.registry.gates[1].center
    channel_id = next(iter(capture.registry.channels))
    channel_before = bundle.registry.channels[channel_id].primary_domain
    seed_id = next(iter(capture.registry.magic10_seeds))
    seed_before = bundle.registry.magic10_seeds[seed_id].template_id
    assert bundle.registry.gates[1] is not capture.registry.gates[1]
    assert bundle.registry.channels[channel_id] is not capture.registry.channels[channel_id]
    assert bundle.registry.magic10_seeds[seed_id] is not capture.registry.magic10_seeds[seed_id]
    object.__setattr__(capture.registry.gates[1], "center", "mutation-probe")
    object.__setattr__(capture.registry.channels[channel_id], "primary_domain", "mutation-probe")
    object.__setattr__(capture.registry.magic10_seeds[seed_id], "template_id", "mutation-probe")
    capture.registry.gates.clear()
    capture.registry.channels.clear()
    assert bundle.mechanics["profiles"][0]["responses"]["none"] == 0
    assert bundle.mechanics["signals"][0]["channels"][0]["weight"] == 1
    assert bundle.mechanics["category_weights"][0]["weights"] == (1, 1)
    assert bundle.mechanics["sources"]["caps"]["sha256"] != "0" * 64
    assert bundle.registry.magic10_caps["harmony"].bounds["max"] == 100
    assert bundle.registry.gates[1].center == gate_before
    assert bundle.registry.channels[channel_id].primary_domain == channel_before
    assert bundle.registry.magic10_seeds[seed_id].template_id == seed_before
    assert len(bundle.registry.gates) == 64
    assert len(bundle.registry.channels) == 36
