"""Owner tests of the PF tool inputs, their resolver and their refresh-and-check tool (HDE-CRD-0003 S17)."""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from tools.pf_tool_inputs import refresh, resolver
from tools.pf_tool_inputs.resolver import PfToolInputError
from tools.qa import qa_harness

ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / "tools" / "pf_tool_inputs" / "refresh.py"
NARRATIVE_READER = "tools/evidence/generate_narrative_registry_diff.py"
CLOSED_RAILS = {
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
    "APP_ENV": "dev",
    "PYTHONDONTWRITEBYTECODE": "1",
}
_VERSION_SUFFIX = re.compile(r"[- ]?v[0-9]+(?:\.[0-9]+)*\Z")


def _run_tool(*args: str) -> subprocess.CompletedProcess[str]:
    env = {key: value for key, value in os.environ.items() if key not in {"DATABASE_URL", "HD_API_KEY", "HDAPI_BASE_URL"}}
    env.update(CLOSED_RAILS)
    return subprocess.run(
        [sys.executable, str(TOOL), *args], cwd=ROOT, env=env, capture_output=True, text=True, check=False
    )


def _copy_input_set(target: Path) -> Path:
    """The repository's input set and the narrative reader, copied under target."""
    shutil.copytree(ROOT / resolver.INPUT_SET_REL, target / resolver.INPUT_SET_REL)
    reader = target / NARRATIVE_READER
    reader.parent.mkdir(parents=True)
    shutil.copyfile(ROOT / NARRATIVE_READER, reader)
    return target


