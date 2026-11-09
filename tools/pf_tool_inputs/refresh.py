#!/usr/bin/env python3
"""Refresh or check the repository's PF tool inputs (HDE-CRD-0003 S17, IF-1d).

``--source <path>`` rewrites ``tools/pf_tool_inputs/manifest.json`` and the
vendored copies under ``tools/pf_tool_inputs/documents/`` from HEAD of a clean
local checkout of ``amthorn78/glow-docs``, reading git objects only, then runs
the check. It refuses a checkout that is not a git work tree's top level, is
dirty (untracked files included), has an ``origin`` other than a GitHub URL of
``amthorn78/glow-docs``, or whose HEAD the local ``origin/main`` does not
contain. It opens no network connection and never edits a reader or its pin.

``--check`` needs no second checkout. It verifies that the manifest is valid and
canonical, that the vendored set is exactly VENDORED_IDS, that each copy's
size, SHA-256 and git blob ID equal its manifest entry, and that every digest
pin a reader holds (READER_PINS) equals the manifest digest it names. A PF18
change upstream therefore fails the check until the narrative catalog is
revalidated and the pin moved by its owner.

The copies are tool input. They confer no PF authority and are not a governed
evidence family; planning resolves PF documents from amthorn78/glow-docs.
"""

from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import argparse  # noqa: E402
import ast  # noqa: E402
import hashlib  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import re  # noqa: E402
import stat  # noqa: E402
import subprocess  # noqa: E402
import tempfile  # noqa: E402
from collections.abc import Iterable, Sequence  # noqa: E402
from pathlib import Path  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.serializer.canon import sercanon  # noqa: E402
from tools.pf_tool_inputs import resolver  # noqa: E402
from tools.pf_tool_inputs.resolver import PfToolInputError  # noqa: E402

# The documents a reader reads by content (HDE-CRD-0003 WU-PR-01 plan, PD-2): the QA
# harness (PF04), the pre-push build-notes report (PF10), the narrative generator (PF18),
# the close-pack writer's deferral registers (PF09.1 to PF09.7, PF30.1), and the floor
# the approved Plan names (PF14, PF19, PF27).
VENDORED_IDS = frozenset(
    {
        "PF04",
        "PF09.1",
        "PF09.2",
        "PF09.3",
        "PF09.4",
        "PF09.5",
        "PF09.6",
        "PF09.7",
        "PF10",
        "PF14",
        "PF18",
        "PF19",
        "PF27",
        "PF30.1",
    }
)
# (reader path, module-level constant, PF ID): each pin must equal that ID's manifest digest.
READER_PINS = (
    ("tools/evidence/generate_narrative_registry_diff.py", "PF18_SOURCE_SHA256", "PF18"),
)

SOURCE_NOT_A_CHECKOUT = "PF_TOOL_INPUTS_SOURCE_NOT_A_CHECKOUT"
SOURCE_DIRTY = "PF_TOOL_INPUTS_SOURCE_DIRTY"
SOURCE_NOT_GLOW_DOCS = "PF_TOOL_INPUTS_SOURCE_NOT_GLOW_DOCS"
SOURCE_NOT_ON_MAIN = "PF_TOOL_INPUTS_SOURCE_NOT_ON_MAIN"
SOURCE_UNSUPPORTED_ENTRY = "PF_TOOL_INPUTS_SOURCE_UNSUPPORTED_ENTRY"
SOURCE_DUPLICATE_ID = "PF_TOOL_INPUTS_SOURCE_DUPLICATE_ID"
SOURCE_INCOMPLETE = "PF_TOOL_INPUTS_SOURCE_INCOMPLETE"

MANIFEST_NOT_CANONICAL = "PF_TOOL_INPUTS_MANIFEST_NOT_CANONICAL"
VENDORED_SET_MISMATCH = "PF_TOOL_INPUTS_VENDORED_SET_MISMATCH"
DOCUMENT_UNEXPECTED = "PF_TOOL_INPUTS_DOCUMENT_UNEXPECTED"
PIN_MISSING = "PF_TOOL_INPUTS_PIN_MISSING"
PIN_MISMATCH = "PF_TOOL_INPUTS_PIN_MISMATCH"

_ORIGIN_RE = re.compile(
    r"(?:https://(?:[^@/\s]+@)?github\.com/|git@github\.com:|ssh://git@github\.com/)"
    r"amthorn78/glow-docs(?:\.git)?/?\Z"
)
_HEX64 = re.compile(r"[0-9a-f]{64}\Z")
_SOURCE_DIRECTORY = resolver.SOURCE_PATH


def git_blob_id(data: bytes) -> str:
    """The git object ID of a blob holding these bytes."""

    return hashlib.sha1(b"blob %d\x00" % len(data) + data).hexdigest()  # noqa: S324 - git object ID


def _git(source: Path, *args: str) -> subprocess.CompletedProcess[bytes]:
    env = {**os.environ, "LC_ALL": "C", "GIT_TERMINAL_PROMPT": "0", "GIT_OPTIONAL_LOCKS": "0"}
    return subprocess.run(
        ["git", "-C", str(source), *args], env=env, capture_output=True, check=False
    )


