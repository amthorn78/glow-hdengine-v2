import socket
import urllib.request

import pytest

from engine.bodygraph import ingest, resolver, vendor_audit
from engine.bodygraph.ingest import IngestOutcome, VendorInputs
from engine.bodygraph.vendor_client import HdApiClient, VendorError, VendorRequest, VendorResult
from engine.db import DBAccess


@pytest.fixture(autouse=True)
def _no_ambient_engine_env(monkeypatch):
    # HDE-CRD-0002 WU-PR-04 ID-8: these mappings set APP_ENV explicitly; a leaked process
    # ENGINE_ENV would conflict with it (HDE-CLI-API-Vendor-Ref §7.1.11b).
    monkeypatch.delenv("ENGINE_ENV", raising=False)


def _make_outcome():
    return IngestOutcome(
        vendor="hdapi",
        vendor_version=1,
        input_fingerprint="fingerprint",
        idempotency_key="idem",
        rows_written=1,
        duration_ms=1.0,
        payload_sha256="payload",
        db_emitted_sha256="payload",
        parity_match=True,
        db_rows_after=1,
        payload={"ok": True},
    )


def test_vendor_resolver_maps_synthetic_user(monkeypatch):
    snapshot = {"safe_mode": False, "allow_network": True}
    vendor_inputs = VendorInputs(
        user_id="epic011-s10-invariance-1",
        birthdate="1990-01-01",
        birthtime="12:00",
        location="Amsterdam, Netherlands",
    )
    monkeypatch.setattr(resolver, "_resolve_inputs", lambda *args, **kwargs: vendor_inputs)

    captured = {}

    def fake_ingest(inputs, env=None, dry_run=False):
        captured["inputs"] = inputs
        return _make_outcome()

    monkeypatch.setattr(resolver, "ingest_vendor_bodygraph", fake_ingest)

    result = resolver._resolve_vendor(
        "epic011-s10-invariance-1",
        snapshot,
        upsert=False,
        dry_run=False,
        env={"APP_ENV": "test", "HD_API_BASE_URL": "https://vendor.test/v1"},
        birthdate=None,
        birthtime=None,
        location=None,
    )

    assert captured["inputs"].user_id == "3fa85f64-5717-4562-b3fc-2c963f66afab"
    assert result.status == "ok"


def test_vendor_resolver_wraps_unexpected_normalization_errors(monkeypatch):
    snapshot = {"safe_mode": False, "allow_network": True}
    vendor_inputs = VendorInputs(
        user_id="epic011-s10-invariance-1",
        birthdate="1990-01-01",
        birthtime="12:00",
        location="Amsterdam, Netherlands",
    )
    monkeypatch.setattr(resolver, "_resolve_inputs", lambda *_, **__: vendor_inputs)

    def boom(*_, **__):
        raise RuntimeError("boom")

    monkeypatch.setattr(resolver, "resolve_db_user_id", boom)

    result = resolver._resolve_vendor(
        "epic011-s10-invariance-1",
        snapshot,
        upsert=False,
        dry_run=False,
        env={"APP_ENV": "test", "HD_API_BASE_URL": "https://vendor.test/v1"},
        birthdate=None,
        birthtime=None,
        location=None,
    )

    assert result.status == "error"
    assert result.payload["error"]["code"] == "PROVIDER_INPUT_INVALID"


def test_vendor_resolver_refuses_closed_safe_rails_before_input_or_ingest(monkeypatch):
    def fail_resolve_inputs(*_, **__):  # pragma: no cover - assertion guard
        raise AssertionError("closed SAFE rails must not resolve vendor inputs")

    monkeypatch.setattr(resolver, "_resolve_inputs", fail_resolve_inputs)
    result = resolver._resolve_vendor(
        "user",
        {"safe_mode": True, "allow_network": False, "requested_source": "vendor"},
        upsert=False,
        dry_run=False,
        env={},
        birthdate=None,
        birthtime=None,
        location=None,
    )

    assert result.status == "error"
    assert result.payload["error"]["code"] == "PROVIDER_REFUSED"


def test_vendor_resolver_requires_open_network_exception_before_ingest(monkeypatch):
    def fail_resolve_inputs(*_, **__):  # pragma: no cover - assertion guard
        raise AssertionError("blocked rails must not resolve vendor inputs")

    monkeypatch.setattr(resolver, "_resolve_inputs", fail_resolve_inputs)
    result = resolver._resolve_vendor(
        "user",
        {"safe_mode": False, "allow_network": False, "requested_source": "vendor"},
        upsert=False,
        dry_run=False,
        env={},
        birthdate=None,
        birthtime=None,
        location=None,
    )

    assert result.status == "error"
    assert result.payload["error"]["code"] == "PROVIDER_NETWORK_BLOCKED"


