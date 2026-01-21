#!/usr/bin/env python3
"""Refresh EPIC024 QA step logs manifest with deterministic ordering."""
from __future__ import annotations

import argparse
import datetime as _dt
import sys
from pathlib import Path
from dataclasses import dataclass
from typing import Iterable

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.runtime.determinism_env import DeterminismEnvError, ensure_determinism_env
from engine.serializer.canon import sercanon
from tools.evidence import update_evidence_index
DEFAULT_QA_ROOT = ROOT / "audit/qa/hde-epic024"
DEFAULT_MANIFEST = DEFAULT_QA_ROOT / "qa_step_logs_manifest.json"


@dataclass(frozen=True)
class CheckEntry:
    check_id: str
    log_path: str
    transcript_path: str | None


def _utc_now() -> str:
    return _dt.datetime.now(_dt.timezone.utc).replace(microsecond=0).isoformat().replace(
        "+00:00", "Z"
    )


def collect_check_entries(checks_root: Path) -> list[CheckEntry]:
    entries: list[CheckEntry] = []
    if not checks_root.exists():
        return entries
    for entry in checks_root.iterdir():
        if not entry.is_dir():
            continue
        primary_log = entry / "primary.log"
        if not primary_log.exists():
            continue
        transcript = entry / "transcript.txt"
        transcript_path = None
        if transcript.exists():
            transcript_path = f"checks/{entry.name}/transcript.txt"
        entries.append(
            CheckEntry(
                check_id=entry.name,
                log_path=f"checks/{entry.name}/primary.log",
                transcript_path=transcript_path,
            )
        )
    return sorted(entries, key=lambda item: item.check_id)


def collect_check_ids(checks_root: Path) -> list[str]:
    return [entry.check_id for entry in collect_check_entries(checks_root)]


def build_manifest_payload(check_entries: Iterable[CheckEntry]) -> dict[str, dict[str, str]]:
    payload: dict[str, dict[str, str]] = {}
    for entry in check_entries:
        item = {"check_id": entry.check_id, "log_path": entry.log_path}
        if entry.transcript_path:
            item["transcript_path"] = entry.transcript_path
        payload[entry.check_id] = item
    return payload


def render_manifest(payload: dict[str, dict[str, str]]) -> bytes:
    return sercanon(payload, sort_keys=True)


def _sha256_path(path: Path) -> str:
    return update_evidence_index._sha256_path(path)


def _write_path_proof(path: Path, *, produced_at: str, check: bool) -> None:
    rel = path.relative_to(ROOT).as_posix()
    stat = path.stat()
    update_evidence_index._write_path_proof(
        rel=rel,
        sha256=_sha256_path(path),
        size_bytes=stat.st_size,
        mtime_utc=update_evidence_index._isoformat_from_timestamp(stat.st_mtime)
        if not check
        else None,
        produced_at=produced_at if not check else None,
        default_produced_at=produced_at,
        check=check,
        stat_mtime=stat.st_mtime,
    )


def write_manifest(path: Path, payload: dict[str, dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    rendered = render_manifest(payload)
    if path.exists() and path.read_bytes() == rendered:
        return
    path.write_bytes(rendered)


def run_refresh(args: argparse.Namespace) -> int:
    produced_at = args.produced_at or _utc_now()
    try:
        ensure_determinism_env()
    except DeterminismEnvError:
        return 2

    qa_root = Path(args.qa_root)
    manifest_path = Path(args.manifest)
    checks_root = qa_root / "checks"
    check_entries = collect_check_entries(checks_root)
    if not check_entries:
        return 2

    payload = build_manifest_payload(check_entries)
    rendered = render_manifest(payload)

    if args.check:
        if not manifest_path.exists():
            return 2
        if manifest_path.read_bytes() != rendered:
            return 1
        for entry in check_entries:
            log_path = qa_root / entry.log_path
            try:
                _write_path_proof(log_path, produced_at=produced_at, check=True)
            except SystemExit:
                return 1
            if entry.transcript_path:
                transcript_path = qa_root / entry.transcript_path
                try:
                    _write_path_proof(transcript_path, produced_at=produced_at, check=True)
                except SystemExit:
                    return 1
        _write_path_proof(manifest_path, produced_at=produced_at, check=True)
        return 0

    write_manifest(manifest_path, payload)
    _write_path_proof(manifest_path, produced_at=produced_at, check=False)
    for entry in check_entries:
        log_path = qa_root / entry.log_path
        _write_path_proof(log_path, produced_at=produced_at, check=False)
        if entry.transcript_path:
            transcript_path = qa_root / entry.transcript_path
            _write_path_proof(transcript_path, produced_at=produced_at, check=False)
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Refresh EPIC024 QA step logs manifest."
    )
    parser.add_argument("--qa-root", default=DEFAULT_QA_ROOT)
    parser.add_argument("--manifest", default=DEFAULT_MANIFEST)
    parser.add_argument("--produced-at", help="UTC ISO8601 timestamp")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    return run_refresh(args)


if __name__ == "__main__":
    raise SystemExit(main())
