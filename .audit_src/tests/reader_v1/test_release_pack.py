import json, re, subprocess, os
HEX64 = re.compile(r"^[0-9a-f]{64}\n$")
def test_release_pack_manifest_and_id(tmp_path, monkeypatch):
    # Pass file list to script via env
    files = "\n".join([
        "schemas/reader.v1.schema.json",
        "goldens/reader/v1/g01_minimal_ineligible.json",
        "goldens/reader/v1/g03_open_leader.json",
        "goldens/reader/v1/g04_warm_leader.json",
        "goldens/reader/v1/g05_cool_leader.json",
        "goldens/reader/v1/g06_error_invalid_input.json",
        "goldens/reader/v1/g02_ab_ba_parity_A.jsonl",
        "goldens/reader/v1/g02_ab_ba_parity_B.jsonl",
    ])
    env = dict(os.environ)
    env["FILES"] = files
    subprocess.check_call(["bash","scripts/make_release_pack.sh"], env=env)
    man = json.load(open("artifacts/release_pack_manifest.json","r",encoding="utf-8"))
    rid = open("artifacts/release_id.txt","r",encoding="utf-8").read()
    assert isinstance(man["files"], list) and len(man["files"]) >= 7
    assert HEX64.match(rid)
