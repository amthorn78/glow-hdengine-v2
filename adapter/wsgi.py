import os
from flask import Flask, Blueprint, jsonify, request, make_response, Response
from engine.presenter.emitter import emit_public
from engine.stable.sercanon import serialize
from adapter.http_reader import bp as reader_bp
from engine.http.compat_handler import compat_blueprint
from adapter.logging_filter import install as install_logging_filter
from adapter.env_guard import validate_or_fail
from engine.compat.errors import error_envelope

def create_app():
    app = Flask(__name__)
    # Minimal identity config (tests may override)
    app.config.setdefault("ENGINE_TAG", "Isis6")
    app.config.setdefault("RELEASE_ID", "rel_dev")

    # Install keys-only logging
    install_logging_filter(app)
    # Env override guard (pre-serve)
    validate_or_fail(app)

    # Register reader + compat blueprints
    app.register_blueprint(reader_bp)
    app.register_blueprint(compat_blueprint)

    def _apply_common_headers(resp: Response) -> Response:
        resp.headers.setdefault("Cache-Control", "no-store")
        resp.headers.setdefault("Content-Type", "application/json; charset=utf-8")
        resp.headers.setdefault("X-Adapter-Version", "v1")
        resp.headers.setdefault("X-Engine-Tag", app.config.get("ENGINE_TAG", ""))
        resp.headers.setdefault("X-Release-Id", app.config.get("RELEASE_ID", ""))
        resp.headers.setdefault("X-Content-Type-Options", "nosniff")
        resp.headers.setdefault("Referrer-Policy", "no-referrer")
        resp.headers.setdefault("X-Frame-Options", "DENY")
        env_mode = (os.environ.get("APP_ENV") or os.environ.get("ENGINE_ENV") or "dev").strip().lower()
        if env_mode in ("prod", "production", "live"):
            resp.headers.setdefault("Strict-Transport-Security", "max-age=31536000; includeSubDomains")
        return resp

    @app.get("/internal/healthz")
    def internal_healthz():
        body = emit_public({"ok": True, "schema": "v1"})
        resp = Response(body, status=200, mimetype="application/json; charset=utf-8")
        return _apply_common_headers(resp)

    @app.get("/internal/readyz")
    def internal_readyz():
        body = emit_public({"ok": True, "schema": "v1"})
        resp = Response(body, status=200, mimetype="application/json; charset=utf-8")
        return _apply_common_headers(resp)

    @app.errorhandler(404)
    def _not_found(err):  # type: ignore[override]
        env = error_envelope("ERR_NOT_FOUND")
        body = emit_public(env)
        resp = Response(body, status=404, mimetype="application/json; charset=utf-8")
        return _apply_common_headers(resp)

    @app.errorhandler(405)
    def _method_not_allowed(err):  # type: ignore[override]
        env = error_envelope("ERR_NOT_FOUND")
        body = emit_public(env)
        resp = Response(body, status=405, mimetype="application/json; charset=utf-8")
        return _apply_common_headers(resp)

    @app.after_request
    def _ensure_common_headers(resp: Response):
        return _apply_common_headers(resp)

    return app

app = create_app()
