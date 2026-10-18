"""HDE-CRD-0002 WU-PR-04 (S14): production vendor override, HDE-CLI-API-Vendor-Ref §7.1.11.

Tables M-1 to M-8 (§7.1.11c rows) and O-1 to O-7 (§7.1.11d steps), the audit
record (§7.1.11f) and its seams. Every refusal runs with guards that fail the
test on vendor-client or database construction, a urllib request, DNS or a
socket. Every sink is a temporary path.
"""

from __future__ import annotations

import json
import os
import socket
import stat
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

import pytest

from engine.bodygraph import resolver, vendor_audit
from engine.bodygraph.resolver import resolve_bodygraph
from engine.bodygraph.vendor_client import HdApiClient, VendorError, VendorRequest, VendorResult
from engine.cli.main import cli
from engine.db import DBAccess

ROOT = Path(__file__).resolve().parents[2]
CHART = json.loads((ROOT / "tests/fixtures/bodygraph/source_invariance/vendor_chart_result.v1.json").read_text())["payload"]
REF = "PO-HDE-CRD-0002/QA:live-1"
BIRTH = {"birthdate": "1990-01-01", "birthtime": "07:41", "location": "Amsterdam, NL"}
V2_BASE = "https://vendor.example.test/v2"
V1_BASE = "https://vendor.example.test/v1"
API_KEY = "api-key-value-not-for-output"
GEO_KEY = "geo-key-value-not-for-output"
FIXED_TIME = datetime(2026, 10, 18, 12, 0, 0, 123456, tzinfo=timezone.utc)
IF2_FIELDS = {
    "schema_version", "event", "occurred_at", "correlation_id", "actor_principal", "authorization_ref",
    "command", "source", "environment", "safe_mode_open", "network_open", "route_family", "resource_path",
    "outcome", "error_code", "outbound_attempted",
}


def _fail(name):
    def _guard(*_args, **_kwargs):
        raise AssertionError(f"forbidden I/O seam reached: {name}")

    return _guard


@pytest.fixture
def no_io(monkeypatch):
    """Fail on vendor-client or DB construction, urllib requests, DNS and sockets."""

    monkeypatch.setattr(HdApiClient, "__init__", _fail("HdApiClient"))
    monkeypatch.setattr(HdApiClient, "from_env", classmethod(lambda cls, **_: _fail("HdApiClient.from_env")()))
    monkeypatch.setattr(DBAccess, "for_current_env", classmethod(lambda cls, **_: _fail("DBAccess")()))
    monkeypatch.setattr(urllib.request, "Request", _fail("urllib.request.Request"))
    monkeypatch.setattr(urllib.request, "urlopen", _fail("urllib.request.urlopen"))
    monkeypatch.setattr(socket, "getaddrinfo", _fail("socket.getaddrinfo"))
    monkeypatch.setattr(socket, "socket", _fail("socket.socket"))


@pytest.fixture
def seams(monkeypatch):
    monkeypatch.setattr(vendor_audit, "utc_now", lambda: FIXED_TIME)
    ids = iter(f"00000000-0000-4000-8000-{n:012d}" for n in range(1, 100))
    monkeypatch.setattr(vendor_audit, "new_correlation_id", lambda: next(ids))
    monkeypatch.setattr(vendor_audit, "resolve_actor_principal", lambda: "qa-operator")
    for name in ("APP_ENV", "ENGINE_ENV", vendor_audit.VENDOR_OVERRIDE_AUDIT_PATH_KEY):
        monkeypatch.delenv(name, raising=False)


class FakeClient:
    def __init__(self, error: VendorError | None = None):
        self.fetches = 0
        self.error = error

    def build_contract_route_request(self, **_kwargs):
        return VendorRequest(url=V2_BASE + "/charts", headers={"Authorization": "Bearer x"}, body_bytes=b"{}\n", input_fingerprint="a" * 64, route="vendor.hdapi.post:/charts")

    def build_request(self, **_kwargs):
        return VendorRequest(url=V1_BASE + "/bodygraphs", headers={"HD-Api-Key": "x"}, body_bytes=b"{}\n", input_fingerprint="b" * 64, route="vendor.hdapi.post:/bodygraphs")

    def fetch(self, request):
        self.fetches += 1
        if self.error is not None:
            raise self.error
        if request.route.endswith("/charts"):
            payload = {"timestamp": "2026-07-16T00:00:00Z", "success": True, "message": "Chart generated", "errorCode": "", "type": "ChartResult", "data": CHART}
        else:
            payload = {"bodygraph": {"type": "Generator"}}
        return VendorResult(payload=payload, duration_ms=1.0, attempts=1)


