"""HDE-EPIC040-PR05: the read-only current-row Magic-10 Gate-readiness tool.

Every run uses the PR04 current-view DB fake (or a variant of it); no database,
vendor or network is reached, and nothing is written.
"""
from __future__ import annotations

import ast
import contextlib
import errno
import hashlib
import importlib
import json
import os
import signal
from pathlib import Path

import pytest

from ci.checks import classify_ci_changes as classifier
from engine.bodygraph import mapped_cache
from engine.bodygraph import resolver
from engine.bodygraph import vendor_client
from engine.compat.error_tokens import CompatBoundaryError
from engine.config.registry_loader import _load_active_mechanics_bundle_from_root, _parse_release_member_bytes
from engine.db import DBAccess
from engine.db.errors import PrimaryUnavailable, SqlExecError
from engine.serializer.canon import sercanon
from tests.config.helpers import synthetic_complete_release_root
from tests.support.pr04_fixtures import FakeCurrentViewDB, complete_chart
from tools.bodygraph import check_magic10_gate_readiness as readiness

ROOT = Path(__file__).resolve().parents[2]
TOOL_PATH = "tools/bodygraph/check_magic10_gate_readiness.py"
THIS_TEST = "tests/bodygraph/test_check_magic10_gate_readiness.py"
UUID_A = "00000000-0000-0000-0000-00000000000a"
UUID_B = "00000000-0000-0000-0000-00000000000b"
UUID_C = "00000000-0000-0000-0000-00000000000c"
GATES_A = ["10", "20", "34"]
REPORT_KEYS = {"schema", "readiness", "provider", "read_only", "selection", "counts", "diagnostics"}
FORBIDDEN_STRINGS = (UUID_A, UUID_B, UUID_C, "birthDateUtc", "\"gates\":", "bodygraph", "Emotional", "2000-01-01",
                     "DATABASE_URL", "postgres://", "[10", "\"10\"", "person_uid", "example.invalid")
ALLOWED_IMPORT_ROOTS = {"__future__", "argparse", "hashlib", "os", "stat", "sys", "collections", "dataclasses", "pathlib", "typing",
                        "engine.bodygraph.mapped_cache", "engine.bodygraph.projection", "engine.db",
                        "engine.db.errors", "engine.runtime.determinism_env", "engine.serializer.canon"}
FORBIDDEN_IMPORTS = ("engine.bodygraph.resolver", "engine.bodygraph.vendor_client", "engine.bodygraph.ingest",
                     "psycopg", "persist_mapped_bodygraph", "requests", "urllib", "subprocess", "json")


class RowVariantDB(FakeCurrentViewDB):
    """The PR04 fake plus per-user raw-row overrides for the adverse matrix."""

    def __init__(self, charts=None, *, rows=None, fail_on=None, none_on=None):
        super().__init__(charts)
        self.rows = dict(rows or {})
        self.fail_on = fail_on
        self.none_on = none_on

    def query(self, sql, params=None):
        uid = params[0]
        if uid == self.fail_on:
            self.queries.append((sql, tuple(params)))
            raise SqlExecError("sql_query_failed", attempts=["DATABASE_URL"], code="sql_query_failed")
        if uid == self.none_on:
            self.queries.append((sql, tuple(params)))
            return None
        if uid in self.rows:
            self.queries.append((sql, tuple(params)))
            return self.rows[uid]
        return super().query(sql, params)


