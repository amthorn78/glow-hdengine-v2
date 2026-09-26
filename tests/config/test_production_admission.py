from __future__ import annotations

import hashlib
import inspect
import json
import os
import py_compile
import shutil
import subprocess
import sys
from dataclasses import FrozenInstanceError, fields, is_dataclass
from collections.abc import Mapping
from pathlib import Path
from types import MappingProxyType

import pytest

from engine.config import registry_loader
from engine.core import core as pure_core
from engine.runtime.identity import identity_meta
from engine.serializer import canon
from engine.magic10 import calculators, composite, signals
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
    closed_rails_env,
    synthetic_complete_release_root,
    write_canonical,
    write_synthetic_release_manifest,
)


MECHANICS_EXECUTION_PATHS = (
    "engine/core/core.py", "engine/magic10/composite.py",
    "engine/magic10/signals.py", "engine/magic10/calculators.py",
)
MECHANICS_OWNERS = dict(zip(MECHANICS_EXECUTION_PATHS, (pure_core, composite, signals, calculators)))


@pytest.mark.parametrize("path", MECHANICS_EXECUTION_PATHS)
def test_pr03_r02_rehashed_different_mechanics_refuse(release_root: Path, path: str) -> None:
    source = release_root / path
    raw = source.read_bytes()
    if path == "engine/magic10/signals.py":
        old = b"numerator += weight * responses[row.state]"
        assert raw.count(old) == 1
        changed = raw.replace(old, b"numerator -= weight * responses[row.state]")
    else:
        changed = raw + b"raise RuntimeError('captured mechanics must never execute')\n"
    compile(changed, str(source), "exec")
    source.write_bytes(changed)
    write_synthetic_release_manifest(release_root)
    _expect_code(release_root, "EXECUTING_SOURCE_MISMATCH")


@pytest.fixture
def release_root(tmp_path: Path) -> Path:
    return synthetic_complete_release_root(tmp_path)


def test_execution_roster_preserves_four_accepted_owners_and_adds_exactly_four() -> None:
    root, executions = registry_loader._admission_execution_provenance()
    assert root == Path(__file__).resolve().parents[2]
    assert tuple(path for path, _, _ in executions) == (
        "engine/config/registry_loader.py", "engine/serializer/canon.py",
        "engine/stable/sercanon.py", "engine/categories/registry.py",
        *MECHANICS_EXECUTION_PATHS,
    )


@pytest.mark.parametrize("path", MECHANICS_EXECUTION_PATHS)
@pytest.mark.parametrize("defect,expected", [
    ("missing", "EXECUTION_PROVENANCE_UNAVAILABLE"),
    ("partial_tuple", "EXECUTION_PROVENANCE_UNAVAILABLE"),
    ("nonmodule_code", "EXECUTION_PROVENANCE_UNAVAILABLE"),
    ("initializing", "EXECUTION_PROVENANCE_UNAVAILABLE"),
    ("optimization", "EXECUTION_SEMANTICS_MISMATCH"),
    ("cache_tag", "EXECUTION_SEMANTICS_MISMATCH"),
    ("origin", "UNSAFE_SOURCE_PATH"),
    ("live_origin", "UNSAFE_SOURCE_PATH"),
])
def test_mechanics_provenance_refuses_before_admission(
    release_root: Path, monkeypatch, path: str, defect: str, expected: str,
) -> None:
    owner = MECHANICS_OWNERS[path]
    provenance = list(owner._MODULE_EXECUTION)
    if defect == "missing":
        value = None
    elif defect == "partial_tuple":
        value = tuple(provenance[:-1])
    elif defect == "nonmodule_code":
        provenance[0] = test_mechanics_provenance_refuses_before_admission.__code__
        value = tuple(provenance)
    elif defect == "optimization":
        provenance[4] = (sys.flags.optimize + 1) % 3
        value = tuple(provenance)
    elif defect == "cache_tag":
        provenance[5] = "incompatible-interpreter"
        value = tuple(provenance)
    elif defect == "origin":
        provenance[3] = "relative/source.py"
        value = tuple(provenance)
    else:
        value = tuple(provenance)
        if defect == "initializing":
            monkeypatch.setattr(owner.__spec__, "_initializing", True, raising=False)
        else:
            monkeypatch.setattr(owner.__spec__, "origin", str(release_root / path))
    monkeypatch.setattr(owner, "_MODULE_EXECUTION", value)
    _expect_code(release_root, expected)
    # A production refusal does not take over accepted candidate APIs.
    assert len(registry_loader.load_registry_config(release_root).gates) == 64


