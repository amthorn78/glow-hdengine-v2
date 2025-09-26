import json, hashlib, pathlib

def _loadp(p: pathlib.Path):
    b = p.read_bytes()
    assert b.endswith(b"\n") and not b[:-1].endswith(b"\n")
    return json.loads(b.decode("utf-8")), hashlib.sha256(b).hexdigest()

def test_g05_and_g08_goldens_identity_and_shape():
    G = pathlib.Path("tests/goldens")
    for stem in ("g05_adjacency_only","g08_throat_em_bonus_paced","g08_throat_em_bonus_not_paced"):
        doc, h = _loadp(G/(stem+".json"))
        hs = (G/(stem+".json.sha256")).read_text().strip()
        assert h == hs
        # Public contract: numeric-free except booleans; keys present
        assert isinstance(doc.get("eligible"), bool)
        assert isinstance(doc.get("bands"), list)
        assert "idempotence_hash" in doc and isinstance(doc["idempotence_hash"], str) and len(doc["idempotence_hash"])==64
