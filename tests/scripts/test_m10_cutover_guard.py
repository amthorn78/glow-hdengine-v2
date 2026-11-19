"""HDE-EPIC043 WU-PR-07 (HDE-COAG003.6): owner tests of the Magic10 cutover guard.

No real passing v2 candidate can exist before the switch and the cut, so the passing case and the
configuration-bound adverse cases use constructed candidates: small temporary git repositories with a
v1-shaped prior commit and a v2-shaped candidate commit. The guard reads nothing from a candidate but
the admission entry point's ``release_id`` and ``config_sha256``, the manifest's JSON rows, the v2
loader's three public constants, compute's cache prefix, the exit codes of the validation pair and the
contract test, the entry points' import graph and git trees. A constructed tree supplies each through
the same path and name, so it presents the guard with the inputs a real candidate does. The real
implementations behind those interfaces run in ``test_real_trees``, which copies the test checkout's
``HEAD`` into a temporary repository and takes its expectations from the checkout's own state, so it
asserts nothing the cut will change.

Each adverse case asserts its own refusal on its named proof and every other proof's result. Closed
rails throughout: no database, no network, temporary roots only.
"""
from __future__ import annotations

import ast
import hashlib
import importlib.util
import io
import json
import os
import re
import socket
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path

import pytest

from engine.config import magic10_v2_loader
from engine.config.registry_loader import RegistryConfigError, load_active_mechanics_bundle
from engine.serializer.canon import sercanon
from scripts import m10_cutover_guard as guard

ROOT = Path(__file__).resolve().parents[2]
V1 = guard.V1_CONFIGURATION_PATH
V2 = guard.V2_CONFIGURATION_PATH
DECLARED = tuple(magic10_v2_loader.MAGIC10_V2_DECLARED_MEMBERS)
NONE_REFUSED = {"P1": [], "P2": [], "P3": [], "P4": []}
_LOG_LINE = re.compile(r"^M10_CUTOVER_GUARD(_RESULT|_REFUSED)?:[A-Z0-9_=]+$")

_ADMISSION = '''"""Constructed admission entry point: the two attributes the guard reads."""
import hashlib
import json
from pathlib import Path
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[2]


class ConstructedRefusal(Exception):
    def __init__(self, code):
        super().__init__(code)
        self.code = code


def load_active_mechanics_bundle():
    raw = (ROOT / "catalog/manifest.json").read_bytes()
    rows = {row["path"]: row for row in json.loads(raw)["files"]}
    for path, row in rows.items():
        data = (ROOT / path).read_bytes()
        if hashlib.sha256(data).hexdigest() != row["sha256"] or len(data) != row["size"]:
            raise ConstructedRefusal("MANIFEST_MEMBER_HASH_MISMATCH")
    configuration = sorted((path for path in rows if path.startswith("catalog/magic10_mechanics_")), reverse=True)[0]
    return SimpleNamespace(release_id=hashlib.sha256(raw).hexdigest(), config_sha256=rows[configuration]["sha256"])
'''


def _loader(declared=DECLARED, prefix="magic10:v2:") -> bytes:
    return (
        '"""Constructed v2 loader: the three public constants the guard reads."""\n'
        f"MAGIC10_V2_DECLARED_MEMBERS = {tuple(declared)!r}\n"
        'MAGIC10_V2_REBOUND_MEMBERS = ("math/thresholds.json",)\n'
        f"MAGIC10_V2_INTRINSIC_CACHE_PREFIX = {prefix!r}\n"
        '_MECHANICS_CONFIGURATION_PATHS = frozenset({"catalog/magic10_mechanics_v1.json", '
        '"catalog/magic10_mechanics_v2.json"})\n'
    ).encode()


def _json(value) -> bytes:
    return sercanon(value)


