import os
import pytest
from typing import Dict, Any

from engine.charts.loader import load_chart
from engine.providers.vendor_http import VendorHttpProvider
from engine.config.provider_errors import ProviderUnavailable

def _is_int_list(xs):
    return isinstance(xs, list) and all(isinstance(i, int) for i in xs)

def test_loader_uses_fixtures_by_default_in_safe_mode(monkeypatch):
    # Default resolution should yield fixtures provider under SAFE_MODE
    monkeypatch.setenv("SAFE_MODE", "1")
    # Clean env: let resolver choose the default (fixtures)
    out: Dict[str, Any] = load_chart("user-abc", correlation_id="CID-deadbeef")
    assert isinstance(out, dict)
    assert "gates" in out and _is_int_list(out["gates"])

def test_loader_vendor_path_is_gated_in_safe_mode(monkeypatch):
    # Force the loader to use the vendor provider and verify SAFE_MODE gating
    monkeypatch.setenv("SAFE_MODE", "1")

    # Monkeypatch resolver to return a vendor provider instance
    import engine.charts.loader as L
    L.resolve_provider = lambda: VendorHttpProvider()  # type: ignore

    with pytest.raises(ProviderUnavailable) as ei:
        load_chart("user-xyz", correlation_id="CID-cafebabe")
    assert "safe_mode" in str(ei.value)
