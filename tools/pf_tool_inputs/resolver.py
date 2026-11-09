"""Resolve the repository's PF tool inputs (HDE-CRD-0003 S17, IF-1c).

Tools and tests that read a PF document at run time read it from the tracked,
digest-pinned tool-input set in this directory: ``manifest.json`` names every PF
Markdown file of ``docs/hde/pfcanon/`` in ``amthorn78/glow-docs`` at one commit,
and ``documents/<pf_id>.md`` holds a byte-identical copy of each document a
reader reads by content. ``tools/pf_tool_inputs/refresh.py`` writes and checks
the set. The copies are tool input: they confer no PF authority, they are not a
governed evidence family, and no reader fetches a PF document over the network.

Standard library only: the AGENTS.md citation check imports this module before
CI installs any dependency.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import stat
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INPUT_SET_REL = "tools/pf_tool_inputs"
MANIFEST_REL = f"{INPUT_SET_REL}/manifest.json"
DOCUMENTS_REL = f"{INPUT_SET_REL}/documents"
SCHEMA_VERSION = "pf_tool_inputs.v1"
SOURCE_REPOSITORY = "amthorn78/glow-docs"
SOURCE_PATH = "docs/hde/pfcanon/"

MANIFEST_KEYS = frozenset(
    {"documents", "schema_version", "source_commit", "source_path", "source_repository"}
)
DOCUMENT_KEYS = frozenset(
    {"file_name", "pf_id", "sha256", "size_bytes", "source_blob", "title", "vendored"}
)

# Refusal codes. Each refusal's message is its code alone: no digit, path or ID.
MANIFEST_MISSING = "PF_TOOL_INPUTS_MANIFEST_MISSING"
MANIFEST_INVALID = "PF_TOOL_INPUTS_MANIFEST_INVALID"
DOCUMENT_UNKNOWN = "PF_TOOL_INPUTS_DOCUMENT_UNKNOWN"
DOCUMENT_NOT_VENDORED = "PF_TOOL_INPUTS_DOCUMENT_NOT_VENDORED"
DOCUMENT_MISSING = "PF_TOOL_INPUTS_DOCUMENT_MISSING"
DOCUMENT_MISMATCH = "PF_TOOL_INPUTS_DOCUMENT_MISMATCH"

_PF_ID_RE = re.compile(r"PF[0-9]{2}(?:\.[0-9]+)?\Z")
_PF_ID_PREFIX_RE = re.compile(r"PF(?P<number>[0-9]{2}(?:\.[0-9]+)?)(?![0-9.]*[0-9])")
# A PF file's title: its name after the optional PF number and the optional Canon or
# Reference kind, and before the optional version, the parts separated by hyphens,
# spaces or both. The same rule as the close-pack writer's PF_DOCUMENT_RE.
_TITLE_RE = re.compile(
    r"PF(?:[0-9]{2}(?:\.[0-9]+)?)?[- ]+(?:(?:Canon|Reference)[- ]+)?"
    r"(?P<name>[A-Za-z0-9&'](?:[A-Za-z0-9&' -]*?[A-Za-z0-9&'])?)"
    r"(?:[- ]?v[0-9]+(?:\.[0-9]+)*)?\.md\Z"
)
_FILE_NAME_RE = re.compile(r"PF[^/\\\x00]*\.md\Z")
_HEX40 = re.compile(r"[0-9a-f]{40}\Z")
_HEX64 = re.compile(r"[0-9a-f]{64}\Z")


class PfToolInputError(RuntimeError):
    """A typed, numeric-free refusal to resolve a PF tool input."""

    def __init__(self, code: str) -> None:
        super().__init__(code)
        self.code = code


@dataclass(frozen=True)
class PfDocument:
    file_name: str
    pf_id: str | None
    title: str
    source_blob: str
    sha256: str
    size_bytes: int
    vendored: bool


def pf_id_from_file_name(file_name: str) -> str | None:
    """The PF number a file name starts with, as ``PF04`` or ``PF09.3``, or None."""

    match = _PF_ID_PREFIX_RE.match(file_name)
    return f"PF{match['number']}" if match else None


def title_from_file_name(file_name: str) -> str | None:
    """A PF file's versionless title, hyphens read as spaces, or None if it has none."""

    match = _TITLE_RE.fullmatch(file_name)
    return " ".join(match["name"].replace("-", " ").split()) if match else None


def copy_rel(pf_id: str) -> str:
    """The repository-relative path of the vendored copy of one PF document."""

    return f"{DOCUMENTS_REL}/{pf_id}.md"


def _reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise PfToolInputError(MANIFEST_INVALID)
        result[key] = value
    return result


def _read_regular(path: Path, missing_code: str) -> bytes:
    try:
        mode = os.lstat(path).st_mode
    except FileNotFoundError:
        raise PfToolInputError(missing_code) from None
    if not stat.S_ISREG(mode):
        raise PfToolInputError(missing_code)
    return path.read_bytes()


