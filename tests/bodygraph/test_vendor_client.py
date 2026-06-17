from __future__ import annotations

import json
from io import BytesIO
from pathlib import Path
from urllib import error as urlerror
from urllib import request as urlrequest

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


def test_fetch_does_not_retry_other_http_statuses() -> None:
    calls = []

    def redirect(req, timeout):
        calls.append(req.full_url)
        return 302, b"{}", {"location": "https://vendor.test/redirect"}

    client = _client(redirect)
    request = VendorRequest(url="https://vendor.test/v1/bodygraphs", headers={}, body_bytes=b"{}\n", input_fingerprint="abc")
    with pytest.raises(VendorError) as excinfo:
        client.fetch(request)

    assert excinfo.value.code == "PROVIDER_ERROR"
    assert excinfo.value.details == {"status": 302}
    assert calls == ["https://vendor.test/v1/bodygraphs"]


def test_default_request_returns_redirect_status_without_following(monkeypatch: pytest.MonkeyPatch) -> None:
    opened = []
    captured_handlers = []

    class RedirectBody(BytesIO):
        def close(self) -> None:
            pass

    class FakeOpener:
        def open(self, req, timeout):
            opened.append((req.full_url, timeout, dict(req.headers)))
            raise urlerror.HTTPError(
                req.full_url,
                302,
                "Found",
                {"Location": "https://vendor.test/redirect"},
                RedirectBody(b"redirect"),
            )

    def fake_build_opener(*handlers):
        captured_handlers.extend(handlers)
        return FakeOpener()

    monkeypatch.setattr(urlrequest, "build_opener", fake_build_opener)
    req = urlrequest.Request(
        "https://vendor.test/v1/bodygraphs",
        data=b"{}\n",
        headers={"HD-Api-Key": "api"},
        method="POST",
    )

    status, body, headers = HdApiClient._default_request(req, 2.0)

    assert status == 302
    assert body == b"redirect"
    assert headers["location"] == "https://vendor.test/redirect"
    assert opened == [("https://vendor.test/v1/bodygraphs", 2.0, {"Hd-api-key": "api"})]
    assert len(captured_handlers) == 1
    assert captured_handlers[0].redirect_request(req, None, 302, "Found", {}, "https://vendor.test/redirect") is None


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


