import json
from pathlib import Path

from engine.categories.registry import FROZEN_MAGIC10_ORDER
from engine.magic10_v2.calculation import BANDS
from tools.config.generate_config_artifacts import expected_config_artifacts


def _read_canonical(path: Path) -> tuple[str, dict]:
    payload = path.read_text(encoding="utf-8")
    obj = json.loads(payload)
    expected = json.dumps(obj, sort_keys=True, separators=(",", ":")) + "\n"
    assert payload == expected
    return payload, obj


def test_magic10_config_snapshot() -> None:
    _, obj = _read_canonical(Path("artifacts/thresholds/magic10_config.json"))
    assert obj["schema"] == "magic10_config.v1"
    assert tuple(obj["order"]) == FROZEN_MAGIC10_ORDER
    caps = obj["caps"]
    assert set(caps) == set(FROZEN_MAGIC10_ORDER)
    for key, entry in caps.items():
        assert entry["inputs"], f"missing inputs for {key}"
        bounds = entry["bounds"]
        assert isinstance(bounds["min"], int) and isinstance(bounds["max"], int)
        assert bounds["min"] <= bounds["max"]
    seeds = obj["seeds"]
    assert set(seeds).issubset(set(FROZEN_MAGIC10_ORDER))
    for seed_key, seed in seeds.items():
        assert seed["template_id"]
        assert seed["seed_version"]
        assert seed["updated_at_utc"]
        assert seed["checksum_sha256"]


def test_band_edges_config() -> None:
    # HDE-EPIC043 WU-PR-10: the cut's version-2 thresholds project to band_edges.v2,
    # one strictly ascending set of inclusive maxima per category, in catalog order.
    _, obj = _read_canonical(Path("artifacts/thresholds/band_edges.json"))
    assert obj["schema"] == "band_edges.v2"
    assert obj["bands"] == list(BANDS)
    assert (obj["source"], obj["version"]) == ("math/thresholds.json", "2")
    assert [entry["category_id"] for entry in obj["categories"]] == list(FROZEN_MAGIC10_ORDER)
    thresholds = json.loads(Path("math/thresholds.json").read_bytes())
    governed = {entry["category_id"]: entry["maxima"] for entry in thresholds["categories"]}
    for entry in obj["categories"]:
        maxima = entry["maxima"]
        assert len(maxima) == len(obj["bands"])
        assert all(earlier < later for earlier, later in zip(maxima, maxima[1:]))
        assert maxima[-1] == 100
        assert maxima == governed[entry["category_id"]]


def test_config_artifact_check_mode_is_read_only() -> None:
    paths = (
        Path("artifacts/registry/registry_report.json"),
        Path("artifacts/thresholds/magic10_config.json"),
        Path("artifacts/thresholds/band_edges.json"),
    )
    before = {path: path.read_bytes() for path in paths}
    first = expected_config_artifacts()
    second = expected_config_artifacts()
    assert first == second
    assert {path: path.read_bytes() for path in paths} == before


import pytest

from tests.config.helpers import catalog_root, closed_rails_env, write_canonical
from tools.config import artifacts as artifact_tools
from tools.config import generate_config_artifacts as config_tools


@pytest.fixture
def writer_root(tmp_path, monkeypatch):
    for name in ("LC_ALL", "LANG", "TZ", "SAFE_MODE", "ALLOW_NETWORK"):
        monkeypatch.setenv(name, closed_rails_env()[name])
    return catalog_root(tmp_path)


def _file_state(root):
    return {path.relative_to(root).as_posix():
            (path.read_bytes(), path.stat().st_mode, path.stat().st_mtime_ns)
            for path in root.rglob("*") if path.is_file() and not path.is_symlink()}


def test_lower_level_threshold_projection_uses_selected_root(writer_root) -> None:
    # This labels a legal lower-level domain fixture, not another mechanics configuration:
    # one category's version-2 maxima change in the selected root only.
    path = writer_root / "math/thresholds.json"
    values = json.loads(path.read_bytes())
    category = values["categories"][0]["category_id"]
    assert values["categories"][0]["maxima"] != [20, 40, 60, 100]
    values["categories"][0]["maxima"] = [20, 40, 60, 100]
    write_canonical(path, values)
    result = artifact_tools.build_band_edges(writer_root)
    assert result["schema"] == "band_edges.v2"
    assert {entry["category_id"]: entry["maxima"] for entry in result["categories"]}[category] == [20, 40, 60, 100]
    assert result["source"] == "math/thresholds.json"
    config_tools.generate_config_artifacts(writer_root)
    assert json.loads((writer_root / "artifacts/thresholds/band_edges.json").read_bytes()) == result


@pytest.mark.parametrize("bad", [True, 24.0, "24", -1])
def test_threshold_writer_does_not_coerce_numeric_types(writer_root, bad) -> None:
    from engine.config.registry_loader import RegistryConfigError

    path = writer_root / "math/thresholds.json"
    values = json.loads(path.read_bytes())
    values["categories"][0]["maxima"][0] = bad
    write_canonical(path, values)
    before = _file_state(writer_root)
    with pytest.raises(RegistryConfigError) as caught:
        config_tools.generate_config_artifacts(writer_root)
    # The owning schema's strict integers refuse each one; nothing is coerced.
    assert caught.value.code == "M10V2_SCHEMA_VALIDATION_FAILED"
    assert _file_state(writer_root) == before


def test_config_source_race_restores_written_outputs(writer_root, monkeypatch) -> None:
    from tools.evidence import update_evidence_index as updater
    from engine.config.registry_loader import RegistryConfigError

    config_tools.generate_config_artifacts(writer_root)
    report = writer_root / "artifacts/registry/registry_report.json"
    prior = json.loads(report.read_bytes())
    prior["notes"] = ["prior writer output"]
    write_canonical(report, prior)
    before = _file_state(writer_root)
    original = updater._publish_staged
    source = writer_root / "math/thresholds.json"
    changed = json.loads(source.read_bytes())
    assert changed["categories"][0]["maxima"] != [20, 40, 60, 100]
    changed["categories"][0]["maxima"] = [20, 40, 60, 100]
    calls = []

    def replace_then_change(payloads):
        original(payloads)
        if not calls:
            assert report.read_bytes() != before["artifacts/registry/registry_report.json"][0]
            calls.append(True)
            write_canonical(source, changed)

    monkeypatch.setattr(updater, "_publish_staged", replace_then_change)
    with pytest.raises(RegistryConfigError, match="changed"):
        config_tools.generate_config_artifacts(writer_root)
    after = _file_state(writer_root)
    for name in before:
        if name != "math/thresholds.json":
            assert after[name] == before[name]
    assert json.loads(source.read_bytes()) == changed
    assert updater._ACTIVE_WRITE_TRANSACTION is None


def test_config_destination_race_refuses_before_overwrite(writer_root, monkeypatch) -> None:
    target = writer_root / "artifacts/registry/registry_report.json"
    original = config_tools._expected_config_artifacts

    def prepare_then_concurrent_edit(capture):
        expected = original(capture)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(b"concurrent user output\n")
        return expected

    monkeypatch.setattr(config_tools, "_expected_config_artifacts", prepare_then_concurrent_edit)
    with pytest.raises(RuntimeError, match="DESTINATION_CHANGED"):
        config_tools.generate_config_artifacts(writer_root)
    assert target.read_bytes() == b"concurrent user output\n"
    assert not (writer_root / "artifacts/thresholds").exists()


def test_config_check_never_repairs_missing_or_stale_outputs(writer_root) -> None:
    config_tools.generate_config_artifacts(writer_root)
    before = _file_state(writer_root)
    config_tools.check_config_artifacts(writer_root)
    assert _file_state(writer_root) == before
    target = writer_root / "artifacts/thresholds/band_edges.json"
    target.unlink()
    before = _file_state(writer_root)
    with pytest.raises(SystemExit, match="STALE"):
        config_tools.check_config_artifacts(writer_root)
    assert _file_state(writer_root) == before


# HDE-EPIC043 WU-PR-10 (HDE-DIST008.2): the catalog logs are rendered only after the
# admitted v2 configuration validates through the v2 loader's rules over the tool's
# own capture (HDE Schemas and Artifacts §8.14.1: fail closed on an absent, invalid,
# ambiguous or hash-mismatched configuration).

def _v2_configuration_inputs(root: Path) -> Path:
    """Copy the governed v2 configuration and the JSON members its rules read into ``root``."""
    import shutil

    from engine.config.magic10_v2_loader import MAGIC10_V2_DECLARED_MEMBERS

    for name in MAGIC10_V2_DECLARED_MEMBERS:
        if name.endswith(".json"):
            target = root / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(config_tools.ROOT / name, target)
    return root


def _manifest_row(root: Path, name: str) -> dict:
    import hashlib

    raw = (root / name).read_bytes()
    return {"path": name, "sha256": hashlib.sha256(raw).hexdigest(), "size": len(raw)}


def _rebind_manifest(root: Path, rows) -> None:
    manifest = json.loads((root / "catalog/manifest.json").read_bytes())
    manifest["files"] = sorted(rows(manifest["files"]), key=lambda row: row["path"])
    write_canonical(root / "catalog/manifest.json", manifest)


def test_catalog_logs_require_actual_initial_candidate_validation(writer_root) -> None:
    from engine.config.magic10_v2_loader import MAGIC10_V2_CONFIGURATION_PATH
    from engine.config.registry_loader import SchemaValidationError

    root = _v2_configuration_inputs(writer_root)
    config_tools.generate_catalog_logs(root)
    paths = [root / name for name in config_tools._CATALOG_LOG_PATHS]
    before = _file_state(root)
    sources = json.loads((root / MAGIC10_V2_CONFIGURATION_PATH).read_bytes())["sources"]
    for path in paths:
        body = path.read_text()
        assert "status: PASS" in body
        assert f"{MAGIC10_V2_CONFIGURATION_PATH} sha256=" in body
        for source in sources.values():
            assert f"source: {source['path']} sha256={source['sha256']} " in body
        assert "magic10_mechanics_v1" not in body
    config_tools.generate_catalog_logs(root, check=True)
    assert _file_state(root) == before
    candidate = root / MAGIC10_V2_CONFIGURATION_PATH
    data = json.loads(candidate.read_bytes())
    data["config_id"] = "unapproved-config"
    write_canonical(candidate, data)
    before = _file_state(root)
    # The manifest row binds the governed bytes, so the edit refuses on its hash first;
    # re-binding the row isolates the pinned v2.0.0 content rule.
    with pytest.raises(SchemaValidationError) as caught:
        config_tools.generate_catalog_logs(root)
    assert caught.value.code == "M10V2_MANIFEST_HASH_MISMATCH"
    assert _file_state(root) == before
    _rebind_manifest(root, lambda rows: [
        _manifest_row(root, MAGIC10_V2_CONFIGURATION_PATH) if row["path"] == MAGIC10_V2_CONFIGURATION_PATH else row
        for row in rows])
    before = _file_state(root)
    for check in (False, True):
        with pytest.raises(SchemaValidationError) as caught:
            config_tools.generate_catalog_logs(root, check=check)
        assert caught.value.code == "M10V2_PINNED_CONTENT_MISMATCH"
    assert _file_state(root) == before


def _v1_only_manifest(root: Path) -> None:
    from engine.config.magic10_v2_loader import MAGIC10_V2_CONFIGURATION_PATH

    _rebind_manifest(root, lambda rows: [
        _manifest_row(config_tools.ROOT, "catalog/magic10_mechanics_v1.json") if row["path"] == MAGIC10_V2_CONFIGURATION_PATH
        else row for row in rows])


def _v1_and_v2_manifest(root: Path) -> None:
    _rebind_manifest(root, lambda rows: [*rows, _manifest_row(config_tools.ROOT, "catalog/magic10_mechanics_v1.json")])


def _absent_configuration(root: Path) -> None:
    from engine.config.magic10_v2_loader import MAGIC10_V2_CONFIGURATION_PATH

    (root / MAGIC10_V2_CONFIGURATION_PATH).unlink()


def _duplicate_key_configuration(root: Path) -> None:
    from engine.config.magic10_v2_loader import MAGIC10_V2_CONFIG_ID, MAGIC10_V2_CONFIGURATION_PATH

    path = root / MAGIC10_V2_CONFIGURATION_PATH
    raw = path.read_bytes()
    assert raw.startswith(b"{")
    path.write_bytes(b'{"config_id":"' + MAGIC10_V2_CONFIG_ID.encode() + b'",' + raw[1:])


@pytest.mark.parametrize(("change", "code"), [
    (_absent_configuration, "MISSING_FILE"),
    (_v1_only_manifest, "M10V2_CONFIGURATION_ROW_MISSING"),
    (_v1_and_v2_manifest, "M10V2_MULTIPLE_CONFIGURATIONS"),
    (_duplicate_key_configuration, "DUPLICATE_JSON_KEY"),
], ids=["absent", "v1_only", "v1_and_v2", "duplicate_key"])
def test_catalog_logs_refuse_an_absent_unbound_ambiguous_or_duplicate_keyed_v2_configuration(
    writer_root, change, code
) -> None:
    from engine.config.registry_loader import SchemaValidationError

    root = _v2_configuration_inputs(writer_root)
    change(root)
    before = _file_state(root)
    for check in (False, True):
        with pytest.raises(SchemaValidationError) as caught:
            config_tools.generate_catalog_logs(root, check=check)
        assert caught.value.code == code
    assert _file_state(root) == before
    assert not any((root / name).exists() for name in config_tools._CATALOG_LOG_PATHS)


