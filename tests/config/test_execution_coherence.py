from __future__ import annotations

import hashlib
import json
import os
import py_compile
import subprocess
import sys
from pathlib import Path

import pytest

from engine.categories import registry as category_registry
from engine.config import registry_loader as loader
from engine.serializer import canon
from tests.config.helpers import (
    closed_rails_env,
    synthetic_complete_release_root,
    write_canonical,
    write_synthetic_release_manifest,
)


ROOT = Path(__file__).resolve().parents[2]
COVERED = (
    ("engine/config/registry_loader.py", loader),
    ("engine/serializer/canon.py", canon),
    ("engine/stable/sercanon.py", canon.stable_sercanon),
    ("engine/categories/registry.py", category_registry),
)
HELPERS = ("engine/stable/sercanon.py", "engine/categories/registry.py")


@pytest.fixture
def release_root(tmp_path: Path) -> Path:
    return synthetic_complete_release_root(tmp_path)


def _refuses(root: Path, code: str) -> None:
    with pytest.raises(loader.RegistryConfigError) as caught:
        loader._load_active_mechanics_bundle_from_root(root)
    assert caught.value.code == code


def _importable(root: Path) -> None:
    # Empty package scaffolding isolates the four real source modules from the
    # installed checkout; it is not added to the synthetic release manifest.
    for package in ("engine", "engine/config", "engine/serializer", "engine/stable", "engine/categories"):
        (root / package / "__init__.py").write_bytes(b"")


def _child(root: Path, script: str, *, optimization: int = 0) -> dict:
    options = ["-I"] + (["-" + "O" * optimization] if optimization else [])
    result = subprocess.run(
        [sys.executable, *options, "-c", script, str(root)],
        cwd=root, env=closed_rails_env(), text=True, capture_output=True,
        check=False, timeout=30,
    )
    assert result.returncode == 0, result.stderr
    assert result.stderr == ""
    return json.loads(result.stdout)


_IMPORT = """
import hashlib, json, sys
from pathlib import Path
root = Path(sys.argv[1])
sys.path.insert(0, str(root))
from engine.config import registry_loader as loader
from engine.serializer import canon
from engine.categories import registry as category_registry
owners = {
    'engine/config/registry_loader.py': loader,
    'engine/serializer/canon.py': canon,
    'engine/stable/sercanon.py': canon.stable_sercanon,
    'engine/categories/registry.py': category_registry,
}
def refresh_manifest():
    path = root / 'catalog/manifest.json'
    manifest = json.loads(path.read_bytes())
    for row in manifest['files']:
        raw = (root / row['path']).read_bytes()
        row.update(sha256=hashlib.sha256(raw).hexdigest(), size=len(raw))
    path.write_bytes(canon.sercanon(manifest))
def admit():
    try:
        bundle = loader.load_active_mechanics_bundle()
    except loader.RegistryConfigError as exc:
        return {'state': 'refused', 'code': exc.code}
    return {'state': 'admitted', 'members': len(bundle.source_identities),
            'release_id': bundle.release_id,
            'sources': {row.path: row.sha256 for row in bundle.source_identities}}
"""


@pytest.mark.parametrize("optimization", [0, 1, 2])
def test_public_fresh_execution_admits_all_four_modules_under_matching_semantics(
    release_root: Path, optimization: int,
) -> None:
    _importable(release_root)
    result = _child(release_root, _IMPORT + "print(json.dumps(admit()))\n", optimization=optimization)
    assert result["state"] == "admitted"
    assert result["members"] == 44
    assert result["release_id"] == hashlib.sha256((release_root / "catalog/manifest.json").read_bytes()).hexdigest()
    for path, _ in COVERED:
        assert result["sources"][path] == hashlib.sha256((release_root / path).read_bytes()).hexdigest()


@pytest.mark.parametrize("path,owner", COVERED, ids=[p for p, _ in COVERED])
def test_each_materially_different_captured_module_refuses_without_execution(
    release_root: Path, path: str, owner,
) -> None:
    source = release_root / path
    source.write_bytes(source.read_bytes() + b"raise RuntimeError('captured source must never execute')\n")
    write_synthetic_release_manifest(release_root)
    _refuses(release_root, "EXECUTING_SOURCE_MISMATCH")


