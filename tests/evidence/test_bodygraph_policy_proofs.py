from __future__ import annotations

import hashlib
import json
import os
import subprocess
from pathlib import Path

import jsonschema
import pytest

from engine.serializer import canon
from tools.evidence import generate_bodygraph_policy_proofs as generator


ROOT = Path(__file__).resolve().parents[2]
ENV = {
    **os.environ,
    "ALLOW_NETWORK": "0",
    "LANG": "C",
    "LC_ALL": "C",
    "SAFE_MODE": "1",
    "TZ": "UTC",
}
PATHS = [
    "artifacts/bodygraph/source_selection.snapshot.json",
    "artifacts/bodygraph/source_invariance/ab.json",
    "artifacts/bodygraph/source_invariance/ba.json",
    "artifacts/bodygraph/source_invariance/summary.json",
    "schemas/bodygraph_source_invariance.run.v2.json",
    "schemas/bodygraph_source_invariance.summary.v2.json",
    "artifacts/bodygraph/refresh_policy.snapshot.json",
    "artifacts/bodygraph/metrics.snapshot.json",
    "artifacts/bodygraph/keys_only.logs.sample",
]


def run(args):
    return subprocess.run(
        ["python", *args],
        cwd=ROOT,
        env=ENV,
        check=True,
        capture_output=True,
        text=True,
    )


def _sha(path):
    return hashlib.sha256((ROOT / path).read_bytes()).hexdigest()


def test_bodygraph_policy_v2_is_deterministic_and_closed_rails():
    run(["tools/evidence/generate_bodygraph_policy_proofs.py"])
    first = {path: _sha(path) for path in PATHS}
    run(["tools/evidence/generate_bodygraph_policy_proofs.py"])
    assert {path: _sha(path) for path in PATHS} == first
    run(["tools/evidence/generate_bodygraph_policy_proofs.py", "--check"])
    assert {path: _sha(path) for path in PATHS} == first

    for path in PATHS:
        raw = (ROOT / path).read_bytes()
        assert raw == canon.sercanon(json.loads(raw), sort_keys=True)

    selection = json.loads((ROOT / PATHS[0]).read_text())
    vendor = [row for row in selection["scenarios"] if row["requested_source"] == "vendor"][0]
    assert vendor["transport_calls"] == 0
    assert vendor["reason"] == "PROVIDER_REFUSED"

    ab = json.loads((ROOT / PATHS[1]).read_text())
    ba = json.loads((ROOT / PATHS[2]).read_text())
    summary = json.loads((ROOT / PATHS[3]).read_text())
    run_schema = json.loads((ROOT / PATHS[4]).read_text())
    summary_schema = json.loads((ROOT / PATHS[5]).read_text())
    jsonschema.validate(ab, run_schema)
    jsonschema.validate(ba, run_schema)
    jsonschema.validate(summary, summary_schema)

    assert ab["schema"] == ba["schema"] == "bodygraph.source_invariance.run.v2"
    assert ab["source_order"] == ["db", "vendor"]
    assert ba["source_order"] == ["vendor", "db"]
    assert ab["status"] == ba["status"] == "PASS"
    for record in (ab, ba):
        assert all(record["predicates"].values())
        assert {row["source"] for row in record["acquisitions"]} == {"db", "vendor"}
        for row in record["acquisitions"]:
            assert len({run["acquisition_id"] for run in row["runs"]}) == 2
            assert len({run["projection_sha256"] for run in row["runs"]}) == 1
            assert len({run["emitted_sha256"] for run in row["runs"]}) == 1
        by_source = {row["source"]: row for row in record["acquisitions"]}
        assert (
            by_source["db"]["source_representation_sha256"]
            != by_source["vendor"]["source_representation_sha256"]
        )

    assert summary["schema"] == "bodygraph.source_invariance.summary.v2"
    assert summary["top_level_pass"] is True
    assert all(summary["predicates"].values())
    receipt = dict(summary["negative_receipt"])
    receipt_sha = receipt.pop("receipt_sha256")
    assert receipt_sha == hashlib.sha256(canon.sercanon(receipt)).hexdigest()
    assert summary["negative_receipt"]["divergence_detected"] is True
    assert (
        summary["negative_receipt"]["observed_failure_code"]
        == "BODYGRAPH_SOURCE_DIVERGENCE"
    )
    assert summary["proof_labels"] == [
        {"name": "BG_SOURCE_INVARIANCE_OK", "type": "non_token"}
    ]

    policy = json.loads((ROOT / PATHS[6]).read_text())
    metrics = json.loads((ROOT / PATHS[7]).read_text())
    counts = policy["sample_counts"]
    assert metrics["counters"] == {
        "breaker_tripped_total": counts["breaker_tripped"],
        "rate_limit_hit_total": counts["rate_limit_hits"],
        "refresh_attempts_total": counts["refresh_attempts"],
        "refresh_failure_total": counts["refresh_failures"],
        "refresh_success_total": counts["refresh_successes"],
    }


def test_source_invariance_rejects_reused_or_mutated_evidence(tmp_path, monkeypatch):
    isolated = {key: tmp_path / path.name for key, path in generator.PATHS.items()}
    monkeypatch.setattr(generator, "PATHS", isolated)
    generator.generate(check=False)
    summary_path = isolated["sum"]
    payload = json.loads(summary_path.read_bytes())
    payload["top_level_pass"] = False
    summary_path.write_bytes(canon.sercanon(payload))
    with pytest.raises(SystemExit, match="STALE:"):
        generator.generate(check=True)
