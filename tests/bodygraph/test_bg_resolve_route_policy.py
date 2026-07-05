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
    }


def _client(base_url: str, calls: list[str]) -> HdApiClient:
    def request(req, timeout):
        calls.append(req.full_url)
        return 200, b'{"ok":true}', {}

    return HdApiClient(
        base_url=base_url,
        api_key="api-key",
        geo_key="geo-key",
        release_id="0" * 64,
        retry=VendorRetryConfig(max_attempts=1, profile="none", exp_base_ms=0, exp_ceiling_ms=0),
        timeouts=VendorTimeouts(connect_timeout_ms=1000, read_timeout_ms=2000, total_timeout_ms=5000),
        request=request,
    )


def _chart_payload() -> dict[str, object]:
    data = {key: f"fixture:{key}" for key in (
        "authority", "birthDateUtc", "circuitries", "cognition", "definition", "determination", "distraction", "environment", "incarnationCross", "motivation", "notSelfTheme", "perspective", "profile", "signature", "strategy", "transference", "type", "variables"
    )}
    data.update({"activations": {"sun": "20"}, "centers": ["G", "Sacral"], "channelsLong": ["The Channel of Charisma (20-34)"], "channelsShort": ["20-34"], "gates": ["20", "34"]})
    return {"timestamp": "2026-07-05T00:00:00Z", "success": True, "message": "ok", "errorCode": "", "type": "ChartResult", "data": data}


def test_configured_v2_base_selects_adapter_backed_chart_route_policy() -> None:
    policy = classify_bg_resolve_route_policy("https://vendor.test/v2")

    assert policy["classification"] == "adapter_backed_v2_chart"
    assert policy["supported"] is True
    assert policy["route_family"] == "recommended_v2_chart"
    assert policy["resource_path"] == "charts"
    assert policy["expected_payload_family"] == "ChartResult"
    assert policy["route_auth_posture"] == "Authorization: Bearer <redacted>"
    assert policy["geocode_required"] is True