# HDE-CRD-0002 WU-PR-04 (S14): environment classification (HDE-CLI-API-Vendor-Ref §7.1.11b)
# and the read-only production override on the legacy write path (ID-3).


@pytest.mark.parametrize("view, process, expected", [
    ({"APP_ENV": "prod"}, {}, ("prod", True)),
    ({"APP_ENV": " Production "}, {}, ("production", True)),
    ({"APP_ENV": "LIVE"}, {}, ("live", True)),
    ({"APP_ENV": "dev"}, {}, ("dev", False)),
    ({"APP_ENV": "staging"}, {}, ("staging", False)),
    ({"APP_ENV": "  ", "ENGINE_ENV": "test"}, {}, ("test", False)),
    ({"ENGINE_ENV": "live"}, {}, ("live", True)),
    ({"APP_ENV": "test", "ENGINE_ENV": "TEST"}, {}, ("test", False)),
    ({"APP_ENV": "test"}, {"APP_ENV": "production"}, ("production", True)),
    ({"APP_ENV": "test"}, {"ENGINE_ENV": "prod"}, ("prod", True)),
    ({"APP_ENV": "local"}, {"APP_ENV": "dev"}, ("local", False)),
])
def test_environment_classification(view, process, expected):
    environment = resolver.classify_vendor_environment(view, process)
    assert (environment.label, environment.production_like) == expected


@pytest.mark.parametrize("view", [{}, {"APP_ENV": ""}, {"APP_ENV": "development"}, {"APP_ENV": "dev", "ENGINE_ENV": "prod"}, {"APP_ENV": "prod", "ENGINE_ENV": "live"}])
def test_environment_classification_refuses_absent_unknown_or_conflicting(view):
    with pytest.raises(VendorError) as excinfo:
        resolver.classify_vendor_environment(view, {})
    assert excinfo.value.code == "PROVIDER_CONFIG_INVALID"
    assert excinfo.value.as_payload()["details"] == {"outbound_attempted": False}


@pytest.mark.parametrize("dry_run, upsert", [(False, False), (False, True), (True, True)])
def test_production_override_refuses_legacy_writes_before_ingest(monkeypatch, tmp_path, dry_run, upsert):
    monkeypatch.setattr(resolver, "ingest_vendor_bodygraph", lambda *a, **k: pytest.fail("ingest reached"))
    monkeypatch.setattr(resolver.HdApiClient, "from_env", classmethod(lambda cls, **_: pytest.fail("client constructed")))
    monkeypatch.setattr("engine.bodygraph.vendor_audit.resolve_actor_principal", lambda: "test-operator")
    result = resolver.resolve_bodygraph(
        "user", source="vendor", upsert=upsert, dry_run=dry_run,
        env={"SAFE_MODE": "0", "ALLOW_NETWORK": "1", "APP_ENV": "prod", "HD_API_BASE_URL": "https://vendor.test/v1", "HDE_VENDOR_OVERRIDE_AUDIT_PATH": str(tmp_path / "a.jsonl")},
        birthdate="1990-01-01", birthtime="12:00", location="Amsterdam", authorization_ref="PO-1",
    )
    assert result.payload["error"] == {"code": "PROVIDER_WRITE_UNSUPPORTED", "message": "BodyGraph persistence is refused in production-like environments"}


def test_non_production_legacy_write_is_unchanged(monkeypatch):
    seen = {}

    def fake_ingest(inputs, env=None, dry_run=False, **kwargs):
        seen.update(dry_run=dry_run, kwargs=kwargs)
        return _make_outcome()

    monkeypatch.setattr(resolver, "ingest_vendor_bodygraph", fake_ingest)
    result = resolver.resolve_bodygraph(
        "user", source="vendor", upsert=False, dry_run=False,
        env={"SAFE_MODE": "0", "ALLOW_NETWORK": "1", "APP_ENV": "test", "HD_API_BASE_URL": "https://vendor.test/v1"},
        birthdate="1990-01-01", birthtime="12:00", location="Amsterdam",
    )
    assert result.status == "ok" and seen == {"dry_run": False, "kwargs": {}}