def _common() -> dict[str, bytes]:
    files = {path: b"" for path in (
        "adapter/__init__.py", "engine/__init__.py", "engine/cli/__init__.py", "engine/compat/__init__.py",
        "engine/config/__init__.py", "engine/http/__init__.py",
    )}
    for entry in guard.ENTRY_POINTS:
        files[entry] = b"from engine.compat import compute\n"
    files.update({
        "engine/config/registry_loader.py": _ADMISSION.encode(),
        "engine/config/magic10_v2_loader.py": _loader(),
        "scripts/release_id_recompute.py": b"raise SystemExit(0)\n",
        "ci/checks/check_release_identity.sh": b"raise SystemExit(0)\n",
        guard.CONTRACT_TEST: b"def test_contract():\n    assert True\n",
        "migrations/005_identity.sql": b"-- constructed 005\n",
        "migrations/008_writers_auth.sql": b"-- constructed 008\n",
        "migrations/011_body_graphs_durability.sql": b"-- constructed 011\n",
        "schemas/reader.v1.schema.json": _json({"title": "constructed reader v1"}),
        "schemas/reader.v2.schema.json": _json({"title": "constructed reader v2"}),
    })
    return files


def prior_files() -> dict[str, bytes]:
    files = _common()
    files.update({
        "engine/compat/compute.py": (
            b"from engine.config import magic10_v2_loader\nfrom engine.magic10 import composite\n"
            b'INTRINSIC_CACHE_PREFIX = "magic10:v1:"\n'
        ),
        "engine/magic10/__init__.py": b"",
        "engine/magic10/composite.py": b"",
        V1: _json({"config_id": guard.V1_CONFIG_ID}),
        "math/thresholds.json": _json({"version": "1"}),
    })
    return files


def candidate_files() -> dict[str, bytes]:
    files = _common()
    files["engine/compat/compute.py"] = (
        b'from engine.config import magic10_v2_loader\nINTRINSIC_CACHE_PREFIX = "magic10:v1:"\n'
    )
    for path in DECLARED:
        files.setdefault(path, _json({"constructed": path}))
    files[V2] = _json({"config_id": guard.V2_CONFIG_ID})
    files["math/thresholds.json"] = _json({"version": "2"})
    return files


PRIOR_ROWS = (V1, "math/thresholds.json")
CANDIDATE_ROWS = tuple(sorted({*DECLARED, "math/thresholds.json"}))


def _release(files: dict[str, bytes], rows, *, corrupt: str | None = None) -> dict[str, bytes]:
    tree = dict(files)
    entries = [
        {"path": path, "sha256": hashlib.sha256(tree[path]).hexdigest(), "size": len(tree[path])}
        for path in sorted(rows)
    ]
    tree["catalog/manifest.json"] = _json(
        {"built_at_utc": "2026-11-18T00:00:00Z", "files": entries, "root": "catalog/", "version": "0.0.0"}
    )
    if corrupt is not None:
        tree[corrupt] = tree[corrupt] + b"\n"
    return tree


def _git(root: Path, *args: str) -> str:
    done = subprocess.run(
        ["git", "-C", str(root), "-c", "user.name=guard-test", "-c", "user.email=guard-test@example.invalid",
         "-c", "commit.gpgsign=false", *args],
        check=True, capture_output=True, text=True,
    )
    return done.stdout.strip()


def _commit(root: Path, tree: dict[str, bytes], message: str) -> str:
    for path in [line for line in _git(root, "ls-files").splitlines() if line]:
        (root / path).unlink()
    for path, data in tree.items():
        (root / path).parent.mkdir(parents=True, exist_ok=True)
        (root / path).write_bytes(data)
    _git(root, "add", "-A", "-f")
    _git(root, "commit", "-q", "--allow-empty", "-m", message)
    return _git(root, "rev-parse", "HEAD")


