from flask import Flask, request as _req
from adapter.http_reader import bp  # existing blueprint with /internal/version
from engine.http.compat_handler import (
    compat_blueprint,
    compat_error_response,
    is_compat_request_path,
)

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp, url_prefix="")  # mount at /
    app.register_blueprint(compat_blueprint)
    @app.after_request
    def _strip_etag_on_internal(resp):
        if (
            is_compat_request_path(_req.path)
            and resp.status_code in (404, 405)
            and resp.mimetype == "text/html"
        ):
            return compat_error_response(resp.status_code)
        if resp.headers.get("ETag") and _req.path.startswith("/internal/"):
            resp.headers.pop("ETag", None)
        return resp
    return app
