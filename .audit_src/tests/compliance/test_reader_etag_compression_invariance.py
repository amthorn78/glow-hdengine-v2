from __future__ import annotations
import re
from tests._helpers.app_import import get_app_factory

_HEX64 = re.compile(r'^"[0-9a-f]{64}"$')

def test_etag_identical_across_encodings_identity_gzip_br():
    create_app = get_app_factory()
    app = create_app()
    with app.test_client() as c:
        etags = {}
        for enc in ("identity", "gzip", "br"):
            r = c.get("/reader", headers={"Accept-Encoding": enc})
            assert r.status_code == 200
            etag = r.headers.get("ETag")
            assert etag and _HEX64.match(etag)
            etags[enc] = etag
            # Vary must include Accept-Encoding
            assert "Accept-Encoding" in (r.headers.get("Vary",""))
        # Invariance: same strong ETag across encodings
        assert etags["identity"] == etags["gzip"] == etags["br"]
