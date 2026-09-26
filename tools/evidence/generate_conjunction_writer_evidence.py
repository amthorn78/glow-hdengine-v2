#!/usr/bin/env python3
"""Dev conjunction writer/readback evidence (F07; PF10 §2.23, HDE-EPIC040-PR06a).

Closed-rails deterministic capture of the three dev conjunction routes through
the real admission owner.  Two complete mapped current-view rows are built in
process from ``fixtures/charts/alice.json`` ("left") and ``fixtures/charts/bob.json``
("right"), rebased to the canonical ids ``resolve_db_user_id`` yields, and installed
as the app-config lookup seam ``DEV_CONJUNCTION_LOCAL_LOOKUP`` that only the dev
routes read (behind ``_dev_admin_gate``).  A control request without the seam is
sent first and must be refused (``PROVIDER_REFUSED`` under closed rails), which
proves the routes fabricate nothing by default.  The routes carry the admitted
``release_id`` (no ``dev_compat_identity`` stamp anywhere).

The generator requires closed rails (``SAFE_MODE=1``, ``ALLOW_NETWORK=0``) and
refuses otherwise, so it can never reach a vendor even when credentials exist;
``DATABASE_URL`` is neutralized in both write and ``--check`` modes.
"""
from __future__ import annotations

import argparse
from contextlib import contextmanager
import hashlib
import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from adapter.http_reader import create_app
from engine.bodygraph.ingest import resolve_db_user_id
from engine.bodygraph.mapped_cache import MappedBodyGraphRow
from engine.bodygraph.projection import project_bodygraph
from engine.runtime.identity import identity_meta
from engine.serializer import canon

WRITE_READBACK_LOG = ROOT / "artifacts/writer/conjunction_write_readback.log"
WRITER_SUMMARY = ROOT / "artifacts/writer/conjunction_writer_summary.json"
SEAM_CONFIG_KEY = "DEV_CONJUNCTION_LOCAL_LOOKUP"
FIXTURES = {"left": ROOT / "fixtures/charts/alice.json", "right": ROOT / "fixtures/charts/bob.json"}
_ENV_UNSET = object()

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


def _as_json_bytes(payload: dict[str, object]) -> bytes:
    return canon.sercanon(payload, sort_keys=True)


def _require_closed_rails() -> None:
    safe_mode = os.environ.get("SAFE_MODE", "1")
    allow_network = os.environ.get("ALLOW_NETWORK", "0")
    if safe_mode != "1" or allow_network != "0":
        raise SystemExit(
            "generate_conjunction_writer_evidence requires closed rails "
            "(SAFE_MODE=1 and ALLOW_NETWORK=0): the dev conjunction evidence is a "
            "deterministic in-process capture and never a vendor acquisition"
        )


def _fixture_rows() -> dict[str, MappedBodyGraphRow]:
    """Two complete current-view rows keyed by the canonical id of each engine key."""

    rows: dict[str, MappedBodyGraphRow] = {}
    for key, path in FIXTURES.items():
        fixture = json.loads(path.read_text(encoding="utf-8"))
        canonical_id = resolve_db_user_id(key)
        chart = {
            "bodygraph": fixture["bodygraph"],
            "person": {"person_uid": canonical_id},
            "person_uid": canonical_id,
        }
        rows[canonical_id] = MappedBodyGraphRow(
            user_id=canonical_id,
            vendor="hdapi",
            vendor_version=2,
            input_fingerprint=hashlib.sha256(canon.sercanon(fixture["bodygraph"], sort_keys=True)).hexdigest(),
            payload=project_bodygraph(chart),
        )
    return rows


def _compat(payload: object) -> dict[str, object] | None:
    if not isinstance(payload, dict):
        return None
    conjunction = payload.get("conjunction")
    if not isinstance(conjunction, dict):
        return None
    compat = conjunction.get("compat")
    return compat if isinstance(compat, dict) else None


def _admitted_identity(payload: object, release_id: str) -> bool:
    compat = _compat(payload)
    return (
        compat is not None
        and compat.get("release_id") == release_id
        and compat.get("schema") == "magic10_compat_result.v1"
    )


def _no_dev_identity_stamp(payload: object) -> bool:
    compat = _compat(payload)
    return compat is not None and "meta" not in compat and compat.get("release_id") != "dev"


