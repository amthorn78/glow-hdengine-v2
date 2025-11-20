from __future__ import annotations

import json
import os
import time
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path
from typing import Any, Mapping, MutableMapping, Sequence
import uuid

from engine.db import DBAccess, Statement
from engine.db.errors import AdapterError
from engine.presenter import emitter

from .vendor_client import HdApiClient, VendorError, VendorRequest

# NOTE [EPIC011 – temporary alias bridge]
# hde.body_graphs.user_id is a UUID column, but the resolver/CLI may be given
# synthetic or non-UUID identifiers (for example "epic011-s10-invariance-1")
# while we still lack a full app user identity system. The map below pins the
# handful of EPIC011 test aliases to deterministic UUIDs so that the ingest and
# source invariance harnesses can share a stable DB row. For any other
# non-UUID identifier we derive a uuid5 alias deterministically. This keeps the
# ingest path idempotent for synthetic IDs today, but the alias layer is not a
# long-term identity model and should be revisited once a proper user system is
# available. The `user_id` here is purely an internal durability anchor for our
# own database row; the vendor never sees this value.
SYNTHETIC_USER_ID_MAP = {
    "epic011-s10-invariance-1": "3fa85f64-5717-4562-b3fc-2c963f66afab",
}


def resolve_db_user_id(user_id: str) -> str:
    normalized = (user_id or "").strip()
    if not normalized:
        raise VendorError("PROVIDER_INPUT_INVALID", "user_id is required")
    mapped = SYNTHETIC_USER_ID_MAP.get(normalized)
    if mapped:
        return mapped
    try:
        uuid.UUID(normalized)
    except ValueError:
        return str(uuid.uuid5(uuid.NAMESPACE_URL, normalized))
    return normalized


INGEST_DIR = Path("artifacts/ingest")
SUCCESS_LOG = INGEST_DIR / "ingest_success.log"
RETRY_LOG = INGEST_DIR / "retry_trace.log"
CANON_COMPARE_LOG = Path("artifacts/presenter/json_canon_compare.log")