# --- HDE-CRD-0002 WU-PR-05 (S19-F05, S19-F06): the resolver opens the rails only for exactly SAFE_MODE=0
# and ALLOW_NETWORK=1 (HDE-CLI-API-Vendor-Ref §7.1.2): an unset or other value refuses at the rails step,
# before environment classification, the override matrix, any audit event or any client construction;
# and a vendor run writes no ingest log under the working directory unless its caller names one ---------

_S19_BIRTH = {"birthdate": "1990-01-01", "birthtime": "07:41", "location": "Amsterdam, NL"}
_S19_V1_BASE = "https://vendor.example.test/v1"
_S19_V2_BASE = "https://vendor.example.test/v2"
_S19_CLOSED_SAFE_MODE = [None, "", "1", " 1 ", "2", "true", "false", "no", "off", "yes"]
_S19_CLOSED_NETWORK = [None, "", "0", "2", "true", "yes", "on", "false"]
_S19_CLOSED_RAILS = [*((s, "1", "PROVIDER_REFUSED") for s in _S19_CLOSED_SAFE_MODE), *(("0", n, "PROVIDER_NETWORK_BLOCKED") for n in _S19_CLOSED_NETWORK)]


def _s19_fail(name):
    def _guard(*_args, **_kwargs):
        raise AssertionError(f"{name} reached under closed rails")

    return _guard


@pytest.fixture
def _s19_vendor_env(monkeypatch, tmp_path):
    for name in ("APP_ENV", "ENGINE_ENV", "SAFE_MODE", "ALLOW_NETWORK", "HD_API_BASE_URL", "HDAPI_BASE_URL"):
        monkeypatch.delenv(name, raising=False)
    monkeypatch.setenv(vendor_audit.VENDOR_OVERRIDE_AUDIT_PATH_KEY, str(tmp_path / "state" / "override.jsonl"))
    monkeypatch.setattr(vendor_audit, "resolve_actor_principal", lambda: "qa-operator")


@pytest.fixture
def _s19_no_io(monkeypatch):
    monkeypatch.setattr(HdApiClient, "__init__", _s19_fail("HdApiClient"))
    monkeypatch.setattr(HdApiClient, "from_env", classmethod(lambda cls, **_: _s19_fail("HdApiClient.from_env")()))
    monkeypatch.setattr(DBAccess, "for_current_env", classmethod(lambda cls, **_: _s19_fail("DBAccess")()))
    monkeypatch.setattr(urllib.request, "urlopen", _s19_fail("urllib.request.urlopen"))
    monkeypatch.setattr(socket, "getaddrinfo", _s19_fail("socket.getaddrinfo"))
    monkeypatch.setattr(socket, "socket", _s19_fail("socket.socket"))


def _s19_env(*, safe, net, app_env="dev", base=_S19_V2_BASE):
    env = {"APP_ENV": app_env, "HD_API_BASE_URL": base, "HD_API_KEY": "fake-key", "GEO_API_KEY": "fake-geo"}
    if safe is not None:
        env["SAFE_MODE"] = safe
    if net is not None:
        env["ALLOW_NETWORK"] = net
    return env

_S19_REF = "PO-HDE-CRD-0002/QA:live-1"


def _s19_sink(tmp_path):
    return tmp_path / "state" / "override.jsonl"


@pytest.mark.usefixtures("_s19_vendor_env", "_s19_no_io")
@pytest.mark.parametrize("ref", [None, _S19_REF])
@pytest.mark.parametrize("app_env", ["dev", "prod"])
@pytest.mark.parametrize("safe", _S19_CLOSED_SAFE_MODE, ids=repr)
def test_s19_safe_rail_refuses_every_value_but_exactly_zero(tmp_path, monkeypatch, safe, app_env, ref):
    monkeypatch.setenv("APP_ENV", app_env)
    result = resolver.resolve_bodygraph("operator-user", source="vendor", upsert=False, dry_run=True,
                                        env=_s19_env(safe=safe, net="1", app_env=app_env), authorization_ref=ref, **_S19_BIRTH)
    assert result.exit_code == 1
    assert result.payload["error"] == {"code": "PROVIDER_REFUSED", "message": "Vendor source is refused under SAFE rails (SAFE_MODE=1)."}
    assert result.payload["resolver"]["safe_mode"] is True
    assert not _s19_sink(tmp_path).exists()


