
from __future__ import annotations
import pytest

def _errcode(exc) -> str:
    return getattr(exc, "code", "") or getattr(getattr(exc, "args", [None])[0] or {}, "get", lambda *_: None)("code")

def test_status_to_typed_errors():
    import engine.providers.vendor_http_hdapi as hd
    for status, exp in [
        (401, "PROVIDER_UNAUTHORIZED"),
        (403, "PROVIDER_FORBIDDEN"),
        (404, "PROVIDER_NOT_FOUND"),
        (429, "PROVIDER_RATE_LIMITED"),
        (500, "PROVIDER_UNAVAILABLE"),
        (503, "PROVIDER_UNAVAILABLE"),
    ]:
        with pytest.raises(Exception) as ei:
            hd.raise_mapped_provider_error(status, correlation_id="CID-feedfacecafebabe")
        assert getattr(ei.value, "code", "") == exp
        # correlation id should be present in details if provided
        details = getattr(ei.value, "details", {})
        assert details.get("correlation_id") == "CID-feedfacecafebabe"

def test_missing_config_maps_to_typed(monkeypatch):
    # blank or missing env is treated as config missing when building headers
    monkeypatch.delenv("HD_API_KEY", raising=False)
    monkeypatch.delenv("GEO_API_KEY", raising=False)
    import engine.providers.vendor_http_hdapi as hd
    with pytest.raises(Exception) as ei:
        hd.prepare_hdapi_request("1990-01-01","12:34","X, US", correlation_id="CID-deadbeefcafebabe")
    assert getattr(ei.value, "code", "") == "PROVIDER_CONFIG_MISSING"