def test_config_publication_refuses_another_root(writer_root) -> None:
    before = _file_state(writer_root)
    with pytest.raises(RuntimeError, match="ROOT_MISMATCH"):
        config_tools.publish_config_family(writer_root)
    assert _file_state(writer_root) == before


# --- HDE-EPIC040-PR06: publication is gated on real admission and the same capture -------

def _repo_status() -> str:
    import subprocess
    return subprocess.run(["git", "status", "--porcelain", "--untracked-files=all"],
                          cwd=config_tools.ROOT, capture_output=True, text=True, check=True).stdout


def test_publish_family_refuses_without_admission(writer_root, monkeypatch) -> None:
    from engine.config.registry_loader import SchemaValidationError

    def refuse():
        raise SchemaValidationError("INCOMPLETE_RELEASE_ROSTER", "patched provider")

    monkeypatch.delenv("HDE_ISOLATED_RELEASE_BUILD", raising=False)
    monkeypatch.setattr(config_tools, "load_active_mechanics_bundle", refuse)
    before = _repo_status()
    with pytest.raises(RuntimeError, match="^CONFIG_PUBLICATION_RELEASE_NOT_ADMITTED:INCOMPLETE_RELEASE_ROSTER$"):
        config_tools.publish_config_family(config_tools.ROOT)
    assert _repo_status() == before
    # --check on the real root keeps its local semantics while the owner does not admit.
    config_tools.check_config_artifacts(config_tools.ROOT)


def test_publish_family_refuses_capture_mismatch(writer_root, monkeypatch) -> None:
    import dataclasses
    from engine.config.registry_loader import load_active_mechanics_bundle

    admitted = load_active_mechanics_bundle()
    monkeypatch.delenv("HDE_ISOLATED_RELEASE_BUILD", raising=False)
    monkeypatch.setattr(config_tools, "load_active_mechanics_bundle",
                        lambda: dataclasses.replace(admitted, config_sha256="0" * 64))
    before = _repo_status()
    with pytest.raises(RuntimeError, match="^CONFIG_PUBLICATION_CAPTURE_MISMATCH$"):
        config_tools.publish_config_family(config_tools.ROOT)
    assert _repo_status() == before
    # --check produces the three primaries from the registry capture, which reads no
    # mechanics configuration, so only the captured member identities bind it.
    config_tools.check_config_artifacts(config_tools.ROOT)
    altered = dataclasses.replace(admitted, source_identities=tuple(
        dataclasses.replace(identity, sha256="0" * 64) if identity.path == "catalog/gates_v1.json" else identity
        for identity in admitted.source_identities))
    monkeypatch.setattr(config_tools, "load_active_mechanics_bundle", lambda: altered)
    with pytest.raises(RuntimeError, match="^CONFIG_PUBLICATION_CAPTURE_MISMATCH$"):
        config_tools.publish_config_family(config_tools.ROOT)
    with pytest.raises(RuntimeError, match="^CONFIG_PUBLICATION_CAPTURE_MISMATCH$"):
        config_tools.check_config_artifacts(config_tools.ROOT)
    assert _repo_status() == before


def test_real_root_check_requires_the_admitted_capture() -> None:
    """On the admitted real root --check asserts the same-capture equality and passes."""
    config_tools.check_config_artifacts(config_tools.ROOT)


def test_generate_and_check_keep_working_on_partial_roots(writer_root) -> None:
    """Local generation and --check on a partial root never consult admission."""
    config_tools.generate_config_artifacts(writer_root)
    config_tools.check_config_artifacts(writer_root)
    for name in config_tools._CONFIG_PATHS:
        assert (writer_root / name).is_file()


def test_config_output_symlink_ancestor_refuses(writer_root, tmp_path_factory) -> None:
    outside = tmp_path_factory.mktemp("outside-config")
    (writer_root / "artifacts").symlink_to(outside, target_is_directory=True)
    with pytest.raises(RuntimeError, match="SYMLINK"):
        config_tools.generate_config_artifacts(writer_root)
    assert list(outside.iterdir()) == []


@pytest.mark.parametrize("changed_kind", ["source", "destination"])
def test_config_check_rechecks_sources_and_outputs_after_comparison(writer_root, monkeypatch, changed_kind) -> None:
    from engine.config.registry_loader import RegistryConfigError

    config_tools.generate_config_artifacts(writer_root)
    before = _file_state(writer_root)
    target = writer_root / ("math/thresholds.json" if changed_kind == "source"
                            else "artifacts/thresholds/band_edges.json")
    original = config_tools._check_expected
    changed = []

    def compare_then_concurrent_change(base, expected):
        state = original(base, expected)
        # Both the version-2 thresholds and band_edges.v2 carry per-category maxima.
        values = json.loads(target.read_bytes())
        assert values["categories"][0]["maxima"] != [20, 40, 60, 100]
        values["categories"][0]["maxima"] = [20, 40, 60, 100]
        write_canonical(target, values)
        changed.append(target.read_bytes())
        return state

    monkeypatch.setattr(config_tools, "_check_expected", compare_then_concurrent_change)
    error = RegistryConfigError if changed_kind == "source" else RuntimeError
    with pytest.raises(error, match="changed|CHANGED"):
        config_tools.check_config_artifacts(writer_root)
    assert target.read_bytes() == changed[0]
    after = _file_state(writer_root)
    for name, state in before.items():
        if name != target.relative_to(writer_root).as_posix():
            assert after[name] == state


def _complete_manifest_cut_fixture(writer_root):
    seeds_path = writer_root / "catalog/magic10_seeds.json"
    seeds = json.loads(seeds_path.read_bytes())
    seeds[next(iter(seeds))]["seed_version"] = "receipt-fixture"
    write_canonical(seeds_path, seeds)
    manifest = writer_root / "catalog/manifest.json"
    metadata = json.loads(manifest.read_bytes())
    source_root = Path(__file__).resolve().parents[2]
    for entry in metadata["files"]:
        member = writer_root / entry["path"]
        if not member.exists():
            member.parent.mkdir(parents=True, exist_ok=True)
            member.write_bytes((source_root / entry["path"]).read_bytes())
    return manifest, metadata


@pytest.mark.parametrize("interference", [None, "same_bytes_replacement", "mode"])
def test_manifest_cut_callback_attributes_only_actual_owner_write(writer_root, monkeypatch, interference) -> None:
    import os
    from scripts import cut_release_manifest
    from tools.evidence import update_evidence_index as updater

    manifest, metadata = _complete_manifest_cut_fixture(writer_root)
    prior = artifact_tools._destination_state(writer_root, [manifest])[manifest]
    observed = []
    error = "injected after manifest receipt" if interference is None else "ROLLBACK_FAILED"

    original_record = updater._record_transaction_write

    def intervene_before_receipt(path, **kwargs):
        if path == manifest and interference is not None and not observed:
            if interference == "same_bytes_replacement":
                replacement = manifest.with_suffix(".replacement")
                replacement.write_bytes(manifest.read_bytes())
                replacement.chmod(manifest.stat().st_mode)
                os.utime(replacement, ns=(manifest.stat().st_atime_ns, manifest.stat().st_mtime_ns))
                os.replace(replacement, manifest)
            else:
                manifest.chmod(0o600)
            observed.append(artifact_tools._destination_state(writer_root, [manifest])[manifest])
        return original_record(path, **kwargs)

    monkeypatch.setattr(updater, "_record_transaction_write", intervene_before_receipt)

    def publish(path, content):
        assert path == manifest and content != prior[0]
        updater._publish_staged({path: content})

    with pytest.raises(RuntimeError, match=error) as caught:
        with updater._ConfigWriteTransaction(writer_root, allowed_paths={manifest}) as transaction:
            transaction.prepare((manifest,))
            assert cut_release_manifest.cut_manifest(manifest, version=metadata["version"],
                built_at_utc=metadata["built_at_utc"], _publish=publish) == 0
            raise RuntimeError("injected after manifest receipt")

    current = artifact_tools._destination_state(writer_root, [manifest])[manifest]
    if interference is None:
        assert (current[0], current[3], current[5]) == (prior[0], prior[3], prior[5])
    else:
        assert "POSTIMAGE" in str(caught.value.__cause__)
        assert current == observed[0]
        assert any("CONFLICT_PRESERVED" in note for note in caught.value.__notes__)
    assert updater._ACTIVE_WRITE_TRANSACTION is None


@pytest.mark.parametrize("failure", ["partial-temp-write", "fsync", "after-replace"])
def test_manifest_cut_callback_recovers_actual_publication_failure(writer_root, monkeypatch, failure) -> None:
    from scripts import cut_release_manifest
    from tools.evidence import update_evidence_index as updater

    manifest, metadata = _complete_manifest_cut_fixture(writer_root)
    before = _file_state(writer_root)
    injected = OSError(f"injected manifest {failure}")
    attempts = []
    original_fdopen = updater.os.fdopen
    original_fsync = updater.os.fsync
    original_record = updater._record_transaction_write

    class PartialWrite:
        def __init__(self, handle):
            self.handle = handle

        def __enter__(self):
            self.handle.__enter__()
            return self

        def __exit__(self, *args):
            return self.handle.__exit__(*args)

        def write(self, content):
            self.handle.write(content[:17])
            self.handle.flush()
            attempts.append("partial")
            assert manifest.read_bytes() == before["catalog/manifest.json"][0]
            raise injected

    def partial_fdopen(descriptor, mode, *args, **kwargs):
        handle = original_fdopen(descriptor, mode, *args, **kwargs)
        return PartialWrite(handle) if mode == "wb" and not attempts else handle

    def failed_fsync(descriptor):
        if not attempts:
            attempts.append("fsync")
            assert manifest.read_bytes() == before["catalog/manifest.json"][0]
            raise injected
        return original_fsync(descriptor)

    def failed_after_replace(path, **kwargs):
        original_record(path, **kwargs)
        if path == manifest and not attempts:
            assert manifest.read_bytes() != before["catalog/manifest.json"][0]
            attempts.append("replaced")
            raise injected

    if failure == "partial-temp-write":
        monkeypatch.setattr(updater.os, "fdopen", partial_fdopen)
    elif failure == "fsync":
        monkeypatch.setattr(updater.os, "fsync", failed_fsync)
    else:
        monkeypatch.setattr(updater, "_record_transaction_write", failed_after_replace)

    def publish(path, content):
        assert path == manifest and content != before["catalog/manifest.json"][0]
        updater._publish_staged({path: content})

    with pytest.raises(OSError, match=failure) as caught:
        with updater._ConfigWriteTransaction(writer_root, allowed_paths={manifest}) as transaction:
            transaction.prepare((manifest,))
            cut_release_manifest.cut_manifest(manifest, version=metadata["version"],
                built_at_utc=metadata["built_at_utc"], _publish=publish)
    assert caught.value is injected
    assert attempts
    assert _file_state(writer_root) == before
    assert updater._ACTIVE_WRITE_TRANSACTION is None


# ---------------------------------------------------------------------------
# HDE-EPIC040-PR05: the PF01 §9.5 golden collection and its read-only
# comparator.  Since HDE-EPIC043 WU-PR-09 the comparator reads the Magic10 v2
# collection (tests/fixtures/magic10/v2/goldens.json) and every positive run
# admits a labelled synthetic v2 candidate root from an isolated copy through
# the test-only roster route in tests/config/helpers.py.  Since WU-PR-10 the
# collection holds M10-G001 to M10-G008, computed at the cut, and every positive
# run's candidate carries the governed cut bytes (``fixture_maxima=False``), never
# the labelled fixture maxima.  Nothing here relaxes admission or touches the
# repository tree.  These tests live in the config
# tooling's registered owner module so a change to ``tools/config/artifacts.py``
# or ``generate_config_artifacts.py`` always runs them.
# ---------------------------------------------------------------------------

import ast
import contextlib
import copy
import errno
import hashlib
import os
import resource
import signal
import stat
import subprocess
import sys

from ci.checks import classify_ci_changes as classifier
from engine.compat import compute
from engine.config.registry_loader import AliasPolicyError, UnknownIdError, _load_active_mechanics_bundle_from_root
from engine.magic10_v2.calculation import assign_band
from engine.narratives import loader as narrative_loader
from engine.narratives import router as narrative_router
from engine.narratives import state as narrative_state
from engine.serializer.canon import sercanon
from tests.config.helpers import (
    synthetic_v2_candidate_root,
    v2_candidate_roster,
    v2_candidate_roster_admission,
    write_release_manifest,
)
from tools.evidence import update_evidence_index as updater

