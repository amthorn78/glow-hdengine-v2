#!/usr/bin/env python3
"""Materialize the immutable four-row Presenter history primary."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import tempfile
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.serializer import canon

SOURCE = ROOT / "tools/evidence/fixtures/presenter/json_canon_compare.history.v1.json"
DESTINATION = ROOT / "artifacts/presenter/json_canon_compare.log"
RECORD_IDS = (
    "epic011_s10_rails_closed_match",
    "epic011_s10_diff",
    "epic011_live_match_a",
    "epic011_live_match_b",
)
ROW_HASHES = (
    "601c48f5a1d57a15e769d34fe02ae9ada830e3e46256e0c66e596cf6d4f8102a",
    "44be55631c71a7717fea11cca56f18c4c389dfc661949ec20626085001d55489",
    "ea2ba6b4097770b6075c9b6b905c9a227f455db1bc47c248858cd8d7d4484cc5",
    "e44b9f222b34335488de917d452f21b2720f655e6545f48672085154687c0cf5",
)
OUTPUT_LENGTH = 1559
OUTPUT_SHA256 = "64980228d042249a10ecc89ebddcff00be27aae9c79ba2330a24a28b0c59676c"


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _load_expected() -> bytes:
    try:
        source_bytes = SOURCE.read_bytes()
        payload = json.loads(source_bytes)
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"INVALID_HISTORY_SOURCE:{exc}") from exc
    if canon.sercanon(payload, sort_keys=True) != source_bytes:
        raise SystemExit("NONCANONICAL_HISTORY_SOURCE")
    if not isinstance(payload, dict) or set(payload) != {"schema", "records", "output_sha256"}:
        raise SystemExit("INVALID_HISTORY_SOURCE_KEYS")
    if payload["schema"] != "presenter.history_source.v1":
        raise SystemExit("INVALID_HISTORY_SOURCE_SCHEMA")
    records = payload["records"]
    if not isinstance(records, list) or len(records) != 4:
        raise SystemExit("INVALID_HISTORY_SOURCE_COUNT")
    if [row.get("record_id") for row in records if isinstance(row, dict)] != list(RECORD_IDS):
        raise SystemExit("INVALID_HISTORY_SOURCE_ORDER")
    if len(set(RECORD_IDS)) != len(RECORD_IDS):
        raise SystemExit("DUPLICATE_HISTORY_RECORD_ID")

    rows: list[bytes] = []
    for index, record in enumerate(records):
        if not isinstance(record, dict) or set(record) != {"record_id", "payload", "payload_sha256"}:
            raise SystemExit(f"INVALID_HISTORY_RECORD_KEYS:{index}")
        if not isinstance(record["payload"], dict):
            raise SystemExit(f"INVALID_HISTORY_PAYLOAD:{index}")
        row_bytes = canon.sercanon(record["payload"], sort_keys=True)
        row_hash = _sha(row_bytes)
        if record["payload_sha256"] != ROW_HASHES[index] or row_hash != ROW_HASHES[index]:
            raise SystemExit(f"INVALID_HISTORY_ROW_HASH:{index}")
        rows.append(row_bytes)

    output = b"".join(rows)
    if len(output) != OUTPUT_LENGTH:
        raise SystemExit(f"INVALID_HISTORY_OUTPUT_LENGTH:{len(output)}")
    if payload["output_sha256"] != OUTPUT_SHA256 or _sha(output) != OUTPUT_SHA256:
        raise SystemExit("INVALID_HISTORY_OUTPUT_HASH")
    return output


def _atomic_write(data: bytes) -> None:
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    fd, raw_tmp = tempfile.mkstemp(prefix=f".{DESTINATION.name}.", dir=DESTINATION.parent)
    temporary = Path(raw_tmp)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, DESTINATION)
    finally:
        temporary.unlink(missing_ok=True)


def generate(*, check: bool = False) -> None:
    expected = _load_expected()
    if check:
        if not DESTINATION.exists() or DESTINATION.read_bytes() != expected:
            raise SystemExit(f"STALE:{DESTINATION.relative_to(ROOT).as_posix()}")
        return
    _atomic_write(expected)


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(list(argv) if argv is not None else None)
    generate(check=args.check)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
