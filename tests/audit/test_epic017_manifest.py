import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST_PATH = ROOT / "audit/EPIC017_MANIFEST.json"
MIRROR_PATH = ROOT / "artifacts/evidence_index.jsonl"

EXPECTED_TOKENS = {
    "TESTS_PASS_OK",
    "DOC_DELTA_PRESENT_OK",
    "CLI_NO_ALT_JSON_OK",
    "CLI_READER_PARITY_OK",
    "CLI_SHOWCOMPAT_CANON_OK",
    "CLI_STDOUT_LF_OK",
    "JSON_CANONICAL_CHECK_OK",
    "TWO_RUN_IDENTITY_OK",
    "COMPOSITE_ABBA_IDENTITY_OK",
    "EVIDENCE_INDEX_UPDATED_OK",
    "MACHINE_MIRROR_UPDATED_OK",
    "EVIDENCE_INDEX_HASH_OK",
    "EVIDENCE_INDEX_MIRROR_OK",
    "EVIDENCE_PATHS_VALIDATED_OK",
    "EVIDENCE_PATH_PROOFS_OK",
    "CI_CHECK_MIRROR_SCHEMA_OK",
    "CI_CHECK_FINAL_LF_OK",
    "CONFIG_GEN_OK",
    "UNKNOWN_IDS_FAIL_CLOSED_OK",
    "TIEBREAK_TOTAL_ORDER_OK",
}


def _load_mirror():
    with MIRROR_PATH.open("r", encoding="utf-8") as handle:
        return {
            (entry["artifact_key"], entry["discovered_physical_path"]): entry
            for entry in (
                json.loads(line)
                for line in handle
                if line.strip()
            )
        }


def _parse_proof(proof_path: Path) -> dict[str, str]:
    data: dict[str, str] = {}
    for line in proof_path.read_text(encoding="utf-8").splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    return data


def test_manifest_includes_expected_tokens():
    manifest = json.loads(MANIFEST_PATH.read_text())
    assert manifest["epic_id"] == "HDE-EPIC017"
    assert set(manifest["tokens"]) == EXPECTED_TOKENS


def test_manifest_entries_match_mirror_and_disk():
    manifest = json.loads(MANIFEST_PATH.read_text())
    mirror = _load_mirror()

    for token, entries in manifest["tokens"].items():
        assert entries, f"token {token} missing entries"
        for entry in entries:
            key = (entry["artifact_key"], entry["discovered_physical_path"])
            assert key in mirror, f"mirror missing {key}"
            mirror_entry = mirror[key]

            path = ROOT / entry["discovered_physical_path"]
            proof = ROOT / entry["proof_anchor"]

            assert path.exists(), f"missing artifact {path}"
            assert proof.exists(), f"missing proof {proof}"

            disk_bytes = path.read_bytes()
            sha = hashlib.sha256(disk_bytes).hexdigest()
            assert len(disk_bytes) == entry["size_bytes"]

            if entry["artifact_key"] != "index.machine_mirror":
                assert sha == entry["sha256"]

            assert mirror_entry["sha256"] == entry["sha256"]
            assert mirror_entry["size_bytes"] == entry["size_bytes"]
            assert mirror_entry["proof_anchor"] == entry["proof_anchor"]

            proof_data = _parse_proof(proof)
            assert proof_data.get("sha256") == entry["sha256"]
            assert int(proof_data.get("size_bytes", "0")) == entry["size_bytes"]