ROOT = Path(__file__).resolve().parents[2]
GOLDENS = ROOT / "tests/fixtures/magic10/v2/goldens.json"
CLOSED_RAILS = {"LC_ALL": "C", "LANG": "C", "TZ": "UTC", "SAFE_MODE": "1", "ALLOW_NETWORK": "0"}
# PF01 §9.5 (Magic10 v2): M10-G001, no Channel and two Reflectors, is fixed by canon: every
# category scores 0, band Cool.  M10-G002 to M10-G008 were computed at the cut (WU-PR-10).
G001_CATEGORIES = [{"category_id": category, "score": 0, "band": "Cool"} for category in FROZEN_MAGIC10_ORDER]
FORBIDDEN_NAMES = {
    "write_magic10_config", "write_band_edges", "_publish_prepared", "generate_config_artifacts",
    "publish_config_family", "generate_catalog_logs", "check_config_artifacts", "_ConfigWriteTransaction",
    "update_evidence_index", "_publish_staged", "cut_release_manifest", "_BUNDLE_PROVIDER", "_PACK",
    "route_keys", "get_pack", "load_pack",
}


@pytest.fixture(scope="module")
def _candidate_root(tmp_path_factory) -> Path:
    return synthetic_v2_candidate_root(tmp_path_factory.mktemp("pr05-goldens"), fixture_maxima=False)


@pytest.fixture
def v2_roster():
    """The test-only v2 candidate roster route (tests/config/helpers.py), for one test only."""
    with v2_candidate_roster_admission() as roster:
        yield roster


@pytest.fixture
def bundle_root(_candidate_root, v2_roster) -> Path:
    """The v2 candidate root; it admits only under the roster route this test holds."""
    return _candidate_root


@pytest.fixture(scope="module")
def bundle(_candidate_root):
    with v2_candidate_roster_admission():
        return _load_active_mechanics_bundle_from_root(_candidate_root)


@pytest.fixture(autouse=True)
def _closed_rails(monkeypatch):
    for key, value in CLOSED_RAILS.items():
        monkeypatch.setenv(key, value)


def _document() -> dict:
    return json.loads(GOLDENS.read_bytes())


def _write_document(path: Path, document: dict) -> Path:
    write_canonical(path, document)
    return path


def _case(document: dict, case_id: str) -> dict:
    return next(case for case in document["cases"] if case["case_id"] == case_id)


def _snapshot(root: Path) -> dict[str, str]:
    files = sorted(p for p in root.rglob("*") if p.is_file())
    return {p.relative_to(root).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}


def _git_status() -> str:
    return subprocess.run(["git", "status", "--porcelain", "--untracked-files=all"], cwd=ROOT,
                          capture_output=True, text=True, check=True).stdout


# --- fixture bytes and PF01 agreement ---------------------------------------------------

def test_fixture_bytes_are_canonical_and_agree_with_pf01() -> None:
    raw = GOLDENS.read_bytes()
    document = json.loads(raw)
    assert sercanon(document, sort_keys=True) == raw
    assert raw.endswith(b"\n") and not raw.endswith(b"\n\n") and b"\r" not in raw and not raw.startswith(b"\xef\xbb\xbf")
    assert GOLDENS == artifact_tools.GOLDENS_DEFAULT_PATH
    assert document["schema"] == artifact_tools.GOLDENS_SCHEMA == "magic10_goldens.v2"
    # PF01 §9.5 v2: the canon set is M10-G001 to M10-G008, in order, each with its kind (D-5, D-6).
    assert artifact_tools.GOLDEN_CASE_TABLE == (
        ("M10-G001", "calculation", "category_vector"),
        ("M10-G002", "calculation", "core"),
        ("M10-G003", "calculation", "signal_operation"),
        ("M10-G004", "calculation", "core"),
        ("M10-G005", "application", "identity_independence"),
        ("M10-G006", "calculation", "band_boundary"),
        ("M10-G007", "application", "self_pair"),
        ("M10-G008", "application", "equal_mask_pair"),
    )
    assert artifact_tools.GOLDEN_CASE_IDS == tuple(f"M10-G00{number}" for number in range(1, 9))
    assert [(case["case_id"], case["case_type"], case["kind"]) for case in document["cases"]] == list(
        artifact_tools.GOLDEN_CASE_TABLE)
    constants = document["constants"]
    assert set(constants) == {"config_id", "release_id", "router_stub", "synthetic_projection_fields"}
    assert (constants["config_id"], constants["release_id"]) == ("m10-relevance-centers-type-v2.0.0", "a" * 64)
    # PF01 §9.5 (M10-G008): the router stub values.
    assert constants["router_stub"] == {"personal_lo_to_hi": "m10.test.personal.lo_to_hi",
                                        "personal_hi_to_lo": "m10.test.personal.hi_to_lo",
                                        "shared": "m10.test.shared.equal_mask"}
    g001 = _case(document, "M10-G001")
    assert g001["inputs"] == {"gates_a": [1], "gates_b": [2]}
    assert g001["expected"] == {"categories": G001_CATEGORIES}
    # PF01 §9.5: the M10-G004 Gate sets and their Channel states (the five-state rule is unchanged in v2).
    g004 = _case(document, "M10-G004")
    assert g004["inputs"] == {"gates_a": [5, 19, 20, 34, 43, 49], "gates_b": [9, 12, 15, 22, 23, 52]}
    assert {row["channel_id"]: (row["state"], row["owner"]) for row in g004["expected"]["channel_states"]
            if row["state"] != "none"} == {
        "05-15": ("electromagnetic", None), "09-52": ("dominance", "member_hi"), "12-22": ("dominance", "member_hi"),
        "19-49": ("dominance", "member_lo"), "20-34": ("dominance", "member_lo"), "23-43": ("electromagnetic", None)}
    assert len(g004["expected"]["channel_states"]) == 36
    # PF01 §9.5: the M10-G007 and M10-G008 inputs, and their values that no configuration or maxima reach.
    uuid_1, uuid_2 = "00000000-0000-0000-0000-000000000001", "00000000-0000-0000-0000-000000000002"
    meta = {"engine_tag": "m10-test", "invocation_tag": "m10-identity-boundary"}
    g007, g008 = _case(document, "M10-G007"), _case(document, "M10-G008")
    assert g007["inputs"]["a"] == g007["inputs"]["b"] == {"gates": [1], "person_uid": uuid_1}
    assert (g007["inputs"]["meta"], g007["inputs"]["release_id"]) == (meta, "a" * 64)
    assert g007["expected"]["reader"] == {
        "categories": [], "eligible": False,
        "idempotence_hash": "8214324eb0129ff1dc213a5d53bd9d7b3758a351032c5258f7ba28eace7adc15"}
    assert (g008["inputs"]["a"], g008["inputs"]["b"]) == ({"gates": [1], "person_uid": uuid_1}, {"gates": [1], "person_uid": uuid_2})
    assert (g008["inputs"]["meta"], g008["inputs"]["release_id"]) == (meta, "a" * 64)
    assert {row["chart_fingerprint"] for row in g008["expected"]["members"]} == {
        "7567338a3be5b35e00366bfe86f3f1ca8b89be1fd02be893abeb62a60dbc2d2b"}
    assert g008["expected"]["orientation"] == {"lo": uuid_1, "hi": uuid_2}
    assert g008["expected"]["reader"]["categories"] == [{"id": "harmony", "band": "Cool"}]
    assert g008["expected"]["reader"]["idempotence_hash"] == "ae435ccc1f9d2043b4ee825f48c54ea421276d49d159b19271e46b24c04f2f6e"
    assert g008["expected"]["reader_v2"]["categories"] == [{"id": category, "band": "Cool"} for category in FROZEN_MAGIC10_ORDER]
    assert {(row["score"], row["band"]) for row in g008["expected"]["categories"]} == {(0, "Cool")}
    # The v1 pair key was under m10-channel-state-v1.0.0; the v2 preimage includes the v2 config_id.
    assert g008["expected"]["pair_key_under_release"]["config_id"] == "m10-relevance-centers-type-v2.0.0"
    assert g008["expected"]["pair_key_under_release"]["pair_key"] != "8a75eafcc4af664e073c1c4daec55f073f416af2c461039539f01717ac01d501"
    for case in document["cases"]:
        provenance = case["input_provenance"]
        assert provenance and len(set(provenance)) == len(provenance) and all(isinstance(tag, str) and tag for tag in provenance)
        assert case["realizable_chart_claim"] in (True, False, None)


# --- positive comparison ----------------------------------------------------------------

def test_a_collection_for_another_configuration_never_matches(bundle_root, bundle, tmp_path) -> None:
    """HDE-EPIC043 WU-PR-09: the document's ``constants.config_id`` must be the candidate's."""
    document = _document()
    document["constants"]["config_id"] = "m10-channel-state-v1.0.0"
    result = artifact_tools.compare_goldens(bundle_root, _write_document(tmp_path / "v1_identity.json", document))
    assert result.ok is False
    assert [(row.case_id, row.path, row.expected, row.actual) for row in result.mismatches] == [
        ("constants", "constants.config_id", "m10-channel-state-v1.0.0", bundle.mechanics["config_id"])]
    assert [row.outcome for row in result.cases] == ["match"] * len(artifact_tools.GOLDEN_CASE_IDS)


def test_positive_comparison_matches_every_case(bundle_root, bundle) -> None:
    result = artifact_tools.compare_goldens(bundle_root, GOLDENS)
    assert result.ok is True and result.mismatches == ()
    assert [(row.case_id, row.outcome) for row in result.cases] == [(case["case_id"], "match") for case in _document()["cases"]]
    assert result.candidate_release_id == bundle.release_id and result.config_id == "m10-relevance-centers-type-v2.0.0"
    assert result.config_id == bundle.mechanics["config_id"]
    assert result.goldens_sha256 == hashlib.sha256(GOLDENS.read_bytes()).hexdigest()
    observed = {row.case_id: row.observed for row in result.cases}
    assert observed["M10-G001"] == {"categories": G001_CATEGORIES}
    # Each band is the admitted candidate's own band for its score, never a literal rule.
    for case_id in ("M10-G001", "M10-G002", "M10-G004"):
        for row in observed[case_id]["categories"]:
            assert row["band"] == assign_band(row["score"], bundle.magic10_v2.maxima[row["category_id"]])
    # The boundary matrix is banded at the cut maxima: the governed thresholds, which the candidate carries.
    cut = {row["category_id"]: row["maxima"] for row in json.loads((ROOT / "math/thresholds.json").read_bytes())["categories"]}
    assert {row["category_id"]: row["maxima"] for row in observed["M10-G006"]["categories"]} == cut
    for row in result.cases:
        assert sercanon(row.observed) == sercanon(row.expected)


def test_a_candidate_at_the_fixture_maxima_never_matches_the_cut_goldens(tmp_path, v2_roster) -> None:
    """The cut's values belong to the cut maxima: the labelled fixture maxima mismatch every banded case."""
    fixture_root = synthetic_v2_candidate_root(tmp_path / "fixture-maxima")
    result = artifact_tools.compare_goldens(fixture_root, GOLDENS)
    assert result.ok is False
    assert [row.case_id for row in result.cases if row.outcome == "mismatch"] == ["M10-G002", "M10-G004", "M10-G005", "M10-G006"]
    assert ("M10-G006", "expected.categories[0].maxima[0]") in {(row.case_id, row.path) for row in result.mismatches}


# --- every mismatch is reported ---------------------------------------------------------

def _alter(document: dict, case_id: str, mutate) -> None:
    mutate(_case(document, case_id))


ALTERATIONS = {
    "g001_score": ("M10-G001", lambda case: case["expected"]["categories"][0].__setitem__("score", 1),
                   {"expected.categories[0].score"}),
    "g001_band": ("M10-G001", lambda case: case["expected"]["categories"][3].__setitem__("band", "Open"),
                  {"expected.categories[3].band"}),
    "g001_category_order": ("M10-G001", lambda case: case["expected"]["categories"].__setitem__(slice(0, 2), case["expected"]["categories"][0:2][::-1]),
                            {"expected.categories[0].category_id", "expected.categories[1].category_id"}),
    "g001_category_dropped": ("M10-G001", lambda case: case["expected"]["categories"].pop(),
                              {"expected.categories.length"}),
    # HDE-EPIC043 WU-PR-10: one perturbed expected value per runner kind.
    "g002_signal": ("M10-G002", lambda case: case["expected"]["signals"][0].__setitem__("q", case["expected"]["signals"][0]["q"] + 1),
                    {"expected.signals[0].q"}),
    "g003_swapped_q": ("M10-G003", lambda case: case["expected"]["scenarios"][0].__setitem__("q_owners_swapped", 999),
                       {"expected.scenarios[0].q_owners_swapped"}),
    "g004_band": ("M10-G004", lambda case: case["expected"]["categories"][0].__setitem__("band", "Cool"),
                  {"expected.categories[0].band"}),
    "g004_owner": ("M10-G004", lambda case: case["expected"]["channel_states"][7].__setitem__("owner", "member_lo"),
                   {"expected.channel_states[7].owner"}),
    "g005_pair_key_equality": ("M10-G005", lambda case: case["expected"].__setitem__("pair_key_equal_across_pairs", False),
                               {"expected.pair_key_equal_across_pairs"}),
    "g006_band": ("M10-G006", lambda case: case["expected"]["categories"][0]["results"][1].__setitem__("band", "Cool"),
                  {"expected.categories[0].results[1].band"}),
    "g007_reader_hash": ("M10-G007", lambda case: case["expected"]["reader"].__setitem__("idempotence_hash", "0" * 64),
                         {"expected.reader.idempotence_hash"}),
    "g008_pair_key": ("M10-G008", lambda case: case["expected"]["pair_key_under_release"].__setitem__("pair_key", "0" * 64),
                      {"expected.pair_key_under_release.pair_key"}),
    "g008_reader_v2_band": ("M10-G008", lambda case: case["expected"]["reader_v2"]["categories"][9].__setitem__("band", "Open"),
                            {"expected.reader_v2.categories[9].band"}),
}