def _truthy(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes", "on"}
    return bool(value)


def _append_jsonl(path: Path, record: Mapping[str, Any]) -> None:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        text = json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n"
        with path.open("a", encoding="utf-8") as handle:
            handle.write(text)
    except Exception:
        return


def _utc_iso() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%S", time.gmtime()) + "Z"


@dataclass(frozen=True)
class VendorInputs:
    user_id: str
    birthdate: str
    birthtime: str
    location: str


@dataclass(frozen=True)
class IngestOutcome:
    vendor: str
    vendor_version: int
    input_fingerprint: str
    idempotency_key: str
    rows_written: int
    duration_ms: float
    payload_sha256: str
    db_emitted_sha256: str
    parity_match: bool
    db_rows_after: int
    payload: Mapping[str, Any]


def gather_inputs_from_env() -> VendorInputs:
    env = os.environ
    missing = [name for name in ("INGEST_TEST_USER_ID", "INGEST_TEST_BIRTHDATE", "INGEST_TEST_BIRTHTIME", "INGEST_TEST_LOCATION") if not (env.get(name) or "").strip()]
    if missing:
        raise VendorError("PROVIDER_INPUT_MISSING", "ingest inputs missing", details={"missing": missing})
    return VendorInputs(
        user_id=env["INGEST_TEST_USER_ID"].strip(),
        birthdate=env["INGEST_TEST_BIRTHDATE"].strip(),
        birthtime=env["INGEST_TEST_BIRTHTIME"].strip(),
        location=env["INGEST_TEST_LOCATION"].strip(),
    )


def ingest_vendor_bodygraph(
    inputs: VendorInputs,
    *,
    env: Mapping[str, object] | None = None,
    dry_run: bool = False,
    client: HdApiClient | None = None,
    db_access: DBAccess | None = None,
    retry_log: Path = RETRY_LOG,
    success_log: Path = SUCCESS_LOG,
    canon_log: Path = CANON_COMPARE_LOG,
    vendor_version: int = 1,
) -> IngestOutcome:
    env = env or os.environ
    safe_mode = _truthy(env.get("SAFE_MODE"))
    allow_network = _truthy(env.get("ALLOW_NETWORK"))
    if safe_mode:
        raise VendorError("PROVIDER_REFUSED", "Vendor source refused under SAFE rails", details={"SAFE_MODE": True})
    if not allow_network:
        raise VendorError("PROVIDER_NETWORK_BLOCKED", "Network blocked by rails")
    start = time.monotonic()
    client = client or HdApiClient.from_env(log_path=retry_log)
    request = client.build_request(birthdate=inputs.birthdate, birthtime=inputs.birthtime, location=inputs.location)
    vendor_result = client.fetch(request)
    payload_bytes, _ = emitter.emit_compact_json(vendor_result.payload)
    payload_text = payload_bytes.decode("utf-8")
    payload_sha = sha256(payload_bytes).hexdigest()
    idempotency_key = _idempotency_key(inputs.user_id, "hdapi", vendor_version, request.input_fingerprint)
    if dry_run:
        duration_ms = (time.monotonic() - start) * 1000.0
        _append_jsonl(success_log, {
            "at": _utc_iso(),
            "route": "ops.ingest.bodygraph",
            "status": "ok",
            "user_id": inputs.user_id,
            "provider": "hdapi",
            "vendor_version": vendor_version,
            "input_fingerprint": request.input_fingerprint,
            "idempotency_key": idempotency_key,
            "rows_affected": 0,
            "duration_ms": round(duration_ms, 3),
        })
        return IngestOutcome(
            vendor="hdapi",
            vendor_version=vendor_version,
            input_fingerprint=request.input_fingerprint,
            idempotency_key=idempotency_key,
            rows_written=0,
            duration_ms=duration_ms,
            payload_sha256=payload_sha,
            db_emitted_sha256=payload_sha,
            parity_match=True,
            db_rows_after=0,
            payload=vendor_result.payload,
        )
    db = db_access or DBAccess.for_current_env()
    rows_before = _row_count(db, inputs.user_id, "hdapi", vendor_version, request.input_fingerprint)
    _persist_bodygraph(db, inputs.user_id, vendor_version, request, payload_text)
    db_rows_after = _row_count(db, inputs.user_id, "hdapi", vendor_version, request.input_fingerprint)
    rows_written = max(db_rows_after - rows_before, 0)
    stored_payload = _fetch_payload(db, inputs.user_id, "hdapi", vendor_version, request.input_fingerprint)
    db_payload = json.loads(stored_payload)
    db_emitted_bytes, _ = emitter.emit_compact_json(db_payload)
    db_emitted_sha = sha256(db_emitted_bytes).hexdigest()
    parity_match = payload_sha == db_emitted_sha
    duration_ms = (time.monotonic() - start) * 1000.0
    _append_jsonl(success_log, {
        "at": _utc_iso(),
        "route": "ops.ingest.bodygraph",
        "status": "ok",
        "user_id": inputs.user_id,
        "provider": "hdapi",
        "vendor_version": vendor_version,
        "input_fingerprint": request.input_fingerprint,
        "idempotency_key": idempotency_key,
        "rows_affected": rows_written,
        "duration_ms": round(duration_ms, 3),
    })
    _append_jsonl(canon_log, {
        "at": _utc_iso(),
        "user_id": inputs.user_id,
        "vendor": "hdapi",
        "vendor_version": vendor_version,
        "input_fingerprint": request.input_fingerprint,
        "vendor_sha256": payload_sha,
        "db_emitted_sha256": db_emitted_sha,
        "match": parity_match,
    })
    return IngestOutcome(
        vendor="hdapi",
        vendor_version=vendor_version,
        input_fingerprint=request.input_fingerprint,
        idempotency_key=idempotency_key,
        rows_written=rows_written,
        duration_ms=duration_ms,
        payload_sha256=payload_sha,
        db_emitted_sha256=db_emitted_sha,
        parity_match=parity_match,
        db_rows_after=db_rows_after,
        payload=vendor_result.payload,
    )


def _persist_bodygraph(db: DBAccess, user_id: str, vendor_version: int, request: VendorRequest, payload_text: str) -> int:
    stmt = Statement(
        sql="""
        INSERT INTO hde.body_graphs (user_id, vendor, vendor_version, input_fingerprint, payload)
        VALUES (%s, %s, %s, %s, %s::jsonb)
        ON CONFLICT DO NOTHING
        """,
        params=[
            user_id,
            "hdapi",
            vendor_version,
            request.input_fingerprint,
            payload_text,
        ],
        fetch=False,
    )
    try:
        db.tx([stmt])
    except AdapterError as exc:
        raise VendorError("DB_WRITER_UNAVAILABLE", "database write failed", details={"code": exc.code}) from exc
    return 0


def _row_count(db: DBAccess, user_id: str, vendor: str, vendor_version: int, fingerprint: str) -> int:
    try:
        rows = db.query(
            """
            SELECT COUNT(*)
            FROM hde.body_graphs
            WHERE user_id = %s AND vendor = %s AND vendor_version = %s AND input_fingerprint = %s
            """,
            (user_id, vendor, vendor_version, fingerprint),
        )
    except AdapterError as exc:
        raise VendorError("DB_QUERY_FAILED", "row count failed", details={"code": exc.code}) from exc
    return int(rows[0][0]) if rows else 0


def _fetch_payload(db: DBAccess, user_id: str, vendor: str, vendor_version: int, fingerprint: str) -> str:
    try:
        rows = db.query(
            """
            SELECT payload::text
            FROM hde.body_graphs
            WHERE user_id = %s AND vendor = %s AND vendor_version = %s AND input_fingerprint = %s
            """,
            (user_id, vendor, vendor_version, fingerprint),
        )
    except AdapterError as exc:
        raise VendorError("DB_QUERY_FAILED", "payload fetch failed", details={"code": exc.code}) from exc
    if not rows:
        raise VendorError("DB_PAYLOAD_MISSING", "stored payload missing", {})
    return rows[0][0]


def _idempotency_key(user_id: str, vendor: str, vendor_version: int, fingerprint: str) -> str:
    return f"{user_id}:{vendor}:{vendor_version}:{fingerprint}"