def test_closed_rails_refuse_before_route_policy_and_external_io() -> None:
    result = resolve_bodygraph(
        "operator-user", source="vendor", upsert=False, dry_run=False, env=_closed_env("https://vendor.test/v2"), birthdate="1990-01-01", birthtime="12:00", location="Amsterdam, NL",
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


def test_hdapi_client_build_request_uses_charts_for_v2_without_double_prefix() -> None:
    calls: list[str] = []
    client = _client("https://vendor.test/prefix/v2", calls)

    request = client.build_request(birthdate="1990-01-01", birthtime="12:00", location="Amsterdam, NL")

    assert request.url == "https://vendor.test/prefix/v2/charts"
    assert request.route == "vendor.hdapi.post:/charts"
    assert b"bodygraphs" not in request.body_bytes
    assert "Authorization" in request.headers
    assert "HD-Api-Key" not in request.headers
    assert "HD-Geocode-Key" in request.headers
    assert calls == []


def test_legacy_build_request_remains_bodygraphs_and_hd_api_key() -> None:
    calls: list[str] = []
    client = _client("https://vendor.test/v1", calls)

    request = client.build_request(birthdate="1990-01-01", birthtime="12:00", location="Amsterdam, NL")

    assert request.url == "https://vendor.test/v1/bodygraphs"
    assert request.route == "vendor.hdapi.post:/bodygraphs"
    assert "HD-Api-Key" in request.headers
    assert "Authorization" not in request.headers


def test_bg_resolve_dry_run_maps_v2_chart_payload_through_adapter(monkeypatch: pytest.MonkeyPatch) -> None:
    captured: dict[str, object] = {}

    class FakeClient:
        def build_contract_route_request(self, **kwargs) -> VendorRequest:
            captured["kwargs"] = kwargs
            return VendorRequest(url="https://vendor.test/v2/charts", headers={"Authorization": "Bearer raw", "HD-Geocode-Key": "raw"}, body_bytes=b"{}\n", input_fingerprint="a" * 64, route="vendor.hdapi.post:/charts")

        def fetch(self, request: VendorRequest) -> VendorResult:
            captured["fetch_url"] = request.url
            return VendorResult(payload=_chart_payload(), duration_ms=1.0, attempts=1)

    monkeypatch.setattr("engine.bodygraph.resolver.HdApiClient.from_env", lambda **kwargs: FakeClient())
    result = resolve_bodygraph("operator-user", source="vendor", upsert=False, dry_run=True, env=_open_env(), birthdate="1990-01-01", birthtime="12:00", location="Amsterdam, NL")

    assert result.status == "ok"
    assert captured["kwargs"]["path"] == "charts"
    assert result.payload["adapter"]["code"] == "ADAPTER_MAPPED"
    assert result.payload["resolved"]["source"] == "hdapi_v2_chart_adapter"
    assert result.payload["cache"]["payload_posture"] == "adapter_mapped_no_raw_vendor_payload"
    assert result.payload["request"]["auth_header_posture"] == "Authorization: Bearer <redacted>"
    assert result.payload["request"]["geocode_header_posture"] == "HD-Geocode-Key: <redacted>"


def test_bg_resolve_v2_adapter_unsupported_returns_typed_nonclaim(monkeypatch: pytest.MonkeyPatch) -> None:
    class FakeClient:
        def build_contract_route_request(self, **kwargs) -> VendorRequest:
            return VendorRequest(url="https://vendor.test/v2/charts", headers={}, body_bytes=b"{}\n", input_fingerprint="a" * 64, route="vendor.hdapi.post:/charts")

        def fetch(self, request: VendorRequest) -> VendorResult:
            return VendorResult(payload={"timestamp": "2026-07-05T00:00:00Z", "success": True, "message": "ok", "errorCode": "", "type": "ChartResult", "data": {"type": "Generator"}}, duration_ms=1.0, attempts=1)

    monkeypatch.setattr("engine.bodygraph.resolver.HdApiClient.from_env", lambda **kwargs: FakeClient())
    result = resolve_bodygraph("operator-user", source="vendor", upsert=False, dry_run=True, env=_open_env(), birthdate="1990-01-01", birthtime="12:00", location="Amsterdam, NL")

    assert result.status == "error"
    assert result.payload["error"]["code"] == "PROVIDER_ROUTE_UNSUPPORTED"
    assert result.payload["error"]["details"]["classification"] == "adapter_unsupported_nonclaim"
    assert result.payload["error"]["details"]["adapter"]["status"] == "unsupported"


def test_bg_resolve_v2_non_dry_run_fails_closed_before_fetch(monkeypatch: pytest.MonkeyPatch) -> None:
    def fail_from_env(**kwargs):
        raise AssertionError("non-dry-run v2 path must fail before client construction")

    monkeypatch.setattr("engine.bodygraph.resolver.HdApiClient.from_env", fail_from_env)
    result = resolve_bodygraph("operator-user", source="vendor", upsert=True, dry_run=False, env=_open_env(), birthdate="1990-01-01", birthtime="12:00", location="Amsterdam, NL")

    assert result.status == "error"
    assert result.payload["error"]["details"]["classification"] == "adapter_mapped_persistence_nonclaim"


def test_bg_resolve_dry_run_cli_uses_v2_adapter_path(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    monkeypatch.setenv("SAFE_MODE", "0")
    monkeypatch.setenv("ALLOW_NETWORK", "1")
    monkeypatch.setenv("HD_API_BASE_URL", "https://vendor.test/v2")
    monkeypatch.setenv("HD_API_KEY", "api-key")
    monkeypatch.setenv("GEO_API_KEY", "geo-key")
    monkeypatch.delenv("HDAPI_BASE_URL", raising=False)

    class FakeClient:
        def build_contract_route_request(self, **kwargs) -> VendorRequest:
            return VendorRequest(url="https://vendor.test/v2/charts", headers={}, body_bytes=b"{}\n", input_fingerprint="a" * 64, route="vendor.hdapi.post:/charts")
        def fetch(self, request: VendorRequest) -> VendorResult:
            return VendorResult(payload=_chart_payload(), duration_ms=1.0, attempts=1)

    monkeypatch.setattr("engine.bodygraph.resolver.HdApiClient.from_env", lambda **kwargs: FakeClient())
    exit_code = cli(["bg:resolve", "--user", "operator-user", "--source", "vendor", "--dry-run", "--birthdate", "1990-01-01", "--birthtime", "12:00", "--location", "Amsterdam, NL"])

    assert exit_code == 0
    captured = capsys.readouterr()
    assert "ADAPTER_MAPPED" in captured.out
    assert "vendor.hdapi.post:/charts" in captured.out


def test_direct_ingest_merges_partial_env_with_process_credentials(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    from engine.bodygraph.ingest import VendorInputs, ingest_vendor_bodygraph
    from engine.bodygraph.vendor_client import VendorRequest, VendorResult

    monkeypatch.setenv("HD_API_BASE_URL", "https://process.test/v2")
    monkeypatch.setenv("HD_API_KEY", "process-api-key")
    monkeypatch.setenv("GEO_API_KEY", "process-geo-key")
    captured: dict[str, object] = {}

    class FakeClient:
        def build_request(self, *, birthdate: str, birthtime: str, location: str) -> VendorRequest:
            return VendorRequest(
                url="https://override.test/v1/bodygraphs",
                headers={},
                body_bytes=b"{}\n",
                input_fingerprint="fingerprint",
                route="vendor.hdapi.post:/bodygraphs",
            )

        def fetch(self, request: VendorRequest) -> VendorResult:
            return VendorResult(payload={"ok": True}, duration_ms=1.0, attempts=1)

    def fake_from_env(*, log_path=None, env=None, **kwargs):
        captured["env"] = env
        return FakeClient()

    monkeypatch.setattr("engine.bodygraph.ingest.HdApiClient.from_env", fake_from_env)
    outcome = ingest_vendor_bodygraph(
        VendorInputs(
            user_id="operator-user",
            birthdate="1990-01-01",
            birthtime="12:00",
            location="Amsterdam, NL",
        ),
        env={"SAFE_MODE": "0", "ALLOW_NETWORK": "1", "HD_API_BASE_URL": "https://override.test/v1"},
        dry_run=True,
        success_log=tmp_path / "success.log",
    )

    assert outcome.input_fingerprint == "fingerprint"
    assert captured["env"]["HD_API_BASE_URL"] == "https://override.test/v1"
    assert "HDAPI_BASE_URL" not in captured["env"]
    assert captured["env"]["HD_API_KEY"] == "process-api-key"
    assert captured["env"]["GEO_API_KEY"] == "process-geo-key"