@pytest.mark.parametrize("name", sorted(ALTERATIONS))
def test_each_alteration_yields_exactly_its_mismatches(bundle_root, tmp_path, name) -> None:
    case_id, mutate, paths = ALTERATIONS[name]
    document = _document()
    _alter(document, case_id, mutate)
    result = artifact_tools.compare_goldens(bundle_root, _write_document(tmp_path / f"{name}.json", document))
    assert result.ok is False
    assert {(row.case_id, row.path) for row in result.mismatches} == {(case_id, path) for path in paths}
    assert [row.outcome for row in result.cases if row.case_id == case_id] == ["mismatch"]
    assert all(row.outcome == "match" for row in result.cases if row.case_id != case_id)


def test_several_alterations_are_all_reported_in_sorted_order(bundle_root, tmp_path) -> None:
    document = _document()
    expected_paths = set()
    for name in ("g001_score", "g001_band", "g001_category_dropped"):
        case_id, mutate, paths = ALTERATIONS[name]
        _alter(document, case_id, mutate)
        expected_paths |= {(case_id, path) for path in paths}
    result = artifact_tools.compare_goldens(bundle_root, _write_document(tmp_path / "multi.json", document))
    reported = [(row.case_id, row.path) for row in result.mismatches]
    assert set(reported) == expected_paths and reported == sorted(reported)
    assert result.ok is False and len(result.mismatches) == len(expected_paths)
    report = json.loads(artifact_tools.render_golden_report(result))
    assert len(report["mismatches"]) == len(expected_paths) and report["ok"] is False


def test_added_or_missing_expected_keys_are_mismatches(bundle_root, tmp_path) -> None:
    document = _document()
    case = _case(document, "M10-G001")
    case["expected"]["extra"] = 1
    del case["expected"]["categories"]
    result = artifact_tools.compare_goldens(bundle_root, _write_document(tmp_path / "keys.json", document))
    assert {(row.path, row.expected, row.actual if row.path.endswith("extra") else "<observed>") for row in result.mismatches} == {
        ("expected.extra", 1, "<absent>"), ("expected.categories", "<absent>", "<observed>")}


def _failing_core(*args, **kwargs):
    raise ValueError("core refused")


_ANY = object()  # a mismatch value this table does not restate


def _swap_first_categories(case):
    case["inputs"]["categories"][0:2] = case["inputs"]["categories"][0:2][::-1]


# A gate list the core's members cannot be built from is reported at its input path; a core
# that raises is the case's execution mismatch; every other runner input a case cannot run
# as stated is reported at its path.  None aborts the comparison.  A core that raises fails
# each case that calls it directly; the application cases reach the core through
# ``evaluate_pair``'s own binding, which this replacement does not touch.
_CORE_REFUSED = ("execution", "completed", "ValueError: core refused")
UNRUNNABLE = {
    "g001_invalid_gate": ("M10-G001", lambda case: case["inputs"].__setitem__("gates_a", [0]), None,
                          [("M10-G001", "inputs.gates_a", "normalized Gate list", "GATE_VALUE_INVALID")]),
    "g001_duplicate_gate": ("M10-G001", lambda case: case["inputs"].__setitem__("gates_b", [2, 2]), None,
                            [("M10-G001", "inputs.gates_b", "normalized Gate list", "GATE_DUPLICATE")]),
    "g001_no_gates": ("M10-G001", lambda case: case["inputs"].__setitem__("gates_a", []), None,
                      [("M10-G001", "inputs.gates_a", "normalized Gate list", "GATES_EMPTY")]),
    "core_raises": ("M10-G001", lambda case: None, _failing_core,
                    [(case_id, *_CORE_REFUSED) for case_id in ("M10-G001", "M10-G002", "M10-G004")]),
    "g004_out_of_range_gate": ("M10-G004", lambda case: case["inputs"].__setitem__("gates_b", [65]), None,
                               [("M10-G004", "inputs.gates_b", "normalized Gate list", "GATE_VALUE_INVALID")]),
    "g003_roster_dropped": ("M10-G003", lambda case: case["inputs"]["channels"].pop(), None,
                            [("M10-G003", "inputs.definition", _ANY, _ANY)]),
    "g003_operation_renamed": ("M10-G003", lambda case: case["inputs"].__setitem__("operation", "twice_min_owner_mass_v1"), None,
                               [("M10-G003", "inputs.definition", _ANY, _ANY)]),
    "g003_unknown_signal": ("M10-G003", lambda case: case["inputs"].__setitem__("signal_id", "unknown_signal"), None,
                            [("M10-G003", "inputs.signal_id", _ANY, "unknown_signal")]),
    "g003_state_not_owned": ("M10-G003", lambda case: case["inputs"].__setitem__("state", "companionship"), None,
                             [("M10-G003", "inputs.state", ["compromise", "dominance"], "companionship")]),
    "g003_unknown_owner": ("M10-G003", lambda case: case["inputs"]["scenarios"][0]["owned"][0].__setitem__("owner", "member_x"), None,
                           [("M10-G003", "inputs.scenarios[0].owned[0].owner", ["member_hi", "member_lo"], "member_x")]),
    "g003_repeated_channel": ("M10-G003", lambda case: case["inputs"]["scenarios"][0]["owned"][1].__setitem__("channel_id", "02-14"), None,
                              [("M10-G003", "inputs.scenarios[0].owned[1].channel_id", "a distinct roster Channel", "02-14")]),
    "g006_category_order": ("M10-G006", _swap_first_categories, None,
                            [("M10-G006", "inputs.categories.category_ids", list(FROZEN_MAGIC10_ORDER),
                              [FROZEN_MAGIC10_ORDER[1], FROZEN_MAGIC10_ORDER[0], *FROZEN_MAGIC10_ORDER[2:]])]),
    "g006_score_out_of_range": ("M10-G006", lambda case: case["inputs"]["categories"][0]["scores"].__setitem__(0, 101), None,
                                [("M10-G006", "inputs.categories[0].scores", "non-empty list of integer scores 0..100", _ANY)]),
    "g005_pair_label": ("M10-G005", lambda case: case["inputs"]["pairs"][0].__setitem__("pair_id", "pair_9"), None,
                        [("M10-G005", "inputs.pairs.pair_id", ["pair_1", "pair_2"], ["pair_9", "pair_2"])]),
    "g007_adverse_party": ("M10-G007", lambda case: case["inputs"]["adverse"][0].__setitem__("party", "c"), None,
                           [("M10-G007", "inputs.adverse[0].party", ["a", "b"], "c")]),
    "g008_invalid_identity": ("M10-G008", lambda case: case["inputs"]["a"].__setitem__("person_uid", "not-a-uuid"), None,
                              [("M10-G008", "execution", "completed", _ANY)]),
}


@pytest.mark.parametrize("name", sorted(UNRUNNABLE))
def test_a_case_that_cannot_execute_is_its_own_mismatch_never_a_crash(bundle_root, tmp_path, capfdbinary, monkeypatch, name) -> None:
    from engine.core import core as engine_core

    case_id, mutate, core, rows = UNRUNNABLE[name]
    if core is not None:
        monkeypatch.setattr(engine_core, "compute_core", core)
    document = _document()
    _alter(document, case_id, mutate)
    goldens = _write_document(tmp_path / f"{name}.json", document)
    result = artifact_tools.compare_goldens(bundle_root, goldens)
    assert result.ok is False
    observed = [(row.case_id, row.path, row.expected, row.actual) for row in result.mismatches]
    assert [(row[0], row[1]) for row in observed] == [(row[0], row[1]) for row in rows]
    for got, want in zip(observed, rows):
        assert all(value is _ANY or value == actual for value, actual in zip(want[2:], got[2:])), got
    assert [row.case_id for row in result.cases if row.outcome == "mismatch"] == sorted({row[0] for row in rows})
    code, out, err = _run_cli(["--compare-goldens", str(bundle_root), "--goldens", str(goldens)], capfdbinary)
    assert (code, out, err) == (config_tools.GOLDEN_COMPARISON_MISMATCH_EXIT_CODE, b"",
                                f"GOLDEN_COMPARISON_MISMATCH:{len(rows)}\n".encode())


def _order_dependent_core(monkeypatch):
    import dataclasses
    from engine.core import core as engine_core

    real = engine_core.compute_core

    def order_dependent(member_a, member_b, bundle, release_id):
        result = real(member_a, member_b, bundle, release_id)
        return dataclasses.replace(result, pair_key="0" * 64) if member_a.mask > member_b.mask else result

    monkeypatch.setattr(engine_core, "compute_core", order_dependent)


def _order_dependent_evaluation(monkeypatch):
    real = compute.evaluate_pair

    def order_dependent(a, b, **seams):
        result = real(a, b, **seams)
        reversed_request = (a.gates.mask, a.canonical_person_id) > (b.gates.mask, b.canonical_person_id)
        return {**result, "pair_key": "0" * 64} if reversed_request and "pair_key" in result else result

    monkeypatch.setattr(compute, "evaluate_pair", order_dependent)


# PF01 §9.5 v2: every case is checked in both pair orders.  A result that depends on member
# order is each affected case's ``pair_order`` mismatch: the Gate-level cases through the core,
# the application cases through ``evaluate_pair``.  M10-G002 has equal masks and M10-G007 is a
# self-pair, so their reversal is vacuous; M10-G003 and M10-G006 have no member order.
@pytest.mark.parametrize(("inject", "cases"), [
    (_order_dependent_core, ("M10-G001", "M10-G004")),
    (_order_dependent_evaluation, ("M10-G005", "M10-G008")),
], ids=["core", "evaluate_pair"])
def test_an_order_dependent_result_is_each_cases_pair_order_mismatch(bundle_root, monkeypatch, inject, cases) -> None:
    inject(monkeypatch)
    result = artifact_tools.compare_goldens(bundle_root, GOLDENS)
    assert result.ok is False
    assert [(row.case_id, row.path) for row in result.mismatches] == [(case_id, "pair_order") for case_id in cases]
    assert [row.case_id for row in result.cases if row.outcome == "mismatch"] == list(cases)


def _setter(*path, value):
    def mutate(case):
        target = case
        for key in path[:-1]:
            target = target[key]
        target[path[-1]] = value
    return mutate


# Every input field is consumed or closed: an unknown or missing input key is refused
# with the document (below), and unknown content nested in a Gate list yields that
# case's mismatch instead of silent equality.
def _extra_key(*path):
    def mutate(case):
        target = case
        for key in path:
            target = target[key]
        target["extra"] = 1
    return mutate


UNCONSUMED_INPUTS = {
    "g001_gate_row_object": ("M10-G001", _setter("inputs", "gates_a", value=[{"gate": 1, "extra": 1}]), "inputs.gates_a"),
    "g001_gate_row_list": ("M10-G001", _setter("inputs", "gates_b", value=[[2]]), "inputs.gates_b"),
    "g001_gates_object": ("M10-G001", _setter("inputs", "gates_b", value={"extra": 1, "gates": [2]}), "inputs.gates_b"),
    # HDE-EPIC043 WU-PR-10: every nested input object of the new kinds is closed.
    "g002_gates_object": ("M10-G002", _setter("inputs", "gates_a", value={"gates": [1]}), "inputs.gates_a"),
    "g003_channel_row": ("M10-G003", _extra_key("inputs", "channels", 0), "inputs.channels[0]"),
    "g003_scenario": ("M10-G003", _extra_key("inputs", "scenarios", 0), "inputs.scenarios[0]"),
    "g003_owned_row": ("M10-G003", _extra_key("inputs", "scenarios", 0, "owned", 0), "inputs.scenarios[0].owned[0]"),
    "g005_pair": ("M10-G005", _extra_key("inputs", "pairs", 0), "inputs.pairs[0]"),
    "g005_party": ("M10-G005", _extra_key("inputs", "pairs", 1, "b"), "inputs.pairs[1].b"),
    "g006_category_row": ("M10-G006", _extra_key("inputs", "categories", 0), "inputs.categories[0]"),
    "g007_adverse": ("M10-G007", _extra_key("inputs", "adverse", 0), "inputs.adverse[0]"),
    "g007_meta": ("M10-G007", _extra_key("inputs", "meta"), "inputs.meta"),
    "g008_party": ("M10-G008", _extra_key("inputs", "a"), "inputs.a"),
    "g008_meta": ("M10-G008", _extra_key("inputs", "meta"), "inputs.meta"),
}


