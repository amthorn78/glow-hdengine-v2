from __future__ import annotations
import os
from flask import Flask
from adapter.http_reader import get_reader_bp
from engine.emit_public import emit_public_envelope

def create_app() -> Flask:
    if os.environ.get("APP_ENV","dev") != "dev":
        raise SystemExit("DEV HARNESS ONLY: set APP_ENV=dev")
    app = Flask(__name__)
    bp = get_reader_bp(emit_public_envelope)
    app.register_blueprint(bp, url_prefix="/api")
    @app.get("/health")
    def health(): return ("ok\n", 200, {"Content-Type":"text/plain; charset=utf-8"})
    return app

app = create_app()

if __name__ == "__main__":
    app.run(host=os.environ.get("HOST","127.0.0.1"), port=int(os.environ.get("PORT","5000")), debug=False)
