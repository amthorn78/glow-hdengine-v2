import hashlib
import json
from pathlib import Path

import pytest

from tools.config.generate_bundles import expected_bundles


jsonschema = pytest.importorskip(
    "jsonschema",
    reason="jsonschema is required for config bundle schema validation; install from requirements-dev.txt",
)


ROOT = Path(__file__).resolve().parents[1].parent
FE_BUNDLE_PATH = ROOT / "artifacts" / "config_bundles" / "fe_bundle.json"
BE_BUNDLE_PATH = ROOT / "artifacts" / "config_bundles" / "be_bundle.json"


def _read_canonical(path: Path) -> dict:
    payload = path.read_text(encoding="utf-8")
    obj = json.loads(payload)
    expected = json.dumps(obj, sort_keys=True, separators=(",", ":")) + "\n"
    assert payload == expected
    return obj


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _expected_bundle_bytes() -> tuple[bytes, bytes]:
    expected = expected_bundles()
    return expected[FE_BUNDLE_PATH], expected[BE_BUNDLE_PATH]


def test_two_run_identity() -> None:
    fe_first, be_first = _expected_bundle_bytes()
    fe_second, be_second = _expected_bundle_bytes()
    assert fe_first == fe_second
    assert be_first == be_second


def test_bundle_check_mode_is_read_only() -> None:
    fe_before = FE_BUNDLE_PATH.read_bytes()
    be_before = BE_BUNDLE_PATH.read_bytes()
    fe_expected, be_expected = _expected_bundle_bytes()
    assert (fe_expected, be_expected) == (fe_before, be_before)
    assert FE_BUNDLE_PATH.read_bytes() == fe_before
    assert BE_BUNDLE_PATH.read_bytes() == be_before


def test_frontend_bundle_schema_and_sources() -> None:
    fe_bundle = _read_canonical(FE_BUNDLE_PATH)
    fe_schema = json.loads((ROOT / "docs" / "schemas" / "config_bundle_fe.json").read_text(encoding="utf-8"))
    jsonschema.validate(instance=fe_bundle, schema=fe_schema)

    magic10_config = _read_canonical(ROOT / "artifacts" / "thresholds" / "magic10_config.json")
    band_edges = _read_canonical(ROOT / "artifacts" / "thresholds" / "band_edges.json")
    registry_report = _read_canonical(ROOT / "artifacts" / "registry" / "registry_report.json")

    assert fe_bundle["magic10"]["order"] == magic10_config["order"]
    assert fe_bundle["magic10"]["caps"] == magic10_config["caps"]
    assert fe_bundle["bands"]["edges"] == band_edges["edges"]
    assert fe_bundle["bands"]["bands"] == band_edges["bands"]
    assert fe_bundle["channels"]["ids"] == registry_report["artifacts"]["registry"]["channel_ids"]

    for key, src in fe_bundle["sources"].items():
        artifact_path = ROOT / src["path"]
        assert artifact_path.exists()
        assert src["sha256"] == _sha256(artifact_path)
        assert src["size_bytes"] == artifact_path.stat().st_size


def test_backend_bundle_schema_and_sources() -> None:
    be_bundle = _read_canonical(BE_BUNDLE_PATH)
    be_schema = json.loads((ROOT / "docs" / "schemas" / "config_bundle_be.json").read_text(encoding="utf-8"))
    jsonschema.validate(instance=be_bundle, schema=be_schema)

    magic10_config = _read_canonical(ROOT / "artifacts" / "thresholds" / "magic10_config.json")
    band_edges = _read_canonical(ROOT / "artifacts" / "thresholds" / "band_edges.json")
    registry_report = _read_canonical(ROOT / "artifacts" / "registry" / "registry_report.json")

    assert be_bundle["magic10"] == magic10_config
    assert be_bundle["bands"] == band_edges

    registry_channels = registry_report["artifacts"]["registry"]["channel_ids"]
    assert [entry["id"] for entry in be_bundle["channels"]] == registry_channels
    assert be_bundle["domains"] == registry_report["artifacts"]["registry"]["domains"]
    assert be_bundle["centers"] == registry_report["artifacts"]["registry"]["centers"]
    assert be_bundle["alias_policy"] == registry_report["artifacts"]["registry"]["alias_policy"]

    for key, src in be_bundle["sources"].items():
        artifact_path = ROOT / src["path"]
        assert artifact_path.exists()
        assert src["sha256"] == _sha256(artifact_path)
        assert src["size_bytes"] == artifact_path.stat().st_size


