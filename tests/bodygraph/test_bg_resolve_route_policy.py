from __future__ import annotations

import pytest
from pathlib import Path

from engine.bodygraph.resolver import resolve_bodygraph
from engine.bodygraph.vendor_client import (
    HdApiClient,
    VendorError,
    VendorRequest,
    VendorResult,
    VendorRetryConfig,
    VendorTimeouts,
    classify_bg_resolve_route_policy,
)
from engine.cli.main import cli
from tests.bodygraph.test_v2_adapter import chart_result_payload


def _open_env(base_url: str = "https://vendor.test/v2") -> dict[str, object]:
    return {
        "SAFE_MODE": "0",
        "ALLOW_NETWORK": "1",
        "HD_API_BASE_URL": base_url,
        "HD_API_KEY": "api-key",
        "GEO_API_KEY": "geo-key",
    }


def _closed_env(base_url: str = "https://vendor.test/v2") -> dict[str, object]:
    return {
        "SAFE_MODE": "1",
        "ALLOW_NETWORK": "0",
        "HD_API_BASE_URL": base_url,
        "HD_API_KEY": "api-key",
        "GEO_API_KEY": "geo-key",
    }


def _client(base_url: str, calls: list[str]) -> HdApiClient:
    def request(req, timeout):
        calls.append(req.full_url)
        return 200, b'{"timestamp":"2026-07-05T00:00:00.000Z","success":true,"message":"Chart generated","errorCode":"","type":"ChartResult","data":{}}', {}

    return HdApiClient(
        base_url=base_url,
        api_key="api-key",
        geo_key="geo-key",
        release_id="0" * 64,
        retry=VendorRetryConfig(max_attempts=1, profile="none", exp_base_ms=0, exp_ceiling_ms=0),
        timeouts=VendorTimeouts(connect_timeout_ms=1000, read_timeout_ms=2000, total_timeout_ms=5000),
        request=request,
    )


def test_configured_v2_base_selects_adapter_backed_chart_policy() -> None:
    policy = classify_bg_resolve_route_policy("https://vendor.test/v2")

    assert policy["classification"] == "adapter_backed_v2_chart"
    assert policy["supported"] is True
    assert policy["configured_base_version"] == "v2"
    assert policy["route_family"] == "recommended_v2_chart"
    assert policy["payload_family"] == "ChartResult"
    assert policy["resource_path"] == "charts"
    assert policy["route_auth_posture"] == "Authorization: Bearer <redacted>"
    assert policy["geocode_required"] is True


def test_closed_rails_refuse_before_route_policy_and_external_io() -> None:
    result = resolve_bodygraph(
        "operator-user",
        source="vendor",
        upsert=False,
        dry_run=False,
        env=_closed_env("https://vendor.test/v2"),
        birthdate="1990-01-01",
        birthtime="12:00",
        location="Amsterdam, NL",
    )

    assert result.status == "error"
    assert result.payload["error"]["code"] == "PROVIDER_REFUSED"
    assert "route_policy" not in result.payload["resolver"]


def test_explicit_legacy_fallback_remains_available_for_non_v2_configured_base() -> None:
    policy = classify_bg_resolve_route_policy("https://vendor.test/v1")

    assert policy["classification"] == "explicit_legacy_fallback"
    assert policy["supported"] is True
    assert policy["configured_base_version"] == "v1"
    assert policy["route_family"] == "legacy_bodygraph"
    assert policy["resource_path"] == "bodygraphs"
    assert policy["route_auth_posture"] == "HD-Api-Key: <redacted>"


def test_generic_build_request_guards_v2_chart_route_from_raw_ingest() -> None:
    calls: list[str] = []
    client = _client("https://vendor.test/custom/v2", calls)

    with pytest.raises(VendorError) as excinfo:
        client.build_request(birthdate="1990-01-01", birthtime="12:00", location="Amsterdam, NL")

    assert excinfo.value.code == "PROVIDER_ROUTE_REQUIRES_ADAPTER"
    assert excinfo.value.details["resource_path"] == "charts"
    assert calls == []


def test_build_contract_route_request_builds_v2_charts_and_preserves_prefix() -> None:
    calls: list[str] = []
    client = _client("https://vendor.test/custom/v2", calls)

    request = client.build_contract_route_request(path="charts", request_fields=("birthdate", "birthtime", "location"), geocode_required=True, birthdate="1990-01-01", birthtime="12:00", location="Amsterdam, NL")

    assert request.url == "https://vendor.test/custom/v2/charts"
    assert "/v2/v2/" not in request.url
    assert not request.url.endswith("/bodygraphs")
    assert request.route == "vendor.hdapi.post:/charts"
    assert "Authorization" in request.headers
    assert "HD-Api-Key" not in request.headers
    assert "HD-Geocode-Key" in request.headers
    assert calls == []