@pytest.mark.parametrize("path", MECHANICS_EXECUTION_PATHS)
def test_mechanics_same_executable_different_bytes_preserve_math_not_release_identity(
    release_root: Path, path: str,
) -> None:
    from engine.bodygraph.gates import normalize_gates
    from engine.serializer.canon import sercanon

    before = _load_active_mechanics_bundle_from_root(release_root)
    source = release_root / path
    source.write_bytes(source.read_bytes() + b"# Nonexecuting trailing comment.\n")
    write_synthetic_release_manifest(release_root)
    after = _load_active_mechanics_bundle_from_root(release_root)
    a = normalize_gates([5, 19, 20, 34, 43, 49])
    b = normalize_gates([9, 12, 15, 22, 23, 52])
    old = pure_core.compute_core(a, b, before, before.release_id)
    new = pure_core.compute_core(a, b, after, after.release_id)
    assert old.signals == new.signals and old.categories == new.categories
    assert old.config_id == new.config_id
    assert old.release_id != new.release_id and old.pair_key != new.pair_key
    assert sercanon(new.to_payload()) == sercanon(
        pure_core.compute_core(b, a, after, after.release_id).to_payload(),
    )


@pytest.mark.parametrize("path", MECHANICS_EXECUTION_PATHS)
def test_mechanics_uncaptured_source_has_no_fallback_read(release_root: Path, monkeypatch, path: str) -> None:
    original = registry_loader._validate_executing_admission_sources

    def omit_source(capture, executions):
        capture.sources.pop(path)
        return original(capture, executions)

    monkeypatch.setattr(registry_loader, "_validate_executing_admission_sources", omit_source)
    _expect_code(release_root, "UNBOUND_SOURCE")


@pytest.mark.parametrize("path", MECHANICS_EXECUTION_PATHS)
def test_mechanics_capture_that_parses_but_cannot_compile_refuses(release_root: Path, path: str) -> None:
    # ast.parse accepts this module-level statement; passive compile must refuse.
    (release_root / path).write_bytes(b"return\n")
    write_synthetic_release_manifest(release_root)
    _expect_code(release_root, "EXECUTION_COMPILATION_FAILED")


@pytest.mark.parametrize("path", MECHANICS_EXECUTION_PATHS)
def test_mechanics_changed_after_capture_is_not_reread_or_executed(
    release_root: Path, monkeypatch, path: str,
) -> None:
    original = registry_loader._read_captured_file
    changed = False

    def change_after_capture(root, relative):
        nonlocal changed
        result = original(root, relative)
        if relative == path and not changed:
            changed = True
            (root / path).write_bytes(b"raise RuntimeError('not executed')\n")
        return result

    monkeypatch.setattr(registry_loader, "_read_captured_file", change_after_capture)
    _expect_code(release_root, "SOURCE_CHANGED")
    assert changed


def _isolated_mechanics_script(root: Path, script: str, *, optimization: int = 0) -> dict:
    # Test-only package scaffolding, not additional release-manifest members.
    for package in ("engine", "engine/config", "engine/serializer", "engine/stable", "engine/categories"):
        (root / package / "__init__.py").write_bytes(b"")
    options = ["-I"] + (["-" + "O" * optimization] if optimization else [])
    result = subprocess.run(
        [sys.executable, *options, "-c", script, str(root)], cwd=root,
        env=closed_rails_env(), text=True, capture_output=True, timeout=30,
    )
    assert result.returncode == 0, result.stderr
    assert result.stderr == ""
    return json.loads(result.stdout)


_MECHANICS_IMPORT_SCRIPT = """
import json, sys
from pathlib import Path
root = Path(sys.argv[1])
sys.path.insert(0, str(root))
"""
_MECHANICS_ADMIT_SCRIPT = """
try:
    bundle = loader.load_active_mechanics_bundle()
except loader.RegistryConfigError as exc:
    result = {'state': 'refused', 'code': exc.code}
else:
    result = {'state': 'admitted', 'members': len(bundle.source_identities)}
"""


@pytest.mark.parametrize("first", ["loader", "core"])
@pytest.mark.parametrize("optimization", [0, 1, 2])
def test_mechanics_fresh_startup_and_optimization_semantics(
    release_root: Path, first: str, optimization: int,
) -> None:
    script = _MECHANICS_IMPORT_SCRIPT
    if first == "core":
        script += "from engine.core import core\n"
    script += "from engine.config import registry_loader as loader\n"
    script += _MECHANICS_ADMIT_SCRIPT + "print(json.dumps(result))\n"
    assert _isolated_mechanics_script(release_root, script, optimization=optimization) == {
        "state": "admitted", "members": 45,
    }


