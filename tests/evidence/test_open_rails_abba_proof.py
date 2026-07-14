from __future__ import annotations

import json
import subprocess
from pathlib import Path

import pytest

from tools.evidence import generate_open_rails_abba_proof as proof
from engine.bodygraph.vendor_client import VendorError

ROOT = Path(__file__).resolve().parents[2]


def test_fixture_backed_open_rails_abba_positive_matrix() -> None:
    payload = proof.build_fixture_proof(canon_gate_result={"command": "fixture", "passed": True})
    assert payload["top_level_pass"] is True
    assert payload["transport_call_count"] == 0
    assert payload["acceptance_token_satisfied"] is False
    assert payload["abba_contract_mode"] == "raw_byte_identity_after_existing_canonical_pair_normalization"
    assert all(payload["predicates"].values())


@pytest.mark.parametrize(
    "override_key,mutator,predicate",
    [
        ("ba_reader_open", lambda b: b.replace(b'"idempotence_hash"', b'"idempotence_hash_mutated"', 1), "abba_byte_identity"),
        ("ab_cli_open", lambda b: b.replace(b'"idempotence_hash"', b'"idempotence_hash_mutated"', 1), "reader_cli_ab_identity"),
        ("ab_run2", lambda b: b.replace(b'"idempotence_hash"', b'"idempotence_hash_mutated"', 1), "two_run_ab_identity"),
        ("ab_closed", lambda b: b.replace(b'"idempotence_hash"', b'"idempotence_hash_mutated"', 1), "open_closed_ab_identity"),
        ("ab_reader_open", lambda b: b[:-1], "single_lf_all"),
        ("ab_reader_open", lambda b: b + b"\n", "single_lf_all"),
        ("ab_reader_open", lambda b: b.replace(b"\n", b"\r\n"), "single_lf_all"),
        ("ab_reader_open", lambda b: b.replace(b'"idempotence_hash":', b'"zz":0,"idempotence_hash":', 1), "preimage_ab_match"),
    ],
)
def test_fixture_backed_open_rails_negative_matrix(override_key: str, mutator, predicate: str) -> None:
    baseline = proof.build_fixture_proof(canon_gate_result={"command": "fixture", "passed": True})
    # Rebuild the original compared bytes by using hashes indirectly is not enough; call helpers for exact target.
    originals = {
        "ab_reader_open": proof.reader_bytes(proof.A_FIXTURE, proof.B_FIXTURE),
        "ba_reader_open": proof.reader_bytes(proof.B_FIXTURE, proof.A_FIXTURE),
        "ab_cli_open": proof.cli_reader_bytes(proof.A_FIXTURE, proof.B_FIXTURE, rails=proof.RAILS_OPEN),
        "ab_run2": proof.reader_bytes(proof.A_FIXTURE, proof.B_FIXTURE),
        "ab_closed": proof.cli_reader_bytes(proof.A_FIXTURE, proof.B_FIXTURE, rails=proof.RAILS_CLOSED),
    }
    payload = proof.build_fixture_proof(
        canon_gate_result={"command": "fixture", "passed": True},
        overrides={override_key: mutator(originals[override_key])},
    )
    assert baseline["top_level_pass"] is True
    assert payload["top_level_pass"] is False
    assert payload["predicates"][predicate] is False


def test_canonical_gate_failure_is_negative() -> None:
    payload = proof.build_fixture_proof(canon_gate_result={"command": "fixture", "passed": False})
    assert payload["top_level_pass"] is False
    assert payload["predicates"]["canonical_gate_success"] is False


def test_attempted_fixture_transport_is_negative() -> None:
    def probe() -> None:
        proof.HdApiClient._default_request(None, object(), 1.0)  # type: ignore[arg-type]

    with pytest.raises(AssertionError):
        proof.build_fixture_proof(canon_gate_result={"command": "fixture", "passed": True}, transport_probe=probe)


def test_fixture_producer_check_writes_only_primary(tmp_path: Path) -> None:
    payload = proof.build_fixture_proof(canon_gate_result={"command": "fixture", "passed": True})
    data = proof.canonical_json_bytes(payload)
    assert data.endswith(b"\n") and not data.endswith(b"\n\n") and b"\r" not in data
    assert json.loads(data)["top_level_pass"] is True


