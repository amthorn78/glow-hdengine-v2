from __future__ import annotations
import os
from typing import Dict, Any
from flask import Blueprint, request, Response
from engine.presenter import emit_public
from engine.compat.errors import error_envelope
from engine.compat.compute import compat_public
from engine.validation.viewer_prefs import validate_viewer_prefs

compat_blueprint = Blueprint("compat", __name__, url_prefix="/api/compat/v1")


def _writer_payload(env: Dict[str, Any], *, status: int) -> Response:
    payload = emit_public(env)
    resp = Response(payload, status=status, mimetype="application/json; charset=utf-8")
    resp.headers["Cache-Control"] = "no-store"
    resp.headers.pop("ETag", None)
    resp.headers.pop("Content-Encoding", None)
    resp.headers["Content-Length"] = str(len(payload))
    return resp


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


def _collect_keys_list(body: Dict[str, Any]) -> list[str]:
    keys: list[str] = []
    for cat in body.get("categories", []):
        if not isinstance(cat, dict):
            continue
        for key_name in ("personal_key", "shared_key"):
            value = cat.get(key_name)
            if isinstance(value, str) and value and not value.isdigit():
                keys.append(value)
    return keys


@compat_blueprint.before_app_request
def _compat_writer_transport_guard():
    if request.path.rstrip("/") != "/api/compat/v1":
        return None
    if request.method == "HEAD":
        return _writer_head_response()
    if request.method == "OPTIONS":
        return _writer_options_response()
    return None

# Minimal id resolver (fixtures/people.json optional). Fallback: build from ids.
def _resolve_person_by_id(pid: str) -> Dict[str,Any]:
    return {"person_uid": pid}

@compat_blueprint.get("")
def get_ids_only():
    if request.data:  # reject GET with body
        env = error_envelope("invalid_json")
        return _writer_payload(env, status=400)
    body = {"ok": True, "schema": "v1"}
    return _writer_payload(body, status=200)

@compat_blueprint.route("", methods=["POST"], provide_automatic_options=False)
def post_json():
    if (os.environ.get("APP_ENV") or "").lower() == "prod":
        env = error_envelope("ERR_NOT_FOUND")
        return _writer_payload(env, status=404)
    data = request.get_json(silent=True) or {}
    a, b = data.get("a"), data.get("b")
    a_id, b_id = data.get("a_id"), data.get("b_id")
    # Reject mixing id+payload per party
    if (a and a_id) or (b and b_id) or ((a_id or b_id) and (a or b)):
        env = error_envelope("invalid_json")
        return _writer_payload(env, status=400)
    if a_id or b_id:
        if not isinstance(a_id, str) or not isinstance(b_id, str):
            env = error_envelope("invalid_json")
            return _writer_payload(env, status=400)
        a = _resolve_person_by_id(a_id)
        b = _resolve_person_by_id(b_id)
    if not isinstance(a, dict) or not isinstance(b, dict) or "person_uid" not in a or "person_uid" not in b:
        env = error_envelope("invalid_json")
        return _writer_payload(env, status=400)
    vp = data.get("viewer_prefs") or {}
    err = validate_viewer_prefs(vp)
    if err:
        return _writer_payload(err, status=400)
    body = compat_public(
        a, b, vp["top_category"], vp["weights"],
        engine_tag="dev", release_id="dev", invocation_tag="INV-DEV",
    )
    body = dict(body)
    body["keys"] = _collect_keys_list(body)
    return _writer_payload(body, status=200)


@compat_blueprint.route("", methods=["HEAD"], provide_automatic_options=False)
def post_json_head():
    return _writer_head_response()


@compat_blueprint.route("", methods=["OPTIONS"], provide_automatic_options=False)
def post_json_options():
    return _writer_options_response()
