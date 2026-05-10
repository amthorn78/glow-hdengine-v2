from __future__ import annotations

import json
from pathlib import Path

import pytest

from engine.bodygraph.vendor_client import HdApiClient, VendorError, VendorRequest, VendorResult, VendorRetryConfig, VendorTimeouts


def _client(request_func, log_path: Path | None = None):
    return HdApiClient(
        base_url="https://vendor.test/v1",
        api_key="api",
        geo_key="geo",
        release_id="0" * 64,
        retry=VendorRetryConfig(max_attempts=2, profile="exponential", exp_base_ms=250, exp_ceiling_ms=500),
        timeouts=VendorTimeouts(connect_timeout_ms=1000, read_timeout_ms=2000, total_timeout_ms=5000),
        log_path=log_path,
        request=request_func,
        sleep=lambda _: None,
        monotonic_ms=lambda: 0.0,
    )


def test_build_request_validates_date():
    client = _client(lambda req, timeout: (200, b"{}", {}))
    with pytest.raises(VendorError) as excinfo:
        client.build_request(birthdate="1990-13-01", birthtime="12:00", location="X")
    assert excinfo.value.code == "PROVIDER_INPUT_INVALID"


def test_from_env_normalizes_base_and_headers(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("HDAPI_BASE_URL", "https://vendor.test/v1")
    monkeypatch.setenv("HD_API_KEY", "api-key")
    monkeypatch.setenv("GEO_API_KEY", "geo-key")

    client = HdApiClient.from_env(release_id="0" * 64)
    request = client.build_request(birthdate="1990-01-01", birthtime="12:00", location="X")

    assert request.url == "https://vendor.test/v1/bodygraphs"
    assert request.headers["HD-Api-Key"] == "api-key"
    assert request.headers["HD-Geocode-Key"] == "geo-key"


def test_fetch_maps_status_to_typed_error():
    def failing_request(req, timeout):
        return 401, b"{}", {}

    client = _client(failing_request)
    request = VendorRequest(url="https://vendor.test/v1/bodygraphs", headers={}, body_bytes=b"{}\n", input_fingerprint="abc")
    with pytest.raises(VendorError) as excinfo:
        client.fetch(request)
    assert excinfo.value.code == "PROVIDER_UNAUTHORIZED"


def test_fetch_success_parses_json(tmp_path: Path):
    log_path = tmp_path / "retry.log"

    def ok_request(req, timeout):
        body = json.dumps({"ok": True}).encode("utf-8")
        return 200, body, {"content-type": "application/json"}

    client = _client(ok_request, log_path=log_path)
    req = VendorRequest(url="https://vendor.test/v1/bodygraphs", headers={}, body_bytes=b"{}\n", input_fingerprint="abc")
    result = client.fetch(req)
    assert isinstance(result, VendorResult)
    assert result.payload["ok"] is True
    assert log_path.exists()


def test_fetch_does_not_retry_429_and_parses_retry_after_delta() -> None:
    calls = []

    def rate_limited(req, timeout):
        calls.append(req.full_url)
        return 429, b"{}", {"retry-after": "4"}

    client = _client(rate_limited)
    request = VendorRequest(url="https://vendor.test/v1/bodygraphs", headers={}, body_bytes=b"{}\n", input_fingerprint="abc")
    with pytest.raises(VendorError) as excinfo:
        client.fetch(request)

    assert excinfo.value.code == "PROVIDER_RATE_LIMITED"
    assert calls == ["https://vendor.test/v1/bodygraphs"]


def test_fetch_does_not_retry_other_4xx_statuses() -> None:
    calls = []

    def forbidden(req, timeout):
        calls.append(req.full_url)
        return 403, b"{}", {}

    client = _client(forbidden)
    request = VendorRequest(url="https://vendor.test/v1/bodygraphs", headers={}, body_bytes=b"{}\n", input_fingerprint="abc")
    with pytest.raises(VendorError) as excinfo:
        client.fetch(request)

    assert excinfo.value.code == "PROVIDER_FORBIDDEN"
    assert calls == ["https://vendor.test/v1/bodygraphs"]


def test_fetch_retries_only_5xx_and_network_errors() -> None:
    statuses = [500, 200]
    sleeps = []

    def flaky(req, timeout):
        status = statuses.pop(0)
        body = json.dumps({"ok": True}).encode("utf-8")
        return status, body, {}

    client = HdApiClient(
        base_url="https://vendor.test/v1",
        api_key="api",
        geo_key="geo",
        release_id="0" * 64,
        retry=VendorRetryConfig(max_attempts=2, profile="fixed", exp_base_ms=250, exp_ceiling_ms=250),
        timeouts=VendorTimeouts(connect_timeout_ms=1000, read_timeout_ms=2000, total_timeout_ms=5000),
        request=flaky,
        sleep=lambda seconds: sleeps.append(seconds),
        monotonic_ms=lambda: 0.0,
    )
    request = VendorRequest(url="https://vendor.test/v1/bodygraphs", headers={}, body_bytes=b"{}\n", input_fingerprint="abc")

    result = client.fetch(request)

    assert result.payload == {"ok": True}
    assert result.attempts == 2
    assert sleeps == [0.25]


def test_retry_after_parses_http_date_and_omits_invalid_or_overflow() -> None:
    client = HdApiClient(
        base_url="https://vendor.test/v1",
        api_key="api",
        geo_key="geo",
        release_id="0" * 64,
        retry=VendorRetryConfig(max_attempts=1, profile="none", exp_base_ms=0, exp_ceiling_ms=0),
        timeouts=VendorTimeouts(connect_timeout_ms=1000, read_timeout_ms=2000, total_timeout_ms=5000),
        request=lambda req, timeout: (200, b"{}", {}),
        wall_time=lambda: 1_700_000_000.0,
    )

    assert client._retry_after_ms({"retry-after": "Tue, 14 Nov 2023 23:13:20 GMT"}) == 3_600_000
    assert client._retry_after_ms({"retry-after": "not-a-date"}) is None
    assert client._retry_after_ms({"retry-after": "2147484"}) is None


def test_vendor_policy_rejects_unpinned_retry_and_timeout_profiles() -> None:
    with pytest.raises(VendorError) as retry_exc:
        HdApiClient(
            base_url="https://vendor.test/v1",
            api_key="api",
            geo_key="geo",
            release_id="0" * 64,
            retry=VendorRetryConfig(max_attempts=4, profile="exponential", exp_base_ms=250, exp_ceiling_ms=500),
            timeouts=VendorTimeouts(connect_timeout_ms=1000, read_timeout_ms=2000, total_timeout_ms=5000),
        )
    assert retry_exc.value.code == "PROVIDER_CONFIG_INVALID"

    with pytest.raises(VendorError) as timeout_exc:
        HdApiClient(
            base_url="https://vendor.test/v1",
            api_key="api",
            geo_key="geo",
            release_id="0" * 64,
            retry=VendorRetryConfig(max_attempts=1, profile="none", exp_base_ms=0, exp_ceiling_ms=0),
            timeouts=VendorTimeouts(connect_timeout_ms=999, read_timeout_ms=2000, total_timeout_ms=5000),
        )
    assert timeout_exc.value.code == "PROVIDER_CONFIG_INVALID"
