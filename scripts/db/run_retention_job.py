"""Run the EPIC-011 retention harness under closed rails."""
from __future__ import annotations

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from time import perf_counter

from engine.bodygraph.retention import run_bodygraph_retention
from engine.db.adapter import DBAccess

LOG_PATH = Path("artifacts/db/retention/retention_run.log")
ROUTE = "ops.retention.bodygraph"


def _iso_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _ensure_rails_closed() -> None:
    safe_mode = os.getenv("SAFE_MODE")
    allow_network = os.getenv("ALLOW_NETWORK")
    if safe_mode != "1" or allow_network != "0":
        print(
            json.dumps(
                {
                    "status": "error",
                    "code": "rails_not_closed",
                    "safe_mode": safe_mode,
                    "allow_network": allow_network,
                },
                separators=(",", ":"),
                sort_keys=True,
            ),
            file=sys.stderr,
        )
        raise SystemExit(1)


def _write_log(records: list[dict]) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("w", encoding="utf-8") as handle:
        for record in records:
            text = json.dumps(record, separators=(",", ":"), sort_keys=True)
            handle.write(text + "\n")


def main() -> None:
    _ensure_rails_closed()

    db = DBAccess.for_current_env()
    start = perf_counter()
    entries = run_bodygraph_retention(db)
    duration_ms = (perf_counter() - start) * 1000

    timestamp = _iso_now()
    records: list[dict] = []
    for entry in entries:
        record = {
            "action": entry["action"],
            "at": timestamp,
            "deleted_rows": entry["deleted_rows"],
            "inspected_rows": entry["inspected_rows"],
            "route": ROUTE,
            "status": "ok",
            "table": entry["table"],
        }
        records.append(record)

    records.append(
        {
            "at": timestamp,
            "duration_ms": round(duration_ms, 3),
            "route": ROUTE,
            "status": "ok",
            "summary": {
                "checked_tables": len(entries),
                "bodygraph_deletes": 0,
            },
        }
    )

    _write_log(records)


if __name__ == "__main__":  # pragma: no cover - script entrypoint
    main()
