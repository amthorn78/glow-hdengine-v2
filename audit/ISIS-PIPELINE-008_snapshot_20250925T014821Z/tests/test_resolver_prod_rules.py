import sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
p = str(ROOT)
if p not in sys.path:
    sys.path.insert(0, p)

import json, pathlib as _pl, contextlib, pytest, os

# Canonical resolver import (no hd_core package in this repo)
from core.config.toggles_resolver import resolve_toggles, OverridesNotAllowedInProd

OVR_PATH = _pl.Path("config/runtime_overrides.json")

@contextlib.contextmanager
def temp_override_file(payload: dict):
    OVR_PATH.parent.mkdir(parents=True, exist_ok=True)
    try:
        with OVR_PATH.open("w", encoding="utf-8") as f:
            json.dump(payload, f, separators=(",", ":"))
        yield
    finally:
        if OVR_PATH.exists():
            OVR_PATH.unlink()

def test_prod_fails_if_override_file_present(monkeypatch):
    monkeypatch.setenv("ENGINE_ENV", "prod")
    with temp_override_file({"experiment": {"patch": {"intimacy.mode": "aggressive"}}}):
        with pytest.raises(OverridesNotAllowedInProd):
            resolve_toggles()

def test_prod_ignores_overrides_when_no_file(monkeypatch):
    if OVR_PATH.exists():
        OVR_PATH.unlink()
    monkeypatch.setenv("ENGINE_ENV", "prod")
    resolved, frozen_sha, applied = resolve_toggles()
    assert isinstance(resolved, dict)
    assert isinstance(frozen_sha, str) and len(frozen_sha) == 64
    assert applied is False

def test_dev_applies_overrides_when_allowed(monkeypatch):
    monkeypatch.setenv("ENGINE_ENV", "dev")
    with temp_override_file({"experiment": {"patch": {"intimacy.mode": "aggressive"}}}):
        resolved, frozen_sha, applied = resolve_toggles()
        assert isinstance(resolved, dict)
        assert isinstance(frozen_sha, str) and len(frozen_sha) == 64
        assert applied in (True, False)
