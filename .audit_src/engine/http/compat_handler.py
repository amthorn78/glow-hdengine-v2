from __future__ import annotations
from typing import Dict, Any
from flask import Blueprint, request, Response
from engine.presenter import emit_compact_json
from engine.compat.errors import error_envelope
from engine.compat.compute import compat_public
from engine.validation.viewer_prefs import validate_viewer_prefs

compat_blueprint = Blueprint("compat", __name__, url_prefix="/api/compat/v1")

# Minimal id resolver (fixtures/people.json optional). Fallback: build from ids.
def _resolve_person_by_id(pid: str) -> Dict[str,Any]:
    return {"person_uid": pid}

@compat_blueprint.get("")
def get_ids_only():
    a_id = request.args.get("a_id"); b_id = request.args.get("b_id")
    if request.data:  # reject GET with body
        env = error_envelope("invalid_json")
        return Response(emit_compact_json(env)[0], status=400, headers={"Cache-Control":"no-store"},
                        mimetype="application/json; charset=utf-8")
    if not a_id or not b_id:
        env = error_envelope("invalid_json")
        return Response(emit_compact_json(env)[0], status=400, headers={"Cache-Control":"no-store"},
                        mimetype="application/json; charset=utf-8")
    a = _resolve_person_by_id(a_id); b = _resolve_person_by_id(b_id)
    # viewer prefs defaults (equal weights)
    from engine.compat.categories import CATEGORIES_ORDER_V1
    w = {k:50 for k in CATEGORIES_ORDER_V1}
    body = compat_public(a,b, CATEGORIES_ORDER_V1[0], w,
                         engine_tag="dev", release_id="dev", invocation_tag="INV-DEV")
    return Response(emit_compact_json(body)[0], status=200, mimetype="application/json; charset=utf-8")

@compat_blueprint.post("")
def post_json():
    data = request.get_json(silent=True) or {}
    a, b = data.get("a"), data.get("b")
    a_id, b_id = data.get("a_id"), data.get("b_id")
    # Reject mixing id+payload per party
    if (a and a_id) or (b and b_id):
        env = error_envelope("invalid_json")
        return Response(emit_compact_json(env)[0], status=400, headers={"Cache-Control":"no-store"},
                        mimetype="application/json; charset=utf-8")
    if a_id: a = _resolve_person_by_id(a_id)
    if b_id: b = _resolve_person_by_id(b_id)
    if not isinstance(a, dict) or not isinstance(b, dict) or "person_uid" not in a or "person_uid" not in b:
        env = error_envelope("invalid_json")
        return Response(emit_compact_json(env)[0], status=400, headers={"Cache-Control":"no-store"},
                        mimetype="application/json; charset=utf-8")
    vp = data.get("viewer_prefs") or {}
    err = validate_viewer_prefs(vp)
    if err:
        return Response(emit_compact_json(err)[0], status=400, headers={"Cache-Control":"no-store"},
                        mimetype="application/json; charset=utf-8")
    body = compat_public(
        a, b, vp["top_category"], vp["weights"],
        engine_tag="dev", release_id="dev", invocation_tag="INV-DEV",
    )
    return Response(emit_compact_json(body)[0], status=200, mimetype="application/json; charset=utf-8")
