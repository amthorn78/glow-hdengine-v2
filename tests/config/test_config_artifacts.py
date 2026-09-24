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


# ---------------------------------------------------------------------------
# HDE-EPIC040-PR05: the PF01 §9.5 golden collection and its read-only
# comparator.  Every positive run admits the synthetic complete release from an
# isolated copy through the private fixture seam; nothing here relaxes
# admission or touches the repository tree.  These tests live in the config
# tooling's registered owner module so a change to ``tools/config/artifacts.py``
# or ``generate_config_artifacts.py`` always runs them.
# ---------------------------------------------------------------------------

import ast
import copy
import hashlib
import subprocess

from ci.checks import classify_ci_changes as classifier
from engine.compat import compute
from engine.config.registry_loader import _load_active_mechanics_bundle_from_root
from engine.narratives import loader as narrative_loader
from engine.narratives import router as narrative_router
from engine.narratives import state as narrative_state
from engine.serializer.canon import sercanon
from tests.config.helpers import synthetic_complete_release_root
from tools.evidence import update_evidence_index as updater

ROOT = Path(__file__).resolve().parents[2]
GOLDENS = ROOT / "tests/fixtures/magic10/v1/goldens.json"
CLOSED_RAILS = {"LC_ALL": "C", "LANG": "C", "TZ": "UTC", "SAFE_MODE": "1", "ALLOW_NETWORK": "0"}
# PF01 v1.3.7 §9.5 literals (the same values tests/compat/test_evaluate_pair_eligibility.py pins).
G007_READER_HASH = "8214324eb0129ff1dc213a5d53bd9d7b3758a351032c5258f7ba28eace7adc15"
G008_FINGERPRINT = "7567338a3be5b35e00366bfe86f3f1ca8b89be1fd02be893abeb62a60dbc2d2b"
G008_PAIR_KEY = "8a75eafcc4af664e073c1c4daec55f073f416af2c461039539f01717ac01d501"
G008_READER_HASH = "ae435ccc1f9d2043b4ee825f48c54ea421276d49d159b19271e46b24c04f2f6e"
G004_Q = [25, 63, 0, 38, 40, 20, 0, 25, 50, 38, 50, 0, 0, 0, 50, 20, 0, 60, 0, 33]
G004_SCORES = [22, 10, 15, 6, 22, 13, 0, 18, 15, 8]
G002_SCORES = [100, 50, 75, 100, 100, 100, 50, 63, 50, 50]
G002_BANDS = ["Glow", "Warm", "Glow", "Glow", "Glow", "Glow", "Warm", "Warm", "Warm", "Warm"]
FORBIDDEN_NAMES = {
    "write_magic10_config", "write_band_edges", "_publish_prepared", "generate_config_artifacts",
    "publish_config_family", "generate_catalog_logs", "check_config_artifacts", "_ConfigWriteTransaction",
    "update_evidence_index", "_publish_staged", "cut_release_manifest", "_BUNDLE_PROVIDER", "_PACK",
    "route_keys", "get_pack", "load_pack",
}


@pytest.fixture(scope="module")
def bundle_root(tmp_path_factory) -> Path:
    return synthetic_complete_release_root(tmp_path_factory.mktemp("pr05-goldens"))