from tests.config.helpers import catalog_root, closed_rails_env, write_canonical
from engine.config import bundles as bundle_tools
from tools.config import generate_config_artifacts as config_tools
from tools.config.generate_bundles import check_bundles


@pytest.fixture
def bundle_root(tmp_path, monkeypatch):
    for name in ("LC_ALL", "LANG", "TZ", "SAFE_MODE", "ALLOW_NETWORK"):
        monkeypatch.setenv(name, closed_rails_env()[name])
    root = catalog_root(tmp_path)
    config_tools.generate_config_artifacts(root)
    return root


def _bundle_state(root):
    return {path.relative_to(root).as_posix():
            (path.read_bytes(), path.stat().st_mode, path.stat().st_mtime_ns)
            for path in root.rglob("*") if path.is_file() and not path.is_symlink()}


def test_selected_root_bundles_preserve_complete_payload_and_schema_bytes(bundle_root) -> None:
    schemas = {name: (bundle_root / f"docs/schemas/config_bundle_{name}.json").read_bytes()
               for name in ("be", "fe")}
    # Domain-valid lower-level projection variation exposes payload/root leakage.
    threshold_path = bundle_root / "math/thresholds.json"
    thresholds = json.loads(threshold_path.read_bytes())
    thresholds["edges"] = [20, 40, 60, 100]
    write_canonical(threshold_path, thresholds)
    config_tools.generate_config_artifacts(bundle_root)
    outputs = bundle_tools.generate_bundles(bundle_root)
    be, fe = (json.loads(outputs[name].read_bytes()) for name in ("be_bundle", "fe_bundle"))
    assert be["bands"]["edges"] == fe["bands"]["edges"] == [20, 40, 60, 100]
    assert be["channels"] == json.loads((bundle_root / "catalog/channels_v1.json").read_bytes())["channels"]
    assert fe["channels"]["ids"] == [row["id"] for row in be["channels"]]
    assert set(fe["channels"]) == {"ids", "alias_policy", "domains", "centers"}
    for name, original in schemas.items():
        assert (bundle_root / f"docs/schemas/config_bundle_{name}.json").read_bytes() == original
    for payload in (be, fe):
        for source in payload["sources"].values():
            raw = (bundle_root / source["path"]).read_bytes()
            assert source["sha256"] == hashlib.sha256(raw).hexdigest()
            assert source["size_bytes"] == len(raw)
    before = _bundle_state(bundle_root)
    bundle_tools.generate_bundles(bundle_root)
    check_bundles(bundle_root)
    assert _bundle_state(bundle_root) == before


@pytest.mark.parametrize("relative", ["artifacts/registry/registry_report.json",
    "artifacts/thresholds/magic10_config.json", "artifacts/thresholds/band_edges.json"])
def test_bundle_refuses_stale_primary_without_laundering_digest(bundle_root, relative) -> None:
    target = bundle_root / relative
    data = json.loads(target.read_bytes())
    data["unexpected_stale_field"] = "stale"
    write_canonical(target, data)
    before = _bundle_state(bundle_root)
    with pytest.raises(RuntimeError, match="STALE_CONFIG_PRIMARY"):
        bundle_tools.generate_bundles(bundle_root)
    assert _bundle_state(bundle_root) == before
    assert not (bundle_root / "artifacts/config_bundles").exists()


def test_both_consumer_schemas_validate_before_first_write(bundle_root) -> None:
    from engine.config.registry_loader import RegistryConfigError

    target = bundle_root / "docs/schemas/config_bundle_fe.json"
    schema = json.loads(target.read_bytes())
    schema["required"].append("unavailable_field")
    # Existing consumer format remains pretty-printed and is accepted as such.
    target.write_text(json.dumps(schema, indent=2) + "\n")
    before = _bundle_state(bundle_root)
    with pytest.raises(RegistryConfigError):
        bundle_tools.generate_bundles(bundle_root)
    assert _bundle_state(bundle_root) == before
    assert not (bundle_root / "artifacts/config_bundles").exists()


