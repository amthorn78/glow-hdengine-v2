import os
import types
from typing import Dict, Any

from engine.providers.fixtures_provider import FixturesProvider
from engine.providers.internal_engine import InternalEngineProvider, _safe_mode_enabled
from engine.config.provider_errors import ProviderRefusedInSafeMode

def _is_int_list(xs):
    return isinstance(xs, list) and all(isinstance(i, int) for i in xs)

def test_fixtures_provider_contract():
    p = FixturesProvider()
    out: Dict[str, Any] = p.get_chart("user-123", correlation_id="CID-deadbeef")
    assert isinstance(out, dict)
    assert "gates" in out
    assert _is_int_list(out["gates"])

def test_internal_engine_refused_in_safe_mode(monkeypatch):
    monkeypatch.setenv("SAFE_MODE", "1")
    assert _safe_mode_enabled() is True
    p = InternalEngineProvider()
    try:
        p.get_chart("user-xyz", correlation_id="CID-cafebabe")
        assert False, "expected refusal in SAFE_MODE"
    except ProviderRefusedInSafeMode:
        pass

def test_internal_engine_allows_when_not_safe(monkeypatch):
    monkeypatch.setenv("SAFE_MODE", "0")
    p = InternalEngineProvider()
    out = p.get_chart("user-xyz")
    assert isinstance(out, dict) and "gates" in out and _is_int_list(out["gates"])