@pytest.fixture(autouse=True)
def _rails_and_spies(monkeypatch):
    for key, value in {"LC_ALL": "C", "LANG": "C", "TZ": "UTC", "SAFE_MODE": "1", "ALLOW_NETWORK": "0", "APP_ENV": "dev"}.items():
        monkeypatch.setenv(key, value)
    monkeypatch.delenv("DATABASE_URL", raising=False)
    for name in ("DB_ALLOW_BRIDGE_IN_PROD", "DB_BRIDGE_URL", "DB_FORCE_BRIDGE"):
        monkeypatch.delenv(name, raising=False)
    monkeypatch.setattr(resolver.HdApiClient, "from_env", lambda **kwargs: pytest.fail("vendor client constructed"))
    monkeypatch.setattr(resolver, "ingest_vendor_bodygraph", lambda *a, **k: pytest.fail("ingest attempted"))
    monkeypatch.setattr(resolver, "persist_mapped_bodygraph", lambda *a, **k: pytest.fail("mapped-cache write attempted"))
    monkeypatch.setattr(mapped_cache, "persist_mapped_bodygraph", lambda *a, **k: pytest.fail("mapped-cache write attempted"))
    monkeypatch.setattr(vendor_client.HdApiClient, "__init__", lambda self, *a, **k: pytest.fail("vendor client constructed"))


def _use(monkeypatch, fake) -> None:
    monkeypatch.setattr(readiness.DBAccess, "for_current_env", classmethod(lambda cls, *a, **k: fake))


def _run(argv, capfdbinary):
    code = readiness.main(argv)
    out, err = capfdbinary.readouterr()
    return code, out, err


def _good_db(*uids):
    return RowVariantDB({uid: complete_chart(uid, GATES_A) for uid in uids})


def _row(uid, chart=None, *, vendor="hdapi", version=2, fingerprint="a" * 64, payload=None):
    body = json.dumps(chart if chart is not None else complete_chart(uid, GATES_A), sort_keys=True) if payload is None else payload
    return [(uid, vendor, version, fingerprint, body)]


def _assert_no_leak(*streams: bytes) -> None:
    for stream in streams:
        text = stream.decode("utf-8")
        for forbidden in FORBIDDEN_STRINGS:
            assert forbidden not in text, forbidden


# --- ready and not-ready reports --------------------------------------------------------

def test_good_rows_are_ready_with_identity_safe_aggregate_report(monkeypatch, capfdbinary) -> None:
    fake = _good_db(UUID_A, UUID_B)
    _use(monkeypatch, fake)
    code, out, err = _run(["--user-id", UUID_B, "--user-id", UUID_A], capfdbinary)
    assert (code, err) == (0, b"") and out.endswith(b"\n") and out.count(b"\n") == 1
    report = json.loads(out)
    assert set(report) == REPORT_KEYS and report["schema"] == readiness.REPORT_SCHEMA
    assert report["readiness"] == "READY" and report["read_only"] is True
    assert report["counts"] == {"ready": 2, "missing": 0, "duplicate": 0, "row_invalid": 0, "payload_invalid": 0, "gates_invalid": 0}
    assert report["diagnostics"] == [] and report["selection"]["requested"] == 2
    assert report["selection"]["sha256"] == hashlib.sha256(sercanon(sorted([UUID_A, UUID_B]))).hexdigest()
    assert out == sercanon(json.loads(out), sort_keys=True)
    assert [params for _sql, params in fake.queries] == [(UUID_A,), (UUID_B,)]
    _assert_no_leak(out, err)


