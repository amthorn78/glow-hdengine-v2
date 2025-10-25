from flask import Flask, request as _req
from adapter.http_reader import bp  # existing blueprint with /internal/version

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp, url_prefix="")  # mount at /
    @app.after_request
    def _strip_etag_on_internal(resp):
        if resp.headers.get("ETag") and _req.path.startswith("/internal/"):
            resp.headers.pop("ETag", None)
        return resp
    return app
