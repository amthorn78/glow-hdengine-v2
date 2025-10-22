from __future__ import annotations
from typing import Dict, Tuple

# Canonical error messages (exact strings, tests assert these)
ERROR_MESSAGES: Dict[str, str] = {
    "invalid_json": "malformed or mixed id/payload: supply either a_id/b_id or a/b objects",
    "invalid_prefs": "viewer_prefs.weights must include all 10 categories as integers 0..100",
    "missing_narrative_key": "narrative key not found for category/band/perspective",
}

def error_envelope(code: str) -> Dict[str, object]:
    msg = ERROR_MESSAGES.get(code, "unknown error")
    return {"ok": False, "code": code, "error": msg}