@pytest.mark.parametrize(
    ("label", "rows", "bucket", "code"),
    [
        ("empty_gates", lambda: _row(UUID_B, complete_chart(UUID_B, [])), "gates_invalid", "GATES_EMPTY"),
        ("duplicate_gate", lambda: _row(UUID_B, complete_chart(UUID_B, ["10", "10"])), "gates_invalid", "GATE_DUPLICATE"),
        ("bool_gate", lambda: _row(UUID_B, complete_chart(UUID_B, [True])), "gates_invalid", "GATE_VALUE_INVALID"),
        ("zero_gate", lambda: _row(UUID_B, complete_chart(UUID_B, [0])), "gates_invalid", "GATE_VALUE_INVALID"),
        ("gate_65", lambda: _row(UUID_B, complete_chart(UUID_B, [65])), "gates_invalid", "GATE_VALUE_INVALID"),
        ("leading_zero", lambda: _row(UUID_B, complete_chart(UUID_B, ["01"])), "gates_invalid", "GATE_VALUE_INVALID"),
        ("gates_not_list", lambda: _row(UUID_B, {**complete_chart(UUID_B, GATES_A), "bodygraph": {**complete_chart(UUID_B, GATES_A)["bodygraph"], "gates": "10"}}), "gates_invalid", "GATES_NOT_LIST"),
        ("wrong_vendor", lambda: _row(UUID_B, vendor="other"), "row_invalid", "DB_ROW_CONTRACT_VIOLATED"),
        ("bool_version", lambda: _row(UUID_B, version=True), "row_invalid", "DB_ROW_CONTRACT_VIOLATED"),
        ("bad_fingerprint", lambda: _row(UUID_B, fingerprint="zz"), "row_invalid", "DB_ROW_CONTRACT_VIOLATED"),
        ("identity_mismatch", lambda: [(UUID_C, "hdapi", 2, "a" * 64, json.dumps(complete_chart(UUID_B, GATES_A)))], "row_invalid", "DB_ROW_CONTRACT_VIOLATED"),
        ("payload_not_json", lambda: _row(UUID_B, payload="{"), "payload_invalid", "DB_PAYLOAD_INVALID"),
        ("payload_not_object", lambda: _row(UUID_B, payload="[]"), "payload_invalid", "DB_PAYLOAD_INVALID"),
        ("payload_missing_keys", lambda: _row(UUID_B, payload=json.dumps({"bodygraph": complete_chart(UUID_B, GATES_A)["bodygraph"]})), "payload_invalid", None),
        ("person_uid_mismatch", lambda: _row(UUID_B, {**complete_chart(UUID_B, GATES_A), "person_uid": UUID_C}), "payload_invalid", None),
        ("payload_names_another_uuid", lambda: _row(UUID_B, complete_chart(UUID_C, GATES_A)), "payload_invalid", "IDENTITY_CONFLICT"),
        ("payload_names_another_label", lambda: _row(UUID_B, complete_chart("person-" + UUID_C, GATES_A)), "payload_invalid", "IDENTITY_CONFLICT"),
        ("payload_names_a_non_uuid", lambda: _row(UUID_B, complete_chart("someone-else", GATES_A)), "payload_invalid", "IDENTITY_CONFLICT"),
        ("duplicate_rows", lambda: _row(UUID_B) + _row(UUID_B), "duplicate", "DB_ROW_CONTRACT_VIOLATED"),
    ],
)
def test_bad_rows_are_counted_without_a_false_ready(monkeypatch, capfdbinary, label, rows, bucket, code) -> None:
    fake = RowVariantDB({UUID_A: complete_chart(UUID_A, GATES_A)}, rows={UUID_B: rows()})
    _use(monkeypatch, fake)
    exit_code, out, err = _run(["--user-id", UUID_A, "--user-id", UUID_B], capfdbinary)
    assert (exit_code, err) == (0, b"")
    report = json.loads(out)
    assert report["readiness"] == "NOT_READY"
    expected_counts = {"ready": 1, "missing": 0, "duplicate": 0, "row_invalid": 0, "payload_invalid": 0, "gates_invalid": 0}
    expected_counts[bucket] += 1
    assert report["counts"] == expected_counts
    assert len(report["diagnostics"]) == 1 and report["diagnostics"][0]["count"] == 1
    if code is not None:
        assert report["diagnostics"][0]["code"] == code
    else:
        assert report["diagnostics"][0]["code"] not in {"GATES_NOT_LIST", "GATES_EMPTY", "GATE_VALUE_INVALID", "GATE_DUPLICATE"}
    _assert_no_leak(out, err)
    assert fake.writes == []


def test_missing_row_is_not_ready_and_mixed_diagnostics_are_sorted(monkeypatch, capfdbinary) -> None:
    fake = RowVariantDB({UUID_A: complete_chart(UUID_A, GATES_A)}, rows={UUID_C: _row(UUID_C, complete_chart(UUID_C, [0]))})
    _use(monkeypatch, fake)
    code, out, err = _run(["--user-id", UUID_C, "--user-id", UUID_B, "--user-id", UUID_A], capfdbinary)
    assert (code, err) == (0, b"")
    report = json.loads(out)
    assert report["readiness"] == "NOT_READY"
    assert report["counts"] == {"ready": 1, "missing": 1, "duplicate": 0, "row_invalid": 0, "payload_invalid": 0, "gates_invalid": 1}
    assert report["diagnostics"] == [{"code": "GATE_VALUE_INVALID", "count": 1}]
    assert [params for _sql, params in fake.queries] == [(UUID_A,), (UUID_B,), (UUID_C,)]


