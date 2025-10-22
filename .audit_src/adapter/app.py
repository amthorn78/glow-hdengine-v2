from __future__ import annotations
from flask import Flask
from engine.http.compat_handler import compat_blueprint

def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(compat_blueprint)
    return app

# For `flask --app adapter.app run`
app = create_app()
