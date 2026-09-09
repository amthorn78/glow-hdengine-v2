import json
from pathlib import Path

from engine.categories.registry import FROZEN_MAGIC10_ORDER
from engine.magic10.thresholds import BANDS
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
    _, obj = _read_canonical(Path("artifacts/thresholds/band_edges.json"))
    assert obj["schema"] == "band_edges.v1"
    assert obj["bands"] == list(BANDS)
    edges = obj["edges"]
    assert edges == sorted(edges)
    assert len(edges) == len(obj["bands"])
    clamp = obj["clamp"]
    assert len(clamp) == 2
    assert clamp[0] <= clamp[1]
    assert edges[-1] == clamp[1]
    assert obj["rounding"] == "ROUND_HALF_UP"


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
    # This labels a legal lower-level domain fixture, not another initial mechanics config.
    path = writer_root / "math/thresholds.json"
    values = json.loads(path.read_bytes())
    values["edges"] = [20, 40, 60, 100]
    write_canonical(path, values)
    result = artifact_tools.build_band_edges(writer_root)
    assert result["edges"] == [20, 40, 60, 100]
    assert result["source"] == "math/thresholds.json"
    config_tools.generate_config_artifacts(writer_root)
    assert json.loads((writer_root / "artifacts/thresholds/band_edges.json").read_bytes()) == result


@pytest.mark.parametrize("bad", [True, 24.0, "24", -1])
def test_threshold_writer_does_not_coerce_numeric_types(writer_root, bad) -> None:
    from engine.config.registry_loader import RegistryConfigError

    path = writer_root / "math/thresholds.json"
    values = json.loads(path.read_bytes())
    values["edges"][0] = bad
    write_canonical(path, values)
    before = _file_state(writer_root)
    with pytest.raises(RegistryConfigError):
        config_tools.generate_config_artifacts(writer_root)
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
    changed["edges"] = [20, 40, 60, 100]
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


def test_catalog_logs_require_actual_initial_candidate_validation(writer_root) -> None:
    from engine.config.registry_loader import RegistryConfigError

    config_tools.generate_catalog_logs(writer_root)
    paths = [writer_root / name for name in config_tools._CATALOG_LOG_PATHS]
    before = _file_state(writer_root)
    for path in paths:
        body = path.read_text()
        assert "status: PASS" in body
        assert "catalog/channels_v1.json sha256=" in body
        assert "catalog/magic10_mechanics_v1.json sha256=" in body
    config_tools.generate_catalog_logs(writer_root, check=True)
    assert _file_state(writer_root) == before
    candidate = writer_root / "catalog/magic10_mechanics_v1.json"
    data = json.loads(candidate.read_bytes())
    data["config_id"] = "unapproved-config"
    write_canonical(candidate, data)
    before = _file_state(writer_root)
    with pytest.raises(RegistryConfigError):
        config_tools.generate_catalog_logs(writer_root)
    assert _file_state(writer_root) == before


def test_config_publication_refuses_another_root(writer_root) -> None:
    before = _file_state(writer_root)
    with pytest.raises(RuntimeError, match="ROOT_MISMATCH"):
        config_tools.publish_config_family(writer_root)
    assert _file_state(writer_root) == before


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
        values = json.loads(target.read_bytes())
        values["edges"] = [20, 40, 60, 100]
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
