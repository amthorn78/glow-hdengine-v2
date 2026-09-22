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

    # Magic-10 Reader and internal failure contract (PF05 §5.2.3).  Registered
    # here first and regenerated into errors/token_map/token_map.json only through
    # tools/errors/generate_error_artifacts.py.  Existing tokens keep their
    # messages; the transport status lives in MAGIC10_HTTP_STATUS below.
    "ERR_READER_INVALID_INPUT": {
        "message": "invalid Reader request",
    },
    "ERR_M10_PERSON_UNRESOLVED": {
        "message": "BodyGraph not found",
    },
    "ERR_M10_RESOLVER_UNAVAILABLE": {
        "message": "BodyGraph resolver unavailable",
    },
    "ERR_M10_BODYGRAPH_INCOMPLETE": {
        "message": "BodyGraph is incomplete",
    },
    "ERR_M10_GATES_MISSING": {
        "message": "Gate data is required",
    },
    "ERR_M10_GATES_INVALID": {
        "message": "Gate data is invalid",
    },
    "ERR_M10_LEGACY_INPUT_UNSUPPORTED": {
        "message": "legacy scoring input is unsupported",
    },
    "ERR_M10_CONFIG_MISMATCH": {
        "message": "Magic10 configuration mismatch",
    },
    "ERR_M10_MANIFEST_MISMATCH": {
        "message": "Magic10 release manifest mismatch",
    },
    "ERR_M10_RESULT_SCHEMA_MISMATCH": {
        "message": "Magic10 result schema mismatch",
    },
    "ERR_M10_STALE_RESULT": {
        "message": "Magic10 cached result is stale",
    },
}


# PF05 §5.2.3 transport statuses for the production Reader route.  Application
# boundaries (CLI, /api/compat/v1, conjunction) keep their existing carriers.
MAGIC10_HTTP_STATUS: Dict[str, int] = {
    "ERR_READER_INVALID_INPUT": 422,
    "ERR_READER_INVALID_CHART": 422,
    "ERR_M10_PERSON_UNRESOLVED": 404,
    "ERR_M10_RESOLVER_UNAVAILABLE": 503,
    "ERR_M10_BODYGRAPH_INCOMPLETE": 503,
    "ERR_M10_GATES_MISSING": 422,
    "ERR_M10_GATES_INVALID": 422,
    "ERR_M10_LEGACY_INPUT_UNSUPPORTED": 422,
    "ERR_M10_CONFIG_MISMATCH": 503,
    "ERR_M10_MANIFEST_MISMATCH": 503,
    "ERR_M10_RESULT_SCHEMA_MISMATCH": 503,
    "ERR_M10_STALE_RESULT": 503,
}


# Stable private failure classes raised at the Magic-10 application boundary.
# Each maps to the governed application-boundary token used by CLI, compat and
# conjunction carriers, and to the PF05 §5.2.3 token/status used by POST /reader.
BOUNDARY_REASONS: Dict[str, tuple[str, str, int]] = {
    # reason: (application token, Reader transport token, Reader status)
    "input_invalid": ("ERR_COMPAT_INVALID_JSON", "ERR_READER_INVALID_INPUT", 422),
    "chart_missing": ("ERR_READER_MISSING_PARAM", "ERR_M10_BODYGRAPH_INCOMPLETE", 503),
    "chart_incomplete": ("ERR_READER_MISSING_PARAM", "ERR_M10_BODYGRAPH_INCOMPLETE", 503),
    "chart_invalid": ("ERR_READER_INVALID_CHART", "ERR_M10_BODYGRAPH_INCOMPLETE", 503),
    "gates_missing": ("ERR_READER_MISSING_PARAM", "ERR_M10_BODYGRAPH_INCOMPLETE", 503),
    # PF05 §5.2.3: a stored BodyGraph whose Gate array is duplicate, malformed,
    # noncanonical or outside 1..64 is ERR_M10_BODYGRAPH_INCOMPLETE/503 on the Reader
    # transport -- the request identities were valid and the server-side chart is
    # unusable, so 422 would blame the client.  ERR_M10_GATES_INVALID/422 belongs to
    # the separate internal/CLI Gate-value row, which the application token above
    # still serves.
    "gates_invalid": ("ERR_READER_INVALID_CHART", "ERR_M10_BODYGRAPH_INCOMPLETE", 503),
    "identity_unresolved": ("ERR_READER_MISSING_PARAM", "ERR_M10_BODYGRAPH_INCOMPLETE", 503),
    "identity_invalid": ("ERR_READER_INVALID_CHART", "ERR_READER_INVALID_INPUT", 422),
    "identity_conflict": ("ERR_READER_INVALID_CHART", "ERR_M10_BODYGRAPH_INCOMPLETE", 503),
    "provenance_mismatch": ("ERR_READER_INVALID_CHART", "ERR_M10_RESOLVER_UNAVAILABLE", 503),
    "inconsistent_self": ("ERR_READER_INVALID_CHART", "ERR_READER_INVALID_CHART", 422),
    "person_unresolved": ("ERR_NOT_FOUND", "ERR_M10_PERSON_UNRESOLVED", 404),
    "resolver_unavailable": ("ERR_M10_RESOLVER_UNAVAILABLE", "ERR_M10_RESOLVER_UNAVAILABLE", 503),
    "legacy_input": ("ERR_M10_LEGACY_INPUT_UNSUPPORTED", "ERR_M10_LEGACY_INPUT_UNSUPPORTED", 422),
    "admission_config": ("ERR_M10_CONFIG_MISMATCH", "ERR_M10_CONFIG_MISMATCH", 503),
    "admission_manifest": ("ERR_M10_MANIFEST_MISMATCH", "ERR_M10_MANIFEST_MISMATCH", 503),
    "result_schema": ("ERR_M10_RESULT_SCHEMA_MISMATCH", "ERR_M10_RESULT_SCHEMA_MISMATCH", 503),
    "stale_result": ("ERR_M10_STALE_RESULT", "ERR_M10_STALE_RESULT", 503),
    "narrative_key": ("ERR_MISSING_NARRATIVE_KEY", "ERR_M10_RESULT_SCHEMA_MISMATCH", 503),
}