def _install_client(monkeypatch, client):
    monkeypatch.setattr(HdApiClient, "from_env", classmethod(lambda cls, **_: client))
    monkeypatch.setattr(DBAccess, "for_current_env", classmethod(lambda cls, **_: _fail("DBAccess")()))
    return client


def _env(tmp_path, *, app_env="prod", base=V2_BASE, safe="0", net="1", **extra):
    env = {
        "SAFE_MODE": safe,
        "ALLOW_NETWORK": net,
        "HD_API_BASE_URL": base,
        "HD_API_KEY": API_KEY,
        "GEO_API_KEY": GEO_KEY,
        vendor_audit.VENDOR_OVERRIDE_AUDIT_PATH_KEY: str(tmp_path / "state" / "override.jsonl"),
    }
    if app_env is not None:
        env["APP_ENV"] = app_env
    env.update(extra)
    return env


def _sink_lines(tmp_path):
    path = tmp_path / "state" / "override.jsonl"
    if not path.exists():
        return []
    raw = path.read_bytes()
    assert raw == b"" or raw.endswith(b"\n")
    return [json.loads(line) for line in raw.decode("utf-8").splitlines()]


def _resolve(env, *, ref=None, dry_run=True, upsert=False):
    return resolve_bodygraph("operator-user", source="vendor", upsert=upsert, dry_run=dry_run, env=env, authorization_ref=ref, **BIRTH)


def _code(result):
    return result.payload["error"]["code"]


def _assert_policy_refusal(result, code):
    assert result.status == "error" and result.exit_code == 1
    assert result.payload["error"]["code"] == code
    assert result.payload["error"]["details"] == {"outbound_attempted": False}
    assert set(result.payload) == {"status", "error", "resolver"}


# --- M-1 to M-8: the §7.1.11c matrix --------------------------------------------------------


@pytest.mark.parametrize("app_env", ["prod", "production", "live", "dev", "staging"])
@pytest.mark.parametrize("ref", [None, REF])
def test_m1_safe_mode_closed_refuses_with_existing_bytes(no_io, seams, tmp_path, app_env, ref):
    result = _resolve(_env(tmp_path, app_env=app_env, safe="1", net="0"), ref=ref)
    assert result.payload["error"] == {"code": "PROVIDER_REFUSED", "message": "Vendor source is refused under SAFE rails (SAFE_MODE=1)."}
    assert _sink_lines(tmp_path) == []


@pytest.mark.parametrize("app_env", ["prod", "live", "dev", "local"])
@pytest.mark.parametrize("ref", [None, REF])
def test_m2_network_closed_refuses_with_existing_bytes(no_io, seams, tmp_path, app_env, ref):
    result = _resolve(_env(tmp_path, app_env=app_env, safe="0", net="0"), ref=ref)
    assert result.payload["error"] == {"code": "PROVIDER_NETWORK_BLOCKED", "message": "Network disabled under current rails."}
    assert _sink_lines(tmp_path) == []


@pytest.mark.parametrize("app_env", ["prod", "production", "live", " PROD ", "Live"])
@pytest.mark.parametrize("dry_run", [True, False])
def test_m3_production_flag_absent_requires_override_and_records_refusal(no_io, seams, tmp_path, app_env, dry_run):
    result = _resolve(_env(tmp_path, app_env=app_env), dry_run=dry_run)
    _assert_policy_refusal(result, "PROVIDER_PROD_OVERRIDE_REQUIRED")
    (event,) = _sink_lines(tmp_path)
    assert event["outcome"] == "refused" and event["error_code"] == "PROVIDER_PROD_OVERRIDE_REQUIRED"
    assert event["authorization_ref"] is None and event["outbound_attempted"] is False
    assert event["route_family"] is None and event["resource_path"] is None
    assert event["environment"] == app_env.strip().lower()


