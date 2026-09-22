"""Controlled persistence for configured-v2, adapter-mapped BodyGraph data."""
from __future__ import annotations

import json
import re
import uuid
from dataclasses import dataclass
from hashlib import sha256
from typing import Any, Mapping

from engine.db import DBAccess, Statement
from engine.db.errors import AdapterError
from engine.serializer.canon import sercanon

from .projection import BodyGraphProjectionError, CanonicalBodyGraph, project_bodygraph, strict_canonical_uuid

_FINGERPRINT = re.compile(r"^[0-9a-f]{64}$")
_EXPECTED_VENDOR = "hdapi"
_EXPECTED_POSTURE = "adapter_mapped_no_raw_vendor_payload"

# PF05 §5.1.0 read-only current-row lookup.  The vendor literal is fixed in the
# statement and only the canonical UUID is a bound parameter.
CURRENT_ROW_VIEW = "public.hde_body_graphs_current"
CURRENT_ROW_SQL = (
    "SELECT user_id, vendor, vendor_version, input_fingerprint, payload "
    f"FROM {CURRENT_ROW_VIEW} WHERE user_id = %s AND vendor = '{_EXPECTED_VENDOR}'"
)


class MappedCacheError(RuntimeError):
    """Value-free typed failure raised by the mapped-cache boundary."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        super().__init__(message)


@dataclass(frozen=True)
class MappedCacheResult:
    provider: str
    canonical_sha256: str
    rows_before: int
    rows_after: int
    rows_written: int
    read_back_match: bool
    idempotent: bool

    def as_dict(self) -> dict[str, object]:
        return {
            "provider": self.provider,
            "canonical_sha256": self.canonical_sha256,
            "rows_before": self.rows_before,
            "rows_after": self.rows_after,
            "rows_written": self.rows_written,
            "read_back_match": self.read_back_match,
            "idempotent": self.idempotent,
        }


def persist_mapped_bodygraph(db: DBAccess, cache: Mapping[str, Any]) -> MappedCacheResult:
    """Project, write, read back, and canonically verify one mapped cache row."""

    if not isinstance(cache, Mapping):
        raise MappedCacheError("PROVIDER_WRITE_UNSUPPORTED", "mapped cache input is invalid")
    required = {"user_id", "vendor", "vendor_version", "input_fingerprint", "payload_posture", "payload"}
    if set(cache) != required:
        raise MappedCacheError("PROVIDER_WRITE_UNSUPPORTED", "mapped cache metadata is invalid")
    user_id = cache["user_id"]
    try:
        normalized_user_id = str(uuid.UUID(user_id)) if isinstance(user_id, str) else ""
    except (ValueError, AttributeError):
        normalized_user_id = ""
    if not normalized_user_id or normalized_user_id != user_id.lower():
        raise MappedCacheError("PROVIDER_WRITE_UNSUPPORTED", "mapped cache user identity is invalid")
    vendor_version = cache["vendor_version"]
    if isinstance(vendor_version, bool) or not isinstance(vendor_version, int):
        raise MappedCacheError("PROVIDER_WRITE_UNSUPPORTED", "mapped cache vendor version is invalid")
    fingerprint = cache["input_fingerprint"]
    if not isinstance(fingerprint, str) or _FINGERPRINT.fullmatch(fingerprint) is None:
        raise MappedCacheError("PROVIDER_WRITE_UNSUPPORTED", "mapped cache fingerprint is invalid")
    if cache["vendor"] != _EXPECTED_VENDOR or cache["payload_posture"] != _EXPECTED_POSTURE:
        raise MappedCacheError("PROVIDER_WRITE_UNSUPPORTED", "mapped cache contract is unsupported")
    payload = cache["payload"]
    if not isinstance(payload, Mapping):
        raise MappedCacheError("PROVIDER_WRITE_UNSUPPORTED", "mapped cache payload is invalid")
    try:
        projected = project_bodygraph(payload)
    except BodyGraphProjectionError as exc:
        raise MappedCacheError("PROVIDER_WRITE_UNSUPPORTED", "mapped cache projection was refused") from exc
    canonical = sercanon(projected)
    identity = (normalized_user_id, _EXPECTED_VENDOR, vendor_version, fingerprint)
    statement = Statement(
        sql="""INSERT INTO hde.body_graphs (user_id, vendor, vendor_version, input_fingerprint, payload)