@pytest.mark.parametrize("name", sorted(UNCONSUMED_INPUTS))
def test_unconsumed_or_unknown_input_fields_are_mismatches(bundle_root, tmp_path, name) -> None:
    case_id, mutate, path = UNCONSUMED_INPUTS[name]
    document = _document()
    _alter(document, case_id, mutate)
    result = artifact_tools.compare_goldens(bundle_root, _write_document(tmp_path / f"{name}.json", document))
    assert result.ok is False
    assert [(row.case_id, row.path) for row in result.mismatches] == [(case_id, path)]
    assert all(row.outcome == "match" for row in result.cases if row.case_id != case_id)


# --- refusals ---------------------------------------------------------------------------

def _refusal(root: Path, goldens: Path) -> str:
    with pytest.raises(artifact_tools.GoldenComparisonRefusal) as raised:
        artifact_tools.compare_goldens(root, goldens)
    return raised.value.code


def _document_without(case_id: str) -> dict:
    document = _document()
    document["cases"] = [case for case in document["cases"] if case["case_id"] != case_id]
    return document


def _document_duplicating(case_id: str) -> dict:
    document = _document()
    document["cases"].append(copy.deepcopy(_case(document, case_id)))
    return document


def _document_relabeled() -> dict:
    document = _document()
    _case(document, "M10-G001")["case_type"] = "application"
    return document


def _document_unknown_kind() -> dict:
    document = _document()
    _case(document, "M10-G001")["kind"] = "evaluate_pair"
    return document


def _document_unknown_top_key() -> dict:
    document = _document()
    document["extra"] = True
    return document


def _document_unknown_case_key() -> dict:
    document = _document()
    _case(document, "M10-G001")["comment"] = "x"
    return document


def _document_unknown_input_key() -> dict:
    document = _document()
    _case(document, "M10-G001")["inputs"]["extra"] = 1
    return document


def _document_missing_input_key() -> dict:
    document = _document()
    del _case(document, "M10-G001")["inputs"]["gates_b"]
    return document


# HDE-EPIC043 WU-PR-10 (D-6): the case table is closed and ordered.
def _document_with_extra_case() -> dict:
    document = _document()
    extra = copy.deepcopy(_case(document, "M10-G001"))
    extra["case_id"] = "M10-G999"
    document["cases"].append(extra)
    return document


def _document_swapped() -> dict:
    document = _document()
    document["cases"][1:3] = document["cases"][1:3][::-1]
    return document


def _document_renamed() -> dict:
    document = _document()
    _case(document, "M10-G001")["case_id"] = "M10-G001-v2"
    return document


def _document_without_cases() -> dict:
    document = _document()
    document["cases"] = []
    return document


def _document_kind_relabeled() -> dict:
    document = _document()
    _case(document, "M10-G004")["kind"] = "signal_operation"
    return document


def _document_application_relabeled() -> dict:
    document = _document()
    _case(document, "M10-G005")["case_type"] = "calculation"
    return document


def _document_with_constants(mutate) -> dict:
    document = _document()
    mutate(document["constants"])
    return document


@pytest.mark.parametrize(
    ("build", "code"),
    [
        (lambda: _document_without("M10-G001"), "GOLDENS_MEMBERSHIP_INVALID"),
        (lambda: _document_without("M10-G005"), "GOLDENS_MEMBERSHIP_INVALID"),
        (lambda: _document_duplicating("M10-G001"), "GOLDENS_MEMBERSHIP_INVALID"),
        (_document_with_extra_case, "GOLDENS_MEMBERSHIP_INVALID"),
        (_document_swapped, "GOLDENS_MEMBERSHIP_INVALID"),
        (_document_renamed, "GOLDENS_MEMBERSHIP_INVALID"),
        (_document_without_cases, "GOLDENS_MEMBERSHIP_INVALID"),
        (_document_relabeled, "GOLDENS_CASE_TYPE_INVALID"),
        (_document_kind_relabeled, "GOLDENS_CASE_TYPE_INVALID"),
        (_document_application_relabeled, "GOLDENS_CASE_TYPE_INVALID"),
        (_document_unknown_kind, "GOLDENS_INVALID"),
        (_document_unknown_top_key, "GOLDENS_INVALID"),
        (_document_unknown_case_key, "GOLDENS_INVALID"),
        (_document_unknown_input_key, "GOLDENS_INVALID"),
        (_document_missing_input_key, "GOLDENS_INVALID"),
        (lambda: _document_with_constants(lambda c: c.__setitem__("uuid_1", "00000000-0000-0000-0000-000000000001")), "GOLDENS_INVALID"),
        (lambda: _document_with_constants(lambda c: c.pop("router_stub")), "GOLDENS_INVALID"),
        (lambda: _document_with_constants(lambda c: c["router_stub"].pop("shared")), "GOLDENS_INVALID"),
        (lambda: _document_with_constants(lambda c: c["router_stub"].__setitem__("shared", "")), "GOLDENS_INVALID"),
        (lambda: _document_with_constants(lambda c: c["synthetic_projection_fields"].__setitem__("gates", [1])), "GOLDENS_INVALID"),
        (lambda: _document_with_constants(lambda c: c.__setitem__("synthetic_projection_fields", {})), "GOLDENS_INVALID"),
        (lambda: _document_with_constants(lambda c: c.__setitem__("config_id", 2)), "GOLDENS_INVALID"),
    ],
    ids=[
        "g001_missing", "g005_missing", "g001_duplicated", "g999_extra", "g002_g003_swapped", "g001_renamed", "no_cases",
        "g001_case_type", "g004_kind", "g005_case_type", "unknown_kind", "unknown_top_key", "unknown_case_key",
        "unknown_input_key", "missing_input_key", "constants_unknown_key", "constants_no_router_stub",
        "router_stub_missing_key", "router_stub_empty_key", "projection_fields_with_gates", "projection_fields_empty",
        "config_id_not_string",
    ],
)
def test_membership_type_and_schema_refusals(bundle_root, tmp_path, build, code) -> None:
    assert _refusal(bundle_root, _write_document(tmp_path / "doc.json", build())) == code


@pytest.mark.parametrize(
    ("raw", "label"),
    [
        (lambda: json.dumps(_document(), indent=2, sort_keys=True).encode("utf-8") + b"\n", "pretty"),
        (lambda: GOLDENS.read_bytes().replace(b"\n", b"\r\n"), "crlf"),
        (lambda: GOLDENS.read_bytes() + b"\n", "double_lf"),
        (lambda: GOLDENS.read_bytes()[:-1], "no_final_lf"),
        (lambda: b"\xef\xbb\xbf" + GOLDENS.read_bytes(), "bom"),
        (lambda: b"{not json\n", "not_json"),
        (lambda: b'{"schema":"magic10_goldens.v2","schema":"magic10_goldens.v2"}\n', "duplicate_key"),
    ],
)
def test_noncanonical_or_invalid_bytes_refuse(bundle_root, tmp_path, raw, label) -> None:
    path = tmp_path / f"{label}.json"
    path.write_bytes(raw())
    assert _refusal(bundle_root, path) == "GOLDENS_INVALID"


def test_symlinked_or_missing_goldens_refuse(bundle_root, tmp_path) -> None:
    link = tmp_path / "link.json"
    link.symlink_to(GOLDENS)
    assert _refusal(bundle_root, link) == "GOLDENS_INVALID"
    assert _refusal(bundle_root, tmp_path / "absent.json") == "GOLDENS_INVALID"


# The goldens are read through a bound (CR-19): the committed collection fits well
# inside it, and a document one byte longer than the bound allows is refused.
def test_the_goldens_size_bound_is_pinned_and_holds_the_committed_collection(bundle_root, monkeypatch) -> None:
    assert artifact_tools.GOLDENS_MAX_BYTES == 1_048_576
    size = GOLDENS.stat().st_size
    assert size < artifact_tools.GOLDENS_MAX_BYTES
    monkeypatch.setattr(artifact_tools, "GOLDENS_MAX_BYTES", size)
    assert artifact_tools.compare_goldens(bundle_root, GOLDENS).ok is True
    monkeypatch.setattr(artifact_tools, "GOLDENS_MAX_BYTES", size - 1)
    assert _refusal(bundle_root, GOLDENS) == "GOLDENS_INVALID"


# A sparse 8 GiB file under a 2 GiB address-space limit: reading it whole cannot
# succeed, so only a bounded read reaches the refusal, and it does so before admission.
def test_an_oversized_goldens_file_is_refused_without_reading_it_whole(bundle_root, tmp_path) -> None:
    big = tmp_path / "big.json"
    with big.open("wb") as handle:
        handle.truncate(8 * 1024 ** 3)

    def cap_address_space() -> None:
        _soft, hard = resource.getrlimit(resource.RLIMIT_AS)
        limit = 2 * 1024 ** 3 if hard == resource.RLIM_INFINITY else min(2 * 1024 ** 3, hard)
        resource.setrlimit(resource.RLIMIT_AS, (limit, hard))

    result = subprocess.run(
        [sys.executable, str(ROOT / "tools/config/generate_config_artifacts.py"),
         "--compare-goldens", str(bundle_root), "--goldens", str(big)],
        cwd=tmp_path, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}, capture_output=True,
        timeout=120, preexec_fn=cap_address_space)
    assert (result.returncode, result.stdout, result.stderr) == (
        config_tools.GOLDEN_COMPARISON_REFUSAL_EXIT_CODE, b"", b"GOLDENS_INVALID\n")


class _Blocked(Exception):
    """Raised by the test deadline; deliberately not an ``OSError``, so no handler absorbs it."""


@contextlib.contextmanager
def _deadline(seconds):
    def expire(signum, frame):
        raise _Blocked("reading the goldens blocked")

    previous = signal.signal(signal.SIGALRM, expire)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, previous)


def _open_descriptors() -> set[str]:
    return set(os.listdir("/proc/self/fd"))


# A FIFO, device or directory is refused on the opened descriptor before any read, an
# oversized file after at most one byte past the bound, and every refusal closes the
# descriptor it opened.
@pytest.mark.parametrize("kind", ["fifo", "device", "directory", "oversized"])
def test_special_or_oversized_goldens_refuse_and_close_their_descriptor(bundle_root, tmp_path, kind) -> None:
    if kind == "fifo":
        path = tmp_path / "goldens.fifo"
        os.mkfifo(path)  # no writer: a blocking open or read would never return
    elif kind == "device":
        path = Path(os.devnull)  # a character device, which reads as empty
    elif kind == "directory":
        path = tmp_path
    else:
        path = tmp_path / "goldens.big"
        path.write_bytes(b" " * (artifact_tools.GOLDENS_MAX_BYTES + 1))
    before = _open_descriptors()
    with _deadline(2):
        assert _refusal(bundle_root, path) == "GOLDENS_INVALID"
    assert _open_descriptors() == before


def test_admission_refusals_are_never_equality(tmp_path, v2_roster) -> None:
    incomplete = synthetic_v2_candidate_root(tmp_path / "incomplete")
    manifest = json.loads((incomplete / "catalog/manifest.json").read_bytes())
    manifest["files"] = manifest["files"][:-1]
    write_canonical(incomplete / "catalog/manifest.json", manifest)
    assert _refusal(incomplete, GOLDENS) == "CANDIDATE_ADMISSION_REFUSED:INCOMPLETE_RELEASE_ROSTER"

    tampered = synthetic_v2_candidate_root(tmp_path / "tampered")
    member = tampered / "tools/bodygraph/check_magic10_gate_readiness.py"
    member.write_bytes(member.read_bytes() + b"# changed after the manifest was cut\n")
    assert _refusal(tampered, GOLDENS) == "CANDIDATE_ADMISSION_REFUSED:MANIFEST_MEMBER_HASH_MISMATCH"


# --- HDE-EPIC040-PR06: the actual complete admitted candidate ---------------------------

def test_compare_goldens_admits_the_real_root(tmp_path, capfdbinary) -> None:
    """The repository root is the admitted release: every golden matches."""
    from engine.runtime.identity import identity_meta

    before_status = _git_status()
    result = artifact_tools.compare_goldens(ROOT, GOLDENS)
    assert result.ok is True and result.mismatches == ()
    assert [(row.case_id, row.outcome) for row in result.cases] == [(case["case_id"], "match") for case in _document()["cases"]]
    assert result.candidate_release_id == identity_meta()["release_id"]
    report_path = tmp_path / "golden_report.json"
    code, out, err = _run_cli(["--compare-goldens", str(ROOT), "--report", str(report_path)], capfdbinary)
    assert (code, err) == (0, b"")
    assert out == report_path.read_bytes() == artifact_tools.render_golden_report(result)
    assert json.loads(out)["ok"] is True
    # The report went outside the tree and nothing inside it changed.
    assert _git_status() == before_status


# --- HDE-EPIC040-PR06 (O-17 / CR-06): executed roster members are bound to the candidate --

