
 - Pins: `python scripts/ensure_env.py` → `[ENV] OK`
 - Tests: `pytest -q tests/test_sercanon.py`
 <!-- EPIC-004 PATCH: RUN posture -->
 ### Deterministic run posture (Reader)
 ```bash
 python -m adapter.http_reader
 ```
 
 Bind target for captures: http://127.0.0.1:5000
 
 Environment for reproducible bytes/headers (same shell):
 ```
 PYTHONHASHSEED=0
 PYTHONUTF8=1
 TZ=UTC
 SAFE_MODE=1
 ```
 
 Auto-reload: **off** when capturing evidence.
 
 <!-- EPIC-004 RUN posture -->
 ```bash
 python -m adapter.http_reader
 ```
 Bind: http://127.0.0.1:5000  ·  Env: PYTHONHASHSEED=0 PYTHONUTF8=1 TZ=UTC SAFE_MODE=1  ·  Auto-reload: off
+
+---
+
+## RUN — Production start (EPIC-005, Railway)
+
+Use the exact start line that shipped in EPIC-005 (tactical; normalize later if desired):
+
+```bash
+python -m pip install --no-cache-dir -r requirements.txt \
+  && python -m gunicorn 'adapter.factory:create_app()' \
+     --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 30
+```
+
+Evidence: `artifacts/validation/service_cmd.txt` *(deferred to HDE-EPIC-006 if not yet captured)*
