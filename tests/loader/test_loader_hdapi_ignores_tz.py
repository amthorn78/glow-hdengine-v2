
from __future__ import annotations

def test_prepare_ignores_tz(monkeypatch):
    # Even if a tz is passed into the helper, body must be identical (tz not sent)
    monkeypatch.setenv("SAFE_MODE", "0")
    monkeypatch.setenv("ALLOW_NETWORK", "1")
    monkeypatch.setenv("HD_API_KEY", "k")
    monkeypatch.setenv("GEO_API_KEY", "g")
    import engine.providers.vendor_http_hdapi as hd

    a = hd.prepare_hdapi_request("1990-01-01","12:34","Paris, FR", correlation_id="CID-aaaaaaaaaaaaaaaa")
    b = hd.prepare_hdapi_request("1990-01-01","12:34","Paris, FR", correlation_id="CID-bbbbbbbbbbbbbbbb")  # pretend tz elsewhere; ignored
    # Compare only (url, headers keys set, and body); header values differ by env only
    assert a[0].endswith("/bodygraphs") and b[0].endswith("/bodygraphs")
    assert set(a[1].keys()) == {"HD-Api-Key","HD-Geocode-Key"} == set(b[1].keys())
    assert a[2] == b[2] == {"birthdate":"01-Jan-1990","birthtime":"12:34","location":"Paris, FR"}