def _git(repo: Path, *args: str) -> str:
    return subprocess.run(
        ["git", "-c", "user.name=fixture", "-c", "user.email=fixture@invalid", "-C", str(repo), *args],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.strip()


def _glow_docs_checkout(path: Path, origin: str = "https://github.com/amthorn78/glow-docs") -> Path:
    """A local glow-docs-shaped checkout: the vendored copies' bytes, placeholders for the rest."""
    directory = path / resolver.SOURCE_PATH
    directory.mkdir(parents=True)
    for entry in resolver.pf_entries():
        data = (
            resolver.pf_document(entry.pf_id).read_bytes()
            if entry.vendored and entry.pf_id is not None
            else f"placeholder for {entry.file_name}\n".encode()
        )
        (directory / entry.file_name).write_bytes(data)
    (directory / "README.md").write_text("Not a PF document.\n", encoding="utf-8")
    _git(path, "init", "--quiet", "--initial-branch=main")
    _git(path, "add", "-A")
    _git(path, "commit", "--quiet", "-m", "fixture canon")
    _git(path, "remote", "add", "origin", origin)
    _git(path, "update-ref", "refs/remotes/origin/main", "HEAD")
    return path


# --------------------------------------------------------------------------
# --check on the repository and on changed copies of it (acceptance 7)
# --------------------------------------------------------------------------


def test_check_passes_on_the_repository() -> None:
    result = _run_tool("--check")
    assert result.returncode == 0, result.stdout + result.stderr
    assert result.stdout == "PF_TOOL_INPUTS_CHECK_OK\n"
    assert refresh.check(ROOT) == []


def test_a_changed_vendored_byte_fails_the_check(tmp_path: Path) -> None:
    root = _copy_input_set(tmp_path)
    copy = root / resolver.copy_rel("PF04")
    data = bytearray(copy.read_bytes())
    data[100] ^= 0x01
    copy.write_bytes(bytes(data))
    assert refresh.check(root) == [(resolver.DOCUMENT_MISMATCH, resolver.copy_rel("PF04"))]


def test_a_mismatched_reader_pin_fails_the_check(tmp_path: Path) -> None:
    root = _copy_input_set(tmp_path)
    reader = root / NARRATIVE_READER
    pin = resolver.pf_entry("PF18").sha256
    text = reader.read_text(encoding="utf-8")
    assert text.count(pin) == 1
    reader.write_text(text.replace(pin, "0" * 64), encoding="utf-8")
    assert refresh.check(root) == [(refresh.PIN_MISMATCH, NARRATIVE_READER)]


def test_a_non_canonical_manifest_fails_the_check(tmp_path: Path) -> None:
    root = _copy_input_set(tmp_path)
    manifest = root / resolver.MANIFEST_REL
    manifest.write_text(json.dumps(json.loads(manifest.read_bytes()), indent=1, sort_keys=True) + "\n", encoding="utf-8")
    assert refresh.check(root) == [(refresh.MANIFEST_NOT_CANONICAL, resolver.MANIFEST_REL)]


def test_an_extra_or_missing_copy_fails_the_check(tmp_path: Path) -> None:
    root = _copy_input_set(tmp_path)
    (root / resolver.copy_rel("PF12")).write_text("not vendored\n", encoding="utf-8")
    (root / resolver.copy_rel("PF10")).unlink()
    assert refresh.check(root) == [
        (refresh.DOCUMENT_UNEXPECTED, resolver.copy_rel("PF12")),
        (resolver.DOCUMENT_MISSING, resolver.copy_rel("PF10")),
    ]


def test_the_vendored_set_is_exact() -> None:
    entries = resolver.pf_entries()
    assert {entry.pf_id for entry in entries if entry.vendored} == refresh.VENDORED_IDS
    assert sorted(path.name for path in (ROOT / resolver.DOCUMENTS_REL).iterdir()) == sorted(
        f"{pf_id}.md" for pf_id in refresh.VENDORED_IDS
    )


# --------------------------------------------------------------------------
# the resolver
# --------------------------------------------------------------------------


def test_pf_document_returns_the_digest_named_copy() -> None:
    path = resolver.pf_document("PF04")
    assert path == ROOT / resolver.copy_rel("PF04")
    entry = resolver.pf_entry("PF04")
    assert refresh.git_blob_id(path.read_bytes()) == entry.source_blob
    assert entry.title == "HDE Governance" and entry.vendored


@pytest.mark.parametrize(
    ("pf_id", "code"),
    (
        ("PF99", resolver.DOCUMENT_UNKNOWN),
        ("PF04-Canon-HDE-Governance", resolver.DOCUMENT_UNKNOWN),
        ("PF12", resolver.DOCUMENT_NOT_VENDORED),
    ),
)
def test_pf_document_refusals_are_typed_and_numeric_free(pf_id: str, code: str) -> None:
    with pytest.raises(PfToolInputError) as raised:
        resolver.pf_document(pf_id)
    assert raised.value.code == code
    assert str(raised.value) == code and not re.search(r"[0-9]", str(raised.value))


def test_a_changed_or_absent_copy_is_refused(tmp_path: Path) -> None:
    root = _copy_input_set(tmp_path)
    copy = root / resolver.copy_rel("PF18")
    copy.write_bytes(copy.read_bytes() + b"\n")
    with pytest.raises(PfToolInputError, match=resolver.DOCUMENT_MISMATCH):
        resolver.pf_document("PF18", root=root)
    copy.unlink()
    with pytest.raises(PfToolInputError, match=resolver.DOCUMENT_MISSING):
        resolver.pf_document("PF18", root=root)
    (root / resolver.MANIFEST_REL).unlink()
    with pytest.raises(PfToolInputError, match=resolver.MANIFEST_MISSING):
        resolver.pf_titles(root=root)


def test_titles_and_names_come_from_the_manifest() -> None:
    entries = resolver.pf_entries()
    assert resolver.pf_titles() == tuple(entry.title for entry in entries)
    assert resolver.pf_file_names() == tuple(entry.file_name for entry in entries)
    assert all(entry.file_name.startswith("PF") and entry.file_name.endswith(".md") for entry in entries)
    assert len(set(resolver.pf_titles())) == len(entries)


def test_the_qa_harness_pf_refs_name_manifest_documents() -> None:
    # The PF27 v2 pf_refs the QA harness cites are in-document titles: the versionless stem of
    # exactly one manifest file name (HDE-CRD-0003 WU-PR-01 plan, PD-7).
    stems = [_VERSION_SUFFIX.sub("", name.removesuffix(".md")) for name in resolver.pf_file_names()]
    for reference in (*qa_harness.PYTEST_CHECK_PF_REFS, *qa_harness.VIABILITY_PF_REFS):
        assert stems.count(reference) == 1, reference


# --------------------------------------------------------------------------
# --source refresh from a local glow-docs checkout
# --------------------------------------------------------------------------


def test_refresh_reproduces_the_vendored_inputs(tmp_path: Path) -> None:
    source = _glow_docs_checkout(tmp_path / "glow-docs")
    target = _copy_input_set(tmp_path / "target")
    head = refresh.refresh(source, target)
    assert head == _git(source, "rev-parse", "HEAD")
    assert resolver.source_commit(target) == head
    produced = {entry.file_name: entry for entry in resolver.pf_entries(target)}
    for entry in resolver.pf_entries():
        assert produced[entry.file_name].title == entry.title
        assert produced[entry.file_name].vendored == entry.vendored
        if entry.vendored:
            assert produced[entry.file_name] == entry
            assert (target / resolver.copy_rel(entry.pf_id)).read_bytes() == (ROOT / resolver.copy_rel(entry.pf_id)).read_bytes()
    assert refresh.check(target) == []


def test_refresh_refuses_an_unusable_source(tmp_path: Path) -> None:
    with pytest.raises(PfToolInputError, match=refresh.SOURCE_NOT_A_CHECKOUT):
        refresh.refresh(tmp_path, tmp_path / "target")
    dirty = _glow_docs_checkout(tmp_path / "dirty")
    (dirty / "untracked.txt").write_text("x\n", encoding="utf-8")
    with pytest.raises(PfToolInputError, match=refresh.SOURCE_DIRTY):
        refresh.refresh(dirty, tmp_path / "target")
    other = _glow_docs_checkout(tmp_path / "other", origin="https://example.invalid/amthorn78/glow-docs.git")
    with pytest.raises(PfToolInputError, match=refresh.SOURCE_NOT_GLOW_DOCS):
        refresh.refresh(other, tmp_path / "target")
    ahead = _glow_docs_checkout(tmp_path / "ahead")
    _git(ahead, "commit", "--quiet", "--allow-empty", "-m", "not on main")
    with pytest.raises(PfToolInputError, match=refresh.SOURCE_NOT_ON_MAIN):
        refresh.refresh(ahead, tmp_path / "target")
    assert not (tmp_path / "target").exists()


@pytest.mark.parametrize(
    ("origin", "accepted"),
    (
        ("https://github.com/amthorn78/glow-docs", True),
        ("https://github.com/amthorn78/glow-docs.git", True),
        ("https://x-access-token@github.com/amthorn78/glow-docs/", True),
        ("git@github.com:amthorn78/glow-docs.git", True),
        ("ssh://git@github.com/amthorn78/glow-docs", True),
        ("https://github.com/amthorn78/glow-hdengine-v2", False),
        ("https://github.com/someone/glow-docs", False),
        ("file:///srv/glow-docs", False),
    ),
)
def test_origin_forms(origin: str, accepted: bool) -> None:
    assert bool(refresh._ORIGIN_RE.fullmatch(origin)) is accepted


def test_help_exits_zero_and_writes_nothing() -> None:
    before = (ROOT / resolver.MANIFEST_REL).read_bytes()
    result = _run_tool("--help")
    assert result.returncode == 0 and result.stdout.startswith("usage:")
    assert (ROOT / resolver.MANIFEST_REL).read_bytes() == before
