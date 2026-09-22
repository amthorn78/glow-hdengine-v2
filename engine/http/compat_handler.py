from __future__ import annotations
import os
from typing import Dict, Any
from flask import Blueprint, request, Response
from adapter.env_guard import _compute_env_mode
from engine.presenter import emit_public
from engine.bodygraph.mapped_cache import MappedCacheError, read_current_mapped_bodygraph
from engine.bodygraph.projection import BodyGraphProjectionError
from engine.bodygraph.resolver import ResolvedCompatChart, projection_refusal, resolve_compat_chart
from engine.compat.compute import evaluate_pair, evaluation_party
from engine.compat.error_tokens import MAGIC10_HTTP_STATUS, CompatBoundaryError, admission_token_for
from engine.compat.errors import error_envelope
from engine.config.registry_loader import RegistryConfigError
from engine.db import DBAccess
from engine.db.errors import AdapterError
from engine.validation.viewer_prefs import normalize_viewer_prefs, validate_viewer_prefs
from engine.compat.ordering import UID_RE

compat_blueprint = Blueprint("compat", __name__, url_prefix="/api/compat/v1")


def is_compat_request_path(path: str) -> bool:
    prefix = (compat_blueprint.url_prefix or "").rstrip("/")
    normalized = path.rstrip("/")
    return normalized == prefix or normalized.startswith(f"{prefix}/")


def _writer_payload(
    env: Dict[str, Any], *, status: int, allow: str | None = None
) -> Response:
    payload = emit_public(env)
    resp = Response(payload, status=status, mimetype="application/json; charset=utf-8")
    resp.headers["Cache-Control"] = "no-store"
    if allow:
        resp.headers["Allow"] = allow
    resp.headers.pop("ETag", None)
    resp.headers.pop("Content-Encoding", None)
    resp.headers["Content-Length"] = str(len(payload))
    return resp


def compat_error_response(status: int, *, allow: str | None = None) -> Response:
    return _writer_payload(error_envelope("ERR_NOT_FOUND"), status=status, allow=allow)


class _WriterTransportResponse(Response):
    def get_wsgi_headers(self, environ):  # type: ignore[override]
        headers = super().get_wsgi_headers(environ)
        if self.status_code == 204:
            headers["Content-Length"] = "0"
        return headers


def _writer_head_response() -> Response:
    resp = _WriterTransportResponse(b"", status=405)
    resp.headers["Allow"] = "POST, OPTIONS"
    resp.headers["Cache-Control"] = "no-store"
    resp.headers["Content-Length"] = "0"
    resp.headers.pop("Content-Type", None)
    resp.headers.pop("ETag", None)
    resp.headers.pop("Content-Encoding", None)
    return resp


def _writer_options_response() -> Response:
    resp = _WriterTransportResponse(b"", status=204)
    resp.headers["Allow"] = "POST, OPTIONS"
    resp.headers["Cache-Control"] = "no-store"
    resp.headers["Content-Length"] = "0"
    resp.direct_passthrough = False
    resp.set_data(b"")
    resp.headers.pop("Content-Type", None)
    resp.headers.pop("ETag", None)
    resp.headers.pop("Content-Encoding", None)
    return resp


def _boundary_status(exc: CompatBoundaryError) -> int:
    if exc.token == "ERR_NOT_FOUND":
        return 404
    return MAGIC10_HTTP_STATUS.get(exc.token, 422)


def _admission_token(exc: RegistryConfigError) -> str:
    return admission_token_for(getattr(exc, "code", None))


def _current_row_lookup(canonical_user_id: str):
    """Input class 2: one parameterized read-only current-row lookup, no fallback."""

    try:
        db = DBAccess.for_current_env()
    except AdapterError as exc:
        raise CompatBoundaryError("resolver_unavailable", detail=str(getattr(exc, "code", "adapter"))) from exc
    try:
        return read_current_mapped_bodygraph(db, canonical_user_id)
    except MappedCacheError as exc:
        reason = "resolver_unavailable" if exc.code in {"DB_QUERY_FAILED", "DB_ROW_CONTRACT_VIOLATED"} else "chart_invalid"
        raise CompatBoundaryError(reason, detail=exc.code) from exc
    except BodyGraphProjectionError as exc:
        raise projection_refusal(exc) from None


def _resolve_stored_party(person_id: str) -> ResolvedCompatChart:
    return resolve_compat_chart({"user_id": person_id}, source_policy="local", env=None, local_lookup=_current_row_lookup)


@compat_blueprint.before_app_request
def _compat_writer_transport_guard():
    if not is_compat_request_path(request.path):
        return None
    if _compute_env_mode(os.environ) == "prod":
        return compat_error_response(404)
    if request.path.rstrip("/") != (compat_blueprint.url_prefix or "").rstrip("/"):
        return None
    if request.method == "HEAD":
        return _writer_head_response()
    if request.method == "OPTIONS":
        return _writer_options_response()
    return None

@compat_blueprint.get("")
def get_ids_only():
    if request.data:  # reject GET with body
        env = error_envelope("invalid_json")
        return _writer_payload(env, status=400)
    body = {"ok": True, "schema": "v1"}
    return _writer_payload(body, status=200)

@compat_blueprint.route("", methods=["POST"], provide_automatic_options=False)
def post_json():
    data = request.get_json(silent=True) or {}
    a, b = data.get("a"), data.get("b")
    a_id, b_id = data.get("a_id"), data.get("b_id")
    # Reject mixing id+payload per party
    if (a and a_id) or (b and b_id) or ((a_id or b_id) and (a or b)):
        env = error_envelope("invalid_json")
        return _writer_payload(env, status=400)
    stored_ids = bool(a_id or b_id)
    if stored_ids:
        if (
            not isinstance(a_id, str)
            or not isinstance(b_id, str)
            or not UID_RE.match(a_id)
            or not UID_RE.match(b_id)
        ):
            env = error_envelope("invalid_json")
            return _writer_payload(env, status=400)
    elif not isinstance(a, dict) or not isinstance(b, dict) or "person_uid" not in a or "person_uid" not in b:
        env = error_envelope("invalid_json")
        return _writer_payload(env, status=400)
    vp = data.get("viewer_prefs") or {}
    err = validate_viewer_prefs(vp)
    if err:
        return _writer_payload(err, status=400)
    # Viewer preferences are an input-side handoff only; they never enter scoring.
    normalize_viewer_prefs(vp)
    try:
        if stored_ids:
            left = _resolve_stored_party(a_id)
            right = _resolve_stored_party(b_id)
        else:
            # Inline parties must be complete mapped charts (input class 1).
            left = resolve_compat_chart(a, source_policy="local", env=None)
            right = resolve_compat_chart(b, source_policy="local", env=None)
        body = evaluate_pair(evaluation_party(left), evaluation_party(right))
    except CompatBoundaryError as exc:
        return _writer_payload(error_envelope(exc.token), status=_boundary_status(exc))
    except RegistryConfigError as exc:
        return _writer_payload(error_envelope(_admission_token(exc)), status=503)
    # PF05 §5.5: the canonical ``magic10_compat_result.v1`` document (or the PF01
    # §4.7 carrier for a valid self-pair); no ``keys`` list and no Reader bytes.
    return _writer_payload(dict(body), status=200)


@compat_blueprint.route("", methods=["HEAD"], provide_automatic_options=False)
def post_json_head():
    return _writer_head_response()


@compat_blueprint.route("", methods=["OPTIONS"], provide_automatic_options=False)
def post_json_options():
    return _writer_options_response()