def test_v2_resolver_dry_run_maps_payload_through_adapter(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: list[str] = []

    class FakeClient:
        def build_contract_route_request(self, **kwargs):
            assert kwargs["path"] == "charts"
            assert kwargs["request_fields"] == ("birthdate", "birthtime", "location")
            request = _client("https://vendor.test/v2", calls).build_contract_route_request(**kwargs)
            assert request.url == "https://vendor.test/v2/charts"
            return request

        def fetch(self, request: VendorRequest) -> VendorResult:
            calls.append(request.url)
            return VendorResult(
                payload={"timestamp": "2026-07-05T00:00:00.000Z", "success": True, "message": "Chart generated", "errorCode": "", "type": "ChartResult", "data": chart_result_payload()},
                duration_ms=1.0,
                attempts=1,
            )

    monkeypatch.setattr("engine.bodygraph.resolver.HdApiClient.from_env", lambda **kwargs: FakeClient())
    result = resolve_bodygraph(
        "operator-user",
        source="vendor",
        upsert=False,
        dry_run=True,
        env=_open_env("https://vendor.test/v2"),
        birthdate="1990-01-01",
        birthtime="12:00",
        location="Amsterdam, NL",
    )

    assert result.status == "ok"
    assert calls == ["https://vendor.test/v2/charts"]
    assert result.payload["adapter"] == {"status": "mapped", "code": "ADAPTER_MAPPED", "payload_family": "ChartResult"}
    assert result.payload["resolved"]["source"] == "hdapi_v2_chart_adapter"
    assert result.payload["cache"]["payload_posture"] == "adapter_mapped_no_raw_vendor_payload"
    assert result.payload["resolver"]["request"]["header_posture"] == ["Authorization: Bearer <redacted>", "HD-Geocode-Key: <redacted>"]
    assert result.payload["resolver"]["request"]["configured_base_url"] == "<redacted>"
    assert result.payload["resolver"]["request"]["url_posture"] == "configured_base_url/<resource_path>"


def test_v2_adapter_unsupported_becomes_typed_resolver_error(monkeypatch: pytest.MonkeyPatch) -> None:
    class FakeClient:
        def build_contract_route_request(self, **kwargs):
            return _client("https://vendor.test/v2", []).build_contract_route_request(**kwargs)

        def fetch(self, request: VendorRequest) -> VendorResult:
            return VendorResult(payload={"timestamp": "2026-07-05T00:00:00.000Z", "success": True, "message": "Chart generated", "errorCode": "", "type": "ChartResult", "data": {"type": "Generator"}}, duration_ms=1.0, attempts=1)

    monkeypatch.setattr("engine.bodygraph.resolver.HdApiClient.from_env", lambda **kwargs: FakeClient())
    result = resolve_bodygraph("operator-user", source="vendor", upsert=False, dry_run=True, env=_open_env(), birthdate="1990-01-01", birthtime="12:00", location="Amsterdam, NL")

    assert result.status == "error"
    assert result.payload["error"]["code"] == "ADAPTER_VENDOR_DETAIL_INSUFFICIENT"
    assert result.payload["error"]["details"]["adapter_status"] == "unsupported"


def test_v2_non_dry_run_fails_closed_before_fetch(monkeypatch: pytest.MonkeyPatch) -> None:
    def fail_from_env(**kwargs):  # pragma: no cover - assertion guard
        raise AssertionError("client construction must not happen for unsupported v2 write path")

    monkeypatch.setattr("engine.bodygraph.resolver.HdApiClient.from_env", fail_from_env)
    result = resolve_bodygraph("operator-user", source="vendor", upsert=True, dry_run=False, env=_open_env(), birthdate="1990-01-01", birthtime="12:00", location="Amsterdam, NL")

    assert result.status == "error"
    assert result.payload["error"]["code"] == "PROVIDER_WRITE_UNSUPPORTED"


def test_bg_resolve_cli_v2_dry_run_uses_adapter(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    monkeypatch.setenv("SAFE_MODE", "0")
    monkeypatch.setenv("ALLOW_NETWORK", "1")
    monkeypatch.setenv("HD_API_BASE_URL", "https://vendor.test/v2")
    monkeypatch.setenv("HD_API_KEY", "api-key")
    monkeypatch.setenv("GEO_API_KEY", "geo-key")
    monkeypatch.delenv("HDAPI_BASE_URL", raising=False)

    class FakeClient:
        def build_contract_route_request(self, **kwargs):
            return _client("https://vendor.test/v2", []).build_contract_route_request(**kwargs)

        def fetch(self, request: VendorRequest) -> VendorResult:
            return VendorResult(payload={"timestamp": "2026-07-05T00:00:00.000Z", "success": True, "message": "Chart generated", "errorCode": "", "type": "ChartResult", "data": chart_result_payload()}, duration_ms=1.0, attempts=1)

    monkeypatch.setattr("engine.bodygraph.resolver.HdApiClient.from_env", lambda **kwargs: FakeClient())
    exit_code = cli(["bg:resolve", "--user", "operator-user", "--source", "vendor", "--dry-run", "--birthdate", "1990-01-01", "--birthtime", "12:00", "--location", "Amsterdam, NL"])

    assert exit_code == 0
    captured = capsys.readouterr()
    assert "ADAPTER_MAPPED" in captured.out
    assert "vendor.hdapi.post:/charts" in captured.out


def test_resolver_uses_single_merged_config_source_for_policy_and_ingest(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("HD_API_BASE_URL", "https://process.test/v2")
    captured: dict[str, object] = {}

    def fake_ingest(inputs, env=None, dry_run=False):
        captured["env"] = env
        from engine.bodygraph.ingest import IngestOutcome

        return IngestOutcome(vendor="hdapi", vendor_version=1, input_fingerprint="fingerprint", idempotency_key="idem", rows_written=0, duration_ms=1.0, payload_sha256="payload", db_emitted_sha256="payload", parity_match=True, db_rows_after=0, payload={"ok": True})

    monkeypatch.setattr("engine.bodygraph.resolver.ingest_vendor_bodygraph", fake_ingest)
    result = resolve_bodygraph("operator-user", source="vendor", upsert=False, dry_run=True, env={"SAFE_MODE": "0", "ALLOW_NETWORK": "1", "HD_API_BASE_URL": "https://override.test/v1"}, birthdate="1990-01-01", birthtime="12:00", location="Amsterdam, NL")

    assert result.status == "ok"
    assert captured["env"]["HD_API_BASE_URL"] == "https://override.test/v1"
    assert result.payload["resolver"]["route_policy"]["classification"] == "explicit_legacy_fallback"


def test_resolver_v2_override_uses_v2_even_when_process_env_is_v1(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("HD_API_BASE_URL", "https://process.test/v1")

    def fail_from_env(**kwargs):  # pragma: no cover - assertion guard
        raise AssertionError("non-dry-run v2 path must fail closed before client construction")

    monkeypatch.setattr("engine.bodygraph.resolver.HdApiClient.from_env", fail_from_env)
    result = resolve_bodygraph("operator-user", source="vendor", upsert=False, dry_run=False, env={"SAFE_MODE": "0", "ALLOW_NETWORK": "1", "HD_API_BASE_URL": "https://override.test/v2", "HD_API_KEY": "api-key", "GEO_API_KEY": "geo-key"}, birthdate="1990-01-01", birthtime="12:00", location="Amsterdam, NL")

    assert result.status == "error"
    assert result.payload["error"]["code"] == "PROVIDER_WRITE_UNSUPPORTED"
    assert result.payload["resolver"]["route_policy"]["configured_base_version"] == "v2"


def test_direct_ingest_merges_partial_env_with_process_credentials(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    from engine.bodygraph.ingest import VendorInputs, ingest_vendor_bodygraph

    monkeypatch.setenv("HD_API_BASE_URL", "https://process.test/v2")
    monkeypatch.setenv("HD_API_KEY", "process-api-key")
    monkeypatch.setenv("GEO_API_KEY", "process-geo-key")
    captured: dict[str, object] = {}

    class FakeClient:
        def build_request(self, *, birthdate: str, birthtime: str, location: str) -> VendorRequest:
            return VendorRequest(url="https://override.test/v1/bodygraphs", headers={}, body_bytes=b"{}\n", input_fingerprint="fingerprint", route="vendor.hdapi.post:/bodygraphs")

        def fetch(self, request: VendorRequest) -> VendorResult:
            return VendorResult(payload={"ok": True}, duration_ms=1.0, attempts=1)

    def fake_from_env(*, log_path=None, env=None, **kwargs):
        captured["env"] = env
        return FakeClient()

    monkeypatch.setattr("engine.bodygraph.ingest.HdApiClient.from_env", fake_from_env)
    outcome = ingest_vendor_bodygraph(VendorInputs(user_id="operator-user", birthdate="1990-01-01", birthtime="12:00", location="Amsterdam, NL"), env={"SAFE_MODE": "0", "ALLOW_NETWORK": "1", "HD_API_BASE_URL": "https://override.test/v1"}, dry_run=True, success_log=tmp_path / "success.log")

    assert outcome.input_fingerprint == "fingerprint"
    assert captured["env"]["HD_API_BASE_URL"] == "https://override.test/v1"
    assert "HDAPI_BASE_URL" not in captured["env"]
    assert captured["env"]["HD_API_KEY"] == "process-api-key"
    assert captured["env"]["GEO_API_KEY"] == "process-geo-key"