def _capture_outputs() -> dict[Path, bytes]:
    os.environ.setdefault("APP_ENV", "dev")
    _require_closed_rails()
    release_id = identity_meta()["release_id"]

    app = create_app()
    app.config.update(TESTING=True)
    assert SEAM_CONFIG_KEY not in app.config

    with app.test_client() as client:
        # Control: without the seam the routes resolve nothing and refuse under closed rails.
        control = client.get("/dev/reader/conjunction", query_string=QUERY)
        control_payload = json.loads(control.data) if control.data else {}
        seam_absent_refuses = (
            control.status_code == 503
            and control_payload.get("code") == "ERR_WRITER_RAILS_CLOSED"
            and isinstance(control_payload.get("details"), dict)
            and control_payload["details"].get("provider_code") == "PROVIDER_REFUSED"
        )

        app.config[SEAM_CONFIG_KEY] = _fixture_rows().get
        writer_first = client.get("/dev/writer/conjunction", query_string=QUERY)
        writer_second = client.get("/dev/writer/conjunction", query_string=QUERY)
        reader = client.get("/dev/reader/conjunction", query_string=QUERY)
        writer_invalid = client.get(
            "/dev/writer/conjunction",
            query_string={"a_user_id": "left"},
        )

    if (
        not seam_absent_refuses
        or writer_first.status_code != 200
        or writer_second.status_code != 200
        or reader.status_code != 200
        or writer_invalid.status_code != 422
    ):
        raise SystemExit(
            "writer/readback failure statuses: "
            f"control={control.status_code} "
            f"writer_first={writer_first.status_code} "
            f"writer_second={writer_second.status_code} "
            f"reader={reader.status_code} "
            f"writer_invalid={writer_invalid.status_code}"
        )

    writer_first_payload = json.loads(writer_first.data)
    writer_second_payload = json.loads(writer_second.data)
    reader_payload = json.loads(reader.data)
    writer_invalid_payload = json.loads(writer_invalid.data)

    writer_result = writer_first_payload.get("result")
    parity_writer_bytes = writer_first.data == writer_second.data
    parity_writer_result = writer_first_payload == writer_second_payload
    parity_readback = writer_result == reader_payload

    checks = {
        "seam_absent_refuses_closed_rails": seam_absent_refuses,
        "writer_status_200": True,
        "reader_status_200": True,
        "writer_bytes_two_run_equal": parity_writer_bytes,
        "writer_payload_two_run_equal": parity_writer_result,
        "writer_result_reader_readback_equal": parity_readback,
        "writer_success_typed_envelope": writer_first_payload.get("type")
        == "dev.writer.conjunction.success.v1",
        "writer_error_typed_envelope": writer_invalid_payload.get("type")
        == "dev.writer.conjunction.error.v1",
        "writer_admitted_release_identity": _admitted_identity(writer_result, release_id),
        "reader_admitted_release_identity": _admitted_identity(reader_payload, release_id),
        "no_dev_identity_stamp": _no_dev_identity_stamp(writer_result) and _no_dev_identity_stamp(reader_payload),
    }
    summary = {
        "schema": "conjunction_writer_summary.v2",
        "route": "/dev/writer/conjunction",
        "reader_route": "/dev/reader/conjunction",
        "rails": "closed",
        "release_id": release_id,
        "writer_route_id": writer_first_payload.get("writer", {}).get(
            "writer_route_id"
        ),
        "idempotence_hash": writer_first_payload.get("writer", {}).get(
            "idempotence_hash"
        ),
        "checks": checks,
        "query": QUERY,
    }

    if not all(summary["checks"].values()):
        raise SystemExit(f"writer evidence checks failed: {summary['checks']}")

    log_body = "\n".join(
        [
            "schema=conjunction_write_readback.log.v2",
            "rails=closed",
            f"release_id={release_id}",
            "route=/dev/writer/conjunction",
            "reader_route=/dev/reader/conjunction",
            f"control_status={control.status_code}",
            "writer_first_status=200",
            "writer_second_status=200",
            "reader_status=200",
            "writer_invalid_status=422",
            f"writer_route_id={summary['writer_route_id']}",
            f"idempotence_hash={summary['idempotence_hash']}",
            *(f"{name}={str(value).lower()}" for name, value in checks.items()),
            f"writer_success_type={writer_first_payload.get('type')}",
            f"writer_error_type={writer_invalid_payload.get('type')}",
            f"writer_payload_sha256={hashlib.sha256(_as_json_bytes(writer_first_payload)).hexdigest()}",
            f"reader_payload_sha256={hashlib.sha256(_as_json_bytes(reader_payload)).hexdigest()}",
            "",
        ]
    ).encode("utf-8")

    return {
        WRITE_READBACK_LOG: log_body,
        WRITER_SUMMARY: _as_json_bytes(summary),
    }


@contextmanager
def _non_persistent_capture():
    """Run the capture without the dev writer database persistence path (both modes)."""
    original_database_url = os.environ.get("DATABASE_URL", _ENV_UNSET)
    try:
        os.environ.pop("DATABASE_URL", None)
        yield
    finally:
        if original_database_url is _ENV_UNSET:
            os.environ.pop("DATABASE_URL", None)
        else:
            os.environ["DATABASE_URL"] = original_database_url


# Retained name: the check-mode context manager is the same neutralization.
_non_persistent_check_capture = _non_persistent_capture


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv)

    with _non_persistent_capture():
        expected = _capture_outputs()

    if args.check:
        drift = [
            path.relative_to(ROOT).as_posix()
            for path, body in expected.items()
            if not path.exists() or path.read_bytes() != body
        ]
        if drift:
            raise SystemExit("DRIFT:" + ",".join(drift))
        return 0

    for path, body in expected.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(body)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
