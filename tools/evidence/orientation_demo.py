#!/usr/bin/env python3
"""Produce topology orientation demo and coherence check for evidence skeleton."""
from __future__ import annotations

import argparse
import datetime as _dt
import json
import sys
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.evidence.update_evidence_index import (  # noqa: E402
    MIRROR_PATH,
    ROOT as EVIDENCE_ROOT,
    _load_existing_proof,
    _load_human_index,
)

ORIENTATION_PATH = ROOT / "audit/gates/topology/orientation_demo.txt"


def _load_mirror_records() -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for raw in MIRROR_PATH.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        rec = json.loads(raw)
        records.append(rec)
    records.sort(key=lambda rec: (rec["artifact_key"], rec["discovered_physical_path"]))
    return records


def _validate(entries: Iterable[dict[str, str]], records: Iterable[dict[str, object]]) -> tuple[list[str], int]:
    messages: list[str] = []
    record_map = {
        (rec["artifact_key"], rec["discovered_physical_path"]): rec for rec in records
    }
    total = 0
    for entry in entries:
        total += 1
        key = (entry["artifact_key"], entry["discovered_physical_path"])
        if key not in record_map:
            messages.append(f"MISSING_MIRROR {key[0]} -> {key[1]}")
            continue
        rec = record_map[key]
        artifact_path = ROOT / entry["discovered_physical_path"]
        proof_path = ROOT / rec.get("proof_anchor", "")
        if not artifact_path.exists():
            messages.append(f"MISSING_ARTIFACT {artifact_path.as_posix()}")
            continue
        if not proof_path.exists():
            messages.append(f"MISSING_PROOF {proof_path.as_posix()}")
            continue
        proof = _load_existing_proof(proof_path)
        sha = proof.get("sha256")
        size = proof.get("size_bytes")
        mtime = proof.get("mtime_utc")
        produced = proof.get("produced_at_utc")
        if produced is None or mtime is None:
            messages.append(f"PROOF_FIELDS {key[0]} missing mtime_utc/produced_at_utc")
        else:
            try:
                _dt.datetime.fromisoformat(mtime.replace("Z", "+00:00"))
            except ValueError:
                messages.append(f"PROOF_MTIME_FORMAT {key[0]} {mtime}")
        if sha != rec.get("sha256"):
            messages.append(f"SHA_MISMATCH {key[0]} {sha}!={rec.get('sha256')}")
        if size is None or int(size) != rec.get("size_bytes"):
            messages.append(f"SIZE_MISMATCH {key[0]} {size}!={rec.get('size_bytes')}")

    return messages, total


def _render_report(messages: list[str], total: int) -> str:
    header = [
        "orientation demo (evidence skeleton)",
        f"total_artifacts: {total}",
        f"status: {'ok' if not messages else 'mismatch'}",
    ]
    if messages:
        header.append("issues:")
        header.extend(f"- {msg}" for msg in messages)
    else:
        header.append("sample: INDEX and mirror entries are coherent")
    return "\n".join(header) + "\n"


def generate_orientation(check: bool = False) -> None:
    entries = _load_human_index()
    records = _load_mirror_records()
    messages, total = _validate(entries, records)
    text = _render_report(messages, total)
    # Note: ORIENTATION_DRIFT means the evidence skeleton is coherent (messages empty)
    # but the committed orientation_demo.txt is stale relative to the newly rendered
    # report. The explicit comparison below keeps --check aligned to that semantics.
    if check and messages:
        raise SystemExit("ORIENTATION_MISMATCH")
    ORIENTATION_PATH.parent.mkdir(parents=True, exist_ok=True)
    existing_text = (
        ORIENTATION_PATH.read_text(encoding="utf-8") if ORIENTATION_PATH.exists() else None
    )
    if existing_text != text:
        if check:
            raise SystemExit("ORIENTATION_DRIFT")
        ORIENTATION_PATH.write_text(text, encoding="utf-8")


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Generate topology orientation demo")
    parser.add_argument("--check", action="store_true", help="Fail on mismatches or drift")
    args = parser.parse_args(argv)
    generate_orientation(check=args.check)


if __name__ == "__main__":
    main()