def build(tmp_path: Path, *, prior=None, candidate=None, candidate_rows=CANDIDATE_ROWS,
          prior_corrupt=None, candidate_corrupt=None) -> tuple[Path, str, str]:
    """A two-commit repository: (root, prior commit, candidate commit); the candidate is checked out."""
    root = tmp_path / "repository"
    root.mkdir()
    _git(root, "init", "-q")
    prior_tree = {**prior_files(), **(prior or {})}
    prior_sha = _commit(root, _release(prior_tree, PRIOR_ROWS, corrupt=prior_corrupt), "prior")
    candidate_tree = {**candidate_files(), **(candidate or {})}
    candidate_sha = _commit(root, _release(candidate_tree, candidate_rows, corrupt=candidate_corrupt), "candidate")
    return root, prior_sha, candidate_sha


def run(capsysbinary, root: Path, prior: str) -> tuple[int, dict, list[str]]:
    # "--prior=<value>" so that a value starting with "-" reaches the guard, as it can from a shell.
    code = guard.main(["--candidate", str(root), f"--prior={prior}"])
    captured = capsysbinary.readouterr()
    return code, json.loads(captured.out), captured.err.decode().splitlines()


def refusals(report: dict) -> dict[str, list[str]]:
    for proof in report["proofs"].values():
        assert proof["result"] == ("FAIL" if proof["refusals"] else "PASS")
    return {key: proof["refusals"] for key, proof in report["proofs"].items()}


@pytest.fixture(autouse=True)
def guard_tmp(monkeypatch, tmp_path_factory) -> Path:
    """Closed rails, no network, and a test-owned temporary directory for the guard."""
    monkeypatch.setenv("SAFE_MODE", "1")
    monkeypatch.setenv("ALLOW_NETWORK", "0")
    monkeypatch.delenv("DATABASE_URL", raising=False)

    def _refuse_network(*_args, **_kwargs):
        raise AssertionError("network access attempted")

    monkeypatch.setattr(socket.socket, "connect", _refuse_network)
    directory = tmp_path_factory.mktemp("guard_tmp")
    monkeypatch.setattr(tempfile, "tempdir", str(directory))
    return directory


# --------------------------------------------------------------------- constructed candidates

def test_a_good_candidate_passes_all_four_proofs(tmp_path, capsysbinary, guard_tmp):
    root, prior, candidate = build(tmp_path)
    code, report, _ = run(capsysbinary, root, prior)
    assert code == 0 and report["result"] == "PASS" and report["exit_code"] == 0
    assert refusals(report) == NONE_REFUSED
    assert report["candidate"]["head"] == candidate and report["prior"]["resolved"] == prior
    assert report["candidate_release_id"] != report["prior_release_id"]
    assert report["admitted_config_id"] == guard.V2_CONFIG_ID
    assert report["validation_pair"] == {"release_id_recompute": 0, "check_release_identity": 0}
    assert report["contract_test"] == 0
    assert report["admission_codes"] == {"candidate": None, "prior": None}
    # S-12 control: the closure reaches the loader, which names v1 only inside a set display.
    closure, unreadable = guard.static_closure(root)
    assert "engine.config.magic10_v2_loader" in closure and unreadable == []
    assert list(guard_tmp.iterdir()) == []


def test_a_second_active_configuration_fails_p1(tmp_path, capsysbinary):
    root, prior, _ = build(
        tmp_path, candidate={V1: _json({"config_id": guard.V1_CONFIG_ID})}, candidate_rows=(*CANDIDATE_ROWS, V1)
    )
    code, report, _ = run(capsysbinary, root, prior)
    assert code == 1 and report["result"] == "FAIL"
    assert refusals(report) == {**NONE_REFUSED, "P1": ["P1_MULTIPLE_CONFIGURATIONS"]}
    assert report["proofs"]["P1"]["subjects"] == [V1, V2]


