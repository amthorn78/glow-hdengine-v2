from __future__ import annotations

from tools.evidence import run_canonical_json_gate


def test_stale_outputs_detects_missing_and_drift(tmp_path):
    current = tmp_path / "current.log"
    missing = tmp_path / "missing.log"
    current.write_bytes(b"expected\n")
    expected = {
        current: b"expected\n",
        missing: b"expected\n",
    }

    assert run_canonical_json_gate._stale_outputs(expected) == [missing]

    current.write_bytes(b"drifted\n")
    assert run_canonical_json_gate._stale_outputs(expected) == [
        current,
        missing,
    ]