def test_executed_member_module_map_is_derived_from_the_roster(bundle, monkeypatch) -> None:
    from engine.config import registry_loader

    mapping = artifact_tools.golden_executed_member_modules(bundle)
    # Derived from the admitted candidate's manifest, not from the import-time roster constant.
    assert tuple(mapping) == tuple(row.path for row in bundle.manifest.files if row.path.endswith(".py"))
    assert tuple(mapping) == tuple(path for path in v2_candidate_roster() if path.endswith(".py"))
    assert "engine/magic10_v2/calculation.py" in mapping and "engine/magic10_v2/calculation.py" in registry_loader.ADMITTED_RELEASE_ROSTER
    # HDE-EPIC043 WU-PR-10: the cut roster now lists the v2 modules too, so the constant is
    # replaced to show the map does not read it.
    monkeypatch.setattr(registry_loader, "ADMITTED_RELEASE_ROSTER", ())
    assert artifact_tools.golden_executed_member_modules(bundle) == mapping
    assert mapping["engine/compat/compute.py"] == "engine.compat.compute"
    assert mapping["engine/magic10_v2/calculation.py"] == "engine.magic10_v2.calculation"
    assert mapping["presenter/reader_v1/emitter.py"] == "presenter.reader_v1.emitter"
    assert mapping["tools/bodygraph/check_magic10_gate_readiness.py"] == "tools.bodygraph.check_magic10_gate_readiness"
    assert "migrations/005_identity.sql" not in mapping
    assert all(name == path[:-3].replace("/", ".") for path, name in mapping.items())


@pytest.mark.parametrize("path", ["engine/compat/compute.py", "engine/bodygraph/gates.py", "engine/narratives/router.py"])
def test_executed_member_source_mismatch_refuses(tmp_path, capfdbinary, v2_roster, path) -> None:
    """A manifest-consistent candidate whose executed member differs from the executing
    installation's source is a refusal (exit 5), never a match and never a mismatch row."""
    altered = synthetic_v2_candidate_root(tmp_path / "altered")
    member = altered / path
    member.write_bytes(member.read_bytes() + b"# altered application member\n")
    write_release_manifest(altered, v2_roster)
    # Admission alone still succeeds: the member is outside the covered mechanics set.
    admitted = _load_active_mechanics_bundle_from_root(altered)
    assert admitted.release_id
    module_name = artifact_tools.golden_executed_member_modules(admitted)[path]
    assert module_name in sys.modules
    assert _refusal(altered, GOLDENS) == f"CANDIDATE_EXECUTING_SOURCE_MISMATCH:{path}"
    code, out, err = _run_cli(["--compare-goldens", str(altered)], capfdbinary)
    assert (code, out, err) == (config_tools.GOLDEN_COMPARISON_REFUSAL_EXIT_CODE, b"",
                                f"CANDIDATE_EXECUTING_SOURCE_MISMATCH:{path}\n".encode())


@pytest.mark.parametrize("kind", ["deleted", "missing", "symlink", "not_source"])
def test_executed_member_without_readable_source_refuses(bundle_root, tmp_path, monkeypatch, kind) -> None:
    module = sys.modules["engine.compat.compute"]
    if kind == "deleted":
        monkeypatch.delattr(module, "__file__")
    elif kind == "missing":
        monkeypatch.setattr(module, "__file__", str(tmp_path / "gone.py"))
    elif kind == "symlink":
        link = tmp_path / "compute.py"
        link.symlink_to(Path(module.__file__))
        monkeypatch.setattr(module, "__file__", str(link))
    else:
        compiled = tmp_path / "compute.pyc"
        compiled.write_bytes(b"\x00")
        monkeypatch.setattr(module, "__file__", str(compiled))
    assert _refusal(bundle_root, GOLDENS) == "CANDIDATE_EXECUTING_SOURCE_UNAVAILABLE:engine/compat/compute.py"


def test_unloaded_members_are_not_bound(tmp_path, monkeypatch, v2_roster) -> None:
    name = "tools.bodygraph.check_magic10_gate_readiness"
    monkeypatch.delitem(sys.modules, name, raising=False)
    altered = synthetic_v2_candidate_root(tmp_path / "altered", fixture_maxima=False)
    member = altered / "tools/bodygraph/check_magic10_gate_readiness.py"
    member.write_bytes(member.read_bytes() + b"# altered but never executed by the goldens\n")
    write_release_manifest(altered, v2_roster)
    assert artifact_tools.compare_goldens(altered, GOLDENS).ok is True
    assert name not in sys.modules


def test_executed_member_binding_is_read_only(bundle_root) -> None:
    artifact_tools.compare_goldens(bundle_root, GOLDENS)  # warm every lazy runner import
    before_modules, before_root = dict(sys.modules), _snapshot(bundle_root)
    assert artifact_tools.compare_goldens(bundle_root, GOLDENS).ok is True
    assert dict(sys.modules) == before_modules
    assert _snapshot(bundle_root) == before_root
    candidate = str(bundle_root)
    assert not any(str(getattr(module, "__file__", "") or "").startswith(candidate)
                   for module in list(sys.modules.values()))
    tree = ast.parse((ROOT / "tools/config/artifacts.py").read_text(encoding="utf-8"))
    binding = _module_functions(tree)["_golden_bind_executed_members"]
    assert not (_referenced_names(binding) & {"import_module", "reload", "exec", "compile", "__import__",
                                              "spec_from_file_location", "exec_module", "write_bytes"})
    assert not any(isinstance(node, (ast.Import, ast.ImportFrom)) for node in ast.walk(binding))


def test_candidate_root_must_be_a_real_directory(bundle_root, tmp_path) -> None:
    assert _refusal(tmp_path / "missing", GOLDENS) == "CANDIDATE_ROOT_INVALID"
    file_root = tmp_path / "file"
    file_root.write_bytes(b"x\n")
    assert _refusal(file_root, GOLDENS) == "CANDIDATE_ROOT_INVALID"
    link = tmp_path / "link"
    link.symlink_to(bundle_root, target_is_directory=True)
    assert _refusal(link, GOLDENS) == "CANDIDATE_ROOT_INVALID"


def _deny(monkeypatch, method: str, denied: Path) -> None:
    """Make one ``Path`` method raise EACCES for exactly one path (root can read anything)."""
    original = getattr(Path, method)

    def guarded(self, *args, **kwargs):
        if os.path.realpath(self) == os.path.realpath(denied):
            raise PermissionError(errno.EACCES, "Permission denied", str(self))
        return original(self, *args, **kwargs)

    monkeypatch.setattr(Path, method, guarded)


def _deny_open(monkeypatch, denied: Path) -> None:
    """Make ``os.open`` raise EACCES for exactly one path (root can open anything)."""
    original = os.open

    def guarded(path, flags, *args, **kwargs):
        if kwargs.get("dir_fd") is None and os.path.realpath(path) == os.path.realpath(denied):
            raise PermissionError(errno.EACCES, "Permission denied", str(path))
        return original(path, flags, *args, **kwargs)

    monkeypatch.setattr(os, "open", guarded)


# The goldens reader opens the path itself and reads the opened descriptor, so its two
# failures are injected there: a denied open, and a regular file whose read fails
# (``/proc/self/mem`` is a regular, zero-length file whose offset 0 is unmapped: EIO).
@pytest.mark.parametrize(("target", "method", "code"), [
    ("goldens", "open", "GOLDENS_INVALID"),
    ("goldens", "read", "GOLDENS_INVALID"),
    ("candidate", "is_symlink", "CANDIDATE_ROOT_INVALID"),
])
def test_inputs_that_cannot_be_inspected_or_read_refuse(bundle_root, tmp_path, capfdbinary, monkeypatch, target, method, code) -> None:
    goldens = tmp_path / "goldens.json"
    goldens.write_bytes(GOLDENS.read_bytes())
    if method == "open":
        _deny_open(monkeypatch, goldens)
    elif method == "read":
        goldens = Path("/proc/self/mem")
        assert stat.S_ISREG(goldens.stat().st_mode)
    else:
        _deny(monkeypatch, method, bundle_root)
    assert _refusal(bundle_root, goldens) == code
    result = _run_cli(["--compare-goldens", str(bundle_root), "--goldens", str(goldens)], capfdbinary)
    assert result == (config_tools.GOLDEN_COMPARISON_REFUSAL_EXIT_CODE, b"", f"{code}\n".encode("ascii"))


# HDE-EPIC043 WU-PR-09 retired, with their subjects, the v1 golden tests of the annotation
# and transcription pins, the M10-G005/G007/G008 application runners (self-pair seams,
# compute._route routing, the router stub) and the consistently-altered-case pins.  WU-PR-10
# restores the three application runners on the v2 path (their negative controls are in the
# tables above); the annotation and transcription pins stay retired.


@pytest.mark.parametrize("tags", [[{"tag": "pf01_9_5"}], [["pf01_9_5"]], [1], [None]])
def test_non_string_provenance_refuses(bundle_root, tmp_path, capfdbinary, tags) -> None:
    document = _document()
    _case(document, "M10-G001")["input_provenance"] = tags
    goldens = _write_document(tmp_path / "provenance.json", document)
    assert _refusal(bundle_root, goldens) == "GOLDENS_INVALID"
    result = _run_cli(["--compare-goldens", str(bundle_root), "--goldens", str(goldens)], capfdbinary)
    assert result == (config_tools.GOLDEN_COMPARISON_REFUSAL_EXIT_CODE, b"", b"GOLDENS_INVALID\n")


def test_deeply_nested_goldens_refuse(bundle_root, tmp_path) -> None:
    path = tmp_path / "deep.json"
    path.write_bytes(b'{"cases":' + b"[" * 100000 + b"]" * 100000 + b"}\n")
    assert _refusal(bundle_root, path) == "GOLDENS_INVALID"


# Canonical JSON carries integers only, so a non-finite or fractional number is
# refused before it could reach a report (bare NaN is not JSON at all).
@pytest.mark.parametrize("value", [float("nan"), float("inf"), float("-inf"), 25.5], ids=["nan", "inf", "neg_inf", "fraction"])
def test_non_integer_numbers_refuse(bundle_root, tmp_path, capfdbinary, value) -> None:
    document = _document()
    _case(document, "M10-G001")["expected"]["categories"][0]["score"] = value
    goldens = _write_document(tmp_path / "number.json", document)
    assert _refusal(bundle_root, goldens) == "GOLDENS_INVALID"
    result = _run_cli(["--compare-goldens", str(bundle_root), "--goldens", str(goldens)], capfdbinary)
    assert result == (config_tools.GOLDEN_COMPARISON_REFUSAL_EXIT_CODE, b"", b"GOLDENS_INVALID\n")


class _Opaque:
    pass


def _strict_number(token: str) -> object:
    raise ValueError(f"non-integer JSON number: {token}")


# The same holds for what an entrypoint returns: a float, a non-finite number, bytes or
# an arbitrary object is that case's mismatch with a described value, the report stays
# canonical JSON, and the CLI keeps its exit contract instead of crashing.
@pytest.mark.parametrize("value, described", [(24.5, "<float 24.5>"), (float("nan"), "<float nan>"), (b"24", "<bytes>"),
                                              (_Opaque(), "<_Opaque>")], ids=["float", "nan", "bytes", "object"])
def test_non_canonical_observed_values_are_described_never_a_crash(bundle_root, tmp_path, capfdbinary, monkeypatch,
                                                                     value, described) -> None:
    real = artifact_tools._GOLDEN_RUNNERS["category_vector"]

    def regressed(case, constants, bundle):
        observed = real(case, constants, bundle)
        observed["categories"][0]["score"] = value
        return observed

    monkeypatch.setitem(artifact_tools._GOLDEN_RUNNERS, "category_vector", regressed)
    result = artifact_tools.compare_goldens(bundle_root, GOLDENS)
    assert [(row.case_id, row.path, row.expected, row.actual) for row in result.mismatches] == [
        ("M10-G001", "expected.categories[0].score", 0, described)]
    report_path = tmp_path / "report.json"
    code, out, err = _run_cli(["--compare-goldens", str(bundle_root), "--report", str(report_path)], capfdbinary)
    assert (code, out, err) == (config_tools.GOLDEN_COMPARISON_MISMATCH_EXIT_CODE, b"", b"GOLDEN_COMPARISON_MISMATCH:1\n")
    raw = report_path.read_bytes()
    report = json.loads(raw, parse_constant=_strict_number, parse_float=_strict_number)
    assert sercanon(report, sort_keys=True) == raw
    assert report["mismatches"] == [{"case_id": "M10-G001", "path": "expected.categories[0].score", "expected": 0,
                                     "actual": described}]


def test_every_registry_admission_error_is_a_refusal(bundle_root, tmp_path, capfdbinary, monkeypatch) -> None:
    duplicated = synthetic_v2_candidate_root(tmp_path / "duplicated")
    manifest = json.loads((duplicated / "catalog/manifest.json").read_bytes())
    manifest["files"].append(copy.deepcopy(manifest["files"][0]))
    write_canonical(duplicated / "catalog/manifest.json", manifest)
    assert _refusal(duplicated, GOLDENS) == "CANDIDATE_ADMISSION_REFUSED:DUPLICATE_MANIFEST_ENTRY"
    result = _run_cli(["--compare-goldens", str(duplicated)], capfdbinary)
    assert result == (config_tools.GOLDEN_COMPARISON_REFUSAL_EXIT_CODE, b"",
                      b"CANDIDATE_ADMISSION_REFUSED:DUPLICATE_MANIFEST_ENTRY\n")
    for error in (UnknownIdError("UNKNOWN_CHANNEL", "unknown"), AliasPolicyError("ALIAS_FORBIDDEN", "alias")):
        def refuse(root, _error=error):
            raise _error
        monkeypatch.setattr(artifact_tools, "_load_active_mechanics_bundle_from_root", refuse)
        assert _refusal(bundle_root, GOLDENS) == f"CANDIDATE_ADMISSION_REFUSED:{error.code}"