@pytest.fixture(scope="module")
def bundle(bundle_root):
    return _load_active_mechanics_bundle_from_root(bundle_root)


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
    assert document["schema"] == artifact_tools.GOLDENS_SCHEMA
    assert [case["case_id"] for case in document["cases"]] == list(artifact_tools.GOLDEN_CASE_IDS)
    for case_id, case_type, kind in artifact_tools.GOLDEN_CASE_TABLE:
        case = _case(document, case_id)
        assert (case["case_type"], case["kind"]) == (case_type, kind)
    constants = document["constants"]
    assert constants["release_id"] == "a" * 64 and constants["config_id"] == "m10-channel-state-v1.0.0"
    assert constants["meta"] == {"engine_tag": "m10-test", "invocation_tag": "m10-identity-boundary"}
    assert constants["uuid_1"] == "00000000-0000-0000-0000-000000000001"
    assert constants["uuid_2"] == "00000000-0000-0000-0000-000000000002"
    g004 = _case(document, "M10-G004")
    assert g004["inputs"] == {"member_a_gates": [5, 19, 20, 34, 43, 49], "member_b_gates": [9, 12, 15, 22, 23, 52]}
    assert [row["q"] for row in g004["expected"]["signals"]] == G004_Q
    assert [row["score"] for row in g004["expected"]["categories"]] == G004_SCORES
    assert {row["band"] for row in g004["expected"]["categories"]} == {"Cool"}
    active = {row["channel_id"]: (row["state"], row["owner"]) for row in g004["expected"]["channel_states"] if row["state"] != "none"}
    assert active == {"05-15": ("electromagnetic", None), "09-52": ("dominance", "member_hi"), "12-22": ("dominance", "member_hi"),
                      "19-49": ("dominance", "member_lo"), "20-34": ("dominance", "member_lo"), "23-43": ("electromagnetic", None)}
    g002 = _case(document, "M10-G002")
    assert [row["score"] for row in g002["expected"]["categories"]] == G002_SCORES
    assert [row["band"] for row in g002["expected"]["categories"]] == G002_BANDS
    assert len(g002["inputs"]["channel_states"]) == 36 and {row["state"] for row in g002["inputs"]["channel_states"]} == {"companionship"}
    g006 = _case(document, "M10-G006")
    assert [(row["score"], row["band"]) for row in g006["expected"]["results"]] == [
        (24, "Cool"), (25, "Open"), (49, "Open"), (50, "Warm"), (74, "Warm"), (75, "Glow"), (100, "Glow")]
    g007 = _case(document, "M10-G007")
    assert g007["expected"]["reader"]["idempotence_hash"] == G007_READER_HASH
    assert g007["expected"]["evaluate_pair_result"] == {"categories": [], "eligible": False}
    g008 = _case(document, "M10-G008")
    assert g008["expected"]["pair_key_under_release"] == {"config_id": "m10-channel-state-v1.0.0", "release_id": "a" * 64, "pair_key": G008_PAIR_KEY}
    assert {row["chart_fingerprint"] for row in g008["expected"]["members"]} == {G008_FINGERPRINT}
    assert g008["expected"]["reader"]["idempotence_hash"] == G008_READER_HASH
    assert g008["expected"]["reader"]["categories"] == [{"id": "harmony", "band": "Cool"}]
    for case in document["cases"]:
        assert case["input_provenance"] and set(case["input_provenance"]) <= artifact_tools._GOLDEN_PROVENANCE_TAGS
        assert case["realizable_chart_claim"] in (True, False, None)


# --- positive comparison ----------------------------------------------------------------

def test_positive_comparison_matches_all_eight_cases(bundle_root, bundle) -> None:
    result = artifact_tools.compare_goldens(bundle_root, GOLDENS)
    assert result.ok is True and result.mismatches == ()
    assert [(row.case_id, row.outcome) for row in result.cases] == [(case_id, "match") for case_id in artifact_tools.GOLDEN_CASE_IDS]
    assert result.candidate_release_id == bundle.release_id and result.config_id == "m10-channel-state-v1.0.0"
    assert result.goldens_sha256 == hashlib.sha256(GOLDENS.read_bytes()).hexdigest()
    observed = {row.case_id: row.observed for row in result.cases}
    assert [row["q"] for row in observed["M10-G004"]["signals"]] == G004_Q
    assert [row["state"] for row in observed["M10-G004"]["channel_states"]].count("none") == 30
    assert observed["M10-G007"]["evaluate_pair_result"] == {"categories": [], "eligible": False}
    assert observed["M10-G007"]["adverse"][0]["token"] == "ERR_READER_INVALID_CHART"
    assert observed["M10-G008"]["pair_key_under_release"]["pair_key"] == G008_PAIR_KEY
    assert observed["M10-G008"]["reader"]["idempotence_hash"] == G008_READER_HASH
    assert observed["M10-G005"]["pair_key_equal_across_pairs"] is True
    assert observed["M10-G003"]["scenarios"][0] == {"scenario_id": "split_3_3", "q": 200, "q_owners_swapped": 200}
    assert observed["M10-G006"]["results"][3] == {"q": [100, 100], "score": 50, "band": "Warm"}
    for row in result.cases:
        assert sercanon(row.observed) == sercanon(row.expected)


