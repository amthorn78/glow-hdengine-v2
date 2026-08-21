from __future__ import annotations

import copy
import hashlib
import json
import os
import signal
import shutil
import stat
import struct
import subprocess
import zlib
from collections.abc import Callable
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

from tools.qa import generate_epic_close_pack as close_pack


ROOT = Path(__file__).resolve().parents[2]
SOURCE_REL = "close/epic123.json"
REPORT_REL = "audit/EPIC-123_close_report.md"
MANIFEST_REL = "audit/EPIC-123_MANIFEST.json"


@pytest.fixture(autouse=True)
def closed_rails(monkeypatch: pytest.MonkeyPatch) -> None:
    for key, value in close_pack.CLOSED_RAILS.items():
        monkeypatch.setenv(key, value)


def _git(repo: Path, *args: str, check: bool = True) -> str:
    completed = subprocess.run(
        ("git", *args),
        cwd=repo,
        capture_output=True,
        text=True,
        check=False,
    )
    if check and completed.returncode != 0:
        raise AssertionError(completed.stderr)
    return completed.stdout.strip()


def _write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, ensure_ascii=True, separators=(",", ":"), sort_keys=True)
        + "\n",
        encoding="utf-8",
    )


def _valid_source() -> dict[str, object]:
    return {
        "schema_version": "epic_close_candidate_source.v1",
        "epic_id": "HDE-EPIC123",
        "plan_path": "plans/epic123.md",
        "evidence_inputs": [
            {"binding": "determinism", "path": "evidence/determinism.txt"},
            {"binding": "scope", "path": "evidence/scope.json"},
        ],
        "report_sections": [
            {
                "heading": "Delivered scope",
                "body_lines": [
                    "Candidate scope is bounded by the declared tracked inputs.",
                    "Candidate validation compares exact committed bytes.",
                ],
            },
            {
                "heading": "Validation posture",
                "body_lines": ["The report and manifest are accepted only as one committed pair."],
            },
        ],
        "key_outputs": {
            "close_report": REPORT_REL,
            "close_manifest": MANIFEST_REL,
        },
        "nonclaims": [
            "no_epic_closeout_or_pf09_movement",
            "no_hosted_feedback_or_external_attestation",
            "no_ops_live_qa_deployment_or_release",
            "no_public_contract_runtime_or_data_change",
            "no_qa_acceptance_or_token_satisfaction",
        ],
    }


def _init_repo(
    tmp_path: Path,
    *,
    source: dict[str, object] | None = None,
    raw_source: bytes | None = None,
) -> Path:
    repo = tmp_path / "repo"
    repo.mkdir(parents=True)
    (repo / "schemas").mkdir()
    shutil.copyfile(
        ROOT / close_pack.SCHEMA_REL,
        repo / close_pack.SCHEMA_REL,
    )
    (repo / "plans").mkdir()
    (repo / "plans/epic123.md").write_text("# Plan\n\nTracked plan.\n", encoding="utf-8")
    (repo / "evidence").mkdir()
    (repo / "evidence/determinism.txt").write_text(
        "two-run identity\n", encoding="utf-8"
    )
    _write_json(repo / "evidence/scope.json", {"scope": "bounded"})
    (repo / "audit").mkdir()
    (repo / "audit/README.md").write_text("candidate output home\n", encoding="utf-8")
    source_path = repo / SOURCE_REL
    source_path.parent.mkdir()
    if raw_source is not None:
        source_path.write_bytes(raw_source)
    else:
        _write_json(source_path, source or _valid_source())

    _git(repo, "init")
    _git(repo, "config", "user.email", "close-pack@example.invalid")
    _git(repo, "config", "user.name", "Close Pack Test")
    _git(repo, "add", "audit/README.md", SOURCE_REL, "evidence", "plans", "schemas")
    _git(repo, "commit", "-m", "tracked candidate inputs")
    assert _git(repo, "status", "--porcelain=v1", "--untracked-files=all") == ""
    return repo


def _run(
    repo: Path,
    monkeypatch: pytest.MonkeyPatch,
    *args: str,
) -> int:
    monkeypatch.chdir(repo)
    return close_pack.main(list(args))


