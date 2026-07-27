from __future__ import annotations

import json
import subprocess
from pathlib import Path

import pytest

from engine.bodygraph.ingest import CANON_COMPARE_LOG, RETRY_LOG, SUCCESS_LOG
from engine.bodygraph.vendor_client import VendorError
from tools.evidence import generate_open_rails_abba_proof as proof

ROOT = Path(__file__).resolve().parents[2]


def _current_live_payload() -> dict[str, object]:
    payload = json.loads((proof.ROOT / proof.LIVE_ABBA_REL).read_bytes())
    payload["non_production_environment"]["reason"] = proof.CANONICAL_LIVE_VENDOR_REASON
    payload["po_override_note"] = proof.CANONICAL_LIVE_VENDOR_AUTHORITY_NOTE
    payload["authority_scope"] = proof.CANONICAL_LIVE_VENDOR_AUTHORITY_SCOPE
    payload["po_event_receipt_sha256"] = proof.sha(b"historical-test-event-receipt-not-live-authority")
    payload["target_identity"] = {
        "base_sha256": proof.CANONICAL_LIVE_VENDOR_BASE_SHA256,
        "identifier": proof.CANONICAL_LIVE_VENDOR_TARGET_ID,
    }
    return payload


def _current_live_bytes() -> bytes:
    return proof.canonical_json_bytes(_current_live_payload())


def _configure_authorized_live_env(monkeypatch: pytest.MonkeyPatch) -> None:
    for key in (*proof.SENSITIVE_ENV, *proof.LIVE_INPUT_ENV, "SAFE_MODE", "ALLOW_NETWORK", "APP_ENV", "QA08_AUTHORIZATION_CONFIRMATION"):
        monkeypatch.delenv(key, raising=False)
    for key, value in {
        "SAFE_MODE": "0",
        "ALLOW_NETWORK": "1",
        "APP_ENV": "dev",
        "LC_ALL": "C",
        "LANG": "C",
        "TZ": "UTC",
        "HD_API_BASE_URL": proof.CANONICAL_LIVE_VENDOR_BASE,
        "HD_API_KEY": "secret-key",
        "GEO_API_KEY": "geo-key",
        "QA08_AUTHORIZATION_CONFIRMATION": "CONFIRMED",
        proof.PO_EVENT_RECEIPT_ENV: "test-event-receipt-0000000000000001",
    }.items():
        monkeypatch.setenv(key, value)


def test_live_readiness_accepts_only_fresh_authorized_exact_target(monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]) -> None:
    _configure_authorized_live_env(monkeypatch)
    assert proof.live_generation_ready() is True
    assert proof.main(["--live-readiness-check"]) == 0
    captured = capsys.readouterr()
    assert captured.out == "OPEN_RAILS_READY\n" and captured.err == ""


@pytest.mark.parametrize(
    "key,value",
    [
        ("SAFE_MODE", "1"),
        ("ALLOW_NETWORK", "0"),
        ("APP_ENV", "production"),
        ("LC_ALL", "en_US.UTF-8"),
        ("LANG", "en_US.UTF-8"),
        ("TZ", "Europe/Amsterdam"),
        ("QA08_AUTHORIZATION_CONFIRMATION", ""),
        (proof.PO_EVENT_RECEIPT_ENV, "too-short"),
        ("HD_API_BASE_URL", "https://sandbox.vendor.test/v2"),
        ("HD_API_KEY", ""),
        ("GEO_API_KEY", ""),
        ("OPEN_RAILS_VENDOR_ABBA_A_USER_ID", "personal-input"),
    ],
)
def test_live_readiness_rejects_any_missing_or_widened_authority(
    monkeypatch: pytest.MonkeyPatch,
    key: str,
    value: str,
) -> None:
    _configure_authorized_live_env(monkeypatch)
    monkeypatch.setenv(key, value)
    assert proof.live_generation_ready() is False


def test_live_readiness_rejects_alias_when_canonical_is_present(monkeypatch: pytest.MonkeyPatch) -> None:
    _configure_authorized_live_env(monkeypatch)
    monkeypatch.setenv("HDAPI_BASE_URL", proof.CANONICAL_LIVE_VENDOR_BASE)
    assert proof.live_generation_ready() is False