def test_rails_are_required_before_anything_runs(bundle_root, monkeypatch) -> None:
    monkeypatch.delenv("SAFE_MODE", raising=False)
    with pytest.raises(SystemExit) as raised:
        artifact_tools.compare_goldens(bundle_root, GOLDENS)
    assert str(raised.value.code).startswith("RAILS_CLOSED_REQUIRED:")


# --- non-mutation and spies -------------------------------------------------------------

def test_runs_leave_candidate_goldens_repository_and_seams_untouched(bundle_root, tmp_path, monkeypatch) -> None:
    for name, target in (
        ("write_magic10_config", artifact_tools), ("write_band_edges", artifact_tools), ("_publish_prepared", artifact_tools),
        ("generate_config_artifacts", config_tools), ("check_config_artifacts", config_tools),
        ("publish_config_family", config_tools), ("generate_catalog_logs", config_tools),
        ("_publish_staged", updater), ("route_keys", narrative_router), ("get_pack", narrative_state), ("load_pack", narrative_loader),
    ):
        monkeypatch.setattr(target, name, lambda *a, _n=name, **k: pytest.fail(f"{_n} reached"))
    before_root, before_goldens = _snapshot(bundle_root), GOLDENS.read_bytes()
    before_status, before_pack = _git_status(), narrative_state._PACK
    mounts = (ROOT / "narratives", Path.cwd() / "narratives")
    before_mounts = [_snapshot(mount) if mount.exists() else None for mount in mounts]
    mismatch_document = _document()
    _alter(mismatch_document, *ALTERATIONS["g001_score"][:2])
    mismatch_goldens = _write_document(tmp_path / "mismatch.json", mismatch_document)
    incomplete = synthetic_v2_candidate_root(tmp_path / "incomplete")
    write_canonical(incomplete / "catalog/manifest.json", {**json.loads((incomplete / "catalog/manifest.json").read_bytes()), "files": []})
    before_incomplete = _snapshot(incomplete)

    assert artifact_tools.compare_goldens(bundle_root, GOLDENS).ok is True
    assert artifact_tools.compare_goldens(bundle_root, mismatch_goldens).ok is False
    with pytest.raises(artifact_tools.GoldenComparisonRefusal):
        artifact_tools.compare_goldens(incomplete, GOLDENS)
    with pytest.raises(artifact_tools.GoldenComparisonRefusal):
        artifact_tools.compare_goldens(bundle_root, tmp_path / "absent.json")

    assert _snapshot(bundle_root) == before_root and GOLDENS.read_bytes() == before_goldens
    assert _snapshot(incomplete) == before_incomplete
    assert _git_status() == before_status
    assert [_snapshot(mount) if mount.exists() else None for mount in mounts] == before_mounts
    assert narrative_state._PACK is before_pack
    assert compute._BUNDLE_PROVIDER is compute.load_active_mechanics_bundle


# --- structural guard -------------------------------------------------------------------

def _module_functions(tree: ast.Module) -> dict[str, ast.FunctionDef]:
    return {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}


def _module_assignments(tree: ast.Module) -> dict[str, ast.AST]:
    found = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    found[target.id] = node.value
    return found


def _referenced_names(node: ast.AST) -> set[str]:
    names = set()
    for child in ast.walk(node):
        if isinstance(child, ast.Name):
            names.add(child.id)
        elif isinstance(child, ast.Attribute):
            names.add(child.attr)
    return names


def test_compare_path_is_structurally_unable_to_reach_write_activation_or_generation() -> None:
    tree = ast.parse((ROOT / "tools/config/artifacts.py").read_text(encoding="utf-8"))
    functions, assignments = _module_functions(tree), _module_assignments(tree)
    reachable, frontier = set(), ["compare_goldens", "render_golden_report"]
    while frontier:
        name = frontier.pop()
        if name in reachable or name not in functions:
            continue
        reachable.add(name)
        referenced = _referenced_names(functions[name])
        for table in sorted(referenced & set(assignments)):
            referenced |= _referenced_names(assignments[table])
        frontier.extend(sorted(referenced & set(functions)))
    assert "compare_goldens" in reachable and any(name.startswith("_golden_run_") for name in reachable)
    for name in sorted(reachable):
        assert not (_referenced_names(functions[name]) & FORBIDDEN_NAMES), name
    assert not any(name in FORBIDDEN_NAMES for name in reachable)

    cli_tree = ast.parse((ROOT / "tools/config/generate_config_artifacts.py").read_text(encoding="utf-8"))
    cli_functions = _module_functions(cli_tree)
    compare_main = cli_functions["_compare_goldens_main"]
    assert not (_referenced_names(compare_main) & FORBIDDEN_NAMES)
    assert {"compare_goldens", "render_golden_report", "_write_golden_report", "require_closed_rails"} <= _referenced_names(compare_main)
    main = cli_functions["_main"]
    branch = next(node for node in ast.walk(main) if isinstance(node, ast.If)
                  and isinstance(node.test, ast.Compare) and "compare_goldens" in ast.unparse(node.test))
    assert not (_referenced_names(branch) & FORBIDDEN_NAMES)
    assert "_compare_goldens_main" in _referenced_names(branch)


# --- CLI --------------------------------------------------------------------------------

def _run_cli(argv: list[str], capfdbinary) -> tuple[int, bytes, bytes]:
    code = config_tools.main(argv)
    out, err = capfdbinary.readouterr()
    return code, out, err


def test_cli_match_prints_the_canonical_report(bundle_root, capfdbinary) -> None:
    code, out, err = _run_cli(["--compare-goldens", str(bundle_root)], capfdbinary)
    assert code == 0 and err == b""
    assert out == artifact_tools.render_golden_report(artifact_tools.compare_goldens(bundle_root, GOLDENS))
    assert out.endswith(b"\n") and out.count(b"\n") == 1
    report = json.loads(out)
    assert report["ok"] is True and report["schema"] == artifact_tools.GOLDEN_COMPARISON_SCHEMA
    assert [row["outcome"] for row in report["cases"]] == ["match"] * len(_document()["cases"]) and report["mismatches"] == []


def test_cli_mismatch_is_a_single_token_and_the_report_holds_every_mismatch(bundle_root, tmp_path, capfdbinary) -> None:
    document = _document()
    for name in ("g001_score", "g001_band"):
        _alter(document, *ALTERATIONS[name][:2])
    goldens = _write_document(tmp_path / "mismatch.json", document)
    report_path = tmp_path / "out" / "report.json"
    report_path.parent.mkdir()
    code, out, err = _run_cli(["--compare-goldens", str(bundle_root), "--goldens", str(goldens), "--report", str(report_path)], capfdbinary)
    assert (code, out) == (config_tools.GOLDEN_COMPARISON_MISMATCH_EXIT_CODE, b"")
    assert err == b"GOLDEN_COMPARISON_MISMATCH:2\n"
    report = json.loads(report_path.read_bytes())
    assert report["ok"] is False and {(row["case_id"], row["path"]) for row in report["mismatches"]} == {
        ("M10-G001", "expected.categories[0].score"), ("M10-G001", "expected.categories[3].band")}
    assert report_path.read_bytes() == artifact_tools.render_golden_report(artifact_tools.compare_goldens(bundle_root, goldens))


def test_cli_match_report_file_and_determinism(bundle_root, tmp_path, capfdbinary) -> None:
    report_path = tmp_path / "match.json"
    code, out, _ = _run_cli(["--compare-goldens", str(bundle_root), "--report", str(report_path)], capfdbinary)
    assert code == 0 and report_path.read_bytes() == out
    second, out_two, _ = _run_cli(["--compare-goldens", str(bundle_root)], capfdbinary)
    assert second == 0 and out_two == out
    other_root = synthetic_v2_candidate_root(tmp_path / "other", fixture_maxima=False)
    third, out_three, _ = _run_cli(["--compare-goldens", str(other_root)], capfdbinary)
    assert third == 0 and out_three == out  # the report names no host path, so the location drops out


def test_reports_carry_no_host_path(bundle_root, tmp_path, capfdbinary) -> None:
    report = json.loads(artifact_tools.render_golden_report(artifact_tools.compare_goldens(bundle_root, GOLDENS)))
    assert (report["candidate_root"], report["goldens_path"]) == ("<external>", "tests/fixtures/magic10/v2/goldens.json")
    document = _document()
    _alter(document, *ALTERATIONS["g001_score"][:2])
    goldens = _write_document(tmp_path / "mismatch.json", document)
    report_path = tmp_path / "out.json"
    code, _, _ = _run_cli(["--compare-goldens", str(bundle_root), "--goldens", str(goldens), "--report", str(report_path)],
                          capfdbinary)
    raw = report_path.read_bytes()
    assert code == config_tools.GOLDEN_COMPARISON_MISMATCH_EXIT_CODE
    assert (json.loads(raw)["candidate_root"], json.loads(raw)["goldens_path"]) == ("<external>", "<external>")
    for host_path in (bundle_root, tmp_path, ROOT):
        assert str(host_path).encode("utf-8") not in raw
    assert artifact_tools._golden_display(ROOT) == "."
    assert artifact_tools._golden_display(ROOT / "catalog") == "catalog"


@pytest.mark.parametrize("spelling", ["same_path", "through_symlinked_directory"])
def test_cli_report_path_equal_to_the_goldens_refuses(bundle_root, tmp_path, capfdbinary, spelling) -> None:
    goldens = tmp_path / "custom.json"
    goldens.write_bytes(GOLDENS.read_bytes())
    report_path = goldens
    if spelling == "through_symlinked_directory":
        (tmp_path / "alias").symlink_to(tmp_path, target_is_directory=True)
        report_path = tmp_path / "alias" / "custom.json"
    code, out, err = _run_cli(["--compare-goldens", str(bundle_root), "--goldens", str(goldens), "--report", str(report_path)],
                              capfdbinary)
    assert (code, out, err) == (config_tools.GOLDEN_COMPARISON_REFUSAL_EXIT_CODE, b"", b"REPORT_PATH_INVALID\n")
    assert goldens.read_bytes() == GOLDENS.read_bytes()


@pytest.mark.parametrize("target", ["candidate", "repository"])
def test_cli_report_path_inside_candidate_or_repository_refuses(bundle_root, tmp_path, capfdbinary, target) -> None:
    report_path = (bundle_root / "report.json") if target == "candidate" else (ROOT / "tests/fixtures/magic10/v1/report.json")
    code, out, err = _run_cli(["--compare-goldens", str(bundle_root), "--report", str(report_path)], capfdbinary)
    assert (code, out, err) == (config_tools.GOLDEN_COMPARISON_REFUSAL_EXIT_CODE, b"", b"REPORT_PATH_INVALID\n")
    assert not report_path.exists()


@pytest.mark.parametrize("stage", ["mkstemp", "replace"])
@pytest.mark.parametrize("goldens_kind", ["match", "mismatch"])
def test_cli_report_write_failure_is_a_refusal_never_a_mismatch(bundle_root, tmp_path, capfdbinary, monkeypatch,
                                                                stage, goldens_kind) -> None:
    goldens = GOLDENS
    if goldens_kind == "mismatch":
        document = _document()
        _alter(document, *ALTERATIONS["g001_score"][:2])
        goldens = _write_document(tmp_path / "mismatch.json", document)
    report_dir = tmp_path / "out"
    report_dir.mkdir()
    report_path = report_dir / "report.json"
    real_mkstemp, real_replace = config_tools.tempfile.mkstemp, config_tools.os.replace

    def mkstemp(*args, **kwargs):
        if os.path.realpath(kwargs.get("dir", "")) == os.path.realpath(report_dir):
            raise OSError(errno.ENOSPC, "No space left on device")
        return real_mkstemp(*args, **kwargs)

    def replace(src, dst, *args, **kwargs):
        if os.path.realpath(dst) == os.path.realpath(report_path):
            raise OSError(errno.EIO, "Input/output error")
        return real_replace(src, dst, *args, **kwargs)

    if stage == "mkstemp":
        monkeypatch.setattr(config_tools.tempfile, "mkstemp", mkstemp)
    else:
        monkeypatch.setattr(config_tools.os, "replace", replace)
    code, out, err = _run_cli(["--compare-goldens", str(bundle_root), "--goldens", str(goldens), "--report", str(report_path)],
                              capfdbinary)
    assert (code, out, err) == (config_tools.GOLDEN_COMPARISON_REFUSAL_EXIT_CODE, b"", b"REPORT_WRITE_FAILED\n")
    assert list(report_dir.iterdir()) == []  # neither a report nor a temporary file is left behind


def test_cli_report_path_that_cannot_be_inspected_refuses(bundle_root, tmp_path, capfdbinary, monkeypatch) -> None:
    report_dir = tmp_path / "sealed"
    report_dir.mkdir()
    _deny(monkeypatch, "is_dir", report_dir)
    code, out, err = _run_cli(["--compare-goldens", str(bundle_root), "--report", str(report_dir / "report.json")], capfdbinary)
    assert (code, out, err) == (config_tools.GOLDEN_COMPARISON_REFUSAL_EXIT_CODE, b"", b"REPORT_PATH_INVALID\n")
    assert list(report_dir.iterdir()) == []


