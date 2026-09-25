#!/usr/bin/env python3
"""Perform the one intentional Git input change for a release cut."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import sys
from pathlib import Path
from typing import Callable, Sequence

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.config import registry_loader as _admission
from engine.serializer import canon

_VERSION = re.compile(
    r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)"
    r"(?:-(?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*)"
    r"(?:\.(?:0|[1-9][0-9]*|[0-9]*[A-Za-z-][0-9A-Za-z-]*))*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$"
)
_BUILT_AT = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$")
_TOP_LEVEL_KEYS = {"root", "version", "built_at_utc", "files"}
_ENTRY_KEYS = {"path", "sha256", "size"}
_REQUIRED_RAILS = {
    "ALLOW_NETWORK": "0",
    "LANG": "C",
    "LC_ALL": "C",
    "SAFE_MODE": "1",
    "TZ": "UTC",
}


def _require_closed_rails() -> None:
    missing = {
        name: expected
        for name, expected in _REQUIRED_RAILS.items()
        if os.environ.get(name) != expected
    }
    if missing:
        raise ValueError("release_cut_requires_closed_rails")


def _validate_inputs(version: str, built_at_utc: str) -> None:
    if _VERSION.fullmatch(version) is None:
        raise ValueError("release_version_invalid")
    if _BUILT_AT.fullmatch(built_at_utc) is None:
        raise ValueError("release_built_at_invalid")
    try:
        dt.datetime.fromisoformat(built_at_utc.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("release_built_at_invalid") from exc


def _path_unsafe(name: str, manifest_rel: str) -> bool:
    """Lexical member-path rule, shared by existing rows and roster-derived rows."""
    rel = Path(name)
    return (
        not name
        or rel.is_absolute()
        or "\\" in name
        or ".." in rel.parts
        or rel.as_posix() != name
        or name == manifest_rel
    )


def _validate_roster(roster: Sequence[str], manifest_rel: str) -> tuple[str, ...]:
    """Accept only a non-empty, duplicate-free, ASCII-sorted roster of safe paths."""
    members = tuple(roster)
    if (
        not members
        or any(not isinstance(name, str) or not name.isascii() for name in members)
        or len(set(members)) != len(members)
        or list(members) != sorted(members)
        or any(_path_unsafe(name, manifest_rel) for name in members)
    ):
        raise ValueError("release_manifest_roster_invalid")
    return members


def cut_manifest(
    manifest_path: Path,
    *,
    version: str,
    built_at_utc: str,
    check: bool = False,
    roster: Sequence[str] | None = None,
    _publish: Callable[[Path, bytes], None] | None = None,
) -> int:
    """Render or verify one canonical manifest without derived evidence writes.

    Without ``roster`` every existing row is refreshed from disk.  With a
    roster the membership is constructed as exactly that roster: every roster
    path receives one row (an existing row refreshed, an absent row added) and
    an existing row outside the roster is refused as a non-input extra.  In
    both modes each member's owning format is validated with the admission
    owner's member rule before its hash and size are taken over the exact
    bytes on disk; the cutter never normalizes or rewrites a member.

    A coordinating owner may supply a private final-byte publisher to include
    this cut in its existing transaction. The cutter still validates every
    input and constructs all bytes; check mode never calls the publisher.
    """

    _require_closed_rails()
    _validate_inputs(version, built_at_utc)
    original = manifest_path.read_bytes()
    payload = json.loads(original.decode("utf-8"))
    if not isinstance(payload, dict) or set(payload) != _TOP_LEVEL_KEYS:
        raise ValueError("release_manifest_shape_invalid")
    if original != canon.sercanon(payload, sort_keys=True):
        raise ValueError("release_manifest_not_canonical")
    if payload.get("root") != "catalog/":
        raise ValueError("release_manifest_root_invalid")
    payload["version"] = version
    payload["built_at_utc"] = built_at_utc
    entries = payload.get("files")
    if not isinstance(entries, list) or not entries:
        raise ValueError("release_manifest_files_invalid")
    repo_root = manifest_path.parent.parent.resolve()
    manifest_rel = manifest_path.resolve().relative_to(repo_root).as_posix()
    existing: dict[str, dict] = {}
    for entry in entries:
        if (
            not isinstance(entry, dict)
            or set(entry) != _ENTRY_KEYS
            or not isinstance(entry.get("path"), str)
        ):
            raise ValueError("release_manifest_entry_invalid")
        name = entry["path"]
        if _path_unsafe(name, manifest_rel) or name in existing:
            raise ValueError("release_manifest_entry_path_unsafe")
        existing[name] = entry
    if roster is not None:
        members = _validate_roster(roster, manifest_rel)
        member_set = set(members)
        for name in existing:
            if name not in member_set:
                raise ValueError(f"release_manifest_extra_member:{name}")
        entries = [
            existing.get(name, {"path": name, "sha256": "", "size": 0})
            for name in members
        ]
        payload["files"] = entries
    for entry in entries:
        name = entry["path"]
        source = repo_root / Path(name)
        try:
            source.resolve().relative_to(repo_root)
        except ValueError as exc:
            raise ValueError("release_manifest_entry_path_unsafe") from exc
        if source.is_symlink():
            raise ValueError("release_manifest_source_symlink")
        if not source.is_file():
            raise ValueError("release_manifest_source_missing")
        body = source.read_bytes()
        try:
            _admission._parse_release_member_bytes(body, name)
        except _admission.RegistryConfigError as exc:
            raise ValueError(
                f"release_manifest_member_format_invalid:{name}:{exc.code}"
            ) from exc
        entry["sha256"] = hashlib.sha256(body).hexdigest()
        entry["size"] = len(body)
    entries.sort(key=lambda entry: entry["path"])
    expected = canon.sercanon(payload, sort_keys=True)
    if check:
        return 0 if original == expected else 1
    if _publish is None:
        manifest_path.write_bytes(expected)
    else:
        _publish(manifest_path, expected)
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=ROOT / "catalog/manifest.json")
    parser.add_argument("--version", required=True)
    parser.add_argument("--built-at-utc", required=True)
    parser.add_argument("--check", action="store_true")
    parser.add_argument(
        "--roster-from-admission",
        action="store_true",
        help="construct the membership as exactly the admission owner's ADMITTED_RELEASE_ROSTER",
    )
    args = parser.parse_args(argv)
    roster = _admission.ADMITTED_RELEASE_ROSTER if args.roster_from_admission else None
    try:
        return cut_manifest(
            args.manifest,
            version=args.version,
            built_at_utc=args.built_at_utc,
            check=args.check,
            roster=roster,
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        print(f"RELEASE_MANIFEST_CUT_FAILED:{exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
