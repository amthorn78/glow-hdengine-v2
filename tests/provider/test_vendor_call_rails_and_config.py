import json
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


# --- HDE-CRD-0003 X-03: each rail opens only on its exact value (PF05 §7.1.2) ----------------

CLOSED_VALUES = [None, "", "true", "yes", "on", "2"]


def _set(monkeypatch, name, value):
    if value is None:
        monkeypatch.delenv(name, raising=False)
    else:
        monkeypatch.setenv(name, value)


@pytest.mark.parametrize("value", [*CLOSED_VALUES, "1", "false", " TRUE "])
def test_x03_vendor_http_safe_rail_stays_closed_except_for_exact_zero(monkeypatch, value):
    for name in ("CI", "PYTEST_CURRENT_TEST"):  # the old default opened unset SAFE_MODE outside CI and tests
        monkeypatch.delenv(name, raising=False)
    _set(monkeypatch, "SAFE_MODE", value)
    monkeypatch.setenv("ALLOW_NETWORK", "1")
    with pytest.raises(Exception) as ei:
        VendorHttpProvider().get_chart("user-x")
    assert "safe_mode" in str(ei.value)


@pytest.mark.parametrize("value", [*CLOSED_VALUES, "0", "1.0"])
def test_x03_vendor_http_network_rail_stays_closed_except_for_exact_one(monkeypatch, value):
    monkeypatch.setenv("SAFE_MODE", "0")
    _set(monkeypatch, "ALLOW_NETWORK", value)
    with pytest.raises(Exception) as ei:
        VendorHttpProvider().get_chart("user-x")
    assert "allow_network_gate" in str(ei.value)


from scripts.bodygraph import run_refresh_worker as worker  # noqa: E402


@pytest.mark.parametrize("value", [*CLOSED_VALUES, "1", True])
def test_x03_refresh_worker_safe_rail_stays_closed_except_for_exact_zero(value):
    assert worker._safe_mode_closed(value) is True
    assert worker._safe_mode_closed("0") is False and worker._safe_mode_closed(False) is False


@pytest.mark.parametrize("value", [*CLOSED_VALUES, "0", False])
def test_x03_refresh_worker_network_rail_stays_closed_except_for_exact_one(value):
    assert worker._network_allowed(value) is False
    assert worker._network_allowed("1") is True and worker._network_allowed(True) is True


@pytest.mark.parametrize("env, reason", [
    ({"ALLOW_NETWORK": "1"}, "safe_mode"),
    ({"SAFE_MODE": "", "ALLOW_NETWORK": "1"}, "safe_mode"),
    ({"SAFE_MODE": "0", "ALLOW_NETWORK": "true"}, "network_closed"),
    ({"SAFE_MODE": "0", "ALLOW_NETWORK": "yes"}, "network_closed"),
])
def test_x03_refresh_worker_makes_no_vendor_attempt_unless_both_rails_are_exact(monkeypatch, tmp_path, capsys, env, reason):
    monkeypatch.chdir(tmp_path)  # the worker writes its state and samples relative to the working directory
    monkeypatch.setattr(worker, "ingest_vendor_bodygraph", lambda *a, **k: pytest.fail("vendor ingest attempted"))
    worker.run_refresh(env)
    summary = json.loads(capsys.readouterr().out)
    assert summary["status"] == reason and summary["counts"]["refresh_attempts"] == 0