@pytest.mark.parametrize("path", MECHANICS_EXECUTION_PATHS)
def test_mechanics_timestamp_valid_stale_bytecode_refuses_and_fresh_source_admits(
    release_root: Path, path: str,
) -> None:
    source = release_root / path
    raw_a = source.read_bytes() + b"\ndef _r02_behavior():\n    return 'A'\n"
    source.write_bytes(raw_a)
    before = source.stat()
    cached = Path(py_compile.compile(
        str(source), doraise=True, invalidation_mode=py_compile.PycInvalidationMode.TIMESTAMP,
    ))
    raw_b = raw_a.replace(b"return 'A'", b"return 'B'")
    assert raw_a != raw_b and len(raw_a) == len(raw_b)
    source.write_bytes(raw_b)
    os.utime(source, ns=(before.st_atime_ns, before.st_mtime_ns))
    write_synthetic_release_manifest(release_root)
    script = _MECHANICS_IMPORT_SCRIPT + "from engine.config import registry_loader as loader\n"
    script += _MECHANICS_ADMIT_SCRIPT
    name = path.removesuffix(".py").replace("/", ".")
    script += f"result['behavior'] = sys.modules[{name!r}]._r02_behavior()\nprint(json.dumps(result))\n"
    assert _isolated_mechanics_script(release_root, script) == {
        "state": "refused", "code": "EXECUTING_SOURCE_MISMATCH", "behavior": "A",
    }
    cached.unlink()
    assert _isolated_mechanics_script(release_root, script) == {
        "state": "admitted", "members": 45, "behavior": "B",
    }


@pytest.mark.parametrize("path", MECHANICS_EXECUTION_PATHS)
def test_mechanics_unavailable_import_frame_fails_closed_without_breaking_candidates(
    release_root: Path, path: str,
) -> None:
    name = path.removesuffix(".py").replace("/", ".")
    script = _MECHANICS_IMPORT_SCRIPT + f"""
from engine.config import registry_loader as loader
original_frame = sys._getframe
def unavailable_frame(depth=0):
    frame = original_frame(depth + 1)
    if depth == 0 and frame.f_code.co_name == '<module>' and frame.f_globals.get('__name__') == {name!r}:
        raise RuntimeError('frame provenance unavailable')
    return frame
sys._getframe = unavailable_frame
from engine.core import core
sys._getframe = original_frame
assert len(loader.load_registry_config(root).gates) == 64
"""
    script += _MECHANICS_ADMIT_SCRIPT + "print(json.dumps(result))\n"
    assert _isolated_mechanics_script(release_root, script) == {
        "state": "refused", "code": "EXECUTION_PROVENANCE_UNAVAILABLE",
    }


@pytest.mark.parametrize("path", MECHANICS_EXECUTION_PATHS)
def test_mechanics_origin_cannot_come_from_a_different_installation(
    release_root: Path, monkeypatch, path: str,
) -> None:
    owner = MECHANICS_OWNERS[path]
    provenance = list(owner._MODULE_EXECUTION)
    filename = str(release_root / path)
    provenance[0] = provenance[0].replace(co_filename=filename)
    provenance[2] = provenance[3] = filename
    monkeypatch.setattr(owner, "_MODULE_EXECUTION", tuple(provenance))
    monkeypatch.setattr(owner, "__file__", filename)
    monkeypatch.setattr(owner.__spec__, "origin", filename)
    _expect_code(release_root, "UNSAFE_SOURCE_PATH")


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
    assert len(ADMITTED_RELEASE_ROSTER) == 45
    assert "schemas/gates_v1.schema.json" in ADMITTED_RELEASE_ROSTER
    assert "schemas/reader.v2.schema.json" in ADMITTED_RELEASE_ROSTER
    assert "engine/stable/sercanon.py" in ADMITTED_RELEASE_ROSTER
    assert "engine/categories/registry.py" in ADMITTED_RELEASE_ROSTER
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


# The fifteen members of the pre-PR06 release manifest (version 1.0.0).
_PRE_PR06_MEMBERS = frozenset({
    "adapter/http_reader.py",
    "catalog/channels_v1.json",
    "catalog/gates_v1.json",
    "catalog/magic10.json",
    "catalog/magic10_caps.json",
    "catalog/magic10_seeds.json",
    "catalog/narratives/keys.json",
    "catalog/narratives/manifest.json",
    "catalog/narratives/palettes.json",
    "catalog/narratives/suppression_map.json",
    "catalog/narratives/templates.json",
    "engine/presenter/emitter.py",
    "engine/serializer/canon.py",
    "math/thresholds.json",
    "migrations/005_identity.sql",
})


