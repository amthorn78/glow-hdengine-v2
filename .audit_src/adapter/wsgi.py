from flask import Flask, Blueprint, jsonify, request, make_response
from engine.stable.sercanon import serialize
from adapter.http_reader import bp as reader_bp
from adapter.logging_filter import install as install_logging_filter
from adapter.env_guard import validate_or_fail

def create_app():
    app = Flask(__name__)
    # Minimal identity config (tests may override)
    app.config.setdefault("ENGINE_TAG", "Isis6")
    app.config.setdefault("RELEASE_ID", "rel_dev")

    # Install keys-only logging
    install_logging_filter(app)
    # Env override guard (pre-serve)
    validate_or_fail(app)

    # Register reader blueprint
    app.register_blueprint(reader_bp)
    return app

app = create_app()
