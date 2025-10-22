- Flask smoke (no external network; fine inside Codespaces):
```bash
python - <<'PY'
from adapter.wsgi import create_app
app = create_app()
with app.test_client() as c:
  r1 = c.get("/reader"); print("GET 200:", r1.status_code, "ETag:", r1.headers.get("ETag"))
  r2 = c.get("/reader", headers={"If-None-Match": r1.headers["ETag"]}); print("GET 304:", r2.status_code)
  r3 = c.head("/reader"); print("HEAD 200:", r3.status_code, "CL:", r3.headers.get("Content-Length"))
