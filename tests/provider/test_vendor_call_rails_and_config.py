import os
import pytest
from engine.providers.vendor_http import VendorHttpProvider

def test_vendor_refused_when_safe_mode_on(monkeypatch):
    monkeypatch.setenv("SAFE_MODE", "1")
    monkeypatch.delenv("ALLOW_NETWORK", raising=False)
    p = VendorHttpProvider()
    with pytest.raises(Exception) as ei:
        p.get_chart("user-x")
    assert "safe_mode" in str(ei.value)

def test_vendor_unavailable_when_allow_network_missing(monkeypatch):
    monkeypatch.setenv("SAFE_MODE", "0")
    monkeypatch.delenv("ALLOW_NETWORK", raising=False)
    p = VendorHttpProvider()
    with pytest.raises(Exception) as ei:
        p.get_chart("user-x")
    assert "allow_network_gate" in str(ei.value)

def test_vendor_config_missing_checked_at_call_time(monkeypatch):
    monkeypatch.setenv("SAFE_MODE", "0")
    monkeypatch.setenv("ALLOW_NETWORK", "1")
    # Explicitly blank both
    monkeypatch.setenv("VENDOR_HTTP_BASE_URL", "   ")
    monkeypatch.setenv("VENDOR_HTTP_API_KEY", "")
    p = VendorHttpProvider()
    with pytest.raises(Exception) as ei:
        p.get_chart("user-x")
    s = str(ei.value)
    assert "missing config" in s
    assert "VENDOR_HTTP_BASE_URL" in s and "VENDOR_HTTP_API_KEY" in s

def test_vendor_still_unavailable_in_tests_even_with_config(monkeypatch):
    monkeypatch.setenv("SAFE_MODE", "0")
    monkeypatch.setenv("ALLOW_NETWORK", "1")
    monkeypatch.setenv("VENDOR_HTTP_BASE_URL", "https://example.test")
    monkeypatch.setenv("VENDOR_HTTP_API_KEY", "secret")
    p = VendorHttpProvider()
    with pytest.raises(Exception) as ei:
        p.get_chart("user-x")
    assert "network_disabled_in_tests" in str(ei.value)
