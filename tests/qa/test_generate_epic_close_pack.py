from __future__ import annotations

import copy
import hashlib
import json
import os
import shutil
import stat
import struct
import subprocess
import zlib
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
                    "The bounded implementation is represented by the tracked inputs.",
                    "Candidate validation remains separate from acceptance.",
                ],
            },
            {
                "heading": "Validation posture",
                "body_lines": ["Only exact committed candidate bytes are checked."],
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
    rel: str,
    *,
    require_change: bool,
) -> None:
    assert before.keys() == after.keys()
    for path, prior in before.items():
        current = after[path]
        if path != rel:
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

    digest_line = copy.deepcopy(valid)
    digest_line["report_sections"][0]["body_lines"][0] = "a" * 64
    assert validator.is_valid(digest_line)

    assert validator.is_valid(valid)
    assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    assert schema["$id"] == close_pack.SCHEMA_REL
    assert schema["additionalProperties"] is False


@pytest.mark.parametrize(
    ("location", "value"),
    (
        ("binding", "run_id"),
        ("binding", "hosted-result"),
        ("evidence_path", "audit/hosted_receipt.json"),
        ("evidence_path", "audit/hosted/result.json"),
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
        ("evidence_path", "audit/hosted-result.json"),
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


def test_check_preserves_stale_git_control_atime_without_mutating_it(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
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

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--check") == 0
    assert head_path.stat().st_atime_ns == stale_atime_ns


def test_check_preserves_stale_loose_object_atime(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
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

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--check") == 0
    assert object_path.stat().st_atime_ns == stale_atime_ns
    assert _git(repo, "status", "--porcelain=v1", "--untracked-files=all") == ""


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


def test_checksum_valid_poisoned_symlink_stat_cache_cannot_hide_target_change(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    repo = _init_repo(tmp_path)
    rel = "tracked-link"
    link = repo / rel
    link.symlink_to("target-one")
    _git(repo, "add", rel)
    _git(repo, "commit", "-m", "add unrelated tracked symlink")
    _generate_and_commit(repo, monkeypatch)

    mode, object_type, object_id, path = _git(
        repo, "ls-tree", "HEAD", "--", rel
    ).split()
    algorithm = _git(repo, "rev-parse", "--show-object-format")
    assert (mode, object_type, path) == ("120000", "blob", rel)
    assert close_pack._git_blob_id(b"target-one", algorithm) == object_id
    assert close_pack._git_blob_id(b"target-two", algorithm) != object_id

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

    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--check") == 1
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


def test_all_candidate_bytes_are_rendered_before_publication(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path)
    original = close_pack._publish_pair
    observed: dict[str, bytes] = {}

    def inspect_pair(root: Path, outputs: dict[str, bytes], verifier) -> None:
        observed.update(outputs)
        assert set(outputs) == {REPORT_REL, MANIFEST_REL}
        assert all(payload.endswith(b"\n") for payload in outputs.values())
        original(root, outputs, verifier)

    monkeypatch.setattr(close_pack, "_publish_pair", inspect_pair)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 0
    assert observed[REPORT_REL] == (repo / REPORT_REL).read_bytes()
    assert observed[MANIFEST_REL] == (repo / MANIFEST_REL).read_bytes()


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
    source["report_sections"][0]["body_lines"].append("A later tracked revision.")
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
    ) -> None:
        nonlocal calls
        calls += 1
        if calls == 2:
            raise OSError("injected second installation failure")
        original(anchor, staged_name, expected, installed)

    monkeypatch.setattr(close_pack, "_install_staged_output", fail_second_install)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert _read_noatime(repo / REPORT_REL) == old_report
    assert _read_noatime(repo / MANIFEST_REL) == old_manifest
    assert _metadata(repo / REPORT_REL) == old_metadata[REPORT_REL]
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
    source["report_sections"][0]["body_lines"].append("A tracked revision.")
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
    ) -> None:
        nonlocal calls
        calls += 1
        original_install(anchor, staged_name, expected, installed)
        if calls == 1:
            raise OSError("injected exception after installation")

    monkeypatch.setattr(close_pack, "_install_staged_output", install_then_fail)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert _read_noatime(repo / REPORT_REL) == old_report
    assert _read_noatime(repo / MANIFEST_REL) == old_manifest
    assert not list((repo / "audit").glob(".*.epic-close-pack.*"))
    assert _git(repo, "status", "--porcelain=v1", "--untracked-files=all") == ""


@pytest.mark.parametrize("failure_point", ("staging", "first_install"))
def test_failure_before_any_install_preserves_all_target_metadata(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    failure_point: str,
) -> None:
    repo = _init_repo(tmp_path)
    old_report, old_manifest = _generate_and_commit(repo, monkeypatch)
    source = _valid_source()
    source["report_sections"][0]["body_lines"].append("A tracked revision.")
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
            "A concurrent-publication revision."
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
            "A post-install concurrency revision."
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
        assert (repo / REPORT_REL).read_bytes() == old_report
    else:
        assert not (repo / REPORT_REL).exists()
    assert not list((repo / "audit").glob(".*.epic-close-pack.*"))


def test_post_install_concurrent_output_is_not_clobbered_by_rollback(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path)
    old_report, old_manifest = _generate_and_commit(repo, monkeypatch)
    source = _valid_source()
    source["report_sections"][0]["body_lines"].append("A tracked revision.")
    _write_json(repo / SOURCE_REL, source)
    _git(repo, "add", SOURCE_REL)
    _git(repo, "commit", "-m", "change tracked candidate source")
    concurrent = b"concurrent post-install bytes\n"
    original_publish = close_pack._publish_pair

    def mutate_in_verifier(root: Path, outputs: dict[str, bytes], verifier) -> None:
        def concurrent_failure() -> None:
            (repo / MANIFEST_REL).write_bytes(concurrent)
            raise OSError("injected verifier failure after concurrent mutation")

        original_publish(root, outputs, concurrent_failure)

    monkeypatch.setattr(close_pack, "_publish_pair", mutate_in_verifier)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 1
    assert (repo / MANIFEST_REL).read_bytes() == concurrent
    assert old_manifest != concurrent
    assert (repo / REPORT_REL).read_bytes() == old_report
    assert not list((repo / "audit").glob(".*.epic-close-pack.*"))


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
        "os.utime(",
        "os.utimes(",
        "utimensat",
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


def test_check_uses_no_git_subprocess(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = _init_repo(tmp_path)
    _generate_and_commit(repo, monkeypatch)
    repository_before = close_pack._repository_metadata(repo)
    index_path = repo / ".git/index"
    index_before = (_read_noatime(index_path), _metadata(index_path))

    def reject_git_subprocess(*_args: object, **_kwargs: object) -> bytes:
        raise AssertionError("check mode attempted a Git subprocess")

    monkeypatch.setattr(close_pack, "_run_git", reject_git_subprocess)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--check") == 0
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


def test_git_subprocesses_bypass_path_shadowing_and_disable_lazy_fetch(
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

    original_run = subprocess.run
    git_environments: list[dict[str, str]] = []

    def observe_git(*args: object, **kwargs: object) -> subprocess.CompletedProcess[bytes]:
        environment = kwargs.get("env")
        if isinstance(environment, dict):
            git_environments.append(environment)
        return original_run(*args, **kwargs)

    monkeypatch.setattr(close_pack.subprocess, "run", observe_git)
    assert _run(repo, monkeypatch, "--source", SOURCE_REL, "--write") == 0
    assert git_environments
    assert all(
        environment.get("GIT_NO_LAZY_FETCH") == "1"
        for environment in git_environments
    )
    assert all(
        environment.get("GIT_NO_REPLACE_OBJECTS") == "1"
        for environment in git_environments
    )
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