VALUES (%s, %s, %s, %s, %s::jsonb)
ON CONFLICT (user_id, vendor, vendor_version, input_fingerprint) DO NOTHING
RETURNING 1""",
        params=(*identity, canonical.decode("utf-8")),
        fetch=True,
    )
    try:
        tx_results = db.tx([statement])
    except AdapterError as exc:
        raise MappedCacheError("DB_WRITER_UNAVAILABLE", "mapped cache write failed") from exc
    if len(tx_results) != 1 or tx_results[0] is None:
        raise MappedCacheError("DB_WRITER_UNAVAILABLE", "mapped cache write result is invalid")
    inserted_rows = tx_results[0]
    if list(inserted_rows) not in ([], [(1,)]):
        raise MappedCacheError("DB_WRITER_UNAVAILABLE", "mapped cache write cardinality is invalid")
    rows_written = len(inserted_rows)
    rows_after = _count(db, identity)
    if rows_after != 1:
        raise MappedCacheError("DB_QUERY_FAILED", "mapped cache identity cardinality failed")
    stored = _read(db, identity)
    try:
        decoded = json.loads(stored) if isinstance(stored, str) else stored
        read_back = sercanon(project_bodygraph(decoded))
    except (TypeError, json.JSONDecodeError, BodyGraphProjectionError) as exc:
        raise MappedCacheError("DB_QUERY_FAILED", "mapped cache read-back is invalid") from exc
    if read_back != canonical:
        raise MappedCacheError("DB_QUERY_FAILED", "mapped cache canonical parity failed")
    return MappedCacheResult(
        provider=db.provider_name,
        canonical_sha256=sha256(canonical).hexdigest(),
        rows_before=1 - rows_written,
        rows_after=rows_after,
        rows_written=rows_written,
        read_back_match=True,
        idempotent=rows_written == 0,
    )


def _count(db: DBAccess, identity: tuple[object, ...]) -> int:
    try:
        rows = db.query("""SELECT COUNT(*) FROM hde.body_graphs
WHERE user_id = %s AND vendor = %s AND vendor_version = %s AND input_fingerprint = %s""", identity)
    except AdapterError as exc:
        raise MappedCacheError("DB_QUERY_FAILED", "mapped cache count failed") from exc
    if not rows:
        raise MappedCacheError("DB_QUERY_FAILED", "mapped cache count missing")
    return int(rows[0][0])


def _read(db: DBAccess, identity: tuple[object, ...]) -> object:
    try:
        rows = db.query("""SELECT payload::text FROM hde.body_graphs
WHERE user_id = %s AND vendor = %s AND vendor_version = %s AND input_fingerprint = %s""", identity)
    except AdapterError as exc:
        raise MappedCacheError("DB_QUERY_FAILED", "mapped cache read failed") from exc
    if len(rows) != 1:
        raise MappedCacheError("DB_PAYLOAD_MISSING", "mapped cache row missing")
    return rows[0][0]


@dataclass(frozen=True)
class MappedBodyGraphRow:
    """One current-view row whose identity is bound to the requested canonical key."""

    user_id: str
    vendor: str
    vendor_version: int
    input_fingerprint: str | None
    payload: CanonicalBodyGraph


def read_current_mapped_bodygraph(db: DBAccess, canonical_user_id: str) -> MappedBodyGraphRow | None:
    """Read one complete current BodyGraph row for a canonical UUID, or ``None``.

    Read-only: exactly one parameterized ``SELECT`` on the current view, no
    write, no vendor call and no UUID5 conversion.  A row whose identity,
    metadata or payload violates the current-view contract refuses with a
    value-free ``MappedCacheError``; an incomplete or invalid mapped payload
    surfaces the projection's own ``BodyGraphProjectionError``.
    """

    if strict_canonical_uuid(canonical_user_id) is None:
        raise MappedCacheError("PROVIDER_INPUT_INVALID", "current-row lookup requires a canonical UUID")
    try:
        rows = db.query(CURRENT_ROW_SQL, (canonical_user_id,))
    except AdapterError as exc:
        raise MappedCacheError("DB_QUERY_FAILED", "current-row lookup failed") from exc
    if rows is None:
        raise MappedCacheError("DB_QUERY_FAILED", "current-row lookup returned no result set")
    rows = list(rows)
    if not rows:
        return None
    if len(rows) != 1:
        raise MappedCacheError("DB_ROW_CONTRACT_VIOLATED", "current view returned more than one row")
    row = rows[0]
    if not isinstance(row, (list, tuple)) or len(row) != 5:
        raise MappedCacheError("DB_ROW_CONTRACT_VIOLATED", "current-row shape is invalid")
    row_user_id, vendor, vendor_version, fingerprint, payload = row
    if isinstance(row_user_id, uuid.UUID):
        row_user_id = str(row_user_id)
    if row_user_id != canonical_user_id:
        raise MappedCacheError("DB_ROW_CONTRACT_VIOLATED", "current-row identity does not match the request")
    if vendor != _EXPECTED_VENDOR:
        raise MappedCacheError("DB_ROW_CONTRACT_VIOLATED", "current-row vendor is unsupported")
    if isinstance(vendor_version, bool) or not isinstance(vendor_version, int) or vendor_version <= 0:
        raise MappedCacheError("DB_ROW_CONTRACT_VIOLATED", "current-row vendor version is invalid")
    if fingerprint is not None and (not isinstance(fingerprint, str) or _FINGERPRINT.fullmatch(fingerprint) is None):
        raise MappedCacheError("DB_ROW_CONTRACT_VIOLATED", "current-row fingerprint is invalid")
    if isinstance(payload, (str, bytes, bytearray)):
        try:
            decoded = json.loads(payload)
        except (ValueError, TypeError) as exc:
            raise MappedCacheError("DB_PAYLOAD_INVALID", "current-row payload is not JSON") from exc
    else:
        decoded = payload
    if not isinstance(decoded, Mapping):
        raise MappedCacheError("DB_PAYLOAD_INVALID", "current-row payload is not an object")
    projected = project_bodygraph(decoded)
    return MappedBodyGraphRow(
        user_id=canonical_user_id,
        vendor=_EXPECTED_VENDOR,
        vendor_version=int(vendor_version),
        input_fingerprint=fingerprint,
        payload=projected,
    )