def _generate_and_commit(
    repo: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> tuple[bytes, bytes]:
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 0
    report = (repo / REPORT_REL).read_bytes()
    manifest = (repo / MANIFEST_REL).read_bytes()
    _git(repo, "add", REPORT_REL, MANIFEST_REL)
    _git(repo, "commit", "-m", "commit complete candidate")
    assert _git(repo, "status", "--porcelain=v1", "--untracked-files=all") == ""
    return report, manifest


def _render_expected_outputs(
    repo: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> dict[str, bytes]:
    monkeypatch.chdir(repo)
    root = close_pack._repository_root()
    context = close_pack._establish_git_context(root)
    head = close_pack._head(context)
    model, _ = close_pack._load_model(root, context, head, SOURCE_REL)
    return close_pack._render_twice(model)


def _kill_writer_at_boundary(repo: Path, boundary: str) -> None:
    read_fd, write_fd = os.pipe()
    pid = os.fork()
    if pid == 0:  # pragma: no cover - assertions run in the parent
        try:
            os.close(read_fd)

            def stop_at_boundary(name: str) -> None:
                if name == boundary:
                    os.write(write_fd, b"1")
                    os.close(write_fd)
                    signal.pause()

            close_pack._publication_boundary = stop_at_boundary
            os.chdir(repo)
            result = close_pack.main(["--source", SOURCE_REL, "--write"])
            os._exit(10 + result)
        except BaseException:
            os._exit(99)
    os.close(write_fd)
    observed = os.read(read_fd, 1)
    os.close(read_fd)
    if observed != b"1":
        _, status = os.waitpid(pid, 0)
        raise AssertionError(
            f"writer exited before boundary {boundary}: status={status}"
        )
    os.kill(pid, signal.SIGKILL)
    _, status = os.waitpid(pid, 0)
    assert os.WIFSIGNALED(status)
    assert os.WTERMSIG(status) == signal.SIGKILL


def _metadata(path: Path) -> tuple[int, int, int, int, int, int]:
    value = path.stat()
    return (
        stat.S_IMODE(value.st_mode),
        value.st_size,
        value.st_mtime_ns,
        value.st_ctime_ns,
        value.st_ino,
        value.st_atime_ns,
    )


def _read_noatime(path: Path) -> bytes:
    descriptor = os.open(
        path,
        os.O_RDONLY | os.O_NOFOLLOW | os.O_NOATIME,
    )
    try:
        chunks: list[bytes] = []
        while True:
            chunk = os.read(descriptor, 1024 * 1024)
            if not chunk:
                break
            chunks.append(chunk)
        return b"".join(chunks)
    finally:
        os.close(descriptor)


def _replace_index_stat_cache_with_worktree_metadata(repo: Path, rel: str) -> bytes:
    """Make one checksum-valid index stat cache match the current worktree inode."""
    algorithm = _git(repo, "rev-parse", "--show-object-format")
    digest_size = hashlib.new(algorithm).digest_size
    index_path = repo / ".git/index"
    payload = bytearray(_read_noatime(index_path))
    assert payload[:4] == b"DIRC"
    assert len(payload) >= 12 + digest_size
    content_end = len(payload) - digest_size
    version, count = struct.unpack(">II", payload[4:12])
    assert version in {2, 3}

    metadata = (repo / rel).lstat()
    offset = 12
    found = False
    for _ in range(count):
        start = offset
        cached = list(struct.unpack(">10I", payload[offset : offset + 40]))
        offset += 40 + digest_size
        flags = struct.unpack(">H", payload[offset : offset + 2])[0]
        offset += 2
        if flags & 0x4000:
            assert version == 3
            offset += 2
        terminator = payload.find(b"\0", offset, content_end)
        assert terminator >= 0
        path = bytes(payload[offset:terminator]).decode("utf-8")
        offset = terminator + 1
        offset += (8 - ((offset - start) % 8)) % 8
        if path != rel:
            continue

        ctime_seconds, ctime_nanoseconds = divmod(
            metadata.st_ctime_ns, 1_000_000_000
        )
        mtime_seconds, mtime_nanoseconds = divmod(
            metadata.st_mtime_ns, 1_000_000_000
        )
        cached[0:6] = [
            ctime_seconds,
            ctime_nanoseconds,
            mtime_seconds,
            mtime_nanoseconds,
            metadata.st_dev & 0xFFFFFFFF,
            metadata.st_ino & 0xFFFFFFFF,
        ]
        cached[7:10] = [
            metadata.st_uid & 0xFFFFFFFF,
            metadata.st_gid & 0xFFFFFFFF,
            metadata.st_size & 0xFFFFFFFF,
        ]
        payload[start : start + 40] = struct.pack(">10I", *cached)
        found = True

    assert found
    content = bytes(payload[:content_end])
    payload[content_end:] = hashlib.new(algorithm, content).digest()
    index_path.write_bytes(payload)
    poisoned = _read_noatime(index_path)
    assert (
        hashlib.new(algorithm, poisoned[:content_end]).digest()
        == poisoned[content_end:]
    )
    return poisoned


def _append_checksum_valid_index_extension(
    repo: Path, signature: bytes, extension: bytes = b""
) -> bytes:
    assert len(signature) == 4
    algorithm = _git(repo, "rev-parse", "--show-object-format")
    digest_size = hashlib.new(algorithm).digest_size
    index_path = repo / ".git/index"
    original = _read_noatime(index_path)
    content = (
        original[:-digest_size]
        + signature
        + len(extension).to_bytes(4, "big")
        + extension
    )
    updated = content + hashlib.new(algorithm, content).digest()
    index_path.write_bytes(updated)
    assert _read_noatime(index_path) == updated
    return updated


def _assert_only_symlink_atime_may_differ(
    before: dict[str, tuple[int, int, int, int, int, int, int]],
    after: dict[str, tuple[int, int, int, int, int, int, int]],
    rel: str | set[str],
    *,
    require_change: bool,
) -> None:
    allowed = {rel} if isinstance(rel, str) else rel
    assert before.keys() == after.keys()
    for path, prior in before.items():
        current = after[path]
        if path not in allowed:
            assert current == prior, path
            continue
        assert current[:2] == prior[:2]
        assert current[3:] == prior[3:]
        if require_change:
            assert current[2] != prior[2]


def test_schema_is_closed_and_admits_truthful_dependency_nonclaims() -> None:
    schema = json.loads((ROOT / close_pack.SCHEMA_REL).read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    valid = _valid_source()
    assert validator.is_valid(valid)

    for field in (
        "run_id",
        "receipt",
        "hosted_result",
        "release_id",
        "current_attestation",
        "later_commit_result",
        "output_root",
    ):
        invalid = copy.deepcopy(valid)
        invalid[field] = "prohibited dependency"
        assert not validator.is_valid(invalid), field

    for container, field in (
        ("evidence_inputs", "unexpected_evidence_key"),
        ("report_sections", "unexpected_section_key"),
    ):
        invalid = copy.deepcopy(valid)
        invalid[container][0][field] = "prohibited"
        assert not validator.is_valid(invalid), f"{container}.{field}"
    invalid = copy.deepcopy(valid)
    invalid["key_outputs"]["unexpected_output"] = "audit/EPIC-123_OTHER.json"
    assert not validator.is_valid(invalid)

    assert validator.is_valid(valid)
    assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    assert schema["$id"] == close_pack.SCHEMA_REL
    assert schema["additionalProperties"] is False


@pytest.mark.parametrize(
    ("location", "value"),
    (
        ("binding", "run_id"),
        ("binding", "hosted-result"),
        ("binding", "workflow_results"),
        ("evidence_path", "audit/hosted_receipt.json"),
        ("evidence_path", "audit/hosted/result.json"),
        ("evidence_path", "evidence/workflow-results.json"),
        ("evidence_path", "audit/current_attestation.json"),
        ("plan_path", "catalog/manifest.json"),
        ("plan_path", "catalog/manifest.json.path_proof.txt"),
        ("plan_path", "plans/later-commit.md"),
        ("heading", "Run:id result"),
        ("heading", "Later\tcommit outcome"),
        ("heading", "Release ID result"),
        ("heading", "Release/id result"),
        ("body", "Hosted result is current."),
        ("body", "Source commit " + "a" * 40),
        ("body", "Source:commit is not a causal field."),
    ),
)
def test_schema_rejects_feedback_dependencies_in_every_causal_role(
    location: str,
    value: str,
) -> None:
    schema = json.loads((ROOT / close_pack.SCHEMA_REL).read_text(encoding="utf-8"))
    source = _valid_source()
    if location == "binding":
        source["evidence_inputs"][0]["binding"] = value
    elif location == "evidence_path":
        source["evidence_inputs"][0]["path"] = value
    elif location == "plan_path":
        source["plan_path"] = value
    elif location == "heading":
        source["report_sections"][0]["heading"] = value
    else:
        source["report_sections"][0]["body_lines"][0] = value
    assert not Draft202012Validator(schema).is_valid(source)


def test_semantic_guard_contract_is_schema_runtime_identical() -> None:
    schema = json.loads((ROOT / close_pack.SCHEMA_REL).read_text(encoding="utf-8"))
    assert (
        schema["$defs"]["feedback_dependency"]["pattern"]
        == close_pack.FEEDBACK_DEPENDENCY_PATTERN
    )
    assert (
        schema["$defs"]["causal_report_heading"]["allOf"][1]["enum"]
        == list(close_pack.REPORT_SECTION_HEADINGS)
    )
    assert (
        schema["$defs"]["causal_report_body_line"]["allOf"][1]["enum"]
        == list(close_pack.REPORT_BODY_LINES)
    )


@pytest.mark.parametrize(
    "value",
    (
        "Workflow run identifier: 12345",
        "Release identity: abc",
        "Hosted outcome: pass",
        "Workflow run number 42",
        "CI/outcome: green",
        "Workflow run identity value",
        "Workflow run result: green.",
        "CI job outcome: green.",
        "Hosted status: green.",
        "Release number: 12.",
        "Workflow execution identifier: 12.",
        "Hosted check result: pass.",
        "Hosted check status: green.",
        "Workflow attempt number: 2.",
        "Hosted validation result: pass.",
        "Workflow conclusion: success.",
        "CI check conclusion: green.",
        "Build result: pass.",
        "Workflow results: green.",
        "Build conclusions: success.",
        "Continuous integration result: success.",
        "Job identifier: 12345.",
    ),
)
def test_full_form_feedback_identifiers_fail_schema_and_runtime(value: str) -> None:
    schema = json.loads((ROOT / close_pack.SCHEMA_REL).read_text(encoding="utf-8"))
    source = _valid_source()
    source["report_sections"][0]["body_lines"][0] = value
    assert not Draft202012Validator(schema).is_valid(source)
    with pytest.raises(close_pack.ClosePackError, match="FEEDBACK_DEPENDENCY_PROHIBITED"):
        close_pack._require_feedback_free_source(source, SOURCE_REL, "a" * 40)


@pytest.mark.parametrize(
    ("location", "value"),
    (
        ("binding", "run_url"),
        ("binding", "run_identity"),
        ("binding", "workflow_run_url"),
        ("binding", "check_run_url"),
        ("binding", "hosted_check_url"),
        ("binding", "job_url"),
        ("binding", "run_attempt"),
        ("binding", "github_run_attempt"),
        ("binding", "run_conclusion"),
        ("binding", "check_run_conclusion"),
        ("binding", "github_sha"),
        ("binding", "head_sha"),
        ("binding", "commit_identifier"),
        ("binding", "commit_sha"),
        ("evidence_path", "evidence/workflow_run_url.json"),
        ("evidence_path", "evidence/run_identity.json"),
        ("evidence_path", "evidence/github_run_attempt.json"),
        ("evidence_path", "evidence/github_run_conclusion.json"),
        ("evidence_path", "evidence/head_sha.txt"),
        ("plan_path", "plans/commit_identifier.md"),
    ),
)
def test_hosted_and_source_identity_aliases_fail_every_filter_layer(
    location: str,
    value: str,
) -> None:
    schema = json.loads((ROOT / close_pack.SCHEMA_REL).read_text(encoding="utf-8"))
    source = _valid_source()
    if location == "binding":
        source["evidence_inputs"][0]["binding"] = value
    elif location == "evidence_path":
        source["evidence_inputs"][0]["path"] = value
    else:
        source["plan_path"] = value
    assert not Draft202012Validator(schema).is_valid(source)
    with pytest.raises(close_pack.ClosePackError, match="FEEDBACK_DEPENDENCY_PROHIBITED"):
        close_pack._require_feedback_free_source(source, SOURCE_REL, "a" * 40)


@pytest.mark.parametrize(
    "value",
    (
        "artifacts/ops/internal_version/two_run_identity.log",
        "artifacts/parity/two_run_identity.log",
        "artifacts/core/two_run/identity.json",
        "proofs/TWO_RUN_IDENTITY.txt",
    ),
)
def test_tracked_two_run_identity_evidence_is_not_feedback_metadata(
    value: str,
) -> None:
    schema = json.loads((ROOT / close_pack.SCHEMA_REL).read_text(encoding="utf-8"))
    source = _valid_source()
    source["evidence_inputs"][0]["path"] = value
    assert Draft202012Validator(schema).is_valid(source)
    close_pack._require_feedback_free_source(source, SOURCE_REL, "a" * 40)


@pytest.mark.parametrize(
    "value",
    (
        "QA PASS and acceptance tokens are satisfied.",
        "Product Owner closeout is complete.",
        "Product-Owner closeout: completed.",
        "HDE-EPIC123 completion is achieved.",
        "Acceptance approval is granted.",
        "Deployment success is complete.",
        "Release completion succeeded.",
        "PF09/status movement is performed.",
        "Runtime behavior changed.",
        "QA passed.",
        "QA has passed.",
        "QA is complete.",
        "We completed Product Owner closeout.",
        "Product Owner has completed closeout.",
        "Deployment occurred.",
        "OPS ran.",
        "Live QA ran.",
        "Migration applied.",
        "QA was reviewed and passed.",
        "Acceptance was reviewed and granted.",
        "OPS was prepared and performed.",
        "Deployment was prepared and executed.",
        "Product Owner considered and approved closeout.",
        "QA " + "x" * 64 + " passed.",
        "Closeout is complete.",
        "Epic is complete.",
        "QA green.",
        "Acceptance confirmed.",
        "Tokens fulfilled.",
        "Deployed to production.",
        "PF09 moved.",
        "Release shipped.",
        "Acceptance signed off.",
        "Product Owner signed off closeout.",
        "OPS happened.",
        "Production deployment happened.",
        "Deployment took place.",
        "PF09 status progressed.",
        "Release issued.",
        "The public contract was altered.",
        "Runtime behavior differs.",
        "Persistent data was altered.",
        "No deployment was completed.",
        "Deployment is incomplete.",
        "Acceptance was not granted.",
        "QA wasn't passed.",
        "QA hasn't passed.",
        "QA cannot pass.",
        "Acceptance was neither requested nor granted.",
        "QA wasn't reviewed and passed.",
        "Quality assurance passed.",
        "Releases shipped.",
        "Migrations applied.",
        "Public contracts changed.",
        "The Product Owners approved closure.",
        "PF-09 moved.",
        "Operations ran.",
        "Go-live completed.",
        "Q**A** passed.",
        "Q&#65; passed.",
    ),
)
def test_protected_nonclaim_subjects_fail_schema_and_runtime(value: str) -> None:
    schema = json.loads((ROOT / close_pack.SCHEMA_REL).read_text(encoding="utf-8"))
    source = _valid_source()
    source["report_sections"][0]["body_lines"][0] = value
    assert not Draft202012Validator(schema).is_valid(source)
    with pytest.raises(close_pack.ClosePackError, match="REPORT_NONCLAIM_CONTRADICTION"):
        close_pack._require_report_nonclaim_posture(source)


@pytest.mark.parametrize("value", close_pack.REPORT_BODY_LINES)
def test_semantic_guards_admit_registered_neutral_report_text(value: str) -> None:
    schema = json.loads((ROOT / close_pack.SCHEMA_REL).read_text(encoding="utf-8"))
    source = _valid_source()
    source["report_sections"][0]["body_lines"][0] = value
    assert Draft202012Validator(schema).is_valid(source)
    close_pack._require_feedback_free_source(source, SOURCE_REL, "a" * 40)
    close_pack._require_report_nonclaim_posture(source)


@pytest.mark.parametrize(
    "lines",
    (
        ["Public", "contract changed."],
        ["Runtime", "behavior changed."],
        ["Persistent", "data changed."],
        ["PF", "09 moved."],
        ["Product", "Owner approved closure."],
        ["Workflow run", "result: green."],
        ["Hosted", "result: success."],
        ["Later", "commit outcome: green."],
    ),
)
def test_closed_report_contract_rejects_split_unregistered_prose(
    lines: list[str],
) -> None:
    schema = json.loads((ROOT / close_pack.SCHEMA_REL).read_text(encoding="utf-8"))
    source = _valid_source()
    source["report_sections"][0]["body_lines"] = lines
    assert not Draft202012Validator(schema).is_valid(source)
    with pytest.raises(close_pack.ClosePackError, match="REPORT_NONCLAIM_CONTRADICTION"):
        close_pack._require_report_nonclaim_posture(source)


@pytest.mark.parametrize(
    "value",
    (
        "QA passed; acceptance was not granted.",
        "No deployment was completed, but OPS ran.",
        "Acceptance was not granted; Product Owner closeout is complete.",
        "Deployment is incomplete; Live QA ran.",
        "QA wasn't reviewed but passed.",
        "Acceptance wasn't requested but granted.",
        "Deployment wasn't planned but executed.",
        "OPS wasn't prepared but performed.",
        "QA did not run but passed.",
        "Product Owner didn't deliberate but approved closeout.",
        "Candidate remains pending;QA passed.",
        "Candidate remains pending:Acceptance confirmed.",
    ),
)
def test_nonclaim_guard_rejects_affirmative_claim_in_mixed_clause(
    value: str,
) -> None:
    schema = json.loads((ROOT / close_pack.SCHEMA_REL).read_text(encoding="utf-8"))
    source = _valid_source()
    source["report_sections"][0]["body_lines"][0] = value
    assert not Draft202012Validator(schema).is_valid(source)
    with pytest.raises(close_pack.ClosePackError, match="REPORT_NONCLAIM_CONTRADICTION"):
        close_pack._require_report_nonclaim_posture(source)


@pytest.mark.parametrize(
    ("value", "expected"),
    (
        ("Workflow run identifier: 12345", "FEEDBACK_DEPENDENCY_PROHIBITED"),
        ("Product Owner closeout is complete.", "REPORT_NONCLAIM_CONTRADICTION"),
        ("Quality assurance passed.", "REPORT_NONCLAIM_CONTRADICTION"),
    ),
)
def test_runtime_semantic_defenses_fail_before_outputs(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    value: str,
    expected: str,
) -> None:
    source = _valid_source()
    source["report_sections"][0]["body_lines"][0] = value
    repo = _init_repo(tmp_path, source=source)
    monkeypatch.setattr(close_pack, "_validate_source", lambda payload, schema: payload)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert f"EPIC_CLOSE_PACK_ERROR:{expected}" in capsys.readouterr().err
    assert not (repo / REPORT_REL).exists()
    assert not (repo / MANIFEST_REL).exists()


@pytest.mark.parametrize(
    "lines",
    (
        ["# HDE-EPIC123 Close Candidate"],
        ["## Source bindings"],
        ["## **Source bindings**"],
        ["    ## Output bindings"],
        ["Source bindings", "---"],
        ["Source bindings", "    ---"],
        ["```markdown", "## Source bindings", "```"],
        ["- Source bindings", "    ---"],
        ["1. Scope", "    ## Output bindings"],
        ["> " * 17 + "## Explicit nonclaims"],
        ["[source]: docs/source.md"],
        ["<h2>Source bindings</h2>"],
        ["prefix <h2", "class=canonical>Source bindings"],
        ["See <https://example.invalid/path>."],
    ),
)
def test_schema_and_runtime_reject_structural_report_body_lines(
    lines: list[str],
) -> None:
    schema = json.loads((ROOT / close_pack.SCHEMA_REL).read_text(encoding="utf-8"))
    source = _valid_source()
    source["report_sections"][0]["body_lines"] = lines
    assert not Draft202012Validator(schema).is_valid(source)
    with pytest.raises(close_pack.ClosePackError, match="REPORT_SECTION_AMBIGUOUS"):
        close_pack._require_report_structure(source)


@pytest.mark.parametrize(
    "heading",
    (
        "**Source bindings**",
        "[Output bindings](#output-bindings)",
        "[Source bindings]",
        "<em>Explicit nonclaims</em>",
    ),
)
def test_schema_and_runtime_reject_markup_in_dedicated_report_headings(
    heading: str,
) -> None:
    schema = json.loads((ROOT / close_pack.SCHEMA_REL).read_text(encoding="utf-8"))
    source = _valid_source()
    source["report_sections"][0]["heading"] = heading
    assert not Draft202012Validator(schema).is_valid(source)
    with pytest.raises(close_pack.ClosePackError, match="REPORT_SECTION_AMBIGUOUS"):
        close_pack._require_report_structure(source)


@pytest.mark.parametrize(
    "heading",
    (
        "API_v2 posture",
        "PR-05 scope",
        "Validation posture (bounded)",
        "Plan/path alignment",
    ),
)
def test_closed_report_heading_contract_rejects_unregistered_values(
    heading: str,
) -> None:
    schema = json.loads((ROOT / close_pack.SCHEMA_REL).read_text(encoding="utf-8"))
    source = _valid_source()
    source["report_sections"][0]["heading"] = heading
    assert not Draft202012Validator(schema).is_valid(source)
    with pytest.raises(close_pack.ClosePackError, match="REPORT_SECTION_AMBIGUOUS"):
        close_pack._require_report_structure(source)


@pytest.mark.parametrize("heading", close_pack.REPORT_SECTION_HEADINGS)
def test_closed_report_heading_contract_admits_registered_values(
    heading: str,
) -> None:
    schema = json.loads((ROOT / close_pack.SCHEMA_REL).read_text(encoding="utf-8"))
    source = _valid_source()
    source["report_sections"][0]["heading"] = heading
    source["report_sections"] = [source["report_sections"][0]]
    assert Draft202012Validator(schema).is_valid(source)
    close_pack._require_report_nonclaim_posture(source)
    close_pack._require_report_structure(source)


@pytest.mark.parametrize(
    "line",
    (
        "Source bindings remain deterministic prose.",
        "**Source bindings** remain deterministic prose.",
        "### Source bindings",
        "### **Source bindings**",
        "Use `tracked bytes` deterministically.",
        "A [local plan](docs/plans/candidate.md) remains tracked prose.",
        "    Indented plain text remains nonstructural.",
    ),
)
def test_closed_report_body_contract_rejects_unregistered_lines(line: str) -> None:
    schema = json.loads((ROOT / close_pack.SCHEMA_REL).read_text(encoding="utf-8"))
    source = _valid_source()
    source["report_sections"][0]["body_lines"][0] = line
    assert not Draft202012Validator(schema).is_valid(source)
    with pytest.raises(close_pack.ClosePackError, match="REPORT_NONCLAIM_CONTRADICTION"):
        close_pack._require_report_nonclaim_posture(source)


@pytest.mark.parametrize("line", close_pack.REPORT_BODY_LINES)
def test_closed_report_body_contract_admits_registered_lines(line: str) -> None:
    schema = json.loads((ROOT / close_pack.SCHEMA_REL).read_text(encoding="utf-8"))
    source = _valid_source()
    source["report_sections"][0]["body_lines"] = [line]
    assert Draft202012Validator(schema).is_valid(source)
    close_pack._require_report_nonclaim_posture(source)
    close_pack._require_report_structure(source)


@pytest.mark.parametrize(
    "control",
    (
        "\x00",
        "\t",
        "\x1b",
        "\x7f",
        "\x85",
        "\u061c",
        "\u200e",
        "\u2028",
        "\u2029",
        "\u202e",
        "\u2066",
        "\u206f",
        "\ud800",
    ),
)
def test_schema_and_runtime_reject_report_text_controls(control: str) -> None:
    schema = json.loads((ROOT / close_pack.SCHEMA_REL).read_text(encoding="utf-8"))
    source = _valid_source()
    source["report_sections"][0]["body_lines"][0] = f"tracked{control}text"
    assert not Draft202012Validator(schema).is_valid(source)
    with pytest.raises(close_pack.ClosePackError, match="REPORT_SECTION_AMBIGUOUS"):
        close_pack._require_report_structure(source)


@pytest.mark.parametrize("field", ("heading", "body"))
def test_schema_and_runtime_reject_final_lf_in_report_text(field: str) -> None:
    schema = json.loads((ROOT / close_pack.SCHEMA_REL).read_text(encoding="utf-8"))
    source = _valid_source()
    if field == "heading":
        source["report_sections"][0]["heading"] += "\n"
    else:
        source["report_sections"][0]["body_lines"][0] += "\n"
    assert not Draft202012Validator(schema).is_valid(source)
    with pytest.raises(close_pack.ClosePackError, match="REPORT_SECTION_AMBIGUOUS"):
        close_pack._require_report_structure(source)


def test_report_body_remains_unicode_capable() -> None:
    schema = json.loads((ROOT / close_pack.SCHEMA_REL).read_text(encoding="utf-8"))
    source = _valid_source()
    source["report_sections"][0]["body_lines"][0] = (
        "Tracked résumé evidence remains deterministic."
    )
    assert Draft202012Validator(schema).is_valid(source)
    close_pack._require_report_structure(source)


@pytest.mark.parametrize("control", ("\x00", "\n", "\ud800", "\u202e"))
def test_writer_rejects_report_control_without_outputs(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    control: str,
) -> None:
    source = _valid_source()
    source["report_sections"][0]["body_lines"][0] = f"tracked text{control}"
    repo = _init_repo(tmp_path, source=source)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert "EPIC_CLOSE_PACK_ERROR:SOURCE_SCHEMA_INVALID" in capsys.readouterr().err
    assert not (repo / REPORT_REL).exists()
    assert not (repo / MANIFEST_REL).exists()


def test_writer_runtime_defense_rejects_reserved_body_heading_without_outputs(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    source = _valid_source()
    source["report_sections"][0]["body_lines"][0] = "## Explicit nonclaims"
    repo = _init_repo(tmp_path, source=source)
    monkeypatch.setattr(close_pack, "_validate_source", lambda payload, schema: payload)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert "EPIC_CLOSE_PACK_ERROR:REPORT_SECTION_AMBIGUOUS" in capsys.readouterr().err
    assert not (repo / REPORT_REL).exists()
    assert not (repo / MANIFEST_REL).exists()


def test_writer_schema_rejects_structural_body_before_outputs(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    source = _valid_source()
    source["report_sections"][0]["body_lines"] = [
        "```markdown",
        "## Source bindings",
        "```",
    ]
    repo = _init_repo(tmp_path, source=source)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert "EPIC_CLOSE_PACK_ERROR:SOURCE_SCHEMA_INVALID" in capsys.readouterr().err
    assert not (repo / REPORT_REL).exists()
    assert not (repo / MANIFEST_REL).exists()


@pytest.mark.parametrize(
    "mutation",
    ("reserved-heading-closing-hashes", "duplicate-heading-closing-hashes"),
)
def test_report_heading_aliases_fail_before_publication(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    mutation: str,
) -> None:
    source = _valid_source()
    if mutation == "reserved-heading-closing-hashes":
        source["report_sections"][0]["heading"] = "Source bindings ##"
    else:
        source["report_sections"][1]["heading"] = "Delivered scope ##"
    repo = _init_repo(tmp_path, source=source)
    monkeypatch.setattr(close_pack, "_validate_source", lambda payload, schema: payload)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert "EPIC_CLOSE_PACK_ERROR:REPORT_SECTION_AMBIGUOUS" in capsys.readouterr().err
    assert not (repo / REPORT_REL).exists()
    assert not (repo / MANIFEST_REL).exists()


def test_shortcut_reference_reserved_heading_fails_runtime_defense(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    source = _valid_source()
    source["report_sections"][0]["heading"] = "[Source bindings]"
    source["report_sections"][0]["body_lines"] = ["[Source bindings]: /local"]
    repo = _init_repo(tmp_path, source=source)
    monkeypatch.setattr(close_pack, "_validate_source", lambda payload, schema: payload)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert "EPIC_CLOSE_PACK_ERROR:REPORT_SECTION_AMBIGUOUS" in capsys.readouterr().err
    assert not (repo / REPORT_REL).exists()
    assert not (repo / MANIFEST_REL).exists()


@pytest.mark.parametrize(
    "path",
    (
        "",
        ".",
        "..",
        "/absolute/path",
        "plans//epic123.md",
        "plans/./epic123.md",
        "plans/../epic123.md",
        "plans\\epic123.md",
    ),
)
def test_schema_rejects_noncanonical_repository_paths(path: str) -> None:
    schema = json.loads((ROOT / close_pack.SCHEMA_REL).read_text(encoding="utf-8"))
    source = _valid_source()
    source["plan_path"] = path
    assert not Draft202012Validator(schema).is_valid(source)


@pytest.mark.parametrize(
    ("location", "value"),
    (
        ("binding", "receipt"),
        ("binding", "workflow_results"),
        ("evidence_path", "audit/hosted-result.json"),
        ("evidence_path", "evidence/workflow-results.json"),
        ("plan_path", "catalog/manifest.json"),
        ("heading", "Mutable attestation"),
        ("body", "Later commit " + "b" * 40),
    ),
)
def test_writer_rejects_feedback_dependencies_without_outputs(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    location: str,
    value: str,
) -> None:
    source = _valid_source()
    if location == "binding":
        source["evidence_inputs"][0]["binding"] = value
    elif location == "evidence_path":
        source["evidence_inputs"][0]["path"] = value
    elif location == "plan_path":
        source["plan_path"] = value
    elif location == "heading":
        source["report_sections"][0]["heading"] = value
    else:
        source["report_sections"][0]["body_lines"][0] = value
    repo = _init_repo(tmp_path, source=source)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert not (repo / REPORT_REL).exists()
    assert not (repo / MANIFEST_REL).exists()


def test_canonical_nonclaims_render_fixed_explicit_statements(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source = _valid_source()
    repo = _init_repo(tmp_path, source=source)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 0
    report = (repo / REPORT_REL).read_text(encoding="utf-8")
    manifest = json.loads((repo / MANIFEST_REL).read_text(encoding="utf-8"))
    for code, statement in close_pack.NONCLAIM_TEXT.items():
        assert f"- {statement}" in report
        assert {"code": code, "statement": statement} in manifest["nonclaims"]


def test_actual_head_cannot_enter_through_nonclaims(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path)
    source = _valid_source()
    source["nonclaims"][0] = _git(repo, "rev-parse", "HEAD")
    _write_json(repo / SOURCE_REL, source)
    _git(repo, "add", SOURCE_REL)
    _git(repo, "commit", "-m", "inject prohibited nonclaim identifier")
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert not (repo / REPORT_REL).exists()
    assert not (repo / MANIFEST_REL).exists()


@pytest.mark.parametrize(
    ("keyword", "reference"),
    (
        ("$ref", "https://example.invalid/schema.json"),
        ("$dynamicRef", "https://example.invalid/dynamic.json"),
        ("$ref", "#/$defs/missing"),
    ),
)
def test_unsafe_schema_reference_is_rejected_without_network_or_outputs(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    keyword: str,
    reference: str,
) -> None:
    repo = _init_repo(tmp_path)
    schema_path = repo / close_pack.SCHEMA_REL
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    schema["properties"]["plan_path"][keyword] = reference
    _write_json(schema_path, schema)
    _git(repo, "add", close_pack.SCHEMA_REL)
    _git(repo, "commit", "-m", "add prohibited external schema reference")

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert not (repo / REPORT_REL).exists()
    assert not (repo / MANIFEST_REL).exists()


@pytest.mark.parametrize(
    ("rel", "payload"),
    (
        (
            "plans/epic123.md",
            b"No hosted receipt, run ID, or current attestation is used.\n"
            + b"a" * 64
            + b"\n",
        ),
        (
            "evidence/determinism.txt",
            b"No later commit or hosted result is a candidate input.\n",
        ),
        (
            "evidence/scope.json",
            b'{"nonclaim":"Source commit identity is not embedded."}\n',
        ),
        ("evidence/scope.json", b"\xff\xfe\x00\x01"),
    ),
)
def test_tracked_causal_payloads_are_opaque_byte_inputs(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    rel: str,
    payload: bytes,
) -> None:
    repo = _init_repo(tmp_path)
    (repo / rel).write_bytes(payload)
    _git(repo, "add", rel)
    _git(repo, "commit", "-m", "change tracked causal payload")

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 0
    manifest = json.loads((repo / MANIFEST_REL).read_text(encoding="utf-8"))
    bindings = [manifest["inputs"]["plan"], *manifest["inputs"]["evidence"]]
    binding = next(item for item in bindings if item["path"] == rel)
    assert binding["sha256"] == hashlib.sha256(payload).hexdigest()


def test_mismatched_derived_output_binding_fails_without_outputs(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source = _valid_source()
    source["key_outputs"]["close_report"] = "audit/EPIC-999_close_report.md"
    repo = _init_repo(tmp_path, source=source)

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert not (repo / REPORT_REL).exists()
    assert not (repo / MANIFEST_REL).exists()


def test_complete_candidate_lifecycle_is_committable_exact_and_idempotent(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 0
    assert {path.as_posix() for path in (repo / "audit").glob("EPIC-123*")} == {
        (repo / REPORT_REL).as_posix(),
        (repo / MANIFEST_REL).as_posix(),
    }
    first_report = (repo / REPORT_REL).read_bytes()
    first_manifest = (repo / MANIFEST_REL).read_bytes()
    assert first_report.endswith(b"\n") and b"\r" not in first_report
    assert first_manifest.endswith(b"\n") and not first_manifest.startswith(b"\xef\xbb\xbf")
    parsed = json.loads(first_manifest)
    assert first_manifest == (
        json.dumps(parsed, ensure_ascii=True, separators=(",", ":"), sort_keys=True)
        + "\n"
    ).encode("utf-8")
    assert parsed["outputs"]["close_report"]["path"] == REPORT_REL
    assert parsed["outputs"]["close_manifest"]["path"] == MANIFEST_REL
    assert _git(repo, "status", "--porcelain=v1", "--untracked-files=all").splitlines() == [
        f"?? {MANIFEST_REL}",
        f"?? {REPORT_REL}",
    ]

    _git(repo, "add", REPORT_REL, MANIFEST_REL)
    _git(repo, "commit", "-m", "commit complete candidate")
    exact_head = _git(repo, "rev-parse", "HEAD")
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--check") == 0
    assert _git(repo, "rev-parse", "HEAD") == exact_head

    before = {
        REPORT_REL: _metadata(repo / REPORT_REL),
        MANIFEST_REL: _metadata(repo / MANIFEST_REL),
    }
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 0
    assert (repo / REPORT_REL).read_bytes() == first_report
    assert (repo / MANIFEST_REL).read_bytes() == first_manifest
    assert before == {
        REPORT_REL: _metadata(repo / REPORT_REL),
        MANIFEST_REL: _metadata(repo / MANIFEST_REL),
    }
    assert _git(repo, "diff", "--exit-code") == ""
    assert _git(repo, "status", "--porcelain=v1", "--untracked-files=all") == ""


def test_check_mode_is_nonwriting_for_bytes_mode_and_metadata(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path)
    _generate_and_commit(repo, monkeypatch)
    paths = [
        repo / SOURCE_REL,
        repo / close_pack.SCHEMA_REL,
        repo / "plans/epic123.md",
        repo / "evidence/determinism.txt",
        repo / "evidence/scope.json",
        repo / REPORT_REL,
        repo / MANIFEST_REL,
    ]
    before = {path: (_read_noatime(path), _metadata(path)) for path in paths}
    repository_before = close_pack._repository_metadata(repo)
    git_control_paths = close_pack._git_control_paths(
        close_pack._establish_git_context(repo)
    )
    git_control_before = close_pack._git_control_state(git_control_paths)

    def forbidden_publish(*_args: object, **_kwargs: object) -> None:
        raise AssertionError("check mode attempted publication")

    monkeypatch.setattr(close_pack, "_publish_pair", forbidden_publish)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--check") == 0
    assert repository_before == close_pack._repository_metadata(repo)
    assert git_control_before == close_pack._git_control_state(git_control_paths)
    assert before == {path: (_read_noatime(path), _metadata(path)) for path in paths}
    assert _git(repo, "status", "--porcelain=v1", "--untracked-files=all") == ""


def test_check_mode_preserves_stale_atimes_on_all_candidate_files(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path)
    _generate_and_commit(repo, monkeypatch)
    paths = [
        repo / SOURCE_REL,
        repo / close_pack.SCHEMA_REL,
        repo / "plans/epic123.md",
        repo / "evidence/determinism.txt",
        repo / "evidence/scope.json",
        repo / REPORT_REL,
        repo / MANIFEST_REL,
    ]
    stale_atime_ns = 946_684_800_000_000_000
    for path in paths:
        metadata = path.stat()
        os.utime(
            path,
            ns=(stale_atime_ns, metadata.st_mtime_ns),
            follow_symlinks=False,
        )
    before = {path: path.stat().st_atime_ns for path in paths}

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--check") == 0
    assert before == {path: path.stat().st_atime_ns for path in paths}
    assert _git(repo, "status", "--porcelain=v1", "--untracked-files=all") == ""


@pytest.mark.parametrize("mode", ("check", "write"))
def test_modes_preserve_stale_git_control_atime_without_mutating_it(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mode: str,
) -> None:
    repo = _init_repo(tmp_path)
    _generate_and_commit(repo, monkeypatch)
    head_path = repo / ".git/HEAD"
    metadata = head_path.stat()
    stale_atime_ns = 946_684_800_000_000_000
    os.utime(
        head_path,
        ns=(stale_atime_ns, metadata.st_mtime_ns),
        follow_symlinks=False,
    )

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, f"--{mode}") == 0
    assert head_path.stat().st_atime_ns == stale_atime_ns


@pytest.mark.parametrize("mode", ("check", "write"))
def test_modes_preserve_stale_loose_object_atime(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mode: str,
) -> None:
    repo = _init_repo(tmp_path)
    _generate_and_commit(repo, monkeypatch)
    source_object = _git(repo, "rev-parse", f"HEAD:{SOURCE_REL}")
    object_path = repo / ".git/objects" / source_object[:2] / source_object[2:]
    metadata = object_path.stat()
    stale_atime_ns = 946_684_800_000_000_000
    os.utime(
        object_path,
        ns=(stale_atime_ns, metadata.st_mtime_ns),
        follow_symlinks=False,
    )

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, f"--{mode}") == 0
    assert object_path.stat().st_atime_ns == stale_atime_ns
    assert _git(repo, "status", "--porcelain=v1", "--untracked-files=all") == ""


@pytest.mark.parametrize("mode", ("check", "write"))
@pytest.mark.parametrize("control", ("config", "head_ref"))
def test_modes_preserve_stale_config_and_ref_atime(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mode: str,
    control: str,
) -> None:
    repo = _init_repo(tmp_path)
    _generate_and_commit(repo, monkeypatch)
    if control == "config":
        path = repo / ".git/config"
    else:
        head = _read_noatime(repo / ".git/HEAD").decode("ascii").strip()
        assert head.startswith("ref: ")
        path = repo / ".git" / head.removeprefix("ref: ")
    metadata = path.stat()
    stale_atime_ns = 946_684_800_000_000_000
    os.utime(
        path,
        ns=(stale_atime_ns, metadata.st_mtime_ns),
        follow_symlinks=False,
    )
    before = (_read_noatime(path), _metadata(path))

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, f"--{mode}") == 0
    assert before == (_read_noatime(path), _metadata(path))


def test_noncanonical_loose_object_header_at_canonical_path_fails(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    repo = _init_repo(tmp_path)
    evidence_path = repo / "evidence/determinism.txt"
    evidence_path.write_bytes(b"x")
    _git(repo, "add", "evidence/determinism.txt")
    _git(repo, "commit", "-m", "use one-byte evidence blob")
    _generate_and_commit(repo, monkeypatch)

    algorithm = _git(repo, "rev-parse", "--show-object-format")
    object_id = _git(repo, "rev-parse", "HEAD:evidence/determinism.txt")
    assert object_id == close_pack._git_blob_id(b"x", algorithm)
    object_path = repo / ".git/objects" / object_id[:2] / object_id[2:]
    assert object_path.is_file()
    original_mode = stat.S_IMODE(object_path.stat().st_mode)
    object_path.chmod(original_mode | stat.S_IWUSR)
    try:
        object_path.write_bytes(zlib.compress(b"blob 01\0x"))
    finally:
        object_path.chmod(original_mode)
    index_path = repo / ".git/index"
    index_before = _read_noatime(index_path)

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--check") == 1
    captured = capsys.readouterr()
    assert "EPIC_CLOSE_PACK_ERROR:GIT_OBJECT_INVALID" in captured.err
    assert _read_noatime(index_path) == index_before


@pytest.mark.skipif(os.name != "posix", reason="requires POSIX byte-path semantics")
def test_unrelated_clean_non_utf8_tracked_path_keeps_lifecycle_reachable(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path)
    name = b"unrelated-\xff.txt"
    byte_path = os.path.join(os.fsencode(repo), name)
    descriptor = os.open(byte_path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    try:
        os.write(descriptor, b"unrelated tracked bytes\n")
    finally:
        os.close(descriptor)
    _git(repo, "add", "--all")
    _git(repo, "commit", "-m", "add non-UTF8 tracked path")
    listed = subprocess.run(
        ("git", "ls-files", "-z"),
        cwd=repo,
        capture_output=True,
        check=True,
    ).stdout
    assert name + b"\0" in listed

    _generate_and_commit(repo, monkeypatch)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--check") == 0
    assert _git(repo, "status", "--porcelain=v1", "--untracked-files=all") == ""


def test_packed_object_lifecycle_reaches_clean_exact_head(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path)
    _git(repo, "gc", "--prune=now")
    assert not any((repo / ".git/objects").glob("[0-9a-f][0-9a-f]/*"))

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 0
    _git(repo, "add", REPORT_REL, MANIFEST_REL)
    _git(repo, "commit", "-m", "commit packed candidate")
    _git(repo, "gc", "--prune=now")
    exact_head = _git(repo, "rev-parse", "HEAD")

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--check") == 0
    assert _git(repo, "rev-parse", "HEAD") == exact_head
    assert _git(repo, "status", "--porcelain=v1", "--untracked-files=all") == ""


def test_delta_backed_causal_object_preserves_stale_pack_metadata(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path)
    evidence_path = repo / "evidence/determinism.txt"
    evidence_path.write_bytes(b"A" * 60_000 + b"base\n")
    _git(repo, "add", "evidence/determinism.txt")
    _git(repo, "commit", "-m", "add delta base evidence")
    evidence_path.write_bytes(b"A" * 50_000 + b"candidate\n")
    _git(repo, "add", "evidence/determinism.txt")
    _git(repo, "commit", "-m", "select delta target evidence")
    _generate_and_commit(repo, monkeypatch)
    causal_oid = _git(repo, "rev-parse", "HEAD:evidence/determinism.txt")

    _git(repo, "repack", "-adf", "--depth=50", "--window=50")
    pack_directory = repo / ".git/objects/pack"
    pack_paths = sorted(pack_directory.glob("*.pack"))
    index_paths = sorted(pack_directory.glob("*.idx"))
    assert len(pack_paths) == len(index_paths) == 1
    assert not (repo / ".git/objects" / causal_oid[:2] / causal_oid[2:]).exists()
    verified = subprocess.run(
        ("git", "verify-pack", "-v", str(index_paths[0])),
        cwd=repo,
        capture_output=True,
        check=True,
        text=True,
    ).stdout.splitlines()
    causal_fields = next(line.split() for line in verified if line.startswith(causal_oid))
    assert causal_fields[1] == "blob"
    assert len(causal_fields) >= 7
    assert int(causal_fields[5]) >= 1

    stale_atime_ns = 946_684_800_000_000_000
    protected_paths = [*pack_paths, *index_paths]
    for path in protected_paths:
        metadata = path.stat()
        os.utime(
            path,
            ns=(stale_atime_ns, metadata.st_mtime_ns),
            follow_symlinks=False,
        )
    protected_before = {path: _metadata(path) for path in protected_paths}

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--check") == 0
    assert protected_before == {path: _metadata(path) for path in protected_paths}
    assert _git(repo, "status", "--porcelain=v1", "--untracked-files=all") == ""


def test_unrelated_clean_tracked_symlink_preserves_terminal_reachability(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path)
    link = repo / "tracked-link"
    link.symlink_to("target-one")
    _git(repo, "add", "tracked-link")
    _git(repo, "commit", "-m", "add unrelated tracked symlink")
    symlink_atime_before_write = link.lstat().st_atime_ns

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 0
    assert link.lstat().st_atime_ns == symlink_atime_before_write
    _git(repo, "add", REPORT_REL, MANIFEST_REL)
    _git(repo, "commit", "-m", "commit complete candidate")
    index_path = repo / ".git/index"
    index_before_check = _read_noatime(index_path)
    index_metadata_before_check = _metadata(index_path)
    repository_before_check = close_pack._repository_metadata(repo)
    symlink_atime_before_check = link.lstat().st_atime_ns
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--check") == 0
    assert link.lstat().st_atime_ns == symlink_atime_before_check
    assert close_pack._repository_metadata(repo) == repository_before_check
    assert _read_noatime(index_path) == index_before_check
    assert _metadata(index_path) == index_metadata_before_check

    link.unlink()
    link.symlink_to("target-two")
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--check") == 1


@pytest.mark.parametrize("mode", ("check", "write"))
def test_checksum_valid_poisoned_symlink_stat_cache_cannot_hide_target_change(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    mode: str,
) -> None:
    repo = _init_repo(tmp_path)
    rel = "tracked-link"
    link = repo / rel
    link.symlink_to("target-one")
    _git(repo, "add", rel)
    _git(repo, "commit", "-m", "add unrelated tracked symlink")
    _generate_and_commit(repo, monkeypatch)

    tree_mode, object_type, object_id, path = _git(
        repo, "ls-tree", "HEAD", "--", rel
    ).split()
    algorithm = _git(repo, "rev-parse", "--show-object-format")
    assert (tree_mode, object_type, path) == ("120000", "blob", rel)
    assert close_pack._git_blob_id(b"target-one", algorithm) == object_id
    assert close_pack._git_blob_id(b"target-two", algorithm) != object_id

    original_blob_id = close_pack._git_blob_id

    def poisoned_blob_id(payload: bytes, selected_algorithm: str) -> str:
        if payload == b"target-two":
            return object_id
        return original_blob_id(payload, selected_algorithm)

    monkeypatch.setattr(close_pack, "_git_blob_id", poisoned_blob_id)

    link.unlink()
    link.symlink_to("target-two")
    index_path = repo / ".git/index"
    poisoned_index = _replace_index_stat_cache_with_worktree_metadata(repo, rel)
    index_metadata_before = _metadata(index_path)
    repository_before = close_pack._repository_metadata(repo)
    outputs_before = {
        REPORT_REL: _read_noatime(repo / REPORT_REL),
        MANIFEST_REL: _read_noatime(repo / MANIFEST_REL),
    }

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, f"--{mode}") == 1
    captured = capsys.readouterr()
    assert "EPIC_CLOSE_PACK_ERROR:DIRTY_TREE" in captured.err
    _assert_only_symlink_atime_may_differ(
        repository_before,
        close_pack._repository_metadata(repo),
        rel,
        require_change=False,
    )
    assert _read_noatime(index_path) == poisoned_index
    assert _metadata(index_path) == index_metadata_before
    assert outputs_before == {
        REPORT_REL: _read_noatime(repo / REPORT_REL),
        MANIFEST_REL: _read_noatime(repo / MANIFEST_REL),
    }
    assert link.readlink() == Path("target-two")


def test_check_allows_only_relatime_symlink_atime_update(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    mount_flags = os.statvfs(tmp_path).f_flag
    relatime = getattr(os, "ST_RELATIME", 0)
    noatime = getattr(os, "ST_NOATIME", 0)
    if not relatime or not mount_flags & relatime or mount_flags & noatime:
        pytest.skip("test requires a relatime mount without noatime")

    repo = _init_repo(tmp_path)
    rel = "tracked-link"
    link = repo / rel
    link.symlink_to("target-one")
    _git(repo, "add", rel)
    _git(repo, "commit", "-m", "add unrelated tracked symlink")
    _generate_and_commit(repo, monkeypatch)

    stale_atime_ns = 946_684_800_000_000_000
    metadata = link.lstat()
    os.utime(
        link,
        ns=(stale_atime_ns, metadata.st_mtime_ns),
        follow_symlinks=False,
    )
    index_path = repo / ".git/index"
    index_before = _replace_index_stat_cache_with_worktree_metadata(repo, rel)
    index_metadata_before = _metadata(index_path)
    repository_before = close_pack._repository_metadata(repo)
    assert repository_before[rel][2] == stale_atime_ns

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--check") == 0
    repository_after = close_pack._repository_metadata(repo)
    _assert_only_symlink_atime_may_differ(
        repository_before,
        repository_after,
        rel,
        require_change=True,
    )
    assert repository_after[rel][2] > repository_before[rel][2]
    assert _read_noatime(index_path) == index_before
    assert _metadata(index_path) == index_metadata_before
    assert link.readlink() == Path("target-one")


@pytest.mark.skipif(os.name != "posix", reason="requires POSIX symlink atime semantics")
def test_write_allows_only_inspected_relatime_symlink_atime_updates(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    mount_flags = os.statvfs(tmp_path).f_flag
    relatime = getattr(os, "ST_RELATIME", 0)
    noatime = getattr(os, "ST_NOATIME", 0)
    if not relatime or not mount_flags & relatime or mount_flags & noatime:
        pytest.skip("test requires a relatime mount without noatime")

    repo = _init_repo(tmp_path)
    links = {
        "tracked-link-a": "target-one",
        "tracked-link-b": "target-two",
    }
    for rel, target in links.items():
        (repo / rel).symlink_to(target)
    _git(repo, "add", *links)
    _git(repo, "commit", "-m", "add unrelated tracked symlinks")
    _generate_and_commit(repo, monkeypatch)

    stale_atime_ns = 946_684_800_000_000_000
    for rel in links:
        link = repo / rel
        metadata = link.lstat()
        os.utime(
            link,
            ns=(stale_atime_ns, metadata.st_mtime_ns),
            follow_symlinks=False,
        )
    index_path = repo / ".git/index"
    index_before = (_read_noatime(index_path), _metadata(index_path))
    head_before = _git(repo, "rev-parse", "HEAD")
    outputs_before = {
        rel: (_read_noatime(repo / rel), _metadata(repo / rel))
        for rel in (REPORT_REL, MANIFEST_REL)
    }
    repository_before = close_pack._repository_metadata(repo)
    assert all(repository_before[rel][2] == stale_atime_ns for rel in links)

    timestamp_api_called = False

    def reject_timestamp_write(*_args: object, **_kwargs: object) -> None:
        nonlocal timestamp_api_called
        timestamp_api_called = True
        raise AssertionError("write mode attempted explicit timestamp mutation")

    monkeypatch.setattr(close_pack.os, "utime", reject_timestamp_write)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 0

    repository_after = close_pack._repository_metadata(repo)
    _assert_only_symlink_atime_may_differ(
        repository_before,
        repository_after,
        set(links),
        require_change=True,
    )
    assert all(
        repository_after[rel][2] > repository_before[rel][2] for rel in links
    )
    assert not timestamp_api_called
    assert _git(repo, "rev-parse", "HEAD") == head_before
    assert index_before == (_read_noatime(index_path), _metadata(index_path))
    assert outputs_before == {
        rel: (_read_noatime(repo / rel), _metadata(repo / rel))
        for rel in (REPORT_REL, MANIFEST_REL)
    }
    assert {
        rel: os.readlink(repo / rel).encode("utf-8") for rel in links
    } == {rel: target.encode("utf-8") for rel, target in links.items()}


@pytest.mark.skipif(os.name != "posix", reason="requires byte-preserving POSIX symlinks")
def test_write_compares_non_utf8_symlink_target_to_exact_head_blob(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path)
    rel = "tracked-byte-link"
    target = b"target-\xff-byte"
    os.symlink(target, os.fsencode(repo / rel))
    _git(repo, "add", rel)
    _git(repo, "commit", "-m", "add byte-preserving tracked symlink")

    context = close_pack._establish_git_context(repo)
    store = close_pack._GitObjectStore(context)
    entry = close_pack._tree_entries(context, store)[rel]
    assert entry.mode == "120000"
    assert close_pack._git_blob_payload(context, entry.object_id, store) == target
    assert os.readlink(os.fsencode(repo / rel)) == target

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 0
    assert os.readlink(os.fsencode(repo / rel)) == target
    assert close_pack._git_blob_payload(context, entry.object_id, store) == target


def test_all_candidate_bytes_are_rendered_before_publication(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path)
    original = close_pack._publish_pair
    observed: dict[str, bytes] = {}

    def inspect_pair(
        root: Path,
        outputs: dict[str, bytes],
        report_rel: str,
        manifest_rel: str,
        expected_preimages,
        verifier,
    ) -> None:
        observed.update(outputs)
        assert set(outputs) == {REPORT_REL, MANIFEST_REL}
        assert (report_rel, manifest_rel) == (REPORT_REL, MANIFEST_REL)
        assert all(payload.endswith(b"\n") for payload in outputs.values())
        original(
            root,
            outputs,
            report_rel,
            manifest_rel,
            expected_preimages,
            verifier,
        )

    monkeypatch.setattr(close_pack, "_publish_pair", inspect_pair)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 0
    assert observed[REPORT_REL] == (repo / REPORT_REL).read_bytes()
    assert observed[MANIFEST_REL] == (repo / MANIFEST_REL).read_bytes()


def test_publication_uses_report_first_manifest_commit_point_order(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path)
    boundaries: list[str] = []
    monkeypatch.setattr(close_pack, "_publication_boundary", boundaries.append)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 0
    assert boundaries == [
        "report_staged",
        "manifest_staged",
        "staged_pair_verified",
        "report_installed",
        "report_directory_synced",
        "manifest_installed",
        "manifest_directory_synced",
        "pair_verified",
        "report_residue_removed",
        "manifest_residue_removed",
        "cleanup_directory_synced",
    ]


def test_both_staged_outputs_are_verified_before_any_canonical_install(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path)
    old_report, old_manifest = _generate_and_commit(repo, monkeypatch)
    old_metadata = {
        REPORT_REL: _metadata(repo / REPORT_REL),
        MANIFEST_REL: _metadata(repo / MANIFEST_REL),
    }
    source = _valid_source()
    source["report_sections"][0]["body_lines"].append(
        "Recovery requires a fresh derivation from tracked inputs."
    )
    _write_json(repo / SOURCE_REL, source)
    _git(repo, "add", SOURCE_REL)
    _git(repo, "commit", "-m", "advance candidate source")

    installed: list[str] = []
    original_install = close_pack._install_staged_output

    def observe_install(
        anchor: close_pack.OutputAnchor,
        staged_name: str,
        expected: bytes,
        installed_outputs: list[close_pack.InstalledOutput],
        install_attempts: set[str],
    ) -> None:
        installed.append(anchor.rel)
        original_install(
            anchor, staged_name, expected, installed_outputs, install_attempts
        )

    def corrupt_staged_manifest(boundary: str) -> None:
        if boundary != "manifest_staged":
            return
        matches = list(
            (repo / "audit").glob(
                f".{Path(MANIFEST_REL).name}.epic-close-pack.*"
            )
        )
        assert len(matches) == 1
        corrupted = bytearray(_read_noatime(matches[0]))
        corrupted[0] ^= 1
        matches[0].write_bytes(corrupted)

    monkeypatch.setattr(close_pack, "_install_staged_output", observe_install)
    monkeypatch.setattr(
        close_pack, "_publication_boundary", corrupt_staged_manifest
    )
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert installed == []
    assert _read_noatime(repo / REPORT_REL) == old_report
    assert _read_noatime(repo / MANIFEST_REL) == old_manifest
    assert old_metadata == {
        REPORT_REL: _metadata(repo / REPORT_REL),
        MANIFEST_REL: _metadata(repo / MANIFEST_REL),
    }
    assert not list((repo / "audit").glob(".*.epic-close-pack.*"))
    assert _git(repo, "status", "--porcelain=v1", "--untracked-files=all") == ""


def test_readers_at_every_publication_boundary_accept_only_complete_generations(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path)
    old_report, old_manifest = _generate_and_commit(repo, monkeypatch)
    old_outputs = {REPORT_REL: old_report, MANIFEST_REL: old_manifest}
    source = _valid_source()
    source["report_sections"][0]["body_lines"].append(
        "Recovery requires a fresh derivation from tracked inputs."
    )
    _write_json(repo / SOURCE_REL, source)
    _git(repo, "add", SOURCE_REL)
    _git(repo, "commit", "-m", "advance candidate source")
    new_outputs = _render_expected_outputs(repo, monkeypatch)
    observations: list[tuple[str, tuple[str, str], str]] = []

    def generation(rel: str) -> str:
        payload = _read_noatime(repo / rel)
        if payload == old_outputs[rel]:
            return "old"
        if payload == new_outputs[rel]:
            return "new"
        return "unknown"

    def reader_result(expected: dict[str, bytes]) -> bool:
        try:
            close_pack._read_manifest_committed_pair(
                repo, expected, REPORT_REL, MANIFEST_REL
            )
        except close_pack.ClosePackError:
            return False
        return True

    def inspect_boundary(boundary: str) -> None:
        pair_state = (generation(REPORT_REL), generation(MANIFEST_REL))
        accepts_old = reader_result(old_outputs)
        accepts_new = reader_result(new_outputs)
        assert not (accepts_old and accepts_new)
        accepted = "old" if accepts_old else "new" if accepts_new else "fail"
        observations.append((boundary, pair_state, accepted))

    monkeypatch.setattr(close_pack, "_publication_boundary", inspect_boundary)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 0
    assert observations == [
        ("report_staged", ("old", "old"), "old"),
        ("manifest_staged", ("old", "old"), "old"),
        ("staged_pair_verified", ("old", "old"), "old"),
        ("report_installed", ("new", "old"), "fail"),
        ("report_directory_synced", ("new", "old"), "fail"),
        ("manifest_installed", ("new", "new"), "new"),
        ("manifest_directory_synced", ("new", "new"), "new"),
        ("pair_verified", ("new", "new"), "new"),
        ("report_residue_removed", ("new", "new"), "new"),
        ("manifest_residue_removed", ("new", "new"), "new"),
        ("cleanup_directory_synced", ("new", "new"), "new"),
    ]


@pytest.mark.parametrize("mutated_rel", (REPORT_REL, MANIFEST_REL))
def test_target_mutation_between_write_posture_and_publication_fails_closed(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    mutated_rel: str,
) -> None:
    repo = _init_repo(tmp_path)
    concurrent = b"concurrent bytes after write-posture validation\n"
    original = close_pack._prepare_write_posture

    def mutate_after_posture(*args, **kwargs):
        posture = original(*args, **kwargs)
        (repo / mutated_rel).write_bytes(concurrent)
        return posture

    monkeypatch.setattr(close_pack, "_prepare_write_posture", mutate_after_posture)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert "EPIC_CLOSE_PACK_ERROR:OUTPUT_TARGET_CHANGED" in capsys.readouterr().err
    assert _read_noatime(repo / mutated_rel) == concurrent
    untouched_rel = MANIFEST_REL if mutated_rel == REPORT_REL else REPORT_REL
    assert not (repo / untouched_rel).exists()
    assert not list((repo / "audit").glob(".*.epic-close-pack.*"))


def test_duplicate_temp_shaped_residue_is_ambiguous_and_remains_untouched(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    repo = _init_repo(tmp_path)
    outputs = _render_expected_outputs(repo, monkeypatch)
    residues = [
        repo
        / "audit"
        / f".{Path(REPORT_REL).name}.epic-close-pack.{token:032x}"
        for token in (1, 2)
    ]
    for residue in residues:
        residue.write_bytes(outputs[REPORT_REL])
        os.chmod(residue, close_pack.OUTPUT_MODE)
    before = {residue: _read_noatime(residue) for residue in residues}

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert "EPIC_CLOSE_PACK_ERROR:RECOVERY_RESIDUE_AMBIGUOUS" in capsys.readouterr().err
    assert before == {residue: _read_noatime(residue) for residue in residues}
    assert not (repo / REPORT_REL).exists()
    assert not (repo / MANIFEST_REL).exists()


def test_index_staged_temp_shaped_residue_fails_before_cleanup(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path)
    outputs = _render_expected_outputs(repo, monkeypatch)
    residue_rel = (
        "audit/"
        f".{Path(REPORT_REL).name}.epic-close-pack.{'c' * 32}"
    )
    residue = repo / residue_rel
    residue.write_bytes(outputs[REPORT_REL])
    os.chmod(residue, close_pack.OUTPUT_MODE)
    _git(repo, "add", residue_rel)
    index_path = repo / ".git/index"
    protected_before = {
        residue: (_read_noatime(residue), _metadata(residue)),
        index_path: (_read_noatime(index_path), _metadata(index_path)),
    }

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert protected_before == {
        residue: (_read_noatime(residue), _metadata(residue)),
        index_path: (_read_noatime(index_path), _metadata(index_path)),
    }
    assert not (repo / REPORT_REL).exists()
    assert not (repo / MANIFEST_REL).exists()


@pytest.mark.parametrize("drift_rel", (REPORT_REL, MANIFEST_REL))
def test_index_only_output_drift_fails_before_publication(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    drift_rel: str,
) -> None:
    repo = _init_repo(tmp_path)
    _generate_and_commit(repo, monkeypatch)
    hashed = subprocess.run(
        ("git", "hash-object", "-w", "--stdin"),
        cwd=repo,
        input=b"index-only staged output drift\n",
        capture_output=True,
        check=False,
    )
    assert hashed.returncode == 0, hashed.stderr.decode("utf-8", errors="replace")
    object_id = hashed.stdout.decode("ascii").strip()
    _git(repo, "update-index", "--cacheinfo", "100644", object_id, drift_rel)
    index_path = repo / ".git/index"
    protected_before = {
        repo / REPORT_REL: (
            _read_noatime(repo / REPORT_REL),
            _metadata(repo / REPORT_REL),
        ),
        repo / MANIFEST_REL: (
            _read_noatime(repo / MANIFEST_REL),
            _metadata(repo / MANIFEST_REL),
        ),
        index_path: (_read_noatime(index_path), _metadata(index_path)),
    }

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert protected_before == {
        repo / REPORT_REL: (
            _read_noatime(repo / REPORT_REL),
            _metadata(repo / REPORT_REL),
        ),
        repo / MANIFEST_REL: (
            _read_noatime(repo / MANIFEST_REL),
            _metadata(repo / MANIFEST_REL),
        ),
        index_path: (_read_noatime(index_path), _metadata(index_path)),
    }
    assert not list((repo / "audit").glob(".*.epic-close-pack.*"))


def test_state_inconsistent_residue_is_ambiguous_and_remains_untouched(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    repo = _init_repo(tmp_path)
    old_report, old_manifest = _generate_and_commit(repo, monkeypatch)
    source = _valid_source()
    source["report_sections"][0]["body_lines"].append(
        "Recovery requires a fresh derivation from tracked inputs."
    )
    _write_json(repo / SOURCE_REL, source)
    _git(repo, "add", SOURCE_REL)
    _git(repo, "commit", "-m", "advance candidate source")

    residue = (
        repo
        / "audit"
        / f".{Path(REPORT_REL).name}.epic-close-pack.{'3' * 32}"
    )
    # With both canonical files still old, an exclusive writer can have staged
    # only new report bytes.  An old-report residue is therefore ambiguous.
    residue.write_bytes(old_report)
    os.chmod(residue, close_pack.OUTPUT_MODE)

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert "EPIC_CLOSE_PACK_ERROR:RECOVERY_RESIDUE_AMBIGUOUS" in capsys.readouterr().err
    assert _read_noatime(repo / REPORT_REL) == old_report
    assert _read_noatime(repo / MANIFEST_REL) == old_manifest
    assert _read_noatime(residue) == old_report


@pytest.mark.skipif(not hasattr(os, "fork"), reason="POSIX process termination required")
@pytest.mark.parametrize("target_posture", ("existing", "absent"))
@pytest.mark.parametrize(
    "boundary",
    (
        "report_staged",
        "manifest_staged",
        "staged_pair_verified",
        "report_installed",
        "report_directory_synced",
        "manifest_installed",
        "manifest_directory_synced",
        "pair_verified",
        "report_residue_removed",
        "manifest_residue_removed",
        "cleanup_directory_synced",
    ),
)
def test_process_termination_is_fail_closed_and_fresh_write_recovers(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    target_posture: str,
    boundary: str,
) -> None:
    repo = _init_repo(tmp_path)
    old_outputs: dict[str, bytes] | None = None
    if target_posture == "existing":
        old_report, old_manifest = _generate_and_commit(repo, monkeypatch)
        old_outputs = {REPORT_REL: old_report, MANIFEST_REL: old_manifest}
        source = _valid_source()
        source["report_sections"][0]["body_lines"].append(
            "Recovery requires a fresh derivation from tracked inputs."
        )
        _write_json(repo / SOURCE_REL, source)
        _git(repo, "add", SOURCE_REL)
        _git(repo, "commit", "-m", "advance candidate source")

    new_outputs = _render_expected_outputs(repo, monkeypatch)
    head_before = _git(repo, "rev-parse", "HEAD")
    index_path = repo / ".git/index"
    index_before = _read_noatime(index_path)
    index_metadata_before = _metadata(index_path)

    _kill_writer_at_boundary(repo, boundary)

    assert _git(repo, "rev-parse", "HEAD") == head_before
    assert _read_noatime(index_path) == index_before
    assert _metadata(index_path) == index_metadata_before

    def state(rel: str) -> str:
        path = repo / rel
        if not path.exists():
            return "absent"
        payload = _read_noatime(path)
        if payload == new_outputs[rel]:
            return "new"
        if old_outputs is not None and payload == old_outputs[rel]:
            return "old"
        return "unknown"

    observed = (state(REPORT_REL), state(MANIFEST_REL))
    allowed = (
        {("old", "old"), ("new", "old"), ("new", "new")}
        if old_outputs is not None
        else {("absent", "absent"), ("new", "absent"), ("new", "new")}
    )
    assert observed in allowed
    assert observed != ("old", "new")

    if observed == ("new", "new"):
        assert close_pack._read_manifest_committed_pair(
            repo, new_outputs, REPORT_REL, MANIFEST_REL
        ) == {MANIFEST_REL: new_outputs[MANIFEST_REL], REPORT_REL: new_outputs[REPORT_REL]}
    elif observed == ("old", "old"):
        assert old_outputs is not None
        assert close_pack._read_manifest_committed_pair(
            repo, old_outputs, REPORT_REL, MANIFEST_REL
        ) == {MANIFEST_REL: old_outputs[MANIFEST_REL], REPORT_REL: old_outputs[REPORT_REL]}
    else:
        with pytest.raises(close_pack.ClosePackError):
            close_pack._read_manifest_committed_pair(
                repo, new_outputs, REPORT_REL, MANIFEST_REL
            )

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--check") == 1
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 0
    assert _read_noatime(repo / REPORT_REL) == new_outputs[REPORT_REL]
    assert _read_noatime(repo / MANIFEST_REL) == new_outputs[MANIFEST_REL]
    assert not list((repo / "audit").glob(".*.epic-close-pack.*"))
    assert _read_noatime(index_path) == index_before
    assert _metadata(index_path) == index_metadata_before
    assert _git(repo, "rev-parse", "HEAD") == head_before
    _git(repo, "add", REPORT_REL, MANIFEST_REL)
    _git(repo, "commit", "-m", "commit recovered candidate")
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--check") == 0


@pytest.mark.skipif(not hasattr(os, "fork"), reason="POSIX process termination required")
@pytest.mark.parametrize(
    "boundary",
    (
        "recovery_residue_quarantined",
        "recovery_residue_removed",
        "recovery_directory_synced",
    ),
)
def test_process_termination_during_recovery_cleanup_is_safely_recoverable(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    boundary: str,
) -> None:
    repo = _init_repo(tmp_path)
    _generate_and_commit(repo, monkeypatch)
    source = _valid_source()
    source["report_sections"][0]["body_lines"].append(
        "Recovery requires a fresh derivation from tracked inputs."
    )
    _write_json(repo / SOURCE_REL, source)
    _git(repo, "add", SOURCE_REL)
    _git(repo, "commit", "-m", "advance candidate source")
    new_outputs = _render_expected_outputs(repo, monkeypatch)
    head_before = _git(repo, "rev-parse", "HEAD")
    index_path = repo / ".git/index"
    index_before = (_read_noatime(index_path), _metadata(index_path))

    _kill_writer_at_boundary(repo, "report_installed")
    assert list((repo / "audit").glob(".*.epic-close-pack.*"))
    _kill_writer_at_boundary(repo, boundary)

    assert _git(repo, "rev-parse", "HEAD") == head_before
    assert index_before == (_read_noatime(index_path), _metadata(index_path))
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 0
    assert _git(repo, "rev-parse", "HEAD") == head_before
    assert index_before == (_read_noatime(index_path), _metadata(index_path))
    assert _read_noatime(repo / REPORT_REL) == new_outputs[REPORT_REL]
    assert _read_noatime(repo / MANIFEST_REL) == new_outputs[MANIFEST_REL]
    assert not list((repo / "audit").glob(".*.epic-close-pack.*"))
    assert close_pack._read_manifest_committed_pair(
        repo, new_outputs, REPORT_REL, MANIFEST_REL
    ) == {
        MANIFEST_REL: new_outputs[MANIFEST_REL],
        REPORT_REL: new_outputs[REPORT_REL],
    }


@pytest.mark.parametrize("drift", ("same_tree_head", "index_bytes"))
def test_recovery_cleanup_refuses_git_identity_drift_before_mutation(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    drift: str,
) -> None:
    repo = _init_repo(tmp_path)
    _generate_and_commit(repo, monkeypatch)
    source = _valid_source()
    source["report_sections"][0]["body_lines"].append(
        "Recovery requires a fresh derivation from tracked inputs."
    )
    _write_json(repo / SOURCE_REL, source)
    _git(repo, "add", SOURCE_REL)
    _git(repo, "commit", "-m", "advance candidate source")
    new_outputs = _render_expected_outputs(repo, monkeypatch)

    _kill_writer_at_boundary(repo, "report_installed")
    residue_paths = sorted((repo / "audit").glob(".*.epic-close-pack.*"))
    assert residue_paths
    residue_before = {
        path.name: (_read_noatime(path), _metadata(path))
        for path in residue_paths
    }
    canonical_before = {
        rel: (_read_noatime(repo / rel), _metadata(repo / rel))
        for rel in (REPORT_REL, MANIFEST_REL)
    }
    original_cleanup = close_pack._cleanup_recovery_residue
    injected_head = ""
    injected_index: tuple[bytes, tuple[int, int, int, int, int, int]] | None = None

    def drift_before_cleanup(
        root: Path,
        residues: tuple[close_pack.RecoveryResidue, ...],
        verifier: Callable[[], None],
    ) -> None:
        nonlocal injected_head, injected_index
        assert root == repo
        assert residues
        if drift == "same_tree_head":
            _git(repo, "commit", "--allow-empty", "-m", "inject same-tree head drift")
        else:
            _append_checksum_valid_index_extension(repo, b"DRFT")
        injected_head = _git(repo, "rev-parse", "HEAD")
        index_path = repo / ".git/index"
        injected_index = (_read_noatime(index_path), _metadata(index_path))
        original_cleanup(root, residues, verifier)

    monkeypatch.setattr(
        close_pack, "_cleanup_recovery_residue", drift_before_cleanup
    )
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    error = capsys.readouterr().err
    expected_error = (
        "GIT_CONTEXT_CHANGED"
        if drift == "same_tree_head"
        else "GIT_CONTROL_STATE_CHANGED"
    )
    assert f"EPIC_CLOSE_PACK_ERROR:{expected_error}" in error
    assert _git(repo, "rev-parse", "HEAD") == injected_head
    assert injected_index is not None
    assert injected_index == (
        _read_noatime(repo / ".git/index"),
        _metadata(repo / ".git/index"),
    )
    assert canonical_before == {
        rel: (_read_noatime(repo / rel), _metadata(repo / rel))
        for rel in (REPORT_REL, MANIFEST_REL)
    }
    assert residue_before == {
        path.name: (_read_noatime(path), _metadata(path))
        for path in sorted((repo / "audit").glob(".*.epic-close-pack.*"))
    }

    monkeypatch.setattr(close_pack, "_cleanup_recovery_residue", original_cleanup)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 0
    assert _git(repo, "rev-parse", "HEAD") == injected_head
    assert injected_index == (
        _read_noatime(repo / ".git/index"),
        _metadata(repo / ".git/index"),
    )
    assert _read_noatime(repo / REPORT_REL) == new_outputs[REPORT_REL]
    assert _read_noatime(repo / MANIFEST_REL) == new_outputs[MANIFEST_REL]
    assert not list((repo / "audit").glob(".*.epic-close-pack.*"))


def test_publication_refuses_byte_only_index_drift_and_preserves_residue(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    repo = _init_repo(tmp_path)
    _generate_and_commit(repo, monkeypatch)
    source = _valid_source()
    source["report_sections"][0]["body_lines"].append(
        "Recovery requires a fresh derivation from tracked inputs."
    )
    _write_json(repo / SOURCE_REL, source)
    _git(repo, "add", SOURCE_REL)
    _git(repo, "commit", "-m", "advance candidate source")
    new_outputs = _render_expected_outputs(repo, monkeypatch)
    head_before = _git(repo, "rev-parse", "HEAD")
    original_boundary = close_pack._publication_boundary
    injected_index: tuple[bytes, tuple[int, int, int, int, int, int]] | None = None

    def mutate_index_after_pair_verification(boundary: str) -> None:
        nonlocal injected_index
        if boundary != "pair_verified" or injected_index is not None:
            return
        updated = _append_checksum_valid_index_extension(repo, b"DRFT")
        injected_index = (updated, _metadata(repo / ".git/index"))

    monkeypatch.setattr(
        close_pack,
        "_publication_boundary",
        mutate_index_after_pair_verification,
    )
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert (
        "EPIC_CLOSE_PACK_ERROR:GIT_CONTROL_STATE_CHANGED"
        in capsys.readouterr().err
    )
    assert injected_index is not None
    assert _git(repo, "rev-parse", "HEAD") == head_before
    assert injected_index == (
        _read_noatime(repo / ".git/index"),
        _metadata(repo / ".git/index"),
    )
    assert _read_noatime(repo / REPORT_REL) == new_outputs[REPORT_REL]
    assert _read_noatime(repo / MANIFEST_REL) == new_outputs[MANIFEST_REL]
    assert list((repo / "audit").glob(".*.epic-close-pack.*"))

    monkeypatch.setattr(close_pack, "_publication_boundary", original_boundary)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 0
    assert _git(repo, "rev-parse", "HEAD") == head_before
    assert injected_index == (
        _read_noatime(repo / ".git/index"),
        _metadata(repo / ".git/index"),
    )
    assert _read_noatime(repo / REPORT_REL) == new_outputs[REPORT_REL]
    assert _read_noatime(repo / MANIFEST_REL) == new_outputs[MANIFEST_REL]
    assert not list((repo / "audit").glob(".*.epic-close-pack.*"))


def test_write_pins_exact_index_before_model_rendering(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    repo = _init_repo(tmp_path)
    _generate_and_commit(repo, monkeypatch)
    old_outputs = {
        rel: _read_noatime(repo / rel) for rel in (REPORT_REL, MANIFEST_REL)
    }
    source = _valid_source()
    source["report_sections"][0]["body_lines"].append(
        "Recovery requires a fresh derivation from tracked inputs."
    )
    _write_json(repo / SOURCE_REL, source)
    _git(repo, "add", SOURCE_REL)
    _git(repo, "commit", "-m", "advance candidate source")
    head_before = _git(repo, "rev-parse", "HEAD")
    original_render = close_pack._render_twice
    injected_index: tuple[bytes, tuple[int, int, int, int, int, int]] | None = None

    def render_then_drift(
        model: close_pack.CandidateModel,
    ) -> dict[str, bytes]:
        nonlocal injected_index
        outputs = original_render(model)
        updated = _append_checksum_valid_index_extension(repo, b"DRFT")
        injected_index = (updated, _metadata(repo / ".git/index"))
        return outputs

    monkeypatch.setattr(close_pack, "_render_twice", render_then_drift)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert (
        "EPIC_CLOSE_PACK_ERROR:GIT_CONTROL_STATE_CHANGED"
        in capsys.readouterr().err
    )
    assert injected_index is not None
    assert injected_index == (
        _read_noatime(repo / ".git/index"),
        _metadata(repo / ".git/index"),
    )
    assert _git(repo, "rev-parse", "HEAD") == head_before
    assert old_outputs == {
        rel: _read_noatime(repo / rel) for rel in (REPORT_REL, MANIFEST_REL)
    }
    assert not list((repo / "audit").glob(".*.epic-close-pack.*"))


@pytest.mark.parametrize(
    "boundary",
    (
        "report_staged",
        "report_directory_synced",
        "manifest_installed",
        "cleanup_directory_synced",
    ),
)
def test_publication_checks_exact_index_at_material_boundaries(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    boundary: str,
) -> None:
    repo = _init_repo(tmp_path)
    _generate_and_commit(repo, monkeypatch)
    old_outputs = {
        rel: _read_noatime(repo / rel) for rel in (REPORT_REL, MANIFEST_REL)
    }
    source = _valid_source()
    source["report_sections"][0]["body_lines"].append(
        "Recovery requires a fresh derivation from tracked inputs."
    )
    _write_json(repo / SOURCE_REL, source)
    _git(repo, "add", SOURCE_REL)
    _git(repo, "commit", "-m", "advance candidate source")
    new_outputs = _render_expected_outputs(repo, monkeypatch)
    head_before = _git(repo, "rev-parse", "HEAD")
    original_boundary = close_pack._publication_boundary
    injected_index: tuple[bytes, tuple[int, int, int, int, int, int]] | None = None

    def drift_at_boundary(observed: str) -> None:
        nonlocal injected_index
        if observed == boundary and injected_index is None:
            updated = _append_checksum_valid_index_extension(repo, b"DRFT")
            injected_index = (updated, _metadata(repo / ".git/index"))
        original_boundary(observed)

    monkeypatch.setattr(close_pack, "_publication_boundary", drift_at_boundary)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert (
        "EPIC_CLOSE_PACK_ERROR:GIT_CONTROL_STATE_CHANGED"
        in capsys.readouterr().err
    )
    assert injected_index is not None
    assert injected_index == (
        _read_noatime(repo / ".git/index"),
        _metadata(repo / ".git/index"),
    )
    assert _git(repo, "rev-parse", "HEAD") == head_before

    valid_generations = 0
    for expected in (old_outputs, new_outputs):
        try:
            close_pack._read_manifest_committed_pair(
                repo,
                expected,
                REPORT_REL,
                MANIFEST_REL,
            )
        except close_pack.ClosePackError:
            continue
        valid_generations += 1
    assert valid_generations <= 1

    monkeypatch.setattr(close_pack, "_publication_boundary", original_boundary)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 0
    assert injected_index == (
        _read_noatime(repo / ".git/index"),
        _metadata(repo / ".git/index"),
    )
    assert _read_noatime(repo / REPORT_REL) == new_outputs[REPORT_REL]
    assert _read_noatime(repo / MANIFEST_REL) == new_outputs[MANIFEST_REL]
    assert not list((repo / "audit").glob(".*.epic-close-pack.*"))


@pytest.mark.parametrize("injection_read", (2, 3))
def test_write_rechecks_exact_index_after_final_pair_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    injection_read: int,
) -> None:
    repo = _init_repo(tmp_path)
    _generate_and_commit(repo, monkeypatch)
    source = _valid_source()
    source["report_sections"][0]["body_lines"].append(
        "Recovery requires a fresh derivation from tracked inputs."
    )
    _write_json(repo / SOURCE_REL, source)
    _git(repo, "add", SOURCE_REL)
    _git(repo, "commit", "-m", "advance candidate source")
    new_outputs = _render_expected_outputs(repo, monkeypatch)
    head_before = _git(repo, "rev-parse", "HEAD")
    original_reader = close_pack._read_manifest_committed_pair
    read_count = 0
    injected_index: tuple[bytes, tuple[int, int, int, int, int, int]] | None = None

    def read_then_drift(*args: object, **kwargs: object) -> dict[str, bytes]:
        nonlocal read_count, injected_index
        accepted = original_reader(*args, **kwargs)
        read_count += 1
        if read_count == injection_read:
            updated = _append_checksum_valid_index_extension(repo, b"DRFT")
            injected_index = (updated, _metadata(repo / ".git/index"))
        return accepted

    monkeypatch.setattr(close_pack, "_read_manifest_committed_pair", read_then_drift)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert read_count == injection_read
    assert (
        "EPIC_CLOSE_PACK_ERROR:GIT_CONTROL_STATE_CHANGED"
        in capsys.readouterr().err
    )
    assert injected_index is not None
    assert injected_index == (
        _read_noatime(repo / ".git/index"),
        _metadata(repo / ".git/index"),
    )

    assert _git(repo, "rev-parse", "HEAD") == head_before
    assert _read_noatime(repo / REPORT_REL) == new_outputs[REPORT_REL]
    assert _read_noatime(repo / MANIFEST_REL) == new_outputs[MANIFEST_REL]

    monkeypatch.setattr(close_pack, "_read_manifest_committed_pair", original_reader)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 0
    assert injected_index == (
        _read_noatime(repo / ".git/index"),
        _metadata(repo / ".git/index"),
    )


@pytest.mark.parametrize("mutation", ("symlink", "untracked"))
def test_write_rechecks_worktree_after_final_pair_read(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    mutation: str,
) -> None:
    repo = _init_repo(tmp_path)
    link = repo / "tracked-link"
    link.symlink_to("target-one")
    _git(repo, "add", "tracked-link")
    _git(repo, "commit", "-m", "add tracked symlink")
    _generate_and_commit(repo, monkeypatch)
    source = _valid_source()
    source["report_sections"][0]["body_lines"].append(
        "Recovery requires a fresh derivation from tracked inputs."
    )
    _write_json(repo / SOURCE_REL, source)
    _git(repo, "add", SOURCE_REL)
    _git(repo, "commit", "-m", "advance candidate source")
    original_reader = close_pack._read_manifest_committed_pair
    read_count = 0

    def read_then_mutate(*args: object, **kwargs: object) -> dict[str, bytes]:
        nonlocal read_count
        accepted = original_reader(*args, **kwargs)
        read_count += 1
        if read_count == 3:
            if mutation == "symlink":
                link.unlink()
                link.symlink_to("target-two")
            else:
                (repo / "late-untracked.txt").write_text(
                    "late mutation\n", encoding="utf-8"
                )
        return accepted

    monkeypatch.setattr(close_pack, "_read_manifest_committed_pair", read_then_mutate)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert read_count == 3
    assert "EPIC_CLOSE_PACK_ERROR:UNEXPECTED_WRITE_RESIDUE" in capsys.readouterr().err
    if mutation == "symlink":
        assert os.fsencode(os.readlink(link)) == b"target-two"
    else:
        assert (repo / "late-untracked.txt").read_bytes() == b"late mutation\n"


def test_write_rechecks_pair_after_final_metadata_scan(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    repo = _init_repo(tmp_path)
    _generate_and_commit(repo, monkeypatch)
    source = _valid_source()
    source["report_sections"][0]["body_lines"].append(
        "Recovery requires a fresh derivation from tracked inputs."
    )
    _write_json(repo / SOURCE_REL, source)
    _git(repo, "add", SOURCE_REL)
    _git(repo, "commit", "-m", "advance candidate source")
    new_outputs = _render_expected_outputs(repo, monkeypatch)
    head_before = _git(repo, "rev-parse", "HEAD")
    index_before = (
        _read_noatime(repo / ".git/index"),
        _metadata(repo / ".git/index"),
    )
    original_boundary = close_pack._publication_boundary
    original_metadata = close_pack._repository_metadata
    publication_complete = False
    mutated = False

    def observe_boundary(boundary: str) -> None:
        nonlocal publication_complete
        original_boundary(boundary)
        if boundary == "cleanup_directory_synced":
            publication_complete = True

    def scan_then_mutate(
        root: Path,
    ) -> dict[str, tuple[int, int, int, int, int, int, int]]:
        nonlocal mutated
        metadata = original_metadata(root)
        if publication_complete and not mutated:
            report = repo / REPORT_REL
            payload = _read_noatime(report)
            report.write_bytes(bytes([payload[0] ^ 1]) + payload[1:])
            mutated = True
        return metadata

    monkeypatch.setattr(close_pack, "_publication_boundary", observe_boundary)
    monkeypatch.setattr(close_pack, "_repository_metadata", scan_then_mutate)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert mutated
    assert "EPIC_CLOSE_PACK_ERROR:REPORT_HASH_MISMATCH" in capsys.readouterr().err
    assert _git(repo, "rev-parse", "HEAD") == head_before
    assert index_before == (
        _read_noatime(repo / ".git/index"),
        _metadata(repo / ".git/index"),
    )
    assert len(_read_noatime(repo / REPORT_REL)) == len(new_outputs[REPORT_REL])
    assert _read_noatime(repo / REPORT_REL) != new_outputs[REPORT_REL]
    assert _read_noatime(repo / MANIFEST_REL) == new_outputs[MANIFEST_REL]


def test_write_rechecks_symlink_target_after_final_metadata_scan(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    repo = _init_repo(tmp_path)
    rel = "tracked-link"
    link = repo / rel
    link.symlink_to("target-one")
    _git(repo, "add", rel)
    _git(repo, "commit", "-m", "add tracked symlink")
    _generate_and_commit(repo, monkeypatch)
    source = _valid_source()
    source["report_sections"][0]["body_lines"].append(
        "Recovery requires a fresh derivation from tracked inputs."
    )
    _write_json(repo / SOURCE_REL, source)
    _git(repo, "add", SOURCE_REL)
    _git(repo, "commit", "-m", "advance candidate source")
    original_boundary = close_pack._publication_boundary
    original_metadata = close_pack._repository_metadata
    publication_complete = False
    mutated = False

    def observe_boundary(boundary: str) -> None:
        nonlocal publication_complete
        original_boundary(boundary)
        if boundary == "cleanup_directory_synced":
            publication_complete = True

    def scan_then_mutate(
        root: Path,
    ) -> dict[str, tuple[int, int, int, int, int, int, int]]:
        nonlocal mutated
        metadata = original_metadata(root)
        if publication_complete and not mutated:
            link.unlink()
            link.symlink_to("target-two")
            mutated = True
        return metadata

    monkeypatch.setattr(close_pack, "_publication_boundary", observe_boundary)
    monkeypatch.setattr(close_pack, "_repository_metadata", scan_then_mutate)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert mutated
    assert "EPIC_CLOSE_PACK_ERROR:UNEXPECTED_WRITE_RESIDUE" in capsys.readouterr().err
    assert os.fsencode(os.readlink(link)) == b"target-two"


def test_write_does_not_exempt_output_parent_atime_change(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    repo = _init_repo(tmp_path)
    _generate_and_commit(repo, monkeypatch)
    source = _valid_source()
    source["report_sections"][0]["body_lines"].append(
        "Recovery requires a fresh derivation from tracked inputs."
    )
    _write_json(repo / SOURCE_REL, source)
    _git(repo, "add", SOURCE_REL)
    _git(repo, "commit", "-m", "advance candidate source")
    original_boundary = close_pack._publication_boundary
    original_metadata = close_pack._repository_metadata
    publication_complete = False
    mutated = False

    def observe_boundary(boundary: str) -> None:
        nonlocal publication_complete
        original_boundary(boundary)
        if boundary == "cleanup_directory_synced":
            publication_complete = True

    def mutate_then_scan(
        root: Path,
    ) -> dict[str, tuple[int, int, int, int, int, int, int]]:
        nonlocal mutated
        if publication_complete and not mutated:
            audit = repo / "audit"
            metadata = audit.stat()
            os.utime(
                audit,
                ns=(946_684_800_000_000_000, metadata.st_mtime_ns),
                follow_symlinks=False,
            )
            mutated = True
        return original_metadata(root)

    monkeypatch.setattr(close_pack, "_publication_boundary", observe_boundary)
    monkeypatch.setattr(close_pack, "_repository_metadata", mutate_then_scan)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert mutated
    assert "EPIC_CLOSE_PACK_ERROR:WRITE_MODE_MUTATION" in capsys.readouterr().err


@pytest.mark.skipif(not hasattr(os, "fork"), reason="POSIX process termination required")
@pytest.mark.parametrize(
    "boundary",
    (
        "report_staged",
        "manifest_staged",
        "staged_pair_verified",
        "report_installed",
        "report_directory_synced",
        "manifest_installed",
        "manifest_directory_synced",
        "pair_verified",
        "report_residue_removed",
        "manifest_residue_removed",
        "cleanup_directory_synced",
    ),
)
def test_interrupted_republish_recovers_when_report_is_already_expected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    boundary: str,
) -> None:
    repo = _init_repo(tmp_path)
    _generate_and_commit(repo, monkeypatch)
    source = _valid_source()
    source["report_sections"][0]["body_lines"].append(
        "Recovery requires a fresh derivation from tracked inputs."
    )
    _write_json(repo / SOURCE_REL, source)
    _git(repo, "add", SOURCE_REL)
    _git(repo, "commit", "-m", "advance candidate source")
    new_outputs = _render_expected_outputs(repo, monkeypatch)

    # Commit the authorized mixed state: the report is already the expected
    # generation while the manifest still binds the prior report.
    (repo / REPORT_REL).write_bytes(new_outputs[REPORT_REL])
    _git(repo, "add", REPORT_REL)
    _git(repo, "commit", "-m", "commit mixed candidate for recovery")
    head_before = _git(repo, "rev-parse", "HEAD")
    index_path = repo / ".git/index"
    index_before = (_read_noatime(index_path), _metadata(index_path))

    # The exchanged report residue has bytes equal to both the exact-HEAD blob
    # and the newly rendered report; it is still an unambiguous tool residue.
    _kill_writer_at_boundary(repo, boundary)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 0
    assert _git(repo, "rev-parse", "HEAD") == head_before
    assert index_before == (_read_noatime(index_path), _metadata(index_path))
    assert _read_noatime(repo / REPORT_REL) == new_outputs[REPORT_REL]
    assert _read_noatime(repo / MANIFEST_REL) == new_outputs[MANIFEST_REL]
    assert not list((repo / "audit").glob(".*.epic-close-pack.*"))


def test_manifest_rename_effect_then_catchable_interrupt_remains_recoverable(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path)
    old_report, old_manifest = _generate_and_commit(repo, monkeypatch)
    source = _valid_source()
    source["report_sections"][0]["body_lines"].append(
        "Recovery requires a fresh derivation from tracked inputs."
    )
    _write_json(repo / SOURCE_REL, source)
    _git(repo, "add", SOURCE_REL)
    _git(repo, "commit", "-m", "advance candidate source")
    new_outputs = _render_expected_outputs(repo, monkeypatch)
    original_rename = close_pack._rename_with_flags
    interrupted = False

    def rename_then_interrupt(
        source_name: str,
        destination_name: str,
        parent_fd: int,
        flags: int,
    ) -> None:
        nonlocal interrupted
        original_rename(source_name, destination_name, parent_fd, flags)
        if destination_name == Path(MANIFEST_REL).name and not interrupted:
            interrupted = True
            raise KeyboardInterrupt("injected immediately after manifest rename")

    monkeypatch.setattr(close_pack, "_rename_with_flags", rename_then_interrupt)
    with pytest.raises(KeyboardInterrupt, match="after manifest rename"):
        _run(repo, monkeypatch, "--source", SOURCE_REL, "--write")
    monkeypatch.setattr(close_pack, "_rename_with_flags", original_rename)

    assert interrupted
    assert _read_noatime(repo / REPORT_REL) == new_outputs[REPORT_REL]
    assert _read_noatime(repo / MANIFEST_REL) == new_outputs[MANIFEST_REL]
    assert _read_noatime(repo / REPORT_REL) != old_report
    assert _read_noatime(repo / MANIFEST_REL) != old_manifest
    assert list((repo / "audit").glob(".*.epic-close-pack.*"))
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 0
    assert _read_noatime(repo / REPORT_REL) == new_outputs[REPORT_REL]
    assert _read_noatime(repo / MANIFEST_REL) == new_outputs[MANIFEST_REL]
    assert not list((repo / "audit").glob(".*.epic-close-pack.*"))


def test_temp_shaped_hardlink_residue_is_rejected_and_preserved(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    repo = _init_repo(tmp_path)
    old_report, old_manifest = _generate_and_commit(repo, monkeypatch)
    source = _valid_source()
    source["report_sections"][0]["body_lines"].append(
        "Recovery requires a fresh derivation from tracked inputs."
    )
    _write_json(repo / SOURCE_REL, source)
    _git(repo, "add", SOURCE_REL)
    _git(repo, "commit", "-m", "advance candidate source")
    new_outputs = _render_expected_outputs(repo, monkeypatch)
    residue = (
        repo
        / "audit"
        / f".{Path(REPORT_REL).name}.epic-close-pack.{'a' * 32}"
    )
    hardlink_source = tmp_path / "hardlink-source"
    hardlink_source.write_bytes(new_outputs[REPORT_REL])
    os.chmod(hardlink_source, close_pack.OUTPUT_MODE)
    os.link(hardlink_source, residue)
    source_before = hardlink_source.lstat()
    residue_before = residue.lstat()
    assert source_before.st_ino == residue_before.st_ino
    assert source_before.st_nlink == residue_before.st_nlink == 2

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert (
        "EPIC_CLOSE_PACK_ERROR:RECOVERY_RESIDUE_AMBIGUOUS"
        in capsys.readouterr().err
    )
    assert residue.exists()
    assert hardlink_source.exists()
    assert _read_noatime(residue) == new_outputs[REPORT_REL]
    assert _read_noatime(hardlink_source) == new_outputs[REPORT_REL]
    assert _read_noatime(repo / REPORT_REL) == old_report
    assert _read_noatime(repo / MANIFEST_REL) == old_manifest
    source_after = hardlink_source.lstat()
    residue_after = residue.lstat()
    assert source_after.st_ino == residue_after.st_ino == source_before.st_ino
    assert source_after.st_nlink == residue_after.st_nlink == 2


def test_residue_hardlinked_after_classification_is_rejected_and_preserved(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    repo = _init_repo(tmp_path)
    old_report, old_manifest = _generate_and_commit(repo, monkeypatch)
    source = _valid_source()
    source["report_sections"][0]["body_lines"].append(
        "Recovery requires a fresh derivation from tracked inputs."
    )
    _write_json(repo / SOURCE_REL, source)
    _git(repo, "add", SOURCE_REL)
    _git(repo, "commit", "-m", "advance candidate source")
    new_outputs = _render_expected_outputs(repo, monkeypatch)
    residue = (
        repo
        / "audit"
        / f".{Path(REPORT_REL).name}.epic-close-pack.{'b' * 32}"
    )
    residue.write_bytes(new_outputs[REPORT_REL])
    os.chmod(residue, close_pack.OUTPUT_MODE)
    outside_link = tmp_path / "late-hardlink"
    original_cleanup = close_pack._cleanup_recovery_residue

    def hardlink_before_cleanup(
        root: Path,
        residues: tuple[close_pack.RecoveryResidue, ...],
        verifier: Callable[[], None],
    ) -> None:
        assert root == repo
        assert [item.rel for item in residues] == [
            residue.relative_to(repo).as_posix()
        ]
        os.link(residue, outside_link)
        original_cleanup(root, residues, verifier)

    monkeypatch.setattr(
        close_pack, "_cleanup_recovery_residue", hardlink_before_cleanup
    )
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert "EPIC_CLOSE_PACK_ERROR:RECOVERY_RESIDUE_AMBIGUOUS" in capsys.readouterr().err
    assert residue.exists()
    assert outside_link.exists()
    assert residue.lstat().st_ino == outside_link.lstat().st_ino
    assert residue.lstat().st_nlink == outside_link.lstat().st_nlink == 2
    assert _read_noatime(residue) == new_outputs[REPORT_REL]
    assert _read_noatime(repo / REPORT_REL) == old_report
    assert _read_noatime(repo / MANIFEST_REL) == old_manifest


def test_manifest_reader_rejects_new_report_with_old_manifest(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path)
    _generate_and_commit(repo, monkeypatch)
    source = _valid_source()
    source["report_sections"][0]["body_lines"].append("Existing candidate outputs are not causal inputs.")
    _write_json(repo / SOURCE_REL, source)
    _git(repo, "add", SOURCE_REL)
    _git(repo, "commit", "-m", "advance source")
    outputs = _render_expected_outputs(repo, monkeypatch)
    (repo / REPORT_REL).write_bytes(outputs[REPORT_REL])
    with pytest.raises(close_pack.ClosePackError):
        close_pack._read_manifest_committed_pair(
            repo, outputs, REPORT_REL, MANIFEST_REL
        )
    _git(repo, "add", REPORT_REL)
    _git(repo, "commit", "-m", "commit intentionally mixed generation")
    assert _git(repo, "status", "--porcelain=v1", "--untracked-files=all") == ""
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--check") == 1
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 0
    _git(repo, "add", REPORT_REL, MANIFEST_REL)
    _git(repo, "commit", "-m", "recover complete candidate")
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--check") == 0


def test_manifest_mutation_between_reads_is_rejected(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path)
    _generate_and_commit(repo, monkeypatch)
    outputs = _render_expected_outputs(repo, monkeypatch)
    original = close_pack._stable_anchored_read
    manifest_reads = 0

    def mutate_before_second_manifest_read(parent_fd: int, name: str, **kwargs):
        nonlocal manifest_reads
        if name == Path(MANIFEST_REL).name:
            manifest_reads += 1
            if manifest_reads == 2:
                mutated = bytearray(outputs[MANIFEST_REL])
                index = mutated.index(b"candidate_only")
                mutated[index] = ord("C")
                (repo / MANIFEST_REL).write_bytes(mutated)
        return original(parent_fd, name, **kwargs)

    monkeypatch.setattr(
        close_pack, "_stable_anchored_read", mutate_before_second_manifest_read
    )
    with pytest.raises(close_pack.ClosePackError, match="MANIFEST_UNSTABLE"):
        close_pack._read_manifest_committed_pair(
            repo, outputs, REPORT_REL, MANIFEST_REL
        )


def test_same_length_same_mode_report_substitution_fails_exact_hash(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path)
    _generate_and_commit(repo, monkeypatch)
    outputs = _render_expected_outputs(repo, monkeypatch)
    substituted = bytearray(outputs[REPORT_REL])
    substituted[0] = ord("!")
    (repo / REPORT_REL).write_bytes(substituted)
    os.chmod(repo / REPORT_REL, close_pack.OUTPUT_MODE)
    assert len(substituted) == len(outputs[REPORT_REL])
    with pytest.raises(close_pack.ClosePackError, match="REPORT_HASH_MISMATCH"):
        close_pack._read_manifest_committed_pair(
            repo, outputs, REPORT_REL, MANIFEST_REL
        )


def test_publication_failure_restores_previous_pair_and_leaves_no_temp_residue(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path)
    old_report, old_manifest = _generate_and_commit(repo, monkeypatch)
    old_metadata = {
        REPORT_REL: _metadata(repo / REPORT_REL),
        MANIFEST_REL: _metadata(repo / MANIFEST_REL),
    }
    source = _valid_source()
    source["report_sections"][0]["body_lines"].append("Candidate publication uses the manifest as its commit point.")
    _write_json(repo / SOURCE_REL, source)
    _git(repo, "add", SOURCE_REL)
    _git(repo, "commit", "-m", "change tracked candidate source")

    original = close_pack._install_staged_output
    calls = 0

    def fail_second_install(
        anchor: close_pack.OutputAnchor,
        staged_name: str,
        expected: bytes,
        installed: list[close_pack.InstalledOutput],
        install_attempts: set[str],
    ) -> None:
        nonlocal calls
        calls += 1
        if calls == 2:
            raise OSError("injected second installation failure")
        original(anchor, staged_name, expected, installed, install_attempts)

    monkeypatch.setattr(close_pack, "_install_staged_output", fail_second_install)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert _read_noatime(repo / REPORT_REL) == old_report
    assert _read_noatime(repo / MANIFEST_REL) == old_manifest
    report_after = _metadata(repo / REPORT_REL)
    assert report_after[:3] == old_metadata[REPORT_REL][:3]
    assert report_after[4:] == old_metadata[REPORT_REL][4:]
    assert _metadata(repo / MANIFEST_REL)[:3] == old_metadata[MANIFEST_REL][:3]
    assert not list((repo / "audit").glob(".*.epic-close-pack.*"))
    assert _git(repo, "status", "--porcelain=v1", "--untracked-files=all") == ""


def test_install_effect_followed_by_exception_is_rolled_back(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path)
    old_report, old_manifest = _generate_and_commit(repo, monkeypatch)
    source = _valid_source()
    source["report_sections"][0]["body_lines"].append("The checker does not repair candidate outputs.")
    _write_json(repo / SOURCE_REL, source)
    _git(repo, "add", SOURCE_REL)
    _git(repo, "commit", "-m", "change tracked candidate source")
    original_install = close_pack._install_staged_output
    calls = 0

    def install_then_fail(
        anchor: close_pack.OutputAnchor,
        staged_name: str,
        expected: bytes,
        installed: list[close_pack.InstalledOutput],
        install_attempts: set[str],
    ) -> None:
        nonlocal calls
        calls += 1
        original_install(
            anchor, staged_name, expected, installed, install_attempts
        )
        if calls == 1:
            raise OSError("injected exception after installation")

    monkeypatch.setattr(close_pack, "_install_staged_output", install_then_fail)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert _read_noatime(repo / REPORT_REL) == old_report
    assert _read_noatime(repo / MANIFEST_REL) == old_manifest
    assert not list((repo / "audit").glob(".*.epic-close-pack.*"))
    assert _git(repo, "status", "--porcelain=v1", "--untracked-files=all") == ""


def test_mutated_rollback_backup_is_never_installed_or_deleted(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    repo = _init_repo(tmp_path)
    old_report, old_manifest = _generate_and_commit(repo, monkeypatch)
    source = _valid_source()
    source["report_sections"][0]["body_lines"].append("The checker does not repair candidate outputs.")
    _write_json(repo / SOURCE_REL, source)
    _git(repo, "add", SOURCE_REL)
    _git(repo, "commit", "-m", "change tracked candidate source")
    new_outputs = _render_expected_outputs(repo, monkeypatch)
    mutation = b"x" * len(old_report)
    mutated_residue: Path | None = None

    def mutate_backup_then_fail(boundary: str) -> None:
        nonlocal mutated_residue
        if boundary != "report_directory_synced":
            return
        candidates = list(
            (repo / "audit").glob(
                f".{Path(REPORT_REL).name}.epic-close-pack.*"
            )
        )
        assert len(candidates) == 1
        mutated_residue = candidates[0]
        mutated_residue.write_bytes(mutation)
        os.chmod(mutated_residue, close_pack.OUTPUT_MODE)
        raise OSError("injected failure after backup mutation")

    monkeypatch.setattr(close_pack, "_publication_boundary", mutate_backup_then_fail)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert (
        "EPIC_CLOSE_PACK_ERROR:PUBLICATION_ROLLBACK_INCOMPLETE"
        in capsys.readouterr().err
    )
    assert mutated_residue is not None and mutated_residue.exists()
    assert _read_noatime(mutated_residue) == mutation
    assert _read_noatime(repo / REPORT_REL) == new_outputs[REPORT_REL]
    assert _read_noatime(repo / REPORT_REL) != mutation
    assert _read_noatime(repo / MANIFEST_REL) == old_manifest

    monkeypatch.setattr(close_pack, "_publication_boundary", lambda _name: None)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert "EPIC_CLOSE_PACK_ERROR:RECOVERY_RESIDUE_AMBIGUOUS" in capsys.readouterr().err
    assert mutated_residue.exists()
    assert _read_noatime(mutated_residue) == mutation
    assert _read_noatime(repo / REPORT_REL) == new_outputs[REPORT_REL]
    assert _read_noatime(repo / MANIFEST_REL) == old_manifest


def test_rollback_exchange_failure_preserves_recoverable_residue(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    repo = _init_repo(tmp_path)
    _generate_and_commit(repo, monkeypatch)
    source = _valid_source()
    source["report_sections"][0]["body_lines"].append("The checker does not repair candidate outputs.")
    _write_json(repo / SOURCE_REL, source)
    _git(repo, "add", SOURCE_REL)
    _git(repo, "commit", "-m", "change tracked candidate source")
    new_outputs = _render_expected_outputs(repo, monkeypatch)
    original_rename = close_pack._rename_with_flags
    report_exchanges = 0

    def fail_rollback_exchange(
        source_name: str,
        target_name: str,
        parent_fd: int,
        flags: int,
    ) -> None:
        nonlocal report_exchanges
        if flags == close_pack.RENAME_EXCHANGE and target_name == Path(REPORT_REL).name:
            report_exchanges += 1
            if report_exchanges == 2:
                raise OSError("injected rollback exchange failure")
        original_rename(source_name, target_name, parent_fd, flags)

    def fail_after_report_sync(boundary: str) -> None:
        if boundary == "report_directory_synced":
            raise OSError("injected precommit publication failure")

    monkeypatch.setattr(close_pack, "_rename_with_flags", fail_rollback_exchange)
    monkeypatch.setattr(close_pack, "_publication_boundary", fail_after_report_sync)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert (
        "EPIC_CLOSE_PACK_ERROR:PUBLICATION_ROLLBACK_INCOMPLETE"
        in capsys.readouterr().err
    )
    assert report_exchanges == 2
    assert len(list((repo / "audit").glob(".*.epic-close-pack.*"))) == 2

    monkeypatch.setattr(close_pack, "_rename_with_flags", original_rename)
    monkeypatch.setattr(close_pack, "_publication_boundary", lambda _name: None)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 0
    assert _read_noatime(repo / REPORT_REL) == new_outputs[REPORT_REL]
    assert _read_noatime(repo / MANIFEST_REL) == new_outputs[MANIFEST_REL]
    assert not list((repo / "audit").glob(".*.epic-close-pack.*"))


def test_partial_preinstall_cleanup_leaves_recoverable_report_stage(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    repo = _init_repo(tmp_path)
    _generate_and_commit(repo, monkeypatch)
    source = _valid_source()
    source["report_sections"][0]["body_lines"].append("The checker does not repair candidate outputs.")
    _write_json(repo / SOURCE_REL, source)
    _git(repo, "add", SOURCE_REL)
    _git(repo, "commit", "-m", "change tracked candidate source")
    new_outputs = _render_expected_outputs(repo, monkeypatch)
    original_install = close_pack._install_staged_output
    original_unlink = close_pack._unlink_anchored
    report_cleanup_failed = False

    def fail_first_install(
        _anchor: close_pack.OutputAnchor,
        _staged_name: str,
        _expected: bytes,
        _installed: list[close_pack.InstalledOutput],
        _install_attempts: set[str],
    ) -> None:
        raise OSError("injected first installation failure")

    def fail_report_stage_cleanup(
        anchor: close_pack.OutputAnchor,
        name: str,
    ) -> None:
        nonlocal report_cleanup_failed
        if anchor.rel == REPORT_REL and not report_cleanup_failed:
            report_cleanup_failed = True
            raise OSError("injected report stage cleanup failure")
        original_unlink(anchor, name)

    monkeypatch.setattr(close_pack, "_install_staged_output", fail_first_install)
    monkeypatch.setattr(close_pack, "_unlink_anchored", fail_report_stage_cleanup)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert (
        "EPIC_CLOSE_PACK_ERROR:PUBLICATION_ROLLBACK_INCOMPLETE"
        in capsys.readouterr().err
    )
    residues = list((repo / "audit").glob(".*.epic-close-pack.*"))
    assert report_cleanup_failed
    assert len(residues) == 1
    assert residues[0].name.startswith(f".{Path(REPORT_REL).name}.")
    assert _read_noatime(residues[0]) == new_outputs[REPORT_REL]

    monkeypatch.setattr(close_pack, "_install_staged_output", original_install)
    monkeypatch.setattr(close_pack, "_unlink_anchored", original_unlink)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 0
    assert _read_noatime(repo / REPORT_REL) == new_outputs[REPORT_REL]
    assert _read_noatime(repo / MANIFEST_REL) == new_outputs[MANIFEST_REL]
    assert not list((repo / "audit").glob(".*.epic-close-pack.*"))


@pytest.mark.parametrize("failure_point", ("staging", "first_install"))
def test_failure_before_any_install_preserves_all_target_metadata(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    failure_point: str,
) -> None:
    repo = _init_repo(tmp_path)
    old_report, old_manifest = _generate_and_commit(repo, monkeypatch)
    source = _valid_source()
    source["report_sections"][0]["body_lines"].append("The checker does not repair candidate outputs.")
    _write_json(repo / SOURCE_REL, source)
    _git(repo, "add", SOURCE_REL)
    _git(repo, "commit", "-m", "change tracked candidate source")
    before = {
        REPORT_REL: _metadata(repo / REPORT_REL),
        MANIFEST_REL: _metadata(repo / MANIFEST_REL),
    }

    if failure_point == "staging":
        original_write = close_pack._write_temp
        calls = 0

        def fail_second_stage(
            anchor: close_pack.OutputAnchor, payload: bytes, mode: int
        ) -> str:
            nonlocal calls
            calls += 1
            if calls == 2:
                raise OSError("injected staging failure")
            return original_write(anchor, payload, mode)

        monkeypatch.setattr(close_pack, "_write_temp", fail_second_stage)
    else:
        def fail_first_install(
            _anchor: close_pack.OutputAnchor,
            _staged_name: str,
            _expected: bytes,
            _installed: list[close_pack.InstalledOutput],
            _install_attempts: set[str],
        ) -> None:
            raise OSError("injected first installation failure")

        monkeypatch.setattr(close_pack, "_install_staged_output", fail_first_install)

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert _read_noatime(repo / REPORT_REL) == old_report
    assert _read_noatime(repo / MANIFEST_REL) == old_manifest
    assert before == {
        REPORT_REL: _metadata(repo / REPORT_REL),
        MANIFEST_REL: _metadata(repo / MANIFEST_REL),
    }
    assert not list((repo / "audit").glob(".*.epic-close-pack.*"))
    assert _git(repo, "status", "--porcelain=v1", "--untracked-files=all") == ""


@pytest.mark.parametrize("target_posture", ("existing", "absent"))
def test_target_mutation_after_staging_fails_without_clobbering_concurrent_bytes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    target_posture: str,
) -> None:
    repo = _init_repo(tmp_path)
    old_report: bytes | None = None
    old_manifest: bytes | None = None
    if target_posture == "existing":
        old_report, old_manifest = _generate_and_commit(repo, monkeypatch)
        source = _valid_source()
        source["report_sections"][0]["body_lines"].append(
            "Concurrent readers fail closed while publication is unstable."
        )
        _write_json(repo / SOURCE_REL, source)
        _git(repo, "add", SOURCE_REL)
        _git(repo, "commit", "-m", "change tracked candidate source")

    concurrent = b"concurrent target bytes\n"
    original_preimage_check = close_pack._require_anchor_preimage
    mutated = False

    def mutate_after_preimage_check(anchor: close_pack.OutputAnchor) -> None:
        nonlocal mutated
        original_preimage_check(anchor)
        if anchor.rel == MANIFEST_REL and not mutated:
            mutated = True
            (repo / MANIFEST_REL).write_bytes(concurrent)

    monkeypatch.setattr(
        close_pack,
        "_require_anchor_preimage",
        mutate_after_preimage_check,
    )
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert (repo / MANIFEST_REL).read_bytes() == concurrent
    if target_posture == "existing":
        assert old_report is not None and old_manifest is not None
        assert (repo / REPORT_REL).read_bytes() == old_report
        assert old_manifest != concurrent
    else:
        assert not (repo / REPORT_REL).exists()
    assert not list((repo / "audit").glob(".*.epic-close-pack.*"))


@pytest.mark.parametrize("target_posture", ("existing", "absent"))
def test_post_atomic_install_mutation_is_not_clobbered(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    target_posture: str,
) -> None:
    repo = _init_repo(tmp_path)
    old_report: bytes | None = None
    if target_posture == "existing":
        old_report, _ = _generate_and_commit(repo, monkeypatch)
        source = _valid_source()
        source["report_sections"][0]["body_lines"].append(
            "Publication residue is not a candidate input."
        )
        _write_json(repo / SOURCE_REL, source)
        _git(repo, "add", SOURCE_REL)
        _git(repo, "commit", "-m", "change tracked candidate source")

    concurrent = b"concurrent post-atomic-install bytes\n"
    original_rename = close_pack._rename_with_flags
    mutated = False

    def mutate_after_atomic_install(
        source_name: str,
        target_name: str,
        parent_fd: int,
        flags: int,
    ) -> None:
        nonlocal mutated
        original_rename(source_name, target_name, parent_fd, flags)
        if not mutated and target_name == Path(MANIFEST_REL).name:
            mutated = True
            (repo / MANIFEST_REL).write_bytes(concurrent)

    monkeypatch.setattr(close_pack, "_rename_with_flags", mutate_after_atomic_install)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert mutated
    assert (repo / MANIFEST_REL).read_bytes() == concurrent
    if target_posture == "existing":
        assert old_report is not None
        assert (repo / REPORT_REL).read_bytes() != old_report
        assert list((repo / "audit").glob(".*.epic-close-pack.*"))
    else:
        assert (repo / REPORT_REL).exists()
        assert not list((repo / "audit").glob(".*.epic-close-pack.*"))


def test_post_commit_concurrent_output_is_not_clobbered_or_rolled_back(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path)
    old_report, old_manifest = _generate_and_commit(repo, monkeypatch)
    source = _valid_source()
    source["report_sections"][0]["body_lines"].append("The checker does not repair candidate outputs.")
    _write_json(repo / SOURCE_REL, source)
    _git(repo, "add", SOURCE_REL)
    _git(repo, "commit", "-m", "change tracked candidate source")
    concurrent = b"concurrent post-install bytes\n"
    original_boundary = close_pack._publication_boundary

    def mutate_after_commit(boundary: str) -> None:
        original_boundary(boundary)
        if boundary == "manifest_directory_synced":
            (repo / MANIFEST_REL).write_bytes(concurrent)
            raise OSError("injected verifier failure after concurrent mutation")

    monkeypatch.setattr(close_pack, "_publication_boundary", mutate_after_commit)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert (repo / MANIFEST_REL).read_bytes() == concurrent
    assert old_manifest != concurrent
    assert (repo / REPORT_REL).read_bytes() != old_report
    assert list((repo / "audit").glob(".*.epic-close-pack.*"))


@pytest.mark.parametrize(
    ("raw_source", "expected"),
    (
        (b"", "INPUT_EMPTY"),
        (b"{not-json}\n", "SOURCE_JSON_INVALID"),
        (b'{"schema_version":"epic_close_candidate_source.v1"}\n', "SOURCE_SCHEMA_INVALID"),
        (
            b'{"schema_version":"epic_close_candidate_source.v1",'
            b'"schema_version":"duplicate"}\n',
            "SOURCE_JSON_INVALID",
        ),
    ),
)
def test_empty_malformed_partial_or_duplicate_source_fails(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    raw_source: bytes,
    expected: str,
) -> None:
    repo = _init_repo(tmp_path, raw_source=raw_source)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert expected in capsys.readouterr().err
    assert not (repo / REPORT_REL).exists()
    assert not (repo / MANIFEST_REL).exists()


def test_missing_untracked_empty_symlinked_and_case_ambiguous_inputs_fail(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    cases = ("missing", "untracked", "empty", "symlink", "ambiguous")
    for case in cases:
        case_root = tmp_path / case
        case_root.mkdir()
        source = _valid_source()
        repo = _init_repo(case_root, source=source)
        if case == "missing":
            source["evidence_inputs"][0]["path"] = "evidence/missing.txt"
            _write_json(repo / SOURCE_REL, source)
            _git(repo, "add", SOURCE_REL)
            _git(repo, "commit", "-m", "reference missing input")
        elif case == "untracked":
            source["evidence_inputs"][0]["path"] = "evidence/untracked.txt"
            _write_json(repo / SOURCE_REL, source)
            _git(repo, "add", SOURCE_REL)
            _git(repo, "commit", "-m", "reference untracked input")
            (repo / "evidence/untracked.txt").write_text("untracked\n", encoding="utf-8")
        elif case == "empty":
            (repo / "evidence/determinism.txt").write_bytes(b"")
            _git(repo, "add", "evidence/determinism.txt")
            _git(repo, "commit", "-m", "empty tracked input")
        elif case == "symlink":
            (repo / "evidence/determinism.txt").unlink()
            (repo / "evidence/determinism.txt").symlink_to("scope.json")
            _git(repo, "add", "evidence/determinism.txt")
            _git(repo, "commit", "-m", "symlink tracked input")
        else:
            (repo / "evidence/Determinism.txt").write_text(
                "ambiguous case\n", encoding="utf-8"
            )
            _git(repo, "add", "evidence/Determinism.txt")
            _git(repo, "commit", "-m", "ambiguous tracked input case")
        assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
        assert not (repo / REPORT_REL).exists()
        assert not (repo / MANIFEST_REL).exists()


@pytest.mark.parametrize(
    "source_arg",
    (
        "/absolute/source.json",
        "close//epic123.json",
        "close/./epic123.json",
        "close/../epic123.json",
        "close\\epic123.json",
    ),
)
def test_unsafe_or_aliased_source_arguments_fail(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    source_arg: str,
) -> None:
    repo = _init_repo(tmp_path)
    assert _run(repo, monkeypatch, "--source", source_arg, "--write") == 1
    assert not (repo / REPORT_REL).exists()
    assert not (repo / MANIFEST_REL).exists()


def test_caller_selected_output_root_is_not_a_cli_surface() -> None:
    with pytest.raises(SystemExit) as exc_info:
        close_pack._parse_args(
            ["--source", SOURCE_REL, "--write", "--output-root", "elsewhere"]
        )
    assert exc_info.value.code == 2


@pytest.mark.parametrize(
    "arguments",
    (
        ["--source", SOURCE_REL, "--source", SOURCE_REL, "--write"],
        ["--source", SOURCE_REL, "--write", "--write"],
        ["--source", SOURCE_REL, "--check", "--check"],
        ["--source", SOURCE_REL, "--write", "--check"],
    ),
)
def test_cli_accepts_exactly_one_source_and_one_mode(arguments: list[str]) -> None:
    with pytest.raises(SystemExit) as exc_info:
        close_pack._parse_args(arguments)
    assert exc_info.value.code == 2


def test_output_collision_with_a_causal_input_fails(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source = _valid_source()
    source["plan_path"] = REPORT_REL
    repo = _init_repo(tmp_path, source=source)
    (repo / REPORT_REL).write_text("tracked colliding plan\n", encoding="utf-8")
    _git(repo, "add", REPORT_REL)
    _git(repo, "commit", "-m", "tracked collision")
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert (repo / REPORT_REL).read_text(encoding="utf-8") == "tracked colliding plan\n"
    assert not (repo / MANIFEST_REL).exists()


@pytest.mark.parametrize("posture", ("tracked_alias", "exact_and_alias", "ignored_alias"))
def test_case_ambiguous_output_aliases_fail_without_mutation(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    posture: str,
) -> None:
    repo = _init_repo(tmp_path)
    alias_rel = "audit/EPIC-123_Close_Report.md"
    alias = repo / alias_rel
    alias.write_text("case alias\n", encoding="utf-8")
    tracked = [alias_rel]
    if posture == "exact_and_alias":
        (repo / REPORT_REL).write_text("exact prior target\n", encoding="utf-8")
        tracked.append(REPORT_REL)
    elif posture == "ignored_alias":
        (repo / ".gitignore").write_text(f"/{alias_rel}\n", encoding="utf-8")
        tracked = [".gitignore"]
    _git(repo, "add", *tracked)
    _git(repo, "commit", "-m", "add output case posture")
    assert _git(repo, "status", "--porcelain=v1", "--untracked-files=all") == ""
    paths = [alias]
    if posture == "exact_and_alias":
        paths.append(repo / REPORT_REL)
    before = {path: (_read_noatime(path), _metadata(path)) for path in paths}

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert before == {path: (_read_noatime(path), _metadata(path)) for path in paths}
    assert not (repo / MANIFEST_REL).exists()
    assert not list((repo / "audit").glob(".*.epic-close-pack.*"))


def test_dirty_tree_write_and_check_attempts_fail(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    write_repo = _init_repo(tmp_path / "write")
    (write_repo / "plans/epic123.md").write_text("dirty\n", encoding="utf-8")
    assert _run(write_repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert not (write_repo / REPORT_REL).exists()

    check_repo = _init_repo(tmp_path / "check")
    _generate_and_commit(check_repo, monkeypatch)
    (check_repo / "untracked.txt").write_text("residue\n", encoding="utf-8")
    assert _run(check_repo, monkeypatch, "--source", SOURCE_REL, "--check") == 1

    empty_directory_repo = _init_repo(tmp_path / "empty-directory")
    (empty_directory_repo / "ignored-empty-residue").mkdir()
    assert _run(
        empty_directory_repo,
        monkeypatch,
        "--source",
        SOURCE_REL,
        "--write",
    ) == 1
    assert not (empty_directory_repo / REPORT_REL).exists()


def test_ignored_case_aliases_fail_for_causal_inputs_and_check_outputs(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    input_repo = _init_repo(tmp_path / "input")
    input_alias = "evidence/Determinism.txt"
    (input_repo / ".gitignore").write_text(f"/{input_alias}\n", encoding="utf-8")
    _git(input_repo, "add", ".gitignore")
    _git(input_repo, "commit", "-m", "ignore input alias")
    (input_repo / input_alias).write_text("ignored alias\n", encoding="utf-8")
    assert _git(input_repo, "status", "--porcelain=v1", "--untracked-files=all") == ""
    assert _run(input_repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1

    output_repo = _init_repo(tmp_path / "output")
    _generate_and_commit(output_repo, monkeypatch)
    output_alias = "audit/EPIC-123_Close_Report.md"
    (output_repo / ".gitignore").write_text(f"/{output_alias}\n", encoding="utf-8")
    _git(output_repo, "add", ".gitignore")
    _git(output_repo, "commit", "-m", "ignore output alias")
    (output_repo / output_alias).write_text("ignored alias\n", encoding="utf-8")
    assert _git(output_repo, "status", "--porcelain=v1", "--untracked-files=all") == ""
    assert _run(output_repo, monkeypatch, "--source", SOURCE_REL, "--check") == 1


def test_missing_partial_and_malformed_committed_outputs_fail_check(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    missing = _init_repo(tmp_path / "missing")
    assert _run(missing, monkeypatch, "--source", SOURCE_REL, "--check") == 1

    partial = _init_repo(tmp_path / "partial")
    assert _run(partial, monkeypatch, "--source", SOURCE_REL, "--write") == 0
    (partial / REPORT_REL).unlink()
    _git(partial, "add", MANIFEST_REL)
    _git(partial, "commit", "-m", "commit partial candidate")
    assert _run(partial, monkeypatch, "--source", SOURCE_REL, "--check") == 1

    malformed = _init_repo(tmp_path / "malformed")
    _generate_and_commit(malformed, monkeypatch)
    (malformed / MANIFEST_REL).write_text("{}\n", encoding="utf-8")
    _git(malformed, "add", MANIFEST_REL)
    _git(malformed, "commit", "-m", "commit malformed candidate")
    assert _run(malformed, monkeypatch, "--source", SOURCE_REL, "--check") == 1


def test_input_change_during_evaluation_fails_before_publication(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path)
    original = close_pack._render_candidate
    calls = 0

    def mutate_after_first_render(model: close_pack.CandidateModel) -> dict[str, bytes]:
        nonlocal calls
        calls += 1
        rendered = original(model)
        if calls == 1:
            (repo / "plans/epic123.md").write_text("changed during render\n", encoding="utf-8")
        return rendered

    monkeypatch.setattr(close_pack, "_render_candidate", mutate_after_first_render)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert not (repo / REPORT_REL).exists()
    assert not (repo / MANIFEST_REL).exists()


def test_nondeterministic_rendering_fails_without_writes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path)
    original = close_pack._render_candidate
    calls = 0

    def alternate(model: close_pack.CandidateModel) -> dict[str, bytes]:
        nonlocal calls
        calls += 1
        rendered = original(model)
        if calls == 2:
            rendered[REPORT_REL] = rendered[REPORT_REL][:-1] + b"changed\n"
        return rendered

    monkeypatch.setattr(close_pack, "_render_candidate", alternate)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert not (repo / REPORT_REL).exists()
    assert not (repo / MANIFEST_REL).exists()


def test_source_commit_hash_and_feedback_dependencies_do_not_enter_outputs(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path)
    head = _git(repo, "rev-parse", "HEAD").encode("ascii")
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 0
    combined = (repo / REPORT_REL).read_bytes() + (repo / MANIFEST_REL).read_bytes()
    assert head not in combined
    source_text = (ROOT / "tools/qa/generate_epic_close_pack.py").read_text(
        encoding="utf-8"
    )
    for forbidden in (
        "HDE-EPIC" + "038",
        "_HDE_EPIC" + "038_PRIVATE_CI",
        "update_evidence_index",
        "orientation_demo",
        "path_proof",
        "release_id",
        "build_release_attestation",
        "acceptance_map",
        "token_evidence_matrix",
        "audit/qa/",
        "requests.",
        "urllib.",
        "os.utime",
        "os.utimes",
        ".touch(",
        "futimens",
        "futimes",
        "utimensat",
        "'touch'",
        '"touch"',
    ):
        assert forbidden not in source_text


def test_nonregular_or_symlinked_output_targets_fail_without_replacement(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path)
    (repo / REPORT_REL).symlink_to("README.md")
    _git(repo, "add", REPORT_REL)
    _git(repo, "commit", "-m", "tracked symlink output")
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert (repo / REPORT_REL).is_symlink()
    assert not (repo / MANIFEST_REL).exists()


def test_closed_rails_are_required_without_becoming_candidate_bytes(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path)
    monkeypatch.setenv("ALLOW_NETWORK", "1")
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert not (repo / REPORT_REL).exists()


def test_check_rejects_unsupported_repository_format_without_mutation(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    repo = _init_repo(tmp_path)
    _generate_and_commit(repo, monkeypatch)
    _git(repo, "config", "core.repositoryformatversion", "2")
    config_path = repo / ".git/config"
    index_path = repo / ".git/index"
    protected_before = {
        config_path: (_read_noatime(config_path), _metadata(config_path)),
        index_path: (_read_noatime(index_path), _metadata(index_path)),
    }
    repository_before = close_pack._repository_metadata(repo)

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--check") == 1
    captured = capsys.readouterr()
    assert "EPIC_CLOSE_PACK_ERROR:GIT_CONFIG_UNSUPPORTED" in captured.err
    assert repository_before == close_pack._repository_metadata(repo)
    assert protected_before == {
        config_path: (_read_noatime(config_path), _metadata(config_path)),
        index_path: (_read_noatime(index_path), _metadata(index_path)),
    }


@pytest.mark.parametrize(
    "malformed_value",
    (
        b'"unterminated',
        b"trailing\\",
        b"embedded\0nul",
        b"embedded\x01control",
    ),
    ids=("unterminated-quote", "trailing-backslash", "nul", "control"),
)
def test_check_rejects_malformed_ignored_config_value_without_mutation(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    malformed_value: bytes,
) -> None:
    repo = _init_repo(tmp_path)
    _generate_and_commit(repo, monkeypatch)
    config_path = repo / ".git/config"
    index_path = repo / ".git/index"
    config_path.write_bytes(
        _read_noatime(config_path)
        + b"\n[ignored]\nmalformed = "
        + malformed_value
        + b"\n"
    )
    protected_before = {
        config_path: (_read_noatime(config_path), _metadata(config_path)),
        index_path: (_read_noatime(index_path), _metadata(index_path)),
    }
    repository_before = close_pack._repository_metadata(repo)
    capsys.readouterr()

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--check") == 1
    first_error = capsys.readouterr().err
    assert first_error.startswith("EPIC_CLOSE_PACK_ERROR:GIT_CONFIG_")
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--check") == 1
    assert capsys.readouterr().err == first_error
    assert repository_before == close_pack._repository_metadata(repo)
    assert protected_before == {
        config_path: (_read_noatime(config_path), _metadata(config_path)),
        index_path: (_read_noatime(index_path), _metadata(index_path)),
    }


def test_extensions_subsection_cannot_impersonate_repository_extension(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    repo = _init_repo(tmp_path)
    _generate_and_commit(repo, monkeypatch)
    config_path = repo / ".git/config"
    index_path = repo / ".git/index"
    config = _read_noatime(config_path).replace(
        b"repositoryformatversion = 0", b"repositoryformatversion = 1"
    )
    config_path.write_bytes(
        config + b'\n[extensions "foo"]\nobjectformat = sha1\n'
    )
    git_probe = subprocess.run(
        ("git", "rev-parse", "--verify", "HEAD"),
        cwd=repo,
        capture_output=True,
        check=False,
    )
    assert git_probe.returncode != 0
    protected_before = {
        config_path: (_read_noatime(config_path), _metadata(config_path)),
        index_path: (_read_noatime(index_path), _metadata(index_path)),
    }
    repository_before = close_pack._repository_metadata(repo)

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--check") == 1
    assert "EPIC_CLOSE_PACK_ERROR:GIT_CONFIG_UNSUPPORTED" in capsys.readouterr().err
    assert repository_before == close_pack._repository_metadata(repo)
    assert protected_before == {
        config_path: (_read_noatime(config_path), _metadata(config_path)),
        index_path: (_read_noatime(index_path), _metadata(index_path)),
    }


def test_oversized_unrelated_tracked_file_fails_before_candidate_publication(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    repo = _init_repo(tmp_path)
    oversized = repo / "unrelated-large.bin"
    oversized.write_bytes(b"x" * 2048)
    _git(repo, "add", "unrelated-large.bin")
    _git(repo, "commit", "-m", "add boundedness fixture")
    monkeypatch.setattr(close_pack, "MAX_WORKTREE_FILE_BYTES", 1024)

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert "EPIC_CLOSE_PACK_ERROR:INPUT_TOO_LARGE" in capsys.readouterr().err
    assert not (repo / REPORT_REL).exists()
    assert not (repo / MANIFEST_REL).exists()


@pytest.mark.parametrize("mode", ("check", "write"))
def test_modes_use_no_git_subprocess(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    mode: str,
) -> None:
    repo = _init_repo(tmp_path)
    _generate_and_commit(repo, monkeypatch)
    repository_before = close_pack._repository_metadata(repo)
    index_path = repo / ".git/index"
    index_before = (_read_noatime(index_path), _metadata(index_path))

    def reject_git_subprocess(*_args: object, **_kwargs: object) -> bytes:
        raise AssertionError(f"{mode} mode attempted a subprocess")

    monkeypatch.setattr(subprocess, "run", reject_git_subprocess)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, f"--{mode}") == 0
    assert repository_before == close_pack._repository_metadata(repo)
    assert index_before == (_read_noatime(index_path), _metadata(index_path))


def test_git_control_environment_is_sanitized_and_fsmonitor_is_disabled(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path / "target")
    decoy = _init_repo(tmp_path / "decoy")
    sentinel = tmp_path / "fsmonitor-invoked"
    fsmonitor = tmp_path / "fsmonitor.sh"
    fsmonitor.write_text(
        f"#!/bin/sh\ntouch \"{sentinel}\"\nexit 1\n",
        encoding="utf-8",
    )
    fsmonitor.chmod(0o755)
    _git(repo, "config", "core.fsmonitor", str(fsmonitor))

    poisoned = {
        "GIT_ALTERNATE_OBJECT_DIRECTORIES": str(decoy / ".git/objects"),
        "GIT_COMMON_DIR": str(decoy / ".git"),
        "GIT_CONFIG_COUNT": "1",
        "GIT_CONFIG_KEY_0": "core.worktree",
        "GIT_CONFIG_VALUE_0": str(decoy),
        "GIT_DIR": str(decoy / ".git"),
        "GIT_INDEX_FILE": str(decoy / ".git/index"),
        "GIT_OBJECT_DIRECTORY": str(decoy / ".git/objects"),
        "GIT_WORK_TREE": str(decoy),
    }
    for key, value in poisoned.items():
        monkeypatch.setenv(key, value)

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 0
    assert (repo / REPORT_REL).is_file()
    assert (repo / MANIFEST_REL).is_file()
    assert not (decoy / REPORT_REL).exists()
    assert not (decoy / MANIFEST_REL).exists()
    assert not sentinel.exists()


def test_writer_does_not_invoke_path_shadowed_git(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path / "target")
    fake_bin = tmp_path / "fake-bin"
    fake_bin.mkdir()
    sentinel = tmp_path / "fake-git-invoked"
    fake_git = fake_bin / "git"
    fake_git.write_text(
        f'#!/bin/sh\ntouch "{sentinel}"\nexit 97\n',
        encoding="utf-8",
    )
    fake_git.chmod(0o755)
    monkeypatch.setenv("PATH", f"{fake_bin}{os.pathsep}{os.environ['PATH']}")

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 0
    assert not sentinel.exists()


def test_replace_refs_cannot_substitute_a_different_head_tree(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path)
    original_head = _git(repo, "rev-parse", "HEAD")
    (repo / "plans/epic123.md").write_text(
        "# Plan\n\nReplacement-ref bytes.\n", encoding="utf-8"
    )
    _git(repo, "add", "plans/epic123.md")
    _git(repo, "commit", "-m", "create replacement commit")
    replacement_head = _git(repo, "rev-parse", "HEAD")
    _git(repo, "update-ref", "HEAD", original_head)
    _git(repo, "replace", original_head, replacement_head)

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert _git(repo, "rev-parse", "HEAD") == original_head
    assert not (repo / REPORT_REL).exists()
    assert not (repo / MANIFEST_REL).exists()


@pytest.mark.parametrize(
    "malformation",
    ("bad-oid", "bad-ref", "peeled-placement", "sorted-order"),
)
def test_malformed_unselected_packed_ref_entry_fails_closed(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    malformation: str,
) -> None:
    repo = _init_repo(tmp_path)
    _generate_and_commit(repo, monkeypatch)
    selected_ref = _git(repo, "symbolic-ref", "HEAD")
    selected_oid = _git(repo, "rev-parse", "HEAD")
    _git(repo, "pack-refs", "--all", "--prune")
    assert not (repo / ".git" / selected_ref).exists()
    packed_refs = repo / ".git/packed-refs"
    original = _read_noatime(packed_refs)
    lines = original.splitlines(keepends=True)
    assert lines and lines[0].startswith(b"# pack-refs with:")
    assert any(selected_ref.encode() in line for line in lines)

    if malformation == "bad-oid":
        tampered = original + b"g" * len(selected_oid) + b" refs/heads/zzz\n"
    elif malformation == "bad-ref":
        tampered = original + selected_oid.encode() + b" refs/heads/bad..ref\n"
    elif malformation == "peeled-placement":
        tampered = lines[0] + b"^" + selected_oid.encode() + b"\n" + b"".join(
            lines[1:]
        )
    else:
        assert b" sorted" in lines[0]
        tampered = original + selected_oid.encode() + b" refs/heads/aaa\n"
    packed_refs.write_bytes(tampered)
    index_path = repo / ".git/index"
    protected_before = {
        packed_refs: (_read_noatime(packed_refs), _metadata(packed_refs)),
        index_path: (_read_noatime(index_path), _metadata(index_path)),
    }
    repository_before = close_pack._repository_metadata(repo)
    capsys.readouterr()

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--check") == 1
    assert (
        capsys.readouterr().err
        == "EPIC_CLOSE_PACK_ERROR:GIT_CONTROL_STATE_UNAVAILABLE\n"
    )
    assert repository_before == close_pack._repository_metadata(repo)
    assert protected_before == {
        packed_refs: (_read_noatime(packed_refs), _metadata(packed_refs)),
        index_path: (_read_noatime(index_path), _metadata(index_path)),
    }


def test_annotated_tag_target_with_wrong_object_id_width_fails_closed(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    repo = _init_repo(tmp_path)
    _generate_and_commit(repo, monkeypatch)
    algorithm = _git(repo, "rev-parse", "--show-object-format")
    assert algorithm == "sha1"
    tag_payload = (
        b"object "
        + b"0" * 64
        + b"\ntype commit\ntag wrong-width\n"
        + b"tagger Close Pack Test <close-pack@example.invalid> 0 +0000\n\n"
        + b"wrong object-id width\n"
    )
    tag_oid = close_pack._hash_git_object("tag", tag_payload, algorithm)
    raw_tag = f"tag {len(tag_payload)}\0".encode("ascii") + tag_payload
    object_path = repo / ".git/objects" / tag_oid[:2] / tag_oid[2:]
    object_path.parent.mkdir(parents=True, exist_ok=True)
    object_path.write_bytes(zlib.compress(raw_tag))
    head_path = repo / ".git/HEAD"
    head_path.write_text(f"{tag_oid}\n", encoding="ascii")
    index_path = repo / ".git/index"
    protected_before = {
        head_path: (_read_noatime(head_path), _metadata(head_path)),
        index_path: (_read_noatime(index_path), _metadata(index_path)),
    }
    capsys.readouterr()

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--check") == 1
    assert (
        capsys.readouterr().err
        == "EPIC_CLOSE_PACK_ERROR:GIT_OBJECT_FORMAT_MISMATCH\n"
    )
    assert protected_before == {
        head_path: (_read_noatime(head_path), _metadata(head_path)),
        index_path: (_read_noatime(index_path), _metadata(index_path)),
    }


def test_intent_to_add_index_residue_fails_clean_tree_posture(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path)
    ghost = repo / "ghost"
    ghost.write_text("intent to add\n", encoding="utf-8")
    _git(repo, "add", "-N", "ghost")
    ghost.unlink()

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert not (repo / REPORT_REL).exists()
    assert not (repo / MANIFEST_REL).exists()


def test_checksum_valid_mandatory_index_extension_fails_closed(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    repo = _init_repo(tmp_path)
    _generate_and_commit(repo, monkeypatch)
    index_path = repo / ".git/index"
    index_before = _append_checksum_valid_index_extension(repo, b"abcd")
    index_metadata_before = _metadata(index_path)

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--check") == 1
    captured = capsys.readouterr()
    assert "EPIC_CLOSE_PACK_ERROR:GIT_CLEAN_STATE_UNAVAILABLE" in captured.err
    assert _read_noatime(index_path) == index_before
    assert _metadata(index_path) == index_metadata_before


def test_linked_worktree_lifecycle_reaches_clean_exact_head(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    primary = _init_repo(tmp_path / "primary")
    linked = tmp_path / "linked"
    _git(primary, "worktree", "add", "--detach", str(linked), "HEAD")

    assert _run(linked, monkeypatch, "--source", SOURCE_REL, "--write") == 0
    _git(linked, "add", REPORT_REL, MANIFEST_REL)
    _git(linked, "commit", "-m", "commit linked-worktree candidate")
    exact_head = _git(linked, "rev-parse", "HEAD")
    assert _run(linked, monkeypatch, "--source", SOURCE_REL, "--check") == 0
    assert _git(linked, "rev-parse", "HEAD") == exact_head
    assert _git(linked, "status", "--porcelain=v1", "--untracked-files=all") == ""


@pytest.mark.skipif(
    os.name != "posix" or not getattr(os, "O_PATH", 0),
    reason="requires POSIX O_PATH traversal",
)
def test_linked_marker_traversal_uses_o_path_through_execute_only_ancestor(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    ancestor = tmp_path / "execute-only-ancestor"
    ancestor.mkdir()
    primary = _init_repo(ancestor / "primary")
    linked = ancestor / "linked"
    _git(primary, "worktree", "add", "--detach", str(linked), "HEAD")
    _generate_and_commit(linked, monkeypatch)
    git_dir = Path(_git(linked, "rev-parse", "--absolute-git-dir"))
    git_dir_metadata = git_dir.lstat()
    original_open = os.open
    observed_flags: list[int] = []
    required_flags = os.O_PATH | os.O_DIRECTORY | os.O_NOFOLLOW
    if getattr(os, "O_CLOEXEC", 0):
        required_flags |= os.O_CLOEXEC

    def observe_open(
        path: str | bytes | int,
        flags: int,
        mode: int = 0o777,
        *,
        dir_fd: int | None = None,
    ) -> int:
        if (
            not isinstance(path, int)
            and os.fsdecode(path) == ancestor.name
            and flags & os.O_PATH
        ):
            observed_flags.append(flags)
        return original_open(path, flags, mode, dir_fd=dir_fd)

    ancestor.chmod(0o111)
    monkeypatch.setattr(close_pack.os, "open", observe_open)
    try:
        resolved, identity = close_pack._path_without_symlink_components(
            git_dir,
            final_directory=True,
            code="GIT_CONTEXT_INVALID",
        )
    finally:
        ancestor.chmod(0o755)
    assert resolved == git_dir
    assert identity == (git_dir_metadata.st_dev, git_dir_metadata.st_ino)
    assert observed_flags
    assert all(flags & required_flags == required_flags for flags in observed_flags)
    monkeypatch.setattr(close_pack.os, "open", original_open)
    assert _run(linked, monkeypatch, "--source", SOURCE_REL, "--check") == 0


@pytest.mark.skipif(os.name != "posix", reason="requires POSIX symlink atime semantics")
@pytest.mark.parametrize("marker_kind", ("gitdir", "commondir"))
def test_linked_worktree_marker_intermediate_symlink_fails_without_atime_change(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    marker_kind: str,
) -> None:
    primary = _init_repo(tmp_path / "primary")
    linked = tmp_path / "linked"
    _git(primary, "worktree", "add", "--detach", str(linked), "HEAD")
    _generate_and_commit(linked, monkeypatch)
    git_dir = Path(_git(linked, "rev-parse", "--absolute-git-dir"))

    if marker_kind == "gitdir":
        alias = tmp_path / "gitdir-alias"
        alias.symlink_to(git_dir.parent, target_is_directory=True)
        marker = linked / ".git"
        tampered_marker = f"gitdir: {alias / git_dir.name}\n".encode()
    else:
        alias = git_dir / "common-alias"
        alias.symlink_to(primary, target_is_directory=True)
        marker = git_dir / "commondir"
        tampered_marker = b"common-alias/.git\n"

    original_marker = _read_noatime(marker)
    marker.write_bytes(tampered_marker)
    stale_atime_ns = 946_684_800_000_000_000
    alias_metadata = alias.lstat()
    os.utime(
        alias,
        ns=(stale_atime_ns, alias_metadata.st_mtime_ns),
        follow_symlinks=False,
    )
    index_path = git_dir / "index"
    index_before = (_read_noatime(index_path), _metadata(index_path))
    marker_before = (_read_noatime(marker), _metadata(marker))
    outputs_before = {
        REPORT_REL: _read_noatime(linked / REPORT_REL),
        MANIFEST_REL: _read_noatime(linked / MANIFEST_REL),
    }
    capsys.readouterr()

    try:
        assert _run(linked, monkeypatch, "--source", SOURCE_REL, "--check") == 1
        assert capsys.readouterr().err.startswith(
            "EPIC_CLOSE_PACK_ERROR:GIT_CONTEXT_"
        )
        assert alias.lstat().st_atime_ns == stale_atime_ns
        assert marker_before == (_read_noatime(marker), _metadata(marker))
        assert index_before == (_read_noatime(index_path), _metadata(index_path))
        assert outputs_before == {
            REPORT_REL: _read_noatime(linked / REPORT_REL),
            MANIFEST_REL: _read_noatime(linked / MANIFEST_REL),
        }
    finally:
        marker.write_bytes(original_marker)
    assert _git(linked, "status", "--porcelain=v1", "--untracked-files=all") == ""


def test_linked_worktree_git_marker_redirection_fails_closed(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    primary = _init_repo(tmp_path / "primary")
    linked = tmp_path / "linked"
    decoy = tmp_path / "decoy"
    _git(primary, "worktree", "add", "--detach", str(linked), "HEAD")
    _git(primary, "worktree", "add", "--detach", str(decoy), "HEAD")
    marker = linked / ".git"
    original_marker = marker.read_bytes()
    decoy_marker = (decoy / ".git").read_bytes()
    original_render = close_pack._render_candidate
    calls = 0

    def redirect_after_first_render(
        model: close_pack.CandidateModel,
    ) -> dict[str, bytes]:
        nonlocal calls
        calls += 1
        rendered = original_render(model)
        if calls == 1:
            marker.write_bytes(decoy_marker)
        return rendered

    monkeypatch.setattr(close_pack, "_render_candidate", redirect_after_first_render)
    try:
        assert _run(linked, monkeypatch, "--source", SOURCE_REL, "--write") == 1
        assert not (linked / REPORT_REL).exists()
        assert not (linked / MANIFEST_REL).exists()
        assert not list((linked / "audit").glob(".*.epic-close-pack.*"))
    finally:
        marker.write_bytes(original_marker)
    assert _git(linked, "status", "--porcelain=v1", "--untracked-files=all") == ""


def test_linked_worktree_gitdir_backlink_retargeting_fails_closed(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    primary = _init_repo(tmp_path / "primary")
    linked = tmp_path / "linked"
    _git(primary, "worktree", "add", "--detach", str(linked), "HEAD")
    _generate_and_commit(linked, monkeypatch)
    git_dir = Path(_git(linked, "rev-parse", "--absolute-git-dir"))
    backlink = git_dir / "gitdir"
    original_backlink = backlink.read_bytes()
    index_path = git_dir / "index"
    index_before = _read_noatime(index_path)
    outputs_before = {
        REPORT_REL: _read_noatime(linked / REPORT_REL),
        MANIFEST_REL: _read_noatime(linked / MANIFEST_REL),
    }
    original_render = close_pack._render_candidate
    calls = 0

    def retarget_after_first_render(
        model: close_pack.CandidateModel,
    ) -> dict[str, bytes]:
        nonlocal calls
        calls += 1
        rendered = original_render(model)
        if calls == 1:
            backlink.write_text(f"{primary / '.git'}\n", encoding="utf-8")
        return rendered

    monkeypatch.setattr(close_pack, "_render_candidate", retarget_after_first_render)
    try:
        assert _run(linked, monkeypatch, "--source", SOURCE_REL, "--check") == 1
        captured = capsys.readouterr()
        assert "EPIC_CLOSE_PACK_ERROR:GIT_CONTEXT_CHANGED" in captured.err
        assert outputs_before == {
            REPORT_REL: _read_noatime(linked / REPORT_REL),
            MANIFEST_REL: _read_noatime(linked / MANIFEST_REL),
        }
        assert _read_noatime(index_path) == index_before
        assert not list((linked / "audit").glob(".*.epic-close-pack.*"))
    finally:
        backlink.write_bytes(original_backlink)
    assert _git(linked, "status", "--porcelain=v1", "--untracked-files=all") == ""


def test_linked_worktree_common_dir_retargeting_fails_closed(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    primary = _init_repo(tmp_path / "primary")
    decoy = _init_repo(tmp_path / "decoy-primary")
    linked = tmp_path / "linked"
    _git(primary, "worktree", "add", "--detach", str(linked), "HEAD")
    git_dir = Path(_git(linked, "rev-parse", "--absolute-git-dir"))
    commondir = git_dir / "commondir"
    original_commondir = commondir.read_bytes()
    original_render = close_pack._render_candidate
    calls = 0

    def retarget_after_first_render(
        model: close_pack.CandidateModel,
    ) -> dict[str, bytes]:
        nonlocal calls
        calls += 1
        rendered = original_render(model)
        if calls == 1:
            commondir.write_text(f"{decoy / '.git'}\n", encoding="utf-8")
        return rendered

    monkeypatch.setattr(close_pack, "_render_candidate", retarget_after_first_render)
    try:
        assert _run(linked, monkeypatch, "--source", SOURCE_REL, "--write") == 1
        assert not (linked / REPORT_REL).exists()
        assert not (linked / MANIFEST_REL).exists()
        assert not list((linked / "audit").glob(".*.epic-close-pack.*"))
    finally:
        commondir.write_bytes(original_commondir)
    assert _git(linked, "status", "--porcelain=v1", "--untracked-files=all") == ""