@pytest.mark.parametrize("initially_present", [False, True])
def test_paired_bundle_replacement_restores_after_actual_first_write(bundle_root, monkeypatch, initially_present) -> None:
    from tools.evidence import update_evidence_index as updater

    if initially_present:
        bundle_tools.generate_bundles(bundle_root)
        # Retain known original bytes to prove the first changed write is recovered.
        for name in ("be_bundle", "fe_bundle"):
            (bundle_root / f"artifacts/config_bundles/{name}.json").write_bytes(b"old output\n")
    before = _bundle_state(bundle_root)
    original = updater._publish_staged
    calls = []

    def fail_second(payloads):
        if calls:
            raise RuntimeError("injected second bundle failure")
        original(payloads)
        calls.append(True)
        assert (bundle_root / "artifacts/config_bundles/be_bundle.json").read_bytes().startswith(b"{")

    monkeypatch.setattr(updater, "_publish_staged", fail_second)
    with pytest.raises(RuntimeError, match="second bundle"):
        bundle_tools.generate_bundles(bundle_root)
    assert calls
    assert _bundle_state(bundle_root) == before
    assert (bundle_root / "artifacts/config_bundles").exists() == initially_present
    assert updater._ACTIVE_WRITE_TRANSACTION is None


def test_bundle_check_refuses_missing_companion_without_writing(bundle_root) -> None:
    bundle_tools.generate_bundles(bundle_root)
    (bundle_root / "artifacts/config_bundles/fe_bundle.json").unlink()
    before = _bundle_state(bundle_root)
    with pytest.raises(SystemExit, match="STALE"):
        check_bundles(bundle_root)
    assert _bundle_state(bundle_root) == before


def test_bundle_captured_primary_race_restores_pair(bundle_root, monkeypatch) -> None:
    from tools.evidence import update_evidence_index as updater
    from engine.config.registry_loader import RegistryConfigError

    bundle_tools.generate_bundles(bundle_root)
    (bundle_root / "artifacts/config_bundles/be_bundle.json").write_bytes(b"prior bundle output\n")
    before = _bundle_state(bundle_root)
    source = bundle_root / "artifacts/thresholds/band_edges.json"
    original = updater._publish_staged
    called = []

    def change_after_replace(payloads):
        original(payloads)
        if not called:
            called.append(True)
            data = json.loads(source.read_bytes())
            data["edges"] = [20, 40, 60, 100]
            write_canonical(source, data)

    monkeypatch.setattr(updater, "_publish_staged", change_after_replace)
    with pytest.raises(RegistryConfigError, match="changed"):
        bundle_tools.generate_bundles(bundle_root)
    after = _bundle_state(bundle_root)
    for name in before:
        if name != "artifacts/thresholds/band_edges.json":
            assert after[name] == before[name]
    assert updater._ACTIVE_WRITE_TRANSACTION is None