@pytest.mark.parametrize(("label", "ready"), [
    (UUID_B, True),
    ("person-" + UUID_B, True),
    (UUID_B.upper(), True),
    (UUID_C, False),
    ("person-" + UUID_C, False),
    ("someone-else", False),
], ids=["same_uuid", "person_label_same", "other_spelling_same", "other_uuid", "person_label_other", "non_uuid_label"])
def test_a_row_is_ready_exactly_when_the_reader_resolves_it(label, ready) -> None:
    # The route's own resolution call over the same current row (adapter/http_reader.py).
    fake = RowVariantDB(rows={UUID_B: _row(UUID_B, complete_chart(label, GATES_A))})
    report = readiness.observe(fake, (UUID_B,))
    rows = {UUID_B: mapped_cache.read_current_mapped_bodygraph(fake, UUID_B)}
    if ready:
        resolved = resolver.resolve_compat_chart({"user_id": UUID_B}, source_policy="local", env=None, local_lookup=rows.get)
        assert resolved.canonical_person_id == UUID_B
        assert (report.readiness, report.counts["ready"], report.diagnostics) == ("READY", 1, ())
    else:
        with pytest.raises(CompatBoundaryError) as refused:
            resolver.resolve_compat_chart({"user_id": UUID_B}, source_policy="local", env=None, local_lookup=rows.get)
        assert (refused.value.reason, refused.value.detail) == ("identity_conflict", "IDENTITY_CONFLICT")
        assert (report.readiness, report.counts["ready"], report.counts["payload_invalid"]) == ("NOT_READY", 0, 1)
        assert report.diagnostics == (("IDENTITY_CONFLICT", 1),)


def _deep_list(depth):
    value = []
    for _ in range(depth):
        value = [value]
    return value


@pytest.mark.parametrize("form", ["decoded", "text"])
def test_a_payload_nested_past_the_recursion_limit_is_payload_invalid(monkeypatch, capfdbinary, form) -> None:
    chart = complete_chart(UUID_A, GATES_A)
    if form == "decoded":
        chart["bodygraph"]["authority"] = _deep_list(5000)
        payload = chart
    else:
        chart["bodygraph"]["authority"] = "__deep__"
        payload = json.dumps(chart, sort_keys=True).replace('"__deep__"', "[" * 5000 + "]" * 5000)
    fake = RowVariantDB({UUID_B: complete_chart(UUID_B, GATES_A)}, rows={UUID_A: [(UUID_A, "hdapi", 2, "a" * 64, payload)]})
    _use(monkeypatch, fake)
    code, out, err = _run(["--user-id", UUID_B, "--user-id", UUID_A], capfdbinary)
    assert (code, err) == (0, b"")
    report = json.loads(out)
    assert report["readiness"] == "NOT_READY"
    assert report["counts"] == {"ready": 1, "missing": 0, "duplicate": 0, "row_invalid": 0, "payload_invalid": 1, "gates_invalid": 0}
    assert report["diagnostics"] == [{"code": "DB_PAYLOAD_INVALID", "count": 1}]
    assert [params for _sql, params in fake.queries] == [(UUID_A,), (UUID_B,)]  # the row after it is still read
    _assert_no_leak(out, err)


def test_duplicate_row_message_is_pinned_against_mapped_cache() -> None:
    fake = RowVariantDB(rows={UUID_A: _row(UUID_A) + _row(UUID_A)})
    with pytest.raises(mapped_cache.MappedCacheError) as raised:
        mapped_cache.read_current_mapped_bodygraph(fake, UUID_A)
    assert raised.value.code == "DB_ROW_CONTRACT_VIOLATED" and str(raised.value) == readiness.DUPLICATE_ROW_MESSAGE


