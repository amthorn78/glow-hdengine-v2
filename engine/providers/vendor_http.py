import os
from typing import Optional, Dict, Any
from engine.config.provider_types import Provider
from engine.config.provider_errors import ProviderUnavailable, ProviderConfigMissing

def _rail_value(v: Optional[str]) -> str:
    return "" if v is None else v.strip()

def _is_blank(v: Optional[str]) -> bool:
    return v is None or v.strip() == ""

def _safe_mode_enabled() -> bool:
    # HDE-CLI-API-Vendor-Ref §7.1.2 (HDE-CRD-0003 X-03): the SAFE rail is open only
    # for exactly SAFE_MODE=0; unset, empty and every other value keep it closed.
    return _rail_value(os.getenv("SAFE_MODE")) != "0"

def _network_allowed() -> bool:
    # §7.1.2: the network rail is open only for exactly ALLOW_NETWORK=1.
    return _rail_value(os.getenv("ALLOW_NETWORK")) == "1"

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

        # Rails: ALLOW_NETWORK must be exactly 1
        if not _network_allowed():
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