def _git_text(source: Path, *args: str, code: str) -> str:
    result = _git(source, *args)
    if result.returncode != 0:
        raise PfToolInputError(code)
    return result.stdout.decode("utf-8").strip()


def _verify_source(source: Path) -> str:
    """Refuse an unusable source checkout; return its HEAD commit."""

    if not source.is_dir():
        raise PfToolInputError(SOURCE_NOT_A_CHECKOUT)
    top = _git_text(source, "rev-parse", "--show-toplevel", code=SOURCE_NOT_A_CHECKOUT)
    if Path(top).resolve() != source.resolve():
        raise PfToolInputError(SOURCE_NOT_A_CHECKOUT)
    status = _git(source, "status", "--porcelain", "--untracked-files=all")
    if status.returncode != 0:
        raise PfToolInputError(SOURCE_NOT_A_CHECKOUT)
    if status.stdout.strip():
        raise PfToolInputError(SOURCE_DIRTY)
    origin = _git(source, "remote", "get-url", "origin")
    if origin.returncode != 0 or not _ORIGIN_RE.fullmatch(origin.stdout.decode("utf-8").strip()):
        raise PfToolInputError(SOURCE_NOT_GLOW_DOCS)
    head = _git_text(source, "rev-parse", "--verify", "HEAD^{commit}", code=SOURCE_NOT_A_CHECKOUT)
    _git_text(source, "rev-parse", "--verify", "refs/remotes/origin/main^{commit}", code=SOURCE_NOT_ON_MAIN)
    if _git(source, "merge-base", "--is-ancestor", head, "refs/remotes/origin/main").returncode != 0:
        raise PfToolInputError(SOURCE_NOT_ON_MAIN)
    return head


def _source_documents(source: Path, head: str) -> list[tuple[str, bytes, str]]:
    """Every PF Markdown file directly under docs/hde/pfcanon/ at HEAD: (name, bytes, blob ID)."""

    listing = _git(source, "ls-tree", "-z", head, "--", _SOURCE_DIRECTORY)
    if listing.returncode != 0:
        raise PfToolInputError(SOURCE_NOT_A_CHECKOUT)
    documents: list[tuple[str, bytes, str]] = []
    for record in listing.stdout.split(b"\x00"):
        if not record:
            continue
        meta, _, raw_path = record.partition(b"\t")
        mode, kind, object_id = meta.decode("ascii").split(" ")
        name = raw_path.decode("utf-8").removeprefix(_SOURCE_DIRECTORY)
        if not (name.startswith("PF") and name.endswith(".md")):
            continue
        if kind != "blob" or mode not in {"100644", "100755"} or resolver.title_from_file_name(name) is None:
            raise PfToolInputError(SOURCE_UNSUPPORTED_ENTRY)
        blob = _git(source, "cat-file", "blob", object_id)
        if blob.returncode != 0 or git_blob_id(blob.stdout) != object_id:
            raise PfToolInputError(SOURCE_NOT_A_CHECKOUT)
        documents.append((name, blob.stdout, object_id))
    return documents