def test_m3_flag_absent_result_stands_when_its_event_cannot_persist(no_io, seams, tmp_path, monkeypatch):
    (tmp_path / "state").write_text("not a directory")
    result = _resolve(_env(tmp_path))
    _assert_policy_refusal(result, "PROVIDER_PROD_OVERRIDE_REQUIRED")
    def _unavailable():
        raise vendor_audit.AuditUnavailable()

    monkeypatch.setattr(vendor_audit, "resolve_actor_principal", _unavailable)
    result = _resolve(_env(tmp_path / "other"))
    _assert_policy_refusal(result, "PROVIDER_PROD_OVERRIDE_REQUIRED")


def test_m5_valid_flag_with_unavailable_sink_refuses_before_io(no_io, seams, tmp_path):
    (tmp_path / "state").write_text("not a directory")
    result = _resolve(_env(tmp_path), ref=REF)
    _assert_policy_refusal(result, "PROVIDER_AUDIT_UNAVAILABLE")


def test_m5_valid_flag_with_unavailable_actor_refuses_before_io(no_io, seams, tmp_path, monkeypatch):
    def _unavailable():
        raise vendor_audit.AuditUnavailable()

    monkeypatch.setattr(vendor_audit, "resolve_actor_principal", _unavailable)
    result = _resolve(_env(tmp_path), ref=REF)
    _assert_policy_refusal(result, "PROVIDER_AUDIT_UNAVAILABLE")
    assert _sink_lines(tmp_path) == []


@pytest.mark.parametrize("base, family, resource", [(V2_BASE, "recommended_v2_chart", "charts"), (V1_BASE, "legacy_bodygraph", "bodygraphs")])
def test_m6_valid_auditable_flag_allows_one_bounded_read(seams, tmp_path, monkeypatch, base, family, resource):
    client = _install_client(monkeypatch, FakeClient())
    monkeypatch.setattr("engine.bodygraph.ingest._append_jsonl", lambda *_a, **_k: None)
    result = _resolve(_env(tmp_path, base=base), ref=REF)
    assert result.status == "ok" and result.exit_code == 0
    assert client.fetches == 1
    allowed, state = _sink_lines(tmp_path)
    assert allowed["outcome"] == "allowed" and allowed["outbound_attempted"] is False
    assert allowed["route_family"] is None and allowed["resource_path"] is None and allowed["error_code"] is None
    assert state["outcome"] == "completed" and state["outbound_attempted"] is True
    assert state["route_family"] == family and state["resource_path"] == resource
    assert state["correlation_id"] == allowed["correlation_id"]
    assert allowed["authorization_ref"] == state["authorization_ref"] == REF


@pytest.mark.parametrize("app_env", ["dev", "test", "local", "stage", "staging", " Dev "])
def test_m7_non_production_without_flag_keeps_current_policy(seams, tmp_path, monkeypatch, app_env):
    client = _install_client(monkeypatch, FakeClient())
    result = _resolve(_env(tmp_path, app_env=app_env))
    assert result.status == "ok" and client.fetches == 1
    assert _sink_lines(tmp_path) == []


@pytest.mark.parametrize("app_env", ["dev", "test", "local", "stage", "staging"])
def test_m8_non_production_with_flag_is_invalid(no_io, seams, tmp_path, app_env):
    result = _resolve(_env(tmp_path, app_env=app_env), ref=REF)
    _assert_policy_refusal(result, "PROVIDER_PROD_OVERRIDE_INVALID")
    assert _sink_lines(tmp_path) == []


# --- O-1 to O-7: the §7.1.11d order ---------------------------------------------------------


def _cli(*extra):
    return ["bg:resolve", "--user", "operator-user", *extra]


@pytest.mark.parametrize("argv", [
    _cli("--source", "vendor", "--allow-prod-vendor", "bad value"),
    _cli("--source", "vendor", "--allow-prod-vendor", REF, "--allow-prod-vendor", REF),
])
def test_o1_parse_errors_precede_rails_and_resolver(no_io, seams, monkeypatch, capsys, argv):
    monkeypatch.setenv("SAFE_MODE", "1")
    monkeypatch.setattr("engine.cli.main.resolve_bodygraph", _fail("resolver"))
    assert cli(argv) == 64
    captured = capsys.readouterr()
    assert captured.out == "" and "bad value" not in captured.err and REF not in captured.err