def test_cli_refusals_and_usage(bundle_root, tmp_path, capfdbinary, monkeypatch) -> None:
    incomplete = synthetic_v2_candidate_root(tmp_path / "incomplete")
    manifest = json.loads((incomplete / "catalog/manifest.json").read_bytes())
    write_canonical(incomplete / "catalog/manifest.json", {**manifest, "files": manifest["files"][:-1]})
    code, out, err = _run_cli(["--compare-goldens", str(incomplete)], capfdbinary)
    assert (code, out, err) == (config_tools.GOLDEN_COMPARISON_REFUSAL_EXIT_CODE, b"", b"CANDIDATE_ADMISSION_REFUSED:INCOMPLETE_RELEASE_ROSTER\n")
    code, out, err = _run_cli(["--compare-goldens", str(bundle_root), "--goldens", str(tmp_path / "absent.json")], capfdbinary)
    assert (code, out, err) == (config_tools.GOLDEN_COMPARISON_REFUSAL_EXIT_CODE, b"", b"GOLDENS_INVALID\n")
    code, out, err = _run_cli(["--compare-goldens", str(bundle_root), "--report", str(tmp_path / "missing-dir" / "r.json")], capfdbinary)
    assert (code, out, err) == (config_tools.GOLDEN_COMPARISON_REFUSAL_EXIT_CODE, b"", b"REPORT_PATH_INVALID\n")
    for argv in (["--compare-goldens", str(bundle_root), "--allow-aliases"], ["--goldens", str(GOLDENS)], ["--report", str(tmp_path / "r.json")],
                 ["--compare-goldens", str(bundle_root), "--check"]):
        with pytest.raises(SystemExit) as raised:
            config_tools.main(argv)
        assert raised.value.code == 2
        capfdbinary.readouterr()
    monkeypatch.delenv("ALLOW_NETWORK", raising=False)
    code, out, err = _run_cli(["--compare-goldens", str(bundle_root)], capfdbinary)
    assert code == config_tools.GOLDEN_COMPARISON_REFUSAL_EXIT_CODE and out == b"" and err.startswith(b"RAILS_CLOSED_REQUIRED:")


# An empty path argument (for example an unset variable expanded by automation) is refused:
# it never becomes the current directory, the default goldens or "no report".  The
# current directory here is itself a valid candidate, so an empty root cannot pass by it.
@pytest.mark.parametrize("argument, token", [
    ("--compare-goldens", "CANDIDATE_ROOT_INVALID"),
    ("--goldens", "GOLDENS_INVALID"),
    ("--report", "REPORT_PATH_INVALID"),
], ids=["candidate_root", "goldens", "report"])
def test_cli_empty_path_arguments_refuse(bundle_root, capfdbinary, monkeypatch, argument, token) -> None:
    monkeypatch.chdir(bundle_root)
    before = _snapshot(bundle_root)
    argv = ["--compare-goldens", ""] if argument == "--compare-goldens" else ["--compare-goldens", str(bundle_root), argument, ""]
    assert _run_cli(argv, capfdbinary) == (config_tools.GOLDEN_COMPARISON_REFUSAL_EXIT_CODE, b"", f"{token}\n".encode())
    assert _snapshot(bundle_root) == before


# Outside --compare-goldens, --goldens and --report are usage errors even when empty; an
# empty value never falls through to the default writer mode.
@pytest.mark.parametrize("argument", ["--goldens", "--report"])
def test_golden_arguments_without_compare_goldens_are_usage_errors_even_when_empty(monkeypatch, capfdbinary, argument) -> None:
    for writer in ("generate_config_artifacts", "check_config_artifacts", "publish_config_family"):
        monkeypatch.setattr(config_tools, writer, lambda *args, _writer=writer, **kwargs: pytest.fail(f"{_writer} reached"))
    for value in ("", "value.json"):
        with pytest.raises(SystemExit) as raised:
            config_tools.main([argument, value])
        assert raised.value.code == 2
        capfdbinary.readouterr()


def test_refusal_and_mismatch_exit_codes_never_collide_with_release_not_admitted() -> None:
    assert config_tools.GOLDEN_COMPARISON_MISMATCH_EXIT_CODE == 1
    assert config_tools.GOLDEN_COMPARISON_REFUSAL_EXIT_CODE == 5


# --- classifier coherence ---------------------------------------------------------------

def test_classifier_binds_the_fixture_and_tools_to_this_module() -> None:
    fixture = "tests/fixtures/magic10/v1/goldens.json"
    this_module = "tests/config/test_config_artifacts.py"
    assert classifier.changed_test_targets(ROOT, [fixture]) == (this_module,)
    assert classifier._lanes_for_path(fixture) == {"product", "release"}
    for tool in ("tools/config/artifacts.py", "tools/config/generate_config_artifacts.py"):
        assert this_module in classifier._config_writer_owner_targets(ROOT, tool)
        assert this_module in classifier.changed_test_targets(ROOT, [tool])
    assert this_module in classifier._full_validation_test_targets()


# --- HDE-CRD-0002 WU-PR-05 (S19-F09): the golden comparison's --report refusal covers the candidate root
# as compare_goldens admits it (the lexical absolute path), so <symlink>/.. in the candidate argument
# cannot place the report inside that root (HDE Mechanics Guide §25.6) -------------------------------

def test_s19_golden_report_refusal_covers_the_lexically_admitted_candidate_root(tmp_path):
    (tmp_path / "x" / "cand").mkdir(parents=True)
    (tmp_path / "deep" / "inner").mkdir(parents=True)
    (tmp_path / "deep" / "cand").mkdir()
    (tmp_path / "x" / "link").symlink_to(tmp_path / "deep" / "inner")
    candidate = tmp_path / "x" / "link" / ".." / "cand"  # admitted as x/cand; resolves to deep/cand
    goldens = tmp_path / "goldens.json"
    for inside in (tmp_path / "x" / "cand" / "report.json", tmp_path / "deep" / "cand" / "report.json"):
        with pytest.raises(artifact_tools.GoldenComparisonRefusal) as caught:
            config_tools._golden_report_destination(inside, candidate, goldens)
        assert str(caught.value) == "REPORT_PATH_INVALID"
    outside = tmp_path / "reports" / "report.json"
    outside.parent.mkdir()
    assert config_tools._golden_report_destination(outside, candidate, goldens) == outside


# --- HDE-EPIC043 WU-PR-04 (HDE-DIST008.1; HDE Schemas and Artifacts §8.14.2): the version-2
# band-edges shape. The roots are temporary copies; the labelled fixture
# tests/fixtures/magic10_v2/thresholds_v2.fixture.json and the per-category maxima below are
# test values, not canon and not the cutover maxima, and no maxima value is asserted as canon.
# catalog_root does not copy the v2 owning schema, so each v2 root receives it explicitly. -------

import shutil

from engine.config.registry_loader import SchemaValidationError as _V2SchemaValidationError
from engine.serializer import canon

_V2_THRESHOLDS_FIXTURE = ROOT / "tests/fixtures/magic10_v2/thresholds_v2.fixture.json"
_V2_SCHEMA = "schemas/thresholds_v2.schema.json"
_V2_KEYS = ["bands", "categories", "schema", "source", "version"]


def _v2_thresholds() -> dict:
    return json.loads(_V2_THRESHOLDS_FIXTURE.read_bytes())


def _v2_distinct(document: dict) -> dict:
    """Per-category test maxima ``(5 + i, 20 + i, 40 + i, 100)`` by catalog index."""
    index = {category: position for position, category in enumerate(FROZEN_MAGIC10_ORDER)}
    for entry in document["categories"]:
        offset = index[entry["category_id"]]
        entry["maxima"] = [5 + offset, 20 + offset, 40 + offset, 100]
    return document


def _v2_root(root: Path, document: object) -> Path:
    write_canonical(root / "math/thresholds.json", document)
    (root / "schemas").mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / _V2_SCHEMA, root / _V2_SCHEMA)
    return root


def _v2_expected(document: dict) -> dict:
    by_category = {entry["category_id"]: entry["maxima"] for entry in document["categories"]}
    return {
        "bands": ["Cool", "Open", "Warm", "Glow"],
        "categories": [{"category_id": category, "maxima": by_category[category]} for category in FROZEN_MAGIC10_ORDER],
        "schema": "band_edges.v2",
        "source": "math/thresholds.json",
        "version": "2",
    }


@pytest.mark.parametrize("distinct", [False, True], ids=["fixture", "distinct-maxima"])
def test_v2_band_edges_have_the_exact_shape(writer_root, distinct) -> None:
    document = _v2_distinct(_v2_thresholds()) if distinct else _v2_thresholds()
    result = artifact_tools.build_band_edges(_v2_root(writer_root, document))
    assert sorted(result) == _V2_KEYS
    assert result == _v2_expected(document)
    assert artifact_tools.BAND_EDGES_V2_SCHEMA == "band_edges.v2"
    assert all(list(entry) == ["category_id", "maxima"] for entry in result["categories"])


def test_v2_band_edges_follow_catalog_order_not_input_order(writer_root) -> None:
    document = _v2_distinct(_v2_thresholds())
    document["categories"].reverse()
    assert [entry["category_id"] for entry in document["categories"]] != list(FROZEN_MAGIC10_ORDER)
    result = artifact_tools.build_band_edges(_v2_root(writer_root, document))
    assert [entry["category_id"] for entry in result["categories"]] == list(FROZEN_MAGIC10_ORDER)
    assert result == _v2_expected(document)


def test_v2_band_edges_are_two_run_identical(writer_root) -> None:
    root = _v2_root(writer_root, _v2_distinct(_v2_thresholds()))
    first = canon.sercanon(artifact_tools.build_band_edges(root), sort_keys=True)
    second = canon.sercanon(artifact_tools.build_band_edges(root), sort_keys=True)
    assert first == second


def _v2_mutate(change):
    document = _v2_distinct(_v2_thresholds())
    change(document)
    return document


def _v2_v1_shaped(document: dict) -> None:
    document.clear()
    document.update({"clamp": [0, 100], "edges": [24, 49, 74, 100], "rounding": "ROUND_HALF_UP", "version": "2"})


_V2_REFUSALS = {
    "not-ascending": (lambda d: d["categories"][0].__setitem__("maxima", [49, 24, 74, 100]), "M10V2_MAXIMA_NOT_ASCENDING"),
    "equal-neighbours": (lambda d: d["categories"][1].__setitem__("maxima", [24, 24, 74, 100]), "M10V2_MAXIMA_NOT_ASCENDING"),
    "not-ending-at-100": (lambda d: d["categories"][0].__setitem__("maxima", [24, 49, 74, 99]), "M10V2_SCHEMA_VALIDATION_FAILED"),
    "missing-category": (lambda d: d["categories"].pop(), "M10V2_SCHEMA_VALIDATION_FAILED"),
    "duplicated-category": (lambda d: d["categories"].__setitem__(9, copy.deepcopy(d["categories"][0])), "M10V2_SCHEMA_VALIDATION_FAILED"),
    "extra-key": (lambda d: d.__setitem__("clamp", [0, 100]), "M10V2_SCHEMA_VALIDATION_FAILED"),
    "extra-category-key": (lambda d: d["categories"][0].__setitem__("note", "x"), "M10V2_SCHEMA_VALIDATION_FAILED"),
    "bool-maximum": (lambda d: d["categories"][0]["maxima"].__setitem__(0, True), "M10V2_SCHEMA_VALIDATION_FAILED"),
    "float-maximum": (lambda d: d["categories"][0]["maxima"].__setitem__(0, 5.5), "M10V2_SCHEMA_VALIDATION_FAILED"),
    "v1-shape-at-version-2": (_v2_v1_shaped, "M10V2_SCHEMA_VALIDATION_FAILED"),
    "unknown-version": (lambda d: d.__setitem__("version", "3"), "INVALID_THRESHOLDS"),
}


@pytest.mark.parametrize("case", sorted(_V2_REFUSALS))
def test_v2_band_edges_refuse_an_invalid_document(writer_root, case) -> None:
    change, code = _V2_REFUSALS[case]
    document = _v2_mutate(change)
    root = _v2_root(writer_root, document)
    with pytest.raises(_V2SchemaValidationError) as caught:
        artifact_tools.build_band_edges(root)
    assert caught.value.code == code
    # The refusal names a rule, a path or a category, never a maxima value.
    assert all(isinstance(value, str) for value in caught.value.details.values())
    shown = str(caught.value) + json.dumps(caught.value.details, sort_keys=True)
    for entry in document.get("categories", ()):
        assert json.dumps(entry.get("maxima")) not in shown
    assert "[" not in str(caught.value) and "99" not in shown and "5.5" not in shown


def test_v2_band_edges_are_written_by_the_existing_writer(writer_root) -> None:
    document = _v2_distinct(_v2_thresholds())
    root = _v2_root(writer_root, document)
    target = artifact_tools.write_band_edges(root)
    assert target == root / "artifacts/thresholds/band_edges.json"
    assert target.read_bytes() == canon.sercanon(_v2_expected(document), sort_keys=True)
