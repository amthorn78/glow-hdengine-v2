import pytest

from engine.bodygraph import resolver
from engine.bodygraph.ingest import IngestOutcome, VendorInputs
from engine.bodygraph.vendor_client import VendorError


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