@pytest.mark.parametrize("source", [["--source", "db"], ["--source", "auto"], []])
def test_o2_non_vendor_source_is_usage_before_rails(no_io, seams, monkeypatch, capsys, source):
    monkeypatch.setattr("engine.cli.main.resolve_bodygraph", _fail("resolver"))
    assert cli(_cli(*source, "--allow-prod-vendor", REF)) == 64
    captured = capsys.readouterr()
    assert captured.out == "" and REF not in captured.err


def test_o3_rails_precede_environment_classification(no_io, seams, tmp_path, monkeypatch):
    monkeypatch.setattr(resolver, "classify_vendor_environment", _fail("classification"))
    assert _code(_resolve(_env(tmp_path, app_env="nonsense", safe="1"), ref=REF)) == "PROVIDER_REFUSED"
    assert _code(_resolve(_env(tmp_path, app_env="nonsense", net="0"), ref=REF)) == "PROVIDER_NETWORK_BLOCKED"


@pytest.mark.parametrize("extra", [
    {"APP_ENV": None},
    {"APP_ENV": "   "},
    {"APP_ENV": "development"},
    {"APP_ENV": "qa"},
    {"APP_ENV": "dev", "ENGINE_ENV": "prod"},
    {"APP_ENV": "prod", "ENGINE_ENV": "production"},
    {"APP_ENV": "", "ENGINE_ENV": "unknown"},
])
@pytest.mark.parametrize("ref", [None, REF])
def test_o4_environment_is_classified_before_the_matrix(no_io, seams, tmp_path, monkeypatch, extra, ref):
    monkeypatch.setattr(resolver, "_classify_env_route_policy", _fail("route policy"))
    env = _env(tmp_path, app_env=None)
    env.update({k: v for k, v in extra.items()})
    result = _resolve(env, ref=ref)
    _assert_policy_refusal(result, "PROVIDER_CONFIG_INVALID")
    assert _sink_lines(tmp_path) == []


@pytest.mark.parametrize("extra", [{"APP_ENV": "", "ENGINE_ENV": "prod"}, {"APP_ENV": " ", "ENGINE_ENV": " LIVE "}, {"ENGINE_ENV": "production"}])
def test_o4_engine_env_alias_applies_when_app_env_is_blank(no_io, seams, tmp_path, extra):
    env = _env(tmp_path, app_env=None)
    env.update(extra)
    _assert_policy_refusal(_resolve(env), "PROVIDER_PROD_OVERRIDE_REQUIRED")


def test_o4_process_production_environment_is_never_downgraded(no_io, seams, tmp_path, monkeypatch):
    monkeypatch.setenv("APP_ENV", "production")
    _assert_policy_refusal(_resolve(_env(tmp_path, app_env="test")), "PROVIDER_PROD_OVERRIDE_REQUIRED")
    (event,) = _sink_lines(tmp_path)
    assert event["environment"] == "production"
    monkeypatch.setenv("APP_ENV", "dev")
    monkeypatch.setenv("ENGINE_ENV", "live")
    _assert_policy_refusal(_resolve(_env(tmp_path, app_env="test", ENGINE_ENV=None)), "PROVIDER_PROD_OVERRIDE_REQUIRED")


def test_o5_matrix_precedes_actor_and_event(no_io, seams, tmp_path, monkeypatch):
    monkeypatch.setattr(vendor_audit, "resolve_actor_principal", _fail("actor"))
    monkeypatch.setattr(vendor_audit, "append_event", _fail("event"))
    _assert_policy_refusal(_resolve(_env(tmp_path, app_env="dev"), ref=REF), "PROVIDER_PROD_OVERRIDE_INVALID")


def test_o6_durable_event_precedes_step_seven(seams, tmp_path, monkeypatch):
    seen = []

    def _route_policy(env):
        seen.append(_sink_lines(tmp_path))
        raise VendorError("PROVIDER_CONFIG_MISSING", "missing vendor configuration")

    monkeypatch.setattr(resolver, "_classify_env_route_policy", _route_policy)
    result = _resolve(_env(tmp_path), ref=REF)
    assert _code(result) == "PROVIDER_CONFIG_MISSING"
    assert [event["outcome"] for event in seen[0]] == ["allowed"]
    allowed, state = _sink_lines(tmp_path)
    assert state["outcome"] == "refused" and state["error_code"] == "PROVIDER_CONFIG_MISSING"
    assert state["outbound_attempted"] is False and state["route_family"] is None


