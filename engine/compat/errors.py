from __future__ import annotations
from typing import Dict

from .error_tokens import ERROR_TOKEN_MAP, canonical_token_for

# Legacy alias map preserved for older tests
ERROR_MESSAGES: Dict[str, str] = {}
for token, meta in ERROR_TOKEN_MAP.items():
    for alias in meta.get("aliases", ()):
        ERROR_MESSAGES[alias] = meta["message"]


def error_envelope(code: str, *, details: object | None = None) -> Dict[str, object]:
    token = canonical_token_for(code)
    meta = ERROR_TOKEN_MAP.get(token, {})
    message = meta.get("message", "unknown error")
    envelope: Dict[str, object] = {
        "schema": "v1",
        "ok": False,
        "code": token,
        "error": message,
    }
    if details is not None:
        envelope["details"] = details
    return envelope
