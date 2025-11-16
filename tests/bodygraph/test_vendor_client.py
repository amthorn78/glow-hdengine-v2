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
