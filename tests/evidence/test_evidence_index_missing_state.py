from __future__ import annotations

import json
import hashlib
import os
import shutil
import stat
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
IGNORES = shutil.ignore_patterns(
    ".git", ".mypy_cache", ".pytest_cache", ".ruff_cache", ".venv", "__pycache__"
)
ENV = {
    **os.environ,
    "ALLOW_NETWORK": "0",
    "APP_ENV": "dev",
    "LANG": "C",
    "LC_ALL": "C",
    "PYTHONDONTWRITEBYTECODE": "1",
    "SAFE_MODE": "1",
    "TZ": "UTC",
}
CRD_ROOT = "audit/qa/hde-crd-0001"
CRD_KEY = "audit.qa.hde_crd_0001"
CRD_FIXTURE_PROGRAM = '''
import json
import os
import subprocess
import sys
from pathlib import Path
from tools.evidence import update_evidence_index as writer
from tools.qa import qa_harness as qa

assert writer.ROOT == Path.cwd(), "fixture must import its own complete updater"
config = qa.HarnessConfig(crd_id="HDE-CRD-0001", repo_root=writer.ROOT)
timestamp = "2026-01-01T00:00:00Z"  # deterministic fixture timestamp, not live QA

def observed(check_id="current", *, fail=False):
    command = (sys.executable, "-c", "raise SystemExit(1)" if fail else "raise SystemExit(0)")
    completed = subprocess.run(command, capture_output=True, text=True, check=False)
    return qa.CheckResult(
        check_id, qa.Status.FAIL_BEHAVIOR if completed.returncode else qa.Status.PASS,
        status_reason="fixture command exited 1" if completed.returncode else "",
        command=command, command_provenance="executed child command in an isolated test repository",
        exit_code=completed.returncode, output=completed.stdout + completed.stderr,
    )

def publish(results=None, **kwargs):
    return writer.publish_crd_check_family(
        config, results if results is not None else (observed(),),
        captured_at_utc=timestamp, **kwargs,
    )
'''
SKELETON = (
    "docs/evidence/INDEX.json",
    "docs/evidence/INDEX.json.path_proof.txt",
    "docs/evidence/INDEX.sha256",
    "docs/evidence/INDEX.sha256.path_proof.txt",
    "artifacts/evidence_index.jsonl",
    "artifacts/evidence_index.jsonl.path_proof.txt",
    "artifacts/evidence_index.jsonl.sha256",
    "artifacts/evidence_index.jsonl.sha256.path_proof.txt",
    "audit/gates/topology/orientation_demo.txt",
    "audit/gates/topology/orientation_demo.txt.path_proof.txt",
)


def _run(repo: Path, relative: str, *args: str) -> subprocess.CompletedProcess[str]:
    command = [sys.executable, relative, *args]
    if relative.endswith("check_evidence_index_hash.sh"):
        command = [relative, *args]
    return subprocess.run(
        command,
        cwd=repo,
        env=ENV,
        capture_output=True,
        text=True,
        check=False,
    )


def _success(result: subprocess.CompletedProcess[str]) -> None:
    assert result.returncode == 0, result.stdout + result.stderr


def _checks(repo: Path) -> None:
    for command, args in (
        ("tools/evidence/update_evidence_index.py", ("--check",)),
        ("tools/evidence/orientation_demo.py", ("--check",)),
        ("ci/checks/check_mirror_schema.sh", ()),
        ("tools/evidence/validate_evidence_paths.py", ()),
        ("ci/checks/check_evidence_index_hash.sh", ()),
        ("tools/evidence/check_lf_endings.py", ()),
    ):
        _success(_run(repo, command, *args))


def _snapshot(repo: Path) -> dict[str, tuple[bytes, int]]:
    return {
        relative: (
            (repo / relative).read_bytes(),
            stat.S_IMODE((repo / relative).stat().st_mode),
        )
        for relative in SKELETON
        if (repo / relative).exists()
    }


