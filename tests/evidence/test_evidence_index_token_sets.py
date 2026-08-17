from tools.evidence.update_evidence_index import _normalize_index_entry


def test_tokens_are_deduplicated_and_ascii_sorted():
    entry = _normalize_index_entry(
        {
            "artifact_key": "example",
            "discovered_physical_path": "artifacts/example.txt",
            "tokens": ["UPDATED", "PASSED", "UPDATED"],
        }
    )
    assert entry["tokens"] == ["PASSED", "UPDATED"]