def _write_atomic(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(data)
        os.chmod(temporary, 0o644)
        os.replace(temporary, path)
    except BaseException:
        Path(temporary).unlink(missing_ok=True)
        raise


def write_input_set(
    target_root: Path,
    source_commit: str,
    documents: Iterable[tuple[str, bytes, str]],
    vendored_ids: Iterable[str] = VENDORED_IDS,
) -> bytes:
    """Write a manifest and vendored copies from (file name, bytes, blob ID) triples.

    Returns the manifest bytes. Copies no longer vendored are removed; nothing
    outside the manifest and the documents directory is written.
    """

    vendored = frozenset(vendored_ids)
    entries: list[dict[str, object]] = []
    copies: dict[str, bytes] = {}
    seen_ids: set[str] = set()
    for name, data, object_id in sorted(documents, key=lambda item: item[0]):
        pf_id = resolver.pf_id_from_file_name(name)
        title = resolver.title_from_file_name(name)
        if title is None:
            raise PfToolInputError(SOURCE_UNSUPPORTED_ENTRY)
        if pf_id is not None:
            if pf_id in seen_ids:
                raise PfToolInputError(SOURCE_DUPLICATE_ID)
            seen_ids.add(pf_id)
        is_vendored = pf_id is not None and pf_id in vendored
        entries.append(
            {
                "file_name": name,
                "pf_id": pf_id,
                "sha256": hashlib.sha256(data).hexdigest(),
                "size_bytes": len(data),
                "source_blob": object_id,
                "title": title,
                "vendored": is_vendored,
            }
        )
        if is_vendored:
            copies[pf_id] = data
    if set(copies) != vendored:
        raise PfToolInputError(SOURCE_INCOMPLETE)
    manifest = sercanon(
        {
            "documents": entries,
            "schema_version": resolver.SCHEMA_VERSION,
            "source_commit": source_commit,
            "source_path": resolver.SOURCE_PATH,
            "source_repository": resolver.SOURCE_REPOSITORY,
        }
    )
    resolver.parse_manifest(manifest)
    target_root = Path(target_root)
    documents_dir = target_root / resolver.DOCUMENTS_REL
    documents_dir.mkdir(parents=True, exist_ok=True)
    for pf_id, data in sorted(copies.items()):
        _write_atomic(target_root / resolver.copy_rel(pf_id), data)
    wanted = {f"{pf_id}.md" for pf_id in copies}
    for child in sorted(documents_dir.iterdir()):
        if child.name.endswith(".md") and child.name not in wanted and not child.is_symlink() and child.is_file():
            child.unlink()
    _write_atomic(target_root / resolver.MANIFEST_REL, manifest)
    return manifest


def refresh(source: Path, target_root: Path = ROOT) -> str:
    """Rewrite the input set under target_root from HEAD of a glow-docs checkout; return HEAD."""

    source = Path(source).resolve()
    head = _verify_source(source)
    write_input_set(target_root, head, _source_documents(source, head))
    return head


def _reader_pin(path: Path, constant: str) -> str | None:
    """The one module-level string assignment of a 64-hex digest to ``constant``, or None."""

    try:
        tree = ast.parse(path.read_bytes())
    except (OSError, SyntaxError, ValueError):
        return None
    values: list[object] = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            targets, value = node.targets, node.value
        elif isinstance(node, ast.AnnAssign) and node.value is not None:
            targets, value = [node.target], node.value
        else:
            continue
        if any(isinstance(target, ast.Name) and target.id == constant for target in targets):
            values.append(value.value if isinstance(value, ast.Constant) else None)
    if len(values) != 1 or not isinstance(values[0], str) or not _HEX64.fullmatch(values[0]):
        return None
    return values[0]


def check(root: Path = ROOT) -> list[tuple[str, str]]:
    """Every failure as (code, repository-relative path or ""); empty when the set is sound."""

    root = Path(root)
    try:
        data = resolver.manifest_bytes(root)
        entries = resolver.parse_manifest(data)
    except PfToolInputError as exc:
        return [(exc.code, resolver.MANIFEST_REL)]
    failures: list[tuple[str, str]] = []
    if sercanon(json.loads(data.decode("utf-8"))) != data:
        failures.append((MANIFEST_NOT_CANONICAL, resolver.MANIFEST_REL))
    by_id = {entry.pf_id: entry for entry in entries if entry.pf_id is not None}
    vendored = {entry.pf_id for entry in entries if entry.vendored}
    if vendored != VENDORED_IDS:
        failures.append((VENDORED_SET_MISMATCH, resolver.MANIFEST_REL))
    documents_dir = root / resolver.DOCUMENTS_REL
    present = {child.name for child in documents_dir.iterdir()} if documents_dir.is_dir() else set()
    for name in sorted(present - {f"{pf_id}.md" for pf_id in vendored}):
        failures.append((DOCUMENT_UNEXPECTED, f"{resolver.DOCUMENTS_REL}/{name}"))
    for pf_id in sorted(vendored):
        rel = resolver.copy_rel(pf_id)
        path = root / rel
        try:
            regular = stat.S_ISREG(os.lstat(path).st_mode)
        except FileNotFoundError:
            regular = False
        if not regular:
            failures.append((resolver.DOCUMENT_MISSING, rel))
            continue
        copy = path.read_bytes()
        entry = by_id[pf_id]
        if (
            len(copy) != entry.size_bytes
            or hashlib.sha256(copy).hexdigest() != entry.sha256
            or git_blob_id(copy) != entry.source_blob
        ):
            failures.append((resolver.DOCUMENT_MISMATCH, rel))
    for rel, constant, pf_id in READER_PINS:
        pin = _reader_pin(root / rel, constant)
        if pin is None:
            failures.append((PIN_MISSING, rel))
        elif pf_id not in by_id or pin != by_id[pf_id].sha256:
            failures.append((PIN_MISMATCH, rel))
    return failures


def _report(failures: Sequence[tuple[str, str]]) -> int:
    if not failures:
        print("PF_TOOL_INPUTS_CHECK_OK")
        return 0
    for code, rel in failures:
        print(f"PF_TOOL_INPUTS_CHECK_FAILED:{code}" + (f":{rel}" if rel else ""), file=sys.stderr)
    return 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="python tools/pf_tool_inputs/refresh.py",
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--source", type=Path, help="a clean local checkout of amthorn78/glow-docs")
    mode.add_argument("--check", action="store_true", help="verify the input set; reads no second checkout")
    args = parser.parse_args(argv)
    if args.source is not None:
        try:
            head = refresh(args.source, ROOT)
        except PfToolInputError as exc:
            print(f"PF_TOOL_INPUTS_REFRESH_REFUSED:{exc.code}", file=sys.stderr)
            return 1
        print(f"PF_TOOL_INPUTS_REFRESH_OK source_commit={head}")
    return _report(check(ROOT))


if __name__ == "__main__":
    raise SystemExit(main())
