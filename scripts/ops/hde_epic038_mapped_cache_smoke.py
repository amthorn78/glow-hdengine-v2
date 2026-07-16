#!/usr/bin/env python3
"""PO-only OPS-02 mapped-cache smoke; never run as PR validation."""
from __future__ import annotations

import argparse
import os
import sys
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from engine.bodygraph.mapped_cache import persist_mapped_bodygraph
from engine.bodygraph.projection import project_bodygraph
from engine.bodygraph.v2_adapter import V2ChartAdapterContext, adapt_v2_chart_payload
from engine.bodygraph.vendor_client import HdApiClient
from engine.db import DBAccess
from engine.serializer.canon import sercanon

REQUIRED_ENV = ("HD_API_BASE_URL", "HD_API_KEY", "GEO_API_KEY", "DATABASE_URL")
PRODUCTION_LIKE = {"prod", "production", "live"}


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="PO-authorized one-request configured-v2 mapped-cache smoke")
    parser.add_argument("--synthetic-user-id", required=True)
    parser.add_argument("--synthetic-person-uid", required=True)
    parser.add_argument("--birthdate", required=True)
    parser.add_argument("--birthtime", required=True)
    parser.add_argument("--location", required=True)
    return parser


def _preflight(args: argparse.Namespace) -> None:
    if os.environ.get("SAFE_MODE") != "0" or os.environ.get("ALLOW_NETWORK") != "1":
        raise SystemExit("OPS_REFUSED: explicit open rails required")
    app_env = os.environ.get("APP_ENV", "").strip().lower()
    if not app_env or app_env in PRODUCTION_LIKE:
        raise SystemExit("OPS_REFUSED: explicit non-production APP_ENV required")
    missing = [name for name in REQUIRED_ENV if not os.environ.get(name, "").strip()]
    if missing:
        raise SystemExit("OPS_REFUSED: required environment names are unset: " + ",".join(missing))
    try:
        uuid.UUID(args.synthetic_user_id)
    except ValueError as exc:
        raise SystemExit("OPS_REFUSED: synthetic user identity must be a UUID") from exc
    if not all(str(getattr(args, name)).strip() for name in ("synthetic_person_uid", "birthdate", "birthtime", "location")):
        raise SystemExit("OPS_REFUSED: complete synthetic inputs required")


def main(argv=None) -> int:
    args = _parser().parse_args(argv); _preflight(args)
    client = HdApiClient.from_env(env=os.environ)
    request = client.build_contract_route_request(path="charts", request_fields=("birthdate","birthtime","location"), geocode_required=True,
        birthdate=args.birthdate, birthtime=args.birthtime, location=args.location)
    vendor_result = client.fetch(request)  # exactly one authorized vendor request
    context = V2ChartAdapterContext(person_uid=args.synthetic_person_uid,user_id=args.synthetic_user_id,vendor="hdapi",vendor_version=2,
        input_fingerprint=request.input_fingerprint,route_family="recommended_v2_chart",route=request.route,payload_family="ChartResult")
    adapter = adapt_v2_chart_payload(vendor_result.payload,context).as_dict()
    if adapter["status"] != "mapped": raise SystemExit("OPS_FAILED: adapter mapping refused")
    project_bodygraph(adapter["cache"]["payload"])
    db = DBAccess.for_current_env(snapshot_path=None)
    first = persist_mapped_bodygraph(db,adapter["cache"])
    second = persist_mapped_bodygraph(db,adapter["cache"])
    summary = {"status":"ok","vendor_requests":1,"adapter_status":adapter["code"],"provider":first.provider,
        "canonical_sha256":first.canonical_sha256,"read_back_match":first.read_back_match,"identity_rows":second.rows_after,
        "second_write_rows":second.rows_written,"idempotent":second.idempotent,"retention_decision":"PO_REQUIRED"}
    sys.stdout.buffer.write(sercanon(summary)); return 0


if __name__ == "__main__": raise SystemExit(main())