# --- selection refusals -----------------------------------------------------------------

def test_empty_selection_refuses_before_any_query(monkeypatch, capfdbinary, tmp_path) -> None:
    fake = _good_db(UUID_A)
    _use(monkeypatch, fake)
    assert _run([], capfdbinary) == (readiness.REFUSAL_EXIT_CODE, b"", b"READINESS_EMPTY_SELECTION\n")
    selection = tmp_path / "selection.txt"
    selection.write_text("\n# only a comment\n\n", encoding="utf-8")
    assert _run(["--selection-file", str(selection)], capfdbinary) == (readiness.REFUSAL_EXIT_CODE, b"", b"READINESS_EMPTY_SELECTION\n")
    assert fake.queries == []


@pytest.mark.parametrize("argv", [
    ["--user-id", UUID_A.upper()],
    ["--user-id", "person-x"],
    ["--user-id", UUID_A, "--user-id", UUID_A],
    ["--user-id", "00000000000000000000000000000001"],
    ["--user-id", ""],
    ["--selection-file", ""],
])
def test_invalid_selection_refuses_before_any_query(monkeypatch, capfdbinary, argv) -> None:
    fake = _good_db(UUID_A)
    _use(monkeypatch, fake)
    assert _run(argv, capfdbinary) == (readiness.REFUSAL_EXIT_CODE, b"", b"READINESS_SELECTION_INVALID\n")
    assert fake.queries == []


def test_selection_file_and_flags_combine_sorted_and_deduplicated_checked(monkeypatch, capfdbinary, tmp_path) -> None:
    fake = _good_db(UUID_A, UUID_B, UUID_C)
    _use(monkeypatch, fake)
    selection = tmp_path / "selection.txt"
    selection.write_text(f"# people\n{UUID_C}\n\n{UUID_A}\n", encoding="utf-8")
    code, out, _ = _run(["--user-id", UUID_B, "--selection-file", str(selection)], capfdbinary)
    assert code == 0 and json.loads(out)["counts"]["ready"] == 3
    assert [params for _sql, params in fake.queries] == [(UUID_A,), (UUID_B,), (UUID_C,)]
    selection.write_text(f"{UUID_A}\n{UUID_A}\n", encoding="utf-8")
    assert _run(["--selection-file", str(selection)], capfdbinary)[2] == b"READINESS_SELECTION_INVALID\n"


def test_unreadable_selection_file_refuses_before_any_database_access(monkeypatch, capfdbinary, tmp_path) -> None:
    monkeypatch.setattr(readiness.DBAccess, "for_current_env", classmethod(lambda cls, *a, **k: pytest.fail("database reached")))
    not_utf8 = tmp_path / "latin1.txt"
    not_utf8.write_bytes(b"\xff" + UUID_A.encode("ascii") + b"\n")
    denied = tmp_path / "denied.txt"
    denied.write_text(f"{UUID_A}\n", encoding="utf-8")
    real_open = os.open

    def guarded_open(path, flags, *args, **kwargs):
        if Path(path) == denied:  # root can read anything, so the permission failure is injected
            raise PermissionError(errno.EACCES, "Permission denied", str(path))
        return real_open(path, flags, *args, **kwargs)

    monkeypatch.setattr(readiness.os, "open", guarded_open)
    for path in (tmp_path / "absent.txt", tmp_path, not_utf8, denied):
        code, out, err = _run(["--selection-file", str(path)], capfdbinary)
        assert (code, out, err) == (readiness.REFUSAL_EXIT_CODE, b"", b"READINESS_SELECTION_INVALID\n"), path


class _Blocked(Exception):
    """Raised by the test deadline; deliberately not an ``OSError``, so no handler absorbs it."""


