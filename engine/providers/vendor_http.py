import os
from typing import Optional, Dict, Any
from engine.config.provider_types import Provider
from engine.config.provider_errors import ProviderUnavailable, ProviderConfigMissing

_TRUTHY = {"1", "true", "yes", "on"}

def _is_truthy(v: Optional[str]) -> bool:
    return (v or "").strip().lower() in _TRUTHY

def _is_blank(v: Optional[str]) -> bool:
    return v is None or v.strip() == ""

def _safe_mode_enabled() -> bool:
    val = os.getenv("SAFE_MODE")
    if val is None:
        # Default SAFE_MODE ON in CI/tests
        return bool(os.getenv("CI") or os.getenv("PYTEST_CURRENT_TEST"))
    return _is_truthy(val)

class VendorHttpProvider(Provider):
    """
    Vendor HTTP provider — rails only in tests (no real network here).
    Call-time rules:
      - Require SAFE_MODE=0 AND ALLOW_NETWORK=1, else ProviderUnavailable.
      - Require VENDOR_HTTP_BASE_URL and VENDOR_HTTP_API_KEY (non-blank), else ProviderConfigMissing.
      - In tests, even when rails/config satisfied, still raise ProviderUnavailable(reason=network_disabled_in_tests).
    """
    def get_chart(self, user_id: str, *, correlation_id: Optional[str] = None) -> Dict[str, Any]:
        # Rails: SAFE_MODE must be off
        if _safe_mode_enabled():
            raise ProviderUnavailable("provider unavailable: safe_mode")

        # Rails: ALLOW_NETWORK must be truthy
        if not _is_truthy(os.getenv("ALLOW_NETWORK")):
            raise ProviderUnavailable("provider unavailable: allow_network_gate")

        # Config presence (blank strings treated as missing)
        base = os.getenv("VENDOR_HTTP_BASE_URL")
        key  = os.getenv("VENDOR_HTTP_API_KEY")
        missing = []
        if _is_blank(base): missing.append("VENDOR_HTTP_BASE_URL")
        if _is_blank(key):  missing.append("VENDOR_HTTP_API_KEY")
        if missing:
            raise ProviderConfigMissing(f"missing config: {', '.join(missing)}")

        # Tests never perform real HTTP. Keep path gated.
        raise ProviderUnavailable("provider unavailable: network_disabled_in_tests")
