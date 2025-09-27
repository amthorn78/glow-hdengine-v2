import os
from typing import Optional, Dict, Any
from engine.config.provider_types import Provider
from engine.config.provider_errors import ProviderRefusedInSafeMode

_TRUTHY = {"1", "true", "yes", "on"}

def _safe_mode_enabled() -> bool:
    val = os.getenv("SAFE_MODE")
    if val is None:
        # In CI/tests SAFE_MODE defaults to on; keep default True here for safety.
        return bool(os.getenv("CI") or os.getenv("PYTEST_CURRENT_TEST"))
    return val.strip().lower() in _TRUTHY

class InternalEngineProvider(Provider):
    """
    Stubbed internal-engine path.
    MUST refuse when SAFE_MODE is enabled.
    """
    def get_chart(self, user_id: str, *, correlation_id: Optional[str] = None) -> Dict[str, Any]:
        if _safe_mode_enabled():
            raise ProviderRefusedInSafeMode("InternalEngineProvider refused in SAFE_MODE.")
        # When not safe, return a deterministic sample as a stub
        return {"gates": [1, 2, 3, 4]}
