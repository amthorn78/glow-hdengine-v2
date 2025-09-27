from typing import Optional, Dict, Any
import logging, json, time, secrets, re

from engine.config.provider_loader import resolve_provider  # S2 resolver
from engine.providers.fixtures_provider import FixturesProvider
from engine.providers.vendor_http import VendorHttpProvider
from engine.providers.internal_engine import InternalEngineProvider
from engine.config.provider_errors import ProviderUnavailable, ProviderError

_log = logging.getLogger("provider")
# Ensure INFO-level logs are visible in tests that use caplog
if not _log.handlers:
    _log.addHandler(logging.StreamHandler())
_log.setLevel(logging.INFO)

_CID_RE = re.compile(r"^CID-[0-9a-f]{8}$")

def _ensure_provider_with_get_chart(obj):
    """
    If the resolved provider lacks the new get_chart interface, fall back to the
    deterministic FixturesProvider to preserve S2 behavior under SAFE_MODE.
    """
    if hasattr(obj, "get_chart") and callable(getattr(obj, "get_chart")):
        return obj
    return FixturesProvider()

def _provider_name(p: object) -> str:
    if isinstance(p, FixturesProvider): return "fixtures"
    if isinstance(p, VendorHttpProvider): return "vendor_http"
    if isinstance(p, InternalEngineProvider): return "internal_engine"
    # Fallback: class name lowercased sans 'provider'
    name = p.__class__.__name__.lower()
    return name.replace("provider", "") or name

def _cid_or_new(correlation_id: Optional[str]) -> str:
    if isinstance(correlation_id, str) and _CID_RE.match(correlation_id):
        return correlation_id
    return "CID-" + secrets.token_hex(4)  # 8 hex, lower-case

def _log_call(provider: object, status: str, cid: str, duration_ms: int) -> None:
    rec = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "route": "provider.call",
        "provider": _provider_name(provider),
        "op": "get_chart",
        "status": status,             # ok | unavailable | error
        "duration_ms": duration_ms,   # int
        "safe_mode": True if (  # keep a conservative default; providers can refine later
            # We avoid importing SAFE_MODE helpers here to keep import purity;
            # callers/tests assert status classification.
            True
        ) else False,
        "correlation_id": cid,
    }
    # Keys-only; no payloads/user ids
    _log.info(json.dumps(rec, separators=(",", ":")))

def load_chart(user_id: str, *, correlation_id: Optional[str] = None) -> Dict[str, Any]:
    """
    Resolve the current provider and fetch a chart deterministically.
    Keys-only logging of the call (ok/unavailable/error). No payloads/IDs in logs.
    """
    provider = _ensure_provider_with_get_chart(resolve_provider())
    cid = _cid_or_new(correlation_id)
    t0 = time.monotonic()
    try:
        out = provider.get_chart(user_id, correlation_id=cid)  # type: ignore[attr-defined]
        dur = int((time.monotonic() - t0) * 1000)
        _log_call(provider, "ok", cid, dur)
        return out
    except ProviderUnavailable:
        dur = int((time.monotonic() - t0) * 1000)
        _log_call(provider, "unavailable", cid, dur)
        raise
    except ProviderError:
        dur = int((time.monotonic() - t0) * 1000)
        _log_call(provider, "error", cid, dur)
        raise
