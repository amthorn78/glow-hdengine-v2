from __future__ import annotations
from typing import Any
from adapter.env_guard import EnvGuardError  # typed: (code, message, details)
from .base import PairProfile

class VendorHttpProvider:
    """
    S2 hard stub (no network):
      - If SAFE_MODE=1: refuse to construct.
      - If SAFE_MODE=0: construct, but any call raises PROVIDER_UNAVAILABLE.
    """
    def __init__(self, safe_mode: bool = True):
        if safe_mode:
            raise EnvGuardError(
                "PROVIDER_UNAVAILABLE",
                "vendor_http disabled in SAFE_MODE",
                {"safe_mode": True},
            )

    def get_pair_profile(
        self,
        a: dict[str, Any],
        b: dict[str, Any],
        preset: dict[str, Any] | None = None,
    ) -> PairProfile:
        raise EnvGuardError(
            "PROVIDER_UNAVAILABLE",
            "vendor_http not enabled in S2 (no network)",
            {"reason": "stub"},
        )