def test_o6_event_failure_blocks_step_seven(no_io, seams, tmp_path, monkeypatch):
    monkeypatch.setattr(resolver, "_classify_env_route_policy", _fail("route policy"))

    def _broken(*_a, **_k):
        raise vendor_audit.AuditUnavailable()

    monkeypatch.setattr(vendor_audit, "append_event", _broken)
    _assert_policy_refusal(_resolve(_env(tmp_path), ref=REF), "PROVIDER_AUDIT_UNAVAILABLE")


def test_o6_unpersisted_directory_entry_blocks_step_seven(no_io, seams, tmp_path, monkeypatch):
    monkeypatch.setattr(resolver, "_classify_env_route_policy", _fail("route policy"))
    _fail_directory_fsync(monkeypatch)
    _assert_policy_refusal(_resolve(_env(tmp_path), ref=REF), "PROVIDER_AUDIT_UNAVAILABLE")


@pytest.mark.parametrize("base, dry_run, upsert, message", [
    (V2_BASE, False, True, "mapped-cache persistence is refused in production-like environments"),
    (V2_BASE, True, True, "mapped-cache persistence is refused in production-like environments"),
    (V2_BASE, False, False, "v2 chart-backed mapped-cache persistence requires explicit upsert intent"),
    (V1_BASE, False, False, "BodyGraph persistence is refused in production-like environments"),
    (V1_BASE, False, True, "BodyGraph persistence is refused in production-like environments"),
    (V1_BASE, True, True, "BodyGraph persistence is refused in production-like environments"),
])
def test_o7_production_override_is_read_only_on_both_write_paths(no_io, seams, tmp_path, monkeypatch, base, dry_run, upsert, message):
    monkeypatch.setattr(resolver, "ingest_vendor_bodygraph", _fail("ingest"))
    result = _resolve(_env(tmp_path, base=base), ref=REF, dry_run=dry_run, upsert=upsert)
    assert result.payload["error"]["code"] == "PROVIDER_WRITE_UNSUPPORTED"
    assert result.payload["error"]["message"] == message
    allowed, state = _sink_lines(tmp_path)
    assert state["outcome"] == "refused" and state["error_code"] == "PROVIDER_WRITE_UNSUPPORTED"
    assert state["outbound_attempted"] is False and state["resource_path"] in {"charts", "bodygraphs"}


def test_o7_vendor_failure_after_an_attempt_is_recorded_as_failed(seams, tmp_path, monkeypatch):
    client = _install_client(monkeypatch, FakeClient(error=VendorError("PROVIDER_UNAVAILABLE", "vendor_error", details={"status": 503})))
    result = _resolve(_env(tmp_path), ref=REF)
    assert _code(result) == "PROVIDER_UNAVAILABLE" and client.fetches == 1
    _allowed, state = _sink_lines(tmp_path)
    assert state["outcome"] == "failed" and state["outbound_attempted"] is True and state["error_code"] == "PROVIDER_UNAVAILABLE"


def test_o7_state_event_failure_changes_nothing(seams, tmp_path, monkeypatch, capsys):
    _install_client(monkeypatch, FakeClient())
    original = vendor_audit.append_event
    calls = []

    def _second_fails(sink, event):
        calls.append(event["outcome"])
        if len(calls) > 1:
            raise vendor_audit.AuditUnavailable()
        original(sink, event)

    monkeypatch.setattr(vendor_audit, "append_event", _second_fails)
    result = _resolve(_env(tmp_path), ref=REF)
    assert result.status == "ok" and calls == ["allowed", "completed"]
    assert capsys.readouterr() == ("", "")


def test_production_dry_run_without_flag_refuses(no_io, seams, tmp_path):
    _assert_policy_refusal(_resolve(_env(tmp_path), dry_run=True), "PROVIDER_PROD_OVERRIDE_REQUIRED")


@pytest.mark.parametrize("ref, source", [("", "vendor"), ("bad value", "vendor"), ("-x", "vendor"), ("a" * 129, "vendor"), (123, "vendor"), (REF, "db"), (REF, "auto")])
def test_library_reference_must_be_valid_and_applicable(no_io, seams, tmp_path, ref, source):
    result = resolve_bodygraph("operator-user", source=source, upsert=False, dry_run=True, env=_env(tmp_path, safe="1"), authorization_ref=ref, **BIRTH)
    _assert_policy_refusal(result, "PROVIDER_PROD_OVERRIDE_INVALID")
    assert _sink_lines(tmp_path) == []