@pytest.mark.parametrize("path,owner", COVERED, ids=[p for p, _ in COVERED])
def test_public_execution_refuses_source_replaced_after_import(
    release_root: Path, path: str, owner,
) -> None:
    _importable(release_root)
    script = _IMPORT + f"""
path = root / {path!r}
path.write_bytes(path.read_bytes() + b"raise RuntimeError('not executed')\\n")
refresh_manifest()
print(json.dumps(admit()))
"""
    assert _child(release_root, script) == {"state": "refused", "code": "EXECUTING_SOURCE_MISMATCH"}


@pytest.mark.parametrize("path,owner", COVERED, ids=[p for p, _ in COVERED])
def test_timestamp_valid_stale_bytecode_refuses_but_fresh_b_admits(
    release_root: Path, path: str, owner,
) -> None:
    _importable(release_root)
    source = release_root / path
    raw_a = source.read_bytes() + b"\ndef _f02_behavior():\n    return 'A'\n"
    source.write_bytes(raw_a)
    before = source.stat()
    cached = Path(py_compile.compile(
        str(source), doraise=True, invalidation_mode=py_compile.PycInvalidationMode.TIMESTAMP,
    ))
    raw_b = raw_a.replace(b"return 'A'", b"return 'B'")
    assert raw_a != raw_b and len(raw_a) == len(raw_b)
    source.write_bytes(raw_b)
    os.utime(source, ns=(before.st_atime_ns, before.st_mtime_ns))
    assert source.stat().st_mtime_ns == before.st_mtime_ns
    write_synthetic_release_manifest(release_root)
    script = _IMPORT + f"""
result = admit()
result['behavior'] = owners[{path!r}]._f02_behavior()
print(json.dumps(result))
"""
    stale = _child(release_root, script)
    assert stale == {"state": "refused", "code": "EXECUTING_SOURCE_MISMATCH", "behavior": "A"}
    cached.unlink()
    fresh = _child(release_root, script)
    assert fresh["state"] == "admitted"
    assert fresh["members"] == 44
    assert fresh["behavior"] == "B"
    assert fresh["sources"][path] == hashlib.sha256(raw_b).hexdigest()


def test_code_equivalence_does_not_claim_historical_raw_source_identity(release_root: Path) -> None:
    path = "engine/config/registry_loader.py"
    source = release_root / path
    old_digest = hashlib.sha256(source.read_bytes()).hexdigest()
    source.write_bytes(source.read_bytes() + b"# Nonexecuting trailing source comment.\n")
    write_synthetic_release_manifest(release_root)
    bundle = loader._load_active_mechanics_bundle_from_root(release_root)
    identity = next(row for row in bundle.source_identities if row.path == path)
    assert identity.sha256 != old_digest
    assert identity.sha256 == hashlib.sha256(source.read_bytes()).hexdigest()


@pytest.mark.parametrize("path,owner", COVERED, ids=[p for p, _ in COVERED])
@pytest.mark.parametrize("defect", ["missing", "nonmodule_code", "optimization", "cache_tag", "origin"])
def test_unusable_provenance_fails_closed_and_candidate_apis_remain_usable(
    release_root: Path, monkeypatch, path: str, owner, defect: str,
) -> None:
    provenance = list(owner._MODULE_EXECUTION)
    code = "EXECUTION_PROVENANCE_UNAVAILABLE"
    if defect == "missing":
        value = None
    elif defect == "nonmodule_code":
        provenance[0] = test_unusable_provenance_fails_closed_and_candidate_apis_remain_usable.__code__
        value = tuple(provenance)
    elif defect == "optimization":
        provenance[4] = (sys.flags.optimize + 1) % 3
        value = tuple(provenance)
        code = "EXECUTION_SEMANTICS_MISMATCH"
    elif defect == "cache_tag":
        provenance[5] = "unsupported-interpreter-semantics"
        value = tuple(provenance)
        code = "EXECUTION_SEMANTICS_MISMATCH"
    else:
        provenance[3] = "relative/source.py"
        value = tuple(provenance)
        code = "UNSAFE_SOURCE_PATH"
    monkeypatch.setattr(owner, "_MODULE_EXECUTION", value)
    _refuses(release_root, code)
    assert loader.load_registry_config(ROOT).magic10_order == category_registry.FROZEN_MAGIC10_ORDER