def test_live_harness_individual_mode_request_bound_and_secret_safe(monkeypatch: pytest.MonkeyPatch) -> None:
    for key, value in {
        "SAFE_MODE": "0",
        "ALLOW_NETWORK": "1",
        "HD_API_BASE_URL": "https://sandbox.vendor.test/v1",
        "HD_API_KEY": "secret-key",
        "GEO_API_KEY": "geo-key",
        "OPEN_RAILS_VENDOR_ABBA_A_USER_ID": "alpha-user",
        "OPEN_RAILS_VENDOR_ABBA_A_BIRTHDATE": "1990-01-10",
        "OPEN_RAILS_VENDOR_ABBA_A_BIRTHTIME": "14:05",
        "OPEN_RAILS_VENDOR_ABBA_A_LOCATION": "Synthetic Alpha, Test",
        "OPEN_RAILS_VENDOR_ABBA_B_USER_ID": "bravo-user",
        "OPEN_RAILS_VENDOR_ABBA_B_BIRTHDATE": "1992-03-04",
        "OPEN_RAILS_VENDOR_ABBA_B_BIRTHTIME": "08:15",
        "OPEN_RAILS_VENDOR_ABBA_B_LOCATION": "Synthetic Bravo, Test",
    }.items():
        monkeypatch.setenv(key, value)

    class FakeOutcome:
        def __init__(self, label: str) -> None:
            self.payload = {"person_uid": f"person-{label}", "mechanics": {"type": ("Generator" if label == "a" else "Projector")}}
            self.input_fingerprint = label * 64
            self.payload_sha256 = proof.sha(proof.emitter.emit_public(self.payload))

    calls = []

    def fake_ingest(inputs, **kwargs):
        calls.append(inputs.user_id)
        if len(calls) > 2:
            raise VendorError("PROVIDER_REQUEST_BOUND_EXCEEDED", "too many")
        return FakeOutcome("a" if len(calls) == 1 else "b")

    monkeypatch.setattr(proof, "ingest_vendor_bodygraph", fake_ingest)
    monkeypatch.setattr(proof, "_bounded_live_client", lambda counter: object())
    payload = proof.build_live_proof()
    assert len(calls) == 2
    assert payload["requests_completed"] == 2
    assert payload["same_normalized_inputs_reused_for_ab_ba"] is True
    encoded = proof.canonical_json_bytes(payload).decode("utf-8")
    assert "secret-key" not in encoded and "geo-key" not in encoded
    assert "Synthetic Alpha" not in encoded and "Synthetic Bravo" not in encoded


def test_live_harness_missing_config_is_inconclusive(monkeypatch: pytest.MonkeyPatch) -> None:
    for key in list(proof.SENSITIVE_ENV) + ["OPEN_RAILS_VENDOR_ABBA_A_USER_ID"]:
        monkeypatch.delenv(key, raising=False)
    payload = proof.build_live_proof()
    assert payload["top_level_pass"] is False
    assert payload["result"] == "inconclusive"
    assert payload["requests_attempted"] == 0


def test_live_harness_v2_chart_success_uses_two_requests_and_local_abba(monkeypatch: pytest.MonkeyPatch) -> None:
    for key, value in {
        "SAFE_MODE": "0",
        "ALLOW_NETWORK": "1",
        "HD_API_BASE_URL": "https://sandbox.vendor.test/v2",
        "HD_API_KEY": "secret-key",
        "GEO_API_KEY": "geo-key",
    }.items():
        monkeypatch.setenv(key, value)
    for key in [
        "OPEN_RAILS_VENDOR_ABBA_A_USER_ID",
        "OPEN_RAILS_VENDOR_ABBA_A_BIRTHDATE",
        "OPEN_RAILS_VENDOR_ABBA_A_BIRTHTIME",
        "OPEN_RAILS_VENDOR_ABBA_A_LOCATION",
        "OPEN_RAILS_VENDOR_ABBA_B_USER_ID",
        "OPEN_RAILS_VENDOR_ABBA_B_BIRTHDATE",
        "OPEN_RAILS_VENDOR_ABBA_B_BIRTHTIME",
        "OPEN_RAILS_VENDOR_ABBA_B_LOCATION",
    ]:
        monkeypatch.delenv(key, raising=False)

    class FakeRequest:
        input_fingerprint = "a" * 64
        route = "vendor.hdapi.post:/charts"

    class FakeResult:
        payload = {"data": {}}

    class FakeClient:
        def __init__(self, counter: dict[str, int]) -> None:
            self.counter = counter

        def build_contract_route_request(self, **kwargs):
            return FakeRequest()

        def fetch(self, request):
            if self.counter["attempted"] >= 2:
                raise VendorError("PROVIDER_REQUEST_BOUND_EXCEEDED", "too many")
            self.counter["attempted"] += 1
            return FakeResult()

    class FakeAdapter:
        calls = 0

        def as_dict(self):
            FakeAdapter.calls += 1
            label = "a" if FakeAdapter.calls == 1 else "b"
            return {
                "status": "mapped",
                "code": "ADAPTER_MAPPED",
                "resolved": {
                    "person_uid": f"person-{label}",
                    "bodygraph": {"type": "Generator" if label == "a" else "Projector"},
                },
            }

    monkeypatch.setattr(proof, "_bounded_live_client", lambda counter: FakeClient(counter))
    monkeypatch.setattr(proof, "adapt_v2_chart_payload", lambda payload, context: FakeAdapter())

    payload = proof.build_live_proof()
    assert payload["top_level_pass"] is True
    assert payload["typed_result_class"] == "PASS"
    assert payload["requests_attempted"] == 2
    assert payload["requests_completed"] == 2
    assert payload["same_normalized_inputs_reused_for_ab_ba"] is True
    assert payload["predicates"]["request_bound_ok"] is True


def test_live_check_mode_does_not_reexecute_vendor(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(proof, "build_live_proof", lambda: (_ for _ in ()).throw(AssertionError("live check reexecuted")))
    payload = proof.generate_live(check=True)
    assert payload["artifact_kind"] == "hde_epic038_pr03_open_rails_vendor_abba_proof"
