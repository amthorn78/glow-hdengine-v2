
import json, pathlib
from jsonschema import Draft7Validator

ROOT = pathlib.Path(__file__).resolve().parents[2]

def test_normalized_fixture_schema_and_bytes():
    schema = json.loads((ROOT/"schemas/hdapi.normalized.v1.schema.json").read_text(encoding="utf-8"))
    ndir = ROOT/"fixtures/hdapi/normalized"
    paths = sorted(ndir.glob("*_normalized.json"))
    assert paths, "No normalized fixtures found"
    p = paths[-1]
    raw = p.read_bytes()
    assert raw.endswith(b"\n"), "Must end with single LF"

    obj = json.loads(raw)
    Draft7Validator(schema).validate(obj)

    # Canonical bytes
    canon = json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8") + b"\n"
    assert canon == raw, "Non-canonical bytes"

    # Mechanics sanity
    gates = obj["mechanics"]["gates"]
    assert gates == sorted(set(gates))
    assert all(len(g)==2 and g.isdigit() for g in gates)

    channels = obj["mechanics"]["channels"]
    assert channels == sorted(set(channels))
    assert all(len(c)==5 and c[2]=="-" and c[:2].isdigit() and c[3:].isdigit() for c in channels)

    canon_centers = ["head","ajna","throat","g","ego","spleen","solar_plexus","sacral","root"]
    centers_ids = [c["id"] for c in obj["mechanics"]["centers"]]
    assert centers_ids == canon_centers