def test_a_reachable_retired_scorer_fails_p2(tmp_path, capsysbinary):
    root, prior, _ = build(tmp_path, candidate={
        "engine/magic10/__init__.py": b"",
        "engine/magic10/composite.py": b"",
        "engine/cli/main.py": b"from engine.compat import compute\nfrom engine.magic10 import composite\n",
    })
    code, report, _ = run(capsysbinary, root, prior)
    assert code == 1
    assert refusals(report) == {**NONE_REFUSED, "P2": ["P2_RETIRED_MODULE_REACHABLE"]}
    assert report["proofs"]["P2"]["subjects"] == ["engine.magic10.composite"]


def test_a_reachable_v1_configuration_fails_p2(tmp_path, capsysbinary):
    root, prior, _ = build(tmp_path, candidate={
        "engine/compat/compute.py": (
            b"from engine.config import magic10_v2_loader\n"
            b'INTRINSIC_CACHE_PREFIX = "magic10:v1:"\n_CONFIG = "catalog/magic10_mechanics_v1.json"\n'
        ),
    })
    code, report, _ = run(capsysbinary, root, prior)
    assert code == 1
    assert refusals(report) == {**NONE_REFUSED, "P2": ["P2_V1_CONFIGURATION_NAMED"]}
    assert report["proofs"]["P2"]["subjects"] == ["engine.compat.compute"]


def test_a_missing_declared_member_fails_p3(tmp_path, capsysbinary):
    missing = "schemas/magic10_result_v2.schema.json"
    root, prior, _ = build(tmp_path, candidate_rows=tuple(path for path in CANDIDATE_ROWS if path != missing))
    code, report, _ = run(capsysbinary, root, prior)
    assert code == 1
    assert refusals(report) == {**NONE_REFUSED, "P3": ["P3_DECLARED_MEMBER_MISSING"]}
    assert report["proofs"]["P3"]["subjects"] == [missing]


def test_the_declared_members_are_read_from_the_candidate(tmp_path, capsysbinary):
    extra = "catalog/constructed_only_member.json"
    assert extra not in DECLARED
    root, prior, _ = build(tmp_path, candidate={"engine/config/magic10_v2_loader.py": _loader((*DECLARED, extra))})
    code, report, _ = run(capsysbinary, root, prior)
    assert code == 1
    assert refusals(report) == {**NONE_REFUSED, "P3": ["P3_DECLARED_MEMBER_MISSING"]}
    assert report["proofs"]["P3"]["subjects"] == [extra]


def test_an_unchanged_release_id_fails_p3(tmp_path, capsysbinary):
    root, _, candidate = build(tmp_path)
    code, report, _ = run(capsysbinary, root, candidate)
    assert code == 1
    assert report["candidate_release_id"] == report["prior_release_id"]
    assert refusals(report) == {**NONE_REFUSED, "P3": ["P3_REBOUND_MEMBER_UNCHANGED", "P3_RELEASE_ID_UNCHANGED"]}
    assert report["proofs"]["P3"]["subjects"] == ["math/thresholds.json"]


def test_a_prior_pack_whose_tree_does_not_admit_fails_p4(tmp_path, capsysbinary):
    root, prior, _ = build(tmp_path, prior_corrupt="math/thresholds.json")
    code, report, _ = run(capsysbinary, root, prior)
    assert code == 1
    assert refusals(report) == {
        **NONE_REFUSED, "P3": ["P3_PRIOR_RELEASE_ID_UNAVAILABLE"], "P4": ["P4_PRIOR_NOT_ADMITTED"],
    }
    assert report["admission_codes"] == {"candidate": None, "prior": "MANIFEST_MEMBER_HASH_MISMATCH"}
    assert report["prior_release_id"] is None