def test_actual_repository_root_admits(monkeypatch, release_root: Path) -> None:
    """The real repository root admits through the parameterless owner.

    The owner derives its root from execution provenance: a working directory
    and HDE_CONFIG_ROOT that point at a fixture select nothing.
    """
    monkeypatch.chdir(release_root)
    monkeypatch.setenv("HDE_CONFIG_ROOT", str(release_root))
    monkeypatch.setenv("HDE_RELEASE_ID", _manifest(release_root)["files"][0]["sha256"])
    assert tuple(inspect.signature(load_active_mechanics_bundle).parameters) == ()
    bundle = load_active_mechanics_bundle()
    root = Path(__file__).resolve().parents[2]
    raw = (root / "catalog/manifest.json").read_bytes()
    assert raw == canon.sercanon(json.loads(raw), sort_keys=True)
    assert bundle.manifest.version == ADMITTED_RELEASE_VERSION == "1.2.0"
    assert bundle.manifest.built_at_utc == ADMITTED_RELEASE_BUILT_AT_UTC
    assert len(bundle.source_identities) == 45
    assert tuple(identity.path for identity in bundle.source_identities) == ADMITTED_RELEASE_ROSTER
    for identity in bundle.source_identities:
        body = (root / identity.path).read_bytes()
        assert identity.sha256 == hashlib.sha256(body).hexdigest()
        assert identity.size == len(body)
    assert bundle.release_id == hashlib.sha256(raw).hexdigest()
    assert bundle.release_id == identity_meta()["release_id"]


def test_baseline_partial_manifest_still_refuses(release_root: Path) -> None:
    """The pre-PR06 fifteen-member manifest is still refused as an incomplete roster."""
    manifest = _manifest(release_root)
    manifest["files"] = [row for row in manifest["files"] if row["path"] in _PRE_PR06_MEMBERS]
    manifest["version"] = "1.0.0"
    manifest["built_at_utc"] = "2025-12-26T00:00:00Z"
    assert len(manifest["files"]) == 15
    write_canonical(release_root / "catalog/manifest.json", manifest)
    _expect_code(release_root, "INCOMPLETE_RELEASE_ROSTER")


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


def test_public_admission_refuses_file_only_root_substitution(
    release_root: Path, monkeypatch
) -> None:
    module_path = release_root / "engine/config/registry_loader.py"
    module_path.write_bytes(module_path.read_bytes().rstrip(b"\n") + b"\n# changed after import\n")
    write_synthetic_release_manifest(release_root)
    monkeypatch.setattr(registry_loader, "__file__", str(module_path))

    with pytest.raises(RegistryConfigError) as caught:
        load_active_mechanics_bundle()
    assert caught.value.code == "UNSAFE_SOURCE_PATH"


def test_source_changed_after_its_verification_read_is_refused(release_root: Path, monkeypatch) -> None:
    original = registry_loader._read_captured_file
    reads = 0
    target = "adapter/http_reader.py"

    def replace_verified_source(root, relative_path):
        nonlocal reads
        result = original(root, relative_path)
        if relative_path == target:
            reads += 1
            if reads == 2:
                # Initial capture was read 1. Change a source after read 2
                # returned its old verified bytes, while other reads remain.
                (root / relative_path).write_bytes(b'"""Changed after verification."""\n')
        return result

    monkeypatch.setattr(registry_loader, "_read_captured_file", replace_verified_source)
    _expect_code(release_root, "SOURCE_CHANGED")
    assert reads == 2


def test_packaged_manifest_is_physically_read_once_per_admission(
    release_root: Path, monkeypatch
) -> None:
    original = registry_loader._read_captured_file
    reads = 0

    def count_manifest_reads(root, relative_path):
        nonlocal reads
        if relative_path == "catalog/manifest.json":
            reads += 1
        return original(root, relative_path)

    monkeypatch.setattr(registry_loader, "_read_captured_file", count_manifest_reads)
    bundle = _load_active_mechanics_bundle_from_root(release_root)
    assert isinstance(bundle, AdmittedMechanicsBundle)
    assert reads == 1


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
    raw = target.read_bytes()
    # Corrupt exactly one byte without depending on the former PR03 placeholder.
    target.write_bytes(bytes([raw[0] ^ 1]) + raw[1:])
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


