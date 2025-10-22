from __future__ import annotations
from typing import Dict, Any
from core.stable.sercanon import stable_idempotence_hash

def idempotence_hash(payload: Dict[str, Any]) -> str:
    # Masks _admin_debug/_diagnostics per canon; returns hex sha256
    return stable_idempotence_hash(payload)