@pytest.mark.parametrize("path, data", [
    ("migrations/008_writers_auth.sql", b"-- changed 008\n"),
    ("migrations/012_constructed.sql", b"-- added 012\n"),
], ids=["changed", "added"])
def test_a_changed_migrations_tree_fails_p4(tmp_path, capsysbinary, path, data):
    root, prior, _ = build(tmp_path, candidate={path: data})
    code, report, _ = run(capsysbinary, root, prior)
    assert code == 1
    assert refusals(report) == {**NONE_REFUSED, "P4": ["P4_MIGRATIONS_CHANGED"]}
    assert report["proofs"]["P4"]["subjects"] == [path]


@pytest.mark.parametrize("path", guard.READER_SCHEMAS)
def test_a_changed_reader_schema_fails_p4(tmp_path, capsysbinary, path):
    root, prior, _ = build(tmp_path, candidate={path: _json({"title": "changed"})})
    code, report, _ = run(capsysbinary, root, prior)
    assert code == 1
    assert refusals(report) == {**NONE_REFUSED, "P4": ["P4_READER_SCHEMAS_CHANGED"]}
    assert report["proofs"]["P4"]["subjects"] == [path]


@pytest.mark.parametrize("name, path", [
    ("release_id_recompute", "scripts/release_id_recompute.py"),
    ("check_release_identity", "ci/checks/check_release_identity.sh"),
])
def test_a_failing_validation_pair_step_fails_p3(tmp_path, capsysbinary, name, path):
    root, prior, _ = build(tmp_path, candidate={path: b"raise SystemExit(1)\n"})
    code, report, _ = run(capsysbinary, root, prior)
    assert code == 1
    assert refusals(report) == {**NONE_REFUSED, "P3": ["P3_VALIDATION_PAIR_FAILED"]}
    other = next(key for key in report["validation_pair"] if key != name)
    assert report["validation_pair"] == {name: 1, other: 0}


def test_a_failing_contract_test_fails_p3(tmp_path, capsysbinary):
    root, prior, _ = build(tmp_path, candidate={guard.CONTRACT_TEST: b"def test_contract():\n    assert False\n"})
    code, report, _ = run(capsysbinary, root, prior)
    assert code == 1
    assert refusals(report) == {**NONE_REFUSED, "P3": ["P3_CONTRACT_TEST_FAILED"]}
    assert report["contract_test"] == 1


def test_a_candidate_that_does_not_admit_fails_p1_and_p3(tmp_path, capsysbinary):
    root, prior, _ = build(tmp_path, candidate_corrupt="catalog/centers_v1.json")
    code, report, _ = run(capsysbinary, root, prior)
    assert code == 1
    assert refusals(report) == {
        **NONE_REFUSED, "P1": ["P1_ADMISSION_REFUSED"], "P3": ["P3_CANDIDATE_RELEASE_ID_UNAVAILABLE"],
    }
    assert report["admission_codes"] == {"candidate": "MANIFEST_MEMBER_HASH_MISMATCH", "prior": None}
    assert report["candidate_release_id"] is None and report["admitted_config_id"] is None


def test_overlapping_cache_namespaces_fail_p4(tmp_path, capsysbinary):
    root, prior, _ = build(tmp_path, candidate={"engine/config/magic10_v2_loader.py": _loader(prefix="magic10:v1:")})
    code, report, _ = run(capsysbinary, root, prior)
    assert code == 1
    assert refusals(report) == {**NONE_REFUSED, "P4": ["P4_CACHE_NAMESPACES_NOT_DISJOINT"]}


# ------------------------------------------------------------------------------- preconditions

def _plain(tmp_path, root):
    directory = tmp_path / "plain"
    directory.mkdir()
    return directory, None


def _subdirectory(tmp_path, root):
    return root / "engine", None


def _untracked(tmp_path, root):
    (root / "stray.txt").write_text("x")
    return root, None


def _modified(tmp_path, root):
    with (root / "migrations/005_identity.sql").open("a") as handle:
        handle.write("-- edit\n")
    return root, None


