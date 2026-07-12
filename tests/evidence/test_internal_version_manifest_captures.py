from __future__ import annotations

import hashlib
import json
from pathlib import Path

from tools.evidence import update_evidence_index

ARTIFACT_DIR = Path("artifacts/ops/internal_version")
MANIFEST = ARTIFACT_DIR / "request_chain_manifest.json"
CONDITIONAL_STEPS = {
    "conditional_if_none_match",
    "conditional_if_modified_since",
}


def test_manifest_bound_conditional_captures_and_proofs_are_current():
    manifest = json.loads(MANIFEST.read_bytes())
    steps = {
        step["name"]: step
        for step in manifest["steps"]
        if step["name"] in CONDITIONAL_STEPS
    }
    assert set(steps) == CONDITIONAL_STEPS

    for name in sorted(CONDITIONAL_STEPS):
        filename = steps[name]["artifacts"]["headers"]
        capture = ARTIFACT_DIR / filename
        body = capture.read_bytes()

        assert body.startswith(b"HTTP/1.0 200 OK\n")
        assert b"Cache-Control: no-store\n" in body
        assert b"Content-Type: application/json; charset=utf-8\n" in body
        assert b"ETag: <absent>\n" in body
        assert body != (filename + "\n").encode("utf-8")

        proof_path = Path(str(capture) + ".path_proof.txt")
        proof = update_evidence_index._load_existing_proof(proof_path)
        assert proof["path"] == capture.as_posix()
        assert int(proof["size_bytes"]) == len(body)
        assert proof["sha256"] == hashlib.sha256(body).hexdigest()
