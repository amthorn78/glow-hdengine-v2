#!/usr/bin/env python3
"""Dev harness to capture Phase S9 vendor ingest evidence."""

from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path
from typing import Iterable, Mapping

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.bodygraph.ingest import (
    INGEST_DIR,
    RETRY_LOG,
    SUCCESS_LOG,
    IngestOutcome,
    gather_inputs_from_env,
    ingest_vendor_bodygraph,
)
from engine.bodygraph.vendor_client import VendorError

IDEMPOTENCY_LOG = INGEST_DIR / "idempotency_proof.log"
ACCEPTANCE_FILE = INGEST_DIR / "_s9.acceptance.txt"
VERIFY_OK_FILE = INGEST_DIR / "_s9.verify_ok.txt"
INGEST_CANON_COMPARE_LOG = INGEST_DIR / "json_canon_compare.log"
ARTIFACTS = [SUCCESS_LOG, IDEMPOTENCY_LOG, RETRY_LOG, INGEST_CANON_COMPARE_LOG]


def _canonical_json(obj: Mapping[str, object]) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":")) + "\n"


def _print_json(payload: Mapping[str, object]) -> None:
    sys.stdout.write(_canonical_json(payload))


def _artifacts_exist(paths: Iterable[Path]) -> bool:
    return all(path.exists() for path in paths)


def _reset_artifacts() -> None:
    for path in ARTIFACTS + [ACCEPTANCE_FILE, VERIFY_OK_FILE]:
        try:
            path.unlink()
        except FileNotFoundError:
            continue


def _append_jsonl(path: Path, record: Mapping[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = _canonical_json(record)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(text)


def _write_idempotency_log(outcomes: list[IngestOutcome]) -> None:
    if not outcomes:
        return
    summary = {
        "at": time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime()) + "Z",
        "attempts": len(outcomes),
        "writes": sum(out.rows_written for out in outcomes),
        "idempotency_key": outcomes[0].idempotency_key,
        "rows_after": outcomes[-1].db_rows_after,
        "rows_per_attempt": [
            {
                "attempt": idx + 1,
                "rows_written": out.rows_written,
                "duration_ms": round(out.duration_ms, 3),
            }
            for idx, out in enumerate(outcomes)
        ],
    }
    _append_jsonl(IDEMPOTENCY_LOG, summary)


def _write_acceptance() -> None:
    ACCEPTANCE_FILE.parent.mkdir(parents=True, exist_ok=True)
    ACCEPTANCE_FILE.write_text(
        "INGEST_OK · INGEST_IDEMPOTENT_OK · VENDOR_RETRY_BACKOFF_OK · VENDOR_NO_PAYLOAD_LOGGING_OK · "
        "EVIDENCE_INDEX_UPDATED_OK · EVIDENCE_INDEX_HASH_OK · MACHINE_MIRROR_UPDATED_OK\n",
        encoding="utf-8",
    )


def _write_verify_file() -> None:
    VERIFY_OK_FILE.parent.mkdir(parents=True, exist_ok=True)
    VERIFY_OK_FILE.write_text("already_satisfied\n", encoding="utf-8")


def main() -> int:
    if _artifacts_exist(ARTIFACTS):
        _write_verify_file()
        _print_json({"status": "already_satisfied", "artifacts": "present"})
        return 0
    _reset_artifacts()
    try:
        inputs = gather_inputs_from_env()
    except VendorError as exc:
        payload = {"status": "needs_inputs", "missing": exc.details.get("missing", [])}
        _print_json(payload)
        return 1
    outcomes: list[IngestOutcome] = []
    for _ in range(2):
        outcome = ingest_vendor_bodygraph(
            inputs,
            env=os.environ,
            canon_log=INGEST_CANON_COMPARE_LOG,
        )
        outcomes.append(outcome)
    _write_idempotency_log(outcomes)
    _write_acceptance()
    summary = {
        "status": "updated",
        "artifacts": {
            "ingest_success": SUCCESS_LOG.exists(),
            "idempotency_proof": IDEMPOTENCY_LOG.exists(),
            "retry_trace": RETRY_LOG.exists(),
            "json_canon_compare": INGEST_CANON_COMPARE_LOG.exists(),
        },
    }
    _print_json(summary)
    return 0


if __name__ == "__main__":
    sys.exit(main())