@contextlib.contextmanager
def _deadline(seconds):
    def expire(signum, frame):
        raise _Blocked("reading the selection file blocked")

    previous = signal.signal(signal.SIGALRM, expire)
    signal.alarm(seconds)
    try:
        yield
    finally:
        signal.alarm(0)
        signal.signal(signal.SIGALRM, previous)


def _open_descriptors() -> set[str]:
    return set(os.listdir("/proc/self/fd"))


# Every refusal also closes the descriptor it opened: a directory is opened like the
# others and refused on the opened descriptor.
@pytest.mark.parametrize("kind", ["fifo", "device", "directory", "symlink", "oversized"])
def test_special_symlinked_or_oversized_selection_files_refuse_before_any_read(monkeypatch, capfdbinary, tmp_path, kind) -> None:
    monkeypatch.setattr(readiness.DBAccess, "for_current_env", classmethod(lambda cls, *a, **k: pytest.fail("database reached")))
    regular = tmp_path / "selection.txt"
    regular.write_text(f"{UUID_A}\n", encoding="utf-8")
    if kind == "fifo":
        path = tmp_path / "selection.fifo"
        os.mkfifo(path)  # no writer: a blocking open or read would never return
    elif kind == "device":
        path = Path(os.devnull)  # a character device, which reads as empty
    elif kind == "directory":
        path = tmp_path
    elif kind == "symlink":
        path = tmp_path / "selection.link"
        path.symlink_to(regular)
    else:
        path = tmp_path / "selection.big"
        path.write_bytes(f"{UUID_A}\n#".encode("ascii") + b"x" * readiness.SELECTION_FILE_MAX_BYTES)
    before = _open_descriptors()
    with _deadline(2):
        result = _run(["--selection-file", str(path)], capfdbinary)
    assert result == (readiness.REFUSAL_EXIT_CODE, b"", b"READINESS_SELECTION_INVALID\n")
    assert _open_descriptors() == before


def test_selection_file_at_the_size_bound_is_read(monkeypatch, capfdbinary, tmp_path) -> None:
    assert readiness.SELECTION_FILE_MAX_BYTES == 1_048_576
    fake = _good_db(UUID_A)
    _use(monkeypatch, fake)
    head = f"{UUID_A}\n#".encode("ascii")
    path = tmp_path / "selection.txt"
    path.write_bytes(head + b"x" * (readiness.SELECTION_FILE_MAX_BYTES - len(head) - 1) + b"\n")
    assert path.stat().st_size == readiness.SELECTION_FILE_MAX_BYTES
    code, out, err = _run(["--selection-file", str(path)], capfdbinary)
    assert (code, err) == (0, b"") and json.loads(out)["counts"]["ready"] == 1
    assert [params for _sql, params in fake.queries] == [(UUID_A,)]


# --- unavailable or denied datasets never become ready ----------------------------------

# Closed rails (AGENTS.md): outside them the tool refuses before reading the selection or
# constructing a database provider, and names only the unmet pins' required values.
@pytest.mark.parametrize("change, unmet", [
    ({"SAFE_MODE": "0"}, [("SAFE_MODE", "1")]),
    ({"ALLOW_NETWORK": "1"}, [("ALLOW_NETWORK", "0")]),
    ({"TZ": None}, [("TZ", "UTC")]),
    ({"LC_ALL": "en_US.UTF-8", "LANG": None}, [("LANG", "C"), ("LC_ALL", "C")]),
], ids=["safe_mode_open", "network_allowed", "tz_unset", "locale_unpinned"])
def test_open_or_unpinned_rails_refuse_before_any_database_access(monkeypatch, capfdbinary, tmp_path, change, unmet) -> None:
    for key, value in change.items():
        if value is None:
            monkeypatch.delenv(key, raising=False)
        else:
            monkeypatch.setenv(key, value)
    monkeypatch.setenv("DATABASE_URL", "postgres://example.invalid/db")
    monkeypatch.setattr(readiness.DBAccess, "for_current_env", classmethod(lambda cls, *a, **k: pytest.fail("database reached")))
    expected = (readiness.REFUSAL_EXIT_CODE, b"", f"RAILS_CLOSED_REQUIRED:{unmet}\n".encode())
    code, out, err = _run(["--user-id", UUID_A], capfdbinary)
    assert (code, out, err) == expected
    _assert_no_leak(out, err)
    assert _run([], capfdbinary) == expected
    assert _run(["--selection-file", str(tmp_path / "missing.txt")], capfdbinary) == expected


