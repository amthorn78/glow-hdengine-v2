import os, json, hashlib, subprocess, sys, pathlib, time
from adapter.wsgi import create_app

ART_G = pathlib.Path("artifacts/goldens"); ART_G.mkdir(parents=True, exist_ok=True)
ART_H = pathlib.Path("artifacts/headers"); ART_H.mkdir(parents=True, exist_ok=True)

def _sha256(b: bytes) -> str:
    import hashlib
    return hashlib.sha256(b).hexdigest()

def _write_bytes(path: pathlib.Path, b: bytes):
    path.write_bytes(b)
    (path.with_suffix(path.suffix + ".sha256")).write_text(_sha256(b))

def test_public_success_via_hd_cli_and_error_429_via_adapter():
    # --- Success golden via hd_cli (uses canonical serializer, LF-terminated)
    a = pathlib.Path("tests/fixtures/reader_v1/abba_A.json")
    b = pathlib.Path("tests/fixtures/reader_v1/abba_B.json")
    assert a.exists() and b.exists(), "expected reader_v1 ABBA fixtures"
    out = subprocess.check_output([sys.executable, "scripts/hd_cli.py", str(a), str(b)])
    assert out.endswith(b"\n"), "success stdout must end with exactly one LF"
    env = json.loads(out.decode("utf-8"))
    # Public shape checks (no schema change): release_id at root; meta has exactly the two keys
    assert "reader_version" in env and env["reader_version"] == "v1"
    assert "release_id" in env and isinstance(env["release_id"], str) and len(env["release_id"]) >= 8
    assert set(env.get("meta", {}).keys()) == {"engine_tag","invocation_tag"}
    # Persist success golden + sha256
    succ_path = ART_G / "public_success.json"
    _write_bytes(succ_path, out)

    # --- Error golden via adapter (force 429), map Retry-After -> error.retry_after_ms
    app = create_app()
    with app.test_client() as c:
        r = c.get("/_test/429_seconds?sec=7")
        assert r.status_code == 429
        # No ETag on errors; no-store
        assert r.headers.get("ETag") is None
        assert r.headers.get("Cache-Control") == "no-store"
        body = r.data
        assert body.endswith(b"\n"), "error body must end with exactly one LF"
        err = json.loads(body.decode("utf-8"))
        assert err.get("reader_version") == "v1"
        assert "error" in err and isinstance(err["error"], dict)
        # retry_after_ms present and integer (>= 0)
        ms = err["error"].get("retry_after_ms")
        assert isinstance(ms, int) and ms >= 0

        # Persist error golden + headers snapshot
        err_path = ART_G / "public_error_429.json"
        _write_bytes(err_path, body)
        # Minimal headers snapshot (keys-only interest)
        hdr = {
            "status": r.status_code,
            "Cache-Control": r.headers.get("Cache-Control"),
            "ETag": r.headers.get("ETag"),
            "Retry-After": r.headers.get("Retry-After"),
            "Content-Length": r.headers.get("Content-Length"),
        }
        (ART_H / "reader_429_headers.json").write_text(json.dumps(hdr, separators=(",",":"), sort_keys=True))