@pytest.mark.parametrize("arrange, prior, token", [
    (_plain, None, "CANDIDATE_NOT_A_GIT_WORK_TREE_ROOT"),
    (_subdirectory, None, "CANDIDATE_NOT_A_GIT_WORK_TREE_ROOT"),
    (_untracked, None, "CANDIDATE_NOT_CLEAN"),
    (_modified, None, "CANDIDATE_NOT_CLEAN"),
    (None, "0" * 40, "PRIOR_NOT_RESOLVED"),
    (None, "-x", "PRIOR_NOT_RESOLVED"),
    ("open_rails", None, "CLOSED_RAILS_REQUIRED"),
], ids=["plain-directory", "subdirectory", "untracked-file", "modified-file", "unknown-prior", "option-prior",
        "open-rails"])
def test_a_refused_precondition_evaluates_no_proof(tmp_path, capsysbinary, monkeypatch, arrange, prior, token):
    root, prior_sha, _ = build(tmp_path)
    candidate = root
    if arrange == "open_rails":
        monkeypatch.setenv("SAFE_MODE", "0")
    elif arrange is not None:
        candidate, _ = arrange(tmp_path, root)
    code, report, err = run(capsysbinary, candidate, prior or prior_sha)
    assert code == 3 and report["result"] == "REFUSED" and report["exit_code"] == 3
    assert report["refusal"] == token
    assert {proof["result"] for proof in report["proofs"].values()} == {"NOT_EVALUATED"}
    assert report["candidate"]["head"] is None and report["prior"]["resolved"] is None
    assert report["candidate_release_id"] is None and report["prior_release_id"] is None
    assert report["validation_pair"] == {"release_id_recompute": None, "check_release_identity": None}
    assert report["contract_test"] is None
    assert err[-1] == f"M10_CUTOVER_GUARD_REFUSED:{token}"


def test_a_candidate_that_changes_during_the_run_is_refused(tmp_path, capsysbinary):
    writer = b"from pathlib import Path\n\ndef test_contract():\n    Path(__file__).with_name('written.txt').write_text('x')\n"
    root, prior, _ = build(tmp_path, candidate={guard.CONTRACT_TEST: writer})
    code, report, err = run(capsysbinary, root, prior)
    assert code == 4 and report["result"] == "REFUSED" and report["exit_code"] == 4
    assert report["refusal"] == "CANDIDATE_CHANGED_DURING_RUN"
    assert err[-1] == "M10_CUTOVER_GUARD_REFUSED:CANDIDATE_CHANGED_DURING_RUN"


# ------------------------------------------------------------------------ read-only and report