def test_missing_database_url_is_unavailable_without_a_connection(monkeypatch, capfdbinary) -> None:
    monkeypatch.setattr("engine.db.adapter.PsycopgProvider", lambda *a, **k: pytest.fail("provider constructed"))
    assert _run(["--user-id", UUID_A], capfdbinary) == (readiness.REFUSAL_EXIT_CODE, b"", b"READINESS_UNAVAILABLE\n")


def test_retired_bridge_key_is_unavailable_without_a_connection(monkeypatch, capfdbinary) -> None:
    monkeypatch.setenv("DATABASE_URL", "postgres://example.invalid/db")
    monkeypatch.setenv("DB_BRIDGE_URL", "http://example.invalid")
    monkeypatch.setattr("engine.db.adapter.PsycopgProvider", lambda *a, **k: pytest.fail("provider constructed"))
    code, out, err = _run(["--user-id", UUID_A], capfdbinary)
    assert (code, out, err) == (readiness.REFUSAL_EXIT_CODE, b"", b"READINESS_UNAVAILABLE\n")
    _assert_no_leak(out, err)


def test_connect_failure_is_unavailable(monkeypatch, capfdbinary) -> None:
    def refuse(cls, *a, **k):
        raise PrimaryUnavailable("primary_connect_failed", attempts=["DATABASE_URL"], code="primary_connect_failed")

    monkeypatch.setattr(readiness.DBAccess, "for_current_env", classmethod(refuse))
    assert _run(["--user-id", UUID_A], capfdbinary) == (readiness.REFUSAL_EXIT_CODE, b"", b"READINESS_UNAVAILABLE\n")


def test_query_failure_mid_selection_aborts_without_partial_report(monkeypatch, capfdbinary) -> None:
    fake = RowVariantDB({UUID_A: complete_chart(UUID_A, GATES_A), UUID_C: complete_chart(UUID_C, GATES_A)}, fail_on=UUID_B)
    _use(monkeypatch, fake)
    assert _run(["--user-id", UUID_C, "--user-id", UUID_A, "--user-id", UUID_B], capfdbinary) == (
        readiness.REFUSAL_EXIT_CODE, b"", b"READINESS_UNAVAILABLE\n")
    assert [params for _sql, params in fake.queries] == [(UUID_A,), (UUID_B,)]


def test_missing_result_set_is_unavailable(monkeypatch, capfdbinary) -> None:
    fake = RowVariantDB({UUID_A: complete_chart(UUID_A, GATES_A)}, none_on=UUID_A)
    _use(monkeypatch, fake)
    assert _run(["--user-id", UUID_A], capfdbinary) == (readiness.REFUSAL_EXIT_CODE, b"", b"READINESS_UNAVAILABLE\n")


# --- read-only proof, determinism and streams --------------------------------------------

def test_lookup_is_the_parameterized_read_only_current_row_statement(monkeypatch, capfdbinary) -> None:
    fake = _good_db(UUID_A, UUID_B)
    _use(monkeypatch, fake)
    assert _run(["--user-id", UUID_A, "--user-id", UUID_B], capfdbinary)[0] == 0
    assert [params for _sql, params in fake.queries] == [(UUID_A,), (UUID_B,)]
    for sql, _params in fake.queries:
        assert sql == mapped_cache.CURRENT_ROW_SQL
        assert "public.hde_body_graphs_current" in sql and "vendor = 'hdapi'" in sql and sql.count("%s") == 1
        assert not any(verb in sql.upper() for verb in ("INSERT", "UPDATE", "DELETE", "CALL"))
    assert fake.writes == [] and not hasattr(fake, "readonly_tx")


