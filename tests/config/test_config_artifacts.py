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
# comparator.  Since HDE-EPIC043 WU-PR-09 the comparator reads the Magic10 v2
# collection (tests/fixtures/magic10/v2/goldens.json) and every positive run
# admits a labelled synthetic v2 candidate root from an isolated copy through
# the test-only roster route in tests/config/helpers.py; nothing here relaxes
# admission or touches the repository tree.  These tests live in the config
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
# PF01 §9.5 (Magic10 v2): M10-G001, no Channel and two Reflectors, is the one canon v2
# value before the cut: every category scores 0, band Cool.  The candidate's maxima are a
# labelled non-canon fixture and are asserted nowhere as canon.
G001_CATEGORIES = [{"category_id": category, "score": 0, "band": "Cool"} for category in FROZEN_MAGIC10_ORDER]
FORBIDDEN_NAMES = {
    "write_magic10_config", "write_band_edges", "_publish_prepared", "generate_config_artifacts",
    "publish_config_family", "generate_catalog_logs", "check_config_artifacts", "_ConfigWriteTransaction",
    "update_evidence_index", "_publish_staged", "cut_release_manifest", "_BUNDLE_PROVIDER", "_PACK",
    "route_keys", "get_pack", "load_pack",
}


@pytest.fixture(scope="module")
def _candidate_root(tmp_path_factory) -> Path:
    return synthetic_v2_candidate_root(tmp_path_factory.mktemp("pr05-goldens"))


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
    # Before the cut the v2 collection holds M10-G001 only (WU-PR-10 adds M10-G002 to M10-G008).
    assert [(case["case_id"], case["case_type"], case["kind"]) for case in document["cases"]] == [
        ("M10-G001", "calculation", "category_vector")]
    assert document["constants"] == {"config_id": "m10-relevance-centers-type-v2.0.0", "release_id": "a" * 64}
    g001 = _case(document, "M10-G001")
    assert g001["inputs"] == {"gates_a": [1], "gates_b": [2]}
    assert g001["expected"] == {"categories": G001_CATEGORIES}
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
    assert [row.outcome for row in result.cases] == ["match"]


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
    for row in observed["M10-G001"]["categories"]:
        assert row["band"] == assign_band(row["score"], bundle.magic10_v2.maxima[row["category_id"]])
    for row in result.cases:
        assert sercanon(row.observed) == sercanon(row.expected)


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


# A gate list the core's members cannot be built from is reported at its input path; a core
# that raises is the case's execution mismatch.  Neither aborts the comparison.
UNRUNNABLE = {
    "g001_invalid_gate": ("M10-G001", lambda case: case["inputs"].__setitem__("gates_a", [0]), None,
                          ("inputs.gates_a", "normalized Gate list", "GATE_VALUE_INVALID")),
    "g001_duplicate_gate": ("M10-G001", lambda case: case["inputs"].__setitem__("gates_b", [2, 2]), None,
                            ("inputs.gates_b", "normalized Gate list", "GATE_DUPLICATE")),
    "g001_no_gates": ("M10-G001", lambda case: case["inputs"].__setitem__("gates_a", []), None,
                      ("inputs.gates_a", "normalized Gate list", "GATES_EMPTY")),
    "g001_core_raises": ("M10-G001", lambda case: None, _failing_core,
                         ("execution", "completed", "ValueError: core refused")),
}


@pytest.mark.parametrize("name", sorted(UNRUNNABLE))
def test_a_case_that_cannot_execute_is_its_own_mismatch_never_a_crash(bundle_root, tmp_path, capfdbinary, monkeypatch, name) -> None:
    from engine.core import core as engine_core

    case_id, mutate, core, (path, expected, actual) = UNRUNNABLE[name]
    if core is not None:
        monkeypatch.setattr(engine_core, "compute_core", core)
    document = _document()
    _alter(document, case_id, mutate)
    goldens = _write_document(tmp_path / f"{name}.json", document)
    result = artifact_tools.compare_goldens(bundle_root, goldens)
    assert result.ok is False
    assert [(row.case_id, row.path, row.expected, row.actual) for row in result.mismatches] == [(case_id, path, expected, actual)]
    assert [row.case_id for row in result.cases if row.outcome == "mismatch"] == [case_id]
    code, out, err = _run_cli(["--compare-goldens", str(bundle_root), "--goldens", str(goldens)], capfdbinary)
    assert (code, out, err) == (config_tools.GOLDEN_COMPARISON_MISMATCH_EXIT_CODE, b"", b"GOLDEN_COMPARISON_MISMATCH:1\n")


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
UNCONSUMED_INPUTS = {
    "g001_gate_row_object": ("M10-G001", _setter("inputs", "gates_a", value=[{"gate": 1, "extra": 1}]), "inputs.gates_a"),
    "g001_gate_row_list": ("M10-G001", _setter("inputs", "gates_b", value=[[2]]), "inputs.gates_b"),
    "g001_gates_object": ("M10-G001", _setter("inputs", "gates_b", value={"extra": 1, "gates": [2]}), "inputs.gates_b"),
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


@pytest.mark.parametrize(
    ("build", "code"),
    [
        (lambda: _document_without("M10-G001"), "GOLDENS_INVALID"),
        (lambda: _document_duplicating("M10-G001"), "GOLDENS_MEMBERSHIP_INVALID"),
        (_document_relabeled, "GOLDENS_CASE_TYPE_INVALID"),
        (_document_unknown_kind, "GOLDENS_INVALID"),
        (_document_unknown_top_key, "GOLDENS_INVALID"),
        (_document_unknown_case_key, "GOLDENS_INVALID"),
        (_document_unknown_input_key, "GOLDENS_INVALID"),
        (_document_missing_input_key, "GOLDENS_INVALID"),
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

def test_executed_member_module_map_is_derived_from_the_roster(bundle) -> None:
    from engine.config.registry_loader import ADMITTED_RELEASE_ROSTER

    mapping = artifact_tools.golden_executed_member_modules(bundle)
    # Derived from the admitted candidate's manifest, not from the import-time roster constant.
    assert tuple(mapping) == tuple(row.path for row in bundle.manifest.files if row.path.endswith(".py"))
    assert tuple(mapping) == tuple(path for path in v2_candidate_roster() if path.endswith(".py"))
    assert "engine/magic10_v2/calculation.py" in mapping and "engine/magic10_v2/calculation.py" not in ADMITTED_RELEASE_ROSTER
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
    altered = synthetic_v2_candidate_root(tmp_path / "altered")
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
# compute._route routing, the router stub) and the consistently-altered-case pins: the v2
# comparator has one category_vector runner and no such pins.


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
    other_root = synthetic_v2_candidate_root(tmp_path / "other")
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


def test_v1_band_edges_bytes_are_unchanged() -> None:
    committed = (ROOT / "artifacts/thresholds/band_edges.json").read_bytes()
    assert len(committed) == 177
    assert canon.sercanon(artifact_tools.build_band_edges(), sort_keys=True) == committed
    assert json.loads(committed)["schema"] == "band_edges.v1"


def test_v2_band_edges_are_written_by_the_existing_writer(writer_root) -> None:
    document = _v2_distinct(_v2_thresholds())
    root = _v2_root(writer_root, document)
    target = artifact_tools.write_band_edges(root)
    assert target == root / "artifacts/thresholds/band_edges.json"
    assert target.read_bytes() == canon.sercanon(_v2_expected(document), sort_keys=True)
