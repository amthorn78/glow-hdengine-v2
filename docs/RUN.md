# Greenfield 006 — Run Notes
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