def test_live_readiness_allows_exact_alias_only_when_canonical_is_absent(monkeypatch: pytest.MonkeyPatch) -> None:
    _configure_authorized_live_env(monkeypatch)
    monkeypatch.delenv("HD_API_BASE_URL")
    monkeypatch.setenv("HDAPI_BASE_URL", proof.CANONICAL_LIVE_VENDOR_BASE)
    assert proof.live_generation_ready() is True


def test_live_generation_rejects_reused_event_receipt(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    _configure_authorized_live_env(monkeypatch)
    payload = _current_live_payload()
    payload["po_event_receipt_sha256"] = proof._po_event_receipt_sha256()
    path = tmp_path / proof.LIVE_ABBA_REL
    path.parent.mkdir(parents=True)
    path.write_bytes(proof.canonical_json_bytes(payload))
    monkeypatch.setattr(proof, "ROOT", tmp_path)
    assert proof.live_generation_ready() is False
    with pytest.raises(SystemExit, match="LIVE_GENERATION_AUTHORITY_REUSED"):
        proof._require_unused_po_event()


def test_live_write_refuses_before_proof_construction_without_fresh_authorization(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _configure_authorized_live_env(monkeypatch)
    monkeypatch.delenv("QA08_AUTHORIZATION_CONFIRMATION")
    monkeypatch.setattr(
        proof,
        "build_live_proof",
        lambda: (_ for _ in ()).throw(AssertionError("proof construction reached")),
    )
    with pytest.raises(SystemExit, match="LIVE_GENERATION_REFUSED"):
        proof.generate_live(check=False)


@pytest.mark.parametrize("mode", ["wrong_target", "personal_input"])
def test_live_builder_refuses_before_client_creation(
    monkeypatch: pytest.MonkeyPatch,
    mode: str,
) -> None:
    _configure_authorized_live_env(monkeypatch)
    if mode == "wrong_target":
        monkeypatch.setenv("HD_API_BASE_URL", "https://sandbox.vendor.test/v2")
        expected = "TARGET_REFUSED"
    else:
        monkeypatch.setenv("OPEN_RAILS_VENDOR_ABBA_A_USER_ID", "personal-input")
        expected = "INPUT_REFUSED"

    def forbidden_client_factory(counter: dict[str, int]):
        raise AssertionError("client creation reached")

    payload = proof.build_live_proof(client_factory=forbidden_client_factory)
    assert payload["typed_result_class"] == expected
    assert payload["requests_attempted"] == 0


def test_bounded_client_refuses_closed_rails_before_client_creation(monkeypatch: pytest.MonkeyPatch) -> None:
    _configure_authorized_live_env(monkeypatch)
    monkeypatch.setenv("SAFE_MODE", "1")
    monkeypatch.setattr(
        proof.HdApiClient,
        "from_env",
        lambda **kwargs: (_ for _ in ()).throw(AssertionError("client creation reached")),
    )
    with pytest.raises(SystemExit, match="LIVE_GENERATION_REFUSED"):
        proof._bounded_live_client({"attempted": 0})


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
    assert data == proof.canon.sercanon(payload)
    assert json.loads(data)["top_level_pass"] is True


def test_canonical_json_bytes_preserves_utf8_unicode() -> None:
    payload = {"title": "PF09.6 — HDE-Build-Checklist-Distillation"}
    data = proof.canonical_json_bytes(payload)
    assert data == proof.canon.sercanon(payload)
    assert "—".encode("utf-8") in data
    assert b"\\u2014" not in data


def _configure_individual_live_fake(monkeypatch: pytest.MonkeyPatch) -> list[str]:
    _configure_authorized_live_env(monkeypatch)
    monkeypatch.setenv("HD_API_BASE_URL", "https://sandbox.vendor.test/v1")
    monkeypatch.setattr(proof, "CANONICAL_LIVE_VENDOR_BASE", "https://sandbox.vendor.test/v1")
    for key in proof.LIVE_INPUT_ENV:
        monkeypatch.delenv(key, raising=False)

    class FakeOutcome:
        def __init__(self, label: str) -> None:
            self.payload = {"person_uid": f"person-{label}", "mechanics": {"type": ("Generator" if label == "a" else "Projector")}}
            self.input_fingerprint = label * 64
            self.payload_sha256 = proof.sha(proof.emitter.emit_public(self.payload))

    class FakeClient:
        def __init__(self, counter: dict[str, int]) -> None:
            self.counter = counter

    calls = []

    def fake_ingest(inputs, **kwargs):
        calls.append(inputs.user_id)
        if len(calls) > 2:
            raise VendorError("PROVIDER_REQUEST_BOUND_EXCEEDED", "too many")
        kwargs["client"].counter["attempted"] += 1
        return FakeOutcome("a" if len(calls) == 1 else "b")

    monkeypatch.setattr(proof, "ingest_vendor_bodygraph", fake_ingest)
    monkeypatch.setattr(proof, "_bounded_live_client", FakeClient)
    return calls


def test_live_harness_individual_mode_request_bound_and_secret_safe(monkeypatch: pytest.MonkeyPatch) -> None:
    calls = _configure_individual_live_fake(monkeypatch)
    reader_calls: list[tuple[dict[str, object], dict[str, object]]] = []

    def tracked_reader(left, right):
        reader_calls.append((dict(left), dict(right)))
        return proof._emit_live_reader_bytes(left, right)

    payload = proof.build_live_proof(reader_emitter=tracked_reader)
    assert len(calls) == 2
    assert len(reader_calls) == 4
    assert payload["top_level_pass"] is True
    assert payload["requests_attempted"] == 2
    assert payload["requests_completed"] == 2
    assert payload["optional_env_inputs_absent"] == sorted(proof.LIVE_INPUT_ENV)
    assert payload["same_normalized_inputs_reused_for_ab_ba"] is True
    assert payload["predicates"]["distinct_input_fingerprints"] is True
    assert payload["predicates"]["distinct_normalized_payloads"] is True
    assert payload["predicates"]["normalized_payload_hashes_bound"] is True
    with pytest.raises(SystemExit, match="INVALID_LIVE_PROOF"):
        proof._require_passing_live_proof(dict(payload))
    assert payload["predicates"]["two_run_ab_identity"] is True
    assert payload["predicates"]["two_run_ba_identity"] is True
    encoded = proof.canonical_json_bytes(payload).decode("utf-8")
    assert "secret-key" not in encoded and "geo-key" not in encoded
    assert "Synthetic Alpha" not in encoded and "Synthetic Bravo" not in encoded


@pytest.mark.parametrize(
    "drift_call,predicate,first_hash,run2_hash",
    [
        (3, "two_run_ab_identity", "ab_sha256", "ab_run2_sha256"),
        (4, "two_run_ba_identity", "ba_sha256", "ba_run2_sha256"),
    ],
)
def test_live_harness_rejects_second_reader_emission_drift(
    monkeypatch: pytest.MonkeyPatch,
    drift_call: int,
    predicate: str,
    first_hash: str,
    run2_hash: str,
) -> None:
    _configure_individual_live_fake(monkeypatch)
    reader_call_count = 0

    def drifting_reader(left, right):
        nonlocal reader_call_count
        reader_call_count += 1
        data = proof._emit_live_reader_bytes(left, right)
        if reader_call_count == drift_call:
            payload = json.loads(data)
            payload["run2_drift_probe"] = True
            return proof.canonical_json_bytes(payload)
        return data

    payload = proof.build_live_proof(reader_emitter=drifting_reader)

    assert reader_call_count == 4
    assert payload["top_level_pass"] is False
    assert payload["typed_result_class"] == "FAIL"
    assert payload["result"] == "fail"
    assert payload["predicates"][predicate] is False
    assert payload["reader_hashes"][first_hash] != payload["reader_hashes"][run2_hash]


@pytest.mark.parametrize("duplicate", ["fingerprint", "payload"])
def test_live_harness_rejects_duplicate_acquisitions(monkeypatch: pytest.MonkeyPatch, duplicate: str) -> None:
    _configure_authorized_live_env(monkeypatch)
    monkeypatch.setenv("HD_API_BASE_URL", "https://sandbox.vendor.test/v1")
    monkeypatch.setattr(proof, "CANONICAL_LIVE_VENDOR_BASE", "https://sandbox.vendor.test/v1")
    for key in proof.LIVE_INPUT_ENV:
        monkeypatch.delenv(key, raising=False)


    class FakeOutcome:
        def __init__(self, label: str) -> None:
            payload_label = "a" if duplicate == "payload" else label
            self.payload = {
                "person_uid": f"person-{payload_label}",
                "mechanics": {"type": "Generator" if payload_label == "a" else "Projector"},
            }
            self.input_fingerprint = "same-input" if duplicate == "fingerprint" else label * 64
            self.payload_sha256 = proof.sha(proof.emitter.emit_public(self.payload))

    class FakeClient:
        def __init__(self, counter: dict[str, int]) -> None:
            self.counter = counter

    calls = []

    def fake_ingest(inputs, **kwargs):
        calls.append(inputs.user_id)
        kwargs["client"].counter["attempted"] += 1
        return FakeOutcome("a" if len(calls) == 1 else "b")

    monkeypatch.setattr(proof, "ingest_vendor_bodygraph", fake_ingest)
    monkeypatch.setattr(proof, "_bounded_live_client", FakeClient)

    payload = proof.build_live_proof()

    assert payload["top_level_pass"] is False
    assert payload["typed_result_class"] == "FAIL"
    assert payload["result"] == "fail"
    assert payload["requests_attempted"] == 2
    assert payload["requests_completed"] == 2
    predicate = "distinct_input_fingerprints" if duplicate == "fingerprint" else "distinct_normalized_payloads"
    assert payload["predicates"][predicate] is False


def test_live_harness_missing_config_is_inconclusive(monkeypatch: pytest.MonkeyPatch) -> None:
    for key in list(proof.SENSITIVE_ENV) + ["OPEN_RAILS_VENDOR_ABBA_A_USER_ID"]:
        monkeypatch.delenv(key, raising=False)
    payload = proof.build_live_proof()
    assert payload["top_level_pass"] is False
    assert payload["result"] == "inconclusive"
    assert payload["requests_attempted"] == 0


def test_live_harness_v2_chart_success_uses_two_requests_and_local_abba(monkeypatch: pytest.MonkeyPatch) -> None:
    _configure_authorized_live_env(monkeypatch)
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
        route = "vendor.hdapi.post:/charts"

        def __init__(self, fingerprint: str) -> None:
            self.input_fingerprint = fingerprint

    class FakeResult:
        payload = {"data": {}}

    class FakeClient:
        def __init__(self, counter: dict[str, int]) -> None:
            self.counter = counter

        def build_contract_route_request(self, **kwargs):
            label = "a" if self.counter["attempted"] == 0 else "b"
            return FakeRequest(label * 64)

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
    assert payload["predicates"]["distinct_input_fingerprints"] is True
    assert payload["predicates"]["distinct_normalized_payloads"] is True
    assert payload["predicates"]["normalized_payload_hashes_bound"] is True
    assert payload["predicates"]["two_run_ab_identity"] is True
    assert payload["predicates"]["two_run_ba_identity"] is True


def test_legacy_live_harness_isolates_ingest_logs(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    _configure_authorized_live_env(monkeypatch)
    monkeypatch.setenv("HD_API_BASE_URL", "https://sandbox.vendor.test/v1")
    monkeypatch.setattr(proof, "CANONICAL_LIVE_VENDOR_BASE", "https://sandbox.vendor.test/v1")
    for key in proof.LIVE_INPUT_ENV:
        monkeypatch.delenv(key, raising=False)

    class FakeRequest:
        def __init__(self, fingerprint: str) -> None:
            self.input_fingerprint = fingerprint

    class FakeResult:
        def __init__(self, payload: dict[str, object]) -> None:
            self.payload = payload

    class FakeClient:
        def __init__(self, counter: dict[str, int]) -> None:
            self.counter = counter

        def build_request(self, *, birthdate: str, birthtime: str, location: str) -> FakeRequest:
            label = "a" if birthdate == proof.LIVE_SYNTHETIC_A.birthdate else "b"
            return FakeRequest(label * 64)

        def fetch(self, request: FakeRequest) -> FakeResult:
            if self.counter["attempted"] >= 2:
                raise VendorError("PROVIDER_REQUEST_BOUND_EXCEEDED", "too many")
            self.counter["attempted"] += 1
            label = "a" if request.input_fingerprint.startswith("a") else "b"
            return FakeResult(
                {
                    "person_uid": f"person-{label}",
                    "mechanics": {"type": "Generator" if label == "a" else "Projector"},
                }
            )

    governed_logs = tuple(proof.ROOT / path for path in (RETRY_LOG, SUCCESS_LOG, CANON_COMPARE_LOG))
    before = {path: path.read_bytes() if path.exists() else None for path in governed_logs}
    real_temporary_directory = proof.tempfile.TemporaryDirectory
    created: list[Path] = []

    class TrackingTemporaryDirectory:
        def __init__(self, *args, **kwargs) -> None:
            kwargs["dir"] = tmp_path
            self._delegate = real_temporary_directory(*args, **kwargs)

        def __enter__(self) -> str:
            path = self._delegate.__enter__()
            created.append(Path(path))
            return path

        def __exit__(self, exc_type, exc_value, traceback) -> bool | None:
            return self._delegate.__exit__(exc_type, exc_value, traceback)

    monkeypatch.setattr(proof.tempfile, "TemporaryDirectory", TrackingTemporaryDirectory)
    payload = proof.build_live_proof(client_factory=lambda counter: FakeClient(counter))

    after = {path: path.read_bytes() if path.exists() else None for path in governed_logs}
    assert payload["top_level_pass"] is True
    assert payload["requests_attempted"] == 2
    assert payload["requests_completed"] == 2
    assert before == after
    assert len(created) == 2
    assert all(not path.exists() for path in created)


def test_live_check_mode_does_not_reexecute_vendor(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    path = tmp_path / proof.LIVE_ABBA_REL
    path.parent.mkdir(parents=True)
    path.write_bytes(_current_live_bytes())
    monkeypatch.setattr(proof, "ROOT", tmp_path)
    for key in (*proof.SENSITIVE_ENV, "SAFE_MODE", "ALLOW_NETWORK", "APP_ENV", "QA08_AUTHORIZATION_CONFIRMATION"):
        monkeypatch.delenv(key, raising=False)
    monkeypatch.setattr(proof, "build_live_proof", lambda: (_ for _ in ()).throw(AssertionError("live check reexecuted")))
    payload = proof.generate_live(check=True)
    assert payload["artifact_kind"] == "hde_epic038_pr03_open_rails_vendor_abba_proof"


def test_live_check_mode_rejects_failed_or_inconclusive_artifact(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    original = _current_live_bytes()
    failed = json.loads(original)
    failed["top_level_pass"] = False
    failed["result"] = "inconclusive"
    failed["typed_result_class"] = "MISSING_CREDENTIALS"
    failed["requests_attempted"] = 0
    failed["requests_completed"] = 0
    failed["same_normalized_inputs_reused_for_ab_ba"] = False
    failed["predicates"]["request_bound_ok"] = False
    path = tmp_path / proof.LIVE_ABBA_REL
    path.parent.mkdir(parents=True)
    path.write_bytes(proof.canonical_json_bytes(failed))
    monkeypatch.setattr(proof, "ROOT", tmp_path)
    with pytest.raises(SystemExit, match="INVALID_LIVE_PROOF|FAILED_LIVE_PROOF"):
        proof.generate_live(check=True)
    assert path.read_bytes() == proof.canonical_json_bytes(failed)


def test_live_check_mode_rejects_ascii_escaped_unicode(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    original = _current_live_bytes()
    payload = json.loads(original)
    escaped = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8") + b"\n"
    assert b"\\u2014" in escaped
    assert escaped != proof.canonical_json_bytes(payload)
    path = tmp_path / proof.LIVE_ABBA_REL
    path.parent.mkdir(parents=True)
    path.write_bytes(escaped)
    monkeypatch.setattr(proof, "ROOT", tmp_path)

    with pytest.raises(SystemExit, match="NONCANONICAL"):
        proof.generate_live(check=True)

    assert path.read_bytes() == escaped


@pytest.mark.parametrize(
    "mutation",
    [
        "missing_predicate",
        "duplicate_fingerprint",
        "duplicate_payload",
        "invalid_party_shape",
        "unbound_payload_hash",
        "missing_run2_predicate",
        "run2_mismatch",
        "invalid_run2_hash",
    ],
)
def test_live_check_mode_recomputes_distinctness(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    mutation: str,
) -> None:
    original = _current_live_bytes()
    payload = json.loads(original)
    if mutation == "missing_predicate":
        payload["predicates"].pop("distinct_normalized_payloads")
    elif mutation == "duplicate_fingerprint":
        payload["request_results"][1]["input_fingerprint_sha256"] = payload["request_results"][0]["input_fingerprint_sha256"]
    elif mutation == "duplicate_payload":
        duplicate_hash = payload["request_results"][0]["normalized_payload_sha256"]
        payload["request_results"][1]["normalized_payload_sha256"] = duplicate_hash
        payload["normalized_b_sha256"] = duplicate_hash
    elif mutation == "invalid_party_shape":
        payload["request_results"][1]["party"] = []
    elif mutation == "unbound_payload_hash":
        payload["normalized_b_sha256"] = "f" * 64
    elif mutation == "missing_run2_predicate":
        payload["predicates"].pop("two_run_ab_identity")
    elif mutation == "run2_mismatch":
        payload["reader_hashes"]["ab_run2_sha256"] = "f" * 64
    else:
        payload["reader_hashes"]["ba_run2_sha256"] = "not-a-sha256"

    path = tmp_path / proof.LIVE_ABBA_REL
    path.parent.mkdir(parents=True)
    path.write_bytes(proof.canonical_json_bytes(payload))
    monkeypatch.setattr(proof, "ROOT", tmp_path)

    with pytest.raises(SystemExit, match="FAILED_LIVE_PROOF|INVALID_LIVE_PROOF"):
        proof.generate_live(check=True)

    assert path.read_bytes() == proof.canonical_json_bytes(payload)


@pytest.mark.parametrize(
    "typed_result,result,attempted,completed,predicate",
    [
        ("CONFIGURATION_INCOMPLETE", "inconclusive", 0, 0, "request_bound_ok"),
        ("ACQUISITION_INCOMPLETE", "inconclusive", 1, 0, "request_bound_ok"),
        ("FAIL", "fail", 2, 2, "abba_byte_identity"),
    ],
)
def test_live_write_mode_rejects_nonpassing_proof_without_overwrite(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    typed_result: str,
    result: str,
    attempted: int,
    completed: int,
    predicate: str,
) -> None:
    _configure_authorized_live_env(monkeypatch)
    original = _current_live_bytes()
    failed = json.loads(original)
    failed.update(
        {
            "top_level_pass": False,
            "result": result,
            "typed_result_class": typed_result,
            "requests_attempted": attempted,
            "requests_completed": completed,
            "same_normalized_inputs_reused_for_ab_ba": False,
        }
    )
    failed["predicates"][predicate] = False
    failed["po_event_receipt_sha256"] = proof._po_event_receipt_sha256()
    path = tmp_path / proof.LIVE_ABBA_REL
    path.parent.mkdir(parents=True)
    path.write_bytes(original)
    monkeypatch.setattr(proof, "ROOT", tmp_path)
    monkeypatch.setattr(proof, "build_live_proof", lambda: failed)

    with pytest.raises(SystemExit, match="INVALID_LIVE_PROOF|FAILED_LIVE_PROOF"):
        proof.main(["--live"])

    assert path.read_bytes() == original


def test_live_write_mode_accepts_passing_proof(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    _configure_authorized_live_env(monkeypatch)
    original = _current_live_bytes()
    passing = json.loads(original)
    passing["po_event_receipt_sha256"] = proof._po_event_receipt_sha256()
    path = tmp_path / proof.LIVE_ABBA_REL
    monkeypatch.setattr(proof, "ROOT", tmp_path)
    monkeypatch.setattr(proof, "build_live_proof", lambda: passing)

    payload = proof.generate_live(check=False)

    assert payload == passing
    assert path.read_bytes() == proof.canonical_json_bytes(passing)


def _write_live_check_payload(monkeypatch: pytest.MonkeyPatch, tmp_path: Path, payload: dict[str, object]) -> Path:
    path = tmp_path / proof.LIVE_ABBA_REL
    path.parent.mkdir(parents=True)
    path.write_bytes(proof.canonical_json_bytes(payload))
    monkeypatch.setattr(proof, "ROOT", tmp_path)
    return path


def test_live_check_mode_derives_abba_identity_from_first_run_hashes(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    payload = _current_live_payload()
    different_valid_sha = "f" * 64
    assert different_valid_sha != payload["reader_hashes"]["ab_sha256"]
    payload["reader_hashes"]["ba_sha256"] = different_valid_sha
    payload["reader_hashes"]["ba_run2_sha256"] = different_valid_sha
    payload["predicates"]["abba_byte_identity"] = True
    payload["predicates"]["two_run_ba_identity"] = True
    path = _write_live_check_payload(monkeypatch, tmp_path, payload)

    with pytest.raises(SystemExit, match="FAILED_LIVE_PROOF"):
        proof.generate_live(check=True)

    assert path.read_bytes() == proof.canonical_json_bytes(payload)


@pytest.mark.parametrize(
    "mutation,expected",
    [
        ("target_identity_drift", "INVALID_LIVE_PROOF"),
        ("event_receipt_drift", "INVALID_LIVE_PROOF"),
        ("authority_scope_drift", "UNSAFE_LIVE_PROOF"),
        ("generated_at_drift", "INVALID_LIVE_PROOF"),
        ("unknown_key", "INVALID_LIVE_PROOF"),
        ("raw_vendor_payload", "INVALID_LIVE_PROOF|UNSAFE_LIVE_PROOF"),
        ("raw_request", "INVALID_LIVE_PROOF|UNSAFE_LIVE_PROOF"),
        ("raw_response", "INVALID_LIVE_PROOF|UNSAFE_LIVE_PROOF"),
        ("authorization", "INVALID_LIVE_PROOF|UNSAFE_LIVE_PROOF"),
        ("credential", "INVALID_LIVE_PROOF|UNSAFE_LIVE_PROOF"),
        ("birth", "INVALID_LIVE_PROOF|UNSAFE_LIVE_PROOF"),
        ("location", "INVALID_LIVE_PROOF|UNSAFE_LIVE_PROOF"),
        ("unredacted_url", "UNSAFE_LIVE_PROOF"),
        ("missing_po_override", "UNSAFE_LIVE_PROOF"),
        ("inconsistent_safety_boolean", "UNSAFE_LIVE_PROOF"),
        ("secret_value_under_allowed_key", "INVALID_LIVE_PROOF|UNSAFE_LIVE_PROOF"),
    ],
)
def test_live_check_mode_rejects_closed_shape_and_safety_drift(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
    mutation: str,
    expected: str,
) -> None:
    payload = _current_live_payload()
    if mutation == "target_identity_drift":
        payload["target_identity"]["base_sha256"] = "f" * 64
    elif mutation == "event_receipt_drift":
        payload["po_event_receipt_sha256"] = "not-a-sha256"
    elif mutation == "authority_scope_drift":
        payload["authority_scope"] = "recurring"
    elif mutation == "generated_at_drift":
        payload["generated_at_utc"] = "2026-07-27"
    elif mutation == "unknown_key":
        payload["unexpected"] = True
    elif mutation == "raw_vendor_payload":
        payload["raw_vendor_payload"] = {"data": True}
    elif mutation == "raw_request":
        payload["request_results"][0]["raw_request"] = {}
    elif mutation == "raw_response":
        payload["request_results"][0]["raw_response"] = {}
    elif mutation == "authorization":
        payload["route_policy"]["authorization"] = "Bearer secret"
    elif mutation == "credential":
        payload["secret_presence"]["credential"] = "secret"
    elif mutation == "birth":
        payload["request_results"][0]["birthdate"] = "1990-01-01"
    elif mutation == "location":
        payload["request_results"][0]["location"] = "Amsterdam, NL"
    elif mutation == "unredacted_url":
        payload["non_production_environment"]["configured_base_url"] = "https://sandbox.vendor.test/v2"
    elif mutation == "missing_po_override":
        payload.pop("po_override_note")
    elif mutation == "inconsistent_safety_boolean":
        payload["no_secret_value_predicate"] = False
    else:
        payload["synthetic_input_names"]["a"] = "Bearer secret-key"

    path = _write_live_check_payload(monkeypatch, tmp_path, payload)

    with pytest.raises(SystemExit, match=expected):
        proof.generate_live(check=True)

    assert path.read_bytes() == proof.canonical_json_bytes(payload)