def test_two_runs_are_byte_identical(monkeypatch, capfdbinary) -> None:
    fake = RowVariantDB({UUID_A: complete_chart(UUID_A, GATES_A)}, rows={UUID_B: _row(UUID_B, complete_chart(UUID_B, []))})
    _use(monkeypatch, fake)
    first = _run(["--user-id", UUID_B, "--user-id", UUID_A], capfdbinary)
    second = _run(["--user-id", UUID_A, "--user-id", UUID_B], capfdbinary)
    assert first == second and first[0] == 0


def test_usage_errors_keep_the_parser_exit_and_never_exit_three(capfdbinary) -> None:
    with pytest.raises(SystemExit) as raised:
        readiness.main(["--unknown"])
    assert raised.value.code == 2
    capfdbinary.readouterr()
    assert readiness.REFUSAL_EXIT_CODE == 5 and 3 not in {0, 2, readiness.REFUSAL_EXIT_CODE}


# --- import purity, member format and synthetic release coherence ------------------------

def test_module_imports_only_read_paths_and_is_a_valid_release_member(monkeypatch) -> None:
    raw = (ROOT / TOOL_PATH).read_bytes()
    tree = ast.parse(raw.decode("utf-8"))
    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imported.add(node.module or "")
    assert imported <= ALLOWED_IMPORT_ROOTS, imported - ALLOWED_IMPORT_ROOTS
    text = raw.decode("utf-8")
    for forbidden in FORBIDDEN_IMPORTS:
        assert forbidden not in text, forbidden
    assert _parse_release_member_bytes(raw, TOOL_PATH) is None
    assert raw.endswith(b"\n") and not raw.endswith(b"\n\n") and b"\r" not in raw
    monkeypatch.setattr(DBAccess, "for_current_env", classmethod(lambda cls, *a, **k: pytest.fail("connected at import")))
    importlib.reload(readiness)


def test_synthetic_release_copies_the_real_tool_and_still_admits(tmp_path) -> None:
    root = synthetic_complete_release_root(tmp_path)
    assert (root / TOOL_PATH).read_bytes() == (ROOT / TOOL_PATH).read_bytes()
    bundle = _load_active_mechanics_bundle_from_root(root)
    assert TOOL_PATH in {identity.path for identity in bundle.source_identities}
    assert bundle.mechanics["config_id"] == "m10-channel-state-v1.0.0"


# --- classifier ownership guard ---------------------------------------------------------

def test_classifier_owns_the_readiness_tool_and_fails_closed_for_siblings() -> None:
    assert classifier._lanes_for_path(TOOL_PATH) == {"db", "product", "release"}
    assert THIS_TEST in classifier.changed_test_targets(ROOT, [TOOL_PATH])
    assert THIS_TEST in classifier._full_validation_test_targets()
    result = classifier.classify_paths([TOOL_PATH])
    assert {lane for lane in classifier.LANES if result.flags[lane]} == {"db", "product", "release"}
    with pytest.raises(ValueError, match="CI_BODYGRAPH_TOOL_OWNER_TEST_MISSING:tools/bodygraph/other.py"):
        classifier.changed_test_targets(ROOT, ["tools/bodygraph/other.py"])
    assert classifier._bodygraph_tool_owner_targets(ROOT, "tools/bodygraph/README.md") == ()


# CR-18: every unregistered source suffix under the prefix fails closed, not only ``.py``;
# the prefix's lane mapping would otherwise give a shell or SQL tool no changed tests.
@pytest.mark.parametrize("suffix", [".py", ".sh", ".sql"], ids=["py", "sh", "sql"])
def test_every_unregistered_bodygraph_source_fails_closed(suffix) -> None:
    assert suffix in classifier._UNKNOWN_SOURCE_SUFFIXES
    path = f"tools/bodygraph/other{suffix}"
    assert classifier._lanes_for_path(path) == {"db", "product", "release"}
    with pytest.raises(ValueError, match=f"CI_BODYGRAPH_TOOL_OWNER_TEST_MISSING:{path}$"):
        classifier.changed_test_targets(ROOT, [path])