def _read_jsonl(path: Path) -> list[dict[str, object]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def test_vendor_safe_rails_logs_are_keys_only_bounded_and_secret_free(tmp_path: Path) -> None:
    log_path = tmp_path / "safe_rails.jsonl"
    secret_header = "plain-secret-value"
    payload_body = b'{"birthdate":"01-Jan-1990","birthtime":"12:00","location":"Secret City"}\n'

    def ok_request(req, timeout):
        assert req.data == payload_body
        assert req.headers["Hd-api-key"] == secret_header
        return 200, b'{"ok":true}', {"authorization": "Bearer response-secret"}

    client = HdApiClient(
        base_url="https://vendor.test/v1",
        api_key=secret_header,
        geo_key="plain-geo-secret",
        release_id="0" * 64,
        retry=VendorRetryConfig(max_attempts=1, profile="none", exp_base_ms=0, exp_ceiling_ms=0),
        timeouts=VendorTimeouts(connect_timeout_ms=1000, read_timeout_ms=2000, total_timeout_ms=5000),
        log_path=log_path,
        request=ok_request,
        monotonic_ms=lambda: 0.0,
        wall_time=lambda: 1_700_000_000.0,
    )
    request = VendorRequest(
        url="https://vendor.test/v1/bodygraphs",
        headers={"HD-Api-Key": secret_header, "HD-Geocode-Key": "plain-geo-secret"},
        body_bytes=payload_body,
        input_fingerprint="abc",
    )

    client.fetch(request)

    records = _read_jsonl(log_path)
    assert records == [
        {
            "at": "2023-11-14T22:13:20Z",
            "attempt": 1,
            "duration_ms": 0.0,
            "error_class": "none",
            "outcome": "success",
            "profile": "none",
            "rails_state": "open_exception",
            "route": "vendor.hdapi.post:/bodygraphs",
            "status": 200,
            "timeout_profile": "connect=1000;read=2000;total=5000",
        }
    ]
    rendered = log_path.read_text(encoding="utf-8")
    forbidden_fragments = [
        "plain-secret-value",
        "plain-geo-secret",
        "Secret City",
        "birthdate",
        "birthtime",
        "location",
        "authorization",
        "headers",
        "\"body\"",
        "\"payload\"",
        "HD-Api-Key",
        "HD-Geocode-Key",
    ]
    for fragment in forbidden_fragments:
        assert fragment not in rendered


def test_vendor_safe_rails_failure_classes_are_observable(tmp_path: Path) -> None:
    cases = [
        ("network_error", lambda req, timeout: (_ for _ in ()).throw(OSError("boom")), "PROVIDER_NETWORK_ERROR"),
        ("4xx", lambda req, timeout: (403, b"{}", {}), "PROVIDER_FORBIDDEN"),
        ("5xx", lambda req, timeout: (503, b"{}", {}), "PROVIDER_UNAVAILABLE"),
        ("429", lambda req, timeout: (429, b"{}", {"retry-after": "4"}), "PROVIDER_RATE_LIMITED"),
    ]
    request = VendorRequest(
        url="https://vendor.test/v1/bodygraphs",
        headers={},
        body_bytes=b"{}\n",
        input_fingerprint="abc",
    )

    for index, (expected_class, request_func, expected_code) in enumerate(cases):
        log_path = tmp_path / f"case-{index}.jsonl"
        client = HdApiClient(
            base_url="https://vendor.test/v1",
            api_key="api",
            geo_key="geo",
            release_id="0" * 64,
            retry=VendorRetryConfig(max_attempts=1, profile="none", exp_base_ms=0, exp_ceiling_ms=0),
            timeouts=VendorTimeouts(connect_timeout_ms=1000, read_timeout_ms=2000, total_timeout_ms=5000),
            log_path=log_path,
            request=request_func,
            monotonic_ms=lambda: 0.0,
            wall_time=lambda: 1_700_000_000.0,
        )
        with pytest.raises(VendorError) as excinfo:
            client.fetch(request)
        assert excinfo.value.code == expected_code
        record = _read_jsonl(log_path)[0]
        assert record["error_class"] == expected_class
        assert record["outcome"] == "failure"
        assert record["rails_state"] == "open_exception"
        assert record["route"] == "vendor.hdapi.post:/bodygraphs"
        assert record["timeout_profile"] == "connect=1000;read=2000;total=5000"


def test_from_env_prefers_canonical_hd_api_base_url_and_allows_matching_legacy_alias(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("HD_API_BASE_URL", "https://vendor.test/v1")
    monkeypatch.setenv("HDAPI_BASE_URL", "https://vendor.test/v1")
    monkeypatch.setenv("HD_API_KEY", "api-key")
    monkeypatch.setenv("GEO_API_KEY", "geo-key")
    client = HdApiClient.from_env(release_id="0" * 64)
    request = client.build_request(birthdate="1990-01-01", birthtime="12:00", location="X")
    assert request.url == "https://vendor.test/v1/bodygraphs"


def test_from_env_fails_closed_on_conflicting_base_url_alias(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("HD_API_BASE_URL", "https://vendor.test/v1")
    monkeypatch.setenv("HDAPI_BASE_URL", "https://other.test/v1")
    monkeypatch.setenv("HD_API_KEY", "api-key")
    monkeypatch.setenv("GEO_API_KEY", "geo-key")
    with pytest.raises(VendorError) as excinfo:
        HdApiClient.from_env(release_id="0" * 64)
    assert excinfo.value.code == "PROVIDER_CONFIG_INVALID"
    assert "https://" not in str(excinfo.value.as_payload())


def test_build_contract_route_request_uses_v2_bearer_and_geocode_when_required() -> None:
    client = _client(lambda req, timeout: (200, b"{}", {}))
    request = client.build_contract_route_request(
        path="/v2/charts",
        request_fields=("birthdate", "birthtime", "location"),
        geocode_required=True,
        birthdate="1990-01-01",
        birthtime="12:00",
        location="Test",
    )
    assert request.url == "https://vendor.test/v2/charts"
    assert request.headers["Authorization"] == "Bearer api"
    assert "HD-Api-Key" not in request.headers
    assert request.headers["HD-Geocode-Key"] == "geo"


def test_build_contract_route_request_preserves_v1_hd_api_key_and_coordinates_skip_geocode() -> None:
    client = _client(lambda req, timeout: (200, b"{}", {}))
    legacy = client.build_request(birthdate="1990-01-01", birthtime="12:00", location="X")
    assert legacy.headers["HD-Api-Key"] == "api"
    assert "Authorization" not in legacy.headers
    coordinates = client.build_contract_route_request(
        path="/v2/charts/coordinates",
        request_fields=("birthdate", "birthtime", "lat", "lng"),
        geocode_required=False,
        birthdate="1990-01-01",
        birthtime="12:00",
        lat="52.1",
        lng="4.3",
    )
    assert coordinates.headers["Authorization"] == "Bearer api"
    assert "HD-Geocode-Key" not in coordinates.headers


def test_build_request_rejects_whitespace_required_fields() -> None:
    client = _client(lambda req, timeout: (200, b"{}", {}))
    with pytest.raises(VendorError) as excinfo:
        client.build_request(birthdate="1990-01-01", birthtime="   ", location="   ")
    assert excinfo.value.code == "PROVIDER_INPUT_INVALID"
    assert excinfo.value.details["missing"] == ["birthtime", "location"]


def test_v2_request_body_preserves_iso_birthdate_and_numeric_coordinates() -> None:
    client = _client(lambda req, timeout: (200, b"{}", {}))
    request = client.build_contract_route_request(
        path="/v2/charts/coordinates",
        request_fields=("birthdate", "birthtime", "lat", "lng"),
        geocode_required=False,
        birthdate="1990-01-15",
        birthtime="12:00",
        lat="52.1",
        lng="4.3",
    )
    body = json.loads(request.body_bytes.decode("utf-8"))
    assert body == {"birthdate": "1990-01-15", "birthtime": "12:00", "lat": 52.1, "lng": 4.3}


def test_v2_location_routes_reject_non_contract_birthtime_and_location() -> None:
    client = _client(lambda req, timeout: (200, b"{}", {}))
    for birthtime, location in [("9:00", "Amsterdam, NL"), ("24:00", "Amsterdam, NL"), ("12:60", "Amsterdam, NL"), ("12:00", "X")]:
        with pytest.raises(VendorError):
            client.build_contract_route_request(
                path="/v2/charts",
                request_fields=("birthdate", "birthtime", "location"),
                geocode_required=True,
                birthdate="1990-01-15",
                birthtime=birthtime,
                location=location,
            )


def test_v2_request_body_rejects_non_contract_date_and_coordinates() -> None:
    client = _client(lambda req, timeout: (200, b"{}", {}))
    with pytest.raises(VendorError):
        client.build_contract_route_request(
            path="/v2/charts/coordinates",
            request_fields=("birthdate", "birthtime", "lat", "lng"),
            geocode_required=False,
            birthdate="1990-01-5",
            birthtime="12:00",
            lat="52.1",
            lng="4.3",
        )
    for lat, lng in [("north", "4.3"), ("nan", "4.3"), ("inf", "4.3"), ("91", "4.3"), ("52.1", "181")]:
        with pytest.raises(VendorError):
            client.build_contract_route_request(
                path="/v2/charts/coordinates",
                request_fields=("birthdate", "birthtime", "lat", "lng"),
                geocode_required=False,
                birthdate="1990-01-15",
                birthtime="12:00",
                lat=lat,
                lng=lng,
            )


def test_fetch_logs_shaped_v2_route(tmp_path: Path) -> None:
    log_path = tmp_path / "retry.log"

    def ok_request(req, timeout):
        return 200, b'{"ok":true}', {}

    client = _client(ok_request, log_path=log_path)
    request = client.build_contract_route_request(
        path="/v2/charts",
        request_fields=("birthdate", "birthtime", "location"),
        geocode_required=True,
        birthdate="1990-01-15",
        birthtime="12:00",
        location="Amsterdam, NL",
    )
    client.fetch(request)
    record = _read_jsonl(log_path)[0]
    assert record["route"] == "vendor.hdapi.post:/v2/charts"