def test_orientation_compatibility_write_is_idempotent_after_updater(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    shutil.copytree(ROOT, repo, copy_function=shutil.copy2, ignore=IGNORES)

    _success(_run(repo, "tools/evidence/update_evidence_index.py"))
    before = _snapshot(repo)
    _success(_run(repo, "tools/evidence/orientation_demo.py"))
    assert _snapshot(repo) == before
    _checks(repo)
    assert _snapshot(repo) == before


def test_updater_recovers_missing_governed_doc_delta_proof_in_one_write(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    shutil.copytree(ROOT, repo, copy_function=shutil.copy2, ignore=IGNORES)

    primary = repo / "audit/docdeltas/hde-epic039_doc_deltas.md"
    proof = repo / "audit/docdeltas/hde-epic039_doc_deltas.md.path_proof.txt"
    primary_before = (
        primary.read_bytes(),
        stat.S_IMODE(primary.stat().st_mode),
        primary.stat().st_mtime_ns,
    )
    proof.unlink()

    _success(_run(repo, "tools/evidence/update_evidence_index.py"))
    assert proof.is_file()
    assert (
        primary.read_bytes(),
        stat.S_IMODE(primary.stat().st_mode),
        primary.stat().st_mtime_ns,
    ) == primary_before

    entries = json.loads(
        (repo / "docs/evidence/INDEX.json").read_text(encoding="utf-8")
    )
    primary_entries = [
        entry
        for entry in entries
        if entry["discovered_physical_path"]
        == "audit/docdeltas/hde-epic039_doc_deltas.md"
    ]
    assert [entry["artifact_key"] for entry in primary_entries] == [
        "epic039.pr01.doc_delta"
    ]

    proof_before_checks = (
        proof.read_bytes(),
        stat.S_IMODE(proof.stat().st_mode),
    )
    _checks(repo)
    assert (
        proof.read_bytes(),
        stat.S_IMODE(proof.stat().st_mode),
    ) == proof_before_checks


def test_manifest_only_release_cut_stays_outside_the_evidence_graph(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    shutil.copytree(ROOT, repo, copy_function=shutil.copy2, ignore=IGNORES)

    manifest = repo / "catalog/manifest.json"
    historical_proof = repo / "catalog/manifest.json.path_proof.txt"
    manifest_before = manifest.read_bytes()
    proof_before = historical_proof.read_bytes()
    skeleton_before = _snapshot(repo)

    _success(
        _run(
            repo,
            "scripts/cut_release_manifest.py",
            "--version",
            "1.0.1",
            "--built-at-utc",
            "2026-08-20T00:00:00Z",
        )
    )
    assert manifest.read_bytes() != manifest_before
    assert historical_proof.read_bytes() == proof_before
    assert _snapshot(repo) == skeleton_before

    human_entries = json.loads(
        (repo / "docs/evidence/INDEX.json").read_text(encoding="utf-8")
    )
    mirror_entries = [
        json.loads(line)
        for line in (repo / "artifacts/evidence_index.jsonl")
        .read_text(encoding="utf-8")
        .splitlines()
        if line
    ]
    for entries in (human_entries, mirror_entries):
        assert not any(
            entry["discovered_physical_path"] == "catalog/manifest.json"
            for entry in entries
        )

    _checks(repo)
    assert _snapshot(repo) == skeleton_before
    assert historical_proof.read_bytes() == proof_before

    # HDE-CRD-0002 S12: no capture owner has rerun, so the updater publishes no
    # new-release label; every capture keeps the release that produced it.
    _success(_run(repo, "tools/evidence/update_evidence_index.py"))
    assert _snapshot(repo) == skeleton_before
    assert "release 1.0.1" not in (repo / "artifacts/evidence_index.jsonl").read_text(encoding="utf-8")
    _checks(repo)


def test_updater_recovers_complete_missing_state_in_one_write(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    shutil.copytree(ROOT, repo, copy_function=shutil.copy2, ignore=IGNORES)

    missing_families = (
        ("docs/evidence/INDEX.sha256",),
        ("docs/evidence/INDEX.sha256.path_proof.txt",),
        (
            "artifacts/evidence_index.jsonl",
            "artifacts/evidence_index.jsonl.path_proof.txt",
            "artifacts/evidence_index.jsonl.sha256",
            "artifacts/evidence_index.jsonl.sha256.path_proof.txt",
        ),
        (
            "audit/gates/topology/orientation_demo.txt",
            "audit/gates/topology/orientation_demo.txt.path_proof.txt",
        ),
    )
    for family in missing_families:
        original_modes = {
            relative: stat.S_IMODE((repo / relative).stat().st_mode)
            for relative in family
        }
        for relative in family:
            (repo / relative).unlink()
        _success(_run(repo, "tools/evidence/update_evidence_index.py"))
        assert all((repo / relative).is_file() for relative in family)
        assert {
            relative: stat.S_IMODE((repo / relative).stat().st_mode)
            for relative in family
        } == original_modes
        before_checks = _snapshot(repo)
        _checks(repo)
        assert _snapshot(repo) == before_checks

    # Check mode must fail without repairing a missing proof or changing any
    # other member of the governed skeleton.
    missing_proof = repo / "docs/evidence/INDEX.sha256.path_proof.txt"
    missing_proof.unlink()
    before_failed_check = _snapshot(repo)
    result = _run(repo, "tools/evidence/update_evidence_index.py", "--check")
    assert result.returncode != 0
    assert "MISSING_PROOF" in result.stdout + result.stderr
    assert _snapshot(repo) == before_failed_check
    assert not missing_proof.exists()
    _success(_run(repo, "tools/evidence/update_evidence_index.py"))

    # Exercise updater-owned membership addition and removal through the real
    # index-rendering path, rather than by calling the publication helper.
    index_path = repo / "docs/evidence/INDEX.json"
    entries = json.loads(index_path.read_text(encoding="utf-8"))
    added_key = (
        "registry.registry_report",
        "artifacts/registry/registry_report.json",
    )
    removed_key = (
        "epic031.pr02.keys_only_sample",
        "artifacts/logs/keys_only.sample.jsonl",
    )
    entries = [
        entry
        for entry in entries
        if (entry["artifact_key"], entry["discovered_physical_path"]) != added_key
    ]
    entries.append(
        {
            "artifact_key": removed_key[0],
            "discovered_physical_path": removed_key[1],
        }
    )
    index_path.write_text(
        json.dumps(entries, separators=(",", ":"), sort_keys=True) + "\n",
        encoding="utf-8",
    )

    _success(_run(repo, "tools/evidence/update_evidence_index.py"))
    final_entries = json.loads(index_path.read_text(encoding="utf-8"))
    final_keys = {
        (entry["artifact_key"], entry["discovered_physical_path"])
        for entry in final_entries
    }
    assert added_key in final_keys
    assert removed_key not in final_keys
    before_checks = _snapshot(repo)
    _checks(repo)
    assert _snapshot(repo) == before_checks


@pytest.fixture
def crd_repo(tmp_path: Path) -> Path:
    """Build the tests' coherent pre-first-publication state in a copy.

    The repository retains completed CRD evidence. That history must remain in
    the real checkout, while these tests need an absent CRD family before they
    exercise initial publication or deliberately construct an empty root.
    """
    repo = tmp_path / "repo"
    shutil.copytree(ROOT, repo, copy_function=shutil.copy2, ignore=IGNORES)
    retained_root = repo / CRD_ROOT
    if retained_root.exists():
        shutil.rmtree(retained_root)
    index = repo / "docs/evidence/INDEX.json"
    rows = json.loads(index.read_bytes())
    rows = [
        row for row in rows
        if not (
            row["discovered_physical_path"] == CRD_ROOT
            or row["discovered_physical_path"].startswith(CRD_ROOT + "/")
        )
    ]
    index.write_text(json.dumps(rows, sort_keys=True, separators=(",", ":")) + "\n")
    # Fixture construction changes its seed ledger only. The real owner then
    # regenerates the complete coherent skeleton and validates that state.
    _success(_run(repo, "tools/evidence/update_evidence_index.py"))
    _success(_run(repo, "tools/evidence/update_evidence_index.py", "--check"))
    return repo


def _crd_program(repo: Path, program: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-c", CRD_FIXTURE_PROGRAM + "\n" + program],
        cwd=repo, env=ENV, capture_output=True, text=True, check=False,
    )


def _whole_tree_state(repo: Path, *, metadata: bool = False) -> dict[str, tuple]:
    """Include every fixture file/parent, not just the global skeleton."""
    state = {}
    for path in (repo, *repo.rglob("*")):
        relative = path.relative_to(repo).as_posix()
        info = path.lstat()
        if path.is_symlink():
            content = ("symlink", os.readlink(path))
        elif path.is_file():
            content = ("file", hashlib.sha256(path.read_bytes()).hexdigest())
        else:
            content = ("directory",)
        state[relative] = (*content, stat.S_IMODE(info.st_mode), *((info.st_mtime_ns,) if metadata else ()))
    return state


def test_crd_governed_publication_binds_actual_records_and_is_repeatable(crd_repo):
    before = _whole_tree_state(crd_repo)
    _success(_run(crd_repo, "tools/evidence/update_evidence_index.py", "--check"))
    assert not (crd_repo / CRD_ROOT).exists()
    _success(_crd_program(crd_repo, '''
logs, manifest = publish((observed(), observed("retained", fail=True)))
assert logs == tuple(config.qa_root / "checks" / name / "primary.log" for name in ("current", "retained"))
assert manifest == config.qa_root / "qa_step_logs_manifest.json"
assert qa.validate_crd_check_family(config)["retained"]["status"] == "FAIL_BEHAVIOR"
'''))
    after = _whole_tree_state(crd_repo)
    # Historical primaries and unrelated proofs must not be rewritten.
    for path, prior in before.items():
        if prior[0] == "file" and path not in SKELETON:
            assert after[path] == prior, path
    entries = json.loads((crd_repo / "docs/evidence/INDEX.json").read_bytes())
    selected = [entry for entry in entries if entry["artifact_key"].startswith(CRD_KEY + ".")]
    expected_paths = {
        f"{CRD_ROOT}/qa_step_logs_manifest.json",
        f"{CRD_ROOT}/checks/current/primary.log", f"{CRD_ROOT}/checks/retained/primary.log",
    }
    assert {entry["discovered_physical_path"] for entry in selected} == expected_paths
    assert len(selected) == 3
    for entry in selected:
        assert set(entry) == {"artifact_key", "discovered_physical_path", "role"}
    mirror = [json.loads(line) for line in (crd_repo / "artifacts/evidence_index.jsonl").read_bytes().splitlines()]
    for path in expected_paths:
        row, = [row for row in mirror if row["discovered_physical_path"] == path]
        raw = (crd_repo / path).read_bytes()
        assert row["sha256"] == hashlib.sha256(raw).hexdigest()
        assert row["size_bytes"] == len(raw)
        assert row["proof_anchor"] == path + ".path_proof.txt"
        assert not {"tokens", "epic_id", "crd_id", "status"} & set(row)
        proof = dict(line.split(": ", 1) for line in (crd_repo / row["proof_anchor"]).read_text().splitlines())
        assert proof["sha256"] == row["sha256"]
        assert int(proof["size_bytes"]) == len(raw)
    _checks(crd_repo)
    _success(_crd_program(crd_repo, 'publish((observed(), observed("retained", fail=True)))'))
    assert _whole_tree_state(crd_repo) == after
    retained = (crd_repo / f"{CRD_ROOT}/checks/retained/primary.log").read_bytes()
    _success(_crd_program(crd_repo, 'publish((observed(fail=True),))'))
    manifest = json.loads((crd_repo / f"{CRD_ROOT}/qa_step_logs_manifest.json").read_bytes())
    assert manifest["current"]["status"] == "FAIL_BEHAVIOR"
    assert (crd_repo / f"{CRD_ROOT}/checks/retained/primary.log").read_bytes() == retained
    _checks(crd_repo)


def test_crd_current_manifest_reconciles_supersession_without_history_conversion(crd_repo):
    _success(_crd_program(crd_repo, 'publish()'))
    old_log = crd_repo / f"{CRD_ROOT}/checks/current/primary.log"
    old_bytes = old_log.read_bytes()
    _success(_crd_program(crd_repo, '''
qa.record_check(config, observed("replacement"), supersede_check_ids=("current",))
(config.qa_root / "unlisted.log").write_text("not admitted by discovery\\n")
other = writer.ROOT / "audit/qa/hde-crd-0003"
other.mkdir()
(other / "unlisted.log").write_text("no source-owned admission\\n")
writer.main([])
'''))
    assert old_log.read_bytes() == old_bytes
    entries = json.loads((crd_repo / "docs/evidence/INDEX.json").read_bytes())
    paths = {entry["discovered_physical_path"] for entry in entries}
    assert f"{CRD_ROOT}/checks/current/primary.log" not in paths
    assert f"{CRD_ROOT}/checks/replacement/primary.log" in paths
    assert f"{CRD_ROOT}/unlisted.log" not in paths
    assert "audit/qa/hde-crd-0003/unlisted.log" not in paths
    _checks(crd_repo)


@pytest.mark.parametrize("state", ["empty-root", "missing-indexed-root", "missing-primary", "malformed-manifest", "unrelated-broken-proof"])
def test_crd_publication_refuses_incoherent_prior_state_before_writes(crd_repo, state):
    if state in {"missing-indexed-root", "missing-primary", "malformed-manifest"}:
        _success(_crd_program(crd_repo, 'publish()'))
    if state == "empty-root":
        (crd_repo / CRD_ROOT).mkdir(parents=True)
    elif state == "missing-indexed-root":
        shutil.rmtree(crd_repo / CRD_ROOT)
    elif state == "missing-primary":
        (crd_repo / f"{CRD_ROOT}/checks/current/primary.log").unlink()
    elif state == "malformed-manifest":
        (crd_repo / f"{CRD_ROOT}/qa_step_logs_manifest.json").write_bytes(b"{}\n")
    else:
        (crd_repo / "docs/evidence/INDEX.sha256.path_proof.txt").unlink()
    before = _whole_tree_state(crd_repo, metadata=True)
    result = _crd_program(crd_repo, 'publish((observed("new"),))')
    assert result.returncode != 0
    assert "CRD" in result.stderr or "STALE_PROOF" in result.stderr or "MISSING_PROOF" in result.stderr
    assert _whole_tree_state(crd_repo, metadata=True) == before


@pytest.mark.parametrize("corruption", ["foreign-key", "foreign-path", "aliased-path", "legacy-alias", "tokens", "duplicate", "duplicate-json-key"])
def test_crd_index_admission_rejects_forgery_before_deduplication(crd_repo, corruption):
    _success(_crd_program(crd_repo, 'publish()'))
    index = crd_repo / "docs/evidence/INDEX.json"
    entries = json.loads(index.read_bytes())
    selected = next(entry for entry in entries if entry["artifact_key"].startswith(CRD_KEY + ".checks."))
    if corruption == "foreign-key":
        selected["artifact_key"] = "unrelated.forged"
    elif corruption == "foreign-path":
        selected["discovered_physical_path"] = "audit/qa/hde-crd-0002/checks/current/primary.log"
    elif corruption == "aliased-path":
        selected["artifact_key"] = "unrelated.forged"
        selected["discovered_physical_path"] = selected["discovered_physical_path"].replace("/qa/", "/./qa//")
    elif corruption == "legacy-alias":
        selected["title"] = selected.pop("artifact_key")
        selected["path"] = selected.pop("discovered_physical_path")
    elif corruption == "tokens":
        selected["tokens"] = []
    elif corruption == "duplicate":
        entries.append(dict(selected))
    raw = (json.dumps(entries, sort_keys=True, separators=(",", ":")) + "\n").encode()
    if corruption == "duplicate-json-key":
        needle = json.dumps(selected["artifact_key"]).encode()
        raw = raw.replace(b'"artifact_key":' + needle, b'"artifact_key":' + needle + b',"artifact_key":' + needle)
    index.write_bytes(raw)
    before = _whole_tree_state(crd_repo, metadata=True)
    result = _run(crd_repo, "tools/evidence/update_evidence_index.py")
    assert result.returncode != 0
    assert "CRD" in result.stderr or "duplicate" in result.stderr.lower()
    assert _whole_tree_state(crd_repo, metadata=True) == before


def test_crd_publication_refuses_foreign_scope_and_invalid_inputs(crd_repo):
    before = _whole_tree_state(crd_repo, metadata=True)
    _success(_crd_program(crd_repo, '''
cases = [
    (qa.HarnessConfig(crd_id="HDE-CRD-0003", repo_root=writer.ROOT), (observed(),)),
    (qa.HarnessConfig(crd_id="HDE-CRD-0001", repo_root=writer.ROOT / "tests"), (observed(),)),
    (config, ()), (config, (observed(), observed())), (config, (object(),)),
]
for selected, results in cases:
    try:
        writer.publish_crd_check_family(selected, results)
    except ValueError:
        pass
    else:
        raise AssertionError("unsafe publication was accepted")
'''))
    assert _whole_tree_state(crd_repo, metadata=True) == before


@pytest.mark.parametrize("existing", [False, True])
@pytest.mark.parametrize("failure", ["write", "final-verifier"])
def test_crd_outer_transaction_restores_all_files_and_parents(crd_repo, existing, failure):
    if existing:
        _success(_crd_program(crd_repo, 'publish()'))
        log = crd_repo / f"{CRD_ROOT}/checks/current/primary.log"
        log.chmod(0o640)
    before = _whole_tree_state(crd_repo, metadata=True)
    _success(_crd_program(crd_repo, f'''
failure_kind = {failure!r}
original_publish = writer._publish_staged
def fail_after_earlier_writes(staged):
    assert qa.validate_crd_check_family(config)["current"]["status"] == "FAIL_BEHAVIOR"
    targets = sorted(staged, key=lambda path: path.as_posix())
    assert len(targets) > 3
    original_publish({{path: staged[path] for path in targets[:-1]}})
    assert any(path in writer._ACTIVE_WRITE_TRANSACTION.files for path in targets[:-1])
    raise OSError("injected integrity write failure after actual earlier writes")

def fail_final():
    writer._run_once(check=True)
    rows = json.loads(writer.HUMAN_INDEX.read_bytes())
    assert any(row["discovered_physical_path"].endswith("checks/new/primary.log") for row in rows)
    assert writer._ACTIVE_WRITE_TRANSACTION is not None
    raise RuntimeError("injected final verifier failure after coherent publication")

if failure_kind == "write":
    writer._publish_staged = fail_after_earlier_writes
try:
    publish((observed(fail=True), observed("new")), coherence_verifier=fail_final if failure_kind == "final-verifier" else None)
except (OSError, RuntimeError) as exc:
    assert "injected" in str(exc), str(exc)
else:
    raise AssertionError("injected failure returned publication success")
assert writer._ACTIVE_WRITE_TRANSACTION is None
assert writer._STAGED_VIEW is None
writer._run_once(check=True)
'''))
    assert _whole_tree_state(crd_repo, metadata=True) == before
    _checks(crd_repo)
    assert _whole_tree_state(crd_repo, metadata=True) == before


def test_crd_rollback_failure_retains_original_cause_and_untrustworthy_state(crd_repo):
    _success(_crd_program(crd_repo, '''
original_rollback = writer._WriteTransaction.rollback
def failed_rollback(self):
    original_rollback(self)
    raise OSError("injected rollback diagnostic")
writer._WriteTransaction.rollback = failed_rollback
def reject():
    raise RuntimeError("original final verification failure")
try:
    publish(coherence_verifier=reject)
except RuntimeError as exc:
    assert str(exc) == "EVIDENCE_INDEX_TRANSACTION_ROLLBACK_FAILED"
    assert str(exc.__cause__) == "original final verification failure"
    assert any("injected rollback diagnostic" in note for note in exc.__notes__)
else:
    raise AssertionError("failed rollback was reported as success")
assert writer._ACTIVE_WRITE_TRANSACTION is None
assert writer._STAGED_VIEW is None
'''))



# Configuration publication uses its actual owners and the complete copied
# repository. These are transaction fixtures, not QA records or a CRD client.
CONFIG_LOGS = (
    "artifacts/catalog/catalog_schema_validation.log",
    "artifacts/catalog/domain_closure_report.log",
)
CONFIG_PROGRAM = '''
import json
from pathlib import Path
from tools.config import generate_config_artifacts as coordinator
from tools.evidence import update_evidence_index as writer
assert writer.ROOT == Path.cwd(), "fixture must import its own complete updater"
def publish():
    result = coordinator.main(["--publish-family"])
    assert result in (None, 0), result
'''


def _config_program(repo: Path, program: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-c", CONFIG_PROGRAM + "\n" + program],
        cwd=repo, env=ENV, capture_output=True, text=True, check=False,
    )


@pytest.fixture
def config_repo(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    shutil.copytree(ROOT, repo, copy_function=shutil.copy2, ignore=IGNORES)
    # The fixture must begin with an actual coherent owner-produced family.
    _success(_config_program(repo, "publish()"))
    return repo


def _remove_config_catalog_fixture(repo: Path) -> None:
    """Create a coherent pre-first-generation fixture, not production evidence."""
    index = repo / "docs/evidence/INDEX.json"
    rows = json.loads(index.read_bytes())
    rows = [row for row in rows if row["discovered_physical_path"] not in CONFIG_LOGS]
    index.write_text(json.dumps(rows, sort_keys=True, separators=(",", ":")) + "\n")
    for relative in CONFIG_LOGS:
        for path in (repo / relative, repo / (relative + ".path_proof.txt")):
            path.unlink()
    catalog_dir = repo / "artifacts/catalog"
    if not any(catalog_dir.iterdir()):
        catalog_dir.rmdir()
    # The existing generic owner binds this explicitly constructed historical
    # fixture; publication itself never strips records or uses this helper.
    _success(_run(repo, "tools/evidence/update_evidence_index.py"))
    _checks(repo)


def _prior_config_log_fixture(repo: Path) -> None:
    log = repo / CONFIG_LOGS[0]
    log.write_bytes(b"# Prior transaction test capture\n" + log.read_bytes())
    log.chmod(0o640)
    _success(_run(repo, "tools/evidence/update_evidence_index.py"))


def test_config_family_publication_converges_and_preserves_unrelated_history(config_repo):
    _remove_config_catalog_fixture(config_repo)
    before = _whole_tree_state(config_repo, metadata=True)
    index_before = json.loads((config_repo / "docs/evidence/INDEX.json").read_bytes())
    mirror_before = [json.loads(line) for line in (config_repo / "artifacts/evidence_index.jsonl").read_bytes().splitlines()]
    _success(_config_program(config_repo, "publish()"))
    after = _whole_tree_state(config_repo, metadata=True)
    _success(_config_program(config_repo, '''
import hashlib
rows = json.loads(writer.HUMAN_INDEX.read_bytes())
mirror = [json.loads(line) for line in writer.MIRROR_PATH.read_bytes().splitlines()]
expected = tuple(writer.CATALOG_VALIDATION_ENTRIES)
for entry in expected:
    selected = [row for row in rows if row["artifact_key"] == entry["artifact_key"]]
    assert [writer._strip_current_release_label(row) for row in selected] == [entry]
    assert selected[0]["notes"].startswith("current-release capture: release ")
    selected_mirror, = [row for row in mirror if row["artifact_key"] == entry["artifact_key"]]
    path = writer.ROOT / entry["discovered_physical_path"]
    assert path.is_file() and path.read_bytes()
    assert selected_mirror["sha256"] == hashlib.sha256(path.read_bytes()).hexdigest()
    assert selected_mirror["size_bytes"] == len(path.read_bytes())
    assert selected_mirror["proof_anchor"] == entry["discovered_physical_path"] + ".path_proof.txt"
    assert not {"tokens", "status", "acceptance_token_satisfied"} & set(selected_mirror)
for relative in writer.CONFIG_PRIMARY_PATHS - {"catalog/manifest.json"}:
    selected = [row for row in mirror if row["discovered_physical_path"] == relative]
    assert selected, relative
    raw = (writer.ROOT / relative).read_bytes()
    for row in selected:
        assert row["sha256"] == hashlib.sha256(raw).hexdigest()
        assert row["size_bytes"] == len(raw)
        assert row["proof_anchor"] == relative + ".path_proof.txt"
'''))
    index_after = json.loads((config_repo / "docs/evidence/INDEX.json").read_bytes())
    mirror_after = [json.loads(line) for line in (config_repo / "artifacts/evidence_index.jsonl").read_bytes().splitlines()]
    assert [row for row in index_after if row["discovered_physical_path"] not in CONFIG_LOGS] == index_before
    # Existing payloads are identical in this first-registration fixture; only
    # the shared skeleton and the new catalog family can change.
    skeleton_primaries = {relative for relative in SKELETON if not relative.endswith(".path_proof.txt")}
    unrelated = lambda rows: [row for row in rows if row["discovered_physical_path"] not in skeleton_primaries | set(CONFIG_LOGS)]
    assert unrelated(mirror_after) == unrelated(mirror_before)
    allowed = set(SKELETON) | set(CONFIG_LOGS) | {relative + ".path_proof.txt" for relative in CONFIG_LOGS}
    for relative, prior in before.items():
        if prior[0] == "file" and relative not in allowed:
            assert after[relative] == prior, relative
    _checks(config_repo)
    _success(_config_program(config_repo, "publish()"))
    assert _whole_tree_state(config_repo, metadata=True) == after


@pytest.mark.parametrize("fault", ["unknown-target", "index-metadata", "mirror-metadata", "duplicate-registration", "unrelated-stale-proof"])
def test_config_family_publication_refuses_changes_outside_declared_closure(config_repo, fault):
    if fault == "duplicate-registration":
        index = config_repo / "docs/evidence/INDEX.json"
        rows = json.loads(index.read_bytes())
        rows.append(next(dict(row) for row in rows if row["discovered_physical_path"] == CONFIG_LOGS[0]))
        index.write_text(json.dumps(rows, sort_keys=True, separators=(",", ":")) + "\n")
    elif fault == "unrelated-stale-proof":
        (config_repo / "audit/docdeltas/hde-epic039_doc_deltas.md.path_proof.txt").unlink()
    before = _whole_tree_state(config_repo, metadata=True)
    result = _config_program(config_repo, f'''
fault = {fault!r}
original_run = writer._run_once
def corrupt_stage(*, check, **kwargs):
    original_run(check=check, **kwargs)
    if not check or writer._STAGED_VIEW is None:
        return
    if fault == "unknown-target":
        writer._STAGED_VIEW.stage_bytes(writer.ROOT / "artifacts/unrelated-config-delta.txt", b"outside closure\\n")
    elif fault in {{"index-metadata", "mirror-metadata"}}:
        path = writer.HUMAN_INDEX if fault == "index-metadata" else writer.MIRROR_PATH
        raw = writer._STAGED_VIEW.read_bytes(path)
        rows = json.loads(raw) if fault == "index-metadata" else [json.loads(line) for line in raw.splitlines()]
        row = next(row for row in rows if row["discovered_physical_path"] == "audit/docdeltas/hde-epic039_doc_deltas.md")
        row["notes"] = "unauthorized historical metadata change"
        body = json.dumps(rows, sort_keys=True, separators=(",", ":")) + "\\n" if fault == "index-metadata" else "".join(json.dumps(row, sort_keys=True, separators=(",", ":")) + "\\n" for row in rows)
        writer._STAGED_VIEW.stage_bytes(path, body.encode())
writer._run_once = corrupt_stage
publish()
''')
    assert result.returncode != 0
    assert "CONFIG_PUBLICATION_" in result.stderr or "CONFIG_CATALOG_" in result.stderr
    assert _whole_tree_state(config_repo, metadata=True) == before


@pytest.mark.parametrize("existing", [False, True])
@pytest.mark.parametrize("failure", ["primary", "companion", "convergence", "final-verifier"])
def test_config_family_outer_transaction_restores_files_and_parents(config_repo, existing, failure):
    if existing:
        _prior_config_log_fixture(config_repo)
    else:
        _remove_config_catalog_fixture(config_repo)
    before = _whole_tree_state(config_repo, metadata=True)
    _success(_config_program(config_repo, f'''
failure = {failure!r}
original_adapter = writer.publish_config_family
original_publish = writer._publish_staged
original_run = writer._run_once
log = writer.ROOT / "artifacts/catalog/catalog_schema_validation.log"
prior_log = log.read_bytes() if log.exists() else None

def failed_adapter(**kwargs):
    original_produce = kwargs["produce"]
    original_verify = kwargs["verify"]
    def produce():
        original_produce()
        assert log.read_bytes() != prior_log, "fault must follow an actual primary write"
        if failure == "primary":
            raise OSError("injected primary failure after actual owner writes")
    def verify():
        original_verify()
        assert writer._ACTIVE_WRITE_TRANSACTION is not None
        if failure == "final-verifier":
            raise RuntimeError("injected final verification failure after coherent publication")
    kwargs.update(produce=produce, verify=verify)
    return original_adapter(**kwargs)

def failed_publish(staged):
    # Primary owners also use the shared atomic replacement helper. Inject
    # this fault only after the updater has prepared its ledger convergence.
    if writer.MIRROR_PATH not in staged:
        return original_publish(staged)
    changed = sorted((path for path, body in staged.items() if not path.exists() or path.read_bytes() != body), key=str)
    assert len(changed) > 2
    original_publish({{path: staged[path] for path in changed[:-1]}})
    assert any(path in writer._ACTIVE_WRITE_TRANSACTION.files for path in changed[:-1])
    raise OSError("injected companion failure after actual earlier replacements")

def failed_convergence(*, check, **kwargs):
    original_run(check=check, **kwargs)
    if check and writer._STAGED_VIEW is not None:
        raise SystemExit("injected convergence failure")

writer.publish_config_family = failed_adapter
if failure == "companion":
    writer._publish_staged = failed_publish
if failure == "convergence":
    writer._run_once = failed_convergence
try:
    publish()
except (OSError, RuntimeError, SystemExit) as exc:
    assert "injected" in str(exc), str(exc)
else:
    raise AssertionError("injected failure returned success")
assert writer._ACTIVE_WRITE_TRANSACTION is None
assert writer._STAGED_VIEW is None
writer._run_once = original_run
writer._run_once(check=True)
'''))
    assert _whole_tree_state(config_repo, metadata=True) == before
    _checks(config_repo)
    assert _whole_tree_state(config_repo, metadata=True) == before


def test_config_family_rollback_failure_retains_original_cause(config_repo):
    _success(_config_program(config_repo, '''
original_rollback = writer._WriteTransaction.rollback
original_adapter = writer.publish_config_family
def failed_rollback(self):
    original_rollback(self)
    raise OSError("injected config rollback diagnostic")
def failed_adapter(**kwargs):
    original_verify = kwargs["verify"]
    def verify():
        original_verify()
        raise RuntimeError("original config final verification failure")
    kwargs["verify"] = verify
    return original_adapter(**kwargs)
writer._WriteTransaction.rollback = failed_rollback
writer.publish_config_family = failed_adapter
try:
    publish()
except RuntimeError as exc:
    assert str(exc) == "EVIDENCE_INDEX_TRANSACTION_ROLLBACK_FAILED"
    assert str(exc.__cause__) == "original config final verification failure"
    assert any("injected config rollback diagnostic" in note for note in exc.__notes__)
else:
    raise AssertionError("failed rollback returned success")
assert writer._ACTIVE_WRITE_TRANSACTION is None
assert writer._STAGED_VIEW is None
'''))


@pytest.mark.parametrize("missing", [False, True])
def test_config_family_check_is_nonwriting_for_valid_and_missing_companion(config_repo, missing):
    if missing:
        (config_repo / (CONFIG_LOGS[0] + ".path_proof.txt")).unlink()
    before = _whole_tree_state(config_repo, metadata=True)
    result = _run(config_repo, "tools/evidence/update_evidence_index.py", "--check")
    if missing:
        assert result.returncode != 0
        assert "MISSING_PROOF" in result.stderr or "STALE_PROOF" in result.stderr
    else:
        _success(result)
        _checks(config_repo)
    assert _whole_tree_state(config_repo, metadata=True) == before


def test_config_family_rollback_preserves_concurrent_external_destination(config_repo):
    _prior_config_log_fixture(config_repo)
    before = _whole_tree_state(config_repo, metadata=True)
    external_relative = "artifacts/config_bundles/fe_bundle.json"
    _success(_config_program(config_repo, '''
original_converge = writer._converge_and_publish
external = writer.ROOT / "artifacts/config_bundles/fe_bundle.json"
external_body = b"concurrent external owner edit must survive refusal\\n"
def intervene(**kwargs):
    # This happens after actual primary owners returned, before ledger writes.
    # It deliberately bypasses the updater to represent an external editor.
    external.write_bytes(external_body)
    raise RuntimeError("injected failure after concurrent external destination edit")
writer._converge_and_publish = intervene
try:
    publish()
except RuntimeError as exc:
    assert str(exc) == "EVIDENCE_INDEX_TRANSACTION_ROLLBACK_FAILED"
    assert "concurrent external" in str(exc.__cause__)
    assert any("CONFIG_PUBLICATION_ROLLBACK_CONFLICT_PRESERVED" in note for note in exc.__notes__)
else:
    raise AssertionError("concurrent destination conflict returned success")
assert external.read_bytes() == external_body
assert writer._ACTIVE_WRITE_TRANSACTION is None
assert writer._STAGED_VIEW is None
'''))
    after = _whole_tree_state(config_repo, metadata=True)
    assert (config_repo / external_relative).read_bytes() == b"concurrent external owner edit must survive refusal\n"
    for path, state in before.items():
        if path != external_relative:
            assert after[path] == state, path
    assert set(after) == set(before)


def test_config_family_preserves_same_byte_external_replacement_after_owner_receipt(config_repo):
    _prior_config_log_fixture(config_repo)
    before = _whole_tree_state(config_repo, metadata=True)
    external_relative = "artifacts/config_bundles/fe_bundle.json"
    _success(_config_program(config_repo, '''
import os
import stat
external = writer.ROOT / "artifacts/config_bundles/fe_bundle.json"
observed = {}
def intervene(**kwargs):
    # Byte, mode and mtime equality cannot attribute this later inode to the
    # earlier owner receipt. Preserve the external replacement on refusal.
    prior = external.stat()
    temporary = external.with_name(external.name + ".external-test")
    temporary.write_bytes(external.read_bytes())
    temporary.chmod(stat.S_IMODE(prior.st_mode))
    os.utime(temporary, ns=(prior.st_atime_ns, prior.st_mtime_ns))
    os.replace(temporary, external)
    observed["inode"] = external.stat().st_ino
    observed["parent_mtime"] = external.parent.stat().st_mtime_ns
    assert observed["inode"] != prior.st_ino
    raise RuntimeError("injected failure after external same-byte replacement")
writer._converge_and_publish = intervene
try:
    publish()
except RuntimeError as exc:
    assert str(exc) == "EVIDENCE_INDEX_TRANSACTION_ROLLBACK_FAILED"
    assert "external same-byte replacement" in str(exc.__cause__)
    assert any("CONFIG_PUBLICATION_ROLLBACK_CONFLICT_PRESERVED" in note for note in exc.__notes__)
else:
    raise AssertionError("external replacement was attributed to the publisher")
assert external.stat().st_ino == observed["inode"]
assert external.parent.stat().st_mtime_ns == observed["parent_mtime"]
assert writer._ACTIVE_WRITE_TRANSACTION is None
assert writer._STAGED_VIEW is None
'''))
    after = _whole_tree_state(config_repo, metadata=True)
    protected_parents = {
        path.relative_to(config_repo).as_posix()
        for path in (config_repo / external_relative).parents
        if path == config_repo or path.is_relative_to(config_repo)
    }
    for path, state in before.items():
        if path not in protected_parents:
            assert after[path] == state, path
    assert set(after) == set(before)


@pytest.mark.parametrize("interference", ["foreign-bytes", "foreign-inode"])
def test_config_family_refuses_external_postimage_before_attribution(config_repo, interference):
    _prior_config_log_fixture(config_repo)
    before = _whole_tree_state(config_repo, metadata=True)
    external_relative = CONFIG_LOGS[0]
    _success(_config_program(config_repo, f'''
import os
import stat
interference = {interference!r}
original_replace = writer.os.replace
external = writer.ROOT / "artifacts/catalog/catalog_schema_validation.log"
observed = {{}}
def interfere(source, destination):
    original_replace(source, destination)
    if Path(destination) != external:
        return
    if interference == "foreign-bytes":
        external.write_bytes(b"concurrent post-replacement owner edit\\n")
    else:
        # Same emitted bytes do not establish ownership of a replaced inode.
        temporary = external.with_name(external.name + ".external-test")
        temporary.write_bytes(external.read_bytes())
        original_replace(temporary, external)
    metadata = external.lstat()
    observed["file"] = (external.read_bytes(), metadata.st_ino, stat.S_IMODE(metadata.st_mode), metadata.st_mtime_ns)
    observed["parent_mtime"] = external.parent.stat().st_mtime_ns
writer.os.replace = interfere
try:
    publish()
except RuntimeError as exc:
    assert str(exc) == "EVIDENCE_INDEX_TRANSACTION_ROLLBACK_FAILED"
    assert "CONFIG_PUBLICATION_POSTIMAGE_" in str(exc.__cause__)
    assert any("CONFIG_PUBLICATION_ROLLBACK_CONFLICT_PRESERVED" in note for note in exc.__notes__)
else:
    raise AssertionError("external postimage was claimed as an owned write")
assert observed, "interference must follow an actual owner replacement"
metadata = external.lstat()
assert (external.read_bytes(), metadata.st_ino, stat.S_IMODE(metadata.st_mode), metadata.st_mtime_ns) == observed["file"]
assert external.parent.stat().st_mtime_ns == observed["parent_mtime"]
assert writer._ACTIVE_WRITE_TRANSACTION is None
assert writer._STAGED_VIEW is None
'''))
    after = _whole_tree_state(config_repo, metadata=True)
    protected_parents = {path.relative_to(config_repo).as_posix() for path in (config_repo / external_relative).parents if path == config_repo or path.is_relative_to(config_repo)}
    for path, state in before.items():
        if path != external_relative and path not in protected_parents:
            assert after[path] == state, path
    assert set(after) == set(before)


def test_admitted_crd_table_is_explicit_and_matches_the_harness_roots():
    from tools.evidence import update_evidence_index as writer
    from tools.qa import qa_harness as qa

    assert dict(writer.ADMITTED_CRD_QA) == {
        "HDE-CRD-0001": ("audit/qa/hde-crd-0001", "audit.qa.hde_crd_0001"),
        "HDE-CRD-0002": ("audit/qa/hde-crd-0002", "audit.qa.hde_crd_0002"),
    }
    for crd_id, (root_rel, _key) in writer.ADMITTED_CRD_QA.items():
        assert qa.HarnessConfig(crd_id=crd_id, repo_root=writer.ROOT).qa_root == writer.ROOT / root_rel


def test_absent_admitted_crd_root_publishes_nothing():
    from tools.evidence import update_evidence_index as writer

    assert not (ROOT / "audit/qa/hde-crd-0002").exists()
    _unrelated, current = writer._load_crd_qa_entries([])
    assert not [row for row in current if "hde-crd-0002" in row["discovered_physical_path"]]
    index = json.loads((ROOT / "docs/evidence/INDEX.json").read_bytes())
    assert not [row for row in index if row["discovered_physical_path"].startswith("audit/qa/hde-crd-0002")]


SECOND_CRD = 'second = qa.HarnessConfig(crd_id="HDE-CRD-0002", repo_root=writer.ROOT)\n'


def test_crd_0002_fixture_root_publishes_beside_crd_0001(crd_repo):
    _success(_crd_program(crd_repo, SECOND_CRD + (
        "logs, manifest = writer.publish_crd_check_family(second, (observed(),), captured_at_utc=timestamp)\n"
        "assert manifest == writer.ROOT / 'audit/qa/hde-crd-0002/qa_step_logs_manifest.json'\n"
        "publish()\n"
        "qa.validate_crd_check_family(second)\n"
        "qa.validate_crd_check_family(config)\n"
    )))
    entries = json.loads((crd_repo / "docs/evidence/INDEX.json").read_bytes())
    for root, key in (("audit/qa/hde-crd-0001", "audit.qa.hde_crd_0001"), ("audit/qa/hde-crd-0002", "audit.qa.hde_crd_0002")):
        selected = [entry for entry in entries if entry["artifact_key"].startswith(key + ".")]
        assert {entry["discovered_physical_path"] for entry in selected} == {
            f"{root}/qa_step_logs_manifest.json", f"{root}/checks/current/primary.log",
        }
        assert all(set(entry) == {"artifact_key", "discovered_physical_path", "role"} for entry in selected)
    mirror = [json.loads(line) for line in (crd_repo / "artifacts/evidence_index.jsonl").read_bytes().splitlines()]
    for row in mirror:
        if row["discovered_physical_path"].startswith("audit/qa/hde-crd-"):
            assert not {"tokens", "epic_id", "crd_id"} & set(row)
    _checks(crd_repo)
    after = _whole_tree_state(crd_repo)
    _success(_crd_program(crd_repo, SECOND_CRD + (
        "writer.publish_crd_check_family(second, (observed(),), captured_at_utc=timestamp)\n"
    )))
    assert _whole_tree_state(crd_repo) == after


def test_crd_publication_refuses_an_unadmitted_id_by_name(crd_repo):
    before = _whole_tree_state(crd_repo, metadata=True)
    result = _crd_program(crd_repo, (
        "writer.publish_crd_check_family(qa.HarnessConfig(crd_id='HDE-CRD-0003', repo_root=writer.ROOT), (observed(),))\n"
    ))
    assert result.returncode != 0
    assert "admits only HDE-CRD-0001, HDE-CRD-0002; refused HDE-CRD-0003" in result.stderr
    assert _whole_tree_state(crd_repo, metadata=True) == before


@pytest.mark.parametrize("corruption", ["key-0002-path-0001", "key-0001-path-0002"])
def test_crd_index_admission_rejects_cross_crd_rows(crd_repo, corruption):
    _success(_crd_program(crd_repo, "publish()"))
    index = crd_repo / "docs/evidence/INDEX.json"
    entries = json.loads(index.read_bytes())
    selected = next(entry for entry in entries if entry["artifact_key"] == CRD_KEY + ".qa_step_logs_manifest")
    if corruption == "key-0002-path-0001":
        selected["artifact_key"] = "audit.qa.hde_crd_0002.qa_step_logs_manifest"
    else:
        selected["discovered_physical_path"] = "audit/qa/hde-crd-0002/qa_step_logs_manifest.json"
    index.write_bytes((json.dumps(entries, sort_keys=True, separators=(",", ":")) + "\n").encode())
    before = _whole_tree_state(crd_repo, metadata=True)
    result = _run(crd_repo, "tools/evidence/update_evidence_index.py")
    assert result.returncode != 0
    assert "CRD" in result.stderr
    assert _whole_tree_state(crd_repo, metadata=True) == before


def _write_minimal_mirror(root: Path, metadata: dict[str, object]) -> None:
    stamp = "2026-01-01T00:00:00Z"

    def proof(path: str, body: bytes, extra: str = "") -> None:
        (root / f"{path}.path_proof.txt").write_text(
            f"path: {path}\nsize_bytes: {len(body)}\nsha256: {hashlib.sha256(body).hexdigest()}\n"
            f"mtime_utc: {stamp}\nproduced_at_utc: {stamp}\n{extra}"
        )

    (root / "artifacts").mkdir()
    (root / "artifacts/fixture.txt").write_bytes(b"fixture\n")
    proof("artifacts/fixture.txt", b"fixture\n")
    record = {
        "artifact_key": "fixture.crd_record", "discovered_physical_path": "artifacts/fixture.txt",
        "produced_at_utc": stamp, "proof_anchor": "artifacts/fixture.txt.path_proof.txt", "role": "log",
        "sha256": hashlib.sha256(b"fixture\n").hexdigest(), "size_bytes": 8, **metadata,
    }
    body = json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n"
    self_record = {
        "artifact_key": "index.machine_mirror", "discovered_physical_path": "artifacts/evidence_index.jsonl",
        "produced_at_utc": stamp, "proof_anchor": "artifacts/evidence_index.jsonl.path_proof.txt",
        "role": "self_record", "sha256": hashlib.sha256(body.encode()).hexdigest(), "size_bytes": 0,
    }
    while True:
        lines = sorted([body, json.dumps(self_record, sort_keys=True, separators=(",", ":")) + "\n"])
        size = len("".join(lines).encode())
        if self_record["size_bytes"] == size:
            break
        self_record["size_bytes"] = size
    mirror = "".join(lines).encode()
    (root / "artifacts/evidence_index.jsonl").write_bytes(mirror)
    proof("artifacts/evidence_index.jsonl", mirror, f"mirror_body_sha256: {self_record['sha256']}\n")


@pytest.mark.parametrize(
    "metadata,expected",
    [({"crd_id": "HDE-CRD-0002"}, 0), ({"epic_id": "HDE-EPIC040"}, 0), ({"epic_id": "HDE-EPIC040", "crd_id": "HDE-CRD-0002"}, 1)],
    ids=["crd_id", "epic_id", "both"],
)
def test_mirror_schema_accepts_crd_id_and_refuses_epic_and_crd_together(tmp_path, metadata, expected):
    _write_minimal_mirror(tmp_path, metadata)
    result = subprocess.run(
        [sys.executable, str(ROOT / "ci/checks/check_mirror_schema.sh")],
        cwd=tmp_path, env=ENV, capture_output=True, text=True, check=False,
    )
    assert result.returncode == expected, result.stderr
    assert ("EPIC_CRD_EXCLUSIVE" in result.stderr) is bool(expected)


def _release_label() -> str:
    raw = (ROOT / "catalog/manifest.json").read_bytes()
    version = json.loads(raw)["version"]
    return f"current-release capture: release {version}, release_id {hashlib.sha256(raw).hexdigest()}"


def test_current_release_capture_rows_are_labeled_and_frozen_rows_are_not():
    from tools.evidence import update_evidence_index as writer

    label = _release_label()
    mirror = [json.loads(line) for line in (ROOT / "artifacts/evidence_index.jsonl").read_bytes().splitlines()]
    index = {
        (row["artifact_key"], row["discovered_physical_path"]): row
        for row in json.loads((ROOT / "docs/evidence/INDEX.json").read_bytes())
    }
    labeled_paths = set()
    for row in mirror:
        notes = row.get("notes", "")
        if row["discovered_physical_path"] in writer.CURRENT_RELEASE_CAPTURE_PATHS:
            assert notes.endswith(label), row
            labeled_paths.add(row["discovered_physical_path"])
        else:
            assert "current-release capture:" not in notes, row
        if row["role"] != "self_record":
            assert index[(row["artifact_key"], row["discovered_physical_path"])].get("notes") == row.get("notes")
    assert labeled_paths == writer.CURRENT_RELEASE_CAPTURE_PATHS
    frozen = [row for row in mirror if row["discovered_physical_path"].startswith(
        ("artifacts/identity/", "artifacts/math/", "artifacts/cli/showcompat/", "artifacts/vendor/", "audit/ops/")
    )]
    assert frozen and all("current-release capture:" not in row.get("notes", "") for row in frozen)


def test_release_label_strip_preserves_origin_notes():
    from tools.evidence import update_evidence_index as writer

    label = "current-release capture: release 1.3.0, release_id " + "a" * 64
    assert writer._strip_current_release_label({"notes": "origin; " + label}) == {"notes": "origin"}
    assert writer._strip_current_release_label({"notes": label, "role": "log"}) == {"role": "log"}
    assert writer._strip_current_release_label({"notes": "origin"}) == {"notes": "origin"}


NEXT_RELEASE_LABEL = "current-release capture: release 9.9.9, release_id " + "b" * 64
NEXT_RELEASE_UPDATER = (
    "from tools.evidence import update_evidence_index as writer\n"
    f"writer._current_release_label = lambda: {NEXT_RELEASE_LABEL!r}\n"
    "writer.main([])\n"
)


def test_release_labels_follow_regenerated_captures_through_the_updater_alone(tmp_path):
    repo = tmp_path / "repo"
    shutil.copytree(ROOT, repo, copy_function=shutil.copy2, ignore=IGNORES)
    index = repo / "docs/evidence/INDEX.json"
    original, skeleton = index.read_bytes(), _snapshot(repo)
    label = _release_label()

    def updater_for_next_release() -> None:
        _success(subprocess.run(
            [sys.executable, "-c", NEXT_RELEASE_UPDATER], cwd=repo, env=ENV, capture_output=True, text=True, check=False,
        ))

    # A release change alone relabels nothing: no capture has been regenerated.
    updater_for_next_release()
    assert _snapshot(repo) == skeleton

    # The owner regenerates one capture (two rows): only its rows move, once.
    capture = "artifacts/proofs/success_get.txt"
    capture_bytes = (repo / capture).read_bytes()
    (repo / capture).write_bytes(capture_bytes + b"regenerated=true\n")
    updater_for_next_release()
    rows = [row for row in json.loads(index.read_bytes()) if "current-release capture:" in row.get("notes", "")]
    moved = [row for row in rows if row["discovered_physical_path"] == capture]
    assert len(moved) == 2 and all(row["notes"].endswith(NEXT_RELEASE_LABEL) for row in moved)
    assert all(row["notes"].endswith(label) for row in rows if row["discovered_physical_path"] != capture)
    assert all(row["notes"].count("current-release capture:") == 1 for row in rows)
    mirror = [json.loads(line) for line in (repo / "artifacts/evidence_index.jsonl").read_bytes().splitlines()]
    assert {row["sha256"] for row in mirror if row["discovered_physical_path"] == capture} == {
        hashlib.sha256((repo / capture).read_bytes()).hexdigest()
    }

    # Regenerated again under the admitted release, it takes that release back.
    (repo / capture).write_bytes(capture_bytes)
    _success(_run(repo, "tools/evidence/update_evidence_index.py"))
    assert index.read_bytes() == original
    _checks(repo)


def test_unlabeled_capture_rows_take_the_admitted_release_on_adoption(tmp_path):
    from tools.evidence import update_evidence_index as writer

    repo = tmp_path / "repo"
    shutil.copytree(ROOT, repo, copy_function=shutil.copy2, ignore=IGNORES)
    index = repo / "docs/evidence/INDEX.json"
    original = index.read_bytes()
    unlabeled = [writer._strip_current_release_label(row) for row in json.loads(original)]
    index.write_bytes((json.dumps(unlabeled, separators=(",", ":"), sort_keys=True) + "\n").encode())
    _success(_run(repo, "tools/evidence/update_evidence_index.py"))
    assert index.read_bytes() == original
    _checks(repo)


def test_incoherent_capture_labels_are_refused_before_any_write(tmp_path):
    repo = tmp_path / "repo"
    shutil.copytree(ROOT, repo, copy_function=shutil.copy2, ignore=IGNORES)
    index = repo / "docs/evidence/INDEX.json"
    rows = json.loads(index.read_bytes())
    row = next(row for row in rows if row["artifact_key"] == "a7.success_get")
    row["notes"] = NEXT_RELEASE_LABEL
    index.write_bytes((json.dumps(rows, separators=(",", ":"), sort_keys=True) + "\n").encode())
    before = _whole_tree_state(repo, metadata=True)
    result = _run(repo, "tools/evidence/update_evidence_index.py")
    assert result.returncode != 0
    assert "CURRENT_RELEASE_LABEL_INCOHERENT:artifacts/proofs/success_get.txt" in result.stderr
    assert _whole_tree_state(repo, metadata=True) == before


def test_release_label_refuses_a_manifest_that_fails_full_validation(tmp_path):
    repo = tmp_path / "repo"
    shutil.copytree(ROOT, repo, copy_function=shutil.copy2, ignore=IGNORES)
    member = repo / "migrations/005_identity.sql"
    member.write_bytes(member.read_bytes() + b"-- member changed without a re-cut\n")
    before = _whole_tree_state(repo, metadata=True)
    for args in ((), ("--check",)):
        result = _run(repo, "tools/evidence/update_evidence_index.py", *args)
        assert result.returncode != 0
        assert "CURRENT_RELEASE_LABEL_MANIFEST_INVALID" in result.stderr
    assert _whole_tree_state(repo, metadata=True) == before


def test_config_publication_lets_only_a_regenerated_capture_label_move():
    from tools.evidence import update_evidence_index as writer

    identity = ("catalog.catalog_schema_validation", "artifacts/catalog/catalog_schema_validation.log")
    row = {"artifact_key": identity[0], "discovered_physical_path": identity[1], "record_type": "catalog_validation"}
    before = {identity: {**row, "notes": _release_label()}}
    after = {identity: {**row, "notes": NEXT_RELEASE_LABEL}}
    writer._config_logical_delta(before, after, changed_primaries=frozenset({identity[1]}), mirror=False)
    with pytest.raises(ValueError, match="CONFIG_PUBLICATION_UNRELATED_RECORD_DRIFT"):
        writer._config_logical_delta(before, after, changed_primaries=frozenset(), mirror=False)
    drifted = {identity: {**row, "record_type": "other", "notes": NEXT_RELEASE_LABEL}}
    with pytest.raises(ValueError, match="CONFIG_PUBLICATION_UNRELATED_RECORD_DRIFT"):
        writer._config_logical_delta(before, drifted, changed_primaries=frozenset({identity[1]}), mirror=False)


def test_index_normalizer_keeps_crd_id_and_refuses_epic_and_crd_together():
    from tools.evidence import update_evidence_index as writer

    row = {"artifact_key": "fixture.crd", "discovered_physical_path": "audit/qa/hde-crd-0002/x.log"}
    assert writer._normalize_index_entry({**row, "crd_id": "HDE-CRD-0002"})["crd_id"] == "HDE-CRD-0002"
    assert writer._normalize_index_entry({**row, "epic_id": "HDE-EPIC040"})["epic_id"] == "HDE-EPIC040"
    with pytest.raises(ValueError, match="both epic_id and crd_id"):
        writer._normalize_index_entry({**row, "epic_id": "HDE-EPIC040", "crd_id": "HDE-CRD-0002"})