@pytest.mark.parametrize("path,owner", COVERED, ids=[p for p, _ in COVERED])
def test_live_origin_must_agree_with_retained_actual_origin(
    release_root: Path, monkeypatch, path: str, owner,
) -> None:
    monkeypatch.setattr(owner.__spec__, "origin", str(release_root / path))
    _refuses(release_root, "UNSAFE_SOURCE_PATH")


def test_unavailable_frame_capture_does_not_break_candidate_imports(release_root: Path) -> None:
    _importable(release_root)
    script = """
import json, sys, jsonschema
from pathlib import Path
root = Path(sys.argv[1])
sys.path.insert(0, str(root))
original = sys._getframe
covered = {
    'engine.config.registry_loader', 'engine.serializer.canon',
    'engine.stable.sercanon', 'engine.categories.registry',
}
def unavailable(depth=0):
    frame = original(depth + 1)
    if depth == 0 and frame.f_globals.get('__name__') in covered:
        raise RuntimeError('frame provenance unavailable')
    return frame
sys._getframe = unavailable
from engine.config import registry_loader as loader
sys._getframe = original
candidate = loader.load_registry_config(root)
try:
    loader.load_active_mechanics_bundle()
except loader.RegistryConfigError as exc:
    print(json.dumps({'candidate_gates': len(candidate.gates), 'code': exc.code}))
"""
    assert _child(release_root, script) == {"candidate_gates": 64, "code": "EXECUTION_PROVENANCE_UNAVAILABLE"}


@pytest.mark.parametrize("retarget", [False, True])
def test_real_public_import_through_deployment_symlink_refuses(
    tmp_path: Path, release_root: Path, retarget: bool,
) -> None:
    _importable(release_root)
    alias = tmp_path / "current"
    alias.symlink_to(release_root, target_is_directory=True)
    script = _IMPORT
    if retarget:
        parent = tmp_path / "replacement"
        parent.mkdir()
        replacement = synthetic_complete_release_root(parent)
        _importable(replacement)
        script += f"root.unlink(); root.symlink_to({str(replacement)!r}, target_is_directory=True)\n"
    assert _child(alias, script + "print(json.dumps(admit()))\n") == {"state": "refused", "code": "UNSAFE_SOURCE_PATH"}


@pytest.mark.parametrize("count", [42, 43, 45])
def test_only_the_exact_44_member_roster_admits(release_root: Path, count: int) -> None:
    path = release_root / "catalog/manifest.json"
    manifest = json.loads(path.read_bytes())
    if count < 44:
        omitted = HELPERS[:44 - count]
        manifest["files"] = [row for row in manifest["files"] if row["path"] not in omitted]
        expected = "INCOMPLETE_RELEASE_ROSTER"
    else:
        manifest["files"].append({"path": "engine/unapproved.py", "sha256": "0" * 64, "size": 1})
        manifest["files"].sort(key=lambda row: row["path"])
        expected = "RELEASE_ROSTER_MISMATCH"
    assert len(manifest["files"]) == count
    write_canonical(path, manifest)
    _refuses(release_root, expected)


@pytest.mark.parametrize("path", HELPERS)
@pytest.mark.parametrize("defect,expected", [
    ("missing", "MISSING_FILE"),
    ("malformed", "INVALID_PYTHON_MEMBER"),
    ("noncanonical", "INVALID_MEMBER_FINAL_LF"),
    ("hash", "MANIFEST_MEMBER_HASH_MISMATCH"),
    ("size", "MANIFEST_MEMBER_SIZE_MISMATCH"),
    ("symlink", "UNSAFE_SOURCE_PATH"),
])
def test_both_added_helper_sources_have_full_member_protection(
    release_root: Path, path: str, defect: str, expected: str,
) -> None:
    source = release_root / path
    if defect == "missing":
        source.unlink()
    elif defect == "malformed":
        source.write_bytes(b"def broken(:\n")
    elif defect == "noncanonical":
        source.write_bytes(source.read_bytes() + b"\n")
    elif defect in ("hash", "size"):
        manifest_path = release_root / "catalog/manifest.json"
        manifest = json.loads(manifest_path.read_bytes())
        row = next(row for row in manifest["files"] if row["path"] == path)
        if defect == "hash":
            row["sha256"] = "0" * 64
        else:
            row["size"] += 1
        write_canonical(manifest_path, manifest)
    else:
        target = source.with_suffix(".outside.py")
        source.rename(target)
        source.symlink_to(target)
    _refuses(release_root, expected)


