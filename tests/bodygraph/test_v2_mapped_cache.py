from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest

from engine.bodygraph.mapped_cache import MappedCacheError, persist_mapped_bodygraph
from engine.db.errors import SqlExecError

ROOT = Path(__file__).resolve().parents[2]
PAYLOAD = json.loads((ROOT / "tests/fixtures/bodygraph/source_invariance/db_cached_payload.v1.json").read_text())["payload"]


class MemoryDB:
    provider_name = "fixture"

    def __init__(self) -> None:
        self.rows = {}
        self.statements = []
        self.fail = None

    def query(self, sql, params=None):
        if self.fail == "query":
            raise SqlExecError(code="fixture_query")
        key = tuple(params)
        if "COUNT" in sql:
            return [(int(key in self.rows),)]
        return [(self.rows[key],)] if key in self.rows else []

    def tx(self, statements):
        if self.fail == "write":
            raise SqlExecError(code="fixture_write")
        self.statements.extend(statements)
        statement = statements[0]
        key = tuple(statement.params[:4])
        self.rows.setdefault(key, statement.params[4])
        return [None]


def cache(**changes):
    value = {
        "user_id": "00000000-0000-4000-8000-000000000039",
        "vendor": "hdapi",
        "vendor_version": 2,
        "input_fingerprint": "a" * 64,
        "payload_posture": "adapter_mapped_no_raw_vendor_payload",
        "payload": copy.deepcopy(PAYLOAD),
    }
    value.update(changes)
    return value


def test_write_read_back_and_repeated_write_are_canonical_and_idempotent() -> None:
    db = MemoryDB()
    original = cache()
    snapshot = copy.deepcopy(original)
    first = persist_mapped_bodygraph(db, original)
    second = persist_mapped_bodygraph(db, original)
    assert first.rows_written == 1 and not first.idempotent
    assert second.rows_written == 0 and second.idempotent
    assert first.canonical_sha256 == second.canonical_sha256
    assert first.rows_after == second.rows_after == len(db.rows) == 1
    assert original == snapshot
    statement = db.statements[0]
    assert "INSERT INTO hde.body_graphs" in statement.sql
    assert "ON CONFLICT (user_id, vendor, vendor_version, input_fingerprint) DO NOTHING" in statement.sql
    assert statement.params[:4] == tuple(cache()[key] for key in ("user_id", "vendor", "vendor_version", "input_fingerprint"))
    stored = json.loads(statement.params[4])
    assert set(stored) == {"bodygraph", "person", "person_uid"}


@pytest.mark.parametrize("value", ["not-a-uuid", "", None])
def test_uuid_is_not_derived(value) -> None:
    with pytest.raises(MappedCacheError, match="identity"):
        persist_mapped_bodygraph(MemoryDB(), cache(user_id=value))


@pytest.mark.parametrize("value", [True, "2", 2.0])
def test_vendor_version_must_be_integer_not_boolean(value) -> None:
    with pytest.raises(MappedCacheError, match="version"):
        persist_mapped_bodygraph(MemoryDB(), cache(vendor_version=value))


@pytest.mark.parametrize("value", ["A" * 64, "a" * 63, "g" * 64])
def test_fingerprint_is_exact_lowercase_sha256(value) -> None:
    with pytest.raises(MappedCacheError, match="fingerprint"):
        persist_mapped_bodygraph(MemoryDB(), cache(input_fingerprint=value))


@pytest.mark.parametrize("key", ["request", "response", "transport", "header", "secret", "credential", "authorization"])
def test_raw_envelope_and_secret_like_fields_are_rejected(key) -> None:
    payload = copy.deepcopy(PAYLOAD)
    payload[key] = {"unsafe": True}
    with pytest.raises(MappedCacheError) as exc:
        persist_mapped_bodygraph(MemoryDB(), cache(payload=payload))
    assert exc.value.code == "PROVIDER_WRITE_UNSUPPORTED"


@pytest.mark.parametrize("payload", [{"type": "ChartResult", "data": {}}, {"success": True, "data": {}}, [], "raw"])
def test_unprojected_vendor_shapes_are_rejected(payload) -> None:
    with pytest.raises(MappedCacheError):
        persist_mapped_bodygraph(MemoryDB(), cache(payload=payload))


def test_typed_write_read_missing_and_parity_failures() -> None:
    db = MemoryDB(); db.fail = "write"
    with pytest.raises(MappedCacheError) as exc:
        persist_mapped_bodygraph(db, cache())
    assert exc.value.code == "DB_WRITER_UNAVAILABLE"
    db = MemoryDB(); db.fail = "query"
    with pytest.raises(MappedCacheError) as exc:
        persist_mapped_bodygraph(db, cache())
    assert exc.value.code == "DB_QUERY_FAILED"
    db = MemoryDB()
    original_query = db.query
    def missing(sql, params=None):
        if "payload::text" in sql: return []
        return original_query(sql, params)
    db.query = missing
    with pytest.raises(MappedCacheError) as exc:
        persist_mapped_bodygraph(db, cache())
    assert exc.value.code == "DB_PAYLOAD_MISSING"


def test_exact_metadata_and_supported_contract_are_required() -> None:
    for changed in ({"vendor": "other"}, {"payload_posture": "raw"}, {"extra": True}):
        with pytest.raises(MappedCacheError):
            persist_mapped_bodygraph(MemoryDB(), cache(**changed))