@pytest.mark.parametrize("edited_name", ["be_bundle", "fe_bundle"])
@pytest.mark.parametrize("initially_present", [False, True])
def test_pair_rollback_preserves_concurrent_user_destination_edit(bundle_root, monkeypatch, edited_name, initially_present) -> None:
    """A refused mixed candidate must retain user bytes instead of clobbering them."""
    from tools.evidence import update_evidence_index as updater

    if initially_present:
        bundle_tools.generate_bundles(bundle_root)
        for name in ("be_bundle", "fe_bundle"):
            (bundle_root / f"artifacts/config_bundles/{name}.json").write_bytes(b"prior output\n")
    before = _bundle_state(bundle_root)
    user_target = bundle_root / f"artifacts/config_bundles/{edited_name}.json"
    original = updater._publish_staged
    observed = []

    def publish_then_user_edit(payloads):
        original(payloads)
        if not observed:
            assert (bundle_root / "artifacts/config_bundles/be_bundle.json").read_bytes().startswith(b"{")
            user_target.write_bytes(b"concurrent user content\n")
            user_target.chmod(0o640)
            observed.append((user_target.read_bytes(), user_target.stat().st_mode, user_target.stat().st_mtime_ns))

    monkeypatch.setattr(updater, "_publish_staged", publish_then_user_edit)
    with pytest.raises(RuntimeError, match="ROLLBACK_FAILED") as caught:
        bundle_tools.generate_bundles(bundle_root)
    assert caught.value.__cause__ is not None
    assert any("CONFLICT_PRESERVED" in note and edited_name in note for note in caught.value.__notes__)
    assert (user_target.read_bytes(), user_target.stat().st_mode, user_target.stat().st_mtime_ns) == observed[0]
    other_name = "fe_bundle" if edited_name == "be_bundle" else "be_bundle"
    other = bundle_root / f"artifacts/config_bundles/{other_name}.json"
    if initially_present:
        assert (other.read_bytes(), other.stat().st_mode, other.stat().st_mtime_ns) == before[other.relative_to(bundle_root).as_posix()]
    else:
        assert not other.exists()
    assert updater._ACTIVE_WRITE_TRANSACTION is None
    assert updater._STAGED_VIEW is None


@pytest.mark.parametrize("external_change", ["bytes", "mode"])
def test_postreplace_conflict_is_not_claimed_as_an_owned_write(bundle_root, monkeypatch, external_change) -> None:
    from tools.evidence import update_evidence_index as updater

    original = updater._record_transaction_write
    observed = []
    target = bundle_root / "artifacts/config_bundles/be_bundle.json"

    def intervene_before_receipt(path, **kwargs):
        if path == target and not observed:
            if external_change == "bytes":
                path.write_bytes(b"user changed bytes after replace\n")
            else:
                path.chmod(0o600)
            observed.append((path.read_bytes(), path.stat().st_mode, path.stat().st_mtime_ns))
        return original(path, **kwargs)

    monkeypatch.setattr(updater, "_record_transaction_write", intervene_before_receipt)
    with pytest.raises(RuntimeError, match="ROLLBACK_FAILED") as caught:
        bundle_tools.generate_bundles(bundle_root)
    assert "POSTIMAGE" in str(caught.value.__cause__)
    assert any("CONFLICT_PRESERVED" in note for note in caught.value.__notes__)
    assert (target.read_bytes(), target.stat().st_mode, target.stat().st_mtime_ns) == observed[0]
    assert not (bundle_root / "artifacts/config_bundles/fe_bundle.json").exists()
    assert updater._ACTIVE_WRITE_TRANSACTION is None


@pytest.mark.parametrize("changed_kind", ["source", "destination"])
def test_bundle_check_rechecks_sources_and_outputs_after_comparison(bundle_root, monkeypatch, changed_kind) -> None:
    from engine.config.registry_loader import RegistryConfigError
    from tools.config import generate_bundles as bundle_cli

    bundle_tools.generate_bundles(bundle_root)
    before = _bundle_state(bundle_root)
    target = bundle_root / ("math/thresholds.json" if changed_kind == "source"
                            else "artifacts/config_bundles/fe_bundle.json")
    original = bundle_cli._check_expected
    changed = []

    def compare_then_concurrent_change(base, expected):
        state = original(base, expected)
        values = json.loads(target.read_bytes())
        if changed_kind == "source":
            values["edges"] = [20, 40, 60, 100]
        else:
            values["bands"]["edges"] = [20, 40, 60, 100]
        write_canonical(target, values)
        changed.append(target.read_bytes())
        return state

    monkeypatch.setattr(bundle_cli, "_check_expected", compare_then_concurrent_change)
    error = RegistryConfigError if changed_kind == "source" else RuntimeError
    with pytest.raises(error, match="changed|CHANGED"):
        bundle_cli.check_bundles(bundle_root)
    assert target.read_bytes() == changed[0]
    after = _bundle_state(bundle_root)
    for name, state in before.items():
        if name != target.relative_to(bundle_root).as_posix():
            assert after[name] == state