# --- the audit record (§7.1.11f) -----------------------------------------------------------


def test_record_has_exactly_the_if2_fields_and_canonical_lines(seams, tmp_path, monkeypatch):
    _install_client(monkeypatch, FakeClient())
    _resolve(_env(tmp_path), ref=REF)
    raw = (tmp_path / "state" / "override.jsonl").read_bytes()
    lines = raw.split(b"\n")
    assert lines[-1] == b"" and len(lines) == 3
    for line, event in zip(lines, _sink_lines(tmp_path)):
        assert set(event) == IF2_FIELDS
        assert line == json.dumps(event, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        assert event["schema_version"] == vendor_audit.VENDOR_PROD_OVERRIDE_AUDIT_SCHEMA_VERSION
        assert event["event"] == "vendor_prod_override" and event["command"] == "bg:resolve" and event["source"] == "vendor"
        assert event["safe_mode_open"] is True and event["network_open"] is True
        assert event["occurred_at"] == "2026-10-18T12:00:00.123456Z"
        assert event["actor_principal"] == "qa-operator" and event["environment"] == "prod"


def test_record_and_streams_carry_no_subject_url_or_secret(seams, tmp_path, monkeypatch, capsys):
    _install_client(monkeypatch, FakeClient())
    monkeypatch.setenv("SAFE_MODE", "0")
    monkeypatch.setenv("ALLOW_NETWORK", "1")
    monkeypatch.setenv("APP_ENV", "prod")
    for key, value in _env(tmp_path).items():
        monkeypatch.setenv(key, value)
    exit_code = cli(_cli("--source", "vendor", "--allow-prod-vendor", REF, "--dry-run", *[a for k, v in BIRTH.items() for a in (f"--{k}", v)]))
    captured = capsys.readouterr()
    assert exit_code == 0 and captured.err == ""
    assert REF not in captured.out and "qa-operator" not in captured.out and str(tmp_path) not in captured.out
    sink_text = (tmp_path / "state" / "override.jsonl").read_text()
    for forbidden in ("operator-user", *BIRTH.values(), "vendor.example.test", API_KEY, GEO_KEY, "Bearer"):
        assert forbidden not in sink_text


def test_fields_are_sanitized_against_cr_lf_and_control_bytes(tmp_path):
    event = vendor_audit.build_event(
        correlation_id="c\r\nid", actor_principal="evil\r\n{\"x\":1}\x00 ", authorization_ref=REF,
        environment="prod", outcome="refused", error_code="E\n", outbound_attempted=False,
    )
    sink = tmp_path / "s" / "audit.jsonl"
    vendor_audit.append_event(sink, event)
    raw = sink.read_bytes()
    assert raw.count(b"\n") == 1 and b"\r" not in raw and b"\x00" not in raw
    (parsed,) = [json.loads(raw)]
    assert parsed["actor_principal"] == 'evil??{"x":1}??'
    assert parsed["correlation_id"] == "c??id" and parsed["error_code"] == "E?"


def test_sink_is_created_owner_only_and_appended(tmp_path):
    sink = tmp_path / "new" / "dir" / "audit.jsonl"
    event = vendor_audit.build_event(correlation_id="c", actor_principal="a", authorization_ref=None, environment="prod", outcome="refused", error_code="X", outbound_attempted=False)
    vendor_audit.append_event(sink, event)
    vendor_audit.append_event(sink, event)
    assert stat.S_IMODE(sink.stat().st_mode) == 0o600
    assert stat.S_IMODE(sink.parent.stat().st_mode) == 0o700
    assert sink.read_bytes().count(b"\n") == 2


@pytest.mark.parametrize("make_bad", ["parent_is_file", "sink_is_directory"])
def test_unwritable_sink_is_unavailable(tmp_path, make_bad):
    if make_bad == "parent_is_file":
        (tmp_path / "p").write_text("x")
        sink = tmp_path / "p" / "audit.jsonl"
    else:
        sink = tmp_path / "audit.jsonl"
        sink.mkdir()
    event = vendor_audit.build_event(correlation_id="c", actor_principal="a", authorization_ref=None, environment="prod", outcome="refused", error_code="X", outbound_attempted=False)
    with pytest.raises(vendor_audit.AuditUnavailable):
        vendor_audit.append_event(sink, event)


def _identity(path):
    st = os.stat(path)
    return (st.st_dev, st.st_ino)


def _fail_directory_fsync(monkeypatch):
    real_fsync = os.fsync

    def _fsync(fd):
        if stat.S_ISDIR(os.fstat(fd).st_mode):
            raise OSError(5, "directory fsync failed")
        real_fsync(fd)

    monkeypatch.setattr(vendor_audit.os, "fsync", _fsync)


def test_append_persists_the_line_and_every_new_directory_entry(tmp_path, monkeypatch):
    real_fsync = os.fsync
    synced = []

    def _fsync(fd):
        st = os.fstat(fd)
        synced.append((st.st_dev, st.st_ino))
        real_fsync(fd)

    monkeypatch.setattr(vendor_audit.os, "fsync", _fsync)
    (tmp_path / "existing").mkdir()
    sink = tmp_path / "existing" / "new" / "dir" / "audit.jsonl"
    event = vendor_audit.build_event(correlation_id="c", actor_principal="a", authorization_ref=None, environment="prod", outcome="refused", error_code="X", outbound_attempted=False)
    vendor_audit.append_event(sink, event)
    # The file, then the directory holding it, then each directory that holds a created one.
    assert synced == [_identity(sink), _identity(sink.parent), _identity(sink.parent.parent), _identity(tmp_path / "existing")]
    synced.clear()
    vendor_audit.append_event(sink, event)
    assert synced == [_identity(sink), _identity(sink.parent)]


def test_directory_fsync_failure_is_unavailable(tmp_path, monkeypatch):
    _fail_directory_fsync(monkeypatch)
    sink = tmp_path / "audit.jsonl"
    event = vendor_audit.build_event(correlation_id="c", actor_principal="a", authorization_ref=None, environment="prod", outcome="refused", error_code="X", outbound_attempted=False)
    with pytest.raises(vendor_audit.AuditUnavailable):
        vendor_audit.append_event(sink, event)


def test_sink_path_rule(tmp_path, monkeypatch):
    key = vendor_audit.VENDOR_OVERRIDE_AUDIT_PATH_KEY
    assert vendor_audit.resolve_sink_path({key: str(tmp_path / "a.jsonl")}) == Path(os.path.realpath(tmp_path / "a.jsonl"))
    assert vendor_audit.resolve_sink_path({"XDG_STATE_HOME": str(tmp_path / "xdg")}) == Path(os.path.realpath(tmp_path / "xdg" / "glow-hdengine" / "vendor_prod_override.jsonl"))
    monkeypatch.setenv("HOME", str(tmp_path / "home"))
    expected = Path(os.path.realpath(tmp_path / "home" / ".local" / "state" / "glow-hdengine" / "vendor_prod_override.jsonl"))
    assert vendor_audit.resolve_sink_path({}) == expected
    assert vendor_audit.resolve_sink_path({"XDG_STATE_HOME": "relative/dir"}) == expected
    for bad in ("relative.jsonl", str(ROOT / "audit.jsonl"), str(ROOT / "artifacts" / "x.jsonl")):
        with pytest.raises(vendor_audit.AuditUnavailable):
            vendor_audit.resolve_sink_path({key: bad})


def test_actor_comes_from_the_effective_uid_not_the_environment(monkeypatch):
    import pwd

    monkeypatch.setenv("USER", "attacker")
    monkeypatch.setenv("LOGNAME", "attacker")
    monkeypatch.setenv("USERNAME", "attacker")
    assert vendor_audit.resolve_actor_principal() == pwd.getpwuid(os.geteuid()).pw_name

    def _missing(_uid):
        raise KeyError(_uid)

    monkeypatch.setattr(pwd, "getpwuid", _missing)
    with pytest.raises(vendor_audit.AuditUnavailable):
        vendor_audit.resolve_actor_principal()


def test_unknown_outcome_is_rejected():
    with pytest.raises(ValueError):
        vendor_audit.build_event(correlation_id="c", actor_principal="a", authorization_ref=None, environment="prod", outcome="maybe", error_code=None, outbound_attempted=False)
