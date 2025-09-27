
from __future__ import annotations
import os
from typing import Final

class NetworkDisabledError(RuntimeError):
    """Raised when a network call is attempted while SAFE_MODE is enabled."""

_SAFE_TRUTHY: Final = {"1","true","yes","on"}

def safe_mode_enabled() -> bool:
    val = os.getenv("SAFE_MODE")
    if val is None:
        # Default ON in CI/pytest; OFF otherwise
        return bool(os.getenv("CI") or os.getenv("PYTEST_CURRENT_TEST"))
    return val.strip().lower() in _SAFE_TRUTHY

def require_network(service: str = "network") -> None:
    if safe_mode_enabled():
        raise NetworkDisabledError(f"SAFE_MODE active; {service} calls are disabled.")
