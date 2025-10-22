
from __future__ import annotations
import json, os
from pathlib import Path

def _set_ok_env(monkeypatch):
    monkeypatch.setenv("SAFE_MODE", "0")
    monkeypatch.setenv("ALLOW_NETWORK", "1")
    monkeypatch.setenv("HD_API_KEY", "k_test_api")
    monkeypatch.setenv("GEO_API_KEY", "k_test_geo")
    # Do not set HDAPI_BASE_URL to exercise default

def test_prepare_request_exact_headers_and_body(monkeypatch, tmp_path):
    _set_ok_env(monkeypatch)
    import importlib
    import engine.providers.vendor_http_hdapi as hd  # to be implemented in S3-B

    url, headers, body = hd.prepare_hdapi_request(
        "1990-01-01", "12:34", "Amsterdam, NL", correlation_id="CID-deadbeefdeadbeef"
    )

    # URL targets default base + /bodygraphs
    assert url.endswith("/bodygraphs")
    assert url.startswith("https://api.humandesignapi.nl/v1")

    # Headers: EXACTLY the two dash-case keys, values from env, nothing else
    assert set(headers.keys()) == {"HD-Api-Key", "HD-Geocode-Key"}
    assert headers["HD-Api-Key"] == "k_test_api"
    assert headers["HD-Geocode-Key"] == "k_test_geo"

    # Body: EXACT three keys, with locale-free date conversion and no tz
    assert set(body.keys()) == {"birthdate", "birthtime", "location"}
    assert body["birthdate"] == "01-Jan-1990"
    assert body["birthtime"] == "12:34"
    assert body["location"] == "Amsterdam, NL"

    # Emit sample artifacts (LF, BOM-free)
    outdir = Path("artifacts/hdapi"); outdir.mkdir(parents=True, exist_ok=True)
    Path(outdir/"request_sample.json").write_text(
        json.dumps(body, ensure_ascii=False, separators=(",",":")) + "\n", encoding="utf-8"
    )
    Path(outdir/"headers_sample.json").write_text(
        json.dumps(sorted(list(headers.keys())), ensure_ascii=False) + "\n", encoding="utf-8"
    )

def test_base_url_override(monkeypatch):
    # If HDAPI_BASE_URL is set, /bodygraphs must be appended to that base
    monkeypatch.setenv("SAFE_MODE", "0")
    monkeypatch.setenv("ALLOW_NETWORK", "1")
    monkeypatch.setenv("HD_API_KEY", "k")
    monkeypatch.setenv("GEO_API_KEY", "g")
    monkeypatch.setenv("HDAPI_BASE_URL", "https://example.test/v9")

    import engine.providers.vendor_http_hdapi as hd
    url, headers, body = hd.prepare_hdapi_request("1990-01-01","12:34","X, US", correlation_id="CID-a"*8)
    assert url == "https://example.test/v9/bodygraphs"