def test_gate_schema_is_required_and_an_unlisted_44_member_release_is_incomplete(
    release_root: Path,
) -> None:
    manifest = _manifest(release_root)
    manifest["files"] = [
        row for row in manifest["files"] if row["path"] != "schemas/gates_v1.schema.json"
    ]
    assert len(manifest["files"]) == 44
    _write_manifest(release_root, manifest)
    _expect_code(release_root, "INCOMPLETE_RELEASE_ROSTER")


def test_missing_gate_schema_member_is_refused(release_root: Path) -> None:
    (release_root / "schemas/gates_v1.schema.json").unlink()
    _expect_code(release_root, "MISSING_FILE")


@pytest.mark.parametrize(
    ("raw", "code"),
    [
        (b'{"broken":\n', "INVALID_JSON"),
        (b'{ "$id": "schemas/gates_v1.schema.json" }\n', "NONCANONICAL_JSON"),
    ],
)
def test_gate_schema_member_bytes_must_be_valid_and_canonical(
    release_root: Path, raw: bytes, code: str
) -> None:
    (release_root / "schemas/gates_v1.schema.json").write_bytes(raw)
    write_synthetic_release_manifest(release_root)
    _expect_code(release_root, code)


def test_gate_schema_hash_and_size_are_manifest_bound(release_root: Path) -> None:
    manifest = _manifest(release_root)
    row = next(
        item for item in manifest["files"] if item["path"] == "schemas/gates_v1.schema.json"
    )
    row["sha256"] = "0" * 64
    _write_manifest(release_root, manifest)
    _expect_code(release_root, "MANIFEST_MEMBER_HASH_MISMATCH")

    write_synthetic_release_manifest(release_root)
    manifest = _manifest(release_root)
    row = next(
        item for item in manifest["files"] if item["path"] == "schemas/gates_v1.schema.json"
    )
    row["size"] += 1
    _write_manifest(release_root, manifest)
    _expect_code(release_root, "MANIFEST_MEMBER_SIZE_MISMATCH")


@pytest.mark.parametrize("unsafe", ["/absolute.json", "../escape.json", "a\\b.json", "a/./b.json", "a//b.json"])
def test_manifest_member_paths_remain_canonical(release_root: Path, unsafe: str) -> None:
    manifest = _manifest(release_root)
    manifest["files"][0]["path"] = unsafe
    _write_manifest(release_root, manifest)
    _expect_code(release_root, "INVALID_MANIFEST_PATH")


def test_member_leaf_and_ancestor_symlinks_are_refused(release_root: Path, tmp_path: Path) -> None:
    target = release_root / "engine/magic10/signals.py"
    original = target.read_bytes()
    outside = tmp_path / "outside.py"
    outside.write_text("pass\n", encoding="utf-8")
    target.unlink()
    target.symlink_to(outside)
    _expect_code(release_root, "UNSAFE_SOURCE_PATH")

    target.unlink()
    target.write_bytes(original)
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
    second_member.write_bytes(second_member.read_bytes() + b"# Distinct bytes; equivalent executable.\n")
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


def test_manifest_bound_gate_schema_is_executed(release_root: Path) -> None:
    schema_path = release_root / "schemas/gates_v1.schema.json"
    write_canonical(
        schema_path,
        {
            "$id": "schemas/gates_v1.schema.json",
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "not": {},
        },
    )
    write_synthetic_release_manifest(release_root)
    _expect_code(release_root, "SCHEMA_VALIDATION_FAILED")


def test_gate_schema_remote_reference_and_source_change_fail_closed(
    release_root: Path, monkeypatch
) -> None:
    schema_path = release_root / "schemas/gates_v1.schema.json"
    schema = json.loads(schema_path.read_bytes())
    schema["$ref"] = "https://example.invalid/gates.json"
    write_canonical(schema_path, schema)
    write_synthetic_release_manifest(release_root)
    _expect_code(release_root, "NONLOCAL_SCHEMA_REFERENCE")

    source_schema = Path(__file__).resolve().parents[2] / "schemas/gates_v1.schema.json"
    schema_path.write_bytes(source_schema.read_bytes())
    write_synthetic_release_manifest(release_root)
    original = registry_loader._read_captured_file
    reads = 0

    def change_gate_schema_on_verify(root, relative_path):
        nonlocal reads
        result = original(root, relative_path)
        if relative_path == "schemas/gates_v1.schema.json":
            reads += 1
            if reads == 2:
                (root / relative_path).write_bytes(b"{}\n")
        return result

    monkeypatch.setattr(registry_loader, "_read_captured_file", change_gate_schema_on_verify)
    _expect_code(release_root, "SOURCE_CHANGED")
    assert reads == 2


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

    def retain_capture(capture, **kwargs):
        original(capture, **kwargs)
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
