from __future__ import annotations

import pytest
from pathlib import Path

from engine.bodygraph.resolver import resolve_bodygraph
from engine.bodygraph.vendor_client import (
    HdApiClient,
    VendorError,
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
    }


def _closed_env(base_url: str = "https://vendor.test/v2") -> dict[str, object]:
    return {
        "SAFE_MODE": "1",
        "ALLOW_NETWORK": "0",
        "HD_API_BASE_URL": base_url,
    }


def _client(base_url: str, calls: list[str]) -> HdApiClient:
    def request(req, timeout):  # pragma: no cover - assertions expect no I/O for v2 policy
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


def test_configured_v2_base_returns_unsupported_runtime_nonclaim_before_ingest_io() -> None:
    result = resolve_bodygraph(
        "operator-user",
        source="vendor",
        upsert=False,
        dry_run=False,
        env=_open_env("https://vendor.test/v2"),
        birthdate="1990-01-01",
        birthtime="12:00",
        location="Amsterdam, NL",
    )

    assert result.status == "error"
    assert result.exit_code == 1
    assert result.payload["error"]["code"] == "PROVIDER_ROUTE_UNSUPPORTED"
    policy = result.payload["resolver"]["route_policy"]
    assert policy["classification"] == "unsupported_runtime_nonclaim"
    assert policy["route_family"] == "legacy_bodygraph"
    assert policy["resource_path"] == "bodygraphs"
    assert policy["route_auth_posture"] == "HD-Api-Key: <redacted>"


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
    assert policy["route_auth_posture"] == "HD-Api-Key: <redacted>"


def test_hdapi_client_does_not_build_accidental_v2_bodygraphs_request() -> None:
    calls: list[str] = []
    client = _client("https://vendor.test/v2", calls)

    with pytest.raises(VendorError) as excinfo:
        client.build_request(birthdate="1990-01-01", birthtime="12:00", location="Amsterdam, NL")

    assert excinfo.value.code == "PROVIDER_ROUTE_UNSUPPORTED"
    assert excinfo.value.details["classification"] == "unsupported_runtime_nonclaim"
    assert calls == []


def test_charts_simple_metadata_does_not_change_bg_resolve_v2_nonclaim() -> None:
    calls: list[str] = []
    client = _client("https://vendor.test/v2", calls)
    chart_request = client.build_contract_route_request(
        path="charts/simple",
        request_fields=("birthdate", "birthtime", "location"),
        geocode_required=True,
        birthdate="1990-01-01",
        birthtime="12:00",
        location="Amsterdam, NL",
    )

    assert chart_request.url == "https://vendor.test/v2/charts/simple"
    assert "Authorization" in chart_request.headers
    with pytest.raises(VendorError) as excinfo:
        client.build_request(birthdate="1990-01-01", birthtime="12:00", location="Amsterdam, NL")
    assert excinfo.value.code == "PROVIDER_ROUTE_UNSUPPORTED"
    assert calls == []


def test_bg_resolve_dry_run_does_not_bypass_v2_route_policy(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    monkeypatch.setenv("SAFE_MODE", "0")
    monkeypatch.setenv("ALLOW_NETWORK", "1")
    monkeypatch.setenv("HD_API_BASE_URL", "https://vendor.test/v2")
    monkeypatch.delenv("HDAPI_BASE_URL", raising=False)

    exit_code = cli([
        "bg:resolve",
        "--user",
        "operator-user",
        "--source",
        "vendor",
        "--dry-run",
        "--birthdate",
        "1990-01-01",
        "--birthtime",
        "12:00",
        "--location",
        "Amsterdam, NL",
    ])

    assert exit_code == 1
    captured = capsys.readouterr()
    assert "PROVIDER_ROUTE_UNSUPPORTED" in captured.out
    assert "unsupported_runtime_nonclaim" in captured.out


def test_resolver_uses_single_merged_config_source_for_policy_and_ingest(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("HD_API_BASE_URL", "https://process.test/v2")
    captured: dict[str, object] = {}

    def fake_ingest(inputs, env=None, dry_run=False):
        captured["env"] = env
        from engine.bodygraph.ingest import IngestOutcome

        return IngestOutcome(
            vendor="hdapi",
            vendor_version=1,
            input_fingerprint="fingerprint",
            idempotency_key="idem",
            rows_written=0,
            duration_ms=1.0,
            payload_sha256="payload",
            db_emitted_sha256="payload",
            parity_match=True,
            db_rows_after=0,
            payload={"ok": True},
        )

    monkeypatch.setattr("engine.bodygraph.resolver.ingest_vendor_bodygraph", fake_ingest)
    result = resolve_bodygraph(
        "operator-user",
        source="vendor",
        upsert=False,
        dry_run=True,
        env={"SAFE_MODE": "0", "ALLOW_NETWORK": "1", "HD_API_BASE_URL": "https://override.test/v1"},
        birthdate="1990-01-01",
        birthtime="12:00",
        location="Amsterdam, NL",
    )

    assert result.status == "ok"
    assert captured["env"]["HD_API_BASE_URL"] == "https://override.test/v1"
    assert result.payload["resolver"]["route_policy"]["classification"] == "explicit_legacy_fallback"


def test_resolver_v2_override_refuses_even_when_process_env_is_v1(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("HD_API_BASE_URL", "https://process.test/v1")

    def fail_ingest(*args, **kwargs):  # pragma: no cover - assertion guard
        raise AssertionError("configured-v2 route policy must refuse before ingest")

    monkeypatch.setattr("engine.bodygraph.resolver.ingest_vendor_bodygraph", fail_ingest)
    result = resolve_bodygraph(
        "operator-user",
        source="vendor",
        upsert=False,
        dry_run=True,
        env={"SAFE_MODE": "0", "ALLOW_NETWORK": "1", "HD_API_BASE_URL": "https://override.test/v2"},
        birthdate="1990-01-01",
        birthtime="12:00",
        location="Amsterdam, NL",
    )

    assert result.status == "error"
    assert result.payload["error"]["code"] == "PROVIDER_ROUTE_UNSUPPORTED"
    assert result.payload["resolver"]["route_policy"]["configured_base_version"] == "v2"


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
