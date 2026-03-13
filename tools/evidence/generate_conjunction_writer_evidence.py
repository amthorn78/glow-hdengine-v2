#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from adapter.http_reader import create_app
from engine.serializer import canon

WRITE_READBACK_LOG = ROOT / "artifacts/writer/conjunction_write_readback.log"
WRITER_SUMMARY = ROOT / "artifacts/writer/conjunction_writer_summary.json"

QUERY = {
    "a_user_id": "left",
    "b_user_id": "right",
    "a_birthdate": "1990-01-01",
    "a_birthtime": "08:30",
    "a_location": "Amsterdam",
    "b_birthdate": "1991-02-02",
    "b_birthtime": "09:45",
    "b_location": "Berlin",
}

CONJUNCTION_ENV_PINS = {
    "ENGINE_TAG": "hdengine-alpha",
    "RELEASE_ID": "0" * 64,
    "PRODUCT_INVOCATION_TAG": "INV-UNKNOWN",
}


def _as_json_bytes(payload: dict[str, object]) -> bytes:
    return canon.sercanon(payload, sort_keys=True)


def _require_open_rails() -> None:
    safe_mode = os.environ.get("SAFE_MODE", "1")
    allow_network = os.environ.get("ALLOW_NETWORK", "0")
    if safe_mode != "0" or allow_network != "1":
        raise SystemExit(
            "generate_conjunction_writer_evidence requires explicit open rails from caller "
            "(set SAFE_MODE=0 and ALLOW_NETWORK=1) for /dev/*/conjunction resolver acquisition"
        )


def main() -> int:
    os.environ.setdefault("APP_ENV", "dev")
    _require_open_rails()
    for key, value in CONJUNCTION_ENV_PINS.items():
        os.environ[key] = value

    app = create_app()
    app.config.update(TESTING=True)

    with app.test_client() as client:
        writer_first = client.get("/dev/writer/conjunction", query_string=QUERY)
        writer_second = client.get("/dev/writer/conjunction", query_string=QUERY)
        reader = client.get("/dev/reader/conjunction", query_string=QUERY)

    if writer_first.status_code != 200 or writer_second.status_code != 200 or reader.status_code != 200:
        raise SystemExit(
            f"writer/readback failure statuses: writer_first={writer_first.status_code} writer_second={writer_second.status_code} reader={reader.status_code}"
        )

    writer_first_payload = json.loads(writer_first.data)
    writer_second_payload = json.loads(writer_second.data)
    reader_payload = json.loads(reader.data)

    writer_result = writer_first_payload.get("result")
    parity_writer_bytes = writer_first.data == writer_second.data
    parity_writer_result = writer_first_payload == writer_second_payload
    parity_readback = writer_result == reader_payload

    summary = {
        "schema": "conjunction_writer_summary.v1",
        "route": "/dev/writer/conjunction",
        "reader_route": "/dev/reader/conjunction",
        "writer_route_id": writer_first_payload.get("writer", {}).get("writer_route_id"),
        "idempotence_hash": writer_first_payload.get("writer", {}).get("idempotence_hash"),
        "checks": {
            "writer_status_200": True,
            "reader_status_200": True,
            "writer_bytes_two_run_equal": parity_writer_bytes,
            "writer_payload_two_run_equal": parity_writer_result,
            "writer_result_reader_readback_equal": parity_readback,
        },
        "query": QUERY,
    }

    if not all(summary["checks"].values()):
        raise SystemExit(f"writer evidence checks failed: {summary['checks']}")

    WRITE_READBACK_LOG.parent.mkdir(parents=True, exist_ok=True)
    WRITE_READBACK_LOG.write_text(
        "\n".join(
            [
                "schema=conjunction_write_readback.log.v1",
                "route=/dev/writer/conjunction",
                "reader_route=/dev/reader/conjunction",
                "writer_first_status=200",
                "writer_second_status=200",
                "reader_status=200",
                f"writer_route_id={summary['writer_route_id']}",
                f"idempotence_hash={summary['idempotence_hash']}",
                f"writer_bytes_two_run_equal={str(parity_writer_bytes).lower()}",
                f"writer_payload_two_run_equal={str(parity_writer_result).lower()}",
                f"writer_result_reader_readback_equal={str(parity_readback).lower()}",
                f"writer_payload_sha256={hashlib.sha256(_as_json_bytes(writer_first_payload)).hexdigest()}",
                f"reader_payload_sha256={hashlib.sha256(_as_json_bytes(reader_payload)).hexdigest()}",
                "",
            ]
        ),
        encoding="utf-8",
    )

    WRITER_SUMMARY.write_bytes(_as_json_bytes(summary))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
