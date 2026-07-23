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
from typing import Sequence

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

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


def cut_manifest(
    manifest_path: Path,
    *,
    version: str,
    built_at_utc: str,
    check: bool = False,
) -> int:
    """Render or verify one canonical manifest without derived evidence writes."""

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
    seen: set[str] = set()
    for entry in entries:
        if (
            not isinstance(entry, dict)
            or set(entry) != _ENTRY_KEYS
            or not isinstance(entry.get("path"), str)
        ):
            raise ValueError("release_manifest_entry_invalid")
        name = entry["path"]
        rel = Path(name)
        if (
            rel.is_absolute()
            or ".." in rel.parts
            or rel.as_posix() != name
            or name in seen
            or name == manifest_rel
        ):
            raise ValueError("release_manifest_entry_path_unsafe")
        seen.add(name)
        source = repo_root / rel
        try:
            source.resolve().relative_to(repo_root)
        except ValueError as exc:
            raise ValueError("release_manifest_entry_path_unsafe") from exc
        if source.is_symlink():
            raise ValueError("release_manifest_source_symlink")
        if not source.is_file():
            raise ValueError("release_manifest_source_missing")
        body = source.read_bytes()
        entry["sha256"] = hashlib.sha256(body).hexdigest()
        entry["size"] = len(body)
    entries.sort(key=lambda entry: entry["path"])
    expected = canon.sercanon(payload, sort_keys=True)
    if check:
        return 0 if original == expected else 1
    manifest_path.write_bytes(expected)
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=ROOT / "catalog/manifest.json")
    parser.add_argument("--version", required=True)
    parser.add_argument("--built-at-utc", required=True)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)
    try:
        return cut_manifest(
            args.manifest,
            version=args.version,
            built_at_utc=args.built_at_utc,
            check=args.check,
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        print(f"RELEASE_MANIFEST_CUT_FAILED:{exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