@pytest.mark.usefixtures("_s19_vendor_env", "_s19_no_io")
@pytest.mark.parametrize("ref", [None, _S19_REF])
@pytest.mark.parametrize("app_env", ["dev", "prod"])
@pytest.mark.parametrize("net", _S19_CLOSED_NETWORK, ids=repr)
def test_s19_network_rail_refuses_every_value_but_exactly_one(tmp_path, monkeypatch, net, app_env, ref):
    monkeypatch.setenv("APP_ENV", app_env)
    result = resolver.resolve_bodygraph("operator-user", source="vendor", upsert=False, dry_run=True,
                                        env=_s19_env(safe="0", net=net, app_env=app_env), authorization_ref=ref, **_S19_BIRTH)
    assert result.exit_code == 1
    assert result.payload["error"] == {"code": "PROVIDER_NETWORK_BLOCKED", "message": "Network disabled under current rails."}
    assert result.payload["resolver"]["allow_network"] is False
    assert not _s19_sink(tmp_path).exists()


@pytest.mark.usefixtures("_s19_vendor_env")
@pytest.mark.parametrize("safe,net", [("0", "1"), (" 0 ", " 1 "), (0, 1), (False, True)])
def test_s19_canonical_open_rails_reach_the_route(monkeypatch, safe, net):
    seen = []

    class FakeClient:
        def build_contract_route_request(self, **_kwargs):
            raise VendorError("PROVIDER_INPUT_INVALID", "stop after the rails")

    monkeypatch.setattr(HdApiClient, "from_env", classmethod(lambda cls, **kwargs: seen.append(kwargs) or FakeClient()))
    monkeypatch.setenv("APP_ENV", "dev")
    result = resolver.resolve_bodygraph("operator-user", source="vendor", upsert=False, dry_run=True, env=_s19_env(safe=safe, net=net), **_S19_BIRTH)
    assert result.payload["error"]["code"] == "PROVIDER_INPUT_INVALID"
    assert result.payload["resolver"]["safe_mode"] is False and result.payload["resolver"]["allow_network"] is True
    assert len(seen) == 1


@pytest.mark.usefixtures("_s19_vendor_env", "_s19_no_io")
@pytest.mark.parametrize("safe,net,code", _S19_CLOSED_RAILS, ids=repr)
def test_s19_compat_acquisition_rails_are_exact(safe, net, code):
    with pytest.raises(VendorError) as caught:
        resolver._acquire_dry_run(
            "3fa85f64-5717-4562-b3fc-2c963f66afab", set(), ("1990-01-01", "07:41", "Amsterdam, NL"), _s19_env(safe=safe, net=net)
        )
    assert caught.value.code == code


class _S19LegacyClient:
    def build_request(self, **_kwargs):
        return VendorRequest(url=_S19_V1_BASE + "/bodygraphs", headers={"HD-Api-Key": "x"}, body_bytes=b"{}\n", input_fingerprint="b" * 64, route="vendor.hdapi.post:/bodygraphs")

    def fetch(self, request):
        return VendorResult(payload={"bodygraph": {"type": "Generator"}}, duration_ms=1.0, attempts=1)


@pytest.mark.usefixtures("_s19_vendor_env")
@pytest.mark.parametrize("app_env,ref", [("dev", None), ("prod", _S19_REF)], ids=["non_production", "production_override"])
def test_s19_legacy_vendor_run_writes_no_log_under_the_working_directory(monkeypatch, tmp_path, app_env, ref):
    work = tmp_path / "checkout"
    work.mkdir()
    monkeypatch.chdir(work)
    calls = []
    monkeypatch.setattr(HdApiClient, "from_env", classmethod(lambda cls, **kwargs: calls.append(kwargs) or _S19LegacyClient()))
    monkeypatch.setenv("APP_ENV", app_env)
    result = resolver.resolve_bodygraph("3fa85f64-5717-4562-b3fc-2c963f66afab", source="vendor", upsert=False, dry_run=True,
                                        env=_s19_env(safe="0", net="1", app_env=app_env, base=_S19_V1_BASE), authorization_ref=ref, **_S19_BIRTH)
    assert result.status == "ok", result.payload
    assert len(calls) == 1 and calls[0].get("log_path") is None
    assert sorted(str(path.relative_to(work)) for path in work.rglob("*") if path.is_file()) == []
    assert not (work / ingest.SUCCESS_LOG).exists() and not (work / ingest.RETRY_LOG).exists()
