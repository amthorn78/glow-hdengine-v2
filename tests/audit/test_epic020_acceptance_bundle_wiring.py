from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, List

ACCEPTANCE = Path("docs/acceptance_map_epic020.json")
MANIFEST = Path("audit/EPIC020_MANIFEST.json")
INDEX = Path("docs/evidence/INDEX.json")


def _artifact_items(artifacts: Iterable[object]) -> List[str]:
    paths: List[str] = []
    for entry in artifacts:
        if isinstance(entry, str):
            paths.append(entry)
        elif isinstance(entry, dict) and "discovered_physical_path" in entry:
            paths.append(entry["discovered_physical_path"])
    return paths


def _manifest_artifacts(entry: object) -> Iterable[object]:
    if isinstance(entry, dict):
        return entry.get("artifacts", [])
    return entry


def test_acceptance_and_manifest_follow_index_bundle_records() -> None:
    acceptance = json.loads(ACCEPTANCE.read_text(encoding="utf-8"))
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    index_entries = json.loads(INDEX.read_text(encoding="utf-8"))

    assert acceptance["epic_id"] == "HDE-EPIC020"

    token_status = acceptance["token_status"]
    manifest_artifacts = manifest["token_artifacts"]

    token_bundle_paths: dict[str, set[str]] = {}
    for entry in index_entries:
        if entry.get("epic_id") != "HDE-EPIC020":
            continue
        if entry.get("record_type") not in {"epic020_bundle", "epic020_bundle_manifest"}:
            continue
        for token in entry.get("tokens", []):
            token_bundle_paths.setdefault(token, set()).add(entry["discovered_physical_path"])

    for token, acceptance_entry in token_status.items():
        assert token in manifest_artifacts, f"manifest is missing token {token}"
        manifest_entry = manifest_artifacts[token]

        acceptance_paths = set(_artifact_items(acceptance_entry.get("artifacts", [])))
        manifest_paths = set(_artifact_items(_manifest_artifacts(manifest_entry)))

        expected_paths = token_bundle_paths.get(token, set())
        for path in expected_paths:
            assert path in acceptance_paths, f"{token} missing {path} in acceptance map"
            assert path in manifest_paths, f"{token} missing {path} in manifest"

        if isinstance(manifest_entry, dict):
            for artifact in manifest_entry.get("artifacts", []):
                if isinstance(artifact, dict) and "artifact_key" in artifact:
                    assert artifact["artifact_key"] == token
        else:
            for artifact in manifest_entry:
                if isinstance(artifact, dict) and "artifact_key" in artifact:
                    assert artifact["artifact_key"] == token