@pytest.mark.parametrize("path", HELPERS)
def test_added_helper_changed_after_capture_is_refused(release_root: Path, monkeypatch, path: str) -> None:
    original = loader._read_captured_file
    changed = False
    def mutate_after_capture(root, relative):
        nonlocal changed
        result = original(root, relative)
        if relative == path and not changed:
            changed = True
            (root / path).write_bytes(b"raise RuntimeError('changed after capture')\n")
        return result
    monkeypatch.setattr(loader, "_read_captured_file", mutate_after_capture)
    _refuses(release_root, "SOURCE_CHANGED")


@pytest.mark.parametrize("path", HELPERS)
def test_execution_check_cannot_read_an_uncaptured_helper(release_root: Path, monkeypatch, path: str) -> None:
    original = loader._validate_executing_admission_sources
    def omit_captured_source(capture, executions):
        capture.sources.pop(path)
        return original(capture, executions)
    monkeypatch.setattr(loader, "_validate_executing_admission_sources", omit_captured_source)
    _refuses(release_root, "UNBOUND_SOURCE")


def test_admission_exercises_the_existing_serializer_and_category_owners(release_root: Path, monkeypatch) -> None:
    calls = 0
    original = canon.stable_sercanon.serialize
    def observe(value, *, sort_keys=True):
        nonlocal calls
        calls += 1
        return original(value, sort_keys=sort_keys)
    monkeypatch.setattr(canon.stable_sercanon, "serialize", observe)
    bundle = loader._load_active_mechanics_bundle_from_root(release_root)
    assert calls > 0
    assert loader.FROZEN_MAGIC10_ORDER is category_registry.FROZEN_MAGIC10_ORDER
    assert bundle.registry.magic10_order == category_registry.all_ids()


@pytest.mark.parametrize("outcome", ["success", "malformed_manifest", "member_hash", "manifest_changed"])
def test_packaged_manifest_has_one_physical_open_on_success_and_adverse_paths(
    release_root: Path, monkeypatch, outcome: str,
) -> None:
    manifest_path = release_root / "catalog/manifest.json"
    if outcome == "malformed_manifest":
        manifest_path.write_bytes(b"{invalid\n")
    elif outcome == "member_hash":
        manifest = json.loads(manifest_path.read_bytes())
        manifest["files"][0]["sha256"] = "0" * 64
        write_canonical(manifest_path, manifest)
    original_open = os.open
    original_read = loader._read_captured_file
    manifest_directory = manifest_path.parent.stat()
    opens = 0
    def observe_open(path, flags, *args, **kwargs):
        nonlocal opens
        directory = kwargs.get("dir_fd")
        parent = os.fstat(directory) if directory is not None else None
        if Path(path) == manifest_path or (
            path == manifest_path.name and parent is not None
            and (parent.st_dev, parent.st_ino)
            == (manifest_directory.st_dev, manifest_directory.st_ino)
        ):
            opens += 1
        return original_open(path, flags, *args, **kwargs)
    def change_manifest_after_capture(root, relative):
        result = original_read(root, relative)
        if relative == "catalog/manifest.json":
            manifest_path.write_bytes(b"{}\n")
        return result
    monkeypatch.setattr(os, "open", observe_open)
    if outcome == "manifest_changed":
        monkeypatch.setattr(loader, "_read_captured_file", change_manifest_after_capture)
    if outcome == "success":
        assert isinstance(loader._load_active_mechanics_bundle_from_root(release_root), loader.AdmittedMechanicsBundle)
    else:
        _refuses(release_root, {
            "malformed_manifest": "INVALID_JSON",
            "member_hash": "MANIFEST_MEMBER_HASH_MISMATCH",
            "manifest_changed": "SOURCE_CHANGED",
        }[outcome])
    assert opens == 1