class CompatBoundaryError(Exception):
    """Typed, value-free refusal raised at the Magic-10 application boundary.

    ``reason`` is the stable private failure class from ``BOUNDARY_REASONS``;
    ``token`` is the governed application-boundary token; ``reader_token`` and
    ``reader_status`` carry the PF05 §5.2.3 transport mapping used only by the
    production Reader route.  No chart, identity, Gate, path or database value
    is attached: ``detail`` is a short static label such as a projection code.
    """

    def __init__(self, reason: str, *, detail: str | None = None) -> None:
        if reason not in BOUNDARY_REASONS:
            raise ValueError(f"unknown boundary reason: {reason}")
        token, reader_token, reader_status = BOUNDARY_REASONS[reason]
        self.reason = reason
        self.token = token
        self.reader_token = reader_token
        self.reader_status = reader_status
        self.detail = detail
        super().__init__(f"{token}:{reason}" if detail is None else f"{token}:{reason}:{detail}")


def canonical_token_for(code: str) -> str:
    code_upper = code.upper()
    if code_upper in ERROR_TOKEN_MAP:
        return code_upper
    for token, meta in ERROR_TOKEN_MAP.items():
        for alias in meta.get("aliases", ()):
            if alias == code or alias.upper() == code_upper:
                return token
    return code_upper


# PF05 §5.2.3 splits admission failures in two. A defect in the release manifest
# or the admitted release roster -- its identity, version, timestamp, member
# hashes or completeness -- is ERR_M10_MANIFEST_MISMATCH. Everything else the
# registry loader refuses is configuration, ERR_M10_CONFIG_MISMATCH: that
# includes source-hash and source-binding disagreement (MECHANICS_SOURCE_MISMATCH,
# SOURCE_CHANGED, UNBOUND_SOURCE, INVALID_JSON_SOURCE, ...) and registry content
# rosters (CHANNEL_ID_ROSTER_MISMATCH, PROFILE_ROSTER_MISMATCH, ...), none of
# which say anything about the manifest.
#
# Matching "SOURCE" or a bare "ROSTER" captures exactly those, so the markers are
# "MANIFEST" and "RELEASE": every genuine release-roster code carries RELEASE
# (ADMITTED_RELEASE_ROSTER_INVALID, INCOMPLETE_RELEASE_ROSTER,
# RELEASE_ROSTER_MISMATCH, RELEASE_TIMESTAMP_MISMATCH, RELEASE_VERSION_MISMATCH),
# so dropping the bare ROSTER marker loses none of them.
_MANIFEST_ADMISSION_MARKERS = ("MANIFEST", "RELEASE")


def admission_token_for(code: str | None) -> str:
    """The PF05 §5.2.3 token for a registry-loader admission refusal."""

    text = str(code or "")
    if any(marker in text for marker in _MANIFEST_ADMISSION_MARKERS):
        return "ERR_M10_MANIFEST_MISMATCH"
    return "ERR_M10_CONFIG_MISMATCH"
