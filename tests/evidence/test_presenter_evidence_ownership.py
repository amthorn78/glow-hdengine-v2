import hashlib
import inspect
import json
import os
import subprocess
import sys
from pathlib import Path

import jsonschema

from engine.bodygraph import ingest
from presenter import json_canon_compare
from tools.evidence import generate_db_bridge_parity as bridge_generator

ROOT = Path(__file__).resolve().parents[2]
ENV = {
    **os.environ,
    "SAFE_MODE": "1",
    "ALLOW_NETWORK": "0",
    "LC_ALL": "C",
    "LANG": "C",
    "TZ": "UTC",
}
SHARED = ROOT / "artifacts/presenter/json_canon_compare.log"
DEDICATED = ROOT / "artifacts/presenter/hde_epic038_pr04_db_bridge_compare.json"
SCHEMA = ROOT / "schemas/presenter_db_bridge_compare.v1.json"


def _run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args], cwd=ROOT, env=ENV, check=True, capture_output=True, text=True
    )


def test_presenter_history_is_exact_fixed_point_and_check_is_read_only():
    _run("tools/evidence/generate_presenter_history.py")
    first = SHARED.read_bytes()
    assert len(first) == 1559
    assert hashlib.sha256(first).hexdigest() == "64980228d042249a10ecc89ebddcff00be27aae9c79ba2330a24a28b0c59676c"
    assert len(first.splitlines()) == 4
    _run("tools/evidence/generate_presenter_history.py")
    assert SHARED.read_bytes() == first
    _run("tools/evidence/generate_presenter_history.py", "--check")
    assert SHARED.read_bytes() == first


def test_db_bridge_owns_strict_dedicated_receipt_not_shared_history():
    shared_before = SHARED.read_bytes()
    _run("tools/evidence/generate_db_bridge_parity.py")
    assert SHARED.read_bytes() == shared_before
    payload = json.loads(DEDICATED.read_bytes())
    schema = json.loads(SCHEMA.read_bytes())
    jsonschema.validate(payload, schema)
    assert payload["status"] == "PASS"
    assert payload["direct"]["acquisition_id"] != payload["bridge"]["acquisition_id"]
    assert payload["direct"]["emitted_sha256"] == payload["bridge"]["emitted_sha256"]
    parity_bytes = (ROOT / payload["provider_parity_path"]).read_bytes()
    assert payload["provider_parity_sha256"] == hashlib.sha256(parity_bytes).hexdigest()
    assert payload["predicates"]["unsafe_fields_absent"] is True
    assert payload["negative_receipt"]["divergence_detected"] is True
    assert payload["payload_posture"] == "hashes_and_counts_only_no_case_values"
    _run("tools/evidence/generate_db_bridge_parity.py", "--check")


def test_presenter_receipt_fails_closed_on_unbound_or_unsafe_material():
    parity_bytes = (ROOT / "artifacts/db_bridge/provider_parity.proof.json").read_bytes()
    unbound = bridge_generator._presenter_receipt(
        parity_bytes, expected_parity_bytes=b"different expected artifact bytes"
    )
    assert unbound["status"] == "FAIL"
    assert bridge_generator._receipt_payload_safe({"value": [[1]]}) is False
    assert bridge_generator._receipt_payload_safe({"sql": "SELECT 1"}) is False


def test_no_replay_constants_or_implicit_governed_log_defaults():
    bridge_source = (ROOT / "tools/evidence/generate_db_bridge_parity.py").read_text()
    assert "PRESENTER_BASE_RECORDS" not in bridge_source
    assert "artifacts/presenter/json_canon_compare.log" not in bridge_source
    assert inspect.signature(ingest.ingest_vendor_bodygraph).parameters["canon_log"].default is None
    parsed = json_canon_compare._build_parser().parse_args(["left.json", "right.json"])
    assert parsed.log is None
