import json, os, re, subprocess
from pathlib import Path

HEX64 = re.compile(r"^[0-9a-f]{64}\n$")
MANIFEST = Path("artifacts/release_pack_manifest.json")
RELEASE_ID = Path("artifacts/release_id.txt")
FILES = [
    "schemas/reader.v1.schema.json",
    "goldens/reader/v1/g01_minimal_ineligible.json",
    "goldens/reader/v1/g03_harmony_open.json",
    "goldens/reader/v1/g04_harmony_warm.json",
    "goldens/reader/v1/g05_harmony_cool.json",
    "goldens/reader/v1/g07_harmony_glow.json",
    "goldens/reader/v1/g06_error_invalid_input.json",
    "goldens/reader/v1/g02_ab_ba_parity_A.jsonl",
    "goldens/reader/v1/g02_ab_ba_parity_B.jsonl",
]


def test_release_pack_manifest_and_id(tmp_path, monkeypatch):
    # The script's default list and this list are the same covenant set.
    script = Path("scripts/make_release_pack.sh").read_text(encoding="utf-8")
    for name in FILES:
        assert name in script, name
    assert "_leader" not in script
    before = {path: path.read_bytes() for path in (MANIFEST, RELEASE_ID)}

    # Pass file list to script via env
    env = dict(os.environ)
    env["FILES"] = "\n".join(FILES)
    subprocess.check_call(["bash", "scripts/make_release_pack.sh"], env=env)

    man = json.loads(MANIFEST.read_text(encoding="utf-8"))
    rid = RELEASE_ID.read_text(encoding="utf-8")
    assert man["files"] == FILES
    assert HEX64.match(rid)
    # The tracked artifacts are byte-idempotent under their owner: the run changes nothing.
    assert {path: path.read_bytes() for path in (MANIFEST, RELEASE_ID)} == before
    status = subprocess.run(
        ["git", "status", "--short", "--", str(MANIFEST), str(RELEASE_ID)],
        check=True, capture_output=True, text=True,
    ).stdout
    assert status == "", status
