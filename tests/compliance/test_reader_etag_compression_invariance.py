from __future__ import annotations
import re
from pathlib import Path
from tests._helpers.app_import import get_app_factory
from tests.support.pr04_fixtures import build_bundle, build_pack, inject_seams

_HEX64 = re.compile(r'^"[0-9a-f]{64}"$')

def test_etag_identical_across_encodings_identity_gzip_br(monkeypatch, tmp_path):
    monkeypatch.setenv("APP_ENV", "dev")
    # An eligible pair is served only against an admitted release.
    inject_seams(monkeypatch, build_bundle(tmp_path), build_pack(tmp_path))
    create_app = get_app_factory()
    app = create_app()
    # Dev GET /reader requires exactly v=1 and a complete fixture pair (PF05 5.4).
    q = {
        "v": "1",
        "a": str(Path("fixtures/charts/alice.json").resolve()),
        "b": str(Path("fixtures/charts/bob.json").resolve()),
        "a_tz": "UTC",
        "b_tz": "UTC",
    }
    with app.test_client() as c:
        etags = {}
        for enc in ("identity", "gzip", "br"):
            r = c.get("/reader", query_string=q, headers={"Accept-Encoding": enc})
            assert r.status_code == 200
            etag = r.headers.get("ETag")
            assert etag and _HEX64.match(etag)
            etags[enc] = etag
            # Vary must include Accept-Encoding
            assert "Accept-Encoding" in (r.headers.get("Vary",""))
        # Invariance: same strong ETag across encodings
        assert etags["identity"] == etags["gzip"] == etags["br"]