def _snapshot(root: Path) -> dict[str, object]:
    files = {}
    for current, _, names in os.walk(root):
        for name in names:
            path = Path(current) / name
            files[path.relative_to(root).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return {
        "files": files,
        "status": _git(root, "--no-optional-locks", "status", "--porcelain", "--untracked-files=all", "--ignored"),
        "refs": _git(root, "for-each-ref"),
        "worktrees": _git(root, "worktree", "list", "--porcelain"),
    }


@pytest.mark.parametrize("prior_corrupt", [None, "math/thresholds.json"], ids=["good", "prior-not-admitted"])
def test_a_run_leaves_the_repository_and_the_temporary_directory_unchanged(
    tmp_path, capsysbinary, guard_tmp, prior_corrupt
):
    root, prior, _ = build(tmp_path, prior_corrupt=prior_corrupt)
    before = _snapshot(root)
    run(capsysbinary, root, prior)
    assert _snapshot(root) == before
    assert before["status"] == ""
    assert list(guard_tmp.iterdir()) == []


def test_the_candidates_checks_keep_their_temporary_files_in_the_guard_directory(tmp_path, capsysbinary, guard_tmp):
    # The real contract test writes through pytest's tmp_path; children must not write to the shared
    # temporary root. The constructed contract test fails unless its tmp_path and a tempfile file are
    # inside the guard's directory, and the guard removes that directory.
    contract = (
        "import os\nimport tempfile\nfrom pathlib import Path\n\n"
        f"GUARD_TMP = Path({str(guard_tmp.resolve())!r})\n\n\n"
        "def test_contract(tmp_path):\n"
        "    (tmp_path / 'scratch.txt').write_text('x')\n"
        "    handle, name = tempfile.mkstemp()\n"
        "    os.close(handle)\n"
        "    assert tmp_path.resolve().is_relative_to(GUARD_TMP)\n"
        "    assert Path(name).resolve().is_relative_to(GUARD_TMP)\n"
    ).encode()
    root, prior, _ = build(tmp_path, candidate={guard.CONTRACT_TEST: contract})
    code, report, _ = run(capsysbinary, root, prior)
    assert report["contract_test"] == 0
    assert (code, refusals(report)) == (0, NONE_REFUSED)
    assert list(guard_tmp.iterdir()) == []


_REPORT_KEYS = {
    "schema", "result", "exit_code", "refusal", "candidate", "prior", "candidate_release_id", "prior_release_id",
    "admitted_config_id", "admission_codes", "validation_pair", "contract_test", "proofs",
}


@pytest.mark.parametrize("case", ["pass", "fail", "refused"])
def test_the_report_is_canonical_with_a_closed_key_set_and_keys_only_logs(tmp_path, capsysbinary, case):
    candidate = {V1: _json({"config_id": guard.V1_CONFIG_ID})} if case == "fail" else None
    rows = (*CANDIDATE_ROWS, V1) if case == "fail" else CANDIDATE_ROWS
    root, prior, _ = build(tmp_path, candidate=candidate, candidate_rows=rows)
    code = guard.main(["--candidate", str(root), "--prior", "0" * 40 if case == "refused" else prior])
    captured = capsysbinary.readouterr()
    report = json.loads(captured.out)
    assert captured.out == sercanon(report)
    assert set(report) == _REPORT_KEYS and report["schema"] == guard.REPORT_SCHEMA
    assert set(report["candidate"]) == {"root", "head"} and set(report["prior"]) == {"commit", "resolved"}
    assert set(report["admission_codes"]) == {"candidate", "prior"}
    assert set(report["validation_pair"]) == {"release_id_recompute", "check_release_identity"}
    assert [(key, proof["name"]) for key, proof in report["proofs"].items()] == list(guard.PROOFS)
    assert all(set(proof) == {"name", "result", "refusals", "subjects"} for proof in report["proofs"].values())
    assert report["exit_code"] == code == {"pass": 0, "fail": 1, "refused": 3}[case]
    assert report["candidate"]["root"] == str(root)
    lines = captured.err.decode().splitlines()
    assert lines and all(_LOG_LINE.fullmatch(line) for line in lines)
    assert str(tmp_path) not in captured.err.decode()


def test_the_command_line_runs_the_guard_and_refuses_a_usage_error(tmp_path, guard_tmp):
    root, prior, _ = build(tmp_path)
    env = {"PATH": os.environ["PATH"], "LC_ALL": "C", "LANG": "C", "TZ": "UTC", "SAFE_MODE": "1",
           "ALLOW_NETWORK": "0", "PYTHONDONTWRITEBYTECODE": "1", "TMPDIR": str(guard_tmp)}
    command = [sys.executable, "scripts/m10_cutover_guard.py"]
    done = subprocess.run([*command, "--candidate", str(root), "--prior", prior],
                          cwd=ROOT, env=env, capture_output=True, check=False)
    assert done.returncode == 0
    assert json.loads(done.stdout)["result"] == "PASS"
    assert list(guard_tmp.iterdir()) == []
    usage = subprocess.run(command, cwd=ROOT, env=env, capture_output=True, check=False)
    assert usage.returncode == 2 and usage.stdout == b""


# --------------------------------------------------------------------------------- real trees

def _copy_of_head(destination: Path) -> None:
    archive = subprocess.run(["git", "-C", str(ROOT), "archive", "--format=tar", "HEAD"],
                             check=True, capture_output=True).stdout
    with tarfile.open(fileobj=io.BytesIO(archive), mode="r:") as tar:
        tar.extractall(destination, filter="data")
    _git(destination, "init", "-q")
    _git(destination, "add", "-A", "-f")
    _git(destination, "commit", "-q", "-m", "copy of HEAD")


def test_real_trees(tmp_path, capsysbinary):
    """The real admission, validation pair, contract test, closure and extraction over a copy of HEAD.

    The prior is the same commit. Expectations follow the checkout's own state, read by two oracles
    independent of the guard, so the case holds at every stage: A while it admits and binds only the
    v1 configuration (Stage A); B while it does not admit (the switch head before the cut); C once it
    admits and binds only the v2 configuration (after the cut). P2 is asserted under A (both findings)
    and under C (none: the cut re-targeted the config tool, the last closure module naming v1).
    """
    candidate = tmp_path / "candidate"
    candidate.mkdir()
    _copy_of_head(candidate)
    code, report, _ = run(capsysbinary, candidate, "HEAD")
    assert code == 1 and report["result"] == "FAIL"
    assert "NOT_EVALUATED" not in {proof["result"] for proof in report["proofs"].values()}
    found = refusals(report)

    try:
        oracle = load_active_mechanics_bundle()
    except RegistryConfigError:
        oracle = None
    rows = {row["path"] for row in json.loads((ROOT / "catalog/manifest.json").read_bytes())["files"]}
    configurations = rows & {V1, V2}

    if oracle is not None and configurations == {V1}:
        assert {"P1_ADMITTED_CONFIGURATION_NOT_V2", "P1_V2_CONFIGURATION_ROW_MISSING"} <= set(found["P1"])
        assert {"P2_RETIRED_MODULE_REACHABLE", "P2_V1_CONFIGURATION_NAMED"} <= set(found["P2"])
        assert {"P3_DECLARED_MEMBER_MISSING", "P3_RELEASE_ID_UNCHANGED"} <= set(found["P3"])
        assert found["P4"] == []
        assert report["candidate_release_id"] == report["prior_release_id"] == oracle.release_id
        assert report["admitted_config_id"] == guard.V1_CONFIG_ID
        assert report["validation_pair"] == {"release_id_recompute": 0, "check_release_identity": 0}
        assert report["contract_test"] == 0
    elif oracle is None:
        assert "P1_ADMISSION_REFUSED" in found["P1"]
        assert "P3_CANDIDATE_RELEASE_ID_UNAVAILABLE" in found["P3"]
        assert "P4_PRIOR_NOT_ADMITTED" in found["P4"]
    elif configurations == {V2}:
        assert found["P1"] == []
        assert found["P2"] == []
        assert "P3_RELEASE_ID_UNCHANGED" in found["P3"]
        assert report["admitted_config_id"] == guard.V2_CONFIG_ID
    else:
        pytest.fail(f"unexpected checkout state: admits={oracle is not None} configurations={sorted(configurations)}")


def test_the_guard_closure_equals_the_inv5_helper_closure():
    spec = importlib.util.spec_from_file_location(
        "_hde_epic043_inv5_closure_for_guard", ROOT / "tests" / "m10_v2" / "test_v2_unreachable_from_production.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    closure, unreadable = guard.static_closure(ROOT)
    assert unreadable == []
    assert set(closure) == set(module._static_closure())
    assert {"adapter.factory", "engine.cli.main", "engine.http.compat_handler"} <= set(closure)


def test_the_guard_imports_no_network_module():
    tree = ast.parse((ROOT / "scripts" / "m10_cutover_guard.py").read_text(encoding="utf-8"))
    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module.split(".")[0])
    assert not imported & {"socket", "ssl", "urllib", "http", "requests", "ftplib", "smtplib"}
