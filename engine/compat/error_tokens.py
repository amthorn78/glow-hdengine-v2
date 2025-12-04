from __future__ import annotations

from typing import Dict


# Canonical governed error tokens (PF04/PF05 style: UPPER_SNAKE)
ERROR_TOKEN_MAP: Dict[str, Dict[str, object]] = {
    # Compat/Reader inputs
    "ERR_COMPAT_INVALID_JSON": {
        "message": "malformed or mixed id/payload: supply either a_id/b_id or a/b objects",
        "aliases": ("invalid_json",),
    },
    "ERR_INVALID_VIEWER_PREFS": {
        "message": "viewer_prefs.weights must include all 10 categories as integers 0..100",
        "aliases": ("invalid_prefs",),
    },
    "ERR_MISSING_NARRATIVE_KEY": {
        "message": "narrative key not found for category/band/perspective",
        "aliases": ("missing_narrative_key",),
    },
    "ERR_READER_INVALID_VERSION": {
        "message": "unsupported reader version",
        "aliases": ("invalid_version",),
    },
    "ERR_READER_FORBIDDEN": {
        "message": "reader endpoint disabled",
        "aliases": ("forbidden",),
    },
    "ERR_READER_MISSING_PARAM": {
        "message": "missing required reader parameters",
        "aliases": ("missing_param",),
    },
    "ERR_READER_INVALID_CHART": {
        "message": "invalid reader payload",
        "aliases": ("invalid_chart",),
    },
    "ERR_READER_MISSING_TZ_A": {
        "message": "missing tz for party A",
        "aliases": ("missing_tz_A",),
    },
    "ERR_READER_MISSING_TZ_B": {
        "message": "missing tz for party B",
        "aliases": ("missing_tz_B",),
    },
    "ERR_READER_INVALID_PATH": {
        "message": "invalid chart path",
        "aliases": ("invalid_path",),
    },

    # Writer/diagnostic errors
    "ERR_WRITER_UNAUTHORIZED": {
        "message": "authorization required",
        "aliases": ("unauthorized",),
    },
    "ERR_WRITER_FORBIDDEN": {
        "message": "insufficient scope",
        "aliases": ("forbidden",),
    },
    "ERR_WRITER_INVALID_CONTENT_TYPE": {
        "message": "expected application/json; charset=utf-8",
        "aliases": ("invalid_content_type",),
    },
    "ERR_WRITER_INVALID_JSON": {
        "message": "malformed JSON request",
    },
    "ERR_WRITER_INVALID_INPUT": {
        "message": "schema validation failed",
        "aliases": ("invalid_input",),
    },
    "ERR_WRITER_UNKNOWN_KEY": {
        "message": "unknown request key",
        "aliases": ("unknown_key",),
    },
    "ERR_WRITER_REQUEST_TOO_LARGE": {
        "message": "request body exceeds 32 KiB",
        "aliases": ("request_too_large",),
    },
    "ERR_WRITER_RAILS_CLOSED": {
        "message": "rails are closed",
        "aliases": ("rails_closed",),
    },

    # Adapter generic
    "ERR_NOT_FOUND": {
        "message": "not found",
        "aliases": ("not_found",),
    },
}


def canonical_token_for(code: str) -> str:
    code_upper = code.upper()
    if code_upper in ERROR_TOKEN_MAP:
        return code_upper
    for token, meta in ERROR_TOKEN_MAP.items():
        for alias in meta.get("aliases", ()):
            if alias == code or alias.upper() == code_upper:
                return token
    return code_upper
