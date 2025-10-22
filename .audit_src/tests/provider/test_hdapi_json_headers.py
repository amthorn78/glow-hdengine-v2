
from __future__ import annotations
import os
import engine.providers.vendor_http_hdapi as hd

def test_json_headers_present_and_exact(monkeypatch):
    monkeypatch.setenv("SAFE_MODE", "0")
    monkeypatch.setenv("ALLOW_NETWORK", "1")
    monkeypatch.setenv("HD_API_KEY", "k")
    monkeypatch.setenv("GEO_API_KEY", "g")
    req = hd.prepare_hdapi_request("1990-01-01","12:34","Paris, FR", correlation_id="CID-aaaaaaaaaaaaaaaa")
    h = {k: v for k, v in req["headers"].items()}  # case-exact keys
    assert h.get("Accept") == "application/json"
    assert h.get("Content-Type") in ("application/json", "application/json; charset=utf-8")
    # Must still include only the two auth headers besides JSON headers
    assert "HD-Api-Key" in h and "HD-Geocode-Key" in h
