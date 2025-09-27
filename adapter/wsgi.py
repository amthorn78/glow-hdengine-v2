from flask import Flask
from adapter.http_reader import bp as reader_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(reader_bp)
    return app

app = create_app()
