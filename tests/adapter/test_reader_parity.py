import re
from adapter.wsgi import create_app

ETAG_RX = re.compile(r'^"[0-9a-f]{64}"$')

def _app():
    return create_app()

def test_get_200_has_etag_and_bytes_and_headers():
    app = _app()
    with app.test_client() as c:
        r = c.get("/reader")
        assert r.status_code == 200
        assert r.data.endswith(b"\n") and len(r.data) > 1
        et = r.headers.get("ETag", "")
        assert ETAG_RX.match(et), f"bad ETag: {et!r}"
        vary = r.headers.get("Vary","")
        cc   = r.headers.get("Cache-Control","")
        assert "Authorization" in vary and "Accept-Encoding" in vary
        assert "private" in cc and "no-cache" in cc and "must-revalidate" in cc

def test_get_304_on_exact_match_empty_body_and_parity_headers():
    app = _app()
    with app.test_client() as c:
        r1 = c.get("/reader")
        inm = r1.headers["ETag"]
        r2 = c.get("/reader", headers={"If-None-Match": inm})
        assert r2.status_code == 304
        assert r2.data == b""
        # Some frameworks omit Content-Length on 304; accept '0' or missing.
        cl = r2.headers.get("Content-Length")
        assert (cl is None) or (cl == "0")
        # Parity headers must be identical (ETag / Vary / Cache-Control)
        assert r2.headers.get("ETag") == inm
        assert r2.headers.get("Vary") == r1.headers.get("Vary")
        assert r2.headers.get("Cache-Control") == r1.headers.get("Cache-Control")

def test_head_miss_200_empty_body_and_etag_present_and_compression_invariance():
    app = _app()
    with app.test_client() as c:
        # HEAD miss → 200 with empty body
        rh = c.head("/reader")
        assert rh.status_code == 200
        assert rh.data == b""
        assert rh.headers.get("Content-Length") == "0"
        et_head = rh.headers.get("ETag", "")
        assert ETAG_RX.match(et_head)

        # Compression invariance: ETag must not change with Accept-Encoding
        r_id  = c.get("/reader", headers={"Accept-Encoding":"identity"})
        r_gz  = c.get("/reader", headers={"Accept-Encoding":"gzip"})
        assert ETAG_RX.match(r_id.headers.get("ETag",""))
        assert r_id.headers.get("ETag") == r_gz.headers.get("ETag")
