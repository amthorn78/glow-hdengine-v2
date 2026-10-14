from flask import Flask, Response, request as _req
from adapter.http_reader import api_bp, bp  # dev/internal blueprint and the production Reader blueprint
from engine.compat.errors import error_envelope
from engine.presenter.emitter import emit_public
from engine.http.compat_handler import (
    compat_blueprint,
    compat_error_response,
    is_compat_request_path,
)

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp, url_prefix="")  # mount at /
    app.register_blueprint(api_bp, url_prefix="/api")  # production Reader: POST /api/reader (PF05 §5.4)
    app.register_blueprint(compat_blueprint)

    def _not_found_envelope_response(status: int, allow: str | None) -> Response:
        # The canonical ERR_NOT_FOUND error_v1 envelope through the presenter,
        # no-store, no ETag, application/json (PF05 §5.2 item 1; §5.5 for compat).
        payload = emit_public(error_envelope("ERR_NOT_FOUND"))
        resp = Response(payload, status=status, mimetype="application/json; charset=utf-8")
        resp.headers["Cache-Control"] = "no-store"
        if allow:
            resp.headers["Allow"] = allow
        resp.headers.pop("ETag", None)
        resp.headers.pop("Content-Encoding", None)
        resp.headers["Content-Length"] = str(len(payload))
        return resp

    @app.errorhandler(404)
    def _governed_not_found(err):  # type: ignore[override]
        # An unknown path, compat or not, answers the governed envelope.
        return _not_found_envelope_response(404, None)

    @app.errorhandler(405)
    def _governed_method_not_allowed(err):  # type: ignore[override]
        if is_compat_request_path(_req.path):
            # PF05 §5.5: a converted compat 405 keeps Flask's Allow as Flask built it.
            return _not_found_envelope_response(405, err.get_response().headers.get("Allow"))
        # Elsewhere the routing Allow is sorted for deterministic bytes.
        return _not_found_envelope_response(405, ", ".join(sorted(err.valid_methods or ())))

    @app.after_request
    def _strip_etag_on_internal(resp):
        if (
            is_compat_request_path(_req.path)
            and resp.status_code in (404, 405)
            and resp.mimetype == "text/html"
        ):
            return compat_error_response(
                resp.status_code,
                allow=resp.headers.get("Allow") if resp.status_code == 405 else None,
            )
        if resp.headers.get("ETag") and _req.path.startswith("/internal/"):
            resp.headers.pop("ETag", None)
        return resp
    return app
