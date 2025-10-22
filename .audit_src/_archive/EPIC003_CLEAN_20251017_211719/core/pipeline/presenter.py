from __future__ import annotations
from typing import Any, Dict, Optional
from core.pipeline.idempotence import idempotence_hash

def present_public(
    bands, eligible, prompt, uncertainty, flags, versions,
    *, admin_debug: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    out: Dict[str, Any] = {
        "bands": list(bands),
        "eligible": bool(eligible),
        "prompt": (prompt if uncertainty != "high" else None),
        "uncertainty": str(uncertainty),
        "flags": list(flags),
        "versions": dict(versions),
    }
    if admin_debug is not None:
        out["_admin_debug"] = admin_debug
    out["idempotence_hash"] = idempotence_hash(out)
    return out
