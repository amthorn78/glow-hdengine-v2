from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BUNDLE_DIR = ROOT / "artifacts" / "epic020" / "bundles"
ACCEPTANCE_MAP = ROOT / "docs" / "acceptance_map_epic020.json"


def _run(cmd: list[str]) -> None:
    env = os.environ.copy()
    env.update(
        {
            "SAFE_MODE": "1",
            "ALLOW_NETWORK": "0",
            "LC_ALL": "C",
            "LANG": "C",
            "TZ": "UTC",
            "APP_ENV": env.get("APP_ENV", "ci"),
        }
    )
    subprocess.check_call(cmd, cwd=ROOT, env=env)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _load_index() -> list[dict[str, object]]:
    return json.loads((ROOT / "docs/evidence/INDEX.json").read_text(encoding="utf-8"))


def _load_mirror() -> dict[tuple[str, str], dict[str, object]]:
    records: dict[tuple[str, str], dict[str, object]] = {}
    for line in (ROOT / "artifacts/evidence_index.jsonl").read_text(encoding="utf-8").splitlines():
        rec = json.loads(line)
        records[(rec["artifact_key"], rec["discovered_physical_path"])] = rec
    return records


def test_epic020_bundle_and_manifest_records_match_index_and_mirror():
    _run([sys.executable, "-m", "tools.evidence.epic020_bundle", "build", "--epic-id", "HDE-EPIC020"])
    _run([sys.executable, "tools/evidence/update_evidence_index.py", "--epic-id", "HDE-EPIC020"])

    manifests = sorted(BUNDLE_DIR.glob("*.manifest.json"))
    assert manifests, "expected EPIC020 bundle manifests to be present"

    acceptance = json.loads(ACCEPTANCE_MAP.read_text(encoding="utf-8"))
    allowed_tokens = set(acceptance.get("token_status", {}))
    assert allowed_tokens, "EPIC020 canon tokens are required for bundle indexing"

    index_entries = _load_index()
    mirror_records = _load_mirror()

    for manifest_path in manifests:
        manifest_payload = json.loads(manifest_path.read_text(encoding="utf-8"))
        bundle_key = manifest_payload["artifact_key"]
        produced_at = manifest_payload["produced_at_utc"]
        bundle_rel = manifest_payload["bundle_path"]
        bundle_path = ROOT / bundle_rel

        manifest_rel = manifest_path.relative_to(ROOT).as_posix()

        bundle_records = [
            entry
            for entry in index_entries
            if entry.get("artifact_key") == bundle_key and entry.get("discovered_physical_path") == bundle_rel
        ]
        assert bundle_records, f"missing bundle index record for {bundle_rel}"
        bundle_entry = bundle_records[0]
        assert bundle_entry.get("epic_id") == "HDE-EPIC020"
        assert bundle_entry.get("record_type") == "epic020_bundle"
        assert bundle_entry.get("tokens")
        assert set(bundle_entry["tokens"]).issubset(allowed_tokens)
        assert bundle_entry.get("sha256") == _sha256(bundle_path)
        assert bundle_entry.get("size_bytes") == bundle_path.stat().st_size
        assert bundle_entry.get("produced_at_utc") == produced_at

        manifest_entries = [
            entry
            for entry in index_entries
            if entry.get("artifact_key") == bundle_key and entry.get("discovered_physical_path") == manifest_rel
        ]
        assert manifest_entries, f"missing manifest index record for {manifest_rel}"
        manifest_entry = manifest_entries[0]
        assert manifest_entry.get("record_type") == "epic020_bundle_manifest"
        assert manifest_entry.get("tokens")
        assert set(manifest_entry["tokens"]).issubset(allowed_tokens)
        assert manifest_entry.get("sha256") == _sha256(manifest_path)
        assert manifest_entry.get("size_bytes") == manifest_path.stat().st_size
        assert manifest_entry.get("produced_at_utc") == produced_at

        for target_path in (bundle_rel, manifest_rel):
            mirror_key = (bundle_key, target_path)
            assert mirror_key in mirror_records, f"missing mirror record for {mirror_key}"
            mirror_rec = mirror_records[mirror_key]
            counterpart = bundle_entry if target_path == bundle_rel else manifest_entry
            for field in ["sha256", "size_bytes", "tokens", "epic_id", "record_type", "schema_version"]:
                if field in counterpart:
                    assert mirror_rec.get(field) == counterpart.get(field), f"mirror mismatch for {mirror_key}:{field}"
            assert Path(mirror_rec["discovered_physical_path"]).exists()
            assert mirror_rec.get("proof_anchor")
            assert mirror_rec.get("produced_at_utc")