def manifest_bytes(root: Path = ROOT) -> bytes:
    """The manifest's bytes, refusing an absent manifest or one that is not a regular file."""

    path = Path(root) / MANIFEST_REL
    try:
        mode = os.lstat(path).st_mode
    except FileNotFoundError:
        raise PfToolInputError(MANIFEST_MISSING) from None
    if not stat.S_ISREG(mode):
        raise PfToolInputError(MANIFEST_INVALID)
    return path.read_bytes()


def _entry(raw: object) -> PfDocument:
    if not isinstance(raw, dict) or set(raw) != DOCUMENT_KEYS:
        raise PfToolInputError(MANIFEST_INVALID)
    file_name = raw["file_name"]
    if not isinstance(file_name, str) or not _FILE_NAME_RE.fullmatch(file_name):
        raise PfToolInputError(MANIFEST_INVALID)
    title = title_from_file_name(file_name)
    size = raw["size_bytes"]
    if (
        title is None
        or raw["title"] != title
        or raw["pf_id"] != pf_id_from_file_name(file_name)
        or not isinstance(raw["source_blob"], str)
        or not _HEX40.fullmatch(raw["source_blob"])
        or not isinstance(raw["sha256"], str)
        or not _HEX64.fullmatch(raw["sha256"])
        or not isinstance(size, int)
        or isinstance(size, bool)
        or size < 0
        or not isinstance(raw["vendored"], bool)
        or (raw["vendored"] and raw["pf_id"] is None)
    ):
        raise PfToolInputError(MANIFEST_INVALID)
    return PfDocument(
        file_name=file_name,
        pf_id=raw["pf_id"],
        title=title,
        source_blob=raw["source_blob"],
        sha256=raw["sha256"],
        size_bytes=size,
        vendored=raw["vendored"],
    )


def parse_manifest(data: bytes) -> tuple[PfDocument, ...]:
    """Validate manifest bytes and return their entries in manifest order.

    Structure, types, sort order, uniqueness and the title and PF-ID rules are
    checked here; canonical bytes are checked by ``refresh.py --check``.
    """

    try:
        payload = json.loads(data.decode("utf-8"), object_pairs_hook=_reject_duplicate_keys)
    except (UnicodeDecodeError, ValueError):
        raise PfToolInputError(MANIFEST_INVALID) from None
    if (
        not isinstance(payload, dict)
        or set(payload) != MANIFEST_KEYS
        or payload["schema_version"] != SCHEMA_VERSION
        or payload["source_repository"] != SOURCE_REPOSITORY
        or payload["source_path"] != SOURCE_PATH
        or not isinstance(payload["source_commit"], str)
        or not _HEX40.fullmatch(payload["source_commit"])
        or not isinstance(payload["documents"], list)
        or not payload["documents"]
    ):
        raise PfToolInputError(MANIFEST_INVALID)
    entries = tuple(_entry(raw) for raw in payload["documents"])
    names = [entry.file_name for entry in entries]
    ids = [entry.pf_id for entry in entries if entry.pf_id is not None]
    if any(left >= right for left, right in zip(names, names[1:])) or len(ids) != len(set(ids)):
        raise PfToolInputError(MANIFEST_INVALID)
    return entries


def source_commit(root: Path = ROOT) -> str:
    """The glow-docs commit the input set was refreshed from."""

    data = manifest_bytes(root)
    parse_manifest(data)
    return json.loads(data.decode("utf-8"))["source_commit"]


def pf_entries(root: Path = ROOT) -> tuple[PfDocument, ...]:
    """Every manifest entry, validated, in manifest (file-name) order."""

    return parse_manifest(manifest_bytes(root))


def pf_entry(pf_id: str, root: Path = ROOT) -> PfDocument:
    """The one manifest entry for a PF ID."""

    if not isinstance(pf_id, str) or not _PF_ID_RE.fullmatch(pf_id):
        raise PfToolInputError(DOCUMENT_UNKNOWN)
    for entry in pf_entries(root):
        if entry.pf_id == pf_id:
            return entry
    raise PfToolInputError(DOCUMENT_UNKNOWN)


def pf_document(pf_id: str, *, root: Path = ROOT) -> Path:
    """The one vendored copy for a PF ID, after checking its size and SHA-256."""

    root = Path(root)
    entry = pf_entry(pf_id, root)
    if not entry.vendored:
        raise PfToolInputError(DOCUMENT_NOT_VENDORED)
    path = root / copy_rel(pf_id)
    data = _read_regular(path, DOCUMENT_MISSING)
    if len(data) != entry.size_bytes or hashlib.sha256(data).hexdigest() != entry.sha256:
        raise PfToolInputError(DOCUMENT_MISMATCH)
    return path


def pf_titles(*, root: Path = ROOT) -> tuple[str, ...]:
    """Every manifest title, in manifest order. Reads only the manifest."""

    return tuple(entry.title for entry in pf_entries(root))


def pf_file_names(*, root: Path = ROOT) -> tuple[str, ...]:
    """Every manifest file name, in manifest order. Reads only the manifest."""

    return tuple(entry.file_name for entry in pf_entries(root))
