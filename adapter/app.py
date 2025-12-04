from __future__ import annotations
from adapter.wsgi import create_app

# For `flask --app adapter.app run`
app = create_app()
