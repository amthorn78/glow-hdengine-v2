from flask import Flask, request, Response
from scripts.hdctl import compat_public_stub, sercanon  # shared helpers for byte identity

app = Flask(__name__)

@app.post("/reader")
def reader():
    data = request.get_json(force=True, silent=True) or {}
    a = data.get("a", {}) or {}
    b = data.get("b", {}) or {}
    body = sercanon(compat_public_stub(a, b))
    return Response(body, mimetype="application/json; charset=utf-8"), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