# --- every mismatch is reported ---------------------------------------------------------

def _alter(document: dict, case_id: str, mutate) -> None:
    mutate(_case(document, case_id))


ALTERATIONS = {
    "g004_signal_q": ("M10-G004", lambda case: case["expected"]["signals"][1].__setitem__("q", 64), {"expected.signals[1].q"}),
    "g002_category_order": ("M10-G002", lambda case: case["expected"]["categories"].__setitem__(slice(0, 2), case["expected"]["categories"][0:2][::-1]),
                            {"expected.categories[0].category_id", "expected.categories[0].score", "expected.categories[0].band",
                             "expected.categories[1].category_id", "expected.categories[1].score", "expected.categories[1].band"}),
    "g008_reader_hash_byte": ("M10-G008", lambda case: case["expected"]["reader"].__setitem__("idempotence_hash", "0" + G008_READER_HASH[1:]),
                              {"expected.reader.idempotence_hash"}),
    "g008_identity_flip": ("M10-G008", lambda case: case["inputs"]["b"].__setitem__("person_uid", "00000000-0000-0000-0000-000000000000"),
                           {"expected.members[1].person_uid", "expected.orientation.hi", "expected.orientation.lo"}),
    "g007_reader_hash": ("M10-G007", lambda case: case["expected"]["reader"].__setitem__("idempotence_hash", "f" * 64), {"expected.reader.idempotence_hash"}),
    "g006_score": ("M10-G006", lambda case: case["expected"]["results"][0].__setitem__("band", "Open"), {"expected.results[0].band"}),
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
    for name in ("g004_signal_q", "g008_reader_hash_byte", "g007_reader_hash", "g006_score"):
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


def _document_unknown() -> dict:
    document = _document()
    extra = copy.deepcopy(_case(document, "M10-G001"))
    extra["case_id"] = "M10-G009"
    document["cases"].append(extra)
    return document


def _document_relabeled() -> dict:
    document = _document()
    _case(document, "M10-G004")["case_type"] = "application"
    _case(document, "M10-G004")["kind"] = "evaluate_pair"
    return document


def _document_unknown_top_key() -> dict:
    document = _document()
    document["extra"] = True
    return document


def _document_unknown_case_key() -> dict:
    document = _document()
    _case(document, "M10-G002")["comment"] = "x"
    return document


def _document_bad_provenance() -> dict:
    document = _document()
    _case(document, "M10-G002")["input_provenance"] = ["invented"]
    return document


@pytest.mark.parametrize(
    ("build", "code"),
    [
        (lambda: _document_without("M10-G006"), "GOLDENS_MEMBERSHIP_INVALID"),
        (lambda: _document_duplicating("M10-G003"), "GOLDENS_MEMBERSHIP_INVALID"),
        (_document_unknown, "GOLDENS_MEMBERSHIP_INVALID"),
        (_document_relabeled, "GOLDENS_CASE_TYPE_INVALID"),
        (_document_unknown_top_key, "GOLDENS_INVALID"),
        (_document_unknown_case_key, "GOLDENS_INVALID"),
        (_document_bad_provenance, "GOLDENS_INVALID"),
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
        (lambda: b'{"schema":"magic10_goldens.v1","schema":"magic10_goldens.v1"}\n', "duplicate_key"),
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


def test_admission_refusals_are_never_equality(tmp_path) -> None:
    incomplete = synthetic_complete_release_root(tmp_path / "incomplete")
    manifest = json.loads((incomplete / "catalog/manifest.json").read_bytes())
    manifest["files"] = manifest["files"][:-1]
    write_canonical(incomplete / "catalog/manifest.json", manifest)
    assert _refusal(incomplete, GOLDENS) == "CANDIDATE_ADMISSION_REFUSED:INCOMPLETE_RELEASE_ROSTER"

    tampered = synthetic_complete_release_root(tmp_path / "tampered")
    member = tampered / "tools/bodygraph/check_magic10_gate_readiness.py"
    member.write_bytes(member.read_bytes() + b"# changed after the manifest was cut\n")
    assert _refusal(tampered, GOLDENS) == "CANDIDATE_ADMISSION_REFUSED:MANIFEST_MEMBER_HASH_MISMATCH"

    # The repository root on main is the F01 interval's truthful result, not a golden mismatch.
    assert _refusal(ROOT, GOLDENS) == "CANDIDATE_ADMISSION_REFUSED:INCOMPLETE_RELEASE_ROSTER"


def test_candidate_root_must_be_a_real_directory(bundle_root, tmp_path) -> None:
    assert _refusal(tmp_path / "missing", GOLDENS) == "CANDIDATE_ROOT_INVALID"
    file_root = tmp_path / "file"
    file_root.write_bytes(b"x\n")
    assert _refusal(file_root, GOLDENS) == "CANDIDATE_ROOT_INVALID"
    link = tmp_path / "link"
    link.symlink_to(bundle_root, target_is_directory=True)
    assert _refusal(link, GOLDENS) == "CANDIDATE_ROOT_INVALID"


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
    _alter(mismatch_document, *ALTERATIONS["g004_signal_q"][:2])
    mismatch_goldens = _write_document(tmp_path / "mismatch.json", mismatch_document)
    incomplete = synthetic_complete_release_root(tmp_path / "incomplete")
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
    assert [row["outcome"] for row in report["cases"]] == ["match"] * 8 and report["mismatches"] == []


def test_cli_mismatch_is_a_single_token_and_the_report_holds_every_mismatch(bundle_root, tmp_path, capfdbinary) -> None:
    document = _document()
    for name in ("g004_signal_q", "g007_reader_hash"):
        _alter(document, *ALTERATIONS[name][:2])
    goldens = _write_document(tmp_path / "mismatch.json", document)
    report_path = tmp_path / "out" / "report.json"
    report_path.parent.mkdir()
    code, out, err = _run_cli(["--compare-goldens", str(bundle_root), "--goldens", str(goldens), "--report", str(report_path)], capfdbinary)
    assert (code, out) == (config_tools.GOLDEN_COMPARISON_MISMATCH_EXIT_CODE, b"")
    assert err == b"GOLDEN_COMPARISON_MISMATCH:2\n"
    report = json.loads(report_path.read_bytes())
    assert report["ok"] is False and {(row["case_id"], row["path"]) for row in report["mismatches"]} == {
        ("M10-G004", "expected.signals[1].q"), ("M10-G007", "expected.reader.idempotence_hash")}
    assert report_path.read_bytes() == artifact_tools.render_golden_report(artifact_tools.compare_goldens(bundle_root, goldens))


def test_cli_match_report_file_and_determinism(bundle_root, tmp_path, capfdbinary) -> None:
    report_path = tmp_path / "match.json"
    code, out, _ = _run_cli(["--compare-goldens", str(bundle_root), "--report", str(report_path)], capfdbinary)
    assert code == 0 and report_path.read_bytes() == out
    second, out_two, _ = _run_cli(["--compare-goldens", str(bundle_root)], capfdbinary)
    assert second == 0 and out_two == out
    other_root = synthetic_complete_release_root(tmp_path / "other")
    third, out_three, _ = _run_cli(["--compare-goldens", str(other_root)], capfdbinary)
    first_report, third_report = json.loads(out), json.loads(out_three)
    assert third == 0 and first_report.pop("candidate_root") != third_report.pop("candidate_root")
    assert first_report == third_report


@pytest.mark.parametrize("target", ["candidate", "repository"])
def test_cli_report_path_inside_candidate_or_repository_refuses(bundle_root, tmp_path, capfdbinary, target) -> None:
    report_path = (bundle_root / "report.json") if target == "candidate" else (ROOT / "tests/fixtures/magic10/v1/report.json")
    code, out, err = _run_cli(["--compare-goldens", str(bundle_root), "--report", str(report_path)], capfdbinary)
    assert (code, out, err) == (config_tools.GOLDEN_COMPARISON_REFUSAL_EXIT_CODE, b"", b"REPORT_PATH_INVALID\n")
    assert not report_path.exists()


def test_cli_refusals_and_usage(bundle_root, tmp_path, capfdbinary, monkeypatch) -> None:
    code, out, err = _run_cli(["--compare-goldens", str(ROOT)], capfdbinary)
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
